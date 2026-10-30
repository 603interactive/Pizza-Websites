# Gilford House of Pizza: redesign concept

Built Oct 30, 2026 by 603 Interactive from the shop's own content only. No AI-generated or stock food photos.

## Files

- `preview.html`: the whole site in one file, with a "design concept" ribbon. Open it in any browser to show the owner.
- `site/`: the launch-ready site (no ribbon). Drag the folder onto app.netlify.com/drop.

## What we found on the current site

- Site-builder template with leftovers: the header shows placeholder contact details "555-555-5555" and "mymail@mailservice.com" on every page.
- The Menu page still has the template slider text ("Breathtaking colors of our planet", "Faces of Humanity", "Sands of Time", "Beyond Boundaries") and a row of unlabeled "Button" buttons.
- Instagram and Yelp icons point to the generic instagram.com and yelp.com/biz/ pages instead of the shop's profiles; a WhatsApp link is wired to the landline.
- No online ordering; "L ike and Follow us" typo in the footer; the address block repeats three times in the header; the Location page says "Add your custom HTML here" instead of a map.
- The best content (flat $4 delivery with no DoorDash/Uber fees, specials, seasonal hours) is buried in plain text.

## The one big idea

The Delivery Desk: the customer enters their order and what a delivery app added in fees last time; the page shows the all-in GHOP total (food + 8.5% tax + flat $4) and the fees kept. Built from the shop's own claim: $4 delivery to Gilford and Laconia, drivers paid by the shop, no DoorDash/Uber fees. Also a season-aware hours card (fall/winter vs spring/summer).

## What else the new site does

- Live open / closed status and today's hours, address, phone and directions.
- Full menu with prices, category tabs and search, readable on a phone.
- Sticky call / order bar on phones, parallax hero, Restaurant structured data, sitemap and robots.txt.

## Questions for the owner before launch

1. Is delivery still flat $4 to Gilford and Laconia only? Any minimum order, and what hours does delivery run? (The old site says times are approximate and not guaranteed.)
2. Do you want online ordering? There is none today, so every Order button calls (603) 528-7788. If you use or want a system (Toast, OrderCounter, Slice, etc.) send the link and we will wire it in.
3. Please confirm seasonal hours: fall/winter (Labor Day to Memorial Day weekend) Mon-Thu 11-8, Fri-Sat 11-9, Sun 12-8; spring/summer Mon-Thu 11-9, Fri-Sat 11-10, Sun 12-9.
4. Delivery fee comparison: the "What did the app charge you?" tool lets customers type their own app fee. Are you comfortable naming DoorDash and Uber, as your current site does?
5. Is tax 8.5% still correct? The calculator uses 8.5% (from the old site).
6. The photos on the current site are category tiles with the category name baked into the picture, and we do not know if they are your own photos. Can you send real photos of your food and the shop? The logo and tiles came from your current site.
7. What is your email address and your real Instagram and Yelp links? The old site shows placeholders.
8. The old chips list has stray prices ($10.00, $8) we could not match to an item; please check the drinks and chips prices.

## Photo sources

- `logo.jpg` ← https://irp.cdn-website.com/9dc28497/dms3rep/multi/GHOP+Logo.JPG
- `pizza, gourmet, calzones, subs, steak, dinners, pasta, salads, sides, desserts, chips .jpg` ← the 11 menu category tiles on https://www.gilfordhouseofpizza.com/menu (files PIZZA-6, GREEK_PIZZA1, CALZONE2, TURKEY-SUB2, STEAK-SUB-PHILLY, WING-DING-DINNER, SPAGHETTI-MEATBALLS, SALAD, ONION-RINGS, BAKLAVA, CHIPS under irp.cdn-website.com/9dc28497/dms3rep/multi/).

Left out on purpose:

- `Drinks.JPG` category tile (merged into the Drinks & Chips section, which uses the chips tile).
- Nextdoor badge.
- Note: the tiles have the category name printed into the image, so they are used as-is as menu buttons. They look like stock-style photos; the owner should confirm they are the shop's own.

Fonts are open-license (SIL OFL); licence files ship in `assets/fonts/`.

## Not checked yet

- Real phones (iPhone Safari, Android Chrome) and a screen reader pass.
- Lighthouse scores on the hosted site.
- Placing an order: no order was placed.

## Launch steps

1. Get answers to the questions above and update `clients/gilford-house-of-pizza/data.json`, then rebuild with `python3 engine/build_gilford.py`.
2. Drag `site/` onto Netlify Drop for a staging link; check it on a phone.
3. Point the shop's domain at Netlify (owner's domain account needed).
4. Submit `sitemap.xml` in Google Search Console and update the Google Business Profile website link.
