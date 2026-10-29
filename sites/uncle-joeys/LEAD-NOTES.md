# Uncle Joey's: redesign concept

Built Oct 28, 2026 by 603 Interactive from the shop's own content only. No AI-generated or stock food photos.

## Files

- `preview.html`: the whole site in one file, with a "design concept" ribbon. Open it in any browser to show the owner.
- `uncle-joeys-netlify-site.zip`: the launch-ready site (no ribbon). Unzip and drag the folder onto app.netlify.com/drop.

## What we found on the current site

- The hero title "Uncle Joey's of Merrimack" is overlapped by the tagline, and a popup covers the page on load.
- The menu is a single 3600px image of the printed menu, so it can't be read on a phone, searched or linked to.
- The Order Online button carries copied Google Ads tracking parameters (utm_source=PaidGoogle, gclid=…).
- Navigation has an empty first button; every nav item only scrolls the same page.
- The hours block ends with a stray "Closed" line that doesn't name a day (it means Monday).
- The only real photos on the site are the logo and one cheese pizza; Slice's item photos are stock catalog images, so we didn't use them.

## What the new site does about it

- Order button in the header, the hero, the menu and a sticky phone bar, linking straight into the shop's existing online ordering.
- Live open / closed status and today's hours for each shop, address, phone and directions.
- Full menu with photos, size prices, category tabs and search, readable on a phone.
- Search-engine basics: page title and description, Restaurant structured data, sitemap and robots.txt.

## Questions for the owner before launch

1. Printed-menu prices are lower than Slice (Slice adds a markup: cheese pie $13.99 online vs $11.99/$15.99 in store). Should the website show in-store prices?
2. Two pizzas are on Slice but not the printed menu (The Big Mac, The Bee Sting). Are they current?
3. Can we photograph the shop? One real pie photo isn't enough for the site; a shoot of Chick Stix, the Supremo, a calzone and the family would carry the whole design.
4. Catering: the catering menu image shows half/full tray prices (Caesar $40/$60, Chick Stix $60/$94, etc.). Do you want a catering section with those?
5. Do you want the Nashua shop linked from this site, or kept fully separate?
6. Is the "Closed" line on the current site meant to be Monday?

## Photo sources

Every photo is the shop's own, taken from its current website or its online-ordering menu, then re-saved for the web.

- `hero.jpg` ← https://static.wixstatic.com/media/451d47_095bc89f91a1492ab2ffdec44aec904f~mv2.png
- `logo.webp` ← https://static.wixstatic.com/media/451d47_5f85f138df144bc7af952bf0b391a845~mv2.jpeg
- `logo-square.jpg` ← https://static.wixstatic.com/media/451d47_5f85f138df144bc7af952bf0b391a845~mv2.jpeg
- `hero.jpg` ← https://static.wixstatic.com/media/451d47_095bc89f91a1492ab2ffdec44aec904f~mv2.png

Left out on purpose:

- https://static.wixstatic.com/media/slice-menu-assets (54 item photos): Slice catalog stock photos, not the shop's (same calzone photo repeated 7 times)

Fonts are open-license (SIL OFL); the licence files ship in `assets/fonts/`.

## Not checked yet

- Real phones (iPhone Safari, Android Chrome) and a screen reader pass.
- Lighthouse scores on the hosted site.
- Placing an order: the Order links were opened, but no order was placed.

## Launch steps

1. Get answers to the questions above and update `clients/uncle-joeys/data.json`, then rebuild with `python3 engine/build.py uncle-joeys`.
2. Drag the site folder onto Netlify Drop to get a staging link; check it on a phone.
3. Point the shop's domain at Netlify (the owner's domain account is needed).
4. Submit `sitemap.xml` in Google Search Console and update the Google Business Profile website link.

## Design concept (v2)
- Look: late-night neon sign on black, kitchen-ticket menu wall, Erica One + DM Mono.
- Selling point: the **Chick Stix Builder**. Customer picks count (5/10/15/20), plain or buffalo, dippers and Jo Jos, sees the tray fill, gets a live total from the printed-menu prices and sends the ticket to Slice, the phone, or a copy-to-clipboard.
- Also: live neon OPEN sign driven by the real hours, Tender Pack vs. two 20-piece math.
- Open question: Slice may not accept a pre-built order, so the builder hands off by link/phone/copy until the owner confirms a deeper Slice integration.
