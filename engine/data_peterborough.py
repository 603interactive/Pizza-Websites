"""Writes clients/peterborough-pizza-barn/data.json from the text menu on peterboroughpizzabarn.com. usage: data_peterborough.py"""
import json
from pathlib import Path
R = Path(__file__).resolve().parent.parent / 'clients' / 'peterborough-pizza-barn'
def it(n, p, d=''): return dict(name=n, prices=p if isinstance(p, list) else [p], desc=d)
S3 = ['Personal 7"', 'Small 10"', 'Large 15"']
tops = [('Tomato & Cheese', 5, 10, 15), ('Extra Cheese', 5.75, 11.25, 17.5), ('Feta Cheese', 5.75, 11.25, 17.5), ('Pineapple', 5.75, 11, 17), ('Fresh Garlic', 5.75, 10.75, 16.5), ('Tomatoes', 5.75, 10.75, 16.5),
 ('Onion', 5.75, 11, 17.25), ('Pepper', 5.75, 11, 17.25), ('Pepper & Onion', 5.75, 11.75, 18.75), ('Mushroom', 5.75, 11.75, 18.75), ('Black Olive', 5.75, 11.75, 18.75), ('Broccoli', 5.75, 11.75, 18.75),
 ('Spinach', 5.75, 11.75, 18.75), ('Eggplant', 5.75, 11.75, 18.75), ('Any Chicken, Any Sauce!', 7, 14, 22), ('Sausage', 5.75, 11.75, 18.75), ('Pepperoni', 5.75, 11.75, 18.75), ('Hamburg', 5.75, 11.75, 18.75),
 ('Salami', 5.75, 11.75, 18.75), ('Pastrami', 5.75, 11.75, 18.75), ('Anchovy', 5.75, 11.75, 18.75), ('Imported Ham', 5.75, 12, 19.25), ('Canadian Bacon', 5.75, 12, 19.25), ('Steak', 5.75, 12.5, 19.75),
 ('Bacon', 5.75, 12.5, 19.75), ('Mexican', 7, 14.75, 22.75), ('Special', 6.75, 14.5, 22)]
m = lambda x: f'${x:.2f}'
subs = [('Cheese', 9, 11.95), ('American', 9, 11.95), ('Genoa Salami', 9, 11.95), ('Cooked Salami', 9, 11.95), ('Italian', 9, 11.95), ('Ham & Cheese', 9, 11.95), ('Turkey Breast', 9, 11.95), ('Chicken Salad', 9, 11.95),
 ('Tuna', 9, 11.95), ('Roast Beef', 9.5, 12.75), ('Canadian Bacon', 9, 11.95), ('CrabMeat', 9, 11.95), ('Vegetarian', 9, 11.95), ('BLT & Cheese', 9, 11.95), ('Pepperoni', 9, 11.95), ('Meatball', 9, 11.95),
 ('Sausage', 9, 11.95), ('Pastrami & Cheese', 9.5, 12.75), ('Barbecue Rib', 9, 11.95), ('Haddock', 9, 11.95), ('Chicken Parmesan', 9, 11.95), ('Chicken & Veggie', 9, 11.95), ('Eggplant Parmesan', 9, 11.95),
 ('Grilled Chicken', 9.25, 12.25), ('Chicken Tender', 9.25, 12.25), ('Buffalo Tender', 9.25, 12.25), ('Barn Burner', 9.25, 12.25), ('Steak & Cheese', 9.75, 12.95)]
menu = [
 dict(cat='Pizza', img='', note='Hand-picked toppings priced by size. Alfredo sauce available! NEW: gluten-free pizza (ask for details). *Special: 3 large cheese pizzas, $39.00.', head=S3, items=[it(n, [m(a), m(b), m(c)]) for n, a, b, c in tops] + [it('3 Large Cheese Pizza Special', '$39.00')]),
 dict(cat='Combinations', img='', note='Alfredo sauce available!', head=S3, items=[it('2 Way', ['$6.00', '$12.25', '$19.75']), it('3 Way', ['$6.25', '$12.75', '$20.50']), it('4 Way', ['$6.25', '$13.25', '$21.25']), it('5 Way', ['$6.50', '$13.75', '$21.75'])]),
 dict(cat='Sandwiches', img='', note='Wraps & pockets and small subs are the same price.', head=['Wrap / Pocket', 'Small Sub', 'Large Sub'], items=[it(n, [m(a), m(a), m(b)]) for n, a, b in subs]),
 dict(cat='Pasta & Salads', img='', note='', head=[], items=[it('Lasagna', '$8.95'), it('Spaghetti with sauce', '$8.95'), it('Spaghetti with Meatballs', '$10.95'), it('Spaghetti with Sausage', '$10.95'), it('Spaghetti with Eggplant', '$10.95'), it('Spaghetti with Chicken', '$10.95'),
   it('Tossed Salad', '$5.95'), it('Greek Salad', '$8.95'), it('Grilled Chicken Salad', '$8.95'), it('Chef Salad', '$8.95'), it('Antipasto', '$9.95')]),
 dict(cat='Fried Dinners', img='', note='All dinners are served with fries. 50¢ to add spicy fries. No fries, deduct 75¢.', head=[], items=[it(n, p) for n, p in [('Chicken Nuggets 8 pc', '$7.50'), ('Chicken Nuggets 12 pc', '$9.00'), ('Clam Strips', '$11.50'), ('Fried Shrimp', '$11.50'), ('Chicken Tenders', '$11.50'), ('Barn Burners', '$11.50'), ('Buffalo Tenders', '$11.50'), ('Hot Wings', '$11.95'), ('Chicken Wings', '$11.95'), ('Cod 4 pc', '$11.95'), ('Haddock', '$11.95'), ('Scallops', '$13.95'), ('Seafood Plate', '$14.95')]]),
 dict(cat='Fried Sides & Sides', img='', note='', head=[], items=[it('French Fries', ['Small $3.75', 'Large $6.50']), it('Spicy Fries', ['Small $4.75', 'Large $7.75']), it('Onion Rings', ['Small $5.00', 'Large $8.75']), it('Fried Mushrooms', ['Small $5.00', 'Large $8.75']), it('Fried Cauliflower', ['Small $5.00', 'Large $8.75']),
   it('Broccoli Poppers', '$8.75'), it('Jalapeno Poppers', '$8.75', 'Cheddar or cream cheese'), it('Cheese Sticks', '$8.75'), it('Fried Pickles', '$8.75', 'Chips or spears'), it('Fried Mac & Cheese Bites', '$8.75'), it('Fried Ravioli', '$8.75'), it('Fried Dough', '$4.75'),
   it('Bread Sticks', ['$3.75', 'w/ cheese $4.75']), it('Garlic Bread, Small', ['$1.00', 'w/ cheese $1.70']), it('Garlic Bread, Large', ['$1.95', 'w/ cheese $2.95']), it('Cole Slaw', '$1.25')]),
 dict(cat='Drinks, Chips & Dessert', img='', note="Drink and chip price lists are shown as published on the shop's site.", head=[], items=[it('Canned Soda', '$1.25'), it('Bottled Water', '$1.00'), it('AJ, Sunny D', '$1.50'), it('Gatorade', '$2.00'), it('Pure Leaf Unsweetened', '$2.00'),
   it('Lemonade, Fruit Punch, Ice Tea', ['75¢', '95¢', '$1.25']), it('Milk', ['$1.00', '$1.50']), it('Chocolate Milk', '$1.50'), it('Chips', ['75¢', '$3.50']), it('Ice Cream', '', 'Ask for flavors'), it('Fried Dough', '$4.75'), it("Yaya's Famous Baklava", '$2.50')]),
]
d = dict(slug='peterborough-pizza-barn', name='Peterborough Pizza Barn', short='Peterborough Pizza Barn', domain='https://peterboroughpizzabarn.com',
 tagline='Serving the Monadnock Region since 1974. Pizza, subs, fried dinners and more on Route 202 in Peterborough, NH.',
 seo_title='Peterborough Pizza Barn | Pizza, Subs & Fried Dinners in Peterborough, NH Since 1974', seo_desc='Peterborough Pizza Barn, 71 US-202, Peterborough NH. Serving the Monadnock Region since 1974: pizza, subs, pasta, fried dinners. Open Thursday to Saturday. Call (603) 924-7119.',
 theme=dict(bg='#fbf6e9', surface='#ffffff', ink='#241a17', muted='#6a5a52', accent='#c8102e', accent2='#f2c200', on_accent='#ffffff', head='Big Shoulders Display', body='Work Sans'),
 facebook='https://www.facebook.com/peterboroughpizzabarn/', instagram='', order_any='tel:+16039247119',
 about=['Peterborough Pizza Barn has been serving the Monadnock Region since 1974.', 'Not to be confused with the Jaffrey Pizza Barn: we are the Peterborough shop, at 71 US-202.'],
 extras=[], specials=['3 large cheese pizzas for $39.00', 'Gluten-free pizza now available'],
 delivery='Delivery is through SweenEats: call 603-554-0506 or email Sweeneatsfooddeliveryservices@gmail.com. Call us for more details.', delivery_link='tel:+16035540506', delivery_label='Call SweenEats 603-554-0506',
 gallery=[], hero_img='', logo='',
 locations=[dict(id='peterborough', name='Peterborough', street='71 US-202', city='Peterborough', region='NH', postal='03458', phone='(603) 924-7119', tel='+16039247119',
   hours=[dict(dow=[4, 5, 6], open='11:00', close='21:00')], order='tel:+16039247119',
   maps='https://www.google.com/maps/search/?api=1&query=Peterborough+Pizza+Barn+71+US-202+Peterborough+NH+03458')],
 menu=menu,
 findings=['One-page WordPress site with a single 2016 text banner, no food photos; menu links point to /menu/ which redirects to the homepage.', 'Delivery only by calling or emailing the separate SweenEats service; no online ordering exists, so the site is phone-order only.', 'Source menu lists "Clam Strips" twice at $11.50 (shown once) and the Eggplant price lacked a $ sign ($11.75 assumed).'],
 questions=['Is the menu current? Prices were copied from the live site.', 'Do you have food or shop photos we may use? None were on the site.', 'What does the unlabeled Milk / Chips / Lemonade multi-price list mean (sizes)?', 'Is the gluten-free pizza priced differently?', 'Which flavors of ice cream are served?'])
(R / 'data.json').write_text(json.dumps(d, indent=1, ensure_ascii=False)); print('ok', sum(len(c['items']) for c in menu))
