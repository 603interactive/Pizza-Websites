# Family Pizza Pittsfield: redesign concept

Built Nov 10, 2026 by 603 Interactive from the shop's own public site text only. No AI-generated or stock food photos, and no photos at all in this concept (see Image rights).

## Files

- `preview.html`: the whole site in one file, with a "design concept" ribbon.
- `site/`: the launch-ready site (no ribbon). Drag the folder onto app.netlify.com/drop.

## What we found on the current site

- Stock "demo-restaurant" theme: the hero slides, section images and gallery are the theme's demo files, not the shop's food, so none were used.
- Listed email info@melodypicture.com belongs to the theme vendor, not the shop; it is not published on the new site.
- Instagram and Twitter icons point at the bare instagram.com / twitter.com homepages; only the shop's Facebook page is linked.
- Menu sections ("View More") are dead links; no menu prices are published on the site itself, so none are shown.
- "Latest Tweets" widget never loads.
- Ordering link comes from the Order online button on the contact page (24seveneatsonline); it was not tested by placing an order.

## What the new site does

- Live text menu with category tabs and search (where a menu was published), live open/closed status and today's hours (where hours were published), directions and a sticky call bar on phones.
- Shared `plain` template (engine/templates/plain.*) with this shop's own palette; built by `engine/build_plainshop.py` from `clients/family-pizza-pittsfield/data.json`.
- Online ordering links to the shop's own ordering page: https://www.24seveneatsonline.com/api/fb/_m_o7_vp (not tested by placing an order).
- Restaurant structured data without price range.

## Image rights

No photos are published. None of the shop's own photos could be retrieved and confirmed as the shop's, and reuse permission is unknown for all of them. Get the owner's OK and send full-size food/shop photos before launch; the layout adds a gallery when images are supplied.

## Questions for the owner before launch

1. Do you have photos of your food and shop we may use? The old site shows only theme demo images.
2. Can you send your menu with prices? None is published on the site, so the new site links to your ordering page.
3. Is the 24seveneatsonline link the right ordering page?
4. What email address should customers use?
5. Do you have Instagram or other social pages to link?
6. Hours show 10:30am to 10pm every day: are those current?
7. Do you offer delivery?

Fonts are open-license (SIL OFL); licence files ship in `assets/fonts/`.

## Not checked yet

- Real phones (iPhone Safari, Android Chrome) and a screen reader pass.
- Lighthouse scores on the hosted site.
- Placing an order: no order was placed.
- Menu and hours were read from the shop's public pages on Nov 10, 2026 and may have changed.
