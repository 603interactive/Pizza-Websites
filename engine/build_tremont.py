"""Tremont House of Pizza: bespoke Boat House site with the Points Ladder. usage: build_tremont.py"""
import json, sys, datetime
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import *
FONTS = [('Arsenal SC', 'ArsenalSC-Regular', 400, 'normal'), ('Crimson Pro', 'CrimsonPro-Regular', 400, 'normal'), ('Crimson Pro', 'CrimsonPro-Bold', 700, 'normal')]
ADDON = ('Additional', 'Specialty toppings', 'Traditional toppings', 'Extra', 'VegetaBall', 'Meatball or Sausage')
def extra(d, img):
    items = []
    for c in d['menu']:
        if c['cat'] in ('Calzones',) : pass
        for it in c['items']:
            if it['name'].startswith(ADDON): continue
            if it.get('sizes'): opts = [dict(l=s[0], p=price_num(s[1])) for s in it['sizes']]
            else: opts = [dict(l='', p=price_num(it['price']))]
            items.append(dict(cat=c['cat'], name=it['name'], desc=it.get('desc', ''), opts=opts))
    return dict(items_json=json.dumps(items), rewards_json=json.dumps(d['loyalty']['rewards']), years=datetime.date.today().year - d['founded'],
                lunch=d['lunch'], boathouse=d['boathouse'], honors=d['honors'], community=d['community'], careers=d['careers'], loyalty=d['loyalty'], closed_note=d['closed_note'], links=d['links'], founded=d['founded'], about=d['about'])
build('tremont-house-of-pizza', 'tremont.html.j2', 'tremont.css.j2', ['common.js', 'tremont.js'], FONTS, ['Pizza', 'Sandwiches', 'Italian', 'American'],
      "Concept for Tremont House of Pizza, built only from your own menu, copy and photos. Not your live site.", extra)
