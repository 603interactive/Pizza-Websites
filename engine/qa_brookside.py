"""QA for brookside: overflow, console errors, broken imgs/links, Day Dial + menu features. usage: qa_brookside.py"""
import asyncio, json, http.server, threading, functools
from pathlib import Path
from playwright.async_api import async_playwright
ROOT = Path(__file__).resolve().parent.parent; SLUG = 'brookside-pizza-ii-belmont'; OUT = ROOT / 'dist' / SLUG
def serve(root):
    h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(root))
    class Q(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a): pass
    h = functools.partial(Q, directory=str(root)); h.log_message = lambda *a: None
    s = http.server.ThreadingHTTPServer(('127.0.0.1', 0), h); threading.Thread(target=s.serve_forever, daemon=True).start(); return s
async def main():
    s = serve(OUT / 'site'); port = s.server_address[1]; res = {}
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for label, url in (('site', f'http://127.0.0.1:{port}/index.html'), ('preview', (OUT / 'preview.html').as_uri())):
            for w, h in ((390, 844), (1440, 900)):
                ctx = await b.new_context(viewport={'width': w, 'height': h}); pg = await ctx.new_page(); errs = []
                pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' else None); pg.on('pageerror', lambda e: errs.append(str(e)))
                bad = []; pg.on('response', lambda r: bad.append(r.url) if r.status >= 400 else None)
                await pg.clock.install(time='2026-11-04T15:00:00Z')  # Wed 10:00 AM ET
                await pg.goto(url); await pg.wait_for_timeout(500)
                r = {}
                r['overflow'] = await pg.evaluate("document.documentElement.scrollWidth - innerWidth")
                await pg.evaluate("document.querySelectorAll('img').forEach(i=>i.loading='eager')"); await pg.wait_for_timeout(800)
                r['brokenImgs'] = await pg.evaluate("[...document.images].filter(i=>!i.complete||!i.naturalWidth).map(i=>i.src.slice(0,60))")
                r['noAlt'] = await pg.evaluate("[...document.images].filter(i=>!i.hasAttribute('alt')).length")
                r['status'] = await pg.inner_text('.eyebrow')
                r['now'] = await pg.inner_text('#now')
                await pg.click('#days button[data-d="5"]'); r['fri'] = await pg.inner_text('#now'); r['kitchenFri'] = await pg.inner_text('[data-lane=kitchen] [data-t]')
                r['nowlineHiddenFri'] = await pg.evaluate("document.querySelector('#nowline').hidden")
                await pg.click('#days button[data-d="3"]'); r['nowlineShownToday'] = not await pg.evaluate("document.querySelector('#nowline').hidden")
                r['barW'] = await pg.evaluate("document.querySelector('[data-lane=bar] .bar').style.width")
                await pg.fill('#m-q', 'gyro'); r['gyro'] = await pg.inner_text('#m-count'); await pg.fill('#m-q', 'zzzz'); r['none'] = await pg.evaluate("!document.querySelector('#m-none').hidden"); await pg.fill('#m-q', '')
                await pg.click('#m-tabs button:nth-child(8)'); r['subsVisible'] = await pg.evaluate("[...document.querySelectorAll('.m-panel')].filter(p=>!p.hidden).length")
                r['mItems'] = await pg.evaluate("document.querySelectorAll('.m-it').length")
                hrefs = await pg.evaluate("[...document.querySelectorAll('a[href^=\"#\"]')].map(a=>a.getAttribute('href'))")
                r['badAnchors'] = [x for x in hrefs if x != '#' and not await pg.evaluate("(x)=>!!document.querySelector(x)", x)]
                r['errors'] = errs; r['http400'] = bad
                await pg.screenshot(path=f'/tmp/claude-0/-home-claude-pizza-websites/34ac2a61-0ac1-5107-9f15-4ac07a7c0d5a/scratchpad/brk/{label}-{w}.png', full_page=True)
                res[f'{label}-{w}'] = r; await ctx.close()
        await b.close()
    print(json.dumps(res, indent=1)); s.shutdown()
asyncio.run(main())
