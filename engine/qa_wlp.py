"""QA for White Lake Pizza: 390/1440, console, overflow, images, fonts, nav, menu tabs/search, links, status logic."""
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT = Path(__file__).resolve().parent.parent; slug = 'white-lake-pizza-west-ossipee'
SC = '/tmp/claude-0/-home-claude-pizza-websites/371d6312-fb59-5cf4-a5c5-faa5c6d6419f/scratchpad/'
site = (ROOT / 'dist' / slug / 'site' / 'index.html').as_uri(); pre = (ROOT / 'dist' / slug / 'preview.html').as_uri()
bad = 0
def chk(c, m):
    global bad
    print(('ok   ' if c else 'FAIL ') + m); bad += (not c)
with sync_playwright() as p:
    b = p.chromium.launch()
    for name, u in (('site', site), ('preview', pre)):
        for w, h in ((390, 844), (1440, 900)):
            pg = b.new_page(viewport=dict(width=w, height=h)); errs = []
            pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' else None); pg.on('pageerror', lambda e: errs.append(str(e)))
            pg.on('requestfailed', lambda r: errs.append('reqfail ' + r.url[-50:]))
            pg.goto(u); pg.wait_for_timeout(500)
            ov = pg.evaluate('document.documentElement.scrollWidth-document.documentElement.clientWidth')
            chk(ov <= 0, f'{name} {w}: no h-overflow ({ov})')
            pg.evaluate("document.querySelectorAll('img[loading=lazy]').forEach(i=>i.loading='eager')"); pg.wait_for_timeout(800)
            br = pg.evaluate("[...document.images].filter(i=>!i.complete||i.naturalWidth==0).map(i=>i.src.slice(-40))"); chk(not br, f'{name} {w}: images ok {br}')
            fonts = pg.evaluate("document.fonts.ready.then(()=>[...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family+f.weight))"); chk(len(fonts) >= 3, f'{name} {w}: fonts loaded {fonts}')
            chk(pg.evaluate("getComputedStyle(document.querySelector('h1')).fontFamily").startswith('"Young Serif"'), f'{name} {w}: h1 font')
            chk(pg.evaluate("document.querySelector('[data-status]').textContent")!='Checking hours…', f'{name} {w}: status filled')
            hrefs = pg.evaluate("[...document.querySelectorAll('a[href]')].map(a=>a.getAttribute('href'))")
            chk('tel:+16035396500' in hrefs and 'https://v2.versieats.com/white-lake-pizza/' in hrefs and any('google.com/maps/search' in x for x in hrefs), f'{name} {w}: tel/order/maps links')
            chk(not [x for x in hrefs if x in ('#', '') or x.startswith('http://')], f'{name} {w}: no empty/insecure links')
            bl = pg.evaluate("[...document.querySelectorAll('a[href^=\"#\"]')].map(a=>a.getAttribute('href')).filter(h=>h.length>1&&!document.querySelector(h))"); chk(not bl, f'{name} {w}: anchors ok {bl}')
            n = pg.evaluate("document.querySelectorAll('#m-tabs button').length"); chk(n == 7, f'{name} {w}: 7 tabs')
            for i in range(n):
                pg.click(f'#m-tabs button:nth-child({i+1})'); chk(pg.is_visible(f'#mp{i}') and pg.locator('.m-panel:visible').count() == 1 and pg.locator(f'#mp{i} .m-it:visible').count() > 0, f'{name} {w}: tab {i}')
            pg.fill('#m-q', 'feta'); c = pg.inner_text('#m-count'); chk('match' in c and pg.locator('.m-it:visible').count() > 5, f'{name} {w}: search feta {c}')
            pg.fill('#m-q', 'zzzq'); chk(pg.is_visible('#m-none'), f'{name} {w}: no-match msg'); pg.fill('#m-q', '')
            pg.click('[data-season=summer]'); chk(pg.is_visible('[data-season-table=summer]') and not pg.is_visible('[data-season-table=off]'), f'{name} {w}: season toggle')
            if w == 390:
                pg.click('.burger'); chk(pg.is_visible('#nav a[href="#menu"]'), f'{name}: mobile nav opens'); pg.click('#nav a[href="#menu"]'); chk(not pg.is_visible('#nav a[href="#menu"]'), f'{name}: nav closes')
            else:
                pg.click('.top nav a[href="#visit"]'); pg.wait_for_timeout(600)
            if name == 'site':
                pg.click('#m-tabs button:nth-child(1)')
                pg.evaluate('scrollTo(0,0)'); pg.screenshot(path=f'{SC}wlp{w}.png', full_page=True)
            pg.close()
    def status_at(iso, month_sum=False):
        pg = b.new_page(); pg.add_init_script("const _D=Date;const T=new _D('%s').getTime();Date=class extends _D{constructor(...a){a.length?super(...a):super(T)}static now(){return T}};" % iso)
        pg.goto(site); pg.wait_for_timeout(200); t = pg.inner_text('.pl-head [data-status]'); pg.close(); return t
    for iso, exp, lab in [('2026-11-05T17:00:00Z', 'Open now', 'Thu Nov noon'), ('2026-11-06T01:30:00Z', 'Closed', 'Thu Nov 8:30PM (off-season closed at 8)'), ('2026-11-06T00:00:00Z', 'Open now', 'Thu Nov 7PM'),
                          ('2026-07-10T01:30:00Z', 'Open now', 'Thu Jul 9:30PM? summer Thu closes 9 -> closed'), ('2026-11-05T14:00:00Z', 'Closed', 'Thu 9AM'), ('2026-11-07T01:30:00Z', 'Open now', 'Fri Nov 8:30PM, closes 9')]:
        t = status_at(iso)
        if 'summer' in lab or 'Jul' in lab: exp = 'Closed'
        chk(t.startswith(exp), f'status {lab}: {t}')
    b.close()
print('FAILS', bad)
