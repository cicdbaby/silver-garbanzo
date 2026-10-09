#!/usr/bin/env python3
"""Menzil · Gök görsel hattı.
Kodlu PNG'leri (A1.png, K3.png, C10.png ...) oyuna hazır webp'ye çevirir.
  A*  : zemin dokusu  -> olduğu gibi, 1024 kare (A7/A8/A9 şerit: 1536 genişlik)
  K/B/C*: yeşil fon   -> alfa, yeşil taşma temizliği, en büyük parça + yakın parçalar, kırp
  D*  : yeşil fon     -> alfa, kırp, 384
  E1  : yeşil fon     -> alfa (krater)
  E2-4: siyah fon     -> alfa = parlaklık (additive/normal karışım için)
Kullanım: python3 isle.py <girdi_klasörü> <çıktı_klasörü>
"""
import sys, os, re, json
import numpy as np
from PIL import Image
from scipy import ndimage as ndi

SIZE = {'A': 1024, 'K': 900, 'B': 720, 'C': 560, 'D': 384, 'E': 560}

def green_alpha(rgb):
    r, g, b = [rgb[..., i].astype(np.float32) for i in range(3)]
    # yeşil baskınlığı: g - max(r,b)
    dom = g - np.maximum(r, b)
    a = 1.0 - np.clip((dom - 28) / (90 - 28), 0, 1)       # 28 altı tam opak, 90 üstü tam şeffaf
    return a, dom

def despill(rgb, dom):
    out = rgb.astype(np.float32).copy()
    r, g, b = out[..., 0], out[..., 1], out[..., 2]
    lim = np.maximum(r, b) * 1.02 + 4
    spill = g > lim
    out[..., 1] = np.where(spill, lim, g)
    return np.clip(out, 0, 255).astype(np.uint8)

def keep_main(a, keep_ratio=0.02):
    """Ana gövdeyi ve ona göre anlamlı büyüklükteki parçaları tut; kopuk gölge/kir lekelerini at."""
    solid = a > 0.5
    solid = ndi.binary_opening(solid, iterations=2)
    lab, n = ndi.label(solid)
    if n == 0:
        return a
    sizes = ndi.sum(solid, lab, range(1, n + 1))
    big = sizes.max()
    keep = np.zeros(n + 1, bool)
    keep[1:] = sizes >= big * keep_ratio
    mask = keep[lab]
    mask = ndi.binary_dilation(mask, iterations=3)
    return a * mask

def trim(img, pad=6):
    al = np.array(img)[..., 3]
    ys, xs = np.where(al > 8)
    if len(xs) == 0:
        return img
    x0, x1 = max(0, xs.min() - pad), min(img.width, xs.max() + pad + 1)
    y0, y1 = max(0, ys.min() - pad), min(img.height, ys.max() + pad + 1)
    return img.crop((x0, y0, x1, y1))

def fit(img, S):
    k = S / max(img.size)
    if k < 1:
        img = img.resize((round(img.width * k), round(img.height * k)), Image.LANCZOS)
    return img

def process(path):
    code = os.path.splitext(os.path.basename(path))[0].upper()
    m = re.match(r'([A-E])(\d+)$', code)
    if not m:
        return None, None, 'kod adı değil'
    cat, num = m.group(1), int(m.group(2))
    im = Image.open(path).convert('RGB')
    rgb = np.array(im)
    info = {}
    if cat == 'A':
        out = im
        if num in (7, 8, 9):
            out = fit(out, 1536)
        else:
            out = out.resize((SIZE['A'], SIZE['A']), Image.LANCZOS)
        # dikiş kontrolü: kenar farkı
        h = np.array(out).astype(np.float32)
        info['dikis_LR'] = round(float(np.abs(h[:, 0] - h[:, -1]).mean()), 1)
        if num not in (7, 8, 9):
            info['dikis_UD'] = round(float(np.abs(h[0] - h[-1]).mean()), 1)
        return code, out, info
    if cat == 'E' and num >= 2:
        f = rgb.astype(np.float32)
        lum = f.max(axis=2)
        a = np.clip((lum - 10) / 60, 0, 1)
        col = np.clip(f / np.maximum(a[..., None], 1e-3), 0, 255)
        out = Image.fromarray(np.dstack([col.astype(np.uint8), (a * 255).astype(np.uint8)]), 'RGBA')
        return code, fit(trim(out), SIZE['E']), info
    a, dom = green_alpha(rgb)
    green_px = float((dom > 90).mean())
    a = keep_main(a, 0.004 if cat == 'K' else 0.02)
    # kenar yumuşatma
    a = ndi.gaussian_filter(a, 0.7) * (a > 0.02)
    col = despill(rgb, dom)
    out = Image.fromarray(np.dstack([col, (np.clip(a, 0, 1) * 255).astype(np.uint8)]), 'RGBA')
    out = fit(trim(out), SIZE[cat])
    # yeşil kaçağı kontrolü: opak piksellerde kalan yeşil baskınlık
    o = np.array(out).astype(np.float32)
    op = o[..., 3] > 200
    gl = (o[..., 1] - np.maximum(o[..., 0], o[..., 2]))[op]
    info['yesil_fon_%'] = round(green_px * 100, 1)
    info['kalan_yesil_%'] = round(float((gl > 20).mean() * 100) if op.any() else 0, 2)
    return code, out, info

def main(src, dst):
    os.makedirs(dst, exist_ok=True)
    rep = {}
    for f in sorted(os.listdir(src)):
        if not f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp')):
            continue
        code, out, info = process(os.path.join(src, f))
        if code is None:
            rep[f] = info
            continue
        q = 82 if code[0] in 'AK' else 86
        p = os.path.join(dst, code + '.webp')
        out.save(p, 'WEBP', quality=q, method=6)
        info.update(boyut=out.size, kb=os.path.getsize(p) // 1024)
        rep[code] = info
    print(json.dumps(rep, ensure_ascii=False, indent=1))

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
