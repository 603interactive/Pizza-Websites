"""Shared builder for the `plain` template (cream/dark theme from data.json, live text menu, call/order bar, no photos unless supplied). usage: build_plainshop.py <slug>"""
import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import *
FONTS = [('Big Shoulders Display', 'BigShoulders-Bold', 700, 'normal'), ('Work Sans', 'WorkSans-Regular', 400, 'normal'), ('Work Sans', 'WorkSans-Bold', 700, 'normal')]
def run(slug, cuisines):
    d0 = json.load(open(ROOT / 'clients' / slug / 'data.json')); env.globals['theme'] = d0['theme']
    build(slug, 'plain.html.j2', 'plain.css.j2', ['plain.js'], FONTS, cuisines, f"Concept for {d0['name']}, built only from your own public menu and copy. Not your live site.",
          lambda d, img: {k: d.get(k) for k in ('theme', 'gallery', 'logo', 'specials', 'extras', 'about', 'delivery', 'facebook', 'badge', 'order_url', 'order_label', 'menu_note')})
    drop = ['priceRange'] + ([] if d0['order_url'] else ['potentialAction']) + ([] if d0['locations'][0]['hours'] else ['openingHoursSpecification'])
    strip_jsonld(slug, tuple(drop))
