# Plymouth House of Pizza and Pub: redesign concept

Built Nov 11, 2026 by 603 Interactive from the lead file only. No AI-generated or stock food photos, and no photos at all in this concept (see Image rights).

## Files

- `preview.html`: the whole site in one file, with a "design concept" ribbon.
- `site/`: the launch-ready site (no ribbon). Drag the folder onto app.netlify.com/drop.

## What we found on the current site

- Built on the GoDaddy Website Builder with a stock layout.
- The shop name and "Authentic Greek Flavors" headline repeat over and over in the page copy; the new copy says each once.
- Phone number shown unformatted as 5087460444; now (508) 746-0444 with a tap-to-call link.
- Homepage leads with a notice about dropping in-house delivery instead of the food; the new site leads with the food and ordering, and makes no delivery claim.
- Stray punctuation error in the copy ("Plymouth,. Massachusetts since 1997"); fixed.
- Ordering link (SkyTab) taken from the lead file; not tested by placing an order.
- The shop's website could not be fetched while building (fetch was blocked), so menu, prices and hours were NOT collected; only facts from the lead file are used.

## What the new site does

- Shared `plain` template (engine/templates/plain.*) with a blue/cream palette (chosen for contrast; the shop's own branding was not seen); built by `engine/build_plainshop.py` via `engine/build_plymouthhop.py` from `clients/plymouth-house-of-pizza-ma/data.json`.
- No menu and no hours are shown (not collected); the menu section points to the ordering page and phone. Sticky call bar on phones, directions link, Facebook link.
- Online ordering links to the shop's SkyTab page: https://online.skytab.com/829b61af479ffd363dfe7bf38f076c64/order-settings (not tested by placing an order).
- No delivery claim. Restaurant structured data without price range or opening hours.

## Image rights

No photos are published. None were supplied and reuse permission is unknown. Get the owner's OK and send full-size food/shop photos before launch; the layout adds a gallery when images are supplied.

## Questions for the owner before launch

1. Do you have photos of your food and shop we may use?
2. Can you send your menu with prices? The new site links to your SkyTab ordering page instead.
3. Is the SkyTab link the right ordering page?
4. What are your current hours? None are shown on the concept.
5. Please confirm the ZIP code (02360 used) and that delivery is no longer offered.
6. Do you want the Greek dishes highlighted on the menu?
7. What email address should customers use?

Fonts are open-license (SIL OFL); licence files ship in `assets/fonts/`.

## Not checked yet

- The shop's live website (fetch blocked): menu, prices, hours, ZIP and Greek-menu details unverified. Instagram (instagram.com/plymouthhouseofpizza) is not linked because the template only has a Facebook slot.
- Real phones (iPhone Safari, Android Chrome) and a screen reader pass.
- Lighthouse scores on the hosted site.
- Placing an order: no order was placed.
