# Peterborough Pizza Barn: redesign concept

Built Nov 09, 2026 by 603 Interactive from the shop's own content only. No AI-generated or stock food photos.

## Files

- `preview.html`: the whole site in one file, with a "design concept" ribbon.
- `site/`: the launch-ready site (no ribbon). Drag the folder onto app.netlify.com/drop.

## What we found on the current site

- One-page WordPress site with a single 2016 text banner, no food photos; menu links point to /menu/ which redirects to the homepage.
- Delivery only by calling or emailing the separate SweenEats service; no online ordering exists, so the site is phone-order only.
- Source menu lists "Clam Strips" twice at $11.50 (shown once) and the Eggplant price lacked a $ sign ($11.75 assumed).

## What the new site does

- Full menu as live text with prices, category tabs and search; live open/closed status and today's hours; directions; sticky call bar on phones.
- Shared `plain` template (engine/templates/plain.*) with this shop's own palette. Phone ordering only: no ordering link could be verified, so none was invented.
- Restaurant structured data (no OrderAction or price range).

## Image rights

No photos on the source site; the 2016 text banner was not reused. Site is typographic until the owner supplies photos.

## Questions for the owner before launch

- Is the menu current? Prices were copied from the live site.
- Do you have food or shop photos we may use? None were on the site.
- What does the unlabeled Milk / Chips / Lemonade multi-price list mean (sizes)?
- Is the gluten-free pizza priced differently?
- Which flavors of ice cream are served?
