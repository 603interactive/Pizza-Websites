# Fire 21 Pizza: redesign concept

Built Nov 10, 2026 by 603 Interactive from the shop's own public site text only. No AI-generated or stock food photos, and no photos at all in this concept (see Image rights).

## Files

- `preview.html`: the whole site in one file, with a "design concept" ribbon.
- `site/`: the launch-ready site (no ribbon). Drag the folder onto app.netlify.com/drop.

## What we found on the current site

- Old Yahoo/Turbify builder page: name, phone, address and a map on the homepage, plus an About page.
- No menu, no hours and no online ordering are published anywhere on the current site.
- The Facebook link on the site is an old "Sandwich-Shop" category URL; it is kept as published but should be replaced with the shop's real page.
- Pinch-zoom is blocked on the old site; the new site allows zoom.
- Photos on the old site are Google-hosted images we could not view or confirm as the shop's own, so none were published.

## What the new site does

- Live text menu with category tabs and search (where a menu was published), live open/closed status and today's hours (where hours were published), directions and a sticky call bar on phones.
- Shared `plain` template (engine/templates/plain.*) with this shop's own palette; built by `engine/build_plainshop.py` from `clients/fire-21-pizza-conway/data.json`.
- Phone ordering only: no ordering link could be verified, so none was invented.
- Restaurant structured data without price range or OrderAction.

## Image rights

No photos are published. None of the shop's own photos could be retrieved and confirmed as the shop's, and reuse permission is unknown for all of them. Get the owner's OK and send full-size food/shop photos before launch; the layout adds a gallery when images are supplied.

## Questions for the owner before launch

1. What are your hours?
2. Can you send your menu with prices? None is published online, so the site shows no menu.
3. Which Facebook page is yours? The link on the old site is an outdated category URL.
4. Do you have photos we may use (food, shop, the Henderson family)?
5. Do you offer delivery or online ordering?
6. Is the address 7 West Main St, Conway Village?

Fonts are open-license (SIL OFL); licence files ship in `assets/fonts/`.

## Not checked yet

- Real phones (iPhone Safari, Android Chrome) and a screen reader pass.
- Lighthouse scores on the hosted site.
- Placing an order: no order was placed.
- Menu and hours were read from the shop's public pages on Nov 10, 2026 and may have changed.
