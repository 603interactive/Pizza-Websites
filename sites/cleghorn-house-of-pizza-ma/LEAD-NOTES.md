# Cleghorn House of Pizza: redesign concept

Built Nov 15, 2026 by 603 Interactive from the Pizza-Leads lead file's details only (the shop's own pages were not retrieved in this unattended run). No AI-generated or stock food photos, and no photos at all in this concept (see Image rights).

## Files

- `preview.html`: the whole site in one file, with a "design concept" ribbon.
- `site/`: the launch-ready site (no ribbon). Drag the folder onto app.netlify.com/drop.

## What we found on the current site

- Homepage still shows an out-of-date notice: 'We will be closed Aug. 16 - Sep 16. Reopening Sep 17, 2025.' This concept does not repeat it.
- No online ordering anywhere on the site; customers have to call.
- Homepage is very thin: a two-sentence welcome, the address and phone numbers.
- Menu is a long text page plus a printable PDF, with no food photos.

## What the new site does

- Live text menu with category tabs and search (where a menu was published), live open/closed status and today's hours (where hours were published), directions and a sticky call bar on phones.
- Shared `plain` template (engine/templates/plain.*) with this shop's own palette; built by `engine/build_plainshop.py` from `clients/cleghorn-house-of-pizza-ma/data.json`.
- Phone ordering only: no ordering link could be verified, so none was invented.
- Restaurant structured data without price range or OrderAction.

## Image rights

No photos are published. None of the shop's own photos could be retrieved and confirmed as the shop's, and reuse permission is unknown for all of them. Get the owner's OK and send full-size food/shop photos before launch; the layout adds a gallery when images are supplied.

## Questions for the owner before launch

1. Would you like online ordering? If so, through which service?
2. Is the shop open now, and what are the hours?
3. How many years has the shop been open (the lead notes say 30+)?
4. Do you have photos of your food and shop we may use?
5. Can you send your current menu as text with prices so we can list it?
6. What are your opening hours?

Fonts are open-license (SIL OFL); licence files ship in `assets/fonts/`.

## Not checked yet

- Real phones (iPhone Safari, Android Chrome) and a screen reader pass.
- Lighthouse scores on the hosted site.
- Placing an order: no order was placed.
- Menu and hours were read from the shop's public pages on Nov 15, 2026 and may have changed.
