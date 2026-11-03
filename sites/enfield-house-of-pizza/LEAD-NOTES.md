# Enfield House of Pizza: redesign concept

Built Nov 3, 2026 by 603 Interactive from the shop's own content only. No AI-generated or stock food photos.

## Files

- `preview.html`: the whole site in one file, with a "design concept" ribbon. Open it in any browser to show the owner.
- `site/`: the launch-ready site (no ribbon). Drag the folder onto app.netlify.com/drop.

## What we found on the current site

- Older Wix site with auto-generated URLs (/blank, /blank-1, /blank-2, /menus-1, /menus-2, /menus-3, /fresh-salads-1, /locations-hours-1).
- Header "ORDER ONLINE" links to `http://Togoorder.com/web/5102` (the lead report saw an HTTP 500 on the http link; the https version loads). The new site links to `https://togoorder.com/web/5102`.
- The menu is split across about seven plain-text pages; the homepage is a long asterisk bullet list.
- Header hours have typos ("M onday: Closed", "Tuesday - SUnday"). The Specials page was updated to the November Thanksgiving Pie by the time we built, so the "stale October feature" in the lead notes is already fixed.
- Job application is a PDF to print and bring in; no online form.

## The one big idea

**The Week at EHOP.** The shop runs a different deal every day, Tuesday to Sunday, but it is buried in a text page. The new site shows a seven-day calendar that opens on today's deal (it skips to Tuesday on Mondays, when the shop is closed). Each day has a small calculator that does the math against regular menu prices: Two for Tuesday (2 large cheese for $17.99), Wing It Wednesday ($.90 a wing vs 8 for $11.99), Throw Back Thursday ($4.50 small cheese), Free 2-liter Friday (pick two large pizzas), Bud Light Saturday ($1 off, 3-drink limit) and Sunday $10 large cheese with any large regular-priced pizza.

## What else the new site does

- Full menu on one page: 9 sections, 104 items, real photos for every section, category tabs and search.
- November Thanksgiving Pie card and the $9.50 lunch box (bulkie choices) card.
- Kids' pizza party section ($10 per child, no room fee) with a party-total calculator.
- Family story timeline (1987 Alex Korakas, 1991 Lori Bliss Hill takes over, 2001 new building opens July 4) and community list, #fuelyourcommunity.
- Live open / closed status, hours with today highlighted, both phone numbers, directions, Facebook and Instagram, link to the employment PDF.
- Sticky order / call bar on phones, Restaurant structured data, sitemap and robots.txt.

## Questions for the owner before launch

1. Is Monday still the only closed day, and are hours still 11 AM to 8 PM Tuesday to Sunday (all year, including summer)? The site only gives one set of hours.
2. What does a 2-liter cost? We show "free" on Friday but cannot show a dollar saving without the regular price.
3. The home page says "$12 Monthly Feature Pizzas", but the November Thanksgiving Pie is $14.99 (large only). Which is right? We show $14.99 and list "$12 monthly feature pizzas" as written on the old site.
4. Is there a limit on Throw Back Thursday ($4.50 small cheese) or Wing It Wednesday? We left limits out except the 3-drink limit on Saturday.
5. Do you want an online job application? Today we link to the PDF hosted on the old Wix site; send the PDF or an email address and we will host it or add a form.
6. Is there an email address for the shop? None is listed on the old site, so there is no contact form or email link. The old Get In Touch form has no address we can route to.
7. Gluten-free pizza is "12 inch" and the pizza sizes are 10" and 14"; please confirm calzone sizes (the old site just says small / large).
8. Does the Togo Order link (`togoorder.com/web/5102`) still work for pickup and delivery? Please confirm the pizza party booking should be by phone.

## Photo sources

All food photos come from the shop's own pages on https://www.enfieldhouseofpizza.com (the photo galleries on the Pizza & Calzones, Appetizers & Sides, Fresh Salads, Grinders & Wraps, Burgers and Pasta pages; Wix media files `ab4307_*`), resized and converted to WebP. The logo is the Wix file `ab4307_f6c0ac7b…~mv2.jpg` (EHOP logo). Left out: credit-card logos, the ServSafe badge, and the page background texture.

Fonts are open-license (SIL OFL); licence files ship in `assets/fonts/`.

## Not checked yet

- Real phones (iPhone Safari, Android Chrome) and a screen reader pass.
- Lighthouse scores on the hosted site.
- Placing an order: no order was placed.
- Some gallery photos are small (about 600 to 900 px wide); better originals would sharpen the hero.

## Launch steps

1. Get answers to the questions above and update `clients/enfield-house-of-pizza/data.json`, then rebuild with `python3 engine/build_enfield.py`.
2. Drag `sites/enfield-house-of-pizza/site` onto app.netlify.com/drop, then connect the domain.
