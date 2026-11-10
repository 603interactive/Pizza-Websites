"""Writes clients/<slug>/data.json for Millo's, Fire 21, Lancaster House of Pizza, Pizzeria Roma, Family Pizza Pittsfield from each shop's own public site text (fetched 2026-11-10). usage: data_batch.py"""
import json
from pathlib import Path
CL = Path(__file__).resolve().parent.parent / 'clients'
def it(n, p='', d=''):
    p = [p] if isinstance(p, str) else list(p)
    return dict(name=n, prices=[x for x in p if x], desc=d)
def money(*xs): return ['$%.2f' % x for x in xs]
def cat(name, items, note='', head=()): return dict(cat=name, img='', note=note, head=list(head), items=items)
def mk(slug, name, short, domain, street, city, region, postal, phone, tel, hours, theme, tagline, seo_title, seo_desc, about, badge, maps_q, menu=(), specials=(), extras=(), delivery='', order_url='', order_label='', menu_note='', facebook='', findings=(), questions=()):
    d = dict(slug=slug, name=name, short=short, domain=domain, tagline=tagline, seo_title=seo_title, seo_desc=seo_desc, theme=theme, facebook=facebook, instagram='', order_any=order_url or 'tel:' + tel,
      about=list(about), extras=list(extras), specials=list(specials), delivery=delivery, order_url=order_url, order_label=order_label, menu_note=menu_note, badge=list(badge), gallery=[], hero_img='', logo='',
      locations=[dict(id=slug, name=city, street=street, city=city, region=region, postal=postal, phone=phone, tel=tel, hours=hours, order=order_url or 'tel:' + tel,
        maps='https://www.google.com/maps/search/?api=1&query=' + maps_q)], menu=list(menu), findings=list(findings), questions=list(questions))
    (CL / slug).mkdir(parents=True, exist_ok=True); (CL / slug / 'img').mkdir(exist_ok=True)
    (CL / slug / 'data.json').write_text(json.dumps(d, indent=1, ensure_ascii=False)); print(slug, sum(len(c['items']) for c in menu))
TH = lambda **k: dict(dict(surface='#ffffff', on_accent='#ffffff', head='Big Shoulders Display', body='Work Sans'), **k)
ALL = [0, 1, 2, 3, 4, 5, 6]

# ---------------- Millo's
two = lambda a, b: money(a, b)
sp = [it(n, two(13.95, 18.95)) for n in ["Millo's Choice", 'Neapolitan', 'Buffalo Chicken', 'New Englander', "Millo's Special", 'BBQ Chicken Pizza', 'Vegetarian Pizza', 'Pesto Chicken Pizza', 'Mediterranean Pizza']]
sp.append(it('Hawaiian Pizza', two(12.95, 14.95)))
sp += [it(n, two(13.95, 18.95)) for n in ['Chicken Broccoli Alfredo', 'Greek Pie', 'Shrimp Scampi', 'White Greek Pizza', "Millo's Meat Lovers", 'Chicken Carbonara', 'Feta Bruchetta', 'Picante (Spicy Pizza)']]
sp.append(it('Bianca', two(9.50, 13.50)))
sp += [it(n, two(13.95, 18.95)) for n in ['Shrimp Saganaki', 'Chicken Bruschetta', 'Athenian']] + [it('Taco Pizza', two(13.95, 18.95))]
sp.append(it('Mediterranean Veggie', '', 'Onions, peppers, broccoli, tomatoes, black olives, spinach, extra virgin olive oil, feta, no red sauce. Price not shown on the shop menu: call to ask.'))
sp += [it('Chicken Artichoke', two(13.95, 18.95)), it('Pizza Artichoke', two(13.95, 18.95))]
millo = [
 cat('Specials', [it('Large Cheese Pizza', '$10.00'), it('Small Cheese Pizza', '$6.95'), it('Large Athenian Pizza', '$16.95'), it('Classic Italian Sub', '$8.95'), it('Chicken Rancho Sub', '$8.95'), it('Chicken Parm Dinner', '$14.95'), it('Mix Chicken Grill Dinner', '$14.95')], 'As listed on the shop\'s Specials page (no dates given).'),
 cat('Pizza', [it('Cheese', two(7.95, 13.50)), it('1 Topping', two(10.50, 14.50)), it('2 Toppings', two(11.25, 15.50)), it('3 Toppings', two(12.95, 16.75)), it('4 Toppings', two(13.25, 17.50)), it('Extra Cheese', two(2.50, 4.25))], 'Brick oven pizza, thin crust available. Two prices are listed for each pizza, as on the shop menu.'),
 cat('Specialty Pizza', sp, 'Brick oven, thin crust available. Two prices are listed for most pizzas, as on the shop menu.'),
 cat('Calzones', [it(n, '$13.50') for n in ['Ham', 'Italian', 'Veggie', 'Meatball', 'Sausage', 'Fresh Grilled Chicken', 'Chicken Parmesan', 'Chicken & Broccoli Alfredo', 'Spinach & Feta Cheese']] + [it('Steak', '$15.25'), it('Create Your Own Calzone', '$15.25')], 'All with red sauce except the Alfredo calzones.'),
 cat('Subs', [it(n, '$9.95') for n in ['Italian', 'Ham', 'Turkey', 'Veggie', 'Roast Beef', 'Tuna', 'Grilled Chicken', 'Chicken Fingers', 'B.L.T.', 'Meatball', 'Sausage', 'Hot Pastrami', 'Fried Haddock']] +
   [it('Steak Tip', '$14.50', 'Steak sub'), it('Cheese Steak', '$11.50'), it('Pepper Steak', '$11.50'), it('Onion Steak', '$11.50'), it('Mushroom Steak', '$11.50'), it('Deluxe Steak', '$11.50'), it('Steak Bomb', '$12.50')] +
   [it('Chicken Rancho', '$11.50'), it('Buffalo Chicken', '$11.50'), it('BBQ Roast Beef', '$11.50'), it('Cheeseburger Deluxe', '$11.50'), it("Millo's Steak Tip", '$14.50'), it('Grilled Chicken Gyro', '$11.50'), it('Steak Tip Gyro', '$14.50'), it('Chicken Santorini', '$11.50'), it('Greek Supreme', '$11.50')],
   '12" subs, hot or cold, with mayo or oil, tomatoes, onions, pickles and lettuce. Steak and specialty subs are listed after the classics.'),
 cat('Dinners & Pasta', [it('Chicken Mediterranean', '$18.95', 'With ziti and garlic bread'), it('Mixed Chicken Grille', '$17.95', 'With rice'), it('Chicken Fingers', '$15.95', '6 pieces with fries'), it('Steak Tip', '$19.95', 'With rice or fries'), it('Gyro Platter', '$15.95'), it('Grecian Delight', '$18.95', 'With rice'), it('Shrimp Mediterranean', '$18.95', 'With rice'),
   it('Pasta with sauce', '$11.95', 'Ziti or linguini, garlic bread'), it('Pasta with meatballs or sausage', '$14.95', 'Ziti or linguini, garlic bread'), it('Baked Spaghetti', '$16.50', 'Meatballs or sausage, mozzarella, garlic bread'), it('Chicken Broccoli Alfredo', '$17.95'), it('Chicken Spinach Alfredo', '$17.95'), it('Veal Parmigiana', '$17.95'), it('Chicken Parmigiana', '$17.95'), it('Eggplant Parmigiana', '$17.95'), it('Chicken Scampi', '$18.95'), it('Shrimp Scampi', '$18.95'), it('Shrimp Alfredo', '$18.95')],
   'Dinners come with a side garden or Caesar salad, except Chicken Fingers. Pasta is ziti or linguini.'),
 cat('Burgers & Kids', [it(n, '$12.95') for n in ['Classic American', "Millo's Burger", 'BBQ Burger', 'Bacon Blue Burger']] + [it('Chicken Fingers', '$8.25', 'With fries'), it('Spaghetti & Meatballs', '$8.25'), it('Cheeseburger', '$8.25', 'With fries')],
   'Fresh Angus burgers come with fries or onion rings. Kids menu is for ages 12 and under, dine in only, and includes a fountain drink.'),
 cat('Appetizers & Sides', [it('Garlic Bread', '$4.95'), it('Garlic Bread With Cheese', '$7.25'), it('Nachos', '$9.95', 'Add chicken or ground beef +$3.95'), it('Fried Mushrooms', '$11.95'), it('Mozzarella Sticks', '$9.50', '8 pieces'), it('Cheese Fries', '$12.50'), it('Greek Style Fries', '$9.50'), it('Chicken Tenders', '$10.95', '6 pieces'), it('Chicken Buffalo Fingers', '$10.95', '6 pieces'), it('Chicken Wings', '$13.00'), it('Chicken Buffalo Wings', '$13.00'), it('The Sampler Plate', '$16.95'), it('Sweet Potato Fries', '$8.50'),
   it('Angus Side Burger', '$10.50', '8 oz'), it('French Fries', two(5.50, 7.25)), it('Onion Rings', '$7.25'), it('Chicken Burger', '$8.95', 'Fried or grilled'), it('Jalapeño Poppers', '$9.95', '8 pieces')]),
 cat('Salads', [it('Tossed Salad', two(3.99, 7.95)), it('Greek Salad', two(6.50, 10.50)), it('Chef Salad', '$11.95'), it('Grilled Chicken Salad', '$11.95'), it('Tuna Salad', '$11.95'), it('Steak Tip Salad', '$16.95'), it('Mediterranean Salad', '$12.95'), it('Shrimp Salad', '$14.95'), it('Caesar Salad', '$6.90', 'Add chicken for $11.95'), it('Buffalo Chicken Salad', '$12.95'), it('Taco Salad', '$12.95'), it('Monterey Rancho', '$12.95'), it('Caprese Salad', '$12.95')]),
]
mk('millos-pizza-and-grill-barrington', "Millo's Pizza & Grill", "Millo's", 'https://millospizza.com', '575 Franklin Pierce Highway', 'Barrington', 'NH', '03825', '(603) 664-8871', '+16036648871',
   [dict(dow=ALL, open='11:00', close='21:00')], TH(bg='#fff7ec', ink='#2a1a12', muted='#6b5648', accent='#b3321a', accent2='#9a5b0c'),
   'Brick oven pizza, calzones, subs, burgers and Greek favorites on Franklin Pierce Highway in Barrington, NH.',
   "Millo's Pizza & Grill | Brick Oven Pizza, Subs & Greek Favorites in Barrington, NH",
   "Millo's Pizza & Grill, 575 Franklin Pierce Highway, Barrington NH. Brick oven pizza, calzones, subs, burgers, pasta and Greek favorites. Open daily 11am to 9pm. Call (603) 664-8871.",
   ["Millo's Pizza & Grill is on Franklin Pierce Highway in Barrington, NH. The kitchen makes brick oven pizza (thin crust available), calzones, subs, burgers, pasta dinners and Greek favorites such as gyros and Athenian pizza.", "The whole menu is below as live text so you can read it on your phone. For orders and delivery questions, call the shop."],
   ('Brick oven', 'Pizza', 'Barrington, NH'), "Millo's+Pizza+%26+Grill+575+Franklin+Pierce+Highway+Barrington+NH+03825", menu=millo,
   specials=['Large Cheese Pizza $10.00', 'Small Cheese Pizza $6.95', 'Large Athenian Pizza $16.95', 'Classic Italian Sub or Chicken Rancho Sub $8.95', 'Chicken Parm Dinner or Mix Chicken Grill Dinner $14.95'],
   delivery='The shop offers delivery. Call to ask whether your address is covered.',
   findings=['GoDaddy Website Builder site; homepage was nearly empty (one "A Few Of Our Dishes" caption, address and hours).', 'No online ordering and no social links on the site.', 'Menu and Specials pages were long plain price lists; typos in the source ("Caeser", "cucumberes") were not carried over.', 'No food or shop photos could be collected and cleared: the homepage photo was not retrievable, so this concept is typographic. No photos were published.'],
   questions=['Do you have photos of your food and shop we may use? None were published in this concept.', 'The menu prints two prices for most pizzas with no size labels: which sizes are they (e.g. small/large)?', 'Mediterranean Veggie pizza shows a check mark instead of a price: what is the price?', 'Do you want an online-ordering link? None exists, so the site is phone-order only.', 'Closing time: the homepage says "Open til 9:00pm". Is that every day?', 'What areas do you deliver to?', 'Do you have an About story or an owner name you want shown?'])

# ---------------- Fire 21
mk('fire-21-pizza-conway', 'Fire 21 Pizza', 'Fire 21', 'https://fire21pizza.com', '7 West Main St', 'Conway', 'NH', '03818', '(603) 447-2211', '+16034472211', [],
   TH(bg='#17110e', surface='#241a15', ink='#fff3e4', muted='#c9b3a0', accent='#ff5a1f', accent2='#ffb21e', on_accent='#17110e'),
   'Subs, pizza, pasta and salads in Conway Village, NH. A local favorite since 1979.',
   'Fire 21 Pizza | Subs, Pizza, Pasta & Salads in Conway Village, NH Since 1979',
   'Fire 21 Pizza, 7 West Main St, Conway Village NH. Subs, pizza, pasta and salads, serving Conway since 1979 and reopened in August 2018. Call (603) 447-2211.',
   ['Fire 21 was started in 1979 by Conway native Walter Henderson, who ran it for 25 years. A protégé then ran it for 13 years.', 'After retiring from Kennett High School in June 2018, Walter took the restaurant back with his wife Jocelyn and son Nico. After a renovation, Fire 21 reopened on August 28, 2018.', 'Come in for the subs, pizza, pasta and salads that put Fire 21 on the map.'],
   ('Since', '1979', 'Conway Village'), 'Fire+21+Pizza+7+West+Main+St+Conway+NH+03818', facebook='https://www.facebook.com/pages/category/Sandwich-Shop/FIRE-21-412956765907178/',
   menu_note='Fire 21 serves subs, pizza, pasta and salads. The shop has not published a menu online, so call for items and prices.',
   findings=['Old Yahoo/Turbify builder page: name, phone, address and a map on the homepage, plus an About page.', 'No menu, no hours and no online ordering are published anywhere on the current site.', 'The Facebook link on the site is an old "Sandwich-Shop" category URL; it is kept as published but should be replaced with the shop\'s real page.', 'Pinch-zoom is blocked on the old site; the new site allows zoom.', 'Photos on the old site are Google-hosted images we could not view or confirm as the shop\'s own, so none were published.'],
   questions=['What are your hours?', 'Can you send your menu with prices? None is published online, so the site shows no menu.', 'Which Facebook page is yours? The link on the old site is an outdated category URL.', 'Do you have photos we may use (food, shop, the Henderson family)?', 'Do you offer delivery or online ordering?', 'Is the address 7 West Main St, Conway Village?'])

# ---------------- Lancaster House of Pizza
mk('lancaster-house-of-pizza-lancaster', 'Lancaster House of Pizza', 'Lancaster House of Pizza', 'https://www.lancasterhouseofpizza.com', '281 Summer St', 'Lancaster', 'NH', '03584', '(603) 788-0964', '+16037880964',
   [dict(dow=[1, 2, 3, 4], open='11:00', close='20:00'), dict(dow=[5, 6], open='11:00', close='21:00')], TH(bg='#f6f3e8', ink='#1b2a22', muted='#55645b', accent='#1f6045', accent2='#8a5a00'),
   'Classic and specialty pizzas, calzones, grinders, wraps and more on Summer Street in Lancaster, NH. Pickup or delivery.',
   'Lancaster House of Pizza | Pizza, Grinders & Wraps in Lancaster, NH',
   'Lancaster House of Pizza, 281 Summer St, Lancaster NH. Specialty pizzas, calzones, grinders, wraps, pasta and more. Pickup or delivery. Call (603) 788-0964.',
   ['The menu at Lancaster House of Pizza is full of flavorful pizza dishes, from classic favorites to more adventurous options like Mediterranean, Greek, Seafood Lovers and Chicken Fiesta.', 'Stop by in the Lancaster area, or order online for pickup or delivery.'],
   ('Pickup &', 'Delivery', 'Lancaster, NH'), 'Lancaster+House+of+Pizza+281+Summer+St+Lancaster+NH+03584',
   menu=[cat('Pizza', [it('Plain Cheese Pizza', '$8.99', 'Classic cheese or create your own pizza.')]),
    cat('Specialty Pizza', [it('White Pizza', '$10.99', 'Feta, garlic, virgin olive oil, cheddar, mozzarella & oregano.'), it('Grilled Chicken Pizza', '$12.99', 'Grilled chicken, tomato sauce, cheddar & mozzarella.'), it('BBQ Chicken Pizza', '$11.99', 'BBQ sauce & chicken, served with blue cheese.'), it('Buffalo Pizza', '$11.99', 'Buffalo sauce & chicken, served with blue cheese.'),
      it('Mediterranean Pizza', '$12.99', 'Ricotta, feta, mozzarella, cheddar, garlic, spinach & olives with virgin olive oil.'), it('Greek Pizza', '$12.99', 'Tomato sauce, spinach, feta, olives, tomatoes, garlic & oregano.'), it('Italian Pizza', '$12.99', 'Pepperoni, salami, black olives, onions, tomatoes, garlic.'), it('Meat Lovers Pizza', '$13.99', 'Hamburger, sausage, pepperoni, ham, meatball & bacon.'),
      it('House Pizza', '$14.50', 'Pepperoni, hamburg, sausage, mushrooms, onions, peppers, bacon.'), it('Hawaiian Pizza', '$10.99'), it('Veggie Pizza', '$12.99', 'Mushrooms, onions, peppers, broccoli, black olives, tomatoes.'), it('Chicken Bacon Ranch Pizza', '$12.99', 'Chicken, bacon, ranch dressing.'),
      it('Mexican Pizza', '$13.99', 'Peppers, jalapeños, black olives, tomatoes, tortilla chips, salsa.'), it('Chicken Fiesta Pizza', '$13.99', 'Grilled chicken, onions, peppers, tomatoes, banana peppers, black olives, tortilla chips, salsa.'), it('Seafood Lovers Pizza', '$14.50', 'Shrimp, scallops, mussels.')])],
   menu_note='', order_url='https://www.lancasterhouseofpizza.com/2wctw8mc/lancaster-house-of-pizza-lancaster-03584/order-online', order_label='Order online',
   delivery='Pickup and delivery are both available. Order online or call.',
   findings=['Auto-generated Beyond Menu site; About text is generic and there are no photos of the shop.', 'Only pizza and specialty pizza items were readable on the menu page we could fetch; appetizers, salads, calzones, subs, grinders, wraps, burgers, pasta, kids and desserts appear as headings only.', 'A separate, unofficial site (orderlancasterhouseofpizza.com) lists a Vermont phone number; the new site links only to the shop\'s own order page and (603) 788-0964.', 'No photos were published: the only images on the site are vendor stock paths.'],
   questions=['Please send the full menu: only pizza was readable online, so other sections are not shown.', 'Hours: the order page showed Mon-Thu 11-8, Fri-Sat 11-9, Sun closed. Are those current?', 'Is the online-order link above the one you want customers to use?', 'Do you have photos of your food and shop we may use?', 'Do you have a Facebook page we should link?', 'Can the unofficial order site with the Vermont phone number be taken down?'])

# ---------------- Pizzeria Roma
S3 = ['12"', '16"', '18"']
roma_sp = [('BBQ Chicken', 13.99, 19.99, 24.99), ('Chicken Bacon Ranch', 13.99, 19.99, 24.99), ('Meat Lovers', 14.99, 20.99, 25.99), ('Italian Combo', 14.99, 20.99, 25.99), ('Vegetarian', 13.99, 19.99, 24.99), ('White Pizza Spinach & Feta', 12.99, 18.99, 23.99), ('Buffalo Chicken', 13.99, 19.99, 24.99), ('Grecian Delight', 13.99, 19.99, 24.99),
 ('Philly Steak & Cheese', 14.99, 20.99, 25.99), ('The Roma Special', 14.99, 20.99, 25.99), ('Margherita', 12.99, 18.99, 23.99), ('Hawaiian', 12.99, 18.99, 23.99), ('Big Mac Pizza', 14.99, 19.99, 24.99), ('Melzane', 13.99, 19.99, 24.99), ('Hawaiian BBQ', 14.99, 20.99, 25.99)]
hot = [('Steak and Cheese', 9.25, 11.25), ('Roma Steak Bomb', 9.99, 11.99), ('Chicken Cordon Bleu', 9.99, 11.99), ('Chicken Tender', 9.25, 11.25), ('Sausage, Pepper & Onions', 9.25, 11.25), ('Pastrami', 9.25, 11.25), ('B.L.T.', 9.25, 11.25), ('Cheeseburger (Homemade)', 9.25, 11.25), ('Grilled Chicken', 9.25, 11.25), ('Grilled Chicken Teriyaki', 9.99, 11.99), ('Buffalo Chicken Tender', 9.25, 11.25), ('Grilled Chicken Bomb', 9.99, 11.99)]
roma = [
 cat('Pizza', [it('Cheese', money(9.99, 12.99, 18.99)), it('Each additional topping', money(1.50, 2.00, 2.50)), it('Extra cheese', money(2.25, 3.25, 3.99)), it('Sicilian Pizza', '$17.99', '16"'), it('Gluten Free Pizza', '$14.99', '12"'),
   it('Meat toppings', '', 'Pepperoni, sausage, hamburger, bacon, meatballs, grilled chicken, anchovies, ham, salami'), it('Veggie toppings', '', 'Black olives, onions, mushrooms, tomatoes, eggplant, broccoli, spinach, pineapple, baby spinach, garlic, banana peppers, jalapeños, kalamata olives, fresh basil, fresh mozzarella')],
   'Sizes as printed on the shop menu: 12" Small, 16" Large, 18" X-Large.', S3),
 cat('Specialty Pizza', [it(n, money(a, b, c)) for n, a, b, c in roma_sp], '', S3),
 cat('Subs', [it('Steak Tip', '$13.99', 'Hot sub')] + [it(n, money(a, b)) for n, a, b in hot] +
   [it(n, money(9.25, 11.25), 'Cold sub, also on a wrap') for n in ['Italian', 'Roast Beef', 'Turkey', 'Tuna Fish', 'Chicken Salad', 'Ham & Cheese', 'Salami', 'Vegetarian']] +
   [it(n, money(9.25, 11.25), 'Parmigiana sub') for n in ['Chicken Cutlet (Homemade)', 'Veal Cutlet', 'Meatball (Homemade)', 'Eggplant Parmigiana (Homemade)', 'Chicken Tender (Homemade)']],
   'Two prices are listed for most subs, as on the shop menu (small and large). Extra cheese: add $0.75 small or $1.00 large.'),
 cat('Calzones & Wraps', [it('Cheese Calzone', '$10.99'), it('Buffalo Chicken Calzone', '$13.99'), it('Meatball Parmigiana Calzone', '$13.99'), it('Sausage, Peppers & Onions Calzone', '$13.99'), it('Eggplant Parmigiana Calzone', '$13.99'), it('Spinach Ricotta Calzone', '$13.99'), it('Steak & Cheese Calzone', '$14.99'), it('Chicken Cutlet Parmigiana Calzone', '$13.99'), it('Veggie Calzone', '$13.99'), it('Pepperoni Calzone', '$13.99'), it('Chicken Teriyaki with Onions & Peppers Calzone', '$13.99'), it('Steak Bomb Calzone', '$15.99')] +
   [it(n, '$9.99') for n in ['Chicken Mania Wrap', 'Mediterranean Chicken Wrap', 'Chicken Caesar Wrap', 'Chicken Cordon Bleu Wrap', 'Buffalo Sizzler Wrap', 'Grilled Veggie Wrap', 'Grilled Chicken Teriyaki Wrap', 'Hawaiian BBQ Chicken Wrap', 'Spicy Tropical Wrap']] + [it('Steak Tip Caesar Wrap', '$12.99')],
   'Calzone toppings or ricotta: +$1.50 each. Wraps come on white, wheat, spinach or tomato.'),
 cat('Dinners', [it('Veal Parmigiana', '$14.99'), it('Eggplant Parmigiana', '$14.99'), it('Chicken Parmigiana', '$14.99'), it('Lasagna (meatless)', '$13.99'), it('Ravioli with meatballs or sausage', '$12.99'), it('Spaghetti with marinara', '$12.99'), it('Spaghetti with meatballs or sausage', '$13.99'), it('Spaghetti Combo', '$14.49', 'Meatballs and sausage'),
   it('Chicken Tenders Plate', '$14.99'), it('Buffalo Chicken Tenders Plate', '$14.99'), it('Chicken Wings Plate', '$14.99'), it('Buffalo Chicken Wings Plate', '$14.99'), it('Grilled Chicken Plate', '$14.99'), it('Steak Tips Plate', '$16.99'), it('Grilled Chicken Teriyaki Plate', '$15.49'), it('Cheeseburger Plate', '$11.99', '6 oz patty')],
   'Pasta dinners come with garlic bread and salad. Dinner plates come with french fries, onion rings or rice pilaf, and salad. Make it a double: +$2.00.'),
 cat('Salads', [it('Tossed Salad', '$8.99'), it('Caesar Salad', '$8.99'), it('Antipasto Salad', '$10.99'), it('Chicken Caesar Salad', '$11.99'), it('Greek Salad', '$9.99'), it('Chef Salad', '$10.99'), it('Chicken Salad', '$10.99'), it('Tuna Salad', '$9.99'), it('Grilled Chicken Salad', '$11.99'), it('Steak Tip Salad', '$14.99'), it('Steak Tip Caesar Salad', '$14.99'), it('Buffalo Chicken Tender Salad', '$11.99')],
   'Greek salad: add chicken $3.99 or steak tips $6.99. Extra dressing $0.75, feta $1.75.'),
 cat('Sides & Kids', [it('Onion Rings', ['Sm $4.99', 'Lg $6.99']), it('French Fries', ['Sm $4.99', 'Lg $6.99']), it('Spicy Fries', ['Sm $5.25', 'Lg $7.25']), it('Sweet Potato Fries', ['Sm $5.25', 'Lg $7.25']), it('Cheesy Fries', '$7.99', 'Add bacon +$1.25'), it('Chicken Tenders', '$9.99'), it('Buffalo Chicken Tenders', '$10.49'), it('Mozzarella Sticks', '$8.99'), it('Soup of the Day', '$6.99'), it('Fried Ravioli', '$8.99'), it('Jalapeño Poppers', '$8.99'), it('Chicken Wings', '$9.99'), it('Buffalo Chicken Wings', '$10.49'), it('Cheesy Garlic Bread', '$4.99', 'Add pepperoni or bacon +$1.50'),
   it('Kids: Chicken Tenders & Fries', '$6.99'), it('Kids: Hot Dogs & Fries', '$5.99'), it('Kids: Spaghetti & Meatballs', '$5.99'), it('Kids: Slice of Pizza & Fries', '$5.99')]),
]
mk('pizzeria-roma-milford', 'Pizzeria Roma', 'Pizzeria Roma', 'https://www.pizzeriaromanh.com', '586 Nashua Street, Lordens Plaza', 'Milford', 'NH', '03055', '603-672-2333', '+16036722333',
   [dict(dow=[1, 2, 3, 4, 5, 6], open='11:00', close='21:00')], TH(bg='#fbf6ec', ink='#241812', muted='#66564a', accent='#a3151b', accent2='#2f6e3f'),
   'Italian hand-tossed pizza, subs, wraps, salads and homemade dinners in Lordens Plaza, Milford, NH.',
   'Pizzeria Roma | Italian Hand-Tossed Pizza, Subs & Dinners in Milford, NH',
   'Pizzeria Roma, 586 Nashua Street, Lordens Plaza, Milford NH. Italian hand-tossed pizza, subs, wraps, salads and homemade dinners. Open Monday to Saturday 11am to 9pm. Call 603-672-2333.',
   ['Pizzeria Roma makes Italian hand-tossed pizza with fresh dough and high-quality ingredients. The menu also has subs, wraps, salads and homemade dinners.', 'Ask about the daily specials.'],
   ('Hand-tossed', 'Pizza', 'Milford, NH'), 'Pizzeria+Roma+586+Nashua+Street+Milford+NH+03055', menu=roma,
   delivery='The shop lists takeout and delivery. Call to ask about delivery to your address.',
   findings=['Old Community Communications vendor template; homepage is a single paragraph and the menu is a plain text price table.', 'No online ordering and no social links on the site.', 'Pinch-zoom is blocked on the old site; the new site allows zoom.', 'Only a logo and one homepage image were on the site and neither could be confirmed as the shop\'s own cleared photography, so none were published.', 'Source typos ("Terriyaki", "Jalepeno") were corrected.', 'Gallery, Hours and Contact pages were not read: hours come from the homepage text.'],
   questions=['Do you have photos of your food and shop we may use? None are published in this concept.', 'Pizza sizes were read as 12", 16" and 18" (Small / Large / X-Large). Please confirm.', 'Subs list two prices with no size labels; we show them as listed. Are they small and large?', 'Is the menu current? Prices were copied from the live site.', 'Do you want online ordering? None exists, so the site is phone-order only.', 'Confirm hours: Monday to Saturday 11am to 9pm, closed Sunday.', 'Do you have a Facebook or Instagram page to link?', 'Which delivery area do you cover?'])

# ---------------- Family Pizza Pittsfield
mk('family-pizza-pittsfield', 'Family Pizza Pittsfield', 'Family Pizza', 'https://familypizzapittsfield.com', '16 Elm St', 'Pittsfield', 'NH', '03263', '(603) 435-0009', '+16034350009',
   [dict(dow=ALL, open='10:30', close='22:00')], TH(bg='#fff9ec', ink='#1d2433', muted='#5a6272', accent='#1f56a5', accent2='#7d5a00'),
   'Oven-hot pizza, great subs, fresh salads and dinners on Elm Street in Pittsfield, NH. Family owned and operated.',
   'Family Pizza Pittsfield | Pizza, Subs, Salads & Dinners in Pittsfield, NH',
   'Family Pizza Pittsfield, 16 Elm St, Pittsfield NH. Family owned and operated: oven-hot pizza, subs, calzones, salads and dinners. Open daily 10:30am to 10pm. Call (603) 435-0009.',
   ['Family Pizza Pittsfield is a family owned and operated pizzeria with the goal of providing customers with excellent service and superior quality.', 'The shop serves oven-hot pizza, subs, wings, huge calzones, fresh salads and dinners, including pasta dishes like Alfredo with chicken, spaghetti with meat sauce and meatball, penne marinara and ravioli marinara, served with salad and garlic bread.'],
   ('Family owned', '& operated', 'Pittsfield, NH'), 'Family+Pizza+16+Elm+St+Pittsfield+NH+03263', facebook='https://www.facebook.com/FamilyPizzaPittsfield',
   order_url='https://www.24seveneatsonline.com/api/fb/_m_o7_vp', order_label='Order online',
   menu_note="The shop's menu with prices lives on its online ordering page. Open it there, or call to ask about today's items.",
   findings=['Stock "demo-restaurant" theme: the hero slides, section images and gallery are the theme\'s demo files, not the shop\'s food, so none were used.', 'Listed email info@melodypicture.com belongs to the theme vendor, not the shop; it is not published on the new site.', 'Instagram and Twitter icons point at the bare instagram.com / twitter.com homepages; only the shop\'s Facebook page is linked.', 'Menu sections ("View More") are dead links; no menu prices are published on the site itself, so none are shown.', '"Latest Tweets" widget never loads.', 'Ordering link comes from the Order online button on the contact page (24seveneatsonline); it was not tested by placing an order.'],
   questions=['Do you have photos of your food and shop we may use? The old site shows only theme demo images.', 'Can you send your menu with prices? None is published on the site, so the new site links to your ordering page.', 'Is the 24seveneatsonline link the right ordering page?', 'What email address should customers use?', 'Do you have Instagram or other social pages to link?', 'Hours show 10:30am to 10pm every day: are those current?', 'Do you offer delivery?'])
