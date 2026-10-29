"""Pizza-lead site builder.
usage: python3 engine/build.py <client-slug>
Builds dist/<slug>/preview.html (single self-contained file with a 'design concept' ribbon)
and dist/<slug>/site/ (Netlify-ready production files) plus a zip of the site."""
import base64, json, re, sys, shutil, datetime, zipfile
from pathlib import Path
from jinja2 import Environment, FileSystemLoader

ROOT = Path(__file__).resolve().parent.parent
ENG = ROOT / 'engine'
env = Environment(loader=FileSystemLoader(ENG / 'templates'), autoescape=False, trim_blocks=False)

STYLES = {
  'ny-street': dict(
    concept='NY street pizzeria after dark: chalk-white signage type, red-and-white deli checker, steam over the tray.',
    layout_note='split hero (copy left, tilted tray photo on checker paper right) → ticker → pinned horizontal favorites → cream "menu paper" band → dark location cards.',
    ink='#110C0A', ink2='#1C1411', ink3='#3A2A22', cream='#FFF4E2', muted='#CDB9A0',
    accent='#E8432A', accent_deep='#B32716', on_accent='#110C0A', gold='#F7B53D', leaf='#6BAA5A',
    paper='#FFF4E2', paper2='#FFFBF3', paper_ink='#1A110D', paper_muted='#6A5243', paper_line='#EAD6BA',
    fonts=[('Big Shoulders', 'BigShoulders-Bold', 700, 'normal'), ('Big Shoulders', 'BigShoulders-Regular', 400, 'normal'),
           ('Work Sans', 'WorkSans-Regular', 400, 'normal'), ('Work Sans', 'WorkSans-Bold', 700, 'normal'), ('Work Sans', 'WorkSans-Italic', 400, 'italic')],
    f_display='"Big Shoulders", Impact, "Arial Narrow Bold", sans-serif', f_body='"Work Sans", system-ui, -apple-system, "Segoe UI", sans-serif',
    f_label='"Big Shoulders", Impact, sans-serif', f_script='"Work Sans", system-ui, sans-serif',
    eyebrow_font='700 1.05rem/1 "Big Shoulders", Impact, sans-serif', display_track='.005em', btn_track='.05em',
    h1_vw='13vw', h1_max='10.5rem', h2_max='5.6rem', logo_h='54px', radius='18px',
    hot_extra='text-shadow:0 0 34px color-mix(in srgb,var(--accent) 50%,transparent)',
    tile_min='230px', tile_ratio='4/5', card_ratio='4/5', pinned_ratio='1/1', hero_pos='50% 50%',
    paper_edge='repeating-conic-gradient(var(--accent) 0 25%,var(--paper) 0 50%) 0 0/14px 14px',
    fx='steam', hero_layout='split', stage_ratio='1440/1577'),
  'roadside': dict(
    concept='Family roadside pizzeria: wood-routed park-sign type, oven embers, the logo\'s tomato, cheese and basil stripe.',
    layout_note='full-bleed oven photo hero with embers → ticker → pinned favorites → ticket-stub combo deals → cream menu band → location card → about with the years.',
    ink='#16110D', ink2='#221913', ink3='#3F3027', cream='#FCF1DE', muted='#CCB9A1',
    accent='#E0552B', accent_deep='#A3321A', on_accent='#1A100A', gold='#F4AE3F', leaf='#6FB062',
    paper='#FCF1DE', paper2='#FFF9EE', paper_ink='#1E1610', paper_muted='#6B5444', paper_line='#E9D4B6',
    fonts=[('National Park', 'NationalPark-Bold', 700, 'normal'), ('National Park', 'NationalPark-Regular', 400, 'normal'),
           ('Outfit', 'Outfit-Regular', 400, 'normal'), ('Outfit', 'Outfit-Bold', 700, 'normal'),
           ('Nothing You Could Do', 'NothingYouCouldDo-Regular', 400, 'normal')],
    f_display='"National Park", "Trebuchet MS", sans-serif', f_body='"Outfit", system-ui, -apple-system, "Segoe UI", sans-serif',
    f_label='"Outfit", system-ui, sans-serif', f_script='"Nothing You Could Do", "Segoe Script", cursive',
    eyebrow_font='600 .95rem/1.2 "Outfit", system-ui, sans-serif', display_track='.01em', btn_track='.03em',
    h1_vw='12vw', h1_max='9rem', h2_max='5rem', logo_h='58px', radius='14px', hot_extra='',
    tile_min='260px', tile_ratio='3/2', card_ratio='4/3', pinned_ratio='4/3', hero_pos='50% 62%',
    paper_edge='linear-gradient(90deg,var(--accent) 0 33.3%,var(--gold) 0 66.6%,var(--leaf) 0)',
    fx='embers', hero_layout='full', stage_ratio='4/3', has_script=True),
  'greek-gold': dict(
    concept='Goffstown pizza-and-market: diner gold and Greek blue, maroon jacket red, the half-and-half oversized pie tilted on a marble counter.',
    layout_note='split hero on a marble counter → ticker → pinned favorites → cream menu band → location card → the Galatas family story with the years count.',
    ink='#14100E', ink2='#1F1916', ink3='#3C322C', cream='#FBF3E3', muted='#CEBFA7',
    accent='#C9302C', accent_deep='#8E1F1C', on_accent='#FBF3E3', gold='#E8B542', leaf='#2F6FB5',
    paper='#FBF3E3', paper2='#FFFBF2', paper_ink='#1C1410', paper_muted='#6A5848', paper_line='#E6D6BC',
    fonts=[('Big Shoulders', 'BigShoulders-Bold', 700, 'normal'), ('Big Shoulders', 'BigShoulders-Regular', 400, 'normal'),
           ('Work Sans', 'WorkSans-Regular', 400, 'normal'), ('Work Sans', 'WorkSans-Bold', 700, 'normal'), ('Work Sans', 'WorkSans-Italic', 400, 'italic')],
    f_display='"Big Shoulders", Impact, "Arial Narrow Bold", sans-serif', f_body='"Work Sans", system-ui, -apple-system, "Segoe UI", sans-serif',
    f_label='"Big Shoulders", Impact, sans-serif', f_script='"Work Sans", system-ui, sans-serif',
    eyebrow_font='700 1.05rem/1 "Big Shoulders", Impact, sans-serif', display_track='.005em', btn_track='.05em',
    h1_vw='13vw', h1_max='10rem', h2_max='5.4rem', logo_h='50px', radius='16px',
    hot_extra='color:var(--gold)', tile_min='230px', tile_ratio='4/5', card_ratio='4/5', pinned_ratio='1/1', hero_pos='50% 50%',
    paper_edge='repeating-linear-gradient(90deg,var(--leaf) 0 28px,var(--paper) 28px 56px)',
    fx='steam', hero_layout='split', stage_ratio='1080/810'),
  'blackout': dict(
    concept='Uncle Joey in black and white: the logo\'s flat shapes, white on black, one real pie photo, red only on the Order button.',
    layout_note='full-bleed pie photo hero with the logo mark → ticker → pinned favorites (type-only cards where no photo exists) → cream menu band → hours card.',
    ink='#0B0B0B', ink2='#161616', ink3='#2E2E2E', cream='#F4F1EC', muted='#B9B4AC',
    accent='#D7261E', accent_deep='#961711', on_accent='#FFFFFF', gold='#F4F1EC', leaf='#6BA368',
    paper='#F4F1EC', paper2='#FFFFFF', paper_ink='#0B0B0B', paper_muted='#5F5A54', paper_line='#DCD6CD',
    fonts=[('Big Shoulders', 'BigShoulders-Bold', 700, 'normal'), ('Big Shoulders', 'BigShoulders-Regular', 400, 'normal'),
           ('Outfit', 'Outfit-Regular', 400, 'normal'), ('Outfit', 'Outfit-Bold', 700, 'normal')],
    f_display='"Big Shoulders", Impact, "Arial Narrow Bold", sans-serif', f_body='"Outfit", system-ui, -apple-system, "Segoe UI", sans-serif',
    f_label='"Outfit", system-ui, sans-serif', f_script='"Outfit", system-ui, sans-serif',
    eyebrow_font='700 .85rem/1.2 "Outfit", system-ui, sans-serif', display_track='.01em', btn_track='.06em',
    h1_vw='12vw', h1_max='9.5rem', h2_max='5.4rem', logo_h='46px', radius='6px', hot_extra='color:var(--accent)',
    tile_min='240px', tile_ratio='4/3', card_ratio='4/5', pinned_ratio='1/1', hero_pos='50% 45%',
    paper_edge='linear-gradient(90deg,var(--paper-ink) 0 100%)',
    fx='steam', hero_layout='full', stage_ratio='4/3'),
}
DAYS = [(1, 'Monday'), (2, 'Tuesday'), (3, 'Wednesday'), (4, 'Thursday'), (5, 'Friday'), (6, 'Saturday'), (0, 'Sunday')]

def fmt12(t):
    h, m = map(int, t.split(':')); ap = 'PM' if 12 <= h < 24 else 'AM'; h = h % 12 or 12
    return f'{h}:{m:02d} {ap}' if m else f'{h} {ap}'

def slugify(s): return re.sub(r'[^a-z0-9]+', '-', s.lower()).strip('-')

def b64(path):
    mime = {'.webp': 'image/webp', '.jpg': 'image/jpeg', '.png': 'image/png', '.woff': 'font/woff'}[path.suffix]
    return f'data:{mime};base64,' + base64.b64encode(path.read_bytes()).decode()

def build(slug):
    cdir = ROOT / 'clients' / slug
    d = json.load(open(cdir / 'data.json'))
    t = dict(STYLES[d['style']]); t.update({k: v for k, v in d.get('theme_overrides', {}).items()})
    imap = json.load(open(cdir / 'img' / '_map.json'))['map']
    out = ROOT / 'dist' / slug; site = out / 'site'
    notes = (out / 'LEAD-NOTES.md').read_text() if (out / 'LEAD-NOTES.md').exists() else None
    if out.exists(): shutil.rmtree(out)
    (site / 'assets' / 'img').mkdir(parents=True); (site / 'assets' / 'fonts').mkdir(parents=True)
    if notes: (out / 'LEAD-NOTES.md').write_text(notes)

    used = set()
    def img_name(key):
        n = imap.get(key)
        if n: used.add(n)
        return n

    results = {}
    for mode in ('preview', 'prod'):
        P = mode == 'preview'
        src = (lambda n: b64(cdir / 'img' / n)) if P else (lambda n: f'assets/img/{n}')
        fonts = [dict(family=f, src=(b64(ENG / 'fonts' / f'{fn}.woff') if P else f'fonts/{fn}.woff'), weight=w, style=s) for f, fn, w, s in t['fonts']]
        locs = []
        for l in d['locations']:
            l = dict(l); week = []
            for dow, day in DAYS:
                r = next((h for h in l['hours'] if dow in h['dow']), None)
                week.append(dict(dow=dow, day=day, text=f"{fmt12(r['open'])} – {fmt12(r['close'])}" if r else ('Call' if l.get('hours_note') else 'Closed')))
            l['week'] = week; locs.append(l)
        menu = []
        for c in d['menu']:
            c = dict(c); c['id'] = 'm-' + slugify(c['cat'])
            tiles, rows = [], []
            for it in c['items']:
                it = dict(it); n = img_name(it['img']) if it.get('img') else None
                if n: it['src'] = src(n); tiles.append(it)
                else: rows.append(it)
            c['tiles'], c['rows'] = tiles, rows
            if c['cat'] in ('Pizza',) and d.get('toppings'): c['toppings'] = [x.strip() for x in d['toppings'].split(',')]
            menu.append(c)
        sigs = []
        for s in d['signatures']:
            s = dict(s); n = img_name(s.get('img')); s['src'] = src(n) if n else None; sigs.append(s)
        promos = []
        for p in d.get('promo_cards', []):
            p = dict(p); n = img_name(p.get('img')); p['src'] = src(n) if n else None
            if p['href'].startswith('@'): p['href'] = d['links'][p['href'][1:]]
            p.setdefault('eyebrow', 'For groups' if p['title'] == 'Catering' else 'Give pizza')
            promos.append(p)
        hero_file = 'hero.jpg'
        site_json = json.dumps({'tz': 'America/New_York', 'fx': t['fx'], 'heroLayout': t['hero_layout'],
                                'locations': [{'id': l['id'], 'name': l['name'], 'hours': l['hours']} for l in d['locations']]})
        ctx = dict(d, t=t, preview=P, fonts=fonts, locations=locs, menu=menu, signatures=sigs, promo_cards=promos,
                   hero_layout=t['hero_layout'], deals=d.get('deals'), careers=d['careers'] if d.get('careers', {}).get('enabled') else None,
                   about=d.get('about_block') or (d.get('about') if isinstance(d.get('about'), dict) else None), links=d.get('links', {}), year=datetime.date.today().year,
                   hero_src=src(hero_file), hero_w=d['hero'].get('w',1440), hero_h=d['hero'].get('h',1577), logo_src=src('logo.webp'), icon_src=(src('logo-icon.webp') if d.get('brand_text') else None), brand_text=d.get('brand_text'), logo_w=d['logo'].get('w'), logo_h=d['logo'].get('h'),
                   about_short=d['tagline'], site_json=site_json, og_image='assets/img/hero.jpg', favicon='assets/img/logo.webp',
                   css_href='assets/site.css', js_src='assets/site.js', menu_note=d['menu_note'], order_note=d.get('order_note'),
                   deals_note=d.get('deals_note'))
        css = env.get_template('site.css.j2').render(name=d['name'], t=t, fonts=fonts, hero_layout=t['hero_layout'],
                                                     deals=d.get('deals'), careers=ctx['careers'], about=d.get('about'))
        js = (ENG / 'templates' / 'site.js').read_text()
        if P:
            html = env.get_template('index.html.j2').render(ctx, css=css, js=js, fragment=False)
            (out / 'preview.html').write_text(html)
            (out / 'artifact.html').write_text(env.get_template('index.html.j2').render(ctx, css=css, js=js, fragment=True))
            results['preview'] = out / 'preview.html'
        else:
            ctx['jsonld'] = json.dumps(jsonld(d), ensure_ascii=False).replace('</', '<\\/')
            html = env.get_template('index.html.j2').render(ctx, fragment=False)
            (site / 'index.html').write_text(html)
            (site / 'assets' / 'site.css').write_text(css.replace('url("fonts/', 'url("fonts/'))
            (site / 'assets' / 'site.js').write_text(js)
            for f, fn, w, s in t['fonts']:
                shutil.copy(ENG / 'fonts' / f'{fn}.woff', site / 'assets' / 'fonts' / f'{fn}.woff')
                lic = ENG / 'fonts' / f"{fn.split('-')[0]}-OFL.txt"; shutil.copy(lic, site / 'assets' / 'fonts' / lic.name)
            for n in used | {'hero.jpg', 'logo.webp'} | ({'logo-icon.webp'} if d.get('brand_text') else set()): shutil.copy(cdir / 'img' / n, site / 'assets' / 'img' / n)
            simple_pages(d, site, t)
    # zip
    z = out / f'{slug}-netlify-site.zip'
    with zipfile.ZipFile(z, 'w', zipfile.ZIP_DEFLATED) as zf:
        for p in sorted(site.rglob('*')):
            if p.is_file(): zf.write(p, p.relative_to(site))
    print('built', slug, '| preview', round(results['preview'].stat().st_size / 1e6, 2), 'MB | zip', round(z.stat().st_size / 1e6, 2), 'MB')

def jsonld(d):
    days = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
    places = []
    for l in d['locations']:
        r = {'@type': 'Restaurant', 'name': f"{d['name']} – {l['name']}" if len(d['locations']) > 1 else d['name'],
             'url': d['domain'] + '/', 'telephone': l['tel'], 'servesCuisine': ['Pizza', 'Subs', 'Salads'], 'image': d['domain'] + '/assets/img/hero.jpg',
             'address': {'@type': 'PostalAddress', 'streetAddress': l['street'], 'addressLocality': l['city'], 'addressRegion': l['region'], 'postalCode': l['postal'], 'addressCountry': 'US'},
             'openingHoursSpecification': [{'@type': 'OpeningHoursSpecification', 'dayOfWeek': [days[x] for x in h['dow']], 'opens': h['open'], 'closes': h['close']} for h in l['hours']],
             'potentialAction': {'@type': 'OrderAction', 'target': l['order']}, 'hasMenu': d['domain'] + '/#menu'}
        if l.get('geo'): r['geo'] = {'@type': 'GeoCoordinates', 'latitude': l['geo'][0], 'longitude': l['geo'][1]}
        places.append(r)
    return {'@context': 'https://schema.org', '@graph': places}

def simple_pages(d, site, t):
    def page(title, h, body):
        return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover"><title>{title} | {d['name']}</title><meta name="robots" content="noindex"><link rel="stylesheet" href="/assets/site.css"><link rel="icon" href="/assets/img/logo.webp"></head>
<body><main class="sec"><div class="wrap" style="display:grid;gap:20px;justify-items:start;max-width:720px"><a href="/"><img src="/assets/img/logo.webp" alt="{d['name']}" style="height:90px;width:auto"></a><h1 class="h2">{h}</h1><p class="lede">{body}</p><a class="btn" href="/">Back to {d['short']}</a></div></main></body></html>'''
    (site / 'thanks').mkdir(exist_ok=True)
    (site / 'thanks' / 'index.html').write_text(page('Application sent', 'Thanks! We got it.', 'Your application went to the managers. If your availability fits the schedule, someone will call or email you.'))
    (site / '404.html').write_text(page('Page not found', 'That slice is gone.', "We couldn't find that page. The menu, hours and online ordering are all on the home page."))
    (site / 'robots.txt').write_text(f"User-agent: *\nAllow: /\nSitemap: {d['domain']}/sitemap.xml\n")
    (site / 'sitemap.xml').write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>{d["domain"]}/</loc></url></urlset>\n')

if __name__ == '__main__':
    for s in sys.argv[1:]: build(s)
