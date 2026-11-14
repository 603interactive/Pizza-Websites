# Ware House of Pizza: redesign concept

Built Nov 14, 2026 by 603 Interactive from the Pizza-Leads lead file's details only (the shop's own pages could not be fetched in this unattended run). No AI-generated or stock food photos, and no photos at all in this concept (see Image rights).

## Files

- `preview.html`: the whole site in one file, with a "design concept" ribbon.
- `site/`: the launch-ready site (no ribbon). Drag the folder onto app.netlify.com/drop.

## What we found on the current site

- Stock Menufy ordering template; the only homepage image is the logo.
- Vague copy ('Delicious Slices of Happiness!') with no story about the shop.
- A 'Contact Form' heading appears but no form exists; boilerplate listing fields ('Atmosphere: Chill') appear as content.
- The same hours are repeated three times.
- A second domain, warepizza.com, still appears in search results but opens a blank web-host page.

## What the new site does

- Live text menu with category tabs and search (where a menu was published), live open/closed status and today's hours (where hours were published), directions and a sticky call bar on phones.
- Shared `plain` template (engine/templates/plain.*) with this shop's own palette; built by `engine/build_plainshop.py` from `clients/ware-house-of-pizza-ma/data.json`.
- Online ordering links to the shop's own ordering page: https://www.warehouseofpizza.com/order (not tested by placing an order).
- Restaurant structured data without price range.

## Image rights

No photos are published. None of the shop's own photos could be retrieved and confirmed as the shop's, and reuse permission is unknown for all of them. Get the owner's OK and send full-size food/shop photos before launch; the layout adds a gallery when images are supplied.

## Questions for the owner before launch

1. Is the Facebook page found in public search (profile id 61553245817064) really yours?
2. Do you want warepizza.com pointed at the new site?
3. Do you have a logo file we may use?
4. Do you have photos of your food and shop we may use?
5. Can you send your current menu as text with prices so we can list it?
6. What are your opening hours?

Fonts are open-license (SIL OFL); licence files ship in `assets/fonts/`.

## Not checked yet

- Real phones (iPhone Safari, Android Chrome) and a screen reader pass.
- Lighthouse scores on the hosted site.
- Placing an order: no order was placed.
- Menu items, prices and hours: none shown, because they were not verified (lead file only). Fetch them from the shop before launch.
