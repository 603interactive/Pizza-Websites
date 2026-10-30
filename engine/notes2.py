"""LEAD-NOTES.md for the newer bespoke sites (data.json with findings/questions/usp). usage: notes2.py <slug>..."""
import json, sys, datetime
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
EXTRA = {
 'farmington-house-of-pizza': dict(usp='The Pie Studio: pick Medium or Large and toppings from the real menu (cheese pizza plus $1.00-$2.00 per topping), see the live total, and a tip tells the customer when one of the specialty pizzas (Hawaiian, Meat Lovers, House Special) is cheaper than building it. Prices are the website menu prices.',
   photos=['`pizza-whole.jpg`, `pizza-edge.jpg`, `pizza-slice.jpg`, `tenders.jpg`, `club.jpg`, `sub.jpg`, `salad.jpg` ← https://www.farmingtonhouseofpizza.com/gallery/large/web_6877.jpg (and web_6878, 6887, 6905, 6916, 6929, 6933), the shop\'s own gallery page.'],
   left=['Logo banner `images/logo.jpg`: the shop name is baked into a photo banner with Order/Call buttons, so the new site typesets the name instead.', 'Homepage background photo `images/bg.jpg` and `images/welcome.jpg`: blurred / text graphics.', 'eDiningExpress Google Play and iOS badges.']),
 'gilford-house-of-pizza': dict(usp='The Delivery Desk: the customer enters their order and what a delivery app added in fees last time; the page shows the all-in GHOP total (food + 8.5% tax + flat $4) and the fees kept. Built from the shop\'s own claim: $4 delivery to Gilford and Laconia, drivers paid by the shop, no DoorDash/Uber fees. Also a season-aware hours card (fall/winter vs spring/summer).',
   photos=['`logo.jpg` ← https://irp.cdn-website.com/9dc28497/dms3rep/multi/GHOP+Logo.JPG', '`pizza, gourmet, calzones, subs, steak, dinners, pasta, salads, sides, desserts, chips .jpg` ← the 11 menu category tiles on https://www.gilfordhouseofpizza.com/menu (files PIZZA-6, GREEK_PIZZA1, CALZONE2, TURKEY-SUB2, STEAK-SUB-PHILLY, WING-DING-DINNER, SPAGHETTI-MEATBALLS, SALAD, ONION-RINGS, BAKLAVA, CHIPS under irp.cdn-website.com/9dc28497/dms3rep/multi/).'],
   left=['`Drinks.JPG` category tile (merged into the Drinks & Chips section, which uses the chips tile).', 'Nextdoor badge.', 'Note: the tiles have the category name printed into the image, so they are used as-is as menu buttons. They look like stock-style photos; the owner should confirm they are the shop\'s own.']),
}
def notes(slug):
    d = json.load(open(ROOT / 'clients' / slug / 'data.json')); x = EXTRA[slug]
    L = [f"# {d['name']}: redesign concept", '', f"Built {datetime.date.today():%b %d, %Y} by 603 Interactive from the shop's own content only. No AI-generated or stock food photos.", '',
         '## Files', '', '- `preview.html`: the whole site in one file, with a "design concept" ribbon. Open it in any browser to show the owner.',
         f"- `site/`: the launch-ready site (no ribbon). Drag the folder onto app.netlify.com/drop.", '', '## What we found on the current site', ''] + [f'- {f}' for f in d['findings']] + [
         '', '## The one big idea', '', x['usp'], '', '## What else the new site does', '',
         '- Live open / closed status and today\'s hours, address, phone and directions.', '- Full menu with prices, category tabs and search, readable on a phone.',
         '- Sticky call / order bar on phones, parallax hero, Restaurant structured data, sitemap and robots.txt.', '',
         '## Questions for the owner before launch', ''] + [f'{i}. {q}' for i, q in enumerate(d['questions'], 1)] + [
         '', '## Photo sources', ''] + [f'- {p}' for p in x['photos']] + ['', 'Left out on purpose:', ''] + [f'- {p}' for p in x['left']] + [
         '', 'Fonts are open-license (SIL OFL); licence files ship in `assets/fonts/`.', '', '## Not checked yet', '',
         '- Real phones (iPhone Safari, Android Chrome) and a screen reader pass.', '- Lighthouse scores on the hosted site.', '- Placing an order: no order was placed.',
         '', '## Launch steps', '', '1. Get answers to the questions above and update `clients/' + slug + '/data.json`, then rebuild with `python3 engine/build_' + slug.split('-')[0] + '.py`.',
         '2. Drag `site/` onto Netlify Drop for a staging link; check it on a phone.', '3. Point the shop\'s domain at Netlify (owner\'s domain account needed).',
         '4. Submit `sitemap.xml` in Google Search Console and update the Google Business Profile website link.']
    (ROOT / 'dist' / slug / 'LEAD-NOTES.md').write_text('\n'.join(L) + '\n')
for s in sys.argv[1:]: notes(s); print('notes', s)
