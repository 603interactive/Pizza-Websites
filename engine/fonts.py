"""Subset local OFL fonts to Latin and save as WOFF for self-hosting."""
from fontTools import subset
from fontTools.ttLib import TTFont
from pathlib import Path
SRC = Path('/mnt/skills/examples/canvas-design/canvas-fonts')
OUT = Path(__file__).resolve().parent / 'fonts'
UNI = 'U+0020-007E,U+00A0-00FF,U+2013-2014,U+2018-201D,U+2022,U+2026,U+20AC,U+2122,U+00B7,U+2190-2193,U+2605'
FONTS = ['BigShoulders-Bold', 'BigShoulders-Regular', 'WorkSans-Regular', 'WorkSans-Bold', 'WorkSans-Italic',
         'NationalPark-Bold', 'NationalPark-Regular', 'Outfit-Regular', 'Outfit-Bold', 'PoiretOne-Regular', 'NothingYouCouldDo-Regular',
         'InstrumentSerif-Regular', 'InstrumentSerif-Italic', 'Tektur-Regular', 'Tektur-Medium', 'IBMPlexSerif-Regular', 'IBMPlexSerif-Bold', 'IBMPlexSerif-Italic']
for name in FONTS:
    if (OUT / f'{name}.woff').exists(): continue
    opts = subset.Options(); opts.flavor = 'woff'; opts.layout_features = ['*']; opts.name_IDs = ['*']
    f = TTFont(SRC / f'{name}.ttf')
    s = subset.Subsetter(opts); s.populate(unicodes=subset.parse_unicodes(UNI)); s.subset(f)
    f.flavor = 'woff'; f.save(OUT / f'{name}.woff')
    print(name, (OUT / f'{name}.woff').stat().st_size)
for lic in set(n.split('-')[0] for n in FONTS):
    if not (SRC / f'{lic}-OFL.txt').exists() or (OUT / f'{lic}-OFL.txt').exists(): continue
    (OUT / f'{lic}-OFL.txt').write_bytes((SRC / f'{lic}-OFL.txt').read_bytes())
