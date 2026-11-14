# Farmington House of Pizza: redesign concept

Built Nov 14, 2026 by 603 Interactive from the lead file's details only (the shop's own pages could not be fetched in this unattended run). No AI-generated or stock food photos, and no photos at all in this concept (see Image rights).

## Files

- `preview.html`: the whole site in one file, with a "design concept" ribbon.
- `site/`: the launch-ready site (no ribbon). Drag the folder onto app.netlify.com/drop.

## What we found on the current site

- One-page vendor template (footer credit to eztouse.com, uploads dated 2018) with a footer still reading ©2022.
- The header 'Order Now!' is only the phone number; there is no online ordering.
- The menu is a long text-only price list with no photos next to items.
- Generic SEO filler copy ('Pizza & More For Take-Out & Delivery in farmington, ME', lowercase town).
- Every image has an empty alt attribute; the only real nav item is Home.

## What the new site does

- Live text menu with category tabs and search (where a menu was published), live open/closed status and today's hours (where hours were published), directions and a sticky call bar on phones.
- Shared `plain` template (engine/templates/plain.*) with this shop's own palette; built by `engine/build_plainshop.py` from `clients/farmington-house-of-pizza-me/data.json`.
- Phone ordering only: no ordering link could be verified, so none was invented.
- Restaurant structured data without price range or OrderAction.

## Image rights

No photos are published. None of the shop's own photos could be retrieved and confirmed as the shop's, and reuse permission is unknown for all of them. Get the owner's OK and send full-size food/shop photos before launch; the layout adds a gallery when images are supplied.

## Questions for the owner before launch

1. Would you like online ordering? If so, through which service?
2. Do you have photos of your food and shop we may use?
3. Can you send your current menu as text with prices so we can list it?
4. What are your opening hours?
5. Is the Instagram account fhopmaine yours to link?

Fonts are open-license (SIL OFL); licence files ship in `assets/fonts/`.

## Not checked yet

- Real phones (iPhone Safari, Android Chrome) and a screen reader pass.
- Lighthouse scores on the hosted site.
- Placing an order: no order was placed.
- No menu or hours are shown because none were verified (lead file only, built Nov 14, 2026 and may have changed.
