# Supreme House of Pizza & Teddy's Lounge (Raymond, NH): redesign concept

Built Nov 04, 2026 by 603 Interactive from the shop's own content only (lead brief, website menu, public Facebook page). No AI-generated or stock food photos.

## Files

- `preview.html`: the whole site in one file, with a "design concept" ribbon. Open it in any browser to show the owner.
- `site/`: the launch-ready site (no ribbon). Drag the folder onto app.netlify.com/drop.

## What we found on the current site

- Dated template site (old html5shiv link that now 404s, IE7 stylesheets); viewport tag blocks pinch-zoom on phones.
- Every menu page is a plain text price table; only four tiny generic stock photos, none the shop's own.
- Homepage is a wall of seasonal hours and four "View Menu" buttons; nothing about the shop or Teddy's Lounge.
- "Daily lunch specials" is advertised but none are listed; the catering page shows "$CALL" for everything and links a 2014 Word PDF with old hours.
- Menu typos and inconsistencies (Glunten, Mozarella, Rueben, Potatos); gluten-free pizza has two prices; a Parmesan calzone add-on price is cut off.
- No Facebook link, a fax number shown as a main contact, ordering on a separate differently-branded e-tab app.

## The one big idea

Name Your Price: the hero is a budget dial. Slide to what you want to spend (out the door) and see every real menu price that fits, with the 9% NH meal tax already counted. Tap items into "My order"; the tray shows food, tax, total, what is left, and a delivery meter against the shop's own rule (evening home delivery: $25 minimum, $3 charge). "Copy my order" makes a text to read over the phone. All 223 prices come straight from the shop's menu; nothing is invented.

## What else the new site does

- Live open / closed status with the seasonal hours (Oct 1 to Mar 31 and Apr 1 to Sep 30), current season highlighted.
- Full menu with tabs, search and dotted-leader price lines, readable on a phone.
- Teddy's Lounge section with real photos, parking directions, catering section (items and serving sizes only, no prices), two real customer quotes, sticky call / order bar on phones, Restaurant structured data, sitemap and robots.txt.

## Info we could not find

- Hours: lounge closing time. Owner, founding year and shop history. Email address.
- Actual daily lunch specials. Catering prices (website says "$CALL"; the PDF prices are from 2014 and were not used).
- Instagram (none found).

## Questions for the owner before launch

1. Are the seasonal hours still right (Mon-Thu 10:30-8:30, Fri-Sat 10:30-9:00 Oct to Mar; 9:00 / 9:30 Apr to Sep; closed Sunday)? What time does Teddy's Lounge close, and does it really open daily at 10:30 AM?
2. Delivery: is it "after 4 PM, $25 minimum, $3 charge, about 5 miles" for homes and all day for businesses? Does the $25 minimum count food before tax?
3. Gluten-free pizza: is it $12.50 or $16.95 (the menu shows both)? Is it still offered? Add-on price for mushrooms, onions and peppers on Parmesan calzones was cut off on the site ("Large $3."); what is it?
4. Which of the hidden or unverified items are real: gluten-free block, "Super Pizza Specials", chicken bacon ranch and Greek-style pizza, kabob salad, seasonal homemade soups?
5. What are the daily lunch specials and the catering prices today?
6. Seafood and Surf 'N Turf are "market price / call"; keep it that way?
7. Who runs the shop, since when, and is there a story to tell? Is there an email we can publish?
8. Do you want to keep e-tab for ordering? Every Order button links to it.
9. Facebook photos: please confirm we may use them (storefront, dining room, lounge, catering trays, burger, pizzas, bike night).

## Photo sources

All photos are the shop's own, from its Facebook page and cover photo (see the lead brief). Left out: the 2014 catering PDF, a customer's steak-tip-salad photo, text graphics, the four tiny stock website photos. Fonts are open-license (SIL OFL); licence files ship in `assets/fonts/`.

## Not checked yet

- Real phones (iPhone Safari, Android Chrome) and a screen reader pass; Lighthouse; placing an order.

## Launch steps

1. Get answers above, update `clients/supreme-house-of-pizza-raymond/data.json`, rebuild with `python3 engine/build_supreme.py`.
2. Drag `site/` onto Netlify Drop for a staging link; check on a phone.
3. Point the shop's domain at Netlify; submit `sitemap.xml` in Search Console.
