#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Crée des variantes de cadrage (zoom + recadrage + étalonnage) pour les carrousels."""
import os
from PIL import Image, ImageEnhance

VIS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "visuels")

# source -> nombre de variantes à créer
VARIANTS = {
    "07-miroir-magique": 3,
    "03-livre-or-audio": 1,
    "10-vin-honneur": 2,
    "04-neon": 3,
    "01-hero": 1,
    "05-cierges-magiques": 3,
    "06-bulles-confettis": 3,
    "09-premiere-danse": 3,
    "08-piscine-balles": 3,
}

# presets de cadrage : (zoom, ancrage_x, ancrage_y, chaleur_extra)
PRESETS = [
    (1.15, 0.5, 0.5, 0),
    (1.30, 0.5, 0.26, 0),
    (1.30, 0.5, 0.74, 0.05),
    (1.45, 0.32, 0.5, 0.05),
]

OUT_W, OUT_H = 900, 675  # ratio 4:3

def variant(im, i):
    z, xa, ya, warm = PRESETS[i]
    w, h = im.size
    cw = w / z
    ch = cw * (OUT_H / OUT_W)
    if ch > h:
        ch = h / z
        cw = ch / (OUT_H / OUT_W)
    left = (w - cw) * xa
    top = (h - ch) * ya
    crop = im.crop((left, top, left + cw, top + ch)).resize((OUT_W, OUT_H), Image.LANCZOS)
    if warm:
        crop = ImageEnhance.Color(crop).enhance(1.07)
        crop = ImageEnhance.Brightness(crop).enhance(1.04)
    return crop

for src, n in VARIANTS.items():
    p = os.path.join(VIS, src + ".jpg")
    if not os.path.isfile(p):
        print("⚠️ absent :", src); continue
    im = Image.open(p).convert("RGB")
    for i in range(n):
        out = os.path.join(VIS, f"{src}-v{i+1}.jpg")
        variant(im, i).save(out, "JPEG", quality=85, optimize=True)
        print("✅", os.path.basename(out))
print("Terminé.")
