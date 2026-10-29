"""Shared plumbing for bespoke (one-off design) builders: images, fonts, hours, SEO files, preview + Netlify site + zip."""
import base64, json, re, shutil, datetime, zipfile, html
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
ROOT = Path(__file__).resolve().parent.parent; ENG = ROOT / 'engine'
env = Environment(loader=FileSystemLoader(ENG / 'templates'), autoescape=False)
DAYS = [(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (0, 'Sunday')]
MIME = {'.webp': 'image/webp', '.jpg': 'image/jpeg', '.png': 'image/png', '.woff': 'font/woff', '.svg': 'image/svg+xml'}
def fmt12(t):
    h, m = map(int, t.split(':')); ap = 'PM' if h >= 12 else 'AM'; h = h % 12 or 12
    return f'{h}:{m:02d} {ap}' if m else f'{h} {ap}'
def b64(p): return f'data:{MIME[p.suffix]};base64,' + base64.b64encode(p.read_bytes()).decode()
def slugify(s): return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')
def esc(s): return html.escape(str(s), quote=True)
def week(loc): return [dict(dow=dow, day=day, text=next((f"{fmt12(h['open'])} – {fmt12(h['close'])}" for h in loc['hours'] if dow in h['dow']), 'Closed')) for dow, day in DAYS]
def price_num(s):
    m = re.search(r'\$(\d+(?:\.\d+)?)', s or ''); return float(m.group(1)) if m else None
def build(slug, tpl, css_tpl, js_files, fonts, cuisines, ribbon, extra=None, copy_imgs=()):
    """fonts: [(family, file, weight, style)]; js_files: names in templates/. extra(d, img) -> dict merged into context."""
    cdir = ROOT / 'clients' / slug; d = json.load(open(cdir / 'data.json')); loc = d['locations'][0]
    out = ROOT / 'dist' / slug; site = out / 'site'
    notes = (out / 'LEAD-NOTES.md').read_text() if (out / 'LEAD-NOTES.md').exists() else None
    if out.exists(): shutil.rmtree(out)
    (site / 'assets' / 'img').mkdir(parents=True); (site / 'assets' / 'fonts').mkdir()
    if notes: (out / 'LEAD-NOTES.md').write_text(notes)
    js = '\n'.join((ENG / 'templates' / f).read_text() for f in js_files)
    used = set()
    for P in (True, False):
        def img(rel):
            used.add(rel); return b64(cdir / 'img' / rel) if P else f'assets/img/{rel}'
        faces = ''.join("@font-face{font-family:'%s';src:url(%s) format('woff');font-weight:%s;font-style:%s;font-display:swap}" % (fam, b64(ENG / 'fonts' / f'{fn}.woff') if P else f'fonts/{fn}.woff', w, st) for fam, fn, w, st in fonts)
        css = faces + env.get_template(css_tpl).render()
        ctx = dict(d, loc=loc, preview=P, img=img, week=week(loc), year=datetime.date.today().year, ribbon=ribbon, esc=esc, slugify=slugify,
                   hours_json=json.dumps(loc['hours']), css=css, js=js)
        if extra: ctx.update(extra(d, img))
        if P:
            (out / 'preview.html').write_text(env.get_template(tpl).render(ctx))
        else:
            days = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
            ld = {'@context': 'https://schema.org', '@type': 'Restaurant', 'name': d['name'], 'url': d['domain'] + '/', 'telephone': loc['tel'], 'servesCuisine': cuisines, 'priceRange': '$$',
                  'address': {'@type': 'PostalAddress', 'streetAddress': loc['street'], 'addressLocality': loc['city'], 'addressRegion': loc['region'], 'postalCode': loc['postal'], 'addressCountry': 'US'},
                  'openingHoursSpecification': [{'@type': 'OpeningHoursSpecification', 'dayOfWeek': [days[x] for x in h['dow']], 'opens': h['open'], 'closes': h['close']} for h in loc['hours']],
                  'potentialAction': {'@type': 'OrderAction', 'target': d['order_any']}}
            ctx['jsonld'] = json.dumps(ld).replace('</', '<\\/')
            (site / 'index.html').write_text(env.get_template(tpl).render(ctx))
            (site / 'assets' / 'site.css').write_text(css); (site / 'assets' / 'site.js').write_text(js)
    for fam, fn, w, st in fonts:
        shutil.copy(ENG / 'fonts' / f'{fn}.woff', site / 'assets' / 'fonts')
    for lic in {fn.split('-')[0] for _, fn, _, _ in fonts}:
        p = ENG / 'fonts' / f'{lic}-OFL.txt'
        if p.exists(): shutil.copy(p, site / 'assets' / 'fonts')
    for rel in used: shutil.copy(cdir / 'img' / rel, site / 'assets' / 'img' / rel)
    (site / 'robots.txt').write_text(f"User-agent: *\nAllow: /\nSitemap: {d['domain']}/sitemap.xml\n")
    (site / 'sitemap.xml').write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{d["domain"]}/</loc></url></urlset>\n')
    (site / '404.html').write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Not found | {esc(d["name"])}</title><link rel="stylesheet" href="/assets/site.css"></head><body><main style="padding:12vh 24px;display:grid;gap:18px;justify-items:start;max-width:640px;margin:auto"><h1 style="font-family:inherit">That page is off the menu.</h1><p>Everything is on the home page: menu, hours and online ordering.</p><a class="btn" href="/">Back to {esc(d["short"])}</a></main></body></html>')
    z = out / f'{slug}-netlify-site.zip'
    with zipfile.ZipFile(z, 'w', zipfile.ZIP_DEFLATED) as zf:
        for p in sorted(site.rglob('*')):
            if p.is_file(): zf.write(p, p.relative_to(site))
    print('built', slug, round((out / 'preview.html').stat().st_size / 1e6, 2), 'MB preview;', round(z.stat().st_size / 1e6, 2), 'MB zip')
