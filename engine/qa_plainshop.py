"""QA for plainshop sites: generic checks (qa.py CHECK_JS) at 390px and 1440px on preview and site; tabs/search/links; screenshots to dist/<slug>/qa/. usage: qa_plainshop.py <slug>"""
import sys, json, asyncio, re
from pathlib import Path
from playwright.async_api import async_playwright
ROOT = Path(__file__).resolve().parent.parent
CHECK_JS = re.search(r'CHECK_JS = r"""(.*?)"""', (ROOT / 'engine' / 'qa.py').read_text(), re.S).group(1).replace(".closest('.hero,.ticker,.concept,[hidden],.sr')", ".closest('[hidden],.sr,.ribbon,svg')")
async def main(slug):
    res = {}; (ROOT / 'dist' / slug / 'qa').mkdir(exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for src, f in (('preview', ROOT / 'dist' / slug / 'preview.html'), ('site', ROOT / 'dist' / slug / 'site' / 'index.html')):
            for name, vp, mob in (('phone', {'width': 390, 'height': 844}, True), ('desktop', {'width': 1440, 'height': 900}, False)):
                ctx = await b.new_context(viewport=vp, is_mobile=mob, has_touch=mob); pg = await ctx.new_page(); errs = []; failed = []
                pg.on('console', lambda m, e=errs: e.append(m.text) if m.type == 'error' else None); pg.on('pageerror', lambda e, l=errs: l.append(str(e))); pg.on('requestfailed', lambda q, l=failed: l.append(q.url[-60:]))
                await pg.goto(f.as_uri()); await pg.wait_for_timeout(700)
                r = await pg.evaluate(CHECK_JS); r['errors'] = errs; r['failedReq'] = failed
                r['hscroll'] = await pg.evaluate('document.documentElement.scrollWidth>innerWidth')
                r['status'] = await pg.inner_text('#status')
                if await pg.query_selector('#q'):
                    n = len(await pg.query_selector_all('.tabs button')); await pg.click(f'.tabs button:nth-child({n})' if n > 1 else '.tabs button')
                    r['tabsOk'] = await pg.evaluate("[...document.querySelectorAll('.panel')].filter(p=>!p.hidden).length")
                    await pg.fill('#q', 'chicken'); r['chickenMatches'] = await pg.evaluate("[...document.querySelectorAll('.items li')].filter(l=>!l.hidden).length")
                    await pg.fill('#q', 'zzzz'); r['emptyMsg'] = await pg.evaluate("!document.querySelector('#none').hidden"); await pg.fill('#q', '')
                if mob:
                    await pg.click('.burger'); r['navOpen'] = await pg.evaluate("document.querySelector('#nav').classList.contains('open')")
                    await pg.click('.burger')
                r['links'] = await pg.evaluate("[...new Set([...document.querySelectorAll('a[href]')].map(a=>a.getAttribute('href')))].filter(h=>!h.startsWith('#')&&!h.startsWith('tel:')&&!h.startsWith('assets/'))")
                bad = await pg.evaluate("[...document.querySelectorAll('a[href^=\"#\"]')].map(a=>a.getAttribute('href')).filter(h=>h.length>1&&!document.querySelector(h))"); r['brokenAnchors'] = bad
                if src == 'site':
                    await pg.evaluate('scrollTo(0,0)'); await pg.screenshot(path=str(ROOT / 'dist' / slug / 'qa' / f'{name}-top.png'))
                    await pg.screenshot(path=str(ROOT / 'dist' / slug / 'qa' / f'{name}-full.png'), full_page=True)
                res[f'{src}-{name}'] = {k: v for k, v in r.items() if v not in ([], 0, '', False)}
                await ctx.close()
        await b.close()
    print(json.dumps(res, indent=1))
asyncio.run(main(sys.argv[1]))
