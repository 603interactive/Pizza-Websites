# Lewiston House of Pizza: redesign concept

Built Nov 14, 2026 by 603 Interactive from the lead file's details only (the shop's own pages could not be fetched in this unattended run). No AI-generated or stock food photos, and no photos at all in this concept (see Image rights).

## Files

- `preview.html`: the whole site in one file, with a "design concept" ribbon.
- `site/`: the launch-ready site (no ribbon). Drag the folder onto app.netlify.com/drop.

## What we found on the current site

- One-page vendor template (footer credit to eztouse.com) with a footer still reading ©2022.
- Only nav items are Home and Privacy Notice; catering, banquet rooms and the menu have no pages of their own.
- Confusing history: the page title says 'Best Pizza Since 2002' while the copy says 'Since 1998'. This concept states neither year.
- Ordering is split between an unlabeled Slice icon and a Google Play link to a ChowNow app, with no single Order button.
- Every image has an empty alt attribute; daily specials say 'Fries of O-Rings'.

## What the new site does

- Live text menu with category tabs and search (where a menu was published), live open/closed status and today's hours (where hours were published), directions and a sticky call bar on phones.
- Shared `plain` template (engine/templates/plain.*) with this shop's own palette; built by `engine/build_plainshop.py` from `clients/lewiston-house-of-pizza-me/data.json`.
- Online ordering links to the shop's own ordering page: https://slicelife.com/restaurants/me/lewiston/04240/lewiston-house-of-pizza/menu (not tested by placing an order).
- Restaurant structured data without price range.

## Image rights

No photos are published. None of the shop's own photos could be retrieved and confirmed as the shop's, and reuse permission is unknown for all of them. Get the owner's OK and send full-size food/shop photos before launch; the layout adds a gallery when images are supplied.

## Questions for the owner before launch

1. Which year did the shop open, 1998 or 2002?
2. Is the Slice link the one ordering path you want customers to use?
3. What do you offer for catering and what size are the banquet rooms?
4. Do you have photos of your food and shop we may use?
5. Can you send your current menu as text with prices so we can list it?
6. What are your opening hours?

Fonts are open-license (SIL OFL); licence files ship in `assets/fonts/`.

## Not checked yet

- Real phones (iPhone Safari, Android Chrome) and a screen reader pass.
- Lighthouse scores on the hosted site.
- Placing an order: no order was placed.
- No menu or hours are shown because none were verified (lead file only, built Nov 14, 2026 and may have changed.
