import re
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT = Path(__file__).resolve().parent.parent; slug = 'mr-pizza-gorham'
S = '/tmp/claude-0/-home-claude-pizza-websites/371d6312-fb59-5cf4-a5c5-faa5c6d6419f/scratchpad'
site = ROOT / 'dist' / slug / 'site' / 'index.html'; pre = ROOT / 'dist' / slug / 'preview.html'
bad = 0
def chk(c, m):
    global bad
    print(('ok   ' if c else 'FAIL ') + m); bad += (not c)
with sync_playwright() as p:
    b = p.chromium.launch()
    for name, f in (('site', site), ('preview', pre)):
        for w, h in ((390, 844), (1440, 900)):
            pg = b.new_page(viewport=dict(width=w, height=h)); errs = []
            pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' else None); pg.on('pageerror', lambda e: errs.append(str(e)))
            pg.on('requestfailed', lambda r: errs.append('REQFAIL ' + r.url[-60:]))
            pg.goto(f.as_uri()); pg.wait_for_timeout(500)
            chk(pg.evaluate('document.documentElement.scrollWidth-document.documentElement.clientWidth') <= 0, f'{name} {w}: no h-overflow')
            pg.evaluate("document.querySelectorAll('img[loading=lazy]').forEach(i=>i.loading='eager')"); pg.wait_for_timeout(800)
            br = pg.evaluate("[...document.images].filter(i=>!i.complete||i.naturalWidth==0).map(i=>i.src.slice(-40))"); chk(not br, f'{name} {w}: images ok {br}')
            fonts = pg.evaluate("document.fonts.ready.then(()=>[...document.fonts].filter(f=>f.status=='loaded').map(f=>f.family+f.weight))"); chk(len(fonts) >= 3, f'{name} {w}: fonts loaded {fonts}')
            # builder
            pg.click('label:has(input[name=size][value="1"]) span'); pg.click('label:has(input[value="Pepperoni"]) span'); pg.click('label:has(input[value="Feta"]) span'); pg.click('label:has(#bp-xc) span')
            t = pg.inner_text('#bp-total'); chk(t == '$24', f'{name} {w}: builder 16" +2 toppings + xc = {t}')
            pg.click('#bp-reset'); chk(pg.inner_text('#bp-total') == '$10', 'builder reset')
            pg.click('#m-tabs button:nth-child(5)'); chk(pg.is_visible('#mp4') and not pg.is_visible('#mp0'), f'{name} {w}: tab switch')
            pg.fill('#m-q', 'scallops'); c = pg.inner_text('#m-count'); chk('4 items' in c, f'{name} {w}: search {c}')
            pg.fill('#m-q', 'zzzz'); chk(pg.is_visible('#m-none'), 'no-match message')
            pg.fill('#m-q', '')
            if w == 390:
                pg.click('.burger'); chk(pg.is_visible('#nav a[href="#menu"]'), 'mobile nav opens')
            hrefs = pg.evaluate("[...document.querySelectorAll('a[href]')].map(a=>a.getAttribute('href'))")
            chk(all(h.startswith(('#', 'tel:+16039159266', 'https://www.google.com/maps/search/', 'https://www.facebook.com/profile.php?id=61551594616788')) for h in hrefs), f'{name} {w}: links {sorted(set(hrefs))}')
            chk(not pg.evaluate("[...document.querySelectorAll('a[href^=\"#\"]')].map(a=>a.getAttribute('href')).filter(h=>h.length>1&&!document.querySelector(h))"), 'anchors ok')
            chk(not errs, f'{name} {w}: console clean {errs}')
            if name == 'site':
                pg.click('#m-tabs button:nth-child(1)'); pg.evaluate('window.scrollTo(0,0)'); pg.wait_for_timeout(200)
                pg.screenshot(path=f'{S}/mp{w}.png', full_page=True)
            pg.close()
    b.close()
print('FAILS', bad)
