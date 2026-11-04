"""Brookside Pizza II & The Tap, Belmont NH: cream/black/red saloon-menu look with a live 'Day Dial' (slices / kitchen / bar by hour). usage: build_brookside.py"""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import *
FONTS = [('Gloock', 'Gloock-Regular', 400, 'normal'), ('Arsenal SC', 'ArsenalSC-Regular', 400, 'normal'),
         ('Instrument Sans', 'InstrumentSans-Regular', 400, 'normal'), ('Instrument Sans', 'InstrumentSans-Bold', 700, 'normal')]
def money(p): return p if isinstance(p, str) else f'${p:.2f}'
def extra(d, img): return dict(money=money, brk_json=json.dumps(dict(slices_until=d['slices_until'], bar=d['bar'])))
build('brookside-pizza-ii-belmont', 'brookside.html.j2', 'brookside.css.j2', ['common.js', 'brookside.js'], FONTS, ['Pizza', 'Subs', 'Italian', 'American', 'Bar food'],
      "Concept for Brookside Pizza II, built only from your own menu, copy and photos. Not your live site.", extra)
