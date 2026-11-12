# Princeton House of Pizza: redesign concept

Built Nov 12, 2026 by 603 Interactive from the lead file's details only. No AI-generated or stock food photos, and no photos at all in this concept (see Image rights).

## Files

- `preview.html`: the whole site in one file, with a "design concept" ribbon.
- `site/`: the launch-ready site (no ribbon). Drag the folder onto app.netlify.com/drop.

## What we found on the current site

(From the lead research; the shop's pages could not be re-fetched during this build, see Not checked yet.)

- Stock WordPress 'Flash' theme with a homepage of stacked text blocks.
- The Breakfast Menu page is empty, and the only online ordering link (Slice) is hidden on it.
- The founding date conflicts across the site and Facebook (1960s, 2009, 1991); the new site makes no founding claim.
- Menu typos and inconsistencies on the old site: missing $ signs, 10"/15" sizes vs a 16" thin-crust upcharge.
- No social links on the old site, though the shop is active on Facebook.

## What the new site does

- Directions and a sticky call bar on phones. No menu items, prices or hours are shown, because none were verified (see below).
- Shared `plain` template (engine/templates/plain.*) with a chosen warm palette (the shop's own branding was not seen); built by `engine/build_plainshop.py` from `clients/princeton-house-of-pizza-ma/data.json`.
- Online ordering links to the ordering page named in the lead file: https://slicelife.com/restaurants/ma/princeton/01541/princeton-house-of-pizza-princeton/menu (not opened or tested here).
- Restaurant structured data without price range.

## Image rights

No photos are published. None of the shop's own photos could be retrieved, and reuse permission is unknown for all of them. Get the owner's OK and send full-size food/shop photos and the logo before launch; the layout adds a gallery when images are supplied.

## Questions for the owner before launch

1. Is the Slice ordering link correct and current?
2. Do you have photos of your food and shop we may use?
3. Can you send your current menu with prices so we can list it?
4. What are your opening hours, including breakfast?
5. What year did the shop open, and who owns it?
6. Do you offer delivery?
7. Do you have Instagram or TikTok pages to link?

Fonts are open-license (SIL OFL); licence files ship in `assets/fonts/`.

## Not checked yet

- The shop's website could not be fetched during this build (fetch permission was not granted), so menu items, prices and hours were NOT copied and nothing was verified against the live pages beyond the lead file (https://princetonpizzaria.com).
- Real phones (iPhone Safari, Android Chrome) and a screen reader pass.
- Lighthouse scores on the hosted site.
- Placing a call or order: none made.
