"""Newport Village Pizza: teal + butter-gold + ink awning-stripe site with a receipt-tape "Pie Math" planner. usage: build_newport.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import *
FONTS = [('Big Shoulders', 'BigShoulders-Bold', 700, 'normal'), ('Instrument Sans', 'InstrumentSans-Regular', 400, 'normal'), ('Instrument Sans', 'InstrumentSans-Bold', 700, 'normal'), ('DM Mono', 'DMMono-Regular', 400, 'normal')]
def money(p): return f'${p:.2f}'.replace('.00', '') if p == int(p) else f'${p:.2f}'
def extra(d, img): return dict(money=money, planner_json=json.dumps(d['planner']))
build('newport-village-pizza-newport', 'newport.html.j2', 'newport.css.j2', ['newport.js'], FONTS, ['Pizza', 'Calzones', 'Grinders', 'Italian', 'Greek'],
      "Concept for Newport Village Pizza, built only from your own website's menu and photos. Not your live site.", extra)
