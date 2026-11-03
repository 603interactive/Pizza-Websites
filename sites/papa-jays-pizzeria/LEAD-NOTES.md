# Papa Jay's Pizzeria: redesign concept

Built Nov 3, 2026 by 603 Interactive from the shop's own content only. No AI-generated or stock food photos added by us.

## Files

- `preview.html`: the whole site in one file, with a "design concept" ribbon. Open it in any browser to show the owner.
- `site/`: the launch-ready site (no ribbon). Drag the folder onto app.netlify.com/drop.

## What we found on the current site

- Drupal theme demo slides ("Drupal 8 Theme", "Zymphonies Theme") with Lorem Ipsum are still live on the homepage; the Contact Us and Hiring pages are empty headings.
- There is no menu on papajays.net at all. The full menu lives only on the shop's web-ordering site (papajay.weborder.net), which is where we took every item and price.
- The "Order Now" button sends people to Slice, and Slice's page says Papa Jay's is **no longer active on Slice**. The other button (papajay.weborder.net) works and is the only one we link.
- The street address is never written on the site (only a Google Map). The ordering site gives it: 18 Broadway, Dover, NH 03820.
- Hours table says "9:30-11:00" with no AM/PM. The ordering site says 9:30 AM to 11:00 PM; we show 9:30 AM to 11 PM Monday to Friday and 10 AM to 11 PM Saturday and Sunday.

## The one big idea

**The Crowd Planner.** Papa Jay's offers catering and sells everything from a 12" medium to a 20" jumbo ("biggest pizza in Dover"). The planner takes headcount and appetite (2, 3 or 4 slices each) and a pizza (cheese or any specialty), then finds the cheapest mix of the shop's real sizes and prices to cover everyone. It shows the order ticket, total, price per person, how much cheaper it is than buying all large pizzas, and buttons to order online, call or email the plan to papajays@comcast.net. Assumption: a slice is one eighth of a 14" pie (about 19 sq in); Large and X-Large are counted as 14" and 16" because the menu does not give their diameters.

## What else the new site does

- The whole menu on one page for the first time: 15 sections, about 160 items (pizza, specialty pizzas by size, calzones, wings, appetizers, burgers, hot / chicken / cold subs, salads, pasta, kids, sweets, chips and drinks, beer delivery), "track" tabs and search.
- "What Papa Jay's is known for" cards (steak tip sub, fresh wings, Italian sub, jumbo pizza) taken from Jason Parker's own homepage letter.
- Delivery map of the four towns plus catering, owner note, hours with today highlighted, address, directions, phone, email, Facebook.
- Live open / closed status, sticky order / call bar on phones, Restaurant structured data, sitemap and robots.txt.
- Spelling fixed on the menu (for example "Mozzeralla", "Ceaser", "marinera", "Chedder").

## Questions for the owner before launch

1. Wing prices are not shown anywhere we could read: the ordering site lists fresh and boneless wings (6, 10, 15, 20, 25 pieces) without prices in the menu list. Please send the price per count and we will add them. The same goes for the lunch deals (11 AM to 4 PM, online only), which the ordering site shows as empty.
2. What are the diameters of Large and X-Large pizzas? We assumed 14" and 16".
3. Menu price oddities to check: Hawaiian is $24.99 large but $21.99 extra large; White Pizza is $14.99 / $17.99 / $19.99; Gutbuster is medium only. Several items say "price varies on order size" (fries, mozzarella sticks, chili fries, tenders, poppers) so we show "from" prices. Please send the full size prices.
4. Confirm hours: 9:30 AM to 11 PM Monday to Friday and 10 AM to 11 PM Saturday and Sunday? Any holiday closures?
5. Please confirm Slice is no longer used. We removed it. Is papajay.weborder.net the one ordering link you want?
6. Real photos: the only images on the current site are four banner slides with text baked in (some look like stock photos). We used one cropped pizza picture from the "Delivered Hot & Fresh" slide. Please send real photos of your food, the shop on Broadway and the team.
7. Is papajays@comcast.net the right public address for catering and job questions? Do you want a job application form?
8. Which other towns do you cater to, and is there a minimum order or lead time for catering and delivery?
9. Should the beer delivery list stay public? It is included with the state-law note ("food must be ordered with beer").
10. Logo: the file on the current site is tiny (105 x 60 px). Please send a larger logo.

## Photo sources

- `pizza.webp` ← cropped (590 x 300) from https://www.papajays.net/sites/default/files/slide_02.jpg (the "Delivered Hot & fresh" homepage slide), cropped to remove the baked-in text. It may be a stock image; the owner should confirm.
- `logo.png` ← https://www.papajays.net/sites/default/files/LogoMain_1.png

Left out on purpose: the other three homepage slides (text baked in over the food, stock look), the car and flag icons, and the Slice button image.

Fonts are open-license (SIL OFL); licence files ship in `assets/fonts/`.

## Not checked yet

- Real phones (iPhone Safari, Android Chrome) and a screen reader pass.
- Lighthouse scores on the hosted site.
- Placing an order: no order was placed.
- Item pages on the ordering site load sizes and options with scripts, so size prices for several items could not be read.

## Launch steps

1. Get answers to the questions above and update `clients/papa-jays-pizzeria/data.json`, then rebuild with `python3 engine/build_papajays.py`.
2. Drag `sites/papa-jays-pizzeria/site` onto app.netlify.com/drop, then connect the domain.
