import sys
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT = Path(__file__).resolve().parent.parent; slug = 'pelham-house-of-pizza-pelham'
SHOT = '/tmp/claude-0/-home-claude-pizza-websites/371d6312-fb59-5cf4-a5c5-faa5c6d6419f/scratchpad'
url = (ROOT / 'dist' / slug / 'site' / 'index.html').as_uri(); pre = (ROOT / 'dist' / slug / 'preview.html').as_uri()
bad = 0
def chk(c, m):
    global bad
    print(('ok   ' if c else 'FAIL ') + m); bad += (not c)
with sync_playwright() as p:
    b = p.chromium.launch()
    for name, u in (('site', url), ('preview', pre)):
        for w, h in ((390, 844), (1440, 900)):
            pg = b.new_page(viewport=dict(width=w, height=h)); errs = []
            pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' else None); pg.on('pageerror', lambda e: errs.append(str(e))); pg.on('requestfailed', lambda r: errs.append('REQ ' + r.url[-50:]))
            pg.goto(u); pg.wait_for_timeout(500)
            chk(pg.evaluate('document.documentElement.scrollWidth-document.documentElement.clientWidth') <= 0, f'{name} {w}: no h-overflow'); chk(not errs, f'{name} {w}: console clean {errs}')
            pg.evaluate("document.querySelectorAll('img[loading=lazy]').forEach(i=>i.loading='eager')"); pg.wait_for_timeout(800)
            br = pg.evaluate("[...document.images].filter(i=>!i.complete||i.naturalWidth==0).map(i=>i.src.slice(-40))"); chk(not br, f'{name} {w}: images ok {br}')
            fonts = pg.evaluate("Promise.all(['Young Serif','Work Sans'].map(f=>document.fonts.load('16px \"'+f+'\"').then(r=>r.length)))"); chk(all(fonts), f'{name} {w}: fonts load {fonts}')
            chk(pg.inner_text('[data-status]') != 'Checking hours…', f'{name} {w}: status set')
            pg.click('#m-tabs button:nth-child(2)'); chk(pg.is_visible('#mp1') and not pg.is_visible('#mp0'), f'{name} {w}: tab switch')
            pg.fill('#m-q', 'haddock'); c = pg.inner_text('#m-count'); chk('match' in c, f'{name} {w}: search {c}')
            pg.fill('#m-q', 'zzzz'); chk(pg.is_visible('#m-none'), f'{name} {w}: no-match msg'); pg.fill('#m-q', '')
            if w == 390:
                pg.click('.burger'); chk(pg.is_visible('#nav a[href="#menu"]'), f'{name} mobile nav opens')
                pg.click('#nav a[href="#menu"]'); chk(not pg.is_visible('#nav a[href="#menu"]'), f'{name} mobile nav closes')
            hrefs = pg.evaluate("[...document.querySelectorAll('a')].map(a=>a.getAttribute('href'))")
            chk('tel:+16036352700' in hrefs and any(h.startswith('https://www.google.com/maps/search') for h in hrefs) and any(h.startswith('https://online.skytab.com/') for h in hrefs), f'{name} {w}: tel/maps/order links')
            chk(not pg.evaluate("[...document.querySelectorAll('a[href^=\"#\"]')].map(a=>a.getAttribute('href')).filter(h=>h.length>1&&!document.querySelector(h)).length"), f'{name} {w}: anchors ok')
            pg.fill('#m-q','')
            if name == 'site': pg.screenshot(path=f'{SHOT}/ph{w}.png', full_page=True)
            pg.close()
    def status_at(iso):
        pg = b.new_page(); pg.add_init_script("const _D=Date;const T=new _D('%s').getTime();Date=class extends _D{constructor(...a){a.length?super(...a):super(T)}static now(){return T}};" % iso)
        pg.goto(url); pg.wait_for_timeout(200); t = pg.inner_text('.pill [data-status]'); pg.close(); return t
    for iso, exp, lab in [('2026-11-05T17:00:00Z', 'Open now', 'Thu noon'), ('2026-11-06T02:30:00Z', 'Open now', 'Thu 9:30PM'), ('2026-11-04T02:30:00Z', 'Closed', 'Tue 9:30PM'), ('2026-11-08T16:30:00Z', 'Open now', 'Sun 11:30AM'), ('2026-11-08T14:00:00Z', 'Closed', 'Sun 9AM')]:
        t = status_at(iso); chk(t.startswith(exp), f'status {lab}: {t}')
    b.close()
print('FAILS', bad)
