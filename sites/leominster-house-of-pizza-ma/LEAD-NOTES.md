# Leominster House of Pizza: redesign concept

Built Nov 15, 2026 by 603 Interactive from the Pizza-Leads lead file's details only (the shop's own pages were not retrieved in this unattended run). No AI-generated or stock food photos, and no photos at all in this concept (see Image rights).

## Files

- `preview.html`: the whole site in one file, with a "design concept" ribbon.
- `site/`: the launch-ready site (no ribbon). Drag the folder onto app.netlify.com/drop.

## What we found on the current site

- Web presence is split across two sites: a stock FoodTec ordering template on its own domain and a separate free GoDaddy subdomain site.
- The GoDaddy homepage is one line of welcome text with a single image and GoDaddy's default app logo.
- The own-domain site lists the address as just 'Central St' with no street number, and its main pitch is a FoodTec 'Register' signup box.
- Neither site has an about story, photos of the food, or social links.

## What the new site does

- Live text menu with category tabs and search (where a menu was published), live open/closed status and today's hours (where hours were published), directions and a sticky call bar on phones.
- Shared `plain` template (engine/templates/plain.*) with this shop's own palette; built by `engine/build_plainshop.py` from `clients/leominster-house-of-pizza-ma/data.json`.
- Online ordering links to the shop's own ordering page: https://leominsterhouseofpizza.foodtecsolutions.com/ordering/intro (not tested by placing an order).
- Restaurant structured data without price range.

## Image rights

No photos are published. None of the shop's own photos could be retrieved and confirmed as the shop's, and reuse permission is unknown for all of them. Get the owner's OK and send full-size food/shop photos before launch; the layout adds a gallery when images are supplied.

## Questions for the owner before launch

1. Do you want the GoDaddy site retired in favor of one site on leominsterhouseofpizza.com?
2. Is the FoodTec ordering link current?
3. Do you have photos of your food and shop we may use?
4. Can you send your current menu as text with prices so we can list it?
5. What are your opening hours?

Fonts are open-license (SIL OFL); licence files ship in `assets/fonts/`.

## Not checked yet

- Real phones (iPhone Safari, Android Chrome) and a screen reader pass.
- Lighthouse scores on the hosted site.
- Placing an order: no order was placed.
- Menu and hours were read from the shop's public pages on Nov 15, 2026 and may have changed.
