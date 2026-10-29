"""Build a screenshot-capture plan for a client's photos.
The browser renders photos into an 800x600 viewport; each shot is saved as a PNG
and later cropped into separate image files by crop_capture.py."""
import json, sys
slug = sys.argv[1]
d = json.load(open(f"/home/claude/pizza-sites/clients/{slug}/data.json"))
base = d["img_base"]
keys = []
def add(k):
    if k and k not in keys: keys.append(k)
for s in d.get("signatures", []): add(s.get("img"))
for p in d.get("promo_cards", []): add(p.get("img"))
for c in d["menu"]:
    for it in c["items"]: add(it.get("img"))
shots = []
# card photos: 4:5 at 400x500, two per shot
for i in range(0, len(keys), 2):
    pair = keys[i:i+2]
    cells, crops = [], []
    for j, k in enumerate(pair):
        x = j * 400
        cells.append([base + k, x, 50, 400, 500])
        crops.append({"name": "card-" + k.split("/")[-1].rsplit(".", 1)[0][-14:], "key": k, "box": [x, 50, x + 400, 550]})
    shots.append({"cells": cells, "crops": crops})
json.dump({"slug": slug, "shots": shots}, open(f"/home/claude/pizza-sites/clients/{slug}/capture_plan.json", "w"), indent=1)
print(len(keys), "photos ->", len(shots), "shots")
for n, s in enumerate(shots):
    print(f"{n}: S({json.dumps([c for c in s['cells']])})")
