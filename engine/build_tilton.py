"""Tilton House of Pizza: brick-red / black / gold diner look with a tap-to-build "guest check" call-in order slip. usage: build_tilton.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import *
FONTS = [('IBM Plex Serif', 'IBMPlexSerif-Bold', 700, 'normal'), ('IBM Plex Serif', 'IBMPlexSerif-Italic', 400, 'italic'), ('Bricolage Grotesque', 'BricolageGrotesque-Regular', 400, 'normal'),
         ('Bricolage Grotesque', 'BricolageGrotesque-Bold', 700, 'normal'), ('DM Mono', 'DMMono-Regular', 400, 'normal')]
def money(p): return f'${p:.2f}'
def extra(d, img): return dict(money=money)
build('tilton-house-of-pizza-tilton', 'tilton.html.j2', 'tilton.css.j2', ['tilton.js'], FONTS, ['Pizza', 'Grinders', 'Seafood', 'Family restaurant'],
      "Concept for Tilton House of Pizza, built only from your own photos and menu. Not your live site.", extra)
