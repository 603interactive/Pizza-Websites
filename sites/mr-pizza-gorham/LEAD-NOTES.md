# Mr. Pizza Restaurant & Tavern (Gorham, NH): redesign concept

Built Nov 05, 2026 by 603 Interactive from the shop's own content only. No AI-generated or stock food photos.

## Files
- `preview.html`: whole site in one file with a "design concept" ribbon.
- `site/`: launch-ready site (no ribbon). Drag onto app.netlify.com/drop.

## What we found on the current site (mrpizzanh.net, GoDaddy Website Builder)
- Two pages only (Home, Menu). Home is one headline repeated plus an address block.
- The Menu page is two phone photos of the paper menu: no text, so prices are unreadable on a phone and not searchable.
- Only "Open today 11:00 am - 08:00 pm"; no weekly hours. No online ordering despite "Delivery & Takeout" in the title.
- Hobbit's Tavern history and atmosphere, a real selling point, is not on the home page.

## The one big idea: Build your pie
A price calculator built on the shop's real pricing rules: cheese pie $10 (10") / $16 (16"), each topping +$1 / +$2, extra cheese +$4, with the shop's real topping list. The total updates live and a button calls the shop. Also: full tabbed, searchable menu (6 sections, transcribed from the two menu photos and checked against them), Hobbit's Tavern story using the menu's own words, address, tel: link, directions link, Facebook link, Restaurant structured data, sitemap, robots.txt.

## Content decisions
- No live open/closed status and no weekly hours table: weekly hours are unknown, so the site says to call to confirm. JSON-LD has no opening hours.
- No online-order button: the lead found none. All order buttons are tel: links. Structured data OrderAction points to the site's own #build section.
- Specialty pizza, entree, appetizer and sandwich descriptions come from the menu photos (site-02/03). Words obscured by glare were dropped.
- Not used: the older menu in the Facebook photos (fb-01..03) shows different/older items and prices (e.g. fried haddock $20); the site uses the current menu from the website.
- Logo: mrpizzanh.net logo image, unaltered.

## IMAGE RIGHTS FLAG
Photos from the shop's Facebook page, reuse permission UNCONFIRMED (need owner OK before launch): fb-05 (pizza, hero), fb-04 (hot chocolate), fb-06 (fall drinks chalkboard), fb-07 (cider cocktail), fb-08 (pot roast; used as Comfort Food tab image), fb-09 (smash burger), fb-10 (lobster roll), fb-11 (martini). Not used: fb-01, fb-02, fb-03 (phone photos of older paper menus). The logo is from the shop's own website.

## Questions for the owner
1. What are the full weekly hours (site shows only 11 am - 8 pm "today")? Seasonal changes?
2. Do you deliver? Area, fees, minimums? Takeout by phone only?
3. Do toppings add to House Specialty pizzas, and do sauces (Alfredo, BBQ, garlic oil) change the price? The calculator covers only the cheese pie plus toppings.
4. Butcher's Cut and Soup du Jour prices (shown as "Market price" / "Price will vary").
5. Is the Facebook page the right one to link? Instagram (@mrpizza_160) was unavailable; is it live?
6. Do you want Hobbit's Tavern drinks/beer/wine and hours listed, and do you have newer photos of the dining room and building (none found)?
7. Please confirm the Facebook photos are yours to reuse.
8. Email address for the site? None found.

## Not checked
Real phones, screen reader pass, Lighthouse on the hosted site, geo coordinates (directions use a maps search link, no embed), the ordering process beyond phone.
