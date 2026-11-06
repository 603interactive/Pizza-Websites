"""Supreme House of Pizza (Exeter): split red/sea-blue site from the shop's own logo, with a menu 'tray' that tallies a real-price estimate. usage: build_exeter.py"""
import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import *
SLUG = 'supreme-house-of-pizza-exeter'
FONTS = [('Big Shoulders', 'BigShoulders-Bold', 700, 'normal'), ('Outfit', 'Outfit-Regular', 400, 'normal'), ('Outfit', 'Outfit-Bold', 700, 'normal'), ('DM Mono', 'DMMono-Regular', 400, 'normal')]
def money(p): return f'${p:.2f}'
def extra(d, img):
    byname = {(c['id'], i['name']): i for c in d['menu'] for i in c['items']}
    return dict(money=money, pick=lambda cid, n: byname[(cid, n)], logo=img('logo.webp'), mark=img('mark.webp'))
build(SLUG, 'exeter.html.j2', 'exeter.css.j2', ['exeter.js'], FONTS, ['Pizza', 'Seafood', 'Subs', 'Wings'],
      "Concept for Supreme House of Pizza, built only from the shop's own logo and menu. Not your live site.", extra)
