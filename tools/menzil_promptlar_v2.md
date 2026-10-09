# Menzil · Gök — görsel promptları v2 (İskandinav, akşam güneşi)

**Nasıl:** Her promptu ChatGPT'ye olduğu gibi yapıştır. Aynı başlık altındakileri aynı sohbette sırayla iste. Dosyayı kod adıyla kaydet (`G4.png`, `C10.png`…) ve `Masaüstü/menzil-gorseller` klasörüne at. Hazır olanlar: G1, G2, G3 (zemin), T1/T3 (eski pedsiz tırlar — kullanılmayacak), T5 = C4b.

**Hata olursa aynı promptu tekrar iste:** yandan bakış, yazı/işaret, gölge yeşile taşmış, ped kenarı düz çizgi.

**Sonraki oturum için not (Claude'a):** Kararlar: İskandinav kıyısı coğrafyası; araç/tesis = kendi zemin pediyle tek kare, ped kenarı oyunda yumuşak maske + kenar renk eşleme ile araziye eritilir (`_ped.py`); zemin = G dokularının log-ağırlıklı yama serpiştirmesi + köşegen çevirme + düşük frekans ton (`_zemin.py`); güneş sağ alt ~20°, açı çatı baskın/yan yüz ince şerit; gerçek ölçek (1 araç ≈ 12 m), uzak zoomda askeri sembol, en yakın zoomda araç ~400 px. Menziller harita ölçeğine göre sıkıştırılacak (henüz karar yok). Scriptler `Masaüstü/menzil-gorseller/` içinde.


## Zemin dokuları (G) — G1, G2, G3 HAZIR, yeniden üretme

### G4 · Çam ormanı (tepeden)

```
Photograph taken EXACTLY straight down from high above, true nadir, zero perspective. The frame shows an area about 60 m wide. 
Subject: dense Scandinavian pine and spruce forest seen from above: individual dark-green round and star-shaped tree crowns packed closely, small gaps showing moss and granite, a few birch crowns lighter green. No roads, no buildings. 
Lighting: golden late-evening sun from the LOWER-RIGHT at about 20° elevation: warm amber light on surfaces facing the lower-right, short soft shadows toward the upper-left, shadows cool blue-grey. Natural cinematic grade, no HDR, no haze, no vignette. 
Composition: irregular and organic, no repeating pattern, no single dominant feature. Detail: uniform razor sharpness edge to edge, no blur, no noise. 
Seamless tileable texture: the left edge continues the right edge and the top edge continues the bottom edge with no visible seam. No text, no watermark. Square image, highest resolution.
```

### G5 · Deniz suyu

```
Photograph taken EXACTLY straight down from high above, true nadir, zero perspective. The frame shows an area about 120 m wide. 
Subject: open dark sea water of a Nordic sound: deep blue-green to slate water with gentle small ripples, warm orange sunset glints on the ripples, no shoreline, no boats, no foam lines. 
Lighting: golden late-evening sun from the LOWER-RIGHT at about 20° elevation: warm amber light on surfaces facing the lower-right, short soft shadows toward the upper-left, shadows cool blue-grey. Natural cinematic grade, no HDR, no haze, no vignette. 
Composition: irregular and organic, no repeating pattern, no single dominant feature. Detail: uniform razor sharpness edge to edge, no blur, no noise. 
Seamless tileable texture: the left edge continues the right edge and the top edge continues the bottom edge with no visible seam. No text, no watermark. Square image, highest resolution.
```

### G6 · Kayalık kıyı şeridi

```
Photograph taken EXACTLY straight down from high above, true nadir, zero perspective. The frame shows an area about 60 m wide. 
Subject: a horizontal strip of rocky Scandinavian shoreline running from the left edge to the right edge: smooth grey-pink granite slabs sloping into water along the BOTTOM third, dark wet rock band and a thin line of foam at the waterline, lichen and heather and small pines on the rock in the TOP third. Water at the bottom is dark blue-green. 
Lighting: golden late-evening sun from the LOWER-RIGHT at about 20° elevation: warm amber light on surfaces facing the lower-right, short soft shadows toward the upper-left, shadows cool blue-grey. Natural cinematic grade, no HDR, no haze, no vignette. 
Composition: irregular and organic, no repeating pattern, no single dominant feature. Detail: uniform razor sharpness edge to edge, no blur, no noise. 
Seamless horizontally: the left edge continues the right edge exactly. No text, no watermark. Landscape 3:2, highest resolution.
```

### G7 · Asfalt yol şeridi

```
Photograph taken EXACTLY straight down from high above, true nadir, zero perspective. The frame shows an area about 40 m wide. 
Subject: a two-lane asphalt road running perfectly horizontally across the full width, occupying the middle third of the height: dark grey asphalt with fine cracks, white dashed center line, white edge lines, narrow gravel shoulders, moss and heather and pine forest edge on both sides. No cars. 
Lighting: golden late-evening sun from the LOWER-RIGHT at about 20° elevation: warm amber light on surfaces facing the lower-right, short soft shadows toward the upper-left, shadows cool blue-grey. Natural cinematic grade, no HDR, no haze, no vignette. 
Composition: irregular and organic, no repeating pattern, no single dominant feature. Detail: uniform razor sharpness edge to edge, no blur, no noise. 
Seamless horizontally: the left edge continues the right edge exactly. No text, no watermark. Landscape 3:2, highest resolution.
```

### G8 · Toprak/çakıl yol şeridi

```
Photograph taken EXACTLY straight down from high above, true nadir, zero perspective. The frame shows an area about 40 m wide. 
Subject: a single-lane gravel forest road running horizontally across the full width in the middle third: grey-pink compacted gravel with two darker wheel ruts, grass strip in the middle, ditches with moss, pine forest edge on both sides. 
Lighting: golden late-evening sun from the LOWER-RIGHT at about 20° elevation: warm amber light on surfaces facing the lower-right, short soft shadows toward the upper-left, shadows cool blue-grey. Natural cinematic grade, no HDR, no haze, no vignette. 
Composition: irregular and organic, no repeating pattern, no single dominant feature. Detail: uniform razor sharpness edge to edge, no blur, no noise. 
Seamless horizontally: the left edge continues the right edge exactly. No text, no watermark. Landscape 3:2, highest resolution.
```

### G9 · Çayır / biçilmiş tarla

```
Photograph taken EXACTLY straight down from high above, true nadir, zero perspective. The frame shows an area about 80 m wide. 
Subject: a Scandinavian hay meadow after mowing: pale yellow-green stubble with faint mowing stripes running diagonally, a few round white-wrapped hay bales, scattered darker green patches, a few granite boulders. 
Lighting: golden late-evening sun from the LOWER-RIGHT at about 20° elevation: warm amber light on surfaces facing the lower-right, short soft shadows toward the upper-left, shadows cool blue-grey. Natural cinematic grade, no HDR, no haze, no vignette. 
Composition: irregular and organic, no repeating pattern, no single dominant feature. Detail: uniform razor sharpness edge to edge, no blur, no noise. 
Seamless tileable texture: the left edge continues the right edge and the top edge continues the bottom edge with no visible seam. No text, no watermark. Square image, highest resolution.
```


## Büyük harita (M)

### M0 · Harita — iki kıyı, aradaki deniz geçidi

```
Photorealistic satellite image looking EXACTLY straight down, true nadir, zero perspective, no horizon, no clouds. The image covers a fictional Scandinavian coastal region 360 km wide and 240 km tall. A wide sea sound, 15 to 30 km wide with many small rocky islands and skerries, runs diagonally from the TOP-LEFT corner to the BOTTOM-RIGHT corner and separates two landmasses: one in the lower-left, one in the upper-right. Both landmasses: dark pine and spruce forest as the dominant cover, hundreds of small dark lakes, grey-pink granite highlands, patches of yellow-green farmland in the valleys, thin roads, a few small towns as tiny light clusters along the coast and lakes. Lighting: golden late-evening sun from the LOWER-RIGHT, hills casting soft shadows toward the upper-left, warm light on slopes, water dark blue with warm glints. Uniform sharpness corner to corner, no haze, no vignette, no text, no labels, no borders, no watermark. Landscape 3:2, highest resolution.
```


## Şehirler (K) — her biri ayrı ped, oyunda araziye eritilecek

### K1 · Liman kasabası

```
Photorealistic aerial photograph looking almost straight down from high above, only very slightly from the south, orthographic with no perspective: roofs are fully visible, walls facing the bottom of the frame show only as thin strips. 
The frame shows an area about 1.5 km wide. 
Subject: a Scandinavian harbour town on a rocky shore: red and ochre wooden houses with dark roofs and white trim, a white church with a slender spire, a small marina with boats, a ferry pier, a few 4-storey apartment blocks, streets with parked cars, gardens with trees. The sea fills one side of the patch. 
Setting: Scandinavian landscape in late summer: grey-pink granite, dark pine and spruce forest, moss, lichen, heather. The town sits on its own patch of surrounding forest and rock. 
Lighting: golden late-evening sun from the LOWER-RIGHT at about 20° elevation: warm amber light on surfaces facing the lower-right, every object casts one clean shadow toward the upper-left about three times its height, shadows cool blue-grey. Natural cinematic grade, no HDR, no haze, no vignette. 
Framing: the site with its own surrounding ground fills about 88% of the frame. The ground patch has an irregular natural outline with no straight edges and contains all shadows. Everything outside the ground patch is flat pure chroma green #00FF00 with no gradient and no shadow on the green. 
Detail: every roof, vent, vehicle, pipe, tree crown and path razor sharp, uniform sharpness, no blur, no noise. No text, no signs, no logos, no watermark. Square image, highest resolution.
```

### K2 · Orman içi köy

```
Photorealistic aerial photograph looking almost straight down from high above, only very slightly from the south, orthographic with no perspective: roofs are fully visible, walls facing the bottom of the frame show only as thin strips. 
The frame shows an area about 1.5 km wide. 
Subject: a Scandinavian village in a forest clearing: scattered red wooden farmhouses with white trim, barns, a small church, gravel roads, gardens, a lake shore on one side, surrounding pine forest edge. 
Setting: Scandinavian landscape in late summer: grey-pink granite, dark pine and spruce forest, moss, lichen, heather. The town sits on its own patch of surrounding forest and rock. 
Lighting: golden late-evening sun from the LOWER-RIGHT at about 20° elevation: warm amber light on surfaces facing the lower-right, every object casts one clean shadow toward the upper-left about three times its height, shadows cool blue-grey. Natural cinematic grade, no HDR, no haze, no vignette. 
Framing: the site with its own surrounding ground fills about 88% of the frame. The ground patch has an irregular natural outline with no straight edges and contains all shadows. Everything outside the ground patch is flat pure chroma green #00FF00 with no gradient and no shadow on the green. 
Detail: every roof, vent, vehicle, pipe, tree crown and path razor sharp, uniform sharpness, no blur, no noise. No text, no signs, no logos, no watermark. Square image, highest resolution.
```

### K3 · Modern ilçe

```
Photorealistic aerial photograph looking almost straight down from high above, only very slightly from the south, orthographic with no perspective: roofs are fully visible, walls facing the bottom of the frame show only as thin strips. 
The frame shows an area about 1.5 km wide. 
Subject: a modern Scandinavian town district: 4- to 8-storey apartment blocks with flat roofs around green courtyards, a shopping center with a large flat roof and parking lot, a school with a sports field, roundabouts, birch trees along the streets. 
Setting: Scandinavian landscape in late summer: grey-pink granite, dark pine and spruce forest, moss, lichen, heather. The town sits on its own patch of surrounding forest and rock. 
Lighting: golden late-evening sun from the LOWER-RIGHT at about 20° elevation: warm amber light on surfaces facing the lower-right, every object casts one clean shadow toward the upper-left about three times its height, shadows cool blue-grey. Natural cinematic grade, no HDR, no haze, no vignette. 
Framing: the site with its own surrounding ground fills about 88% of the frame. The ground patch has an irregular natural outline with no straight edges and contains all shadows. Everything outside the ground patch is flat pure chroma green #00FF00 with no gradient and no shadow on the green. 
Detail: every roof, vent, vehicle, pipe, tree crown and path razor sharp, uniform sharpness, no blur, no noise. No text, no signs, no logos, no watermark. Square image, highest resolution.
```

### K4 · Sanayi banliyösü

```
Photorealistic aerial photograph looking almost straight down from high above, only very slightly from the south, orthographic with no perspective: roofs are fully visible, walls facing the bottom of the frame show only as thin strips. 
The frame shows an area about 1.5 km wide. 
Subject: a Scandinavian industrial suburb: large grey and white warehouse roofs, a timber yard with stacked logs, a small sawmill, truck parking lots, rail sidings, some red wooden houses at the edge, pine forest around. 
Setting: Scandinavian landscape in late summer: grey-pink granite, dark pine and spruce forest, moss, lichen, heather. The town sits on its own patch of surrounding forest and rock. 
Lighting: golden late-evening sun from the LOWER-RIGHT at about 20° elevation: warm amber light on surfaces facing the lower-right, every object casts one clean shadow toward the upper-left about three times its height, shadows cool blue-grey. Natural cinematic grade, no HDR, no haze, no vignette. 
Framing: the site with its own surrounding ground fills about 88% of the frame. The ground patch has an irregular natural outline with no straight edges and contains all shadows. Everything outside the ground patch is flat pure chroma green #00FF00 with no gradient and no shadow on the green. 
Detail: every roof, vent, vehicle, pipe, tree crown and path razor sharp, uniform sharpness, no blur, no noise. No text, no signs, no logos, no watermark. Square image, highest resolution.
```

### K5 · Eski şehir merkezi

```
Photorealistic aerial photograph looking almost straight down from high above, only very slightly from the south, orthographic with no perspective: roofs are fully visible, walls facing the bottom of the frame show only as thin strips. 
The frame shows an area about 1.5 km wide. 
Subject: the old center of a Scandinavian town: a dense grid of colorful 3-storey buildings with steep dark roofs, a cobbled market square, a stone cathedral, a river with two bridges, trees along the riverbank. 
Setting: Scandinavian landscape in late summer: grey-pink granite, dark pine and spruce forest, moss, lichen, heather. The town sits on its own patch of surrounding forest and rock. 
Lighting: golden late-evening sun from the LOWER-RIGHT at about 20° elevation: warm amber light on surfaces facing the lower-right, every object casts one clean shadow toward the upper-left about three times its height, shadows cool blue-grey. Natural cinematic grade, no HDR, no haze, no vignette. 
Framing: the site with its own surrounding ground fills about 88% of the frame. The ground patch has an irregular natural outline with no straight edges and contains all shadows. Everything outside the ground patch is flat pure chroma green #00FF00 with no gradient and no shadow on the green. 
Detail: every roof, vent, vehicle, pipe, tree crown and path razor sharp, uniform sharpness, no blur, no noise. No text, no signs, no logos, no watermark. Square image, highest resolution.
```


## Tesisler (B)

### B1 · Komuta merkezi

```
Photorealistic aerial photograph looking almost straight down from high above, only very slightly from the south, orthographic with no perspective: roofs are fully visible, walls facing the bottom of the frame show only as thin strips. 
The frame shows an area about 300 m wide. 
Subject: a fortified military command headquarters: two flat-roofed concrete buildings with rooftop units and satellite dishes, a lattice communications mast, a painted helipad, parked military trucks in Nordic camouflage, earth berms and HESCO barriers, a perimeter fence, gravel yard, cut into the pine forest. 
Setting: Scandinavian landscape in late summer: grey-pink granite, dark pine and spruce forest, moss, lichen, heather.  
Lighting: golden late-evening sun from the LOWER-RIGHT at about 20° elevation: warm amber light on surfaces facing the lower-right, every object casts one clean shadow toward the upper-left about three times its height, shadows cool blue-grey. Natural cinematic grade, no HDR, no haze, no vignette. 
Framing: the site with its own surrounding ground fills about 88% of the frame. The ground patch has an irregular natural outline with no straight edges and contains all shadows. Everything outside the ground patch is flat pure chroma green #00FF00 with no gradient and no shadow on the green. 
Detail: every roof, vent, vehicle, pipe, tree crown and path razor sharp, uniform sharpness, no blur, no noise. No text, no signs, no logos, no watermark. Square image, highest resolution.
```

### B2 · Rafineri

```
Photorealistic aerial photograph looking almost straight down from high above, only very slightly from the south, orthographic with no perspective: roofs are fully visible, walls facing the bottom of the frame show only as thin strips. 
The frame shows an area about 1 km wide. 
Subject: a coastal oil refinery: large white cylindrical storage tanks seen as circles, smaller spherical tanks, distillation columns, dense silver pipe racks, a flare stack with a small flame, asphalt service roads, a jetty with a tanker berth at one edge. 
Setting: Scandinavian landscape in late summer: grey-pink granite, dark pine and spruce forest, moss, lichen, heather.  
Lighting: golden late-evening sun from the LOWER-RIGHT at about 20° elevation: warm amber light on surfaces facing the lower-right, every object casts one clean shadow toward the upper-left about three times its height, shadows cool blue-grey. Natural cinematic grade, no HDR, no haze, no vignette. 
Framing: the site with its own surrounding ground fills about 88% of the frame. The ground patch has an irregular natural outline with no straight edges and contains all shadows. Everything outside the ground patch is flat pure chroma green #00FF00 with no gradient and no shadow on the green. 
Detail: every roof, vent, vehicle, pipe, tree crown and path razor sharp, uniform sharpness, no blur, no noise. No text, no signs, no logos, no watermark. Square image, highest resolution.
```

### B3 · Enerji santrali

```
Photorealistic aerial photograph looking almost straight down from high above, only very slightly from the south, orthographic with no perspective: roofs are fully visible, walls facing the bottom of the frame show only as thin strips. 
The frame shows an area about 700 m wide. 
Subject: a thermal power station: a large turbine hall with a long grey roof, two tall chimneys seen from above as circles casting long shadows, a coal or biomass yard, a switchyard with transformers and high-voltage lines leaving the site, cooling water outlet to a river. 
Setting: Scandinavian landscape in late summer: grey-pink granite, dark pine and spruce forest, moss, lichen, heather.  
Lighting: golden late-evening sun from the LOWER-RIGHT at about 20° elevation: warm amber light on surfaces facing the lower-right, every object casts one clean shadow toward the upper-left about three times its height, shadows cool blue-grey. Natural cinematic grade, no HDR, no haze, no vignette. 
Framing: the site with its own surrounding ground fills about 88% of the frame. The ground patch has an irregular natural outline with no straight edges and contains all shadows. Everything outside the ground patch is flat pure chroma green #00FF00 with no gradient and no shadow on the green. 
Detail: every roof, vent, vehicle, pipe, tree crown and path razor sharp, uniform sharpness, no blur, no noise. No text, no signs, no logos, no watermark. Square image, highest resolution.
```

### B4 · Hava üssü

```
Photorealistic aerial photograph looking almost straight down from high above, only very slightly from the south, orthographic with no perspective: roofs are fully visible, walls facing the bottom of the frame show only as thin strips. 
The frame shows an area about 2 km wide. 
Subject: a military air base cut into pine forest: a runway segment crossing the frame, a parallel taxiway, hardened aircraft shelters with curved concrete roofs, a control tower, fuel tanks, apron with two grey fighter jets. 
Setting: Scandinavian landscape in late summer: grey-pink granite, dark pine and spruce forest, moss, lichen, heather.  
Lighting: golden late-evening sun from the LOWER-RIGHT at about 20° elevation: warm amber light on surfaces facing the lower-right, every object casts one clean shadow toward the upper-left about three times its height, shadows cool blue-grey. Natural cinematic grade, no HDR, no haze, no vignette. 
Framing: the site with its own surrounding ground fills about 88% of the frame. The ground patch has an irregular natural outline with no straight edges and contains all shadows. Everything outside the ground patch is flat pure chroma green #00FF00 with no gradient and no shadow on the green. 
Detail: every roof, vent, vehicle, pipe, tree crown and path razor sharp, uniform sharpness, no blur, no noise. No text, no signs, no logos, no watermark. Square image, highest resolution.
```

### B5 · Fabrika

```
Photorealistic aerial photograph looking almost straight down from high above, only very slightly from the south, orthographic with no perspective: roofs are fully visible, walls facing the bottom of the frame show only as thin strips. 
The frame shows an area about 500 m wide. 
Subject: a large factory complex: long sawtooth-roofed production halls, a smaller office block, loading docks with trucks, a parking lot, a rail siding, stacked containers. 
Setting: Scandinavian landscape in late summer: grey-pink granite, dark pine and spruce forest, moss, lichen, heather.  
Lighting: golden late-evening sun from the LOWER-RIGHT at about 20° elevation: warm amber light on surfaces facing the lower-right, every object casts one clean shadow toward the upper-left about three times its height, shadows cool blue-grey. Natural cinematic grade, no HDR, no haze, no vignette. 
Framing: the site with its own surrounding ground fills about 88% of the frame. The ground patch has an irregular natural outline with no straight edges and contains all shadows. Everything outside the ground patch is flat pure chroma green #00FF00 with no gradient and no shadow on the green. 
Detail: every roof, vent, vehicle, pipe, tree crown and path razor sharp, uniform sharpness, no blur, no noise. No text, no signs, no logos, no watermark. Square image, highest resolution.
```

### B6 · Cephanelik

```
Photorealistic aerial photograph looking almost straight down from high above, only very slightly from the south, orthographic with no perspective: roofs are fully visible, walls facing the bottom of the frame show only as thin strips. 
The frame shows an area about 500 m wide. 
Subject: a military ammunition depot in forest: rows of earth-covered igloo bunkers with concrete fronts, gravel roads between them, a guard post, double fence, cleared strip around. 
Setting: Scandinavian landscape in late summer: grey-pink granite, dark pine and spruce forest, moss, lichen, heather.  
Lighting: golden late-evening sun from the LOWER-RIGHT at about 20° elevation: warm amber light on surfaces facing the lower-right, every object casts one clean shadow toward the upper-left about three times its height, shadows cool blue-grey. Natural cinematic grade, no HDR, no haze, no vignette. 
Framing: the site with its own surrounding ground fills about 88% of the frame. The ground patch has an irregular natural outline with no straight edges and contains all shadows. Everything outside the ground patch is flat pure chroma green #00FF00 with no gradient and no shadow on the green. 
Detail: every roof, vent, vehicle, pipe, tree crown and path razor sharp, uniform sharpness, no blur, no noise. No text, no signs, no logos, no watermark. Square image, highest resolution.
```

### B7 · Yakıt deposu

```
Photorealistic aerial photograph looking almost straight down from high above, only very slightly from the south, orthographic with no perspective: roofs are fully visible, walls facing the bottom of the frame show only as thin strips. 
The frame shows an area about 400 m wide. 
Subject: a fuel depot: six large white storage tanks within earth bund walls, pipe manifolds, tanker truck loading bays, a small pump house, fence. 
Setting: Scandinavian landscape in late summer: grey-pink granite, dark pine and spruce forest, moss, lichen, heather.  
Lighting: golden late-evening sun from the LOWER-RIGHT at about 20° elevation: warm amber light on surfaces facing the lower-right, every object casts one clean shadow toward the upper-left about three times its height, shadows cool blue-grey. Natural cinematic grade, no HDR, no haze, no vignette. 
Framing: the site with its own surrounding ground fills about 88% of the frame. The ground patch has an irregular natural outline with no straight edges and contains all shadows. Everything outside the ground patch is flat pure chroma green #00FF00 with no gradient and no shadow on the green. 
Detail: every roof, vent, vehicle, pipe, tree crown and path razor sharp, uniform sharpness, no blur, no noise. No text, no signs, no logos, no watermark. Square image, highest resolution.
```

### B8 · Haberleşme merkezi

```
Photorealistic aerial photograph looking almost straight down from high above, only very slightly from the south, orthographic with no perspective: roofs are fully visible, walls facing the bottom of the frame show only as thin strips. 
The frame shows an area about 250 m wide. 
Subject: a military communications station on a granite hilltop: a tall lattice tower, three large satellite dishes, a radome, a small concrete building, generator, fence, gravel access road. 
Setting: Scandinavian landscape in late summer: grey-pink granite, dark pine and spruce forest, moss, lichen, heather.  
Lighting: golden late-evening sun from the LOWER-RIGHT at about 20° elevation: warm amber light on surfaces facing the lower-right, every object casts one clean shadow toward the upper-left about three times its height, shadows cool blue-grey. Natural cinematic grade, no HDR, no haze, no vignette. 
Framing: the site with its own surrounding ground fills about 88% of the frame. The ground patch has an irregular natural outline with no straight edges and contains all shadows. Everything outside the ground patch is flat pure chroma green #00FF00 with no gradient and no shadow on the green. 
Detail: every roof, vent, vehicle, pipe, tree crown and path razor sharp, uniform sharpness, no blur, no noise. No text, no signs, no logos, no watermark. Square image, highest resolution.
```

### B9 · Kışla

```
Photorealistic aerial photograph looking almost straight down from high above, only very slightly from the south, orthographic with no perspective: roofs are fully visible, walls facing the bottom of the frame show only as thin strips. 
The frame shows an area about 500 m wide. 
Subject: a military barracks: several long two-storey accommodation blocks with dark roofs, a parade ground, a motor pool with camouflaged trucks, a mess hall, sports field, fence, pine forest around. 
Setting: Scandinavian landscape in late summer: grey-pink granite, dark pine and spruce forest, moss, lichen, heather.  
Lighting: golden late-evening sun from the LOWER-RIGHT at about 20° elevation: warm amber light on surfaces facing the lower-right, every object casts one clean shadow toward the upper-left about three times its height, shadows cool blue-grey. Natural cinematic grade, no HDR, no haze, no vignette. 
Framing: the site with its own surrounding ground fills about 88% of the frame. The ground patch has an irregular natural outline with no straight edges and contains all shadows. Everything outside the ground patch is flat pure chroma green #00FF00 with no gradient and no shadow on the green. 
Detail: every roof, vent, vehicle, pipe, tree crown and path razor sharp, uniform sharpness, no blur, no noise. No text, no signs, no logos, no watermark. Square image, highest resolution.
```


## Hava savunma, radar, rampalar (C) — HEPSİ AYNI SOHBETTE, SIRAYLA. İlk görselden sonra her birine şu cümleyi ekle: "Match the previous image exactly in camera angle, scale, lighting and color grade."

### C4b · Orta menzil HS — radar tırı

HAZIR (T5). Yeniden üretme; bu sohbeti onunla başlatırsan referans olur.

### C1 · Arama radarı

```
Photorealistic aerial photograph looking down at a single military vehicle on the ground, from high above and only slightly to the south, orthographic with no perspective. The view must look like this: the roof of the vehicle is fully visible and is by far the largest surface; the side facing the bottom of the frame shows only as a thin strip, about one third as tall as the roof is wide; wheels or tracks on that side appear as very flat shapes, wheels as ellipses about three times wider than tall. 
Subject: a single 8x8 military truck carrying a large long-range search radar: a big rectangular phased-array antenna raised and tilted up on a hydraulic arm, its face showing a grid of tiles, cooling units, a generator trailer hitched behind, cables on the ground. Matte Nordic camouflage of dark green, grey-green and black patches, light dust on the lower body, small amber beacon lamp on the cab roof. Cab or front pointing to the RIGHT of the frame. 
Ground: it stands on a levelled gravel clearing in a Scandinavian pine forest in late summer: grey-pink crushed granite gravel, compacted tire tracks, patches of moss and pale lichen and low heather at the edges, a few small flat granite slabs. Wheels press slightly into the gravel, with dark contact shadows under the tires and the chassis. 
Lighting: golden late-evening sun from the LOWER-RIGHT at about 20° elevation: warm amber light on surfaces facing the lower-right, every object casts one clean shadow toward the upper-left about three times its height, shadows cool blue-grey. Natural cinematic grade, no HDR, no haze, no vignette. 
Framing: the subject fills about 50% of the frame width, centered slightly to the right so its shadow has room. The ground patch has an irregular natural outline with no straight edges, fills about 90% of the frame, and contains the entire shadow. Everything outside the ground patch is flat pure chroma green #00FF00 with no gradient and no shadow on the green. 
Detail: every bolt, hatch, grille, cable, tire tread and pebble razor sharp, no blur, no noise. No text, no markings, no insignia, no watermark. Landscape 3:2, highest resolution.
```

### C2 · Yakın savunma topu

```
Photorealistic aerial photograph looking down at a single military vehicle on the ground, from high above and only slightly to the south, orthographic with no perspective. The view must look like this: the roof of the vehicle is fully visible and is by far the largest surface; the side facing the bottom of the frame shows only as a thin strip, about one third as tall as the roof is wide; wheels or tracks on that side appear as very flat shapes, wheels as ellipses about three times wider than tall. 
Subject: a single 8x8 military truck carrying a close-in weapon system turret: a rotary multi-barrel gun with a long barrel cluster, a white search radar dome on top of the turret, ammunition boxes, outriggers lowered onto pads. Matte Nordic camouflage of dark green, grey-green and black patches, light dust on the lower body, small amber beacon lamp on the cab roof. Cab or front pointing to the RIGHT of the frame. 
Ground: it stands on a levelled gravel clearing in a Scandinavian pine forest in late summer: grey-pink crushed granite gravel, compacted tire tracks, patches of moss and pale lichen and low heather at the edges, a few small flat granite slabs. Wheels press slightly into the gravel, with dark contact shadows under the tires and the chassis. 
Lighting: golden late-evening sun from the LOWER-RIGHT at about 20° elevation: warm amber light on surfaces facing the lower-right, every object casts one clean shadow toward the upper-left about three times its height, shadows cool blue-grey. Natural cinematic grade, no HDR, no haze, no vignette. 
Framing: the subject fills about 42% of the frame width, centered slightly to the right so its shadow has room. The ground patch has an irregular natural outline with no straight edges, fills about 90% of the frame, and contains the entire shadow. Everything outside the ground patch is flat pure chroma green #00FF00 with no gradient and no shadow on the green. 
Detail: every bolt, hatch, grille, cable, tire tread and pebble razor sharp, no blur, no noise. No text, no markings, no insignia, no watermark. Landscape 3:2, highest resolution.
```

### C3 · Kısa menzil HS

```
Photorealistic aerial photograph looking down at a single military vehicle on the ground, from high above and only slightly to the south, orthographic with no perspective. The view must look like this: the roof of the vehicle is fully visible and is by far the largest surface; the side facing the bottom of the frame shows only as a thin strip, about one third as tall as the roof is wide; wheels or tracks on that side appear as very flat shapes, wheels as ellipses about three times wider than tall. 
Subject: a single tracked air defense vehicle: a turret with two box launchers of four short-range missiles each, an electro-optical sensor ball, a small rotating radar on the turret roof, tracks pressing into the gravel. Matte Nordic camouflage of dark green, grey-green and black patches, light dust on the lower body, small amber beacon lamp on the cab roof. Cab or front pointing to the RIGHT of the frame. 
Ground: it stands on a levelled gravel clearing in a Scandinavian pine forest in late summer: grey-pink crushed granite gravel, compacted tire tracks, patches of moss and pale lichen and low heather at the edges, a few small flat granite slabs. Wheels press slightly into the gravel, with dark contact shadows under the tires and the chassis. 
Lighting: golden late-evening sun from the LOWER-RIGHT at about 20° elevation: warm amber light on surfaces facing the lower-right, every object casts one clean shadow toward the upper-left about three times its height, shadows cool blue-grey. Natural cinematic grade, no HDR, no haze, no vignette. 
Framing: the subject fills about 40% of the frame width, centered slightly to the right so its shadow has room. The ground patch has an irregular natural outline with no straight edges, fills about 90% of the frame, and contains the entire shadow. Everything outside the ground patch is flat pure chroma green #00FF00 with no gradient and no shadow on the green. 
Detail: every bolt, hatch, grille, cable, tire tread and pebble razor sharp, no blur, no noise. No text, no markings, no insignia, no watermark. Landscape 3:2, highest resolution.
```

### C4a · Orta menzil HS — fırlatıcı

```
Photorealistic aerial photograph looking down at a single military vehicle on the ground, from high above and only slightly to the south, orthographic with no perspective. The view must look like this: the roof of the vehicle is fully visible and is by far the largest surface; the side facing the bottom of the frame shows only as a thin strip, about one third as tall as the roof is wide; wheels or tracks on that side appear as very flat shapes, wheels as ellipses about three times wider than tall. 
Subject: a single 8x8 military launcher truck with a vertical launch pod of eight square missile cells, hatch lids closed, outriggers lowered. Matte Nordic camouflage of dark green, grey-green and black patches, light dust on the lower body, small amber beacon lamp on the cab roof. Cab or front pointing to the RIGHT of the frame. 
Ground: it stands on a levelled gravel clearing in a Scandinavian pine forest in late summer: grey-pink crushed granite gravel, compacted tire tracks, patches of moss and pale lichen and low heather at the edges, a few small flat granite slabs. Wheels press slightly into the gravel, with dark contact shadows under the tires and the chassis. 
Lighting: golden late-evening sun from the LOWER-RIGHT at about 20° elevation: warm amber light on surfaces facing the lower-right, every object casts one clean shadow toward the upper-left about three times its height, shadows cool blue-grey. Natural cinematic grade, no HDR, no haze, no vignette. 
Framing: the subject fills about 50% of the frame width, centered slightly to the right so its shadow has room. The ground patch has an irregular natural outline with no straight edges, fills about 90% of the frame, and contains the entire shadow. Everything outside the ground patch is flat pure chroma green #00FF00 with no gradient and no shadow on the green. 
Detail: every bolt, hatch, grille, cable, tire tread and pebble razor sharp, no blur, no noise. No text, no markings, no insignia, no watermark. Landscape 3:2, highest resolution.
```

### C4c · Orta menzil HS — komuta tırı

```
Photorealistic aerial photograph looking down at a single military vehicle on the ground, from high above and only slightly to the south, orthographic with no perspective. The view must look like this: the roof of the vehicle is fully visible and is by far the largest surface; the side facing the bottom of the frame shows only as a thin strip, about one third as tall as the roof is wide; wheels or tracks on that side appear as very flat shapes, wheels as ellipses about three times wider than tall. 
Subject: a single 6x6 military truck carrying a command shelter: a box body with air-conditioning units, a telescopic antenna mast, a small satellite dish, cable reels, a generator box beside it. Matte Nordic camouflage of dark green, grey-green and black patches, light dust on the lower body, small amber beacon lamp on the cab roof. Cab or front pointing to the RIGHT of the frame. 
Ground: it stands on a levelled gravel clearing in a Scandinavian pine forest in late summer: grey-pink crushed granite gravel, compacted tire tracks, patches of moss and pale lichen and low heather at the edges, a few small flat granite slabs. Wheels press slightly into the gravel, with dark contact shadows under the tires and the chassis. 
Lighting: golden late-evening sun from the LOWER-RIGHT at about 20° elevation: warm amber light on surfaces facing the lower-right, every object casts one clean shadow toward the upper-left about three times its height, shadows cool blue-grey. Natural cinematic grade, no HDR, no haze, no vignette. 
Framing: the subject fills about 46% of the frame width, centered slightly to the right so its shadow has room. The ground patch has an irregular natural outline with no straight edges, fills about 90% of the frame, and contains the entire shadow. Everything outside the ground patch is flat pure chroma green #00FF00 with no gradient and no shadow on the green. 
Detail: every bolt, hatch, grille, cable, tire tread and pebble razor sharp, no blur, no noise. No text, no markings, no insignia, no watermark. Landscape 3:2, highest resolution.
```

### C5a · Uzun menzil HS — fırlatıcı

```
Photorealistic aerial photograph looking down at a single military vehicle on the ground, from high above and only slightly to the south, orthographic with no perspective. The view must look like this: the roof of the vehicle is fully visible and is by far the largest surface; the side facing the bottom of the frame shows only as a thin strip, about one third as tall as the roof is wide; wheels or tracks on that side appear as very flat shapes, wheels as ellipses about three times wider than tall. 
Subject: a single semitrailer missile launcher towed by a 6x6 tractor truck: four large missile canisters on an erector raised at a steep angle pointing toward the upper-left, outriggers down. Matte Nordic camouflage of dark green, grey-green and black patches, light dust on the lower body, small amber beacon lamp on the cab roof. Cab or front pointing to the RIGHT of the frame. 
Ground: it stands on a levelled gravel clearing in a Scandinavian pine forest in late summer: grey-pink crushed granite gravel, compacted tire tracks, patches of moss and pale lichen and low heather at the edges, a few small flat granite slabs. Wheels press slightly into the gravel, with dark contact shadows under the tires and the chassis. 
Lighting: golden late-evening sun from the LOWER-RIGHT at about 20° elevation: warm amber light on surfaces facing the lower-right, every object casts one clean shadow toward the upper-left about three times its height, shadows cool blue-grey. Natural cinematic grade, no HDR, no haze, no vignette. 
Framing: the subject fills about 55% of the frame width, centered slightly to the right so its shadow has room. The ground patch has an irregular natural outline with no straight edges, fills about 90% of the frame, and contains the entire shadow. Everything outside the ground patch is flat pure chroma green #00FF00 with no gradient and no shadow on the green. 
Detail: every bolt, hatch, grille, cable, tire tread and pebble razor sharp, no blur, no noise. No text, no markings, no insignia, no watermark. Landscape 3:2, highest resolution.
```

### C5b · Uzun menzil HS — radar

```
Photorealistic aerial photograph looking down at a single military vehicle on the ground, from high above and only slightly to the south, orthographic with no perspective. The view must look like this: the roof of the vehicle is fully visible and is by far the largest surface; the side facing the bottom of the frame shows only as a thin strip, about one third as tall as the roof is wide; wheels or tracks on that side appear as very flat shapes, wheels as ellipses about three times wider than tall. 
Subject: a single semitrailer carrying a large phased-array fire-control radar: a big flat antenna face raised almost vertical, facing the lower-right, towed by a 6x6 tractor truck, generator truck parked beside it. Matte Nordic camouflage of dark green, grey-green and black patches, light dust on the lower body, small amber beacon lamp on the cab roof. Cab or front pointing to the RIGHT of the frame. 
Ground: it stands on a levelled gravel clearing in a Scandinavian pine forest in late summer: grey-pink crushed granite gravel, compacted tire tracks, patches of moss and pale lichen and low heather at the edges, a few small flat granite slabs. Wheels press slightly into the gravel, with dark contact shadows under the tires and the chassis. 
Lighting: golden late-evening sun from the LOWER-RIGHT at about 20° elevation: warm amber light on surfaces facing the lower-right, every object casts one clean shadow toward the upper-left about three times its height, shadows cool blue-grey. Natural cinematic grade, no HDR, no haze, no vignette. 
Framing: the subject fills about 55% of the frame width, centered slightly to the right so its shadow has room. The ground patch has an irregular natural outline with no straight edges, fills about 90% of the frame, and contains the entire shadow. Everything outside the ground patch is flat pure chroma green #00FF00 with no gradient and no shadow on the green. 
Detail: every bolt, hatch, grille, cable, tire tread and pebble razor sharp, no blur, no noise. No text, no markings, no insignia, no watermark. Landscape 3:2, highest resolution.
```

### C6a · Üst katman HS — fırlatıcı

```
Photorealistic aerial photograph looking down at a single military vehicle on the ground, from high above and only slightly to the south, orthographic with no perspective. The view must look like this: the roof of the vehicle is fully visible and is by far the largest surface; the side facing the bottom of the frame shows only as a thin strip, about one third as tall as the roof is wide; wheels or tracks on that side appear as very flat shapes, wheels as ellipses about three times wider than tall. 
Subject: a single 10x10 missile launcher truck with eight long cylindrical interceptor canisters on an erector raised at a moderate angle, outriggers down. Matte Nordic camouflage of dark green, grey-green and black patches, light dust on the lower body, small amber beacon lamp on the cab roof. Cab or front pointing to the RIGHT of the frame. 
Ground: it stands on a levelled gravel clearing in a Scandinavian pine forest in late summer: grey-pink crushed granite gravel, compacted tire tracks, patches of moss and pale lichen and low heather at the edges, a few small flat granite slabs. Wheels press slightly into the gravel, with dark contact shadows under the tires and the chassis. 
Lighting: golden late-evening sun from the LOWER-RIGHT at about 20° elevation: warm amber light on surfaces facing the lower-right, every object casts one clean shadow toward the upper-left about three times its height, shadows cool blue-grey. Natural cinematic grade, no HDR, no haze, no vignette. 
Framing: the subject fills about 55% of the frame width, centered slightly to the right so its shadow has room. The ground patch has an irregular natural outline with no straight edges, fills about 90% of the frame, and contains the entire shadow. Everything outside the ground patch is flat pure chroma green #00FF00 with no gradient and no shadow on the green. 
Detail: every bolt, hatch, grille, cable, tire tread and pebble razor sharp, no blur, no noise. No text, no markings, no insignia, no watermark. Landscape 3:2, highest resolution.
```

### C6b · Üst katman HS — radar

```
Photorealistic aerial photograph looking down at a single military vehicle on the ground, from high above and only slightly to the south, orthographic with no perspective. The view must look like this: the roof of the vehicle is fully visible and is by far the largest surface; the side facing the bottom of the frame shows only as a thin strip, about one third as tall as the roof is wide; wheels or tracks on that side appear as very flat shapes, wheels as ellipses about three times wider than tall. 
Subject: a single very large X-band radar array on a trailer: a long flat antenna face, separate cooling and power units next to it, all connected by thick cables. Matte Nordic camouflage of dark green, grey-green and black patches, light dust on the lower body, small amber beacon lamp on the cab roof. Cab or front pointing to the RIGHT of the frame. 
Ground: it stands on a levelled gravel clearing in a Scandinavian pine forest in late summer: grey-pink crushed granite gravel, compacted tire tracks, patches of moss and pale lichen and low heather at the edges, a few small flat granite slabs. Wheels press slightly into the gravel, with dark contact shadows under the tires and the chassis. 
Lighting: golden late-evening sun from the LOWER-RIGHT at about 20° elevation: warm amber light on surfaces facing the lower-right, every object casts one clean shadow toward the upper-left about three times its height, shadows cool blue-grey. Natural cinematic grade, no HDR, no haze, no vignette. 
Framing: the subject fills about 58% of the frame width, centered slightly to the right so its shadow has room. The ground patch has an irregular natural outline with no straight edges, fills about 90% of the frame, and contains the entire shadow. Everything outside the ground patch is flat pure chroma green #00FF00 with no gradient and no shadow on the green. 
Detail: every bolt, hatch, grille, cable, tire tread and pebble razor sharp, no blur, no noise. No text, no markings, no insignia, no watermark. Landscape 3:2, highest resolution.
```

### C7 · Lazer HS

```
Photorealistic aerial photograph looking down at a single military vehicle on the ground, from high above and only slightly to the south, orthographic with no perspective. The view must look like this: the roof of the vehicle is fully visible and is by far the largest surface; the side facing the bottom of the frame shows only as a thin strip, about one third as tall as the roof is wide; wheels or tracks on that side appear as very flat shapes, wheels as ellipses about three times wider than tall. 
Subject: a single 8x8 armored vehicle carrying a high-energy laser turret: a large cylindrical beam director with a round glass optical aperture, cooling radiators, a power module box, a small radar on a short mast. Matte Nordic camouflage of dark green, grey-green and black patches, light dust on the lower body, small amber beacon lamp on the cab roof. Cab or front pointing to the RIGHT of the frame. 
Ground: it stands on a levelled gravel clearing in a Scandinavian pine forest in late summer: grey-pink crushed granite gravel, compacted tire tracks, patches of moss and pale lichen and low heather at the edges, a few small flat granite slabs. Wheels press slightly into the gravel, with dark contact shadows under the tires and the chassis. 
Lighting: golden late-evening sun from the LOWER-RIGHT at about 20° elevation: warm amber light on surfaces facing the lower-right, every object casts one clean shadow toward the upper-left about three times its height, shadows cool blue-grey. Natural cinematic grade, no HDR, no haze, no vignette. 
Framing: the subject fills about 42% of the frame width, centered slightly to the right so its shadow has room. The ground patch has an irregular natural outline with no straight edges, fills about 90% of the frame, and contains the entire shadow. Everything outside the ground patch is flat pure chroma green #00FF00 with no gradient and no shadow on the green. 
Detail: every bolt, hatch, grille, cable, tire tread and pebble razor sharp, no blur, no noise. No text, no markings, no insignia, no watermark. Landscape 3:2, highest resolution.
```

### C8 · Önleyici İHA rampası

```
Photorealistic aerial photograph looking down at a single military vehicle on the ground, from high above and only slightly to the south, orthographic with no perspective. The view must look like this: the roof of the vehicle is fully visible and is by far the largest surface; the side facing the bottom of the frame shows only as a thin strip, about one third as tall as the roof is wide; wheels or tracks on that side appear as very flat shapes, wheels as ellipses about three times wider than tall. 
Subject: a single 6x6 military truck carrying an angled launch rack of twelve tube launchers for small interceptor drones, a sensor mast, control cabin. Matte Nordic camouflage of dark green, grey-green and black patches, light dust on the lower body, small amber beacon lamp on the cab roof. Cab or front pointing to the RIGHT of the frame. 
Ground: it stands on a levelled gravel clearing in a Scandinavian pine forest in late summer: grey-pink crushed granite gravel, compacted tire tracks, patches of moss and pale lichen and low heather at the edges, a few small flat granite slabs. Wheels press slightly into the gravel, with dark contact shadows under the tires and the chassis. 
Lighting: golden late-evening sun from the LOWER-RIGHT at about 20° elevation: warm amber light on surfaces facing the lower-right, every object casts one clean shadow toward the upper-left about three times its height, shadows cool blue-grey. Natural cinematic grade, no HDR, no haze, no vignette. 
Framing: the subject fills about 46% of the frame width, centered slightly to the right so its shadow has room. The ground patch has an irregular natural outline with no straight edges, fills about 90% of the frame, and contains the entire shadow. Everything outside the ground patch is flat pure chroma green #00FF00 with no gradient and no shadow on the green. 
Detail: every bolt, hatch, grille, cable, tire tread and pebble razor sharp, no blur, no noise. No text, no markings, no insignia, no watermark. Landscape 3:2, highest resolution.
```

### C9 · Elektronik harp

```
Photorealistic aerial photograph looking down at a single military vehicle on the ground, from high above and only slightly to the south, orthographic with no perspective. The view must look like this: the roof of the vehicle is fully visible and is by far the largest surface; the side facing the bottom of the frame shows only as a thin strip, about one third as tall as the roof is wide; wheels or tracks on that side appear as very flat shapes, wheels as ellipses about three times wider than tall. 
Subject: a single 8x8 military truck carrying an electronic warfare system: a large rotating antenna array shaped like an inverted dish on a raised mast, several smaller antenna arrays, generator trailer, cables on the ground. Matte Nordic camouflage of dark green, grey-green and black patches, light dust on the lower body, small amber beacon lamp on the cab roof. Cab or front pointing to the RIGHT of the frame. 
Ground: it stands on a levelled gravel clearing in a Scandinavian pine forest in late summer: grey-pink crushed granite gravel, compacted tire tracks, patches of moss and pale lichen and low heather at the edges, a few small flat granite slabs. Wheels press slightly into the gravel, with dark contact shadows under the tires and the chassis. 
Lighting: golden late-evening sun from the LOWER-RIGHT at about 20° elevation: warm amber light on surfaces facing the lower-right, every object casts one clean shadow toward the upper-left about three times its height, shadows cool blue-grey. Natural cinematic grade, no HDR, no haze, no vignette. 
Framing: the subject fills about 50% of the frame width, centered slightly to the right so its shadow has room. The ground patch has an irregular natural outline with no straight edges, fills about 90% of the frame, and contains the entire shadow. Everything outside the ground patch is flat pure chroma green #00FF00 with no gradient and no shadow on the green. 
Detail: every bolt, hatch, grille, cable, tire tread and pebble razor sharp, no blur, no noise. No text, no markings, no insignia, no watermark. Landscape 3:2, highest resolution.
```

### C10 · Füze rampası (balistik)

```
Photorealistic aerial photograph looking down at a single military vehicle on the ground, from high above and only slightly to the south, orthographic with no perspective. The view must look like this: the roof of the vehicle is fully visible and is by far the largest surface; the side facing the bottom of the frame shows only as a thin strip, about one third as tall as the roof is wide; wheels or tracks on that side appear as very flat shapes, wheels as ellipses about three times wider than tall. 
Subject: a single 8x8 transporter-erector-launcher truck with one large ballistic missile on its erector raised almost vertical, the missile's grey nose pointing upward toward the upper-left, outriggers down on pads, exhaust deflector plate on the ground. Matte Nordic camouflage of dark green, grey-green and black patches, light dust on the lower body, small amber beacon lamp on the cab roof. Cab or front pointing to the RIGHT of the frame. 
Ground: it stands on a levelled gravel clearing in a Scandinavian pine forest in late summer: grey-pink crushed granite gravel, compacted tire tracks, patches of moss and pale lichen and low heather at the edges, a few small flat granite slabs. Wheels press slightly into the gravel, with dark contact shadows under the tires and the chassis. 
Lighting: golden late-evening sun from the LOWER-RIGHT at about 20° elevation: warm amber light on surfaces facing the lower-right, every object casts one clean shadow toward the upper-left about three times its height, shadows cool blue-grey. Natural cinematic grade, no HDR, no haze, no vignette. 
Framing: the subject fills about 55% of the frame width, centered slightly to the right so its shadow has room. The ground patch has an irregular natural outline with no straight edges, fills about 90% of the frame, and contains the entire shadow. Everything outside the ground patch is flat pure chroma green #00FF00 with no gradient and no shadow on the green. 
Detail: every bolt, hatch, grille, cable, tire tread and pebble razor sharp, no blur, no noise. No text, no markings, no insignia, no watermark. Landscape 3:2, highest resolution.
```

### C11 · İHA rampası

```
Photorealistic aerial photograph looking down at a single military vehicle on the ground, from high above and only slightly to the south, orthographic with no perspective. The view must look like this: the roof of the vehicle is fully visible and is by far the largest surface; the side facing the bottom of the frame shows only as a thin strip, about one third as tall as the roof is wide; wheels or tracks on that side appear as very flat shapes, wheels as ellipses about three times wider than tall. 
Subject: a single 6x6 military truck carrying a container launcher with six launch rails for delta-wing kamikaze drones, one drone visible on the top rail, a small ground control shelter beside it. Matte Nordic camouflage of dark green, grey-green and black patches, light dust on the lower body, small amber beacon lamp on the cab roof. Cab or front pointing to the RIGHT of the frame. 
Ground: it stands on a levelled gravel clearing in a Scandinavian pine forest in late summer: grey-pink crushed granite gravel, compacted tire tracks, patches of moss and pale lichen and low heather at the edges, a few small flat granite slabs. Wheels press slightly into the gravel, with dark contact shadows under the tires and the chassis. 
Lighting: golden late-evening sun from the LOWER-RIGHT at about 20° elevation: warm amber light on surfaces facing the lower-right, every object casts one clean shadow toward the upper-left about three times its height, shadows cool blue-grey. Natural cinematic grade, no HDR, no haze, no vignette. 
Framing: the subject fills about 46% of the frame width, centered slightly to the right so its shadow has room. The ground patch has an irregular natural outline with no straight edges, fills about 90% of the frame, and contains the entire shadow. Everything outside the ground patch is flat pure chroma green #00FF00 with no gradient and no shadow on the green. 
Detail: every bolt, hatch, grille, cable, tire tread and pebble razor sharp, no blur, no noise. No text, no markings, no insignia, no watermark. Landscape 3:2, highest resolution.
```

### C12 · Şişme maket

```
Photorealistic aerial photograph looking down at an inflatable decoy on the ground, from high above and only slightly to the south, orthographic with no perspective. The view must look like this: the roof of the vehicle is fully visible and is by far the largest surface; the side facing the bottom of the frame shows only as a thin strip, about one third as tall as the roof is wide; wheels or tracks on that side appear as very flat shapes, wheels as ellipses about three times wider than tall. 
Subject: an inflatable decoy of a long-range air defense launcher semitrailer: four inflatable missile canisters on a raised erector made of slightly wrinkled olive fabric, guy ropes and stakes, a small air pump on the ground. The fabric shows soft folds and seams. Matte Nordic camouflage of dark green, grey-green and black patches, light dust on the lower body, small amber beacon lamp on the cab roof. Cab or front pointing to the RIGHT of the frame. 
Ground: it stands on a levelled gravel clearing in a Scandinavian pine forest in late summer: grey-pink crushed granite gravel, compacted tire tracks, patches of moss and pale lichen and low heather at the edges, a few small flat granite slabs. Wheels press slightly into the gravel, with dark contact shadows under the tires and the chassis. 
Lighting: golden late-evening sun from the LOWER-RIGHT at about 20° elevation: warm amber light on surfaces facing the lower-right, every object casts one clean shadow toward the upper-left about three times its height, shadows cool blue-grey. Natural cinematic grade, no HDR, no haze, no vignette. 
Framing: the subject fills about 55% of the frame width, centered slightly to the right so its shadow has room. The ground patch has an irregular natural outline with no straight edges, fills about 90% of the frame, and contains the entire shadow. Everything outside the ground patch is flat pure chroma green #00FF00 with no gradient and no shadow on the green. 
Detail: every bolt, hatch, grille, cable, tire tread and pebble razor sharp, no blur, no noise. No text, no markings, no insignia, no watermark. Landscape 3:2, highest resolution.
```


## Havadakiler (D) — pedsiz, düz yeşil fon

### D1 · Kamikaze İHA (delta)

```
Photorealistic image seen from directly above (orthographic top view, zero perspective), the nose pointing straight UP in the frame. Subject: a delta-wing kamikaze drone with a rear pusher propeller, small vertical winglets at the wing tips, light grey paint. The object is centered and fills about 80% of the frame height. Lighting: golden late-evening sun from the LOWER-RIGHT: warm amber light on right-facing surfaces, cool blue fill on the left. Natural cinematic grade, no HDR. Razor sharp, every panel line and rivet visible, crisp at 200% zoom. Background flat pure chroma green #00FF00 with no gradient, no shadow, no ground. No text, no insignia, no labels, no watermark. Square image, highest resolution.
```

### D2 · Kamikaze İHA (X kanat)

```
Photorealistic image seen from directly above (orthographic top view, zero perspective), the nose pointing straight UP in the frame. Subject: a small loitering munition with two pairs of X-shaped folding wings, a round sensor nose, a rear propeller, light grey paint. The object is centered and fills about 80% of the frame height. Lighting: golden late-evening sun from the LOWER-RIGHT: warm amber light on right-facing surfaces, cool blue fill on the left. Natural cinematic grade, no HDR. Razor sharp, every panel line and rivet visible, crisp at 200% zoom. Background flat pure chroma green #00FF00 with no gradient, no shadow, no ground. No text, no insignia, no labels, no watermark. Square image, highest resolution.
```

### D3 · Jet kamikaze İHA

```
Photorealistic image seen from directly above (orthographic top view, zero perspective), the nose pointing straight UP in the frame. Subject: a jet-powered delta-wing kamikaze drone with a small dorsal turbojet intake, grey paint. The object is centered and fills about 80% of the frame height. Lighting: golden late-evening sun from the LOWER-RIGHT: warm amber light on right-facing surfaces, cool blue fill on the left. Natural cinematic grade, no HDR. Razor sharp, every panel line and rivet visible, crisp at 200% zoom. Background flat pure chroma green #00FF00 with no gradient, no shadow, no ground. No text, no insignia, no labels, no watermark. Square image, highest resolution.
```

### D4 · Keşif / karıştırıcı İHA

```
Photorealistic image seen from directly above (orthographic top view, zero perspective), the nose pointing straight UP in the frame. Subject: a reconnaissance drone with long straight high-aspect wings, a V-tail, a sensor ball under the nose, a rear propeller, light grey paint. The object is centered and fills about 80% of the frame height. Lighting: golden late-evening sun from the LOWER-RIGHT: warm amber light on right-facing surfaces, cool blue fill on the left. Natural cinematic grade, no HDR. Razor sharp, every panel line and rivet visible, crisp at 200% zoom. Background flat pure chroma green #00FF00 with no gradient, no shadow, no ground. No text, no insignia, no labels, no watermark. Square image, highest resolution.
```

### D5 · Balistik füze

```
Photorealistic image seen from directly above (orthographic top view, zero perspective), the nose pointing straight UP in the frame. Subject: a ballistic missile in flight: long slim cylindrical body, pointed nose cone, four small tail fins, grey and white paint, a bright engine flame at the tail. The object is centered and fills about 80% of the frame height. Lighting: golden late-evening sun from the LOWER-RIGHT: warm amber light on right-facing surfaces, cool blue fill on the left. Natural cinematic grade, no HDR. Razor sharp, every panel line and rivet visible, crisp at 200% zoom. Background flat pure chroma green #00FF00 with no gradient, no shadow, no ground. No text, no insignia, no labels, no watermark. Square image, highest resolution.
```

### D6 · Seyir füzesi

```
Photorealistic image seen from directly above (orthographic top view, zero perspective), the nose pointing straight UP in the frame. Subject: a subsonic cruise missile in flight: long slim light-grey body, two small straight mid-body wings deployed, a cross-shaped tail, a small air intake. The object is centered and fills about 80% of the frame height. Lighting: golden late-evening sun from the LOWER-RIGHT: warm amber light on right-facing surfaces, cool blue fill on the left. Natural cinematic grade, no HDR. Razor sharp, every panel line and rivet visible, crisp at 200% zoom. Background flat pure chroma green #00FF00 with no gradient, no shadow, no ground. No text, no insignia, no labels, no watermark. Square image, highest resolution.
```

### D7 · Hipersonik süzülme aracı

```
Photorealistic image seen from directly above (orthographic top view, zero perspective), the nose pointing straight UP in the frame. Subject: a hypersonic glide vehicle: a flat wedge-shaped dark body with sharp edges, faint orange glow of heat on the leading edges. The object is centered and fills about 80% of the frame height. Lighting: golden late-evening sun from the LOWER-RIGHT: warm amber light on right-facing surfaces, cool blue fill on the left. Natural cinematic grade, no HDR. Razor sharp, every panel line and rivet visible, crisp at 200% zoom. Background flat pure chroma green #00FF00 with no gradient, no shadow, no ground. No text, no insignia, no labels, no watermark. Square image, highest resolution.
```

### D8 · Önleyici füze

```
Photorealistic image seen from directly above (orthographic top view, zero perspective), the nose pointing straight UP in the frame. Subject: an air defense interceptor missile in flight: slim white body, small control fins, a bright rocket flame and short white smoke at the tail. The object is centered and fills about 80% of the frame height. Lighting: golden late-evening sun from the LOWER-RIGHT: warm amber light on right-facing surfaces, cool blue fill on the left. Natural cinematic grade, no HDR. Razor sharp, every panel line and rivet visible, crisp at 200% zoom. Background flat pure chroma green #00FF00 with no gradient, no shadow, no ground. No text, no insignia, no labels, no watermark. Square image, highest resolution.
```

### D9 · Savaş uçağı

```
Photorealistic image seen from directly above (orthographic top view, zero perspective), the nose pointing straight UP in the frame. Subject: a modern twin-engine stealth fighter jet with angular wings and twin canted tails, dark grey paint. The object is centered and fills about 80% of the frame height. Lighting: golden late-evening sun from the LOWER-RIGHT: warm amber light on right-facing surfaces, cool blue fill on the left. Natural cinematic grade, no HDR. Razor sharp, every panel line and rivet visible, crisp at 200% zoom. Background flat pure chroma green #00FF00 with no gradient, no shadow, no ground. No text, no insignia, no labels, no watermark. Square image, highest resolution.
```


## Efektler (E)

### E1 · Krater

```
Photorealistic aerial photograph looking almost straight down from high above, only very slightly from the south, orthographic with no perspective: roofs are fully visible, walls facing the bottom of the frame show only as thin strips. 
The frame shows an area about 30 m wide. 
Subject: a single fresh impact crater from a large missile warhead in a gravel clearing: a dark round pit, a ring of churned earth and broken granite, scattered rubble, black scorch marks radiating outward, small glowing embers. 
Setting: Scandinavian landscape in late summer: grey-pink granite, dark pine and spruce forest, moss, lichen, heather.  
Lighting: golden late-evening sun from the LOWER-RIGHT at about 20° elevation: warm amber light on surfaces facing the lower-right, every object casts one clean shadow toward the upper-left about three times its height, shadows cool blue-grey. Natural cinematic grade, no HDR, no haze, no vignette. 
Framing: the site with its own surrounding ground fills about 88% of the frame. The ground patch has an irregular natural outline with no straight edges and contains all shadows. Everything outside the ground patch is flat pure chroma green #00FF00 with no gradient and no shadow on the green. 
Detail: every roof, vent, vehicle, pipe, tree crown and path razor sharp, uniform sharpness, no blur, no noise. No text, no signs, no logos, no watermark. Square image, highest resolution.
```

### E2 · Yerde patlama

```
A large explosion on the ground seen straight down from high altitude: bright white-yellow fireball core, orange flame, a thick dark smoke ring spreading outward, debris specks flying out. Photographic, razor sharp, no cartoon. Isolated on pure black background #000000, no ground, no text. Square image, highest resolution.
```

### E3 · Havada önleme patlaması

```
Mid-air explosion of a missile being intercepted, seen from directly below: a small bright white-orange fireball, a ring of grey smoke puffs, many glowing metal fragments streaking outward. Photographic, razor sharp, no cartoon. Isolated on pure black background #000000, no ground, no text. Square image, highest resolution.
```

### E4 · Duman bulutu

```
Top-down view of a thick column of dark grey and black smoke rising from a burning target, seen straight down from high altitude, drifting toward the upper-left, lit warm orange on its lower-right side by a low evening sun, a faint orange glow at the center. Photographic, razor sharp, no cartoon. Isolated on pure black background #000000, no ground, no text. Square image, highest resolution.
```
