"""Papa Jay's Pizzeria (Dover NH): iron/amber depot-board site with the Crowd Planner (cheapest pizza mix for N people). usage: build_papajays.py"""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import *
FONTS = [('Big Shoulders', 'BigShoulders-Bold', 700, 'normal'), ('Work Sans', 'WorkSans-Regular', 400, 'normal'), ('Work Sans', 'WorkSans-Bold', 700, 'normal')]
def money(p): return p if isinstance(p, str) else f'${p:.2f}'
def extra(d, img):
    return dict(money=money, sizes_json=json.dumps(d['sizes']), specs_json=json.dumps(d['specs']), email_json=json.dumps(d['email']), email=d['email'], facebook=d['facebook'],
                towns=d['towns'], specialties=d['specialties'], letter=d['letter'], owner=d['owner'], specs=d['specs'])
build('papa-jays-pizzeria', 'papajays.html.j2', 'papajays.css.j2', ['common.js', 'papajays.js'], FONTS, ['Pizza', 'Subs', 'Wings', 'Italian', 'American'],
      "Concept for Papa Jay's Pizzeria, built only from your own menu, copy and photos. Not your live site.", extra)
