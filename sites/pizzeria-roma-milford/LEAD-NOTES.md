# Pizzeria Roma: redesign concept

Built Nov 10, 2026 by 603 Interactive from the shop's own public site text only. No AI-generated or stock food photos, and no photos at all in this concept (see Image rights).

## Files

- `preview.html`: the whole site in one file, with a "design concept" ribbon.
- `site/`: the launch-ready site (no ribbon). Drag the folder onto app.netlify.com/drop.

## What we found on the current site

- Old Community Communications vendor template; homepage is a single paragraph and the menu is a plain text price table.
- No online ordering and no social links on the site.
- Pinch-zoom is blocked on the old site; the new site allows zoom.
- Only a logo and one homepage image were on the site and neither could be confirmed as the shop's own cleared photography, so none were published.
- Source typos ("Terriyaki", "Jalepeno") were corrected.
- Gallery, Hours and Contact pages were not read: hours come from the homepage text.

## What the new site does

- Live text menu with category tabs and search (where a menu was published), live open/closed status and today's hours (where hours were published), directions and a sticky call bar on phones.
- Shared `plain` template (engine/templates/plain.*) with this shop's own palette; built by `engine/build_plainshop.py` from `clients/pizzeria-roma-milford/data.json`.
- Phone ordering only: no ordering link could be verified, so none was invented.
- Restaurant structured data without price range or OrderAction.

## Image rights

No photos are published. None of the shop's own photos could be retrieved and confirmed as the shop's, and reuse permission is unknown for all of them. Get the owner's OK and send full-size food/shop photos before launch; the layout adds a gallery when images are supplied.

## Questions for the owner before launch

1. Do you have photos of your food and shop we may use? None are published in this concept.
2. Pizza sizes were read as 12", 16" and 18" (Small / Large / X-Large). Please confirm.
3. Subs list two prices with no size labels; we show them as listed. Are they small and large?
4. Is the menu current? Prices were copied from the live site.
5. Do you want online ordering? None exists, so the site is phone-order only.
6. Confirm hours: Monday to Saturday 11am to 9pm, closed Sunday.
7. Do you have a Facebook or Instagram page to link?
8. Which delivery area do you cover?

Fonts are open-license (SIL OFL); licence files ship in `assets/fonts/`.

## Not checked yet

- Real phones (iPhone Safari, Android Chrome) and a screen reader pass.
- Lighthouse scores on the hosted site.
- Placing an order: no order was placed.
- Menu and hours were read from the shop's public pages on Nov 10, 2026 and may have changed.
