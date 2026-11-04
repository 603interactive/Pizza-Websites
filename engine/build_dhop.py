"""Durham House of Pizza: 'The Late Shift' night-theme site with a live week-at-a-glance hours scrubber (handles 2 AM closes). usage: build_dhop.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import *
FONTS = [('Smooch Sans', 'SmoochSans-Medium', 500, 'normal'), ('Outfit', 'Outfit-Regular', 400, 'normal'), ('Outfit', 'Outfit-Bold', 700, 'normal')]
def money(p): return f'${p:.2f}'.replace('.00', '') if p == int(p) else f'${p:.2f}'
def extra(d, img):
    loc = d['locations'][0]
    rows = [dict(r, short=r['day'][:3], late=any(r['dow'] in h['dow'] and h['close'] < h['open'] for h in loc['hours'])) for r in week(loc)]
    return dict(money=money, week_order=rows)
build('durham-house-of-pizza-durham', 'dhop.html.j2', 'dhop.css.j2', ['dhop.js'], FONTS, ['Pizza', 'Salads', 'Calzones'],
      "Concept for Durham House of Pizza, built only from your own menu, copy and photos. Not your live site.", extra)
