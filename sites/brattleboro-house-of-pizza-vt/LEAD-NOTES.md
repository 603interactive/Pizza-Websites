# Brattleboro House of Pizza: redesign concept

Built Nov 12, 2026 by 603 Interactive from the lead file's details only. No AI-generated or stock food photos, and no photos at all in this concept (see Image rights).

## Files

- `preview.html`: the whole site in one file, with a "design concept" ribbon.
- `site/`: the launch-ready site (no ribbon). Drag the folder onto app.netlify.com/drop.

## What we found on the current site

(From the lead research; the shop's pages could not be re-fetched during this build, see Not checked yet.)

- Single-page WordPress site on an old 'Tomato' theme, with a short About blurb, three testimonials, hours and contact.
- The only menu is a 4.7 MB PDF; there is no readable or searchable menu on the site.
- Footer reads 'Copyright ® 2018'; images load over plain http:// with generic or missing alt text.
- The copy says to download DoorDash for delivery while the nav's Order Online goes to order.online; the new site links only the order.online page from the lead.
- Only three small 2021 photos on the whole site.

## What the new site does

- Directions and a sticky call bar on phones. No menu items, prices or hours are shown, because none were verified (see below).
- Shared `plain` template (engine/templates/plain.*) with a chosen warm palette (the shop's own branding was not seen); built by `engine/build_plainshop.py` from `clients/brattleboro-house-of-pizza-vt/data.json`.
- Online ordering links to the ordering page named in the lead file: https://order.online/business/house-of-pizza-260353 (not opened or tested here).
- Restaurant structured data without price range.

## Image rights

No photos are published. None of the shop's own photos could be retrieved, and reuse permission is unknown for all of them. Get the owner's OK and send full-size food/shop photos and the logo before launch; the layout adds a gallery when images are supplied.

## Questions for the owner before launch

1. Is the order.online link correct and current? Do you deliver through DoorDash too?
2. Do you have photos of your food and shop we may use?
3. Can you send your current menu as text with prices so we can list it?
4. What are your opening hours?
5. Do you have Instagram?
6. Do the testimonials on your old site come from real customers we may quote (with their OK)?

Fonts are open-license (SIL OFL); licence files ship in `assets/fonts/`.

## Not checked yet

- The shop's website could not be fetched during this build (fetch permission was not granted), so menu items, prices and hours were NOT copied and nothing was verified against the live pages beyond the lead file (https://www.brattleboropizza.com).
- Real phones (iPhone Safari, Android Chrome) and a screen reader pass.
- Lighthouse scores on the hosted site.
- Placing a call or order: none made.
