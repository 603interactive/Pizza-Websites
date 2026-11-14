# Village Pizza & Grill: redesign concept

Built Nov 14, 2026 by 603 Interactive from the Pizza-Leads lead file's details only (the shop's own pages could not be fetched in this unattended run). No AI-generated or stock food photos, and no photos at all in this concept (see Image rights).

## Files

- `preview.html`: the whole site in one file, with a "design concept" ribbon.
- `site/`: the launch-ready site (no ribbon). Drag the folder onto app.netlify.com/drop.

## What we found on the current site

- Hand-built one-page site from about 2019 (footer '© Parkview Pizza LLC', designer credit mjcamara.com).
- About text is out of date ('over 13 years', new owners 'as of December 2018'); this concept does not repeat it.
- No online ordering, only a phone number, shown as 1-603-968-9689.
- Long text-only menu; the printable PDF menu was last modified May 2023.
- Photo carousel images use placeholder alt text ('img 1') and raw camera file names.

## What the new site does

- Live text menu with category tabs and search (where a menu was published), live open/closed status and today's hours (where hours were published), directions and a sticky call bar on phones.
- Shared `plain` template (engine/templates/plain.*) with this shop's own palette; built by `engine/build_plainshop.py` from `clients/village-pizza-grill-ashland/data.json`.
- Phone ordering only: no ordering link could be verified, so none was invented.
- Restaurant structured data without price range or OrderAction.

## Image rights

No photos are published. None of the shop's own photos could be retrieved and confirmed as the shop's, and reuse permission is unknown for all of them. Get the owner's OK and send full-size food/shop photos before launch; the layout adds a gallery when images are supplied.

## Questions for the owner before launch

1. Would you like online ordering? If so, through which service?
2. Do you have photos of your food and shop we may use?
3. Can you send your current menu as text with prices so we can list it?
4. What are your opening hours?
5. Is the printable PDF menu (May 2023) still current?

Fonts are open-license (SIL OFL); licence files ship in `assets/fonts/`.

## Not checked yet

- Real phones (iPhone Safari, Android Chrome) and a screen reader pass.
- Lighthouse scores on the hosted site.
- Placing an order: no order was placed.
- Menu items, prices and hours: none shown, because they were not verified (lead file only). Fetch them from the shop before launch.
