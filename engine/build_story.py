"""Builds the scroll-story site for Jimmy's House of Pizza. usage: build_story.py"""
import base64, json, re, shutil, datetime, zipfile
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
ROOT = Path(__file__).resolve().parent.parent; ENG = ROOT / 'engine'
env = Environment(loader=FileSystemLoader(ENG / 'templates'), autoescape=False)
slug = 'jimmys-house-of-pizza'; cdir = ROOT / 'clients' / slug
d = json.load(open(cdir / 'data.json'))
STAGES = [
  dict(step='Dough', text='Fresh dough, stretched by hand on Kelley Street since the day we opened. Scroll and watch your pie come together.'),
  dict(step='Sauce', eyebrow='Step two', title='House sauce', text='Ladled on and spread to the edge. Nothing from a jar.'),
  dict(step='Cheese', eyebrow='Step three', title='Real mozzarella', text='Shredded in the shop and piled on, edge to edge.'),
  dict(step='Toppings', eyebrow='Step four', title='Pile it on', text='Pepperoni, peppers, olives, gyro, meatballs. One item, two, three, or the House Special with everything.'),
  dict(step='Oven', eyebrow='Step five', title='Into the oven', text='Baked hot until the crust browns and the cheese blisters.'),
  dict(step='Slice', eyebrow='Ready', title='Hot slice.<br>Fair price.', text='Large 14-inch cheese is $13.00, tax included. Order online and pay when you pick it up.'),
]
FONTS = [('Boldonse', 'Boldonse-Regular', 400), ('Bricolage Grotesque', 'BricolageGrotesque-Regular', 400), ('Bricolage Grotesque', 'BricolageGrotesque-Bold', 700)]
DAYS = [(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (0, 'Sunday')]
def fmt12(t):
    h, m = map(int, t.split(':')); ap = 'PM' if h >= 12 else 'AM'; h = h % 12 or 12
    return f'{h}:{m:02d} {ap}' if m else f'{h} {ap}'
def b64(p):
    mime = {'.webp': 'image/webp', '.jpg': 'image/jpeg', '.woff': 'font/woff'}[p.suffix]
    return f'data:{mime};base64,' + base64.b64encode(p.read_bytes()).decode()
loc = d['location']
week = [dict(dow=dow, day=day, text=next((f"{fmt12(h['open'])} – {fmt12(h['close'])}" for h in loc['hours'] if dow in h['dow']), 'Closed')) for dow, day in DAYS]
menu = [dict(c, id='m-' + re.sub(r'[^a-z0-9]+', '-', c['cat'].lower()).strip('-')) for c in d['menu']]
site_json = json.dumps({'hours': loc['hours']})
out = ROOT / 'dist' / slug; site = out / 'site'
notes = (out / 'LEAD-NOTES.md').read_text() if (out / 'LEAD-NOTES.md').exists() else None
if out.exists(): shutil.rmtree(out)
(site / 'assets' / 'img').mkdir(parents=True); (site / 'assets' / 'fonts').mkdir()
if notes: (out / 'LEAD-NOTES.md').write_text(notes)
js = (ENG / 'templates' / 'story.js').read_text()
for P in (True, False):
    fonts = [dict(family=f, src=(b64(ENG / 'fonts' / f'{fn}.woff') if P else f'fonts/{fn}.woff'), weight=w) for f, fn, w in FONTS]
    css = env.get_template('story.css.j2').render(fonts=fonts)
    ctx = dict(d, preview=P, stages=STAGES, menu=menu, week=week, year=datetime.date.today().year, site_json=site_json,
               mascot_src=(b64(cdir / 'img' / 'mascot-900.jpg') if P else 'assets/img/mascot-900.jpg'))
    if P:
        (out / 'preview.html').write_text(env.get_template('story.html.j2').render(ctx, css=css, js=js, fragment=False))
        (out / 'artifact.html').write_text(env.get_template('story.html.j2').render(ctx, css=css, js=js, fragment=True))
    else:
        days = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
        ld = {'@context': 'https://schema.org', '@type': 'Restaurant', 'name': d['name'], 'url': d['domain'] + '/', 'telephone': loc['tel'], 'servesCuisine': ['Pizza', 'Italian', 'Greek'], 'priceRange': '$',
              'address': {'@type': 'PostalAddress', 'streetAddress': loc['street'], 'addressLocality': loc['city'], 'addressRegion': loc['region'], 'postalCode': loc['postal'], 'addressCountry': 'US'},
              'openingHoursSpecification': [{'@type': 'OpeningHoursSpecification', 'dayOfWeek': [days[x] for x in h['dow']], 'opens': h['open'], 'closes': h['close']} for h in loc['hours']],
              'potentialAction': {'@type': 'OrderAction', 'target': d['order']}, 'hasMenu': d['domain'] + '/#menu'}
        ctx['jsonld'] = json.dumps(ld).replace('</', '<\\/')
        (site / 'index.html').write_text(env.get_template('story.html.j2').render(ctx, fragment=False))
        (site / 'assets' / 'site.css').write_text(css); (site / 'assets' / 'site.js').write_text(js)
        for f, fn, w in FONTS:
            shutil.copy(ENG / 'fonts' / f'{fn}.woff', site / 'assets' / 'fonts'); lic = ENG / 'fonts' / f"{fn.split('-')[0]}-OFL.txt"; shutil.copy(lic, site / 'assets' / 'fonts' / lic.name)
        for n in ('mascot-900.jpg', 'mascot-face.webp'): shutil.copy(cdir / 'img' / n, site / 'assets' / 'img' / n)
        (site / 'robots.txt').write_text(f"User-agent: *\nAllow: /\nSitemap: {d['domain']}/sitemap.xml\n")
        (site / 'sitemap.xml').write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{d["domain"]}/</loc></url></urlset>\n')
        (site / '404.html').write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Not found | {d["name"]}</title><link rel="stylesheet" href="/assets/site.css"></head><body><main class="sec"><div class="wrap" style="display:grid;gap:20px;justify-items:start"><h1 class="h2">That slice is gone.</h1><p class="lede">The menu, hours and online ordering are all on the home page.</p><a class="btn" href="/">Back to Jimmy\'s</a></div></main></body></html>')
z = out / f'{slug}-netlify-site.zip'
with zipfile.ZipFile(z, 'w', zipfile.ZIP_DEFLATED) as zf:
    for p in sorted(site.rglob('*')):
        if p.is_file(): zf.write(p, p.relative_to(site))
print('built', slug, round((out / 'preview.html').stat().st_size / 1e6, 2), 'MB preview;', round(z.stat().st_size / 1e6, 2), 'MB zip')
