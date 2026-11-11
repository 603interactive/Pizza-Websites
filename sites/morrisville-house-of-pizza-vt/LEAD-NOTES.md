# Morrisville House of Pizza: redesign concept

Built Nov 11, 2026 by 603 Interactive from the lead file's details only. No AI-generated or stock food photos, and no photos at all in this concept (see Image rights).

## Files

- `preview.html`: the whole site in one file, with a "design concept" ribbon.
- `site/`: the launch-ready site (no ribbon). Drag the folder onto app.netlify.com/drop.

## What we found on the current site

(From the lead research; the shop's pages could not be re-fetched during this build, see Not checked yet.)

- Ziplocal/Divi template ("Powered by Ziplocal", "Designed by Elegant Themes") with only three pages.
- Homepage is one paragraph and a Menu button; the only images are the logo and one 2017 cover photo.
- Header "Order Now" is plain text beside the phone number: there is no online ordering, only calling.
- Menu is a long text-only price list with no photos.
- Page titles are keyword-stuffed and don't match the pages (e.g. "Cheese Calzones in Morrisville, VT" on the Menu page).
- Hours (Tue-Sat 11-8) appear only on the Contact page; the address wording differs between footer ("30 Mountain Plaza") and Contact page ("30 Mountain View Plaza").
- No social links on the site. A Facebook page named "House of Pizza" with a matching Morrisville address turned up in a public listing; it is linked but unconfirmed.

## What the new site does

- Live open/closed status and today's hours, directions and a sticky call bar on phones.
- No menu section with items: the menu is not reproduced (see below); the page points to calling the shop.
- Shared `plain` template (engine/templates/plain.*) with a warm red/green palette (the shop's own branding was not seen, so this is a chosen palette); built by `engine/build_morrisville.py` via `engine/build_plainshop.py` from `clients/morrisville-house-of-pizza-vt/data.json`.
- No online ordering exists, so every order button is a tap-to-call link: (802) 888-5200. Menu page for reference: https://www.morrisvillehouseofpizza.com/menu/
- Restaurant structured data without price range.

## Image rights

No photos are published. The only images known on the old site are the logo and one 2017 cover photo; reuse permission is unknown. Get the owner's OK and send full-size food/shop photos and the logo before launch; the layout adds a gallery when images are supplied.

## Questions for the owner before launch

1. Do you have photos of your food and shop we may use?
2. Can you confirm the street address: 30 Mountain Plaza or 30 Mountain View Plaza? (The new site shows only "Mountain View Plaza, Morrisville, VT 05661" until confirmed.)
3. Hours show Tuesday to Saturday, 11am to 8pm, closed Sunday and Monday: correct? (The source said "11-8"; am/pm assumed.)
4. Is https://www.facebook.com/pages/House-of-Pizza/119648414768703 your Facebook page? Do you have Instagram?
5. Can you send your current menu with prices so we can add a live menu? Would you like online ordering or phone only?
6. Do you offer delivery?
7. "About 30 years" is taken from our lead research: what year did the shop open, and who owns it?

Fonts are open-license (SIL OFL); licence files ship in `assets/fonts/`.

## Not checked yet

- The shop's website could not be fetched during this build (fetch permission was not granted), so menu items and prices were NOT copied and nothing was verified against the live pages beyond the lead file.
- Real phones (iPhone Safari, Android Chrome) and a screen reader pass.
- Lighthouse scores on the hosted site.
- Placing a call/order: none made.
