# Farmington House of Pizza: redesign concept

Built Oct 30, 2026 by 603 Interactive from the shop's own content only. No AI-generated or stock food photos.

## Files

- `preview.html`: the whole site in one file, with a "design concept" ribbon. Open it in any browser to show the owner.
- `site/`: the launch-ready site (no ribbon). Drag the folder onto app.netlify.com/drop.

## What we found on the current site

- Old Community Communications template site; the homepage is almost entirely images (logo banner, background photo, "welcome" graphic) with the Order Online and Call Us buttons drawn into the banner as clickable image-map hotspots.
- Viewport tag uses old, invalid syntax with user-scalable=0, which blocks pinch zoom on phones.
- The plain http:// version returns a server error (HTTP 500) instead of redirecting to https.
- The menu page is a long plain-text price table; the linked "Download Menu" PDF was last updated in May 2016.
- Homepage still promotes an old eDiningExpress phone app (Google Play and iOS badges) next to a separate OrderCounter online ordering page.

## The one big idea

The Pie Studio: pick Medium or Large and toppings from the real menu (cheese pizza plus $1.00-$2.00 per topping), see the live total, and a tip tells the customer when one of the specialty pizzas (Hawaiian, Meat Lovers, House Special) is cheaper than building it. Prices are the website menu prices.

## What else the new site does

- Live open / closed status and today's hours, address, phone and directions.
- Full menu with prices, category tabs and search, readable on a phone.
- Sticky call / order bar on phones, parallax hero, Restaurant structured data, sitemap and robots.txt.

## Questions for the owner before launch

1. The old banner says "We Deliver! Call (603) 755-9001" with tiny text we read as "after 4pm". Is delivery real, from what time, to which towns, and is there a fee or minimum? (We put "Call after 4 PM" on the site and need you to confirm.)
2. Please confirm hours: closed Monday, 11-9 Tuesday to Saturday, 11-8 Sunday (from the current Hours page). Any holiday or seasonal changes?
3. The menu says "NEW! 100% made in-house" chicken tenders and sells them by the bucket. What are bucket sizes and prices so we can list them?
4. Is the Farmington menu on OrderCounter the same price list as the website menu? We used the website prices and the new "Build vs buy" tool depends on them being current (topping prices, medium/large cheese).
5. The menu page shows 9% NH meals tax; Gilford sites show 8.5%. Please confirm the current rate to display.
6. Do you want to keep the eDiningExpress app? We left it off; the app badges point to a separate system from OrderCounter.
7. You have 7 photos of your own food on the old gallery page. Can you send newer ones (storefront, interior, owners, the tenders)? We have no photo of the shop or the people.
8. No logo file exists except a banner image with the shop name baked in, so we typeset the name. Do you have a clean logo file?

## Photo sources

- `pizza-whole.jpg`, `pizza-edge.jpg`, `pizza-slice.jpg`, `tenders.jpg`, `club.jpg`, `sub.jpg`, `salad.jpg` ← https://www.farmingtonhouseofpizza.com/gallery/large/web_6877.jpg (and web_6878, 6887, 6905, 6916, 6929, 6933), the shop's own gallery page.

Left out on purpose:

- Logo banner `images/logo.jpg`: the shop name is baked into a photo banner with Order/Call buttons, so the new site typesets the name instead.
- Homepage background photo `images/bg.jpg` and `images/welcome.jpg`: blurred / text graphics.
- eDiningExpress Google Play and iOS badges.

Fonts are open-license (SIL OFL); licence files ship in `assets/fonts/`.

## Not checked yet

- Real phones (iPhone Safari, Android Chrome) and a screen reader pass.
- Lighthouse scores on the hosted site.
- Placing an order: no order was placed.

## Launch steps

1. Get answers to the questions above and update `clients/farmington-house-of-pizza/data.json`, then rebuild with `python3 engine/build_farmington.py`.
2. Drag `site/` onto Netlify Drop for a staging link; check it on a phone.
3. Point the shop's domain at Netlify (owner's domain account needed).
4. Submit `sitemap.xml` in Google Search Console and update the Google Business Profile website link.
