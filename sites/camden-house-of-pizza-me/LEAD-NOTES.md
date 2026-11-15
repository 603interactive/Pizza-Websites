# Camden House of Pizza: redesign concept

Built Nov 15, 2026 by 603 Interactive from the Pizza-Leads lead file's details only (the shop's own pages were not retrieved in this unattended run). No AI-generated or stock food photos, and no photos at all in this concept (see Image rights).

## Files

- `preview.html`: the whole site in one file, with a "design concept" ribbon.
- `site/`: the launch-ready site (no ribbon). Drag the folder onto app.netlify.com/drop.

## What we found on the current site

- The menu page is a single phone photo of the paper menu, hard to read, search or zoom on a phone.
- Stock WordPress default theme: footer still shows placeholder items (Blog, About, FAQs, Authors, Events) and 'Twenty Twenty-Five' appears in page text.
- Site icon is a cropped 2019 screenshot file.
- Homepage slideshow says 'This slideshow requires JavaScript' and the page has only two images.
- A public review says the customer 'tried ordering online but the website would not cooperate'.

## What the new site does

- Live text menu with category tabs and search (where a menu was published), live open/closed status and today's hours (where hours were published), directions and a sticky call bar on phones.
- Shared `plain` template (engine/templates/plain.*) with this shop's own palette; built by `engine/build_plainshop.py` from `clients/camden-house-of-pizza-me/data.json`.
- Online ordering links to the shop's own ordering page: https://order.online/store/26344237 (not tested by placing an order).
- Restaurant structured data without price range.

## Image rights

No photos are published. None of the shop's own photos could be retrieved and confirmed as the shop's, and reuse permission is unknown for all of them. Get the owner's OK and send full-size food/shop photos before launch; the layout adds a gallery when images are supplied.

## Questions for the owner before launch

1. Is the order.online link the one ordering path you want customers to use?
2. Do you have photos of your food and shop we may use?
3. Can you send your current menu as text with prices so we can list it?
4. What are your opening hours?
5. The shop is on a side street: what landmark should directions mention?

Fonts are open-license (SIL OFL); licence files ship in `assets/fonts/`.

## Not checked yet

- Real phones (iPhone Safari, Android Chrome) and a screen reader pass.
- Lighthouse scores on the hosted site.
- Placing an order: no order was placed.
- Menu and hours were read from the shop's public pages on Nov 15, 2026 and may have changed.
