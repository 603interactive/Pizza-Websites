"""Supreme House of Pizza & Teddy's Lounge (Raymond): lounge-sign slate/maroon/gold site. usage: build_supreme.py"""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import *
FONTS = [('National Park', 'NationalPark-Regular', 400, 'normal'), ('National Park', 'NationalPark-Bold', 700, 'normal'),
         ('Instrument Sans', 'InstrumentSans-Regular', 400, 'normal'), ('Instrument Sans', 'InstrumentSans-Bold', 700, 'normal')]
def money(p): return p if isinstance(p, str) else f'${p:.2f}'
GROUP = {'Pizza': 'Pizza & calzones', 'Specialty Pizza': 'Pizza & calzones', 'Calzones': 'Pizza & calzones', 'Cold Subs': 'Subs & sandwiches', 'Hot Subs': 'Subs & sandwiches',
         'Steak & Chicken Subs': 'Subs & sandwiches', 'From the Grill': 'Subs & sandwiches', 'Clubs': 'Subs & sandwiches', 'Dinners': 'Dinners & pasta', 'Italian Dinners': 'Dinners & pasta',
         'Salads': 'Salads & sides', 'Sides': 'Salads & sides', 'Kids & Dessert': 'Kids & dessert'}
GROUPS = ['Pizza & calzones', 'Subs & sandwiches', 'Dinners & pasta', 'Salads & sides', 'Kids & dessert']
CATERING = [
 ('Salads', 'Tossed, Chef (ham, salami, cheese, turkey), Chicken Deluxe (marinated grilled chicken, mozzarella) and Greek. Small tray serves 6 to 10, large 12 to 15.'),
 ('Sandwich platters', 'Classic (roast beef, ham, smoked turkey, American, Swiss), Italian (ham, Genoa salami, provolone), Wrap platter (chicken salad, tuna or crabmeat) and a Sandwich Sampler. Serves 10 to 15.'),
 ('Appetizer platter', 'Wing dings, chicken fingers or buffalo wings and fingers, with mozzarella sticks and fried ravioli. Serves 10.'),
 ('Pasta lovers', 'Chicken broccoli and ziti, cheese or meat lasagna, chicken, veal or eggplant parmesan, shrimp angelina, shrimp scampi, four-cheese manicotti, stuffed shells, baked ziti, cacciatore and a spaghetti special. Serves 10 to 15.'),
]
def extra(d, img):
    items = []
    for c in d['menu']:
        g = GROUP.get(c['cat'])
        if not g: continue
        h = c['head']
        for it in c['items']:
            for k, p in enumerate(it['prices']):
                if p is None: continue
                items.append(dict(g=GROUPS.index(g), c=c['cat'], n=it['name'], s=(h[k] if len(h) > 1 else ''), p=p))
    summer = week(dict(hours=d['locations'][0]['summer'])); winter = week(d['locations'][0])
    return dict(money=money, items_json=json.dumps(items).replace('</', '<\\/'), groups=GROUPS, catering=CATERING, winter=winter, summer=summer, summer_hours=json.dumps(d['locations'][0]['summer']), n_items=len(items))
build('supreme-house-of-pizza-raymond', 'supreme.html.j2', 'supreme.css.j2', ['common.js', 'supreme.js'], FONTS, ['Pizza', 'Subs', 'Italian', 'American'],
      "Concept for Supreme House of Pizza & Teddy's Lounge, built only from your own menu, copy and photos. Not your live site.", extra)
