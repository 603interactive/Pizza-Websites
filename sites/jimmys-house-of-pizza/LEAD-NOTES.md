# Jimmy's House of Pizza: scroll-story concept

Built Oct 28, 2026 by 603 Interactive.

## The idea

The whole site opens on one pinned scene that makes a pizza as you scroll: dough stretched and tossed, sauce ladled in a spiral, mozzarella falling, toppings dropping in, the oven (brick arch, fire, embers, the crust browning and cheese blistering), then the pie cut and one slice pulled away with cheese strings and steam. Six captions ride along, with Order buttons at the start and the end. Everything in the scene is drawn in code; no AI or stock food photos. With reduced motion on, it shows the finished pie and the captions as plain sections.

## Files

- `preview.html`: one file, with the concept ribbon. Scroll slowly.
- `jimmys-house-of-pizza-netlify-site.zip` / `netlify-site/`: the launch-ready site.

## What we found on the current site

- The current site has one image in total (the cartoon mascot) and no food photos, so every section is text on flat color.
- The menu is a plain price table split across nine tabs; nothing shows what the food looks like or what makes it Jimmy's.
- Online ordering requires a phone-number sign-in before the menu even loads, and the site only says "pay in store, cash only" in one line of small caps.
- No story, no photos of the shop or the family, no social links, and the hours appear three times in slightly different formats.
- The mascot image is a photo of a screen (visible moiré) rather than the original file.

## Questions for the owner

1. Can we photograph the shop? With no real food photos, the new design uses an illustrated pizza scene; a photo shoot (a dozen pies, the oven, the counter, the family) would let us swap in real images.
2. The mascot image looks like a photo of a screen. Do you have the original file?
3. Is 'cash only' still correct for online orders picked up in store? Do you take cards at the counter?
4. What is the story behind Jimmy's: when did it open, who runs it today?
5. Do you deliver, or pickup and dine-in only?
6. Any specials (lunch, Monday pizza night, family deals) we should feature?

## Assets

- Mascot image: the shop's own `logo.png` (an AI-style cartoon; kept small in About only).
- Fonts: Boldonse and Bricolage Grotesque (SIL OFL), licence files in `assets/fonts/`.
- Everything else is drawn by `assets/site.js` on a canvas.

## Checked

- Desktop 1440 and phone 390: no sideways scroll, no script errors, all six stages render, menu search works.
- Not yet: real phones, screen reader pass, a test order.

## Launch

1. Answer the questions, update `clients/jimmys-house-of-pizza/data.json`, rebuild with `python3 engine/build_story.py`.
2. Netlify Drop for staging; check on a phone.
3. Their current site is a Next.js app with its own ordering at /onlineorders; keep that running and point only the home page at the new site.
