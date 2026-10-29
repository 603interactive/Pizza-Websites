"""Turn browser capture screenshots into the site's image files.
Captures are 800x600 frames of the shop's own photos rendered at 1:1 in the browser."""
import json, sys
from pathlib import Path
from PIL import Image
import numpy as np
TR = Path('/root/.claude/projects/-home-claude/43f853ae-e6a4-50f3-9135-5255fa989299/tool-results')
f = lambda sfx: next(TR.glob(f'*-{sfx}.*'))

def save(im, out, q=82):
    out.parent.mkdir(parents=True, exist_ok=True)
    if out.suffix == '.webp': im.save(out, 'WEBP', quality=q, method=6)
    elif out.suffix == '.png': im.save(out, optimize=True)
    else: im.convert('RGB').save(out, 'JPEG', quality=q, optimize=True, progressive=True)

def matte(black_sfx, white_sfx, box, out):
    b = np.asarray(Image.open(f(black_sfx)).convert('RGB').crop(box)).astype(np.float32)
    w = np.asarray(Image.open(f(white_sfx)).convert('RGB').crop(box)).astype(np.float32)
    a = 1.0 - (w - b).mean(axis=2) / 255.0
    a = np.clip(a, 0, 1)
    rgb = np.where(a[..., None] > 0.004, b / np.maximum(a[..., None], 0.004), 0)
    rgba = np.dstack([np.clip(rgb, 0, 255), a * 255]).astype(np.uint8)
    im = Image.fromarray(rgba, 'RGBA')
    bbox = im.getchannel('A').point(lambda v: 255 if v > 8 else 0).getbbox()
    im = im.crop(bbox)
    save(im, out)
    return im.size

def stitch(tiles, size, out, q=80):
    W, H = size
    canvas = Image.new('RGB', (W, H))
    for sfx, ox, oy in tiles:
        t = Image.open(f(sfx)).convert('RGB')
        canvas.paste(t, (ox, oy))
    # paste in order so later tiles overwrite overlaps; crop to size
    save(canvas, out, q)
    return canvas.size
