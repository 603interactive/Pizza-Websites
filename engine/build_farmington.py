"""Farmington House of Pizza: marigold editorial site with the Pie Studio (build-vs-buy topping pricer). usage: build_farmington.py"""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import *
FONTS = [('Instrument Serif', 'InstrumentSerif-Regular', 400, 'normal'), ('Instrument Serif', 'InstrumentSerif-Italic', 400, 'italic'),
         ('Instrument Sans', 'InstrumentSans-Regular', 400, 'normal'), ('Instrument Sans', 'InstrumentSans-Bold', 700, 'normal')]
def money(p): return p if isinstance(p, str) else f'${p:.2f}'
def extra(d, img):
    return dict(money=money, studio=d['studio'], studio_json=json.dumps(d['studio']), facebook=d['facebook'], tax_note=d['tax_note'],
                menu_ids=[slugify(c['cat']) for c in d['menu']], zip=zip)
build('farmington-house-of-pizza', 'farmington.html.j2', 'farmington.css.j2', ['common.js', 'farmington.js'], FONTS, ['Pizza', 'Subs', 'Greek', 'Italian', 'American'],
      "Concept for Farmington House of Pizza, built only from your own menu, copy and photos. Not your live site.", extra)
