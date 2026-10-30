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
FEATS = {'farmington-house-of-pizza': feat_farmington, 'gilford-house-of-pizza': feat_gilford, 'charlestown-house-of-pizza': feat_charlestown, 'uncle-joeys': feat_joeys, 'golden-acres-pizza-market': feat_acres, 'tremont-house-of-pizza': feat_tremont}
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
