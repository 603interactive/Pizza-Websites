"""White Lake Pizza (West Ossipee): roadside-sign blue/red/cream site with summer vs off-season hours toggle + live status. usage: build_wlp.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import *
FONTS = [('Young Serif', 'YoungSerif-Regular', 400, 'normal'), ('Work Sans', 'WorkSans-Regular', 400, 'normal'), ('Work Sans', 'WorkSans-Bold', 700, 'normal')]
def money(p): return f'${p:.2f}'
def extra(d, img):
    loc = d['locations'][0]
    def rows(hrs):
        out = []
        for r in week(dict(hours=hrs)):
            h = next(h for h in hrs if r['dow'] in h['dow'])
            out.append(dict(r, dine='Dining room closes ' + fmt12(h['dine'])))
        return out
    hj = json.dumps({'off': loc['hours'], 'summer': loc['hours_summer']})
    return dict(money=money, week_off=rows(loc['hours']), week_summer=rows(loc['hours_summer']), hours_json=hj)
build('white-lake-pizza-west-ossipee', 'wlp.html.j2', 'wlp.css.j2', ['wlp.js'], FONTS, ['Pizza', 'Calzones', 'Subs', 'Pasta'],
      "Concept for White Lake Pizza, built only from your own menu, copy and photos. Not your live site.", extra)
