# Rochester House of Pizza: redesign concept

Built Oct 28, 2026 by 603 Interactive from the shop's own content only. No AI-generated or stock food photos.

## Files

- `preview.html`: the whole site in one file, with a "design concept" ribbon. Open it in any browser to show the owner.
- `rochester-house-of-pizza-netlify-site.zip`: the launch-ready site (no ribbon). Unzip and drag the folder onto app.netlify.com/drop.

## What we found on the current site

- As of Oct 27, 2026 the website shows a Wix "This domain isn't connected to a site" page at both rochesterhouseofpizza.net addresses: customers searching for the shop currently land on an error.
- The archived site's Online Ordering button uses an insecure http:// link; the https:// ordering site works and is used here.
- The three combo deals are already on the online ordering menu (Specials), but the old site told customers they had to mention the deal by phone.
- The old site footer read "© 2013", its menu showed 10"/16" prices that differ from today's ordering menu, and its photos were small (most under 500px wide).
- On a phone, the old site hid the menu, the Online Ordering button and the combo deals.

## What the new site does about it

- Order button in the header, the hero, the menu and a sticky phone bar, linking straight into the shop's existing online ordering.
- Live open / closed status and today's hours for each shop, address, phone and directions.
- Full menu with photos, size prices, category tabs and search, readable on a phone.
- Combo deals shown on every screen size, with an Order this deal button.
- Search-engine basics: page title and description, Restaurant structured data, sitemap and robots.txt.

## Questions for the owner before launch

1. Is the shop open on Sundays and Mondays? Online ordering shows no times on those days.
2. Are the old website's 10" and 16" sizes the same as Small and Large in online ordering?
3. What are the delivery hours and area? Online ordering shows delivery from 4:30 PM on weekdays and all day Saturday.
4. About page says "over 35 years"; the ordering site says "over 30 years". Which should we use?
5. Can we have larger original photos of the food and the dining room? Most existing photos are under 500 px wide.
6. Do you want the domain reconnected to the new site (we'd need access to the domain account)?

## Photo sources

Every photo is the shop's own, taken from its current website or its online-ordering menu, then re-saved for the web.

- `hero.jpg` ← https://rochesterhouse.foodtecsolutions.com/webfile?name=Homepage&hash=1755518204000
- `logo.webp` ← https://rochesterhouse.foodtecsolutions.com/webfile?default=logo.gif&name=webLogo&hash=1759154538000
- `p-943f3c1e.webp` ← https://static.wixstatic.com/media/1c89c3_943f3c1ec2d065670002d4d518aabb51.jpg
- `p-4379870f.webp` ← https://static.wixstatic.com/media/1c89c3_4379870f7551b18e806a355c00018487.jpg
- `p-eda6b539.webp` ← https://static.wixstatic.com/media/1c89c3_eda6b539e0a44370d4fa9b1506ae1735.jpg
- `p-5c80274b.webp` ← https://static.wixstatic.com/media/1c89c3_5c80274b4cb73faf99fc92e1e3b509b9.jpg
- `p-f5468160.webp` ← https://static.wixstatic.com/media/1c89c3_f5468160f54e60183485583e43aa1d1e.jpg
- `p-9a111a59.webp` ← https://static.wixstatic.com/media/1c89c3_9a111a59f2cdae3fb09ca04762e261d3.jpg
- `p-d0970a76.webp` ← https://static.wixstatic.com/media/1c89c3_d0970a76f50a776c7648d4d92e57554f.jpg
- `p-b9db74ba.webp` ← https://static.wixstatic.com/media/1c89c3_b9db74ba174e7e9bf68f2f44eb623eb6.jpg
- `p-4c73011d.webp` ← https://static.wixstatic.com/media/1c89c3_4c73011dcbbec59edf33cad88a55fa2f.jpg

Fonts are open-license (SIL OFL); the licence files ship in `assets/fonts/`.

## Not checked yet

- Real phones (iPhone Safari, Android Chrome) and a screen reader pass.
- Lighthouse scores on the hosted site.
- Placing an order: the Order links were opened, but no order was placed.

## Launch steps

1. Get answers to the questions above and update `clients/rochester-house-of-pizza/data.json`, then rebuild with `python3 engine/build.py rochester-house-of-pizza`.
2. Drag the site folder onto Netlify Drop to get a staging link; check it on a phone.
3. Point the shop's domain at Netlify (the owner's domain account is needed).
4. Submit `sitemap.xml` in Google Search Console and update the Google Business Profile website link.
