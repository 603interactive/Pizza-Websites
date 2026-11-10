# Lancaster House of Pizza: redesign concept

Built Nov 10, 2026 by 603 Interactive from the shop's own public site text only. No AI-generated or stock food photos, and no photos at all in this concept (see Image rights).

## Files

- `preview.html`: the whole site in one file, with a "design concept" ribbon.
- `site/`: the launch-ready site (no ribbon). Drag the folder onto app.netlify.com/drop.

## What we found on the current site

- Auto-generated Beyond Menu site; About text is generic and there are no photos of the shop.
- Only pizza and specialty pizza items were readable on the menu page we could fetch; appetizers, salads, calzones, subs, grinders, wraps, burgers, pasta, kids and desserts appear as headings only.
- A separate, unofficial site (orderlancasterhouseofpizza.com) lists a Vermont phone number; the new site links only to the shop's own order page and (603) 788-0964.
- No photos were published: the only images on the site are vendor stock paths.

## What the new site does

- Live text menu with category tabs and search (where a menu was published), live open/closed status and today's hours (where hours were published), directions and a sticky call bar on phones.
- Shared `plain` template (engine/templates/plain.*) with this shop's own palette; built by `engine/build_plainshop.py` from `clients/lancaster-house-of-pizza-lancaster/data.json`.
- Online ordering links to the shop's own ordering page: https://www.lancasterhouseofpizza.com/2wctw8mc/lancaster-house-of-pizza-lancaster-03584/order-online (not tested by placing an order).
- Restaurant structured data without price range.

## Image rights

No photos are published. None of the shop's own photos could be retrieved and confirmed as the shop's, and reuse permission is unknown for all of them. Get the owner's OK and send full-size food/shop photos before launch; the layout adds a gallery when images are supplied.

## Questions for the owner before launch

1. Please send the full menu: only pizza was readable online, so other sections are not shown.
2. Hours: the order page showed Mon-Thu 11-8, Fri-Sat 11-9, Sun closed. Are those current?
3. Is the online-order link above the one you want customers to use?
4. Do you have photos of your food and shop we may use?
5. Do you have a Facebook page we should link?
6. Can the unofficial order site with the Vermont phone number be taken down?

Fonts are open-license (SIL OFL); licence files ship in `assets/fonts/`.

## Not checked yet

- Real phones (iPhone Safari, Android Chrome) and a screen reader pass.
- Lighthouse scores on the hosted site.
- Placing an order: no order was placed.
- Menu and hours were read from the shop's public pages on Nov 10, 2026 and may have changed.
