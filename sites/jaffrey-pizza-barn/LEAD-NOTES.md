# Jaffrey Pizza Barn: redesign concept

Built Nov 03, 2026 by 603 Interactive from the shop's own content only. No AI-generated or stock food photos.

## Files

- `preview.html`: the whole site in one file, with a "design concept" ribbon. Open it in any browser to show the owner.
- `site/`: the launch-ready site (no ribbon). Drag the folder onto app.netlify.com/drop.

## What we found on the current site

- Homepage is one short paragraph and two images (a stock-style photo of mozzarella sticks and a banner of grinders and burgers); no hours, specials or menu highlights.
- /menu.html is an empty page (header and footer only); the "Menu" link sends visitors to the eDiningExpress ordering page instead.
- "Order Online" and "Delivery Available" are flat PNG images, not real buttons.
- Old viewport tag with user-scalable=0 blocks pinch-zoom on phones.
- Hours and contact are on separate thin pages; no social links, email or contact form anywhere.
- Stored menu on eDiningExpress has 17 categories and 178 items with real photos, none of which appear on the shop's own site.

## The one big idea

Same Flavor, Every Way: the shop sells its specialties as a pizza, a calzone, a grinder, a salad or a dinner, but its own menu lists them in separate places. Pick one of 12 flavors (Buffalo Chicken, Steak Bomb, Grecian, Barn Burner, Big Mac and more) and see every way to order it side by side with the real menu prices, with the lowest starting price flagged. Pairings are matched by item name and need the owner's OK.

## What else the new site does

- Live open / closed status and today's hours, address, phone and directions.
- Full menu with prices, category tabs and search, readable on a phone.
- Sticky call / order bar on phones, parallax hero, Restaurant structured data, sitemap and robots.txt.

## Questions for the owner before launch

1. Are the hours Tue-Sat 11 AM-8 PM, closed Sun and Mon, still right (the hours page says so)?
2. What are delivery zones, fees and minimums? The site only says "Delivery Available for Online Orders".
3. Is there a Facebook page or Instagram we should link? None is on the current site.
4. Is there a story to tell? The site only says "in business since 1973"; who founded it, and who runs it today?
5. Topping prices for build-your-own pizza and calzones were not on the public menu. Can you send them so we can show them on the site?
6. "Same Flavor, Every Way" links items by name (for example the Steak Bomb pizza, calzone and grinder; the Greek salad is paired with the Grecian). Are these the pairings you would make, and are any specialties missing?
7. Do you want to keep eDiningExpress for ordering? The new site links to it for every Order button.
8. The old homepage photos look like stock images. We used only the food photos from your eDiningExpress menu. Please confirm they are yours.

## Photo sources

- All food photos come from the shop's own eDiningExpress online menu (https://www.ediningexpress.com/live20/business_data/images/965/menu_items/ and /categories/): full-size versions of the Grecian, Big Mac, Barn Burner, BBQ Chicken, BLT, Chicken Club and Cheese pizzas, calzone, bread stix, Steak Bomb and Steak & Cheese grinders, Barn Burn grinder, Greek salad, buffalo nuggets and wings, dinners, haddock, seafood plate, Admirals plate, lasagna, family meals, burger plates, Southwestern eggrolls and triple cheeseburger.
- `logo.png` ← https://jaffreypizzabarn.com/images/logo.png (the shop's logo).

Left out on purpose:

- `homepage.jpg` (mozzarella sticks): EXIF credit shows a 123RF stock photo, not the shop's own.
- `01.png` banner (grinders and burgers): stock-style two-panel photo.
- Order Online and Delivery badge PNGs (replaced with real buttons).

Fonts are open-license (SIL OFL); licence files ship in `assets/fonts/`.

## Not checked yet

- Real phones (iPhone Safari, Android Chrome) and a screen reader pass.
- Lighthouse scores on the hosted site.
- Placing an order: no order was placed.

## Launch steps

1. Get answers to the questions above and update `clients/jaffrey-pizza-barn/data.json`, then rebuild with `python3 engine/build_jaffrey.py`.
2. Drag `site/` onto Netlify Drop for a staging link; check it on a phone.
3. Point the shop's domain at Netlify (owner's domain account needed).
4. Submit `sitemap.xml` in Google Search Console and update the Google Business Profile website link.
