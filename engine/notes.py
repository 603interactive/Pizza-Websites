"""Write the per-lead handoff notes (findings, questions, photo sources, launch steps)."""
import json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
def notes(slug):
    d = json.load(open(ROOT / 'clients' / slug / 'data.json'))
    m = json.load(open(ROOT / 'clients' / slug / 'img' / '_map.json'))
    L = [f"# {d['name']}: redesign concept", '',
         f"Built {__import__('datetime').date.today():%b %d, %Y} by 603 Interactive from the shop's own content only. No AI-generated or stock food photos.", '',
         '## Files', '',
         '- `preview.html`: the whole site in one file, with a "design concept" ribbon. Open it in any browser to show the owner.',
         f"- `{slug}-netlify-site.zip`: the launch-ready site (no ribbon). Unzip and drag the folder onto app.netlify.com/drop.",
         '', '## What we found on the current site', ''] + [f'- {x}' for x in d['findings']] + [
         '', '## What the new site does about it', '',
         '- Order button in the header, the hero, the menu and a sticky phone bar, linking straight into the shop\'s existing online ordering' + (' (with a Hudson / Derry picker)' if len(d['locations']) > 1 else '') + '.',
         '- Live open / closed status and today\'s hours for each shop, address, phone and directions.',
         '- Full menu with photos, size prices, category tabs and search, readable on a phone.',
         ] + (['- Combo deals shown on every screen size, with an Order this deal button.'] if d.get('deals') else []) + (
         ['- A real job application form (Netlify Forms) replacing the "Coming Soon" page.'] if d.get('careers', {}).get('enabled') else []) + [
         '- Search-engine basics: page title and description, Restaurant structured data, sitemap and robots.txt.',
         '', '## Questions for the owner before launch', ''] + [f'{i}. {q}' for i, q in enumerate(d['questions'], 1)] + [
         '', '## Photo sources', '',
         'Every photo is the shop\'s own, taken from its current website or its online-ordering menu, then re-saved for the web.', '']
    base = d.get('img_base', '')
    L.append(f"- `hero.jpg` ← {d['hero']['img'].split('/v1/')[0]}"); L.append(f"- `logo.webp` ← {d['logo']['src'].split('/v1/')[0]}")
    for k, v in m['map'].items(): L.append(f'- `{v}` ← {base}{k}')
    if m.get('excluded'):
        L += ['', 'Left out on purpose:', ''] + [f'- {base}{k}: {why}' for k, why in m['excluded'].items()]
    L += ['', 'Fonts are open-license (SIL OFL); the licence files ship in `assets/fonts/`.',
          '', '## Not checked yet', '',
          '- Real phones (iPhone Safari, Android Chrome) and a screen reader pass.',
          '- Lighthouse scores on the hosted site.',
          '- Placing an order: the Order links were opened, but no order was placed.',
          ] + (['- A test job application on the live Netlify site (Forms must be enabled on the Netlify project).'] if d.get('careers', {}).get('enabled') else []) + [
          '', '## Launch steps', '',
          '1. Get answers to the questions above and update `clients/' + slug + '/data.json`, then rebuild with `python3 engine/build.py ' + slug + '`.',
          '2. Drag the site folder onto Netlify Drop to get a staging link; check it on a phone.',
          '3. Point the shop\'s domain at Netlify (the owner\'s domain account is needed).',
          '4. Submit `sitemap.xml` in Google Search Console and update the Google Business Profile website link.']
    (ROOT / 'dist' / slug / 'LEAD-NOTES.md').write_text('\n'.join(L) + '\n')
for s in sys.argv[1:]: notes(s); print('notes', s)
