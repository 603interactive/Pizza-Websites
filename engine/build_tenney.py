"""Tenney Mountain Pizza (Plymouth NH): navy/red/mountain-blue sign palette, Trail Order Sheet (build-a-pizza + tap-to-add menu with search, phone-only ordering). usage: build_tenney.py"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib import *
FONTS = [('Erica One', 'EricaOne-Regular', 400, 'normal'), ('Bricolage Grotesque', 'BricolageGrotesque-Regular', 400, 'normal'), ('Bricolage Grotesque', 'BricolageGrotesque-Bold', 700, 'normal')]
def extra(d, img): return dict(instagram=d['instagram'], facebook=d['facebook'], total=sum(len(c['items']) for c in d['menu']))
build('tenney-mtn-pizza-plymouth', 'tenney.html.j2', 'tenney.css.j2', ['tenney.js'], FONTS, ['Pizza', 'Calzones', 'Subs', 'Italian', 'American'],
      "Concept for Tenney Mountain Pizza, built only from your own menu, copy and photos. Not your live site.", extra)
# lib's JSON-LD adds a priceRange and an OrderAction we cannot support (no prices published, phone-only): strip them, drop empty hours, re-zip.
import json as _j, re as _re, zipfile as _z
_out = ROOT / 'dist' / 'tenney-mtn-pizza-plymouth'; _idx = _out / 'site' / 'index.html'; _h = _idx.read_text()
def _fix(m):
    ld = _j.loads(m.group(1).replace('<\\/', '</')); [ld.pop(k, None) for k in ('priceRange', 'potentialAction', 'openingHoursSpecification')]
    return '<script type="application/ld+json">' + _j.dumps(ld).replace('</', '<\\/') + '</script>'
_idx.write_text(_re.sub(r'<script type="application/ld\+json">(.*?)</script>', _fix, _h, flags=_re.S))
_zp = _out / 'tenney-mtn-pizza-plymouth-netlify-site.zip'
with _z.ZipFile(_zp, 'w', _z.ZIP_DEFLATED) as zf:
    for p in sorted((_out / 'site').rglob('*')):
        if p.is_file(): zf.write(p, p.relative_to(_out / 'site'))
