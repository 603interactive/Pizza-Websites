"""Writes clients/<slug>/data.json for Farmington HOP (ME), Lewiston HOP (ME), Village Pizza & Grill (Ashland), Ware HOP (MA), Athen's Pizza (VT) from the Pizza-Leads lead files only (2026-11-14; shop sites could not be fetched). usage: data_nov14.py"""
import json
from pathlib import Path
CL = Path(__file__).resolve().parent.parent / 'clients'
TH = lambda **k: dict(dict(surface='#ffffff', on_accent='#ffffff', head='Big Shoulders Display', body='Work Sans'), **k)
Q_COMMON = ['Do you have photos of your food and shop we may use?', 'Can you send your current menu as text with prices so we can list it?', 'What are your opening hours?']
def mk(slug, name, domain, street, city, region, postal, phone, tel, theme, tagline, seo_desc, about, badge, order_url, order_label, menu_note, facebook, findings, questions, delivery=''):
    from urllib.parse import quote_plus
    q = quote_plus(f'{name} {street} {city} {region} {postal}')
    d = dict(slug=slug, name=name, short=name, domain=domain, tagline=tagline, seo_title=f'{name} | Pizza in {city}, {region}', seo_desc=seo_desc, theme=theme, facebook=facebook, instagram='',
      order_any=order_url or 'tel:' + tel, about=about, extras=[], specials=[], delivery=delivery, order_url=order_url, order_label=order_label, menu_note=menu_note, badge=badge, gallery=[], hero_img='', logo='',
      locations=[dict(id=slug, name=city, street=street, city=city, region=region, postal=postal, phone=phone, tel=tel, hours=[], order=order_url or 'tel:' + tel, maps='https://www.google.com/maps/search/?api=1&query=' + q)],
      menu=[], findings=findings, questions=questions)
    (CL / slug).mkdir(parents=True, exist_ok=True); (CL / slug / 'img').mkdir(exist_ok=True)
    (CL / slug / 'data.json').write_text(json.dumps(d, indent=1, ensure_ascii=False)); print(slug)
NOMENU = lambda site, phone: f"The shop's current menu and prices are on its own website ({site}). This concept does not reproduce them: call {phone} for items and prices."
mk('farmington-house-of-pizza-me', 'Farmington House of Pizza', 'https://farmingtonhouseofpizza.net', '195 Broadway', 'Farmington', 'ME', '04938', '(207) 778-6867', '+12077786867',
   TH(bg='#fbf4e6', ink='#2a1d14', muted='#66584c', accent='#b3261e', accent2='#2f5233'),
   'Family pizzeria on Broadway in Farmington, Maine, open since 1988. Dine in, take out or call ahead.',
   'Farmington House of Pizza, 195 Broadway, Farmington ME. A family pizzeria open since 1988. Call (207) 778-6867.',
   ['Farmington House of Pizza is a family pizzeria at 195 Broadway in Farmington, Maine, open since 1988.', 'Call (207) 778-6867 to order.'], ['Family pizzeria', 'Since 1988', 'Farmington, ME'],
   '', 'Call to order', NOMENU('farmingtonhouseofpizza.net', '(207) 778-6867'), 'https://www.facebook.com/Farmington-House-of-Pizza-116622451717027',
   ['One-page vendor template (footer credit to eztouse.com, uploads dated 2018) with a footer still reading ©2022.', "The header 'Order Now!' is only the phone number; there is no online ordering.", 'The menu is a long text-only price list with no photos next to items.', "Generic SEO filler copy ('Pizza & More For Take-Out & Delivery in farmington, ME', lowercase town).", 'Every image has an empty alt attribute; the only real nav item is Home.'],
   ['Would you like online ordering? If so, through which service?'] + Q_COMMON + ['Is the Instagram account fhopmaine yours to link?'])
mk('lewiston-house-of-pizza-me', 'Lewiston House of Pizza', 'https://lewistonhouseofpizza.net', '95 Lincoln Street', 'Lewiston', 'ME', '04240', '(207) 786-2020', '+12077862020',
   TH(bg='#f7f3ea', ink='#1f2a30', muted='#56626a', accent='#1c4f8a', accent2='#b5301f'),
   'Pizza and Greek restaurant at 95 Lincoln Street in Lewiston, Maine, with catering and banquet rooms.',
   'Lewiston House of Pizza, 95 Lincoln Street, Lewiston ME. Pizza, Greek food, catering and banquet rooms. Order online or call (207) 786-2020.',
   ['Lewiston House of Pizza is a family pizza and Greek restaurant at 95 Lincoln Street in Lewiston, Maine, with catering and banquet rooms.', 'Order online or call (207) 786-2020.'], ['Pizza & Greek', 'Catering', 'Lewiston, ME'],
   'https://slicelife.com/restaurants/me/lewiston/04240/lewiston-house-of-pizza/menu', 'Order online', NOMENU('lewistonhouseofpizza.net', '(207) 786-2020'), 'https://www.facebook.com/Lewiston-House-of-Pizza-115140705164095/',
   ['One-page vendor template (footer credit to eztouse.com) with a footer still reading ©2022.', 'Only nav items are Home and Privacy Notice; catering, banquet rooms and the menu have no pages of their own.', "Confusing history: the page title says 'Best Pizza Since 2002' while the copy says 'Since 1998'. This concept states neither year.", 'Ordering is split between an unlabeled Slice icon and a Google Play link to a ChowNow app, with no single Order button.', "Every image has an empty alt attribute; daily specials say 'Fries of O-Rings'."],
   ['Which year did the shop open, 1998 or 2002?', 'Is the Slice link the one ordering path you want customers to use?', 'What do you offer for catering and what size are the banquet rooms?'] + Q_COMMON)
mk('village-pizza-grill-ashland', 'Village Pizza & Grill', 'https://www.villagepizzaashland.com', '116 Main Street', 'Ashland', 'NH', '03217', '(603) 968-9689', '+16039689689',
   TH(bg='#f8f2e4', ink='#2a2118', muted='#625549', accent='#9c2a1a', accent2='#2d5a45'),
   'Greek and Italian family restaurant on Main Street in Ashland, New Hampshire.',
   'Village Pizza & Grill, 116 Main Street, Ashland NH. Greek and Italian family restaurant. Call (603) 968-9689.',
   ['Village Pizza & Grill is a family Greek and Italian restaurant at 116 Main Street in Ashland, New Hampshire.', 'Call (603) 968-9689 to order.'], ['Greek & Italian', 'Family restaurant', 'Ashland, NH'],
   '', 'Call to order', "The shop's takeout menu is a PDF on its own website (villagepizzaashland.com). This concept does not reproduce it: call (603) 968-9689 for items and prices.", 'https://www.facebook.com/Village-Pizza-Grill-Ashland-473081259402420/',
   ["Hand-built one-page site from about 2019 (footer '© Parkview Pizza LLC', designer credit mjcamara.com).", "About text is out of date ('over 13 years', new owners 'as of December 2018'); this concept does not repeat it.", 'No online ordering, only a phone number, shown as 1-603-968-9689.', 'Long text-only menu; the printable PDF menu was last modified May 2023.', "Photo carousel images use placeholder alt text ('img 1') and raw camera file names."],
   ['Would you like online ordering? If so, through which service?'] + Q_COMMON + ['Is the printable PDF menu (May 2023) still current?'])
mk('ware-house-of-pizza-ma', 'Ware House of Pizza', 'https://www.warehouseofpizza.com', '197 West St, Unit A', 'Ware', 'MA', '01082', '(413) 544-1083', '+14135441083',
   TH(bg='#faf4e8', ink='#26201a', muted='#625648', accent='#b8321f', accent2='#2e5b3c'),
   'Pizza shop at 197 West Street in Ware, Massachusetts. Order online or call ahead.',
   'Ware House of Pizza, 197 West St Unit A, Ware MA. Order online or call (413) 544-1083.',
   ['Ware House of Pizza is a pizza shop at 197 West Street, Unit A, in Ware, Massachusetts.', 'Order online or call (413) 544-1083.'], ['Pizza shop', 'Online ordering', 'Ware, MA'],
   'https://www.warehouseofpizza.com/order', 'Order online', NOMENU('warehouseofpizza.com', '(413) 544-1083'), 'https://www.facebook.com/profile.php?id=61553245817064',
   ["Stock Menufy ordering template; the only homepage image is the logo.", "Vague copy ('Delicious Slices of Happiness!') with no story about the shop.", "A 'Contact Form' heading appears but no form exists; boilerplate listing fields ('Atmosphere: Chill') appear as content.", 'The same hours are repeated three times.', 'A second domain, warepizza.com, still appears in search results but opens a blank web-host page.'],
   ['Is the Facebook page found in public search (profile id 61553245817064) really yours?', 'Do you want warepizza.com pointed at the new site?', 'Do you have a logo file we may use?'] + Q_COMMON)
mk('athens-pizza-vt', "Athen's Pizza", 'https://www.athenspizzaonline.com', '83 Westminster St.', 'Bellows Falls', 'VT', '05101', '802-463-9777', '+18024639777',
   TH(bg='#f6f1e6', ink='#1d2a2f', muted='#55636a', accent='#1d5c8f', accent2='#c0392b'),
   "Athen's Pizza on Westminster Street in Bellows Falls, Vermont. Order online or call ahead.",
   "Athen's Pizza, 83 Westminster St., Bellows Falls VT. Order online or call 802-463-9777.",
   ["Athen's Pizza is a family restaurant at 83 Westminster St. in Bellows Falls, Vermont.", 'Order online or call 802-463-9777.'], ['Family restaurant', 'Bellows Falls, VT'],
   'https://athenspizza.hungerrush.com', 'Order online', NOMENU('athenspizzaonline.com', '802-463-9777'), 'https://www.facebook.com/AthensPizzaBellowFalls/',
   ['No menu page on the site; nav is Home, Story, Gallery, Order Online and Apply Now, so the menu is only visible inside the ordering system.', "Stale pandemic-era copy ('now open for dining in!'), odd leftover 'from a Dorm' ordering instructions and a capitalized VPN warning dominate the homepage.", "A scrolling 'now hiring' banner repeats three times.", 'No social links on the site.'],
   ['Are you hiring? We can add an Apply link.'] + Q_COMMON + ['Is the HungerRush ordering link correct and current?'])
