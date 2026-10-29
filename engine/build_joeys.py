"""Uncle Joey's: bespoke neon-sign site with the Chick Stix Builder. usage: build_joeys.py"""
import json, sys
sys.path.insert(0, str(__import__('pathlib').Path(__file__).resolve().parent))
from lib import *
FONTS = [('Erica One', 'EricaOne-Regular', 400, 'normal'), ('DM Mono', 'DMMono-Regular', 400, 'normal'), ('Instrument Sans', 'InstrumentSans-Regular', 400, 'normal'), ('Instrument Sans', 'InstrumentSans-Bold', 700, 'normal')]
SAUCES = [("Sweet n' sour", '#E88A1A'), ('BBQ', '#5B2A12'), ('Honey mustard', '#E9B923'), ('Buffalo', '#E2491B'), ('Garlic parmesan', '#F1E7C6'), ('Sweet heat', '#C8321C'), ('Ranch', '#F7F5EE'), ('Blue cheese', '#DCE3EE'), ('Teriyaki', '#4A2411'), ('Tartar', '#D9DDBA')]
def extra(d, img):
    menu = d['menu']; cs = next(c for c in menu if c['cat'] == 'Chick Stix')
    stix = [(int(sz.split()[0]), price_num(p)) for sz, p in cs['items'][0]['sizes']]
    jojos = [(int(sz.split()[0]), price_num(p)) for sz, p in cs['items'][1]['sizes']]
    fam = next(c for c in menu if c['cat'] == 'Family Dinners'); pack = next(i for i in fam['items'] if i['name'] == 'Tender Pack')
    two20 = 2 * dict(stix)[20]
    return dict(stix=stix, jojos=jojos, stix_json=json.dumps(stix), sauces=[dict(name=n, c=c) for n, c in SAUCES], crowd=dict(two20=two20, pack=price_num(pack['price'])))
build('uncle-joeys', 'joeys.html.j2', 'joeys.css.j2', ['common.js', 'joeys.js'], FONTS, ['Pizza', 'Chicken', 'Subs'],
      'Concept for Uncle Joey\'s, built only from your own menu and photo. Not your live site.', extra)
