import json, asyncio, re
from pathlib import Path
from playwright.async_api import async_playwright
ROOT = Path(__file__).resolve().parent.parent; S = Path('/tmp/claude-0/-home-claude-pizza-websites/34ac2a61-0ac1-5107-9f15-4ac07a7c0d5a/scratchpad')
async def main():
    res = {}
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for src, f in (('preview', ROOT / 'dist/pizza-haven-rindge/preview.html'), ('site', ROOT / 'dist/pizza-haven-rindge/site/index.html')):
            for name, vp, mob in (('phone', {'width': 390, 'height': 844}, True), ('desktop', {'width': 1440, 'height': 900}, False)):
                ctx = await b.new_context(viewport=vp, is_mobile=mob, has_touch=mob); pg = await ctx.new_page(); errs = []; failed = []
                pg.on('console', lambda m, e=errs: e.append(m.text) if m.type == 'error' else None); pg.on('pageerror', lambda e, l=errs: l.append(str(e))); pg.on('requestfailed', lambda q, l=failed: l.append(q.url[-60:]))
                await pg.goto(f.as_uri()); await pg.wait_for_timeout(600)
                H = await pg.evaluate('document.documentElement.scrollHeight')
                for y in range(0, H, 500): await pg.evaluate(f'scrollTo(0,{y})'); await pg.wait_for_timeout(30)
                await pg.evaluate('scrollTo(0,0)')
                r = dict(errors=errs, failed=failed)
                r['overflowX'] = await pg.evaluate('document.documentElement.scrollWidth-innerWidth')
                r['badImgs'] = await pg.evaluate("[...document.images].filter(i=>!i.complete||i.naturalWidth===0).map(i=>i.src.slice(-40))")
                r['noAlt'] = await pg.evaluate("[...document.images].filter(i=>!i.hasAttribute('alt')).length")
                r['wideEls'] = await pg.evaluate("[...document.querySelectorAll('body *')].filter(e=>{const b=e.getBoundingClientRect();return b.width>0&&b.right>innerWidth+1&&!e.closest('.m-tabs,.ring,.hero-pics,.tix-c')}).slice(0,5).map(e=>e.tagName+'.'+e.className)")
                r['links'] = await pg.evaluate("[...document.querySelectorAll('a[href^=\"#\"]')].filter(a=>a.getAttribute('href').length>1&&!document.querySelector(a.getAttribute('href'))).map(a=>a.href)")
                if src == 'preview':
                    r['cards'] = await pg.evaluate("document.querySelectorAll('.pf-card').length")
                    await pg.click('#pf-chips button[data-f=chicken]'); r['chicken'] = await pg.inner_text('#pf-count')
                    await pg.click('#pf-chips button[data-f=wild]'); r['wild'] = await pg.inner_text('#pf-count')
                    await pg.click('#pf-surprise'); r['spot'] = [await pg.inner_text('#sp-name'), await pg.inner_text('#sp-price'), await pg.inner_text('#sp-calz')]
                    r['pickInWild'] = await pg.evaluate("document.querySelectorAll('.pf-card.pick:not([hidden])').length")
                    await pg.click('#pf-chips button[data-f=all]'); r['all'] = await pg.inner_text('#pf-count')
                    await pg.click('#m-tabs button:nth-child(3)'); r['panel'] = await pg.evaluate("[...document.querySelectorAll('.m-panel')].filter(p=>!p.hidden).map(p=>p.getAttribute('aria-label'))")
                    await pg.fill('#m-q', 'gyro'); await pg.wait_for_timeout(100); r['gyro'] = await pg.inner_text('#m-count')
                    await pg.fill('#m-q', 'zzzz'); r['none'] = await pg.evaluate("!document.querySelector('#m-none').hidden"); await pg.fill('#m-q', '')
                    r['status'] = await pg.inner_text('[data-status]')
                    await pg.screenshot(path=str(S / f'ph-{name}.png'), full_page=True)
                res[f'{src}-{name}'] = r; await ctx.close()
        await b.close()
    print(json.dumps(res, indent=1))
asyncio.run(main())
