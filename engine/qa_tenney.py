import sys, re, json
from pathlib import Path
from playwright.sync_api import sync_playwright
D = Path('/home/claude/pizza-websites/dist/tenney-mtn-pizza-plymouth'); res = []
with sync_playwright() as p:
    b = p.chromium.launch()
    for name, f in (('site', D / 'site' / 'index.html'), ('preview', D / 'preview.html')):
        for w, h in ((390, 844), (1440, 900)):
            pg = b.new_page(viewport=dict(width=w, height=h)); errs = []
            pg.on('console', lambda m: errs.append(m.text) if m.type == 'error' else None); pg.on('pageerror', lambda e: errs.append(str(e)))
            pg.goto(f.as_uri()); pg.wait_for_load_state('load')
            ov = pg.evaluate('document.documentElement.scrollWidth-innerWidth')
            for y in range(0, 30000, 600): pg.evaluate(f'scrollTo(0,{y})'); pg.wait_for_timeout(40)
            pg.wait_for_timeout(800); broken = pg.evaluate('[...document.images].filter(i=>!i.complete||!i.naturalWidth).map(i=>i.src.slice(-40))')
            small = pg.evaluate('[...document.querySelectorAll("a,button,input[type=search],input[type=text]")].filter(e=>{const r=e.getBoundingClientRect();return r.width&&r.height&&(r.height<40)&&getComputedStyle(e).position!=="absolute"&&!e.closest(".sr")}).map(e=>e.textContent.trim().slice(0,20)).slice(0,10)')
            # feature tests
            pg.evaluate('localStorage.clear()'); pg.reload(); pg.wait_for_load_state('load')
            pg.fill('#m-q', 'feta'); n = pg.locator('.m-it:visible').count()
            pg.fill('#m-q', 'zzzz'); none = pg.locator('#m-none').is_visible()
            pg.fill('#m-q', '')
            pg.click('#m-tabs button:has-text("Calzones")'); calz = pg.locator('.m-cat:visible').count()
            pg.click('#m-tabs button:has-text("All")')
            pg.eval_on_selector('input[value="1"][name=size]','e=>e.click()'); pg.eval_on_selector('input[name=kind][value="2"]','e=>e.click()')
            pg.eval_on_selector('input[name=top][value=pepperoni]','e=>e.click()'); pg.eval_on_selector('input[name=top][value=onion]','e=>e.click()')
            third = pg.locator('input[name=top][value=olive]').is_disabled()
            pg.eval_on_selector('input[name=sauce][value=white]','e=>e.click()'); pg.click('#b-add'); 
            pg.locator('[data-add][data-name="Greek"]').first.click()
            pg.locator('[data-add][data-name="Cheeseburger"]').first.click()
            lines = pg.locator('#sh-lines li').count(); addon = pg.locator('#sh-addons').inner_text(); sheet = pg.locator('#sh-lines').inner_text()
            pg.reload(); pg.wait_for_load_state('load'); persisted = pg.locator('#sh-lines li').count()
            pg.screenshot(path=f'/tmp/claude-0/-home-claude-pizza-websites/34ac2a61-0ac1-5107-9f15-4ac07a7c0d5a/scratchpad/t-{name}-{w}.png', full_page=True)
            res.append(dict(page=name, w=w, overflow=ov, errs=errs, broken=broken, small=small, feta=n, none=none, calz_cats=calz, third_disabled=third, lines=lines, addon=addon, persisted=persisted))
            pg.close()
    b.close()
for r in res: print(json.dumps(r))
