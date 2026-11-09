"""Cantore's Pizza (West Lebanon NH): dark charcoal + hot-orange menu-board look, real menu text transcribed from the shop's PNG menus, real photo tiles cropped from them, phone ordering. usage: build_cantores.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import *
import json
SLUG = 'cantores-pizza-west-lebanon'
FONTS = [('Big Shoulders Display', 'BigShoulders-Bold', 700, 'normal'), ('Work Sans', 'WorkSans-Regular', 400, 'normal'), ('Work Sans', 'WorkSans-Bold', 700, 'normal')]
env.globals['theme'] = json.load(open(ROOT / 'clients' / SLUG / 'data.json'))['theme']
build('cantores-pizza-west-lebanon', 'plain.html.j2', 'plain.css.j2', ['plain.js'], FONTS, ['Pizza', 'Calzones', 'Subs', 'Pasta', 'Salads'],
      "Concept for Cantore's Pizza, built only from your own menu, copy and photos. Not your live site.", lambda d, img: dict(theme=d['theme'], gallery=d['gallery'], logo=d['logo'], specials=d['specials'], extras=d['extras'], about=d['about'], delivery=d['delivery'], delivery_link=d.get('delivery_link'), delivery_label=d.get('delivery_label'), facebook=d['facebook']))
strip_jsonld(SLUG)
