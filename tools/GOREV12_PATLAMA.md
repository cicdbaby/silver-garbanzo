# Menzil · Gök — GÖREV 12: Patlama, yangın ve yıkım görselleri

72 görsel. Hedef: her isabetin kendine has, fotoğraf gerçekliğinde ve tepeden bakılan bir an olması; rafineri vurulunca dakikalarca süren devasa bir petrol yangını; yıkılan tesisin gerçekten yıkılmış görünmesi.

Hepsi **tam tepeden** (kamera dik aşağı) ve **aynı ışıkla** (güneş sol alttan). Oyun bunları zaman içinde büyütüp söndürerek, döndürerek ve üst üste koyarak canlandırıyor; o yüzden her görsel **tek bir an**, tek bir nesne.

## GPT'ye ilk mesaj (bir kez yapıştır)

```
I need a set of visual-effect images for a top-down military strategy game, one image per message. Rules for every image:
- Camera exactly overhead, looking straight down. No horizon, no perspective, no ground unless I ask for it.
- Photographic realism, like high-altitude reconnaissance or drone footage of real events. Not cartoon, not painterly, no lens flare, no glow halos added on top, no text, no watermark, no border.
- Subject centred, filling about 80% of a square 1024×1024 frame, nothing else in the frame.
- Background: exactly what each prompt says — either PURE BLACK (#000000, for fire and light, which the game adds as light) or TRANSPARENT (PNG with alpha; if transparency is impossible, a plain pure white background).
- Lighting for anything solid (smoke, debris, ruins): soft late-afternoon sun from the lower-left.
After the first image of each group, match it exactly in colour grade, realism and level of detail.
Save each file with the name I give.
```

Her grubun ilk görselinden sonraki mesajların sonuna şunu ekle:
`Match the previous image exactly in colour grade, realism and level of detail, but make the shape clearly different.`

### [STYLE] bloğu (E ve F gruplarında başa yapıştır)

Aşağıdaki istemlerde `[STYLE]` geçen yere bunu aynen yapıştır:

```
Strict top-down orthographic view, camera pointing straight down, no perspective. A museum-grade terrain model of a Scandinavian coast (southern Norway / Swedish west coast) photographed from directly above. Materials of a high-end architectural model: matte painted plaster ground with fine natural texture, dense fine flock for pine and birch forest with individual tree crowns readable, sand-blasted grey-pink granite outcrops, glossy deep slate-blue resin water that turns teal over shallow shores, thin pale gravel and asphalt roads, small muted fields. Colours muted, desaturated and cool: moss green, olive, granite grey-pink, slate blue, bone white. No saturated green, no orange tint. Soft late-afternoon sun from the lower-left (south-west), long soft shadows falling toward the upper-right, gentle ambient occlusion. Crisp focus across the whole frame: no tilt-shift blur, no vignette, no haze, no clouds. No text, labels, grid, borders, watermark or people. Not cartoon, not toy-coloured, not low-poly.
```

---

## A · Patlama ateş topları (15) — saf siyah fon

Her boy üç an: **a** ilk çakma, **b** ateş topu, **c** dumana dönüş. Oyun a→b→c'yi sırayla gösteriyor.

| Dosya | İstem |
|---|---|
| `X_fb_s_a` | `Seen from directly above, the first 20 milliseconds of a small drone warhead (5 kg) detonating on the ground: a tight blinding white-yellow core with a thin ring of orange, a few sparks. Pure black background.` |
| `X_fb_s_b` | `Seen from directly above, the same small explosion 0.3 seconds later: a ragged orange fireball about the size of a car, turbulent lobes, darker red edges, sparks and small fragments flying outward. Pure black background.` |
| `X_fb_s_c` | `Seen from directly above, the same small explosion 1 second later: the fire collapsing into dark smoke with a few glowing embers and orange patches inside. Pure black background.` |
| `X_fb_m_a` | `Seen from directly above, the first 20 milliseconds of a cruise-missile warhead (450 kg) detonating: an intense white core, a sharp spherical shock flash, the beginning of an orange shell. Pure black background.` |
| `X_fb_m_b` | `Seen from directly above, the same explosion 0.4 seconds later: a big boiling orange-yellow fireball with deep red and black folds, a halo of flying debris streaks radiating outward. Pure black background.` |
| `X_fb_m_c` | `Seen from directly above, the same explosion 1.5 seconds later: the fireball rolling into thick black smoke, orange still glowing in the folds, glowing debris scattered around. Pure black background.` |
| `X_fb_l_a` | `Seen from directly above, the first 20 milliseconds of a 700 kg ballistic-missile warhead hitting the ground: a huge blinding white disc, a visible circular shock front, radial jets of hot gas. Pure black background.` |
| `X_fb_l_b` | `Seen from directly above, the same blast 0.5 seconds later: an enormous turbulent fireball, white-yellow centre, orange and blood-red outer layers with black soot veins, long radial streaks of debris and dust. Pure black background.` |
| `X_fb_l_c` | `Seen from directly above, the same blast 2 seconds later: a towering mass of black and brown smoke with fire still burning inside its folds, embers and burning chunks scattered widely. Pure black background.` |
| `X_fb_l2_a`, `X_fb_l2_b`, `X_fb_l2_c` | Aynı üç istem, ikinci bir varyasyon (oyun rastgele seçecek): sonuna `Different shape: asymmetric, blown toward one side.` ekle. |
| `X_fb_oil_a` | `Seen from directly above, the ignition of a large oil storage tank hit by a missile: a gigantic white-orange flash spreading in a wide ring across the tank farm, burning fuel splashing outward in jets. Pure black background.` |
| `X_fb_oil_b` | `Seen from directly above, a fuel-air fireball rising from an oil refinery 1 second after the hit: a colossal rolling orange fireball with black soot boiling through it, several hundred metres wide. Pure black background.` |
| `X_fb_oil_c` | `Seen from directly above, the same fireball 4 seconds later turning into a huge black mushroom of oily smoke with orange fire still raging underneath. Pure black background.` |

## B · Havada önleme (4) — saf siyah fon

| Dosya | İstem |
|---|---|
| `X_air_s` | `Seen from directly above, a small drone destroyed in mid-air by gunfire: a small orange burst, a puff of grey smoke, fragments spraying in one direction. Pure black background.` |
| `X_air_m` | `Seen from directly above, a cruise missile destroyed in mid-air by a surface-to-air missile: a bright orange-white burst, a ring of fragments, a short smoke trail behind it. Pure black background.` |
| `X_air_l` | `Seen from directly above, a ballistic missile warhead destroyed by an interceptor at high altitude: a blinding white flash with a cone of glowing debris continuing forward along the missile's path. Pure black background.` |
| `X_air_hpm` | `Seen from directly above, a swarm of small drones knocked out at once: dozens of tiny sparks and small electrical flashes scattered across the frame, faint blue-white arcs, a few drones trailing smoke. Pure black background.` |

## C · Duman (12) — şeffaf fon

| Dosya | İstem |
|---|---|
| `X_smk_oil1` … `X_smk_oil4` | `Seen from directly above, a single huge billowing cloud of thick black oily smoke from a burning refinery, dense rolling cauliflower shapes, brown-black, lit from the lower-left, soft feathered edges. Transparent background.` (dört farklı şekil) |
| `X_smk_dark1` … `X_smk_dark3` | `Seen from directly above, a cloud of dark grey explosion smoke, a few seconds old, irregular puffy shape, lit from the lower-left, feathered edges. Transparent background.` (üç farklı şekil) |
| `X_dust1`, `X_dust2` | `Seen from directly above, a wide ring of pale brown dust and dirt thrown up by a ground explosion, thicker at the outer edge, thin in the centre. Transparent background.` |
| `X_plume1`, `X_plume2` | `Seen from directly above, a long smoke plume from a large fire drifting to the right with the wind: dense and black at the left end where it rises, thinning and widening toward the right edge of the frame. Transparent background. Wide composition: the plume spans the full width.` |
| `X_steam` | `Seen from directly above, a white cloud of steam and pulverised concrete dust from a collapsing building. Transparent background.` |

## D · Yangın (12) — saf siyah fon

| Dosya | İstem |
|---|---|
| `X_oilfire1` … `X_oilfire4` | `Seen from directly above, a large pool of burning crude oil: tall turbulent flames seen from the top, bright yellow-orange tongues, deep red edges, black soot curling out of the flames. Pure black background.` (dört farklı şekil) |
| `X_tankfire1`, `X_tankfire2` | `Seen from directly above, a single round oil storage tank on fire: the roof gone, a circle of intense flame filling the tank, flames spilling over one side. Pure black background.` |
| `X_bldfire1` … `X_bldfire3` | `Seen from directly above, an industrial building burning through its collapsed roof: flames coming out of holes in the roof and windows, glowing beams, sparks. Pure black background.` |
| `X_grassfire1`, `X_grassfire2` | `Seen from directly above, a ragged line of small grass and brush fire spreading outward, thin flames, glowing edges. Pure black background.` |
| `X_embers` | `Seen from directly above, scattered glowing embers and small burning debris lying on the ground after an explosion, orange points of light of different sizes. Pure black background.` |

## E · Zemin izleri (9) — şeffaf fon, harita maketi tarzıyla uyumlu

Bunlar haritaya kalıcı olarak düşüyor; GÖREV 7'deki **[STYLE]** bloğunu başa ekle.

| Dosya | İstem |
|---|---|
| `X_crater_s1`, `X_crater_s2` | `[STYLE] A small fresh crater from a drone warhead, about 3 m across, scorched soil, a little ejecta, edges fading smoothly to transparency. Transparent background.` |
| `X_crater_m1`, `X_crater_m2` | `[STYLE] A fresh crater from a cruise-missile warhead, about 10 m across, raw earth, a ring of ejecta, black scorch, edges fading to transparency. Transparent background.` |
| `X_crater_l1`, `X_crater_l2` | `[STYLE] A deep fresh crater from a ballistic missile, about 25 m across, steep walls, long radial ejecta rays, a wide black scorch ring, edges fading to transparency. Transparent background.` |
| `X_cluster` | `[STYLE] A field of a dozen small craters and scorch marks scattered over an area, left by a cluster munition, edges fading to transparency. Transparent background.` |
| `X_oilstain` | `[STYLE] A large irregular black stain of burnt oil and soot on the ground, glossy in places, edges fading to transparency. Transparent background.` |
| `X_scorch2` | `[STYLE] A wide burn scar on grass and soil, black centre fading through brown to the natural ground at the edges. Transparent background.` |

## F · Yıkılmış tesisler (14) — şeffaf fon, GÖREV 7 tesisleriyle aynı stil ve ölçek

GÖREV 7'deki tesis görselini (`T_REFN` vb.) **ek olarak ver**, istemin başına `[STYLE]` ve şu cümleyi koy:
`Redraw the attached facility destroyed after a missile strike, same position, size, framing and camera, so it can replace the original exactly.`

| Dosya | Ek | İstem devamı |
|---|---|---|
| `T_REFN_ruin` | `T_REFN` | `Several storage tanks ruptured and burnt black, one collapsed, pipework twisted, a pool of burnt oil, soot everywhere, no flames.` |
| `T_FUEL_ruin` | `T_FUEL` | `Tanks burst and blackened, roofs caved in, burnt oil spread over the bund, no flames.` |
| `T_PWR_ruin` | `T_PWR` | `Turbine hall roof caved in, one cooling tower cracked open, transformer yard blackened and wrecked.` |
| `T_FAB_ruin` | `T_FAB` | `Factory roof collapsed in large sections, exposed steel frame, rubble, burnt interior.` |
| `T_DEPO_ruin` | `T_DEPO` | `Ammunition bunkers blown open, earth mounds blasted apart, scattered craters, scorched ground.` |
| `T_COMM_ruin` | `T_COMM` | `Antenna masts toppled across the site, equipment building gutted.` |
| `T_MIL_ruin` | `T_MIL` | `Barracks blocks partly collapsed, roofs burnt through, vehicles burnt out in the yard.` |
| `T_AIRB_ruin` | `T_AIRB` | `Runway cratered along its length, hangars collapsed, aircraft shelters burnt.` |
| `T_HQ_ruin` | `T_HQ` | `Command bunker's concrete roof shattered with a deep crater, surrounding buildings flattened.` |
| `K_1_ruin` … `K_5_ruin` | `K_1` … `K_5` | `The town heavily bombed: many roofs gone, blocks reduced to rubble, black scorch, streets covered with debris; some buildings still standing.` |

## G · Şok, enkaz, kıvılcım (6)

| Dosya | Fon | İstem |
|---|---|---|
| `X_shock1`, `X_shock2` | saf siyah | `Seen from directly above, the expanding circular shockwave of a large explosion: a thin bright ring of compressed air and dust, faint inside. Pure black background.` |
| `X_debris1`, `X_debris2` | şeffaf | `Seen from directly above, a spray of dark metal and concrete debris chunks of different sizes flying outward from a centre point, some trailing thin smoke. Transparent background.` |
| `X_sparks` | saf siyah | `Seen from directly above, a burst of bright incandescent sparks and tiny hot fragments radiating from the centre with short motion streaks. Pure black background.` |
| `X_flash` | saf siyah | `Seen from directly above, a soft round white-yellow light flash with a warm orange falloff, no structure, like the light of an explosion reflected on the ground. Pure black background.` |

---

## Teslim

PNG olarak, başlıktaki adlarla, tek zip. Siyah fonluları ben ışık olarak işliyorum, şeffafları doğrudan kullanıyorum. Hepsi gelmese de olur: hangi dosya varsa o devreye girer, eksik olan yerine şimdiki çizim kalır.

Kredi azsa sıra şu olsun: **A** (önce `l` ve `oil`), **D** (`oilfire`, `tankfire`), **F** (`T_REFN_ruin`, `T_FUEL_ruin`), **C** (`oil` dumanı), sonra geri kalanı.
