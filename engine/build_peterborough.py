"""Peterborough Pizza Barn: cream + barn-red look, full text menu from the shop site, phone ordering (delivery via SweenEats). usage: build_peterborough.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import *
import json
SLUG = 'peterborough-pizza-barn'
FONTS = [('Big Shoulders Display', 'BigShoulders-Bold', 700, 'normal'), ('Work Sans', 'WorkSans-Regular', 400, 'normal'), ('Work Sans', 'WorkSans-Bold', 700, 'normal')]
env.globals['theme'] = json.load(open(ROOT / 'clients' / SLUG / 'data.json'))['theme']
build('peterborough-pizza-barn', 'plain.html.j2', 'plain.css.j2', ['plain.js'], FONTS, ["Pizza", "Subs", "American"],
      "Concept for Peterborough Pizza Barn, built only from your own menu, copy and photos. Not your live site.", lambda d, img: dict(theme=d['theme'], gallery=d['gallery'], logo=d['logo'], specials=d['specials'], extras=d['extras'], about=d['about'], delivery=d['delivery'], delivery_link=d.get('delivery_link'), delivery_label=d.get('delivery_label'), facebook=d['facebook']))
strip_jsonld(SLUG)
