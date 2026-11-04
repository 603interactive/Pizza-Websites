import sys, json, re
from pathlib import Path
from playwright.sync_api import sync_playwright
ROOT = Path(__file__).resolve().parent.parent; slug = 'durham-house-of-pizza-durham'
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
            pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' else None); pg.on('pageerror', lambda e: errs.append(str(e)))
            pg.goto(u); pg.wait_for_timeout(500)
            ov = pg.evaluate('document.documentElement.scrollWidth-document.documentElement.clientWidth')
            chk(ov <= 0, f'{name} {w}: no h-overflow ({ov})'); chk(not errs, f'{name} {w}: console clean {errs}')
            pg.evaluate("document.querySelectorAll('img[loading=lazy]').forEach(i=>i.loading='eager')"); pg.wait_for_timeout(800)
            br = pg.evaluate("[...document.images].filter(i=>!i.complete||i.naturalWidth==0).map(i=>i.src.slice(-40))"); chk(not br, f'{name} {w}: images ok {br}')
            if name == 'site':
                pg.screenshot(path=f'/tmp/claude-0/-home-claude-pizza-websites/34ac2a61-0ac1-5107-9f15-4ac07a7c0d5a/scratchpad/dh{w}.png', full_page=True)
                # scrubber
                pg.fill('#ls-range', '1500') if False else pg.evaluate("r=document.querySelector('#ls-range');r.value=1500;r.dispatchEvent(new Event('input'))")
                t = pg.inner_text('#ls-read').lower(); chk('thu' in t and 'fri' in t and 'sat' in t and 'mon' not in t, f'{w}: 1AM -> {t!r}')
                pg.evaluate("r=document.querySelector('#ls-range');r.value=1200;r.dispatchEvent(new Event('input'))"); t = pg.inner_text('#ls-read').lower(); chk('mon' in t and 'sun' not in t, f'{w}: 8PM -> {t!r}')
                pg.evaluate("r=document.querySelector('#ls-range');r.value=1560;r.dispatchEvent(new Event('input'))"); t = pg.inner_text('#ls-read').lower(); chk('closed every day' in t, f'{w}: 2AM {t!r}')
                pg.evaluate("r=document.querySelector('#ls-range');r.value=1590;r.dispatchEvent(new Event('input'))"); t = pg.inner_text('#ls-read').lower(); chk('closed every day' in t, f'{w}: 2:30AM {t!r}')
                # menu
                pg.click('#m-tabs button:nth-child(2)'); chk(pg.is_visible('#mp1') and not pg.is_visible('#mp0'), f'{w}: tab switch')
                pg.fill('#m-q', 'feta'); c = pg.inner_text('#m-count'); chk('match' in c, f'{w}: search {c}')
                if w == 390:
                    pg.click('.burger'); chk(pg.is_visible('#nav a[href="#menu"]'), 'mobile nav opens')
                links = pg.evaluate("[...document.querySelectorAll('a[href^=\"#\"]')].map(a=>a.getAttribute('href')).filter(h=>h.length>1&&!document.querySelector(h))"); chk(not links, f'{w}: anchors ok {links}')
            pg.close()
    # status logic with faked time
    import datetime
    cases = [('2026-11-05T05:30:00Z', True, 'Thu 12:30 AM'), ]
    def status_at(iso, tz='America/New_York'):
        pg = b.new_page(); pg.add_init_script("const _D=Date;const T=new _D('%s').getTime();Date=class extends _D{constructor(...a){a.length?super(...a):super(T)}static now(){return T}};" % iso)
        pg.goto(url); pg.wait_for_timeout(200); t = pg.inner_text('.pill [data-status]'); r = pg.inner_text('#ls-read'); pg.close(); return t, r
    # EST Nov: UTC-5. Fri 1:00AM EST = 06:00Z Fri Nov 6
    for iso, exp, lab in [('2026-11-06T06:00:00Z', 'Open now', 'Fri 1AM (Thu night)'), ('2026-11-06T07:30:00Z', 'Closed', 'Fri 2:30AM'), ('2026-11-05T05:00:00Z', 'Closed', 'Thu 12AM (Wed night, closed)'),
                          ('2026-11-08T05:30:00Z', 'Open now', 'Sun 12:30AM (Sat night)'), ('2026-11-08T17:00:00Z', 'Closed', 'Sun noon'), ('2026-11-09T17:00:00Z', 'Open now', 'Mon noon'), ('2026-11-04T02:30:00Z', 'Closed', 'Tue 9:30PM')]:
        t, r = status_at(iso); chk(t.startswith(exp), f'status {lab}: {t} | {r}')
    b.close()
print('FAILS', bad)
