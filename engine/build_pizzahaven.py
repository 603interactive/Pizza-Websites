"""Pizza Haven Rindge: orange/ink 'Pizza With Attitude' site. Big idea: Pick a Pizza With Attitude (filter + surprise-me over all 34 listed pizzas, with the calzone twin price) + the real coupons. usage: build_pizzahaven.py"""
import json, sys, re
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import *
FONTS = [('Bricolage Grotesque', 'BricolageGrotesque-Regular', 400, 'normal'), ('Bricolage Grotesque', 'BricolageGrotesque-Bold', 700, 'normal'),
         ('Instrument Sans', 'InstrumentSans-Regular', 400, 'normal'), ('Instrument Sans', 'InstrumentSans-Bold', 700, 'normal'),
         ('Nothing You Could Do', 'NothingYouCouldDo-Regular', 400, 'normal')]
def money(p): return p if isinstance(p, str) else f'${p:.2f}'
WILD = {'Cheeseburger Pizza', 'Mac & Cheese Pizza', 'Macaroni & Cheese Pizza', 'B.L.T. Pizza', 'Taco Pizza', 'Mexican Pizza', 'Shrimp Pizza', 'Pastrami Pizza', 'BBQ Rib Pizza', 'Bruschetta Pizza', 'Chicken Broccoli Alfredo Pizza'}
def tags(it):
    n = (it['name'] + ' ' + it['desc']).lower(); t = []
    meat = re.search(r'pepperoni|sausage|bacon|ham\b|salami|b\.l\.t|rib|pastrami|steak|beef|hamburger|burger|meatball|shrimp|chicken', n)
    if re.search(r'chicken', n): t.append('chicken')
    if re.search(r'steak|beef|pastrami|hamburger|burger|meatball|rib', n): t.append('beef')
    if re.search(r'pepperoni|sausage|bacon|\bham\b|salami|b\.l\.t', n): t.append('pork')
    if not meat: t.append('veggie')
    if it['name'] == 'Vegetarian Pizza': t.append('veggie')
    if it['name'] in WILD: t.append('wild')
    if re.search(r'^(cheese|white|pesto cheese|five cheese)', it['name'].lower()): t.append('classic')
    return sorted(set(t))
def extra(d, img):
    cats = {c['cat']: c for c in d['menu']}
    cz = {i['name'].replace(' Calzone', ''): i['prices'][0] for i in cats['Calzones']['items']}
    pz = []
    for i in cats['Pizzas']['items']:
        base = i['name'].replace(' Pizza', '')
        pz.append(dict(name=i['name'], desc=i['desc'], price=i['prices'][0], tags=tags(i), calz=cz.get(base)))
    groups = []
    for c in d['menu']:
        g = next((x for x in groups if x['name'] == c['group']), None)
        if not g: g = dict(name=c['group'], id=slugify(c['group']), cats=[]); groups.append(g)
        g['cats'].append(c)
    wk = [dict(dow=dow, day=day, text=(f"{fmt12('11:00')} – {fmt12('21:00')}" if dow in (1, 2, 3, 4, 5) else 'Not confirmed · call'), unk=dow in (0, 6)) for dow, day in DAYS]
    cp = d['coupons']; each = cp[0]['price'] / 2
    return dict(money=money, pizzas=pz, groups=groups, week=wk, coupons=cp, each=f'{each+0.0001:.2f}', soda=f"{cp[1]['price'] - cp[0]['price']:.2f}", npz=len(pz))
build('pizza-haven-rindge', 'pizzahaven.html.j2', 'pizzahaven.css.j2', ['common.js', 'pizzahaven.js'], FONTS, ['Pizza', 'Subs', 'Calzones', 'Seafood', 'American'],
      "Concept for Pizza Haven, built only from your own menu and photos. Not your live site.", extra)
