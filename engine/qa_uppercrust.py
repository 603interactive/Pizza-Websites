import asyncio, json
from pathlib import Path
from playwright.async_api import async_playwright
ROOT = Path(__file__).resolve().parent.parent
async def run():
    async with async_playwright() as p:
        b = await p.chromium.launch(); res = {}
        for name, url in (('preview', (ROOT/'dist/upper-crust-pizzeria-tilton/preview.html').as_uri()), ('site', (ROOT/'dist/upper-crust-pizzeria-tilton/site/index.html').as_uri())):
            for w, h in ((390, 844), (1440, 900)):
                pg = await b.new_page(viewport={'width': w, 'height': h}); errs = []
                pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' else None); pg.on('pageerror', lambda e: errs.append(str(e)))
                await pg.goto(url); await pg.wait_for_timeout(500)
                r = {'errs': errs}
                r['overflow'] = await pg.evaluate("document.documentElement.scrollWidth-innerWidth")
                r['broken'] = await pg.evaluate("[...document.images].filter(i=>i.complete&&!i.naturalWidth).map(i=>i.src.slice(-40))")
                r['noalt'] = await pg.evaluate("[...document.images].filter(i=>i.getAttribute('alt')===null).length")
                r['links'] = await pg.evaluate("[...document.querySelectorAll('a[href]')].filter(a=>{const h=a.getAttribute('href');return h.startsWith('#')&&!document.querySelector(h)}).map(a=>a.getAttribute('href'))")
                if w == 390:
                    await pg.click('.burger'); r['navOpen'] = await pg.evaluate("getComputedStyle(document.querySelector('#nav')).display"); await pg.click('#nav a[href=\"#menu\"]'); r['navClosed'] = await pg.evaluate("getComputedStyle(document.querySelector('#nav')).display")
                # slider test
                await pg.evaluate("(()=>{const r=document.querySelector('#wb-range');r.value=900;r.dispatchEvent(new Event('input'))})()")
                r['say15'] = await pg.inner_text('#wb-say'); r['on15'] = await pg.evaluate("[...document.querySelectorAll('.wb-row.on')].map(x=>x.dataset.dow)")
                await pg.evaluate("(()=>{const r=document.querySelector('#wb-range');r.value=1080;r.dispatchEvent(new Event('input'))})()")
                r['on18'] = await pg.evaluate("[...document.querySelectorAll('.wb-row.on')].map(x=>x.dataset.dow)")
                await pg.fill('#m-q', 'steak'); r['steak'] = await pg.inner_text('#m-count'); await pg.fill('#m-q', 'zzzz'); r['none'] = await pg.evaluate("!document.querySelector('#m-none').hidden"); await pg.fill('#m-q', '')
                await pg.click('#m-tabs button:nth-child(4)'); r['tab4'] = await pg.evaluate("[...document.querySelectorAll('.m-panel')].filter(p=>!p.hidden).length")
                await pg.evaluate("window.scrollTo(0,0)")
                if name == 'preview':
                    await pg.screenshot(path=f'/tmp/claude-0/-home-claude-pizza-websites/34ac2a61-0ac1-5107-9f15-4ac07a7c0d5a/scratchpad/uc{w}.png', full_page=True)
                res[f'{name}{w}'] = r; await pg.close()
        # status logic w/ mocked clocks
        for iso, lab in (('2026-11-04T18:00:00-05:00','wed6pm'),('2026-11-04T15:00:00-05:00','wed3pm'),('2026-11-02T13:00:00-05:00','mon1pm'),('2026-11-03T17:00:00-05:00','tue5pm'),('2026-11-08T20:30:00-05:00','sun830')):
            ctx = await b.new_context(); pg = await ctx.new_page()
            await pg.add_init_script("(()=>{const D=Date,t=new D('%s').getTime();Date=class extends D{constructor(...a){a.length?super(...a):super(t)}static now(){return t}}})()" % iso)
            await pg.goto((ROOT/'dist/upper-crust-pizzeria-tilton/site/index.html').as_uri()); await pg.wait_for_timeout(300)
            res[lab] = await pg.inner_text('[data-status]'); await ctx.close()
        await b.close()
    print(json.dumps(res, indent=1))
asyncio.run(run())
