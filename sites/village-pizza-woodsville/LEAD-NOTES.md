# Village Pizza Woodsville: redesign concept

Built Nov 11, 2026 by 603 Interactive. No AI-generated or stock food photos, and no photos at all in this concept (see Image rights).

## Files

- `preview.html`: the whole site in one file, with a "design concept" ribbon.
- `site/`: the launch-ready site (no ribbon). Drag the folder onto app.netlify.com/drop.

## What we found on the current site

- Generic FoodTec ordering template; the slider uses stock photos (file names still show: pizza-1344720_960_720, america-1238743_1920, salad-g21ef69fd2_1280), so none were used.
- Tagline is vague ("The best pizza experience in town"); replaced with plain, factual wording.
- Testimonials block is empty ("There are no featured comments yet").
- Footer address is only "Central St, Haverhill" with no street number; 179 Central St, Woodsville, NH 03785 comes from the lead research.
- No social links anywhere on the site; only an unofficial auto-generated Facebook page exists, which is not linked.
- Ordering link is the FoodTec page listed on the shop's site; it was not tested by placing an order.

## What the new site does

- Shared `plain` template (engine/templates/plain.*) with a red/green palette chosen by us (the shop's own branding was not retrieved); built by `engine/build_villagepizzawoodsville.py` from `clients/village-pizza-woodsville/data.json`.
- Order online button links to the shop's own ordering page: https://village-woodsville.foodtecsolutions.com (not tested by placing an order).
- Directions link, tap-to-call (603) 747-8111, sticky call bar on phones.
- No menu, hours or reviews are shown: none could be read (see Content gaps). The menu section points to the ordering page and phone.
- Restaurant structured data without price range or opening hours.

## Content gaps

The shop's own pages (homepage, /menu/, FoodTec ordering page) could not be fetched when this was built (fetch permission was not granted), so only facts from the lead file were used. Copy is limited to name, address, phone and ordering link. The Hours section's "not published" wording is template text; confirm it is true. Before launch, someone should read the live menu, hours and about text and add them.

## Image rights

No photos are published. The current site uses stock photos and none of the shop's own photos were retrieved, so reuse permission is unknown. Get the owner's OK and send full-size food/shop photos before launch; the layout adds a gallery when images are supplied.

## Questions for the owner before launch

1. Do you have photos of your food and shop we may use? The current site shows only stock photos.
2. Can you send your menu with prices and hours? The new site links to your ordering page and shows no hours.
3. Is the FoodTec link the right ordering page?
4. What email address should customers use?
5. Do you have Facebook, Instagram or other social pages to link?
6. Do you offer delivery?

Fonts are open-license (SIL OFL); licence files ship in `assets/fonts/`.

## Not checked yet

- Real phones (iPhone Safari, Android Chrome) and a screen reader pass.
- Lighthouse scores on the hosted site.
- Placing an order: no order was placed.
- Menu, hours and copy were not read from the shop's pages; address, phone and links come from the lead file (Nov 10, 2026).
