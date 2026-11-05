"""Pelham House of Pizza: cream + blue + tomato-red site with a menu styled like the shop's own in-store menu boards. usage: build_phop.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import *
FONTS = [('Young Serif', 'YoungSerif-Regular', 400, 'normal'), ('Work Sans', 'WorkSans-Regular', 400, 'normal'), ('Work Sans', 'WorkSans-Bold', 700, 'normal')]
def money(p): return f'${p:.2f}'
def extra(d, img): return dict(money=money)
build('pelham-house-of-pizza-pelham', 'phop.html.j2', 'phop.css.j2', ['phop.js'], FONTS, ['Pizza', 'Subs', 'Salads', 'Seafood'],
      "Concept for Pelham House of Pizza, built only from your own photos and menu board. Not your live site.", extra)
