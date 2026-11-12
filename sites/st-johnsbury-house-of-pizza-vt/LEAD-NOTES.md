# St. Johnsbury House of Pizza: redesign concept

Built Nov 12, 2026 by 603 Interactive from the lead file's details only. No AI-generated or stock food photos, and no photos at all in this concept (see Image rights).

## Files

- `preview.html`: the whole site in one file, with a "design concept" ribbon.
- `site/`: the launch-ready site (no ribbon). Drag the folder onto app.netlify.com/drop.

## What we found on the current site

(From the lead research; the shop's pages could not be re-fetched during this build, see Not checked yet.)

- Single-page Wix site; the page title is cut off as 'HOME | St Johnsbury House o' and is reused as the share title.
- The menu is only a few photo images, with no text, prices or searchable content.
- No online ordering and no Order or Call button, only two phone numbers in the Contact block.
- The hero is a Wix library image, not a shop photo, and images have no alt text.
- Almost nothing about the family history beyond one sentence on being open since 1979.

## What the new site does

- Directions and a sticky call bar on phones. No menu items, prices or hours are shown, because none were verified (see below).
- Shared `plain` template (engine/templates/plain.*) with a chosen warm palette (the shop's own branding was not seen); built by `engine/build_plainshop.py` from `clients/st-johnsbury-house-of-pizza-vt/data.json`.
- Phone ordering only: no verified ordering link, so none was invented. Phone: 802-748-5144.
- Restaurant structured data without price range or OrderAction.

## Image rights

No photos are published. None of the shop's own photos could be retrieved, and reuse permission is unknown for all of them. Get the owner's OK and send full-size food/shop photos and the logo before launch; the layout adds a gallery when images are supplied.

## Questions for the owner before launch

1. Do you have photos of your food and shop we may use?
2. Can you send your menu as text with prices so we can list it?
3. What are your opening hours?
4. Do you want online ordering or phone only?
5. Do you offer delivery?
6. Would you like a short story section about the family and the shop since 1979?

Fonts are open-license (SIL OFL); licence files ship in `assets/fonts/`.

## Not checked yet

- The shop's website could not be fetched during this build (fetch permission was not granted), so menu items, prices and hours were NOT copied and nothing was verified against the live pages beyond the lead file (https://www.houseofpizzavt.com).
- Real phones (iPhone Safari, Android Chrome) and a screen reader pass.
- Lighthouse scores on the hosted site.
- Placing a call or order: none made.
