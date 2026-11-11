# Jimmy's Hometown Pizzeria: redesign concept

Built Nov 11, 2026 by 603 Interactive from the lead details only (the shop's own pages could not be fetched during the build). No AI-generated or stock food photos, and no photos at all in this concept (see Image rights).

## Files

- `preview.html`: the whole site in one file, with a "design concept" ribbon.
- `site/`: the launch-ready site (no ribbon). Drag the folder onto app.netlify.com/drop.

## What we found on the current site

- Squarespace site: the homepage is just "A Slice of Home", the address, phone numbers and hours; no description of the shop or food.
- The Menu page is images only, with no text, so it cannot be searched or read easily on a phone.
- The Delivery page has no content beyond the shared header and footer.
- The only store is a merch shop (cap, tee, hoodie); there is no online food ordering.
- A scrolling hours banner repeats the same line four times.
- Two phone numbers are listed: (603) 903-0200 and (603) 903-0201. The first is used for the call button.

## What the new site does

- Live text menu with category tabs and search (where a menu was published), live open/closed status and today's hours (where hours were published), directions and a sticky call bar on phones. Here the menu and hours are empty, so the site shows the address, phone, directions and a note to call.
- Shared `plain` template (engine/templates/plain.*) with a neutral cream and brick-red palette (no brand colors were available); built by `engine/build_jimmyshometown.py` from `clients/jimmys-hometown-pizzeria/data.json`.
- No online ordering exists, so the order button is a call button: tel:+16039030200.
- Restaurant structured data without price range or hours.

## Image rights

No photos are published. No images were supplied and reuse permission is unknown for the shop's photos. Get the owner's OK and send full-size food/shop photos before launch; the layout adds a gallery when images are supplied.

## Questions for the owner before launch

1. Can you send your menu with prices as text? The current menu is images only, so none is shown.
2. What are your current hours? They were not available to us in readable form, so none are shown.
3. Do you have photos of your food and shop we may use?
4. Do you want online ordering, and if so through which service? Is delivery offered?
5. Which of the two phone numbers should customers call?
6. Is the Facebook page linked the shop's page? Do you have Instagram?
7. What is the ZIP code you want shown in the address?

Fonts are open-license (SIL OFL); licence files ship in `assets/fonts/`.

## Not checked yet

- Real phones (iPhone Safari, Android Chrome) and a screen reader pass.
- Lighthouse scores on the hosted site.
- The shop's live pages: WebFetch was blocked, so nothing was read from jimmyshometownpizza.com; all facts come from the lead file.
