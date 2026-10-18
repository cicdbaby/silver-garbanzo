# Menzil · Gök — GÖREV 12: Patlama (10 görsel)

Her yer aynı patlama setini kullanır. Büyüklüğü kod ayarlıyor: vuran silahın gücü (İHA başlığı küçük, balistik büyük) ve vurulan tesisin büyüklüğü. Yakıt tesisinde yangın daha büyük ve uzun sürüyor. Görseller yalnızca dokuyu (texture, yüzey görüntüsü) veriyor; oyun onları büyütüp döndürüyor, sırayla gösteriyor ve söndürüyor.

## GPT'ye ilk mesaj (bir kez yapıştır)

```
I need 10 visual-effect images for a top-down military strategy game, one image per message. Rules for every image:
- Camera exactly overhead, looking straight down at the ground. No horizon, no perspective, no side view.
- Photographic realism, like high-altitude drone footage of a real event. Not cartoon, not painterly, no lens flare, no added glow, no text, no watermark, no border.
- Subject centred, filling about 80% of a square 1024×1024 frame, nothing else in the frame.
- Background exactly as each prompt says: PURE BLACK (#000000) for fire and light, or TRANSPARENT (PNG with alpha; if transparency is impossible, plain pure white).
- Anything solid (smoke, dirt, debris) is lit by soft late-afternoon sun from the lower-left.
After the first image, match it in colour grade, realism and level of detail.
Save each file with the name I give.
```

Sonra aşağıdakileri sırayla, her biri ayrı mesaj olarak gönder.

---

### Patlamanın üç anı (oyun bunları art arda oynatıyor)

**X_fb_a** — çakma
```
Seen from directly above, the first 20 milliseconds of a high-explosive warhead detonating on the ground: a blinding white-yellow core, a sharp circular shock flash around it, short radial jets of hot gas. Pure black background.
```

**X_fb_b** — ateş topu
```
Seen from directly above, the same explosion half a second later at its peak: a large boiling fireball, white-yellow centre, orange and deep red turbulent lobes, black soot veins folding through it, debris streaks radiating outward. Pure black background.
```

**X_fb_b2** — ateş topu, ikinci biçim (her patlama aynı görünmesin)
```
Seen from directly above, a different explosion fireball at its peak: asymmetric, blown toward one side, ragged orange and red tongues, a darker smoky edge, sparks thrown far on one side. Pure black background.
```

**X_fb_c** — dumana dönüş
```
Seen from directly above, the same explosion two seconds later: the fireball rolling into a mass of black and brown smoke, orange fire still glowing deep inside the folds, embers scattered around it. Pure black background.
```

### Yangın (vurulan tesis, oyun büyüklüğünü ayarlıyor)

**X_fire1**
```
Seen from directly above, a large fire burning on the ground after a missile strike: tall turbulent flames seen from the top, bright yellow-orange tongues with deep red edges, black soot curling out of the flames, burning wreckage visible inside. Pure black background.
```

**X_fire2** — ikinci biçim
```
Seen from directly above, a different large fire: a long irregular patch of flames spreading across burning debris, several separate flame cores, sparks rising. Pure black background.
```

### Duman, krater, havada önleme, enkaz

**X_smoke**
```
Seen from directly above, a single huge billowing cloud of thick black smoke from a burning fuel fire, dense rolling cauliflower shapes, brown-black, soft feathered edges. Transparent background.
```

**X_crater**
```
Seen from directly above, a fresh crater from a heavy explosion on open ground: raw dark earth, a steep pit, a ring of thrown-out soil, long radial ejecta rays, a wide black scorch fading to the natural ground at the edges. The edges must fade smoothly into transparency. Transparent background.
```

**X_air**
```
Seen from directly above, a missile destroyed in mid-air by an interceptor: a bright white-orange burst, a ring of glowing fragments, a cone of debris continuing forward, a short smoke puff. Pure black background.
```

**X_debris**
```
Seen from directly above, a burst of dark metal and concrete debris chunks of many sizes flying outward from a centre point, many of them glowing hot at the edges, thin smoke trails and bright sparks between them. Pure black background.
```

---

## Teslim

PNG olarak, bu adlarla, tek zip. Siyah fonluları ben ışık olarak işliyorum. Kredi kısıtlıysa ilk dördü (`X_fb_a`, `X_fb_b`, `X_fb_c`, `X_fire1`) yeter; geri kalanı çeşitlilik katar.
