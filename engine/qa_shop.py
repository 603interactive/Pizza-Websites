import sys
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT = Path(__file__).resolve().parent.parent; slug = 'seabrook-house-of-pizza-seabrook'
SHOT = '/tmp/claude-0/-home-claude-pizza-websites/371d6312-fb59-5cf4-a5c5-faa5c6d6419f/scratchpad/'
url = (ROOT / 'dist' / slug / 'site' / 'index.html').as_uri(); pre = (ROOT / 'dist' / slug / 'preview.html').as_uri()
bad = 0
def chk(c, m):
    global bad
    print(('ok   ' if c else 'FAIL ') + m); bad += (not c)
with sync_playwright() as p:
    b = p.chromium.launch()
    for name, u in (('site', url), ('preview', pre)):
        for w, h in ((390, 844), (1440, 900)):
            pg = b.new_page(viewport=dict(width=w, height=h)); errs = []; fails = []
            pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' else None); pg.on('pageerror', lambda e: errs.append(str(e))); pg.on('requestfailed', lambda r: fails.append(r.url[-50:]))
            pg.goto(u); pg.wait_for_timeout(500)
            ov = pg.evaluate('document.documentElement.scrollWidth-document.documentElement.clientWidth')
            chk(ov <= 0, f'{name} {w}: no h-overflow ({ov})'); chk(not errs and not fails, f'{name} {w}: console/requests clean {errs} {fails}')
            pg.evaluate("document.querySelectorAll('img[loading=lazy]').forEach(i=>i.loading='eager')"); pg.wait_for_timeout(800)
            br = pg.evaluate("[...document.images].filter(i=>!i.complete||i.naturalWidth==0).map(i=>i.src.slice(-40))"); chk(not br, f'{name} {w}: images ok {br}')
            fo = pg.evaluate("document.fonts.ready.then(()=>[...document.fonts].filter(f=>f.status=='loaded').map(f=>f.family))"); chk('Big Shoulders Display' in fo and 'Work Sans' in fo, f'{name} {w}: fonts {fo}')
            hrefs = pg.evaluate("[...document.querySelectorAll('a[href]')].map(a=>a.getAttribute('href'))")
            chk('tel:+16034747778' in hrefs and any('toasttab.com/online/seabrook-house-of-pizza' in x for x in hrefs) and any(x.startswith('https://maps.app.goo.gl/') for x in hrefs), f'{name} {w}: tel/order/maps links')
            chk(not [x for x in hrefs if x in ('#', '') or 'example' in x], f'{name} {w}: no placeholder links')
            if name == 'site':
                pg.screenshot(path=f'{SHOT}shop{w}.png', full_page=True)
            pg.click('#m-tabs button:nth-child(2)'); chk(pg.is_visible('#mp1') and not pg.is_visible('#mp0'), f'{name} {w}: tab switch')
            pg.fill('#m-q', 'calzone'); c = pg.inner_text('#m-count'); chk(c.startswith('2') and pg.is_visible('#mp0'), f'{name} {w}: search {c}')
            pg.fill('#m-q', 'zzzz'); chk(pg.is_visible('#m-none'), f'{name} {w}: no-match msg')
            if w == 390:
                pg.click('.burger'); chk(pg.is_visible('#nav a[href="#menu"]'), f'{name} mobile nav opens')
            links = pg.evaluate("[...document.querySelectorAll('a[href^=\"#\"]')].map(a=>a.getAttribute('href')).filter(h=>h.length>1&&!document.querySelector(h))"); chk(not links, f'{name} {w}: anchors ok {links}')
            t = pg.inner_text('.pill [data-status]'); chk(t.startswith(('Open', 'Closed')), f'{name} {w}: status {t}')
            pg.close()
    def status_at(iso):
        pg = b.new_page(); pg.add_init_script("const _D=Date;const T=new _D('%s').getTime();Date=class extends _D{constructor(...a){a.length?super(...a):super(T)}static now(){return T}};" % iso)
        pg.goto(url); pg.wait_for_timeout(200); t = pg.inner_text('.pill [data-status]'); pg.close(); return t
    for iso, exp in [('2026-11-05T17:00:00Z', 'Open now'), ('2026-11-06T03:00:00Z', 'Closed'), ('2026-11-05T13:00:00Z', 'Closed')]:
        t = status_at(iso); chk(t.startswith(exp), f'status {iso}: {t}')
    b.close()
print('FAILS', bad)
