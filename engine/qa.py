"""Automated checks + screenshots for a built site. usage: qa.py <slug>"""
import sys, json, asyncio
from pathlib import Path
from playwright.async_api import async_playwright
ROOT = Path('/home/claude/pizza-sites')
CHECK_JS = r"""
() => {
  const out = {};
  const de = document.documentElement;
  out.overflowX = de.scrollWidth - de.clientWidth;
  out.wide = [...document.querySelectorAll('body *')].filter(e => { const r = e.getBoundingClientRect(); return r.right > de.clientWidth + 1 && getComputedStyle(e).position !== 'fixed' && !e.closest('.fav-track,.chips,.ticker,.hero-fx,.fav') }).slice(0, 8).map(e => e.tagName + '.' + e.className + ' ' + Math.round(e.getBoundingClientRect().right));
  out.brokenImgs = [...document.images].filter(i => i.complete && i.naturalWidth === 0).map(i => i.src.slice(0, 60));
  const lum = c => { const m = c.match(/[\d.]+/g).map(Number); const f = v => { v /= 255; return v <= .03928 ? v / 12.92 : ((v + .055) / 1.055) ** 2.4 }; return .2126 * f(m[0]) + .7152 * f(m[1]) + .0722 * f(m[2]) };
  const bgOf = e => { while (e) { const b = getComputedStyle(e).backgroundColor; if (b && !b.startsWith('rgba(0, 0, 0, 0)') && b !== 'transparent') { const a = b.match(/[\d.]+/g); if (a.length < 4 || +a[3] > .85) return b; } e = e.parentElement } return 'rgb(17,12,10)' };
  const fails = [];
  document.querySelectorAll('p,span,a,h1,h2,h3,h4,label,legend,td,b,small,button,li,em,address').forEach(e => {
    if (!e.childNodes.length || ![...e.childNodes].some(n => n.nodeType === 3 && n.textContent.trim())) return;
    const r = e.getBoundingClientRect(); if (!r.width || e.closest('.hero,.ticker,.concept,[hidden],.sr')) return;
    const cs = getComputedStyle(e); const fg = cs.color; const bg = bgOf(e);
    const L1 = lum(fg), L2 = lum(bg); const ratio = (Math.max(L1, L2) + .05) / (Math.min(L1, L2) + .05);
    const size = parseFloat(cs.fontSize), bold = +cs.fontWeight >= 700; const need = (size >= 24 || (bold && size >= 18.66)) ? 3 : 4.5;
    if (ratio < need) fails.push(`${e.tagName} "${e.textContent.trim().slice(0, 30)}" ${ratio.toFixed(2)} need ${need} (${fg} on ${bg})`);
  });
  out.contrast = [...new Set(fails)].slice(0, 15);
  out.headings = [...document.querySelectorAll('h1,h2,h3')].map(h => h.tagName).join('');
  out.h1 = document.querySelectorAll('h1').length;
  out.smallTaps = [...document.querySelectorAll('a,button,input,select')].filter(e => { const r = e.getBoundingClientRect(); return r.width && r.height && r.height < 40 && !e.closest('.foot,.sr,.skip,.chips') && e.type !== 'checkbox' }).slice(0, 10).map(e => e.tagName + ' ' + (e.textContent || e.name || '').trim().slice(0, 20) + ' ' + Math.round(e.getBoundingClientRect().height));
  out.emptyLinks = [...document.querySelectorAll('a')].filter(a => !a.textContent.trim() && !a.getAttribute('aria-label') && !a.querySelector('img[alt]')).length;
  return out;
}"""
async def main(slug):
    f = ROOT / 'dist' / slug / 'preview.html'; outd = ROOT / 'qa' / slug; outd.mkdir(parents=True, exist_ok=True)
    async with async_playwright() as p:
        b = await p.chromium.launch(executable_path='/opt/pw-browsers/chromium-1243/chrome-linux64/chrome')
        res = {}
        for name, vp, mobile in [('phone', {'width': 390, 'height': 844}, True), ('desktop', {'width': 1440, 'height': 900}, False)]:
            ctx = await b.new_context(viewport=vp, device_scale_factor=1, is_mobile=mobile, has_touch=mobile)
            pg = await ctx.new_page(); errs = []
            pg.on('console', lambda m, errs=errs: errs.append(m.text) if m.type == 'error' else None)
            pg.on('pageerror', lambda e, errs=errs: errs.append(str(e)))
            await pg.goto(f.as_uri()); await pg.add_style_tag(content='html{scroll-behavior:auto!important}'); await pg.wait_for_timeout(1500)
            await pg.screenshot(path=str(outd / f'{name}-top.png'))
            r = await pg.evaluate(CHECK_JS); r['errors'] = errs; res[name] = r
            # scroll through for sections
            H = await pg.evaluate('document.documentElement.scrollHeight')
            for sel in ['#favorites', '#deals', '#menu', '#locations', '#careers', '#about', '.foot']:
                if await pg.query_selector(sel):
                    await pg.evaluate(f"document.querySelector('{sel}').scrollIntoView({{block:'start',behavior:'instant'}})"); await pg.wait_for_timeout(500)
                    await pg.screenshot(path=str(outd / f"{name}-{sel.strip('#.')}.png"))
            if name == 'desktop':
                await pg.evaluate("document.querySelector('#favorites').scrollIntoView()"); await pg.evaluate("scrollBy(0, 900)"); await pg.wait_for_timeout(400)
                await pg.screenshot(path=str(outd / 'desktop-fav-scrolled.png'))
            # search + chooser
            await pg.evaluate("document.querySelector('#menu').scrollIntoView()")
            await pg.fill('#menu-search', 'chicken'); await pg.wait_for_timeout(300)
            res[name]['searchVisible'] = await pg.evaluate("[...document.querySelectorAll('[data-item]')].filter(e=>!e.classList.contains('hide')).length")
            await pg.fill('#menu-search', 'zzzz'); await pg.wait_for_timeout(200)
            res[name]['emptyShown'] = await pg.evaluate("getComputedStyle(document.querySelector('#menu-empty')).display")
            await pg.fill('#menu-search', '')
            if await pg.query_selector('[data-order]'):
                await pg.evaluate("scrollTo(0,0)"); await pg.wait_for_timeout(200)
                await pg.click('.hero [data-order]'); await pg.wait_for_timeout(500)
                await pg.screenshot(path=str(outd / f'{name}-order-sheet.png'))
                res[name]['sheetOpen'] = await pg.evaluate("!document.querySelector('#order-sheet').hidden")
                await pg.keyboard.press('Escape'); await pg.wait_for_timeout(400)
            res[name]['height'] = H
            await ctx.close()
        await b.close()
    print(json.dumps(res, indent=1))
asyncio.run(main(sys.argv[1]))
