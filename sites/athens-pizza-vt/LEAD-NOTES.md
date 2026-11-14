# Athen's Pizza: redesign concept

Built Nov 14, 2026 by 603 Interactive from the Pizza-Leads lead file's details only (the shop's own pages could not be fetched in this unattended run). No AI-generated or stock food photos, and no photos at all in this concept (see Image rights).

## Files

- `preview.html`: the whole site in one file, with a "design concept" ribbon.
- `site/`: the launch-ready site (no ribbon). Drag the folder onto app.netlify.com/drop.

## What we found on the current site

- No menu page on the site; nav is Home, Story, Gallery, Order Online and Apply Now, so the menu is only visible inside the ordering system.
- Stale pandemic-era copy ('now open for dining in!'), odd leftover 'from a Dorm' ordering instructions and a capitalized VPN warning dominate the homepage.
- A scrolling 'now hiring' banner repeats three times.
- No social links on the site.

## What the new site does

- Live text menu with category tabs and search (where a menu was published), live open/closed status and today's hours (where hours were published), directions and a sticky call bar on phones.
- Shared `plain` template (engine/templates/plain.*) with this shop's own palette; built by `engine/build_plainshop.py` from `clients/athens-pizza-vt/data.json`.
- Online ordering links to the shop's own ordering page: https://athenspizza.hungerrush.com (not tested by placing an order).
- Restaurant structured data without price range.

## Image rights

No photos are published. None of the shop's own photos could be retrieved and confirmed as the shop's, and reuse permission is unknown for all of them. Get the owner's OK and send full-size food/shop photos before launch; the layout adds a gallery when images are supplied.

## Questions for the owner before launch

1. Are you hiring? We can add an Apply link.
2. Do you have photos of your food and shop we may use?
3. Can you send your current menu as text with prices so we can list it?
4. What are your opening hours?
5. Is the HungerRush ordering link correct and current?

Fonts are open-license (SIL OFL); licence files ship in `assets/fonts/`.

## Not checked yet

- Real phones (iPhone Safari, Android Chrome) and a screen reader pass.
- Lighthouse scores on the hosted site.
- Placing an order: no order was placed.
- Menu items, prices and hours: none shown, because they were not verified (lead file only). Fetch them from the shop before launch.
