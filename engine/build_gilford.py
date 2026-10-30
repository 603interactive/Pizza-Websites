"""Gilford House of Pizza (GHOP): Greek-key black/red/cream site with the Delivery Desk ($4 flat vs delivery-app fees). usage: build_gilford.py"""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import *
FONTS = [('IBM Plex Serif', 'IBMPlexSerif-Regular', 400, 'normal'), ('IBM Plex Serif', 'IBMPlexSerif-Italic', 400, 'italic'), ('IBM Plex Serif', 'IBMPlexSerif-Bold', 700, 'normal'),
         ('Tektur', 'Tektur-Regular', 400, 'normal'), ('Tektur', 'Tektur-Medium', 500, 'normal')]
def money(p): return p if isinstance(p, str) else f'${p:.2f}'
def rows(hours):
    nm = {1: 'Mon', 2: 'Tue', 3: 'Wed', 4: 'Thu', 5: 'Fri', 6: 'Sat', 0: 'Sun'}
    out = []
    for h in hours:
        ds = sorted(h['dow'], key=lambda x: (x + 6) % 7)
        label = nm[ds[0]] if len(ds) == 1 else f'{nm[ds[0]]} – {nm[ds[-1]]}'
        out.append(dict(label=label, dow=h['dow'], text=f"{fmt12(h['open'])} – {fmt12(h['close'])}"))
    return out
def extra(d, img):
    loc = d['locations'][0]
    return dict(money=money, delivery=d['delivery'], specials=d['specials'], facebook=d['facebook'], winter=rows(loc['hours']), summer=rows(loc['hours_summer']),
                winter_json=json.dumps(loc['hours']), summer_json=json.dumps(loc['hours_summer']), dd_json=json.dumps(d['delivery']))
build('gilford-house-of-pizza', 'gilford.html.j2', 'gilford.css.j2', ['common.js', 'gilford.js'], FONTS, ['Pizza', 'Subs', 'Calzones', 'Greek', 'American'],
      "Concept for Gilford House of Pizza, built only from your own menu, copy and photos. Not your live site.", extra)
