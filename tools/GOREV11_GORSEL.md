# Menzil · Gök — GÖREV 11: Yeni silahların görselleri

Sekiz görsel. Hepsi GÖREV 7'deki maket masası stiliyle aynı; oyunda şu an yerlerinde geçici görsel var, bunlar gelince kendiliğinden değişir.

## GPT'ye ilk mesaj (bir kez yapıştır)

```
I need 8 images for a strategy game, one per message, all in exactly the same style. Rules for every image:
- Strict top-down orthographic view, camera pointing straight down, no perspective.
- Style: a 1:87 Herpa/Roco-quality military display model photographed from directly above: precise panel lines, matte NATO-neutral dark olive-grey paint (aircraft and missiles: matte medium grey), subtle dust weathering on lower surfaces, no markings, no numbers, no flags, no crew, no text.
- Soft late-afternoon light from the lower-left (south-west).
- NO cast shadow on the ground, only a faint contact darkening directly beneath.
- Object centred, filling about 80% of a 1024×1024 frame, nothing else in the frame.
- Transparent background (PNG with alpha). If transparency is impossible, a plain pure white background.
- Not cartoon, not toy-coloured, not low-poly, no glow effects.
After the first image, match it exactly in light direction, colour grade, material and level of detail.
I will send the subjects one by one. Save each file with the name I give.
```

Sonra aşağıdakileri **sırayla, her biri ayrı mesaj** olarak gönder. İlkinden sonraki her mesajın sonuna şunu ekle:
`Match the previous image exactly in light direction, colour grade, material and level of detail.`

---

## 1 · Hava savunma parçaları (4)

İki parçalı olanlar üst üste biniyor. İkinci parçanın sonuna ayrıca şunu ekle:
`Same scale and centre point as the previous image so the two layers stack exactly.`

**S_HPM_base** — Mikrodalga HS gövdesi
```
Subject: a high-power microwave counter-drone system: a 20-foot equipment container mounted on a 6-wheel military truck, with a diesel generator and a cooling unit on the rear deck, WITHOUT the emitter antenna — a bare round turntable is visible on the container roof. Truck front toward the right. Vehicle about 9 m long.
```

**S_HPM_ant** — Mikrodalga HS anteni (dönen parça)
```
Subject: ONLY the microwave emitter that sits on that turntable: a flat square phased-array panel about 3 m wide on a short yoke mount, the panel face pointing to the right, seen exactly from above. Nothing else in the frame.
```

**S_GPI_ln** — Süzülme evresi önleyici rampası
```
Subject: a glide-phase interceptor launcher: a heavy 10-wheel truck carrying four very large round missile canisters raised steeply toward the top of the image, outriggers deployed. Vehicle about 14 m long, bigger and heavier than a normal air-defence launcher.
```

**S_GPI_rad** — Süzülme evresi önleyici radarı
```
Subject: a large space-and-missile tracking radar on a semi-trailer: a tall, steeply raised octagonal phased-array face pointing toward the top of the image, with a separate power generator trailer beside it. About 16 m long in total.
```

---

## 2 · Havadakiler (4)

Hepsinde **burun sağa** bakmalı (oyun döndürüyor). Her birinin sonuna şunu ekle:
`Nose pointing exactly to the right of the frame.`

**H_KAAN** — KAAN
```
Subject: the Turkish KAAN fifth-generation stealth fighter seen exactly from above: twin engines, two outward-canted vertical tails, large trapezoidal wings with sharply swept leading edges, diamond-section nose, internal weapons bays closed, matte medium grey, no markings.
```

**H_UCAV** — Kızılelma tipi insansız savaş uçağı (sadık kanat)
```
Subject: a single-engine jet unmanned combat aircraft seen exactly from above, in the style of a loyal-wingman drone: no cockpit canopy, a dorsal air intake behind the nose, small canards, swept delta wings, twin canted tails, matte medium grey, no markings. Noticeably smaller and simpler than a manned fighter.
```

**H_SWRM** — Sürü İHA'sı
```
Subject: one small tube-launched swarm drone seen exactly from above: a slim cylindrical body about 0.6 m long with four folding X-wings fully deployed and a tiny pusher propeller at the tail, matte dark grey.
```

**H_HCM** — Hipersonik seyir füzesi
```
Subject: a hypersonic scramjet cruise missile seen exactly from above: a long, slender, flat-sided wedge body with a rectangular air intake under the forward body, small cruciform tail fins, a heat-darkened, slightly bluish nose cone and leading edges, matte grey.
```

---

## Dosyalar

Görselleri bu adlarla PNG olarak kaydet ve topluca bana getir (zip olur, tek tek de olur):

| Dosya | Oyunda nerede |
|---|---|
| `S_HPM_base.png`, `S_HPM_ant.png` | Kur → Yakın savunma → Mikrodalga HS |
| `S_GPI_ln.png`, `S_GPI_rad.png` | Kur → Balistik savunma → Süzülme Evresi Önleyici |
| `H_KAAN.png` | Türkiye'nin savaş uçağı (SEAD, süzülen bomba, sadık kanat görevleri) |
| `H_UCAV.png` | Sadık kanat görevinde uçaktan ayrılan iki insansız savaş uçağı |
| `H_SWRM.png` | Sürü İHA (İHA sınıfı, tek atışta 12 adet) |
| `H_HCM.png` | Hipersonik seyir füzesi (Seyir sınıfı) |

Ben kesip boyutlandırıp `public/img/v7/` altına koyuyorum; kodda bir şey değiştirmeye gerek yok.
