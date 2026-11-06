"""New England Pizza (Exeter): green + brick red + cream, big type, menu with a cross-menu craving finder. usage: build_nepizza.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import *
FONTS = [('Lora', 'Lora-Bold', 700, 'normal'), ('Lora', 'Lora-BoldItalic', 700, 'italic'), ('DM Mono', 'DMMono-Regular', 400, 'normal'), ('Outfit', 'Outfit-Regular', 400, 'normal'), ('Outfit', 'Outfit-Bold', 700, 'normal')]
def money(p): return f'${p:.2f}'
def extra(d, img): return dict(money=money)
build('new-england-pizza-exeter', 'nepizza.html.j2', 'nepizza.css.j2', ['nepizza.js'], FONTS, ['Pizza', 'Subs', 'Calzones', 'Salads'],
      "Concept for New England Pizza. Menu prices are unverified third-party figures. Not your live site.", extra)
