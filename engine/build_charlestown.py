"""Charlestown House of Pizza: bespoke parlor site with the Soft-Serve Sundae Maker. usage: build_charlestown.py"""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import *
FONTS = [('Young Serif', 'YoungSerif-Regular', 400, 'normal'), ('Smooch Sans', 'SmoochSans-Medium', 500, 'normal'), ('Lora', 'Lora-Regular', 400, 'normal'), ('Lora', 'Lora-Bold', 700, 'normal')]
def extra(d, img):
    ic = d['icecream']
    ICONS={'pizza':'i-pizza','specialty-pizza':'i-slice','calzones':'i-calzone','subs-wraps':'i-sub','salads':'i-salad','pasta':'i-pasta','grill-seafood':'i-burger','sides':'i-side','kids':'i-kids','drinks':'i-drink'}
    PHOTOS={'pizza':('pizza.jpg','Pepperoni pizza on a butcher-block counter'),'grill-seafood':('chicken.jpg','Crispy chicken sandwich with fries'),'sides':('tenders.jpg','Fried chicken tenders with dipping sauce')}
    return dict(photos=PHOTOS, icons=ICONS, ic_json=json.dumps({k: ic[k] for k in ('scoops', 'flurries', 'sundaes', 'floats', 'shakes')}), icecream=ic, catering=d['catering'], delivery=d['delivery'], links=d['links'], about=d['about'])
build('charlestown-house-of-pizza', 'charlestown.html.j2', 'charlestown.css.j2', ['common.js', 'charlestown.js'], FONTS, ['Pizza', 'Sandwiches', 'Italian', 'Ice Cream'],
      "Concept for Charlestown House of Pizza, built only from your own menu and copy. Not your live site.", extra)
