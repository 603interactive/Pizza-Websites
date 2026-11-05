"""Mary's Pizza (Gorham): gingham/family-recipe-card site with a live 'today's deal' card, split-shift hours and a pizza price builder. usage: build_marys.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import *
FONTS = [('Gloock', 'Gloock-Regular', 400, 'normal'), ('Crimson Pro', 'CrimsonPro-Regular', 400, 'normal'), ('Crimson Pro', 'CrimsonPro-Bold', 700, 'normal'), ('Crimson Pro', 'CrimsonPro-Italic', 400, 'italic'),
         ('Instrument Sans', 'InstrumentSans-Regular', 400, 'normal'), ('Instrument Sans', 'InstrumentSans-Bold', 700, 'normal')]
def money(p): return f'${p:.2f}'
def extra(d, img):
    loc = d['locations'][0]
    # split shifts: lib.week() keeps only the first window per day, so build the text ourselves
    rows = []
    for dow, day in DAYS:
        ws = [h for h in loc['hours'] if dow in h['dow']]
        rows.append(dict(dow=dow, day=day, short=day[:3], text=' and '.join(f"{fmt12(h['open'])} – {fmt12(h['close'])}" for h in ws) or 'Closed'))
    toppings = [t.strip() for t in next(i for c in d['menu'] if c['cat'] == 'Build Your Pizza' for i in c['items'] if i['name'] == 'Toppings')['desc'].split(',')]
    toppings = [t.replace(' (fresh or canned)', '') for t in toppings]
    byo = next(c for c in d['menu'] if c['cat'] == 'Build Your Pizza')['items']
    g = lambda n: {p['l']: p['v'] for p in next(i for i in byo if i['name'] == n)['prices']}
    rows5 = [g(n) for n in ('Cheese', '1 Topping', '2 Toppings', '3 Toppings', '4 Toppings')]
    calc = dict(S=[r['S'] for r in rows5], L=[r['L'] for r in rows5], PS=[r['Pan/GF S'] for r in rows5], PL=[r['Pan/GF L'] for r in rows5],
                add=g('Additional Topping'), cheese=g('Extra Cheese'), sauce=g('Extra Sauce'))
    return dict(calc_json=json.dumps(calc), money=money, week=rows, toppings=[t[0].upper() + t[1:] for t in toppings])
build('marys-pizza-gorham', 'marys.html.j2', 'marys.css.j2', ['marys.js'], FONTS, ['Pizza', 'Italian', 'Pasta'],
      "Concept for Mary's Pizza, built only from your own menu, copy and photos. Not your live site.", extra)
