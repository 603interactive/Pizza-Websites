"""QA for bespoke sites (joeys, acres): generic checks + feature tests, on preview.html and the production site/. usage: qa2.py <slug>"""
import sys, json, asyncio, re
from pathlib import Path
from playwright.async_api import async_playwright
ROOT = Path(__file__).resolve().parent.parent
CHECK_JS = re.search(r'CHECK_JS = r"""(.*?)"""', (ROOT / 'engine' / 'qa.py').read_text(), re.S).group(1).replace(".closest('.hero,.ticker,.concept,[hidden],.sr')", ".closest('[hidden],.sr,.ribbon,svg')")
async def feat_joeys(pg, r):
    await pg.click('#f-count label:nth-child(4)'); await pg.click('#f-flavor label:nth-child(2)')
    for i in (1, 7, 8): await pg.click(f'#f-sauce label:nth-child({i})')
    await pg.click('#f-jojo label:nth-child(3)'); await pg.wait_for_timeout(700)
    r['total'] = await pg.inner_text('#t-total'); r['stix'] = await pg.evaluate("document.querySelectorAll('#tray .stix').length"); r['lines'] = await pg.inner_text('#t-lines')
    await pg.click('#t-copy'); r['copyLabel'] = await pg.inner_text('#t-copy')
    await pg.fill('#q', 'steak'); await pg.wait_for_timeout(200); r['steakTickets'] = await pg.evaluate("[...document.querySelectorAll('.tk')].filter(t=>!t.hidden).length")
    await pg.fill('#q', 'zzzz'); r['emptyMsg'] = await pg.evaluate("!document.querySelector('#none').hidden"); await pg.fill('#q', '')
    await pg.click('.tabs button:nth-child(5)'); await pg.wait_for_timeout(200); r['tabVisible'] = await pg.evaluate("[...document.querySelectorAll('.tk')].filter(t=>!t.hidden).length")
async def feat_acres(pg, r):
    r['init'] = [await pg.inner_text(x) for x in ('#a14', '#a20', '#c14', '#c20')]
    await pg.click('#picker label:nth-child(8)'); await pg.wait_for_timeout(900)
    r['marg'] = [await pg.inner_text(x) for x in ('#a14', '#a20', '#c14', '#c20', '#p14', '#p20', '#verdict')]; r['photoBg'] = await pg.evaluate("getComputedStyle(document.querySelector('#d20')).backgroundImage.slice(0,20)")
    await pg.click('#rank li:nth-child(3) button'); await pg.wait_for_timeout(900); r['afterRank'] = await pg.evaluate("document.querySelector('#picker input:checked').closest('label').innerText")
    await pg.check('#rectog'); r['recVisible'] = await pg.evaluate("!document.querySelector('#rec').hidden")
    r['discPx'] = await pg.evaluate("[document.querySelector('#d14').getBoundingClientRect().width, document.querySelector('#d20').getBoundingClientRect().width]")
    await pg.fill('#q', 'baklava'); await pg.wait_for_timeout(200); r['baklavaAisles'] = await pg.evaluate("[...document.querySelectorAll('.aisle')].filter(a=>!a.hidden).length")
    await pg.fill('#q', 'zzzz'); r['emptyMsg'] = await pg.evaluate("!document.querySelector('#none').hidden"); await pg.fill('#q', '')
async def feat_tremont(pg, r):
    r['cats'] = await pg.evaluate("[...document.querySelectorAll('#lp-tabs button')].length")
    await pg.click('#lp-list li:nth-child(1) .sz button:nth-child(3)'); await pg.click('#lp-list li:nth-child(1) .sz button:nth-child(3)')
    r['total1'] = await pg.inner_text('#lp-total'); r['pts1'] = await pg.inner_text('#lp-pts'); r['next1'] = await pg.inner_text('#lp-next')
    await pg.click('#lp-tabs button:nth-child(4)'); await pg.click('#lp-list li:nth-child(3) .sz button:nth-child(2)')
    r['total2'] = await pg.inner_text('#lp-total'); r['pts2'] = await pg.inner_text('#lp-pts'); r['on'] = await pg.evaluate("document.querySelectorAll('#lp-rungs li.on').length")
    await pg.click('#lp-clear'); r['cleared'] = await pg.inner_text('#lp-pts')
    await pg.fill('#m-q', 'pesto'); await pg.wait_for_timeout(150); r['pesto'] = await pg.inner_text('#m-count')
    await pg.fill('#m-q', 'zzzz'); r['emptyMsg'] = await pg.evaluate("!document.querySelector('#m-empty').hidden"); await pg.fill('#m-q', '')
async def feat_charlestown(pg, r):
    await pg.click('#m-tabs button:nth-child(4)'); r['subsVisible'] = await pg.evaluate("[...document.querySelectorAll('.m-panel')].filter(p=>!p.hidden).map(p=>p.dataset.p)")
    await pg.fill('#m-q', 'steak'); await pg.wait_for_timeout(150); r['steak'] = await pg.inner_text('#m-count')
    await pg.fill('#m-q', 'zzzz'); r['emptyMsg'] = await pg.evaluate("!document.querySelector('#m-empty').hidden"); await pg.fill('#m-q', '')
    await pg.fill('#cf input[name=name]', 'Test'); await pg.fill('#cf input[name=phone]', '6035551212'); await pg.click('#cf button[type=submit]'); await pg.wait_for_timeout(200)
    r['formOk'] = await pg.evaluate("!document.querySelector('#cf-ok').hidden")
async def feat_farmington(pg, r):
    await pg.click('#st-size button:nth-child(1)')
    for n in ('Pepperoni', 'Sausage'): await pg.click(f'#st-meat button[data-n="{n}"]')
    r['med2'] = await pg.inner_text('#st-total'); r['tip'] = await pg.inner_text('#st-tip')
    await pg.click('#st-size button:nth-child(2)'); r['lg2'] = await pg.inner_text('#st-total')
    await pg.click('#st-specs .sp:nth-child(2) button'); r['loaded'] = await pg.evaluate("document.querySelectorAll('.tp[aria-pressed=true]').length"); r['tipMeat'] = await pg.inner_text('#st-tip')
    await pg.click('#st-clear'); r['cleared'] = await pg.inner_text('#st-total')
    await pg.click('#m-tabs button:nth-child(4)'); r['subs'] = await pg.evaluate("[...document.querySelectorAll('.m-panel')].filter(p=>!p.hidden).map(p=>p.dataset.p)")
    await pg.fill('#m-q', 'gyro'); await pg.wait_for_timeout(150); r['gyro'] = await pg.inner_text('#m-count')
    await pg.fill('#m-q', 'zzzz'); r['emptyMsg'] = await pg.evaluate("!document.querySelector('#m-empty').hidden"); await pg.fill('#m-q', '')
async def feat_gilford(pg, r):
    await pg.fill('#dd-sub', '40'); await pg.wait_for_timeout(100)
    r['ours'] = await pg.inner_text('#dd-ours'); r['bar'] = await pg.inner_text('#dd-save')
    await pg.fill('#dd-app', '9.5'); await pg.wait_for_timeout(100); r['save'] = await pg.inner_text('#dd-save'); r['verdict'] = await pg.inner_text('#dd-verdict')
    await pg.click('#m-tabs button:nth-child(4)'); r['panel'] = await pg.evaluate("[...document.querySelectorAll('.m-panel')].filter(p=>!p.hidden).map(p=>p.dataset.p)")
    await pg.fill('#m-q', 'steak'); await pg.wait_for_timeout(150); r['steak'] = await pg.inner_text('#m-count')
    await pg.fill('#m-q', 'zzzz'); r['emptyMsg'] = await pg.evaluate("!document.querySelector('#m-empty').hidden"); await pg.fill('#m-q', '')
async def feat_jaffrey(pg, r):
    r['flavors'] = await pg.evaluate("document.querySelectorAll('#fl-pick button').length"); r['first'] = await pg.evaluate("[...document.querySelectorAll('.fl-body:not([hidden]) .fc')].map(c=>c.innerText.replace(/\\n/g,' '))")
    await pg.click('#fl-pick button:nth-child(5)'); r['steakBomb'] = await pg.evaluate("[...document.querySelectorAll('.fl-body:not([hidden]) .fc')].map(c=>c.innerText.replace(/\\n/g,' '))")
    r['visibleBodies'] = await pg.evaluate("[...document.querySelectorAll('.fl-body')].filter(b=>!b.hidden).length")
    r['doorsOpen'] = await pg.evaluate("document.querySelector('#hero').classList.contains('open')")
    await pg.click('#m-tabs button:nth-child(4)'); r['panel'] = await pg.evaluate("[...document.querySelectorAll('.m-panel')].filter(p=>!p.hidden).map(p=>p.dataset.p)")
    await pg.fill('#m-q', 'haddock'); await pg.wait_for_timeout(150); r['haddock'] = await pg.inner_text('#m-count')
    await pg.fill('#m-q', 'zzzz'); r['emptyMsg'] = await pg.evaluate("!document.querySelector('#m-none').hidden"); await pg.fill('#m-q', '')
async def feat_enfield(pg, r):
    r['todayTab'] = await pg.evaluate("document.querySelector('#wk-rail button.today')?.dataset.dow")
    r['sel'] = await pg.evaluate("document.querySelector('#wk-rail button[aria-selected=true]').dataset.dow")
    await pg.click('#wk-rail button[data-dow="2"]'); await pg.click('[data-st="+"]'); r['tue'] = await pg.inner_text('#wk-out')
    await pg.click('#wk-rail button[data-dow="3"]'); await pg.fill('#wk-q', '30'); await pg.wait_for_timeout(100); r['wed'] = await pg.inner_text('#wk-out')
    await pg.click('#wk-rail button[data-dow="5"]'); r['fri'] = await pg.inner_text('#wk-out')
    await pg.click('#wk-rail button[data-dow="0"]'); await pg.select_option('#wk-a', '8'); r['sun'] = await pg.inner_text('#wk-out')
    await pg.click('#wk-rail button[data-dow="1"]'); r['mon'] = await pg.inner_text('#wk-ctl'); await pg.click('#wk-go'); r['afterGo'] = await pg.inner_text('#wk-day')
    await pg.fill('#pp-n', '15'); r['party'] = await pg.inner_text('#pp-t')
    await pg.click('#m-tabs button:nth-child(2)'); r['panel'] = await pg.evaluate("[...document.querySelectorAll('.m-panel')].filter(p=>!p.hidden).map(p=>p.dataset.p)")
    await pg.fill('#m-q', 'gyro'); await pg.wait_for_timeout(150); r['gyro'] = await pg.inner_text('#m-count')
    await pg.fill('#m-q', 'zzzz'); r['emptyMsg'] = await pg.evaluate("!document.querySelector('#m-empty').hidden"); await pg.fill('#m-q', '')
async def feat_papajays(pg, r):
    r['init'] = [await pg.inner_text('#cp-lines'), await pg.inner_text('#cp-total'), await pg.inner_text('#cp-feeds')]
    await pg.fill('#cp-n', '40'); await pg.wait_for_timeout(100); r['n40'] = [await pg.inner_text('#cp-lines'), await pg.inner_text('#cp-total'), await pg.inner_text('#cp-pp'), await pg.inner_text('#cp-vs')]
    await pg.select_option('#cp-k', '0'); await pg.select_option('#cp-h', '4'); r['spec'] = [await pg.inner_text('#cp-lines'), await pg.inner_text('#cp-total')]
    await pg.fill('#cp-r', '6'); r['slider'] = await pg.input_value('#cp-n'); r['mailto'] = (await pg.get_attribute('#cp-mail', 'href'))[:120]
    await pg.click('[data-go="hot-subs"]'); await pg.wait_for_timeout(300); r['go'] = await pg.evaluate("[...document.querySelectorAll('.m-panel')].filter(p=>!p.hidden).map(p=>p.dataset.p)")
    await pg.click('#m-tabs button:nth-child(2)'); r['panel'] = await pg.evaluate("[...document.querySelectorAll('.m-panel')].filter(p=>!p.hidden).map(p=>p.dataset.p)")
    await pg.fill('#m-q', 'steak tip'); await pg.wait_for_timeout(150); r['steak'] = await pg.inner_text('#m-count')
    await pg.fill('#m-q', 'zzzz'); r['emptyMsg'] = await pg.evaluate("!document.querySelector('#m-empty').hidden"); await pg.fill('#m-q', '')
async def feat_supreme(pg, r):
    await pg.fill('#m-q', 'gyro'); await pg.wait_for_timeout(150); r['gyro'] = await pg.inner_text('#m-count')
    await pg.fill('#m-q', 'zzzz'); r['emptyMsg'] = await pg.evaluate("!document.querySelector('#m-none').hidden"); await pg.fill('#m-q', '')
    await pg.click('#m-tabs button:nth-child(4)'); r['panel'] = await pg.evaluate("[...document.querySelectorAll('.m-panel')].filter(p=>!p.hidden).length")
    r['season'] = await pg.evaluate("document.querySelector('.seas.cur').dataset.season")
async def feat_nepizza(pg, r):
    r['total'] = await pg.inner_text('#m-count')
    await pg.click('#chips button[data-k="chicken"]'); await pg.click('#chips button[data-k="veg"]'); r['chickenVeg'] = await pg.inner_text('#m-count')
    r['chickenVegItems'] = await pg.evaluate("[...document.querySelectorAll('.m-it:not([hidden]) .m-n')].map(e=>e.innerText)")
    await pg.click('#m-clear'); await pg.click('#chips button[data-k="nomeat"]'); r['nomeat'] = await pg.inner_text('#m-count'); r['nomeatNote'] = await pg.evaluate("!document.querySelector('#f-nm').hidden")
    r['nomeatHasMeat'] = await pg.evaluate("[...document.querySelectorAll('.m-it:not([hidden]) .m-n')].map(e=>e.innerText).filter(t=>/chicken|steak|ham|bacon|beef|sausage|veal|meatball|pepperoni|tuna|haddock/i.test(t))")
    await pg.click('#m-clear'); await pg.uncheck('#m-px'); r['pxHidden'] = await pg.evaluate("getComputedStyle(document.querySelector('.px')).display"); await pg.check('#m-px')
    await pg.fill('#m-q', 'zzzz'); r['emptyMsg'] = await pg.evaluate("!document.querySelector('#m-none').hidden"); await pg.fill('#m-q', '')
    r['dagger'] = await pg.evaluate("document.querySelectorAll('.px .dag').length>0")
async def feat_alton(pg, r):
    r['init'] = await pg.inner_text('#pc-total')
    await pg.click('#pc .chips label:nth-child(1)'); r['one'] = await pg.inner_text('#pc-total')
    await pg.click('#pc label:has(input[name=size][value="1"])'); r['oneLarge'] = await pg.inner_text('#pc-total')
    for n in ('Tomatoes', 'Fresh Mushrooms', 'Broccoli', 'Black Olives', 'Pepper'): await pg.click(f'#pc .chips label:has(input[value="{n}"])')
    r['six'] = [await pg.inner_text('#pc-total'), await pg.inner_text('#pc-tip')]
    await pg.click('#pc .chips label:has(input[value="Pepperoni"])'); await pg.click('#pc .chips label:has(input[value="Sausage"])'); await pg.click('#pc .chips label:has(input[value="Garlic"])')
    r['nine'] = [await pg.inner_text('#pc-total'), await pg.inner_text('#pc-tip')]
    await pg.click('#pc-copy'); r['copy'] = await pg.inner_text('#pc-copy'); r['rows'] = await pg.inner_text('#pc-rows')
    await pg.click('#pc-clear'); r['cleared'] = await pg.inner_text('#pc-total')
    await pg.click('#m-tabs button:nth-child(7)'); r['panel'] = await pg.evaluate("[...document.querySelectorAll('.m-panel')].filter(p=>!p.hidden).map(p=>p.id)")
    await pg.fill('#m-q', 'baklava'); await pg.wait_for_timeout(150); r['baklava'] = await pg.inner_text('#m-count')
    await pg.fill('#m-q', 'zzzz'); r['emptyMsg'] = await pg.evaluate("!document.querySelector('#m-none').hidden"); await pg.fill('#m-q', '')
async def feat_tilton(pg, r):
    vis = await pg.evaluate("getComputedStyle(document.querySelector('.dock')).display !== 'none'")
    if vis: await pg.click('#dock-check'); r['sheetOpen'] = await pg.evaluate("document.querySelector('#check').classList.contains('open')"); await pg.click('#ck-close')
    await pg.click('#mp0 .m-it:nth-child(1) .add:nth-child(2)'); await pg.click('#mp0 .m-it:nth-child(1) .add:nth-child(2)')
    r['total1'] = await pg.inner_text('#ck-total')
    if vis: await pg.click('#dock-check')
    await pg.click('#ck-lines button[data-d="-1"]'); r['total2'] = await pg.inner_text('#ck-total')
    if vis: await pg.click('#ck-close')
    await pg.click('#mt1'); await pg.click('#mp1 .m-it:nth-child(1) .add:nth-child(1)'); r['total3'] = await pg.inner_text('#ck-total'); r['lines'] = await pg.evaluate("document.querySelectorAll('#ck-lines li').length")
    r['copy'] = None
    await pg.fill('#m-q', 'haddock'); await pg.wait_for_timeout(150); r['haddock'] = await pg.inner_text('#m-count')
    await pg.fill('#m-q', 'zzzz'); r['emptyMsg'] = await pg.evaluate("!document.querySelector('#m-none').hidden"); await pg.fill('#m-q', '')
    await pg.evaluate("document.querySelector('#ck-clear').click()"); r['cleared'] = await pg.inner_text('#ck-total')
FEATS = {'tilton-house-of-pizza-tilton': feat_tilton,'alton-village-pizza-alton': feat_alton, 'new-england-pizza-exeter': feat_nepizza, 'supreme-house-of-pizza-raymond': feat_supreme, 'jaffrey-pizza-barn': feat_jaffrey, 'papa-jays-pizzeria': feat_papajays, 'enfield-house-of-pizza': feat_enfield, 'farmington-house-of-pizza': feat_farmington, 'gilford-house-of-pizza': feat_gilford, 'charlestown-house-of-pizza': feat_charlestown, 'uncle-joeys': feat_joeys, 'golden-acres-pizza-market': feat_acres, 'tremont-house-of-pizza': feat_tremont}
async def feat_newport(pg, r):
    await pg.click('#pm-style label:nth-child(1) input'); await pg.click('#pm-size label:nth-child(3) input')
    for n in ('Pepperoni', 'Mushroom'): await pg.click(f'input[name=top][value="{n}"]')
    await pg.click('#pm-add'); r['line1'] = await pg.inner_text('#tape-lines'); r['total1'] = await pg.inner_text('#tape-total')
    await pg.click('#pm-style label:nth-child(3) input'); r['gourmetSizes'] = await pg.evaluate("[...document.querySelectorAll('#pm-size span')].map(s=>s.innerText)"); r['topsDisabled'] = await pg.evaluate("document.querySelector('input[name=top]').disabled")
    await pg.click('#pm-style label:nth-child(5) input'); r['whiteSizes'] = await pg.evaluate("[...document.querySelectorAll('#pm-size span')].map(s=>s.innerText)")
    await pg.click('#pm-crust label:nth-child(2) input'); await pg.click('#pm-plus'); await pg.click('#pm-add'); r['total2'] = await pg.inner_text('#tape-total')
    await pg.click('#tape-feast'); r['total3'] = await pg.inner_text('#tape-total')
    await pg.click('#tape-lines li:nth-child(1) .x'); r['afterRemove'] = await pg.inner_text('#tape-total')
    await pg.click('#tape-clear'); r['cleared'] = await pg.inner_text('#tape-total')
    await pg.fill('#m-q', 'gyro'); await pg.wait_for_timeout(150); r['gyro'] = await pg.inner_text('#m-count')
    await pg.fill('#m-q', 'zzzz'); r['emptyMsg'] = await pg.evaluate("!document.querySelector('#m-none').hidden"); await pg.fill('#m-q', '')
    await pg.click('#m-tabs button:nth-child(7)'); r['panel'] = await pg.evaluate("[...document.querySelectorAll('.m-panel')].filter(p=>!p.hidden).length")
FEATS['newport-village-pizza-newport'] = feat_newport
async def feat_exeter(pg, r):
    await pg.click('#m-tabs button:nth-child(2)'); await pg.wait_for_timeout(100); r['panel'] = await pg.evaluate("[...document.querySelectorAll('.m-panel')].filter(p=>!p.hidden).map(p=>p.dataset.p)")
    await pg.click('#mp1 .m-it:nth-child(1) .chip:nth-child(2)'); await pg.click('#mp1 .m-it:nth-child(1) .chip:nth-child(2)'); await pg.click('#mp1 .m-it:nth-child(3) .chip:nth-child(2)')
    r['total'] = await pg.inner_text('#t-total'); r['count'] = await pg.inner_text('#t-count'); r['deals'] = (await pg.inner_text('#t-deals-txt'))[:90]
    r['trayLines'] = await pg.evaluate("document.querySelectorAll('#tray-list li').length")
    fab = await pg.evaluate("getComputedStyle(document.querySelector('#fab')).display!=='none'"); r['fabShown'] = fab
    if fab:
        await pg.click('#fab'); await pg.wait_for_timeout(400); r['sheetOpen'] = await pg.evaluate("document.querySelector('#tray').classList.contains('open')")
    await pg.click('#t-copy'); r['copyLabel'] = await pg.inner_text('#t-copy')
    await pg.click('#t-clear'); r['cleared'] = await pg.evaluate("document.querySelector('#tray-empty').hidden===false")
    await pg.fill('#m-q', 'haddock'); await pg.wait_for_timeout(150); r['haddock'] = await pg.inner_text('#m-count')
    await pg.fill('#m-q', 'zzzz'); r['emptyMsg'] = await pg.evaluate("!document.querySelector('#m-none').hidden"); await pg.fill('#m-q', '')
FEATS['supreme-house-of-pizza-exeter'] = feat_exeter
async def main(slug):
    feat = FEATS[slug]; res = {}
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for src, f in (('preview', ROOT / 'dist' / slug / 'preview.html'), ('site', ROOT / 'dist' / slug / 'site' / 'index.html')):
            for name, vp, mob in (('phone', {'width': 390, 'height': 844}, True), ('desktop', {'width': 1440, 'height': 900}, False)):
                ctx = await b.new_context(viewport=vp, is_mobile=mob, has_touch=mob); pg = await ctx.new_page(); errs = []; failed = []
                pg.on('console', lambda m, e=errs: e.append(m.text) if m.type == 'error' else None); pg.on('pageerror', lambda e, l=errs: l.append(str(e))); pg.on('requestfailed', lambda q, l=failed: l.append(q.url[-60:]))
                await pg.goto(f.as_uri()); await pg.add_style_tag(content='html{scroll-behavior:auto!important}.rv{opacity:1!important;transform:none!important}'); await pg.wait_for_timeout(900)
                H = await pg.evaluate('document.documentElement.scrollHeight')
                for y in range(0, H, 600): await pg.evaluate(f'scrollTo(0,{y})'); await pg.wait_for_timeout(40)
                await pg.evaluate('scrollTo(0,0)'); await pg.wait_for_timeout(300)
                r = await pg.evaluate(CHECK_JS); r['errors'] = errs; r['failedReq'] = failed
                r['fonts'] = await pg.evaluate("[...document.fonts].filter(f=>f.status==='loaded').map(f=>f.family+' '+f.weight)")
                if src == 'preview': await feat(pg, r)
                res[f'{src}-{name}'] = {k: v for k, v in r.items() if v not in ([], 0, '')}
                await ctx.close()
        await b.close()
    print(json.dumps(res, indent=1))
asyncio.run(main(sys.argv[1]))
