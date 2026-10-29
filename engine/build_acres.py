"""Golden Acres Pizza Market: bespoke Aegean-market site with the Size Lab. usage: build_acres.py"""
import json, sys, datetime
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import *
FONTS = [('Gloock', 'Gloock-Regular', 400, 'normal'), ('Instrument Sans', 'InstrumentSans-Regular', 400, 'normal'), ('Instrument Sans', 'InstrumentSans-Bold', 700, 'normal')]
IMGMAP = json.load(open(ROOT / 'clients' / 'golden-acres-pizza-market' / 'img' / '_map.json'))['map']
LAB_PHOTO = {'Meat Lovers': ('p-c12.webp', 'Real photo from the shop: half meat lovers, half chicken broccoli feta. Circles are drawn to true size.'),
             'Margherita': ('p-c17.webp', 'Real photo from the shop. Circles are drawn to true size.'),
             'Buffalo & BBQ Chicken': ('p-c16.webp', 'Real photo from the shop: buffalo and BBQ, half and half. Circles are drawn to true size.')}
GALLERY = ['p-1597948412913.webp', 'p-1597948478598.webp', 'p-1597948473615.webp', 'p-1597948482080.webp', 'p-c14.webp', 'p-c18.webp', 'p-c20.webp', 'p-c21.webp', 'p-c23.webp', 'p-c24.webp', 'p-c26.webp', 'p-c27.webp', 'p-c28.webp', 'p-c22.webp', 'p-c15.webp']
def extra(d, img):
    menu = []; thumbs = set()
    for c in d['menu']:
        items = []
        for it in c['items']:
            it = dict(it); src = it.get('img')
            if src and src in IMGMAP and not (c['cat'] == 'Pizza' and it['name'] == 'Cheese Pizza'):  # that photo is a pepperoni pie
                it['thumb'] = img(IMGMAP[src]); thumbs.add(IMGMAP[src])
            items.append(it)
        menu.append(dict(c, items=items))
    pies = []
    for it in next(c for c in d['menu'] if c['cat'] == 'Pizza')['items']:
        if not it.get('sizes'): continue
        s = dict(it['sizes']); ph = LAB_PHOTO.get(it['name'])
        pies.append(dict(name=it['name'], desc=it.get('desc', ''), p14=price_num(s['14"']), p20=price_num(s['20"']), photo=img(ph[0]) if ph else None, cap=ph[1] if ph else None))
    used = thumbs | {'p-c12.webp', 'p-c17.webp', 'p-c16.webp'}
    gallery = [img(g) for g in GALLERY if g not in used]
    return dict(menu=menu, pies_json=json.dumps(pies), years=datetime.date.today().year - 1998, pouliano=next(s for s in d['signatures'] if s['name'] == 'The Pouliano'), gallery=gallery)
build('golden-acres-pizza-market', 'acres.html.j2', 'acres.css.j2', ['common.js', 'acres.js'], FONTS, ['Pizza', 'Greek', 'Subs', 'Salads'],
      "Concept for Golden Acres Pizza Market, built only from your own menu and photos. Not your live site.", extra)
