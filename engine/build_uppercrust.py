"""Upper Crust Pizzeria (Tilton): chalkboard slate + buffalo plaid site with a live split-shift Week Board and 'what time are you hungry' slider. usage: build_uppercrust.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import *
FONTS = [('Bricolage Grotesque', 'BricolageGrotesque-Regular', 400, 'normal'), ('Bricolage Grotesque', 'BricolageGrotesque-Bold', 700, 'normal'),
         ('Nothing You Could Do', 'NothingYouCouldDo-Regular', 400, 'normal'), ('DM Mono', 'DMMono-Regular', 400, 'normal')]
T0, T1 = 11 * 60, 21 * 60
def mins(s): h, m = map(int, s.split(':')); return h * 60 + m
def money(p): return f'${p:.2f}'
def extra(d, img):
    loc = d['locations'][0]; rows = []; wk = []
    for dow, day in DAYS:
        sh = sorted([h for h in loc['hours'] if dow in h['dow']], key=lambda h: h['open'])
        bars = [dict(left=round((mins(h['open']) - T0) / (T1 - T0) * 100, 2), width=round((mins(h['close']) - mins(h['open'])) / (T1 - T0) * 100, 2), label=f"{fmt12(h['open'])} to {fmt12(h['close'])}") for h in sh]
        txt = ', '.join(f"{fmt12(h['open'])} – {fmt12(h['close'])}" for h in sh) or 'Closed'
        gap = None
        if len(sh) > 1: a = (mins(sh[0]['close']) - T0) / (T1 - T0) * 100; b = (mins(sh[1]['open']) - T0) / (T1 - T0) * 100; gap = dict(left=round(a, 2), width=round(b - a, 2))
        rows.append(dict(dow=dow, day=day, bars=bars, text=txt, gap=gap, shifts=len(sh)))
        wk.append(dict(dow=dow, day=day, text=txt))
    ticks = [dict(h=fmt12(f'{h}:00'), left=round((h * 60 - T0) / (T1 - T0) * 100, 2)) for h in (12, 14, 16, 18, 20)]
    return dict(rows=rows, week=wk, ticks=ticks, money=money, t0=T0, t1=T1)
build('upper-crust-pizzeria-tilton', 'uppercrust.html.j2', 'uppercrust.css.j2', ['common.js', 'uppercrust.js'], FONTS, ['Pizza', 'Subs', 'Italian', 'American'],
      "Concept for Upper Crust Pizzeria, built only from your own menu, hours and photos. Not your live site.", extra)
