# Millo's Pizza & Grill: redesign concept

Built Nov 10, 2026 by 603 Interactive from the shop's own public site text only. No AI-generated or stock food photos, and no photos at all in this concept (see Image rights).

## Files

- `preview.html`: the whole site in one file, with a "design concept" ribbon.
- `site/`: the launch-ready site (no ribbon). Drag the folder onto app.netlify.com/drop.

## What we found on the current site

- GoDaddy Website Builder site; homepage was nearly empty (one "A Few Of Our Dishes" caption, address and hours).
- No online ordering and no social links on the site.
- Menu and Specials pages were long plain price lists; typos in the source ("Caeser", "cucumberes") were not carried over.
- No food or shop photos could be collected and cleared: the homepage photo was not retrievable, so this concept is typographic. No photos were published.

## What the new site does

- Live text menu with category tabs and search (where a menu was published), live open/closed status and today's hours (where hours were published), directions and a sticky call bar on phones.
- Shared `plain` template (engine/templates/plain.*) with this shop's own palette; built by `engine/build_plainshop.py` from `clients/millos-pizza-and-grill-barrington/data.json`.
- Phone ordering only: no ordering link could be verified, so none was invented.
- Restaurant structured data without price range or OrderAction.

## Image rights

No photos are published. None of the shop's own photos could be retrieved and confirmed as the shop's, and reuse permission is unknown for all of them. Get the owner's OK and send full-size food/shop photos before launch; the layout adds a gallery when images are supplied.

## Questions for the owner before launch

1. Do you have photos of your food and shop we may use? None were published in this concept.
2. The menu prints two prices for most pizzas with no size labels: which sizes are they (e.g. small/large)?
3. Mediterranean Veggie pizza shows a check mark instead of a price: what is the price?
4. Do you want an online-ordering link? None exists, so the site is phone-order only.
5. Closing time: the homepage says "Open til 9:00pm". Is that every day?
6. What areas do you deliver to?
7. Do you have an About story or an owner name you want shown?

Fonts are open-license (SIL OFL); licence files ship in `assets/fonts/`.

## Not checked yet

- Real phones (iPhone Safari, Android Chrome) and a screen reader pass.
- Lighthouse scores on the hosted site.
- Placing an order: no order was placed.
- Menu and hours were read from the shop's public pages on Nov 10, 2026 and may have changed.
