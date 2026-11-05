import sys, re
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT = Path(__file__).resolve().parent.parent; slug = 'marys-pizza-gorham'
SHOTS = Path(sys.argv[1] if len(sys.argv) > 1 else '/tmp')
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
            pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' else None); pg.on('pageerror', lambda e: errs.append(str(e)))
            pg.on('requestfailed', lambda r: fails.append(r.url[-50:]))
            pg.goto(u); pg.wait_for_timeout(500)
            tag = f'{name} {w}'
            chk(pg.evaluate('document.documentElement.scrollWidth-document.documentElement.clientWidth') <= 0, f'{tag}: no h-overflow')
            chk(not errs and not fails, f'{tag}: console/requests clean {errs} {fails}')
            pg.evaluate("document.querySelectorAll('img[loading=lazy]').forEach(i=>i.loading='eager')"); pg.wait_for_timeout(800)
            br = pg.evaluate("[...document.images].filter(i=>!i.complete||i.naturalWidth==0).map(i=>i.src.slice(-40))"); chk(not br, f'{tag}: images ok {br}')
            fonts = pg.evaluate("document.fonts.ready.then(()=>['400 20px Gloock','400 20px \"Crimson Pro\"','700 20px \"Instrument Sans\"'].map(f=>document.fonts.check(f)))"); chk(all(fonts), f'{tag}: fonts {fonts}')
            chk('Mary' in pg.inner_text('h1') or 'Home-style' in pg.inner_text('h1'), f'{tag}: h1')
            # links
            hrefs = pg.evaluate("[...document.querySelectorAll('a[href]')].map(a=>a.getAttribute('href'))")
            chk('tel:+16037526150' in hrefs, f'{tag}: tel link')
            chk(any(h.startswith('https://www.google.com/maps/search/') for h in hrefs), f'{tag}: maps link')
            chk(all(h.startswith(('#', 'tel:', 'https://')) for h in hrefs), f'{tag}: link schemes')
            chk(not pg.evaluate("[...document.querySelectorAll('a[href^=\"#\"]')].map(a=>a.getAttribute('href')).filter(h=>h.length>1&&!document.querySelector(h))"), f'{tag}: anchors resolve')
            # status/deal text rendered
            chk(re.search(r'Open now|Closed', pg.inner_text('[data-status]')) is not None, f'{tag}: status text')
            chk(len(pg.inner_text('#t-big')) > 5, f'{tag}: deal text')
            # menu
            n = pg.locator('#m-tabs button').count(); chk(n == 11, f'{tag}: {n} tabs')
            pg.click('#m-tabs button:nth-child(5)'); chk(pg.is_visible('#mp4') and not pg.is_visible('#mp0'), f'{tag}: tab switch')
            pg.fill('#m-q', 'lasagna'); c = pg.inner_text('#m-count'); chk('match' in c and int(c.split()[0]) >= 3, f'{tag}: search {c}')
            pg.fill('#m-q', 'zzzz'); chk(pg.is_visible('#m-none'), f'{tag}: no-match msg'); pg.fill('#m-q', '')
            # builder
            pg.locator('#bld label:has-text("Pepperoni")').click(); pg.locator('#bld label:has-text("Mushrooms")').click()
            chk(pg.inner_text('#tk-p') == '$20.99', f'{tag}: large 2-topping = {pg.inner_text("#tk-p")}')
            pg.locator('#bld label:has-text("Gluten-free")').click(); chk(pg.inner_text('#tk-p') == '$16.29', f'{tag}: GF small 2-topping = {pg.inner_text("#tk-p")}')
            pg.locator('#bld label:has-text("Regular")').click(); pg.locator('#bld label:has-text("Large")').click()
            for t in ('Sausage', 'Bacon', 'Ham'): pg.locator(f'#bld label:has-text("{t}")').first.click()
            chk(pg.inner_text('#tk-p') == '$28.49', f'{tag}: large 5-topping = {pg.inner_text("#tk-p")}')
            if w == 390:
                pg.click('.burger'); chk(pg.is_visible('#nav a[href="#menu"]'), f'{tag}: mobile nav opens')
            if name == 'site':
                pg.evaluate('window.scrollTo(0,0)'); pg.screenshot(path=str(SHOTS / f'marys{w}.png'), full_page=True)
            pg.close()
    def status_at(iso):
        pg = b.new_page(); pg.add_init_script("const _D=Date;const T=new _D('%s').getTime();Date=class extends _D{constructor(...a){a.length?super(...a):super(T)}static now(){return T}};" % iso)
        pg.goto(url); pg.wait_for_timeout(200); t = pg.inner_text('.pill [data-status]'); d = pg.inner_text('#t-big'); pg.close(); return t, d
    # EST (UTC-5) Nov 2026: Thu Nov 5
    for iso, exp, lab in [('2026-11-05T17:00:00Z', 'Open now', 'Thu noon'), ('2026-11-05T20:00:00Z', 'Closed · opens today at 4 PM', 'Thu 3PM'), ('2026-11-06T00:30:00Z', 'Open now', 'Thu 7:30PM'),
                          ('2026-11-06T01:30:00Z', 'Closed · opens tomorrow at 11 AM', 'Thu 8:30PM'), ('2026-11-08T17:00:00Z', 'Closed · opens tomorrow at 11 AM', 'Sun noon'), ('2026-11-07T20:00:00Z', 'Closed · opens today at 4 PM', 'Sat 3PM')]:
        t, d = status_at(iso); chk(t.startswith(exp), f'status {lab}: {t}')
    t, d = status_at('2026-11-03T17:00:00Z'); chk('Tuesday' in d and '19.99' in d, f'Tuesday deal: {d}')
    t, d = status_at('2026-11-05T17:00:00Z'); chk('Thursday' in d and '32.99' in d, f'Thursday deal: {d}')
    t, d = status_at('2026-11-08T17:00:00Z'); chk('Closed Sundays' in d, f'Sunday deal: {d}')
    b.close()
print('FAILS', bad)
