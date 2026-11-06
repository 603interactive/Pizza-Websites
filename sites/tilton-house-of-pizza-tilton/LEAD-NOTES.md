# Tilton House of Pizza (Tilton, NH): redesign concept

Built Nov 06, 2026 by 603 Interactive from the lead's content only. No AI-generated or stock food photos.

## Files
- `preview.html`: whole site in one file with a "design concept" ribbon.
- `site/`: launch-ready site (no ribbon). Drag onto app.netlify.com/drop.

## What we found on the current site (thopnh.com, Squarespace)
- "Order Now" only launches a phone call; no online ordering.
- Structured data lists the city as Laconia instead of Tilton.
- Instagram header icon points to the stock Squarespace profile, not @tiltonhouseofpizza; Facebook is not linked.
- Site hours (close 9 PM) disagree with Yelp/Restaurantji (close 10 PM).
- Two phone numbers are published with no explanation.
- Thin About/story content despite a large gallery; menu PDF is still named THOP-2024-menu.pdf.

## The idea: the guest check
The shop only takes orders by phone, so the menu is built around that. Every price is a tap target that adds the item to a diner-style "guest check" (sticky slip on desktop, bottom sheet on phones): quantities, a running subtotal before tax, a notes box for toppings ("2 Way: pepperoni and onions"), "Copy my check", and a Call button. Nothing is sent or paid on the page; it is a list to read over the phone, labelled as an estimate. Also: brick-red/black/gold palette taken from the logo, live open/closed status, today's hours, menu tabs + search, photo wall, directions, Facebook/Instagram links from the lead, Restaurant structured data with the correct city, sitemap, robots.txt.

## Menu accuracy
All 150+ items and prices come from the shop's own Squarespace menu pages in the lead (Pizza & Calzones, Grinders, Dinners incl. kids/desserts, Sides & Salads). No prices were invented. Notes on judgement calls:
- Pizza section heading is "Pizzas & Calzones"; sizes are labelled small 10" / large 16" only for the specialty pizzas in the lead. We applied the same labels to the build-your-own prices. Please confirm calzone sizes and prices.
- Garden/Greek/Tuna/Ham/Turkey salads show two prices with no size labels in the lead. They are shown as listed with a note, and the check records them as price-only lines.
- Wing counts/portion sizes are not in the lead, so none are stated.
- Prices come from a menu PDF named 2024; the page says prices may have changed.

## Hours and phones (not merged)
- Hours: shown as Wed-Sun 11 AM-9 PM (the shop's own site). Yelp/Restaurantji say 10 PM. Page notes the discrepancy; owner must pick one. Live open/closed uses 9 PM.
- Phones: (603) 286-3333 (used by the site's Order Now and Yelp) is the main call button; (603) 286-7181 (BBB primary) is shown as "also listed".

## IMAGE RIGHTS FLAG
All 18 gallery photos, the hero and the logo were downloaded from the shop's own website (thopnh.com), not Facebook or Instagram, so they appear to be the shop's own material. Still confirm with the owner that they hold the rights to the photos (photographer credit unknown) before launch. Unused: none of the 18 gallery photos were skipped; photo descriptions are written from what is visible, no dish names assumed beyond obvious ones. The logo is a JPG with a white border; a transparent PNG/SVG would be better.

## Questions for the owner
1. Is the closing time 9 PM or 10 PM, and are Monday/Tuesday really closed?
2. Which phone number do you want customers to call to order, and what is the other one for?
3. Are the prices on the 2024 PDF current? Can you send the current menu?
4. What are the two sizes on the salads, and what are calzone sizes/prices?
5. Do you offer delivery (Yelp suggests it) or want online ordering added later?
6. Is there a real story (who opened it, when, family name)? We did not invent one.
7. Public email address? Can we correct the Laconia city value and the Instagram link on the current site?
8. Do you have the logo as a transparent PNG/SVG, and are you the rights holder for the food photos?

## Not checked
Real phones, screen-reader pass, Lighthouse, geo coordinates (directions use a maps search link), clipboard behavior in every browser (falls back to the notes box).
