"""Mr. Pizza Restaurant & Tavern (Gorham): 'Build your pie' price calculator from the shop's real price rules. usage: build_mrpizza.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import *
FONTS = [('Erica One', 'EricaOne-Regular', 400, 'normal'), ('Instrument Sans', 'InstrumentSans-Regular', 400, 'normal'), ('Instrument Sans', 'InstrumentSans-Bold', 700, 'normal'), ('Lora', 'Lora-Italic', 400, 'italic')]
def money(p): return f'${p:.2f}'.replace('.00', '') if p == int(p) else f'${p:.2f}'
def extra(d, img): return dict(money=money)
build('mr-pizza-gorham', 'mrpizza.html.j2', 'mrpizza.css.j2', ['mrpizza.js'], FONTS, ['Pizza', 'American', 'Seafood'],
      "Concept for Mr. Pizza Restaurant & Tavern, built only from your own menu, copy and photos. Not your live site.", extra)
