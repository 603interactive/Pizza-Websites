"""Enfield House of Pizza (EHOP): maroon/gold wall-calendar site with The Week at EHOP (daily deal savings calculator). usage: build_enfield.py"""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import *
FONTS = [('Outfit', 'Outfit-Regular', 400, 'normal'), ('Outfit', 'Outfit-Bold', 700, 'normal'), ('Nothing You Could Do', 'NothingYouCouldDo-Regular', 400, 'normal')]
def money(p): return p if isinstance(p, str) else f'${p:.2f}'
def DAYS_ORDER(d): return sorted(d['days'], key=lambda x: (x['dow'] + 6) % 7)
def extra(d, img):
    menu = {c['cat']: c for c in d['menu']}
    lg = [dict(name='Large cheese', price=12.99)]
    for it in menu['Pizza']['items'][1:5]: lg.append(dict(name='Large ' + it['name'].lower(), price=it['prices'][1]))
    for it in menu['Specialty pizzas']['items']: lg.append(dict(name=it['name'], price=it['prices'][1]))
    return dict(money=money, days_json=json.dumps(DAYS_ORDER(d)), large_json=json.dumps(lg), facebook=d['facebook'], instagram=d['instagram'], apply_pdf=d['apply_pdf'],
                days=DAYS_ORDER(d), feature=d['feature'], lunchbox=d['lunchbox'], party=d['party'], story=d['story'], perks=d['perks'])
build('enfield-house-of-pizza', 'enfield.html.j2', 'enfield.css.j2', ['common.js', 'enfield.js'], FONTS, ['Pizza', 'Grinders', 'Calzones', 'Greek', 'American'],
      "Concept for Enfield House of Pizza, built only from your own menu, copy and photos. Not your live site.", extra)
