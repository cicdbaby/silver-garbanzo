# Menzil · Gök — GÖREV 7: Görsellerin baştan üretimi

## 0 · Karar: harekât maket masası

Şimdiki sorunun kökü stil değil, **ölçek**. Harita 360 km genişliğinde, bir füze bataryası ise 34 m. Bataryayı ekranda 16 piksel görmek için piksel başına 2 m gerekir; bu da 180.000 piksel genişliğinde bir harita demek. Hiçbir görsel bunu taşıyamaz. Yakınlaşınca bulanıklık ya da "taş/oyuncak" doku bu yüzden çıkıyor. Tesisler de araziye bu yüzden yapışmıyor.

Çözüm: oyunu bir **genelkurmay maket masası** gibi göstermek.
- **Arazi:** Müze kalitesinde, tepeden fotoğraflanmış bir kıyı maketi. Mat alçı zemin, tek tek seçilen ağaç tepeleri, kumlanmış granit, reçine su. Uzaktan da yakından da kasıtlı görünür; büyütülünce bulanık fotoğraf gibi değil, maket gibi durur.
- **Parçalar:** Tesisler, bataryalar, araçlar ve füzeler masaya konmuş minyatürler. Gerçek ölçeğin 10–15 katı büyüklükte çizilir; maket masasında bu doğal durur. Böylece haritayı 15 m/piksel'in altına yakınlaştırmaya hiç gerek kalmaz.
- **Oyun mantığı değişmez.** Menziller, hasar yarıçapları ve hızlar aynı kalır; değişen yalnızca görünüm.
- **Uyum:** Arazi ve parçalar aynı malzeme, aynı ışık ve aynı kamerayla üretildiği için sprite (oyun içi görsel parça) kesik görünmez. Kurulum yerlerinin altına araziyle aynı stilde zemin pedleri gelir.
- **Performans:** Yakın zoom için kullanılan 9 doku ve ağır gürültü hesapları tamamen kalkar. Zemin shader'ı (ekran kartında çalışan çizim programı) birkaç doku okumasına iner; büyük ihtimalle senin gördüğün GPU takılmalarını da bitirir.

Çocuksu olmaması için: renkler soluk ve serin, plastik parlaklık yok, karikatür ya da low-poly yok. Referans: mimari yarışma maketi, savaş müzesi diyoraması, Herpa/Roco 1:87 askerî modeller.

## 1 · Çalışma kuralları (GPT'ye ilk mesajda bunu da ver)

1. **Aşama sırası:**
   - Önce **A · Stil testi** (3 görsel). Onları bana getir, birlikte bakalım.
   - Beğenilirse B → C → D → E → F → G sırasıyla devam.
   - Kredi azsa önce B-duo + C + D + E. Oyun bunlarla tamamen yeni görünüme geçer.
2. **Aynı sohbet:** Her grup aynı sohbette, sırayla üretilsin. Grubun ilk görselinden sonraki her istemin sonuna şu cümle eklensin:
   `Match the previous image exactly in light direction, colour grade, material and level of detail.`
3. **Işık:** Bütün görsellerde güneş **sol alttan (güneybatı)** gelir, gölgeler **sağ üste** düşer. Bu hiç değişmemeli.
4. **Boyut ve şeffaflık:**
   - Harita karoları 1536×1024.
   - Parçalar 1024×1024, şeffaf arka plan (PNG alfa).
   - Şeffaflık olmazsa düz saf beyaz arka plan; ben kesiyorum.
   - Patlama ateşi saf siyah arka plan üzerine.
5. **Gölge:** Döner ya da hareketli parçalarda **yere düşen gölge olmasın**, yalnız tam altta temas kararması olsun; gölgeyi kod çiziyor. Sabit tesislerde gölge olsun.
6. **Dosya adı:** Her görseli başlıktaki adla kaydet (ör. `M_duo_r2c3.png`, `S_RAD_base.png`).
7. **Yasaklar:** Yazı, etiket, ızgara, çerçeve ve filigran olmasın. İnsan figürü olmasın. Bayrak ya da arma olmasın.

### Ortak stil bloğu (STYLE)

Aşağıdaki istemlerde `[STYLE]` geçen yere bunu aynen yapıştır:

```
Strict top-down orthographic view, camera pointing straight down, no perspective. A museum-grade terrain model of a Scandinavian coast (southern Norway / Swedish west coast) photographed from directly above. Materials of a high-end architectural model: matte painted plaster ground with fine natural texture, dense fine flock for pine and birch forest with individual tree crowns readable, sand-blasted grey-pink granite outcrops, glossy deep slate-blue resin water that turns teal over shallow shores, thin pale gravel and asphalt roads, small muted fields. Colours muted, desaturated and cool: moss green, olive, granite grey-pink, slate blue, bone white. No saturated green, no orange tint. Soft late-afternoon sun from the lower-left (south-west), long soft shadows falling toward the upper-right, gentle ambient occlusion. Crisp focus across the whole frame: no tilt-shift blur, no vignette, no haze, no clouds. No text, labels, grid, borders, watermark or people. Not cartoon, not toy-coloured, not low-poly.
```

### Parça stil bloğu (PIECE)

```
A single military miniature in the quality of a 1:87 Herpa/Roco display model: precise panel lines, matte NATO-neutral dark olive-grey paint, subtle dust weathering on lower surfaces, rubber tyres, no markings, no flags, no crew. Strict top-down orthographic view (camera straight down), same soft late-afternoon light from the lower-left. NO cast shadow on the ground, only a faint contact darkening directly beneath. Object centred, filling about 80% of the frame, nothing else in the frame, transparent background (PNG with alpha; if transparency is impossible use a plain pure white background).
```

---

## A · Stil testi (3 görsel; önce bunlar)

### A1 · Harita karosu testi
Ek: `kaynak_duo/duo_r2c2.png`
```
Redraw the attached map tile in this style: [STYLE]
Keep every coastline, island, lake, river, road and field boundary exactly in place and shape — this tile must line up pixel for pixel with its neighbours. Remove all buildings and settlements (only landscape, roads and fields remain). Output 1536×1024, same framing as the input.
```

### A2 · Parça testi: uzun menzil HS rampası
```
[PIECE]
Subject: a long-range surface-to-air missile launcher on an 8-wheel truck, four large square missile canisters raised at 60° toward the top of the image, outriggers deployed. Vehicle about 12 m long; the canisters point to the top of the frame.
```

### A3 · Patlama testi
```
Seen from directly above: the fireball of a large high-explosive warhead detonating on open ground, a few milliseconds after impact. Bright white-yellow core, orange flame lobes, dark smoke edges starting to curl, a few incandescent fragments flying outward. Isolated on a pure black background (for additive blending), centred, filling 80% of the frame, no ground visible, no text.
```

---

## B · Harita karoları

Kaynakları zip'te: `kaynak_duo/` (16 karo, 4 sütun × 4 satır) ve `kaynak_quad/` (24 karo, 4 sütun × 6 satır). Karolar birbirinin %12'sine taşar; birleştirmeyi ben yapıyorum. Her karoda kaynak görseli ekleyip aynı istemi kullan; ilk karodan sonra eşleşme cümlesini ekle.

```
Redraw the attached map tile in this style: [STYLE]
Keep every coastline, island, lake, river, road and field boundary exactly in place and shape — this tile must line up pixel for pixel with its neighbours. Remove all buildings and settlements (only landscape, roads and fields remain). Output 1536×1024, same framing as the input.
```

- **B-duo:** `M_duo_r1c1` … `M_duo_r4c4` (16). İki kişilik oyunun haritası, öncelikli.
- **B-quad:** `M_quad_r1c1` … `M_quad_r6c4` (24). Dörtlü harekât haritası; kredi kalırsa.

Not: Karonun içinde deniz çoksa GPT suya küçük adalar eklemek isteyebilir. Eklerse o karoyu tekrar ürettir; kıyı çizgisinin aynı kalması şart, kurulum yerleri ona göre hesaplanıyor.

---

## C · Kurulum pedi zeminleri (4)

Parçaların altına konacak zeminler. Kenarları şeffaflığa yumuşakça erimeli ki haritaya kaynasın.

```
[STYLE]
Subject: a prepared military hardstand as part of the terrain model — {VARIANT}. About 80 m across, roughly square with rounded corners, tyre tracks and slight wear, edges blending softly into the surrounding terrain, which then fades to full transparency toward the frame edges (PNG alpha). Centred, top-down, nothing else.
```
`{VARIANT}` yerine sırayla:
- `P_orman`: `a gravel clearing cut into pine forest, a few stumps, a short gravel track leading out to the bottom edge`
- `P_tepe`: `a concrete pad on a bare granite hilltop, low earth berm on the side facing the top of the image`
- `P_acik`: `a compacted gravel hardstand on open grassland next to a field edge`
- `P_kiyi`: `an asphalt hardstand on rocky coast, a strip of water visible along the top edge`

---

## D · Tesisler (14, sabit; gölgeli)

Ortak istem; `{SUBJECT}` yerine aşağıdakileri koy:
```
[STYLE]
Subject: {SUBJECT}. The complete site as one miniature on its own irregular base of ground (gravel, grass, fence, access road stub), the base fading softly into full transparency toward the frame edges (PNG alpha). Cast shadows toward the upper-right as in the style. Centred, filling about 85% of the frame, top-down orthographic.
```
- `T_HQ`: `a hardened military command headquarters: low concrete bunker complex with earth-covered roofs, antenna mast field, satellite dishes, perimeter fence, vehicle park`
- `T_REFN`: `an oil refinery: distillation columns, pipe racks, round storage tanks with floating roofs, flare stack`
- `T_PWR`: `a gas-fired power station: turbine hall, two cooling towers, switchyard with transformers, high-voltage lines leaving toward the top`
- `T_AIRB`: `a military air base section: one runway segment running diagonally, taxiway, six hardened aircraft shelters, control tower, fuel farm`
- `T_FAB`: `a defence factory: long saw-tooth roofed assembly halls, test yard, loading docks`
- `T_DEPO`: `an ammunition depot: rows of earth-covered igloo bunkers separated by blast berms, inner fence`
- `T_FUEL`: `a fuel storage farm: eight large round tanks inside bunded enclosures, pump house, rail spur`
- `T_COMM`: `a communications centre: lattice towers, large dish antennas, low equipment buildings`
- `T_MIL`: `an army barracks: rows of long accommodation blocks, parade ground, motor pool with parked trucks`
- `K_1`: `a small Nordic harbour town: white and ochre wooden houses, church, quay with small boats, streets following the shore`
- `K_2`: `a village in forest clearings: scattered red-brown wooden houses, barns, a school, gravel roads`
- `K_3`: `a modern small town: apartment blocks, shopping centre with car park, sports field, roundabout`
- `K_4`: `an industrial suburb: warehouses, a truck terminal, rail sidings, a few houses`
- `K_5`: `an old town centre: dense pitched roofs, a square with a stone church, narrow streets, a small park`

---

## E · Hava savunma ve rampa parçaları (23; dönen kısımlar ayrı)

Hepsi `[PIECE]` ile başlar. Konu satırı her birinin altında. **Ayrı parçalar** aynı ölçekte ve aynı merkezde çizilmeli; ilkinden sonra şunu ekle: `Same scale and centre point as the previous image so the two layers stack exactly.`

| Ad | Konu (Subject: …) |
|---|---|
| `S_RAD_base` | `a long-range surveillance radar site: trailer-mounted radar base with leveling jacks, generator truck and shelter beside it, WITHOUT the antenna (bare rotating pedestal visible)` |
| `S_RAD_ant` | `ONLY the radar antenna that sits on that pedestal: a large flat rectangular phased-array panel 10 m wide, seen from above, long axis horizontal` |
| `S_CIWS_base` | `a land-based close-in weapon system: low armoured mount on a concrete slab with ammunition container beside it, WITHOUT the gun turret` |
| `S_CIWS_tur` | `ONLY the CIWS gun turret: rounded white-grey radar dome housing with a multi-barrel 20 mm rotary cannon pointing to the right` |
| `S_SHORAD_base` | `a 6-wheel short-range air-defence vehicle chassis WITHOUT its launcher turret` |
| `S_SHORAD_tur` | `ONLY the launcher turret: two pods of four short missiles each and a small electro-optical sensor ball, pointing to the right` |
| `S_MRAD_ln` | `a medium-range air-defence vertical launcher truck: 8 square vertical launch cells in a raised box on a 6-wheel truck` |
| `S_MRAD_rad` | `a medium-range fire-control radar truck with a rotating square radar panel on top (panel included)` |
| `S_MRAD_cmd` | `a medium-range air-defence command shelter truck with antenna masts` |
| `S_LRAD_ln` | `a long-range surface-to-air missile launcher on an 8-wheel truck, four large square missile canisters raised at 60° toward the top of the image` |
| `S_LRAD_rad` | `a long-range engagement radar on a semi-trailer, large raised phased-array panel facing the top of the image` |
| `S_UPPER_ln` | `an exo-atmospheric interceptor launcher: 8-wheel truck with eight round missile canisters raised steeply toward the top of the image` |
| `S_UPPER_rad` | `a very large X-band ballistic-missile-defence radar on a trailer, panel facing the top of the image, with cooling and power units` |
| `S_LASER_base` | `a high-energy laser air-defence system: container module on a truck with power and cooling units, WITHOUT the beam director` |
| `S_LASER_tur` | `ONLY the laser beam director: a compact armoured turret with a large circular optical aperture pointing to the right` |
| `S_IDR` | `an interceptor-drone launcher: truck carrying a box of twelve launch tubes angled toward the top` |
| `S_EW_base` | `an electronic warfare vehicle: 8-wheel truck with equipment shelter, WITHOUT the antenna array` |
| `S_EW_ant` | `ONLY its rotating log-periodic antenna array on a short mast head, long axis horizontal` |
| `S_DEC` | `an inflatable decoy of a long-range SAM launcher: same shape as a missile launcher truck but slightly soft, wrinkled fabric surfaces, inflation hoses and a small blower beside it` |
| `S_TEL_down` | `a ballistic missile transporter-erector-launcher on an 8-wheel truck, missile lying horizontal and covered, front of the truck toward the right` |
| `S_TEL_up` | `the same ballistic missile transporter-erector-launcher with the missile raised vertical on its erector arm, launch pad lowered behind the truck` |
| `S_DLN_closed` | `a containerised drone launcher: a 40-ft container on a truck with its roof doors closed` |
| `S_DLN_open` | `the same containerised drone launcher with roof doors open, six delta-wing drones visible on launch rails angled toward the top` |

---

## F · Havadaki parçalar (12)

`[PIECE]` ile başlar; hepsi **burnu sağa bakacak** şekilde (kod döndürüyor).

| Ad | Konu |
|---|---|
| `H_BM` | `a ballistic missile in flight, single stage, conical nose, small fins` |
| `H_HGV` | `a hypersonic glide vehicle: dark wedge-shaped glider with heat-scorched leading edges` |
| `H_CM` | `a subsonic cruise missile with short swept wings deployed and a small tail` |
| `H_DRN` | `a delta-wing kamikaze drone with a pusher propeller at the rear` |
| `H_ARMD` | `a loitering anti-radiation drone, slender body with straight wings and a twin tail` |
| `H_RCN` | `a small reconnaissance drone with long straight wings and a camera ball under the nose` |
| `H_JAM` | `a jamming drone with long wings and antenna pods at the wingtips` |
| `H_FTR` | `a modern stealth multirole fighter jet, grey, seen exactly from above` |
| `H_ICP` | `a slender surface-to-air interceptor missile with mid-body fins` |
| `H_BAL` | `a high-altitude research balloon seen from above: a large pale envelope with a small instrument gondola` |
| `H_MOTH` | `a large mothership drone carrying eight small drones under its wings` |
| `H_GLIDE` | `a glide bomb with long folding wings deployed` |

---

## G · Efektler (14)

- **Ateş** (saf siyah arka plan, üstten):
  - `X_fire1`: A3'teki patlama.
  - `X_fire2`: aynı ama daha küçük bir dron başlığı: `small, more orange, fewer fragments`.
  - `X_air`: havada önleme: `a mid-air interceptor kill: a bright flash with a ring of fragments and a small smoke puff, no ground`.
- **Duman** (şeffaf arka plan, üstten): `Seen from directly above: a single billowing cloud of {X} smoke, soft volumetric edges, transparent background, centred, no ground.`
  - `X_smoke1`, `X_smoke2`: `dark grey-black` (iki farklı şekil)
  - `X_smoke3`: `light grey dust`
  - `X_smoke4`: `white rocket exhaust`
- **Zemin izleri** (şeffaf, maket stiliyle uyumlu, `[STYLE]` başta):
  - `X_crater1`, `X_crater2`, `X_crater3`: `a fresh impact crater in the terrain model, scorched soil, ejecta rays, edges fading to transparency`. Üçü farklı boyutta: küçük, orta, büyük.
  - `X_scorch`: `a burn scar on grass, edges fading to transparency`.
- **Diğer:**
  - `X_debris`: `scattered burning metal debris pieces, transparent background`.
  - `X_burn`: `flames and smoke rising from a damaged industrial building, seen from above, transparent background`.

---

## Bunlar gelince kod tarafında ne yapacağım

- **Harita:** Karoları hizalayıp tek haritada birleştiririm. Sadece görünen karolar yüklenir. Yakın zoom için kullanılan doku sistemi tamamen kalkar; yakınlaşma, haritanın kendi çözünürlüğünün 1,5 katında durur.
- **Parçalar:** Gerçek ölçeğin yaklaşık 12 katı büyüklükte çizilir. Kurulum yerlerinin altına araziye göre seçilen ped gelir (orman, tepe, açık, kıyı). Gölgeleri kod, güneşe göre tek tip çizer.
- **Hareket:** Hepsi kodla, ayrı katmanlardan:
  - radar ve elektronik harp anteni döner;
  - yakın savunma topu, kısa menzil HS ve lazer taretleri hedefe döner;
  - balistik rampa ateşten önce füzeyi kaldırır, ateşten sonra indirir;
  - İHA konteynerinin kapakları açılır.
- **Efektler:**
  - ateş topu 0,4 sn'de büyüyüp söner;
  - duman rüzgârla sürüklenir;
  - krater kalıcıdır;
  - yanan tesisten sürekli duman çıkar.
- **Hız:** Bütün parçalar tek bir doku atlasında (tüm küçük görsellerin toplandığı tek büyük resim) toplanır. Dosya sayısı ve çizim maliyeti düşer.
