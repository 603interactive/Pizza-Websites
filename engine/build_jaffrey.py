"""Jaffrey Pizza Barn: barn-door red/white-trim site with Same Flavor, Every Way (each specialty as pizza / calzone / grinder / salad / dinner, real prices). usage: build_jaffrey.py"""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import *
FONTS = [('Big Shoulders', 'BigShoulders-Regular', 400, 'normal'), ('Big Shoulders', 'BigShoulders-Bold', 700, 'normal'),
         ('Work Sans', 'WorkSans-Regular', 400, 'normal'), ('Work Sans', 'WorkSans-Bold', 700, 'normal')]
def money(p): return p if isinstance(p, str) else f'${p:.2f}'
# flavor -> {format: (menu category, item name, size labels, photo)}; every price comes from data.json
FLAVORS = [
 ('Buffalo Chicken', {'Pizza': ('Pizza', 'Buffalo Chicken', None), 'Calzone': ('Calzones', 'Buffalo Chicken', None), 'Grinder': ('Grinders & Wraps', 'Buffalo Chicken', None), 'Salad': ('Salads', 'Buffalo Chicken Salad', None), 'Burger plate': ('Burger Plates', 'Buffalo Chicken Burger', None)}),
 ('Barbecue Chicken', {'Pizza': ('Pizza', 'Barbecue Chicken', 'pizza-bbq.webp'), 'Calzone': ('Calzones', 'Barbecue Chicken', None), 'Grinder': ('Grinders & Wraps', 'Barbecue Chicken', None)}),
 ('Barbecue Rib', {'Pizza': ('Pizza', 'Barbecue Rib', None), 'Calzone': ('Calzones', 'Barbecue Rib', None), 'Grinder': ('Grinders & Wraps', 'Barbecue Rib', None)}),
 ('B.L.T.', {'Pizza': ('Pizza', 'B.L.T.', 'pizza-blt.webp'), 'Calzone': ('Calzones', 'B.L.T.', None), 'Grinder': ('Grinders & Wraps', 'B.L.T.', None)}),
 ('Steak Bomb', {'Pizza': ('Pizza', 'Steak Bomb Special', None), 'Calzone': ('Calzones', 'Steak Bomb Special', None), 'Grinder': ('Grinders & Wraps', 'Steak Bomb', 'steakbomb.webp')}),
 ('Grecian', {'Pizza': ('Pizza', 'Grecian', 'pizza-grecian.webp'), 'Calzone': ('Calzones', 'Grecian', None), 'Salad': ('Salads', 'Greek Salad', 'greek-salad.webp')}),
 ('Vegetable', {'Pizza': ('Pizza', 'Vegetable Special', None), 'Calzone': ('Calzones', 'Vegetable Special', None), 'Grinder': ('Grinders & Wraps', 'Vegetarian', None)}),
 ('Barn Burner', {'Pizza': ('Pizza', 'Barn Burner Pizza', 'pizza-barnburner.webp'), 'Grinder': ('Grinders & Wraps', 'Barn Burn Grinder', 'barnburn-grinder.webp'), 'Dinner': ('Dinners', 'Barn Burners', None)}),
 ('Big Mac', {'Pizza': ('Pizza', 'Big Mac Special', 'pizza-bigmac.webp'), 'Calzone': ('Calzones', 'Big Mac Special', None)}),
 ('Chicken Club', {'Pizza': ('Pizza', 'Chicken Club', 'pizza-chickenclub.webp'), 'Calzone': ('Calzones', 'Chicken Club', None)}),
 ('Chicken Bacon Ranch', {'Pizza': ('Pizza', 'Chicken Bacon Ranch', None), 'Calzone': ('Calzones', 'Chicken Bacon Ranch', None)}),
 ('Meatlovers', {'Pizza': ('Pizza', 'Meatlovers Special', None), 'Calzone': ('Calzones', 'Meatlovers Special', None)}),
]
def flip(d):
    cats = {c['cat']: c for c in d['menu']}; out = []
    for fl, forms in FLAVORS:
        fs = []; desc = ''
        for fmt, (cat, name, ph) in forms.items():
            c = cats[cat]; it = next(i for i in c['items'] if i['name'] == name)
            labels = c['head'] if len(c['head']) > 1 else ['']
            if fmt == 'Pizza': labels = ['7"', '10"', '15"', '18"']
            pr = [dict(l=labels[k] if k < len(labels) else '', p=money(p)) for k, p in enumerate(it['prices']) if p is not None]
            if fmt == 'Dinner' or fmt == 'Burger plate' or fmt == 'Salad' and len(pr) == 1: pr = [dict(l='', p=pr[0]['p'])] if len(pr) == 1 else pr
            if fmt == 'Pizza': desc = it['desc']
            low = min(p for p in it['prices'] if p is not None)
            fs.append(dict(fmt=fmt, name=name, desc=it['desc'], prices=pr, low=low, img=ph))
        mn = min(f['low'] for f in fs)
        for f in fs: f['cheapest'] = f['low'] == mn
        out.append(dict(name=fl, desc=desc, forms=fs, id=slugify(fl)))
    return out
def extra(d, img): return dict(money=money, flips=flip(d), flips_n=sum(len(f['forms']) for f in flip(d)))
build('jaffrey-pizza-barn', 'jaffrey.html.j2', 'jaffrey.css.j2', ['common.js', 'jaffrey.js'], FONTS, ['Pizza', 'Grinders', 'Calzones', 'Seafood', 'American'],
      "Concept for Jaffrey Pizza Barn, built only from your own menu, copy and photos. Not your live site.", extra)
