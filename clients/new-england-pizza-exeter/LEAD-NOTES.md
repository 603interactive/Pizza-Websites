# New England Pizza (Exeter, NH): redesign concept

Built Nov 06, 2026 by 603 Interactive from the lead's content only. No AI-generated or stock food photos.

## Files
- `preview.html`: whole site in one file with a "design concept" ribbon.
- `site/`: launch-ready site (no ribbon). Drag onto app.netlify.com/drop.

## What we found on the current site (nepizzaexeter.com, FoodTec brochure shell)
- Apache Tomcat 6.0.39 error pages; "Our Menu" on the shop domain is a hard 404.
- Homepage is a logo, one welcome paragraph and nav. Only image is a small logo.gif.
- No Facebook or Instagram found. Directions use a Yahoo Maps link. Ordering lives on foodtecsolutions.com with no branded menu.

## The idea: the craving finder
The shop has no photos, so the design is typographic: big New England wordmark, green/brick-red/cream from the logo, a checkered band, and a diner-style menu with dotted leaders. The one feature is a **craving finder**: ingredient chips (Chicken, Steak & beef, Ham/bacon/pepperoni, Tuna & seafood, Veggies, Feta & Greek, Buffalo & BBQ, No meat listed) plus search filter all 146 items across 12 sections at once (items must match every chip). It works from the written descriptions only, and "No meat listed" carries a note to ask the shop about allergies/diets. Also: live open/closed status, "Closed Tuesdays" ticket, sticky category rail (scrolling chips on phones), sticky call/order/directions dock on mobile, hours table, Restaurant structured data, sitemap, robots.txt. Ordering links only to the FoodTec URL from the lead.

## Menu accuracy (IMPORTANT)
The shop's own menu pages 404, so the menu is the lead's **third-party mirror** (findrestaurantmenu.com), flagged UNVERIFIED. The site says so in a banner at the top of the menu, marks every price with a dagger and a footnote, and has a "Show unverified prices" toggle (when off, items read "Call for price"). Edits made to the mirror text:
- Merged small/large pizza rows into one item with two prices; merged hot-sub small/large/wrap rows.
- Prices written as "a-b" on the mirror (cheese/white/veg/etc pizza, calzones, cold subs, French fries) are shown as ranges; we assumed small-to-large and said so in the section note. The calzone ranges were printed high-to-low ("$10.50-6.75") and we show them low-to-high.
- Expanded abbreviations and fixed typos: Ch->Cheese, Chix->Chicken, Sm/Lg->Small/Large, Dbl->Double, "D Coke"->Diet Coke, Fesca->Fresca, Diet Sunskit->Diet Sunkist, "Cf Dt Coke"->Caffeine-Free Diet Coke (a guess), Oj->Orange Juice, "10 Ppl"->"for 10". Verify.
- Oddities left as listed: Cheeseburger sub small $6.50 vs large $9.95; Steak & Cheese has no small price; the mirror's stray "$1" category held two Cordon Bleu pizzas, which we moved into Pizza; Mediterranean Salad and chicken parm pasta have no description.
- Delivery is unknown, so the site makes no delivery claim.

## IMAGE RIGHTS FLAG
Only one image: `nep-logo.jpg` (181x132, the red/green "New England Pizza Restaurant" banner around the storefront), taken from the shop's own site (img/logo.gif). It is the shop's own logo from its own site, so reuse risk is low, but confirm. It is tiny and a dithered GIF conversion, so it is shown at native size only (header and hero sticker); never enlarged. No social-sourced images; none were provided (Muse handles social photos separately). There is no food, storefront or interior photography, and none was invented.

## Questions for the owner
1. Please send the current menu with prices (or confirm the FoodTec menu is the source of truth). Are the mirror's prices and size ranges right?
2. Do you deliver, and through which apps? Is online ordering pickup only?
3. Are hours Mon/Wed/Thu 11-9, Fri/Sat 11-10, Sun 12-9, closed Tuesday still correct?
4. Is there a story to tell (who opened it, when)? The only copy we have is the welcome line.
5. Do you have a higher-resolution logo, and photos of the food, storefront or dining room we may use?
6. Public email address? Any Facebook or Instagram page to link?
7. Allergy and diet info: can you confirm which items are meat-free so the "No meat listed" filter can be verified?

## Not checked
Real phones, screen reader pass, Lighthouse, geo coordinates (directions use a maps search link, not the lead's Yahoo link). Whether FoodTec allows linking directly to menu categories.
