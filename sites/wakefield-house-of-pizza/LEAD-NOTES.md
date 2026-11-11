# Wakefield House of Pizza: redesign concept

Built Nov 11, 2026 by 603 Interactive from the shop's own public site text only. No AI-generated or stock food photos, and no photos at all in this concept (see Image rights).

## Files

- `preview.html`: the whole site in one file, with a "design concept" ribbon.
- `site/`: the launch-ready site (no ribbon). Drag the folder onto app.netlify.com/drop.

## What we found on the current site

- The whole site is one long Squarespace page that is just a text price list (pizza, appetizers, dinners, subs, burgers, salads, kids, party platters).
- The only image on the page is the logo; no food or shop photos.
- There is no online ordering, only a phone number, so the new site is phone-order only and no ordering link was invented.
- Opening hours are not shown on the page (they exist only in hidden page data), so none are shown on the new site.
- No About section or story about the shop.
- Our fetch of the live page was blocked, so menu items and prices were not copied; the new site lists the menu categories from the lead research and tells customers to call.

## What the new site does

- Live text menu with category tabs and search (where a menu was published), live open/closed status and today's hours (where hours were published), directions and a sticky call bar on phones.
- Shared `plain` template (engine/templates/plain.*) with this shop's own palette; built by `engine/build_plainshop.py` from `clients/wakefield-house-of-pizza/data.json`.
- Phone ordering only: no ordering link could be verified, so none was invented.
- Restaurant structured data without price range or OrderAction.

## Image rights

No photos are published. None of the shop's own photos could be retrieved and confirmed as the shop's, and reuse permission is unknown for all of them. Get the owner's OK and send full-size food/shop photos before launch; the layout adds a gallery when images are supplied.

## Questions for the owner before launch

1. Do you have photos of your food and shop we may use? The current site has only the logo.
2. Can you send your current menu with prices so we can list it on the new site?
3. What are your opening hours, and are they the same every day?
4. Do you want online ordering? If you already use an ordering service, please send the link.
5. Do you offer delivery?
6. Would you like a short About section (your story, how long you have been open)?
7. Is the Facebook page (facebook.com/whopthereitis) the right social page, and do you have Instagram?

Fonts are open-license (SIL OFL); licence files ship in `assets/fonts/`.

## Not checked yet

- Real phones (iPhone Safari, Android Chrome) and a screen reader pass.
- Lighthouse scores on the hosted site.
- Placing an order: no order was placed.
- Menu: the live page could not be fetched (blocked), so no menu items or prices were copied; categories come from the lead research only. Hours are not published on the shop's page.
