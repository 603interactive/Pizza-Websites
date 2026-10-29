import json, re, sys
from pathlib import Path
from PIL import Image
sys.path.insert(0, 'engine')
from crop_capture import f, save, matte, stitch

def mk_key(k):
    m = re.search(r'item-4000000(\d+)_', k)
    return 'p-' + m.group(1) if m else 'p-' + re.sub(r'[^a-z0-9]', '', k.split('_')[1][:10] if '_' in k else k)[:12]

# ---------- Mickey's ----------
out = Path('clients/mickeys-ny-pizza/img')
plan = json.load(open('clients/mickeys-ny-pizza/capture_plan.json'))
shots = 'gu2lpq fm96wj yd7hho c7zlun byw128 k1quvb 0g3fuc 2y5jmp pncrix ouw9fj axl7wv 9wg4mv ygmleo rd946g k63gik rofq2p w3k81t 4tc9z9 t0y1y1 nrrj1x p26cba rj0ulg x2wfsr cfyky1 jw3e2i ggu1xp mwjex5 ly7ly7'.split()
exclude = {'7/item-400000049379389107_1737436147.jpg': 'social-media screenshot with caption overlay',
           '2/item-400000016537295532_1682896199.jpg': 'studio-style photo, possibly stock; not used until the owner confirms it is theirs',
           '7/item-400000042028862957_1717531388.png': 'text overlay and another brand name in frame',
           '7/item-400000036889918377_1702409478.jpg': 'Instagram carousel badge in frame',
           '0/item-400000000324578900_1683908836.jpg': "another business's sign in frame"}
made = {}
for sfx, shot in zip(shots, plan['shots']):
    im = Image.open(f(sfx)).convert('RGB')
    for c in shot['crops']:
        if c['key'] in exclude: continue
        name = mk_key(c['key']) + '.webp'
        save(im.crop(tuple(c['box'])), out / name, 80)
        made[c['key']] = name
print('mickeys cards', len(made))
stitch([('0wnd8m', 0, 0), ('czu5gu', 640, 0), ('2upej6', 0, 600), ('so2zy7', 640, 600), ('qna3jd', 0, 977), ('tja2ru', 640, 977)], (1440, 1577), out / 'hero.jpg', 82)
h = Image.open(out / 'hero.jpg'); save(h.resize((720, 789), Image.LANCZOS), out / 'hero-720.jpg', 80)
print('logo', matte('obw1y1', 'jabtnv', (0, 0, 537, 438), out / 'logo.png'))
json.dump({'map': made, 'excluded': exclude}, open('clients/mickeys-ny-pizza/img/_map.json', 'w'), indent=1)

# ---------- Rochester ----------
out = Path('clients/rochester-house-of-pizza/img')
R = [('108bqs', (0, 0, 625, 480), '1c89c3_943f3c1ec2d065670002d4d518aabb51.jpg'),
     ('jiazdk', (0, 0, 503, 480), '1c89c3_4379870f7551b18e806a355c00018487.jpg'),
     ('maj3jj', (0, 0, 448, 296), '1c89c3_eda6b539e0a44370d4fa9b1506ae1735.jpg'),
     ('maj3jj', (0, 300, 448, 516), '1c89c3_5c80274b4cb73faf99fc92e1e3b509b9.jpg'),
     ('39p6wk', (0, 0, 416, 336), '1c89c3_f5468160f54e60183485583e43aa1d1e.jpg'),
     ('39p6wk', (0, 340, 448, 502), '1c89c3_9a111a59f2cdae3fb09ca04762e261d3.jpg'),
     ('qfr7rn', (0, 0, 427, 237), '1c89c3_d0970a76f50a776c7648d4d92e57554f.jpg'),
     ('qfr7rn', (0, 240, 448, 518), '1c89c3_b9db74ba174e7e9bf68f2f44eb623eb6.jpg'),
     ('vbizji', (0, 0, 448, 214), '1c89c3_4c73011dcbbec59edf33cad88a55fa2f.jpg')]
rm = {}
for sfx, box, key in R:
    name = 'p-' + key.split('_')[1][:8] + '.webp'
    save(Image.open(f(sfx)).convert('RGB').crop(box), out / name, 84)
    rm[key] = name
stitch([('wzbmuo', 0, 0), ('323lf1', 480, 0), ('pufrcu', 0, 200), ('puvaae', 480, 200)], (1280, 800), out / 'hero.jpg', 84)
print('rlogo', matte('gb60cj', 'rvykdk', (0, 0, 720, 581), out / 'logo.png'))
json.dump({'map': rm}, open(out / '_map.json', 'w'), indent=1)
