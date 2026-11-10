"""LEAD-NOTES.md + copy to sites/<slug>/ for the plainshop sites. usage: notes_batch.py <slug>..."""
import json, sys, shutil, datetime
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
for slug in sys.argv[1:]:
    d = json.load(open(ROOT / 'clients' / slug / 'data.json')); out = ROOT / 'dist' / slug; today = datetime.date.today()
    L = [f"# {d['name']}: redesign concept", '', f"Built {today:%b %d, %Y} by 603 Interactive from the shop's own public site text only. No AI-generated or stock food photos, and no photos at all in this concept (see Image rights).", '',
         '## Files', '', '- `preview.html`: the whole site in one file, with a "design concept" ribbon.', '- `site/`: the launch-ready site (no ribbon). Drag the folder onto app.netlify.com/drop.', '',
         '## What we found on the current site', ''] + [f'- {f}' for f in d['findings']] + ['', '## What the new site does', '',
         '- Live text menu with category tabs and search (where a menu was published), live open/closed status and today\'s hours (where hours were published), directions and a sticky call bar on phones.',
         '- Shared `plain` template (engine/templates/plain.*) with this shop\'s own palette; built by `engine/build_plainshop.py` from `clients/' + slug + '/data.json`.',
         '- ' + ('Online ordering links to the shop\'s own ordering page: ' + d['order_url'] + ' (not tested by placing an order).' if d['order_url'] else 'Phone ordering only: no ordering link could be verified, so none was invented.'),
         '- Restaurant structured data without price range' + ('' if d['order_url'] else ' or OrderAction') + '.', '',
         '## Image rights', '', 'No photos are published. None of the shop\'s own photos could be retrieved and confirmed as the shop\'s, and reuse permission is unknown for all of them. Get the owner\'s OK and send full-size food/shop photos before launch; the layout adds a gallery when images are supplied.', '',
         '## Questions for the owner before launch', ''] + [f'{i}. {q}' for i, q in enumerate(d['questions'], 1)] + ['', 'Fonts are open-license (SIL OFL); licence files ship in `assets/fonts/`.', '',
         '## Not checked yet', '', '- Real phones (iPhone Safari, Android Chrome) and a screen reader pass.', '- Lighthouse scores on the hosted site.', '- Placing an order: no order was placed.', '- Menu and hours were read from the shop\'s public pages on ' + f'{today:%b %d, %Y}' + ' and may have changed.']
    (out / 'LEAD-NOTES.md').write_text('\n'.join(L) + '\n')
    dst = ROOT / 'sites' / slug
    if dst.exists(): sys.exit(f'refusing to overwrite {dst}')
    dst.mkdir(parents=True); shutil.copytree(out / 'site', dst / 'site'); shutil.copy(out / 'preview.html', dst / 'preview.html'); shutil.copy(out / 'LEAD-NOTES.md', dst / 'LEAD-NOTES.md'); print('copied', slug)
