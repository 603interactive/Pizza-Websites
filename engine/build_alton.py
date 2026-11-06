"""Alton Village Pizza: gingham tablecloth + olive-oil green, with a Pizza Price Check (build-your-own vs. specialty math). usage: build_alton.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import *
FONTS = [('National Park', 'NationalPark-Bold', 700, 'normal'), ('National Park', 'NationalPark-Regular', 400, 'normal'), ('Instrument Sans', 'InstrumentSans-Regular', 400, 'normal'), ('Instrument Sans', 'InstrumentSans-Bold', 700, 'normal')]
def money(p): return f'${p:.2f}'
def extra(d, img): return dict(money=money, calc_json=json.dumps(d['calc']), tops_json=json.dumps(d['toppings']))
build('alton-village-pizza-alton', 'alton.html.j2', 'alton.css.j2', ['alton.js'], FONTS, ['Pizza', 'Subs', 'Calzones', 'Greek'],
      "Concept for Alton Village Pizza, built only from your website menu and Instagram photos. Not your live site.", extra)
