"""Seabrook House of Pizza: sunny-boardwalk light theme, 'three ways to eat' + craving-first menu browser. usage: build_shop.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import *
FONTS = [('Big Shoulders Display', 'BigShoulders-Bold', 700, 'normal'), ('Work Sans', 'WorkSans-Regular', 400, 'normal'), ('Work Sans', 'WorkSans-Bold', 700, 'normal')]
build('seabrook-house-of-pizza-seabrook', 'shop.html.j2', 'shop.css.j2', ['shop.js'], FONTS, ['Pizza', 'Subs', 'Seafood', 'Salads', 'Calzones'],
      "Concept for Seabrook House of Pizza, built only from your own listings and photos. Not your live site.")
