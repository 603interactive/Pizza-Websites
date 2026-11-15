"""Writes clients/<slug>/data.json for Camden HOP (ME), Cleghorn HOP (MA), Leominster HOP (MA), Templeton HOP (MA) from the Pizza-Leads lead files only (2026-11-15). usage: data_nov15.py"""
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
mk('camden-house-of-pizza-me', 'Camden House of Pizza', 'https://camdenmainepizza.com', '12 Mechanic Street', 'Camden', 'ME', '04843', '207-230-2464', '+12072302464',
   TH(bg='#f6f1e6', ink='#1e2a33', muted='#55616a', accent='#1f5a7a', accent2='#b8402a'),
   'Pizza shop at 12 Mechanic Street in Camden, Maine. Order online or call ahead.',
   'Camden House of Pizza, 12 Mechanic Street, Camden ME. Order online or call 207-230-2464.',
   ['Camden House of Pizza is a pizza shop at 12 Mechanic Street in Camden, Maine.', 'Order online or call 207-230-2464.'], ['Pizza shop', 'Camden, ME'],
   'https://order.online/store/26344237', 'Order online', NOMENU('camdenmainepizza.com', '207-230-2464'), 'https://www.facebook.com/517253391795633',
   ['The menu page is a single phone photo of the paper menu, hard to read, search or zoom on a phone.', "Stock WordPress default theme: footer still shows placeholder items (Blog, About, FAQs, Authors, Events) and 'Twenty Twenty-Five' appears in page text.", "Site icon is a cropped 2019 screenshot file.", "Homepage slideshow says 'This slideshow requires JavaScript' and the page has only two images.", "A public review says the customer 'tried ordering online but the website would not cooperate'."],
   ['Is the order.online link the one ordering path you want customers to use?'] + Q_COMMON + ['The shop is on a side street: what landmark should directions mention?'])
mk('cleghorn-house-of-pizza-ma', 'Cleghorn House of Pizza', 'https://www.cleghornpizza.com', '416 Franklin Rd.', 'Fitchburg', 'MA', '01420', '978-345-7558', '+19783457558',
   TH(bg='#faf3e6', ink='#2a1f18', muted='#64564a', accent='#a82a1c', accent2='#2c5a3a'),
   'Pizza shop at 416 Franklin Road in Fitchburg, Massachusetts. Call ahead to order.',
   'Cleghorn House of Pizza, 416 Franklin Rd., Fitchburg MA. Call 978-345-7558 or 978-345-7559.',
   ['Cleghorn House of Pizza is a pizza shop at 416 Franklin Rd. in Fitchburg, Massachusetts.', 'Call 978-345-7558 or 978-345-7559 to order.'], ['Pizza shop', 'Fitchburg, MA'],
   '', 'Call to order', NOMENU('cleghornpizza.com', '978-345-7558'), 'https://www.facebook.com/CleghornPizza/',
   ["Homepage still shows an out-of-date notice: 'We will be closed Aug. 16 - Sep 16. Reopening Sep 17, 2025.' This concept does not repeat it.", 'No online ordering anywhere on the site; customers have to call.', 'Homepage is very thin: a two-sentence welcome, the address and phone numbers.', 'Menu is a long text page plus a printable PDF, with no food photos.'],
   ['Would you like online ordering? If so, through which service?', 'Is the shop open now, and what are the hours?', 'How many years has the shop been open (the lead notes say 30+)?'] + Q_COMMON,
   delivery='')
mk('leominster-house-of-pizza-ma', 'Leominster House of Pizza', 'https://leominsterhouseofpizza.com', '753 Central Street', 'Leominster', 'MA', '01453', '(978) 534-4222', '+19785344222',
   TH(bg='#f8f2e4', ink='#231d1a', muted='#5f5650', accent='#a3291d', accent2='#2a5640'),
   'Pizza shop at 753 Central Street in Leominster, Massachusetts. Order online or call ahead.',
   'Leominster House of Pizza, 753 Central Street, Leominster MA. Order online or call (978) 534-4222.',
   ['Leominster House of Pizza is a pizza shop at 753 Central Street in Leominster, Massachusetts.', 'Order online or call (978) 534-4222.'], ['Pizza shop', 'Online ordering', 'Leominster, MA'],
   'https://leominsterhouseofpizza.foodtecsolutions.com/ordering/intro', 'Order online', NOMENU('leominsterhouseofpizza.com', '(978) 534-4222'), 'https://facebook.com/121303407885354',
   ['Web presence is split across two sites: a stock FoodTec ordering template on its own domain and a separate free GoDaddy subdomain site.', "The GoDaddy homepage is one line of welcome text with a single image and GoDaddy's default app logo.", "The own-domain site lists the address as just 'Central St' with no street number, and its main pitch is a FoodTec 'Register' signup box.", 'Neither site has an about story, photos of the food, or social links.'],
   ['Do you want the GoDaddy site retired in favor of one site on leominsterhouseofpizza.com?', 'Is the FoodTec ordering link current?'] + Q_COMMON)
mk('templeton-house-of-pizza-ma', 'Templeton House of Pizza', 'https://templetonhouseofpizza.com', '5 Elm St', 'Baldwinville', 'MA', '01436', '(978) 652-5114', '+19786525114',
   TH(bg='#f9f3e5', ink='#27201a', muted='#625649', accent='#b0301e', accent2='#2d5a42'),
   'Pizza shop at 5 Elm Street in Baldwinville (Templeton), Massachusetts. Order online or call ahead.',
   'Templeton House of Pizza, 5 Elm St, Baldwinville MA. Order online or call (978) 652-5114.',
   ['Templeton House of Pizza is a pizza shop at 5 Elm St in Baldwinville, part of Templeton, Massachusetts.', 'Order online or call (978) 652-5114.'], ['Pizza shop', 'Baldwinville, MA'],
   'https://templetonpizza.24seveneats.com/', 'Order online', NOMENU('templetonhouseofpizza.com', '(978) 652-5114'), 'https://www.facebook.com/profile.php?id=61585594960564',
   ['Generic vendor template (credited to 24SevenEats) with copy shared almost word for word with another shop\'s site.', "Leftover filler copy that does not fit a pizza shop (a 'robust sandwiches menu' line about feeding a crowd).", "Character-encoding glitch on the homepage ('we\u00e2\u20ac\u2122re' instead of 'we're').", "Several homepage links go nowhere (href='#') and images use stock template file names."],
   ['How long has the shop served Templeton and Baldwinville?', 'Is the 24SevenEats ordering link the one you want customers to use?'] + Q_COMMON)
