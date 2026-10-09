# Menzil · Gök — proje devir dosyası

Bu dosya projeyi yeni bir geliştiriciye (ChatGPT) devretmek için yazıldı. Her şey burada: ne yapıldı, kod nasıl kurulu, hangi kararlar neden alındı, ne açık kaldı, nasıl çalışılacak.

**Çalışma düzeni:** Proje sahibi Can. Kodu ChatGPT yazar. Claude danışmandır: ChatGPT'nin çıktılarını inceler, geri bildirim verir. ChatGPT her değişikliği aşağıdaki "Teslim biçimi" bölümüne göre teslim etmelidir.

---

## 1. Oyun ne?

Tarayıcıda oynanan, gerçekçi görünümlü bir hava savunma / füze harekâtı strateji oyunu. Dil Türkçe.

- **Harita:** Gerçek uydu fotoğrafı hissi veren kıyı coğrafyası (İskandinav: granit, çam ormanı, adalar, akşam güneşi). Uzaktan harita fotoğrafı görünür; yaklaştıkça zemin gerçek ölçekli fotoğraf dokularına, tesisler gerçek boyutlu fotoğraflara geçer. En uzakta askerî semboller kullanılır.
- **Akış:** 2 dakika hazırlık (radar, hava savunma, rampa kurulur; kimse ateş etmez), ardından 15 dakika harekât.
- **Para:** Tesislerden (şehir, rafineri, santral…) gelir. Hasar alan tesis daha az kazandırır.
- **Savunma katmanları:**
  - Radar: iz verir, ufuk sınırı vardır.
  - Yakın savunma: top, lazer, önleyici İHA.
  - Kısa ve orta menzil hava savunma.
  - Uzun menzil hava savunma.
  - Üst katman (atmosfer dışı).
  - Elektronik harp.
  - Şişme maket (aldatma).
- **Saldırı:** Balistik, seyir ve hipersonik füze; kamikaze, anti-radar, aldatıcı ve keşif İHA; uçak görevleri (SEAD, süzülen bomba); özel silah tasarımcısı.
- **Ülkeler:** ABD, Rusya, Türkiye, Çin. Her birinin sistem adları ve özellikleri farklı.
- **İki mod:**
  - **Harekât (2 taraf):** Boğaz haritası, 360 × 240 km.
  - **Dörtlü harekât:** Haç biçimli deniz haritası, 300 × 300 km. Oyuncu sol altta, 3 bilgisayar rakip diğer köşelerde. Herkes herkese saldırır; komuta merkezi düşen elenir, sona kalan kazanır. 15 dakika dolarsa en çok hasar verdiren kazanır.
- **Yayındaki adres:** https://silver-garbanzo-k1jt.vercel.app
- **Depo:** github.com/cicdbaby/silver-garbanzo. Ana dala her push edildiğinde Vercel siteyi otomatik yeniden yayınlar.

---

## 2. Teknik yapı

```
index.html        Oyunun tamamı: tek dosya, ~310 KB (HTML + CSS + tek <script> içinde IIFE)
public/img/*.webp Bütün görseller (83 dosya, ~19 MB); sitede /img/ altında yayınlanır
package.json      Sadece Vite (derleme / önizleme)
tools/            Görsel işleme ve test betikleri (Python)
HANDOFF.md        Bu dosya
```

- **Çalıştırma ve yayın:** `npm install` · `npm run dev` · `npm run build` (çıktı `dist/` klasörüne). Vercel derlemeyi kendisi yapar.
- **Çizim düzeni:** Ekranda üst üste iki `<canvas>` var:
  - `#gl` (WebGL2): sadece zemin. Harita fotoğrafı + yakın dokular + su.
  - `#cv` (Canvas 2D): her şey. Tesis fotoğrafları, hava araçları, efektler, semboller, çizgiler.
- **Dünya birimi:** 1 birim = 50 m (`M_U=50`), 1 km = 20 birim (`KMU=20`). `MW`/`MH` haritaya göre değişir: ikili modda 7200×4800, dörtlüde 6000×6000.
- **Kamera:** `cam.z` = ekranda 1 dünya birimi kaç piksel. Değer 0,12 ile 1700 arasında.
- **Kod bölümleri** (index.html içinde `// =====` başlıklarıyla ayrılmış; satır numaraları yaklaşıktır):

| Satır | Bölüm |
|---|---|
| 358 | world: MAPS (duo/quad), setMap, HQPOS, SCOL (taraf renkleri), LAYOUT_W / LAYOUT_Q, qmap, sideOf |
| 392 | catalogs: SITE (savunma sistemleri), PK (vurma olasılıkları), MUN (mühimmat), VAR (varyantlar), NAT (ülkeler), DIFF (zorluk) |
| 505 | terrain: genMap (yükseklik/orman gürültüsü, kabartma katmanı) |
| 622 | state: newGame (taraflar, yerleşim, G durumu), build, buy, income |
| 661 | air objects: balistik/hipersonik yörüngeler, seyir/İHA rotaları, önleyiciler, kill, impact, hurt, eliminate, boom |
| 810 | sensing & intel: sense (iz), engage (otomatik atış), revealLaunch, intel (ELINT) |
| 860 | launch: launch(), sortie, manualEngage |
| 895 | AI: aiThink(s) — her bilgisayar tarafı için ayrı; hedef seçimi kin + zayıflık + rastgelelik |
| 930 | update(dt): ana simülasyon adımı |
| 965 | photographs: IMGKEYS, PADW (her fotoğrafın metre cinsinden genişliği), COMP (tesis = hangi fotoğraflar) |
| 1039 | water: maske (mat görselinden), OCEAN (okyanusa bağlı su), landSpot |
| 1060 | GL zemin shader'ı + uyarlanır çözünürlük (GLQ) + doku ön yükleme |
| 1293 | render(): ana çizim sırası |
| 1638 | sol menzil paneli (taraf/irtifa katmanları) |
| 1670 | hızlı eylem menüsü (düşmana tıklayınca) |
| 1763 | atış konsolu |
| 1902 | danışman |
| 1934 | eğitim |
| 2028 | menüler / bitiş ekranı |
| 2068 | frame döngüsü + DIAG (hata ve takılma raporu) |

- **Taraflar:** `'W'` her zaman oyuncu. İkili modda rakip `'E'`. Dörtlüde `['W','N','E','S']`. Oyuncu açısından "düşman" demek `side!=='W'`. Taraf başına durumlar `G.cash`, `G.stock`, `G.trk`, `G.ghost`, `G.score`, `G.icp`, `G.ai`, `G.grudge`, `G.suf` altında tutulur; döngüler `G.sides` üzerinden kurulur.
- **Test kancası:** `window.__gok` → `{G, update, render, startGame, cam, build, buy, launch, …}`. Headless testler bununla yapılır.

---

## 3. Görseller ve hattı

**Kod adları** (dosyalar `public/img/<kod>.webp`):

| Kod | İçerik |
|---|---|
| m0 / m0s / mat | İkili mod harita fotoğrafı / minimap / malzeme maskesi. Maske kanalları: R=su, G=orman, B=kaya |
| m4 / m4s / mat4 | Dörtlü mod haritası. 3000 px; GPT'nin çizdiği 4 yüksek detaylı çeyrek orijinal düzene hizalanıp harmanlandı (`tools/merge4.py`). Maske `tools/mat4.py` ile çıkarıldı |
| g1–g4 | Yakın zemin dokuları, 80 m kare, gerçek ölçek: g1 çakıl, g2 fundalık, g3 granit, g4 orman. Araç fotoğraflarıyla aynı kamera ve ışıkla çizdirildi |
| g5 | Deniz (120 m) |
| g0 | Mikro doku |
| g10 / g12 / g13 | Orta yakınlık dokuları |
| b1–b9 | Tesis fotoğrafları |
| k1–k5 | Şehirler |
| c1n + ra/rb | Radar gövdesi + dönen anten ön/arka yüzü. Anten kodla döndürülür ve radar taramasıyla eşzamanlıdır |
| c2–c12 | Diğer savunma sistemleri ve rampalar |
| c10e | Füzesi atılmış boş rampa |
| d1–d9 | Hava araçları |
| e1–e5 | Krater ve patlama |
| s1–s4 | Duman |
| w1–w4 | Enkaz |

- **Kurallar:**
  - Tesis ve araç görseli = kendi zemin pediyle tek kare, yeşil (#00FF00) fon. `tools/isle.py` yeşili alfa kanalına çevirir.
  - Güneş sağ altta, alçakta; gölgeler sol üste düşer; akşam ışığı.
  - Yazı, işaret, insan yok.
- **Görsel promptları:** `tools/menzil_promptlar_v2.md`. Görseller Can tarafından ChatGPT'de çizdiriliyor; Masaüstünde `menzil-gorseller` klasöründe duruyor.

---

## 4. Alınan kararlar ve nedenleri

- **Gerçek uydu görüntüsü (Google Photorealistic 3D Tiles) denendi ve bırakıldı.** Her açılışta canlı veri çekip ücretlendiriyor; Google'ın kuralları indirip çevrimdışı kullanmaya izin vermiyor. Kendi görsellerimizle çalışıyoruz; oyun internetsiz ve ücretsiz çalışır.
  - Vercel'de `VITE_GOOGLE_MAPS_API_KEY` diye bir ortam değişkeni kaldı. Artık kullanılmıyor; silinebilir.
- **Artifact (claude.ai) bırakıldı.** Donma ve kararma sorunları yüzünden oyun Vercel'de yayınlanıyor.
- **Asker/insan figürü yok.** Can istemedi; kod hâlâ duruyor ama çağrılmıyor.
- **Gemi yalnızca okyanusa bağlı suda olabilir.** Göl ve iç suda gemi yok (`OCEAN`).
- **Ölçek tutarlılığı en önemli görsel kural.** Yakın dokular asla büyütülmez. Eskiden 4 kat büyütme vardı; ağaçlar kaya gibi görünüyordu, kaldırıldı.
- **Taktik görünüm:** Radar ekranı gibi; ateş/duman yok, sadece işaretler.
- **Arayüz:** Koyu, minimal, "AI yapımı gibi durmayan" premium görünüm. Çocuksu öğe yok.

---

## 5. Açık sorunlar (öncelik sırasıyla)

1. **5–6 saniyelik takılmalar.** Füzeler uçarken, uzaktan bakarken (zoom ≈ 0,23) oluyor.
   - Teşhis kutusu, takılma sırasında oyun kodunun yalnızca 2–3 ms çalıştığını gösterdi; gecikme tarayıcı / GPU tarafında.
   - Tarayıcı ve GPU bilgisi ile Chrome kare dökümü (long-animation-frame) rapora eklendi; yeni rapor bekleniyor.
   - Kesin bilinenler:
     - JS mantığı ucuz: update ~0,5 ms, render ~1,5 ms.
     - Her karede canvas filtresi kullanmak takılma yaratıyordu, kaldırıldı.
     - NaN değerli bir radial gradient oyun döngüsünü öldürüyordu; düzeltildi ve döngü try/catch ile korundu.
   - Şüpheliler:
     - Canvas2D'nin retina çözünürlüğünde (DPR 2) tam ekran çizilmesi.
     - Büyük duman sprite'ları.
     - `globalCompositeOperation='lighter'` ile çizilen gradient'ler.
     - Safari'ye özgü davranış.
2. **Bilgisayar rakiplerin temposu yavaş.** Dörtlüde 6 dakikada kimse elenmedi. Saldırı aralığı ve paket büyüklüğü ayarlanmalı.
3. **Dörtlü mod cilası.**
   - Rakip izlerinin (track) rengi hâlâ hep kırmızı; taraf rengine geçmeli.
   - Kalan taraf isimlerini gösteren göstergeler eklenmeli.
   - Bitiş ekranı dört sütun için düzenlenmeli.
4. **İkili mod haritası (m0) eski çözünürlükte.** m4'teki dört çeyrek yöntemi m0'a da uygulanabilir.
5. **Sonraki büyük adım (karar Can'da):** İnternetten gerçek oyuncularla çok oyunculu mod. Bunun için sunucu, eşleştirme ve hile koruması gerekir.

---

## 6. Can'ın tercihleri (çok önemli)

- **İletişim:**
  - Türkçe, sıcak ve doğrudan konuş.
  - İngilizce kelime en fazla %2–3 olsun; kullanırsan anlamını parantezde ver.
  - Uzun açıklama değil, sonuç.
  - Ahlak dersi ya da gereksiz uyarı yok.
- **Teslim:** "Şunu yapabilirim" diye teklif etme, yap. Bitince ne değiştiğini kısa söyle.
- **Görsel çıta:** Çok yüksek: ultra gerçekçi, Google Earth hissi, gerçek ölçek, tutarlı ışık.
- **Görsel üretimi:** Görsel gerekiyorsa ChatGPT'de çizdirilecek İngilizce promptu hazırla. Kod adlarıyla dosya isimlendir.

---

## 7. Teslim biçimi (ChatGPT için kural)

Her değişiklik için:
1. **Amaç:** Tek cümle.
2. **Kod değişikliği:** `index.html` içinde **bul / değiştir blokları**. Eski metni birebir ver, yeni metni ver. Dosyanın tamamını baştan yazma; dosya 310 KB ve kısaltmalar kod kaybettirir.
3. **Test:** Nasıl doğrulandığı. Headless Chromium ile `tools/fuzz.py` benzeri bir betik çalıştırılmalı: `pageerror` olmamalı, `window.__gok` ile simülasyon ilerletilmeli.
4. **Riskler:** Neyi bozabileceği.

**Dikkat edilecek tuzaklar:**
- **frame() döngüsü:** try/catch içinde. Yeni kod hatayı yutmasın; `diagErr` ile raporlasın.
- **Canvas filtreleri:** `ctx.filter` her karede kullanılmaz; önceden işlenmiş kopya kullanılır (`tinted()`).
- **Efekt boyutları:** Hem dünya biriminde hem piksel tabanıyla verilir: `Math.max(gerçek, px(n))`. Yakın zoomda gerçek boyuta inmeleri için `fxK()` kullanılır.
- **Taraf mantığı:** Yeni kodda `'E'` sabit yazılmaz. Taraf `e.side` / `gS(g)` / `FOE()` / `G.sides` üzerinden alınır.
- **Shader:** Uzak zoomda (`fm>.999`) pahalı dallara girilmez. GL çözünürlüğü `GLQ` ile uyarlanır.

---

## 8. Araçlar

- `tools/isle.py`: Yeşil fonlu görselden alfalı webp üretir.
- `tools/mat4.py`: Harita fotoğrafından su/orman/kaya maskesi çıkarır.
- `tools/merge4.py`: Dört yüksek detaylı çeyreği orijinal haritaya hizalar (ECC) ve harmanlar.
- `tools/srv.py` + `tools/fuzz.py`: `dist/` klasörünü yerelde sunar. Rastgele tıklama, tuş ve ateşleme ile iki modu oynatıp hata arar. Playwright + Chromium (swiftshader) gerekir.

## GÖREV 4 + 5 (Claude, doğrudan uygulandı)
- Menzil paneli: dolgu alfa .2, kesikli kenar 1.6 px, radar görüşü rengi açık gri-beyaz (denizden ayrışır), panel 192 px, özet panelin içinde, "yok" kısa etiket (tam metin title'da).
- Deneysel sınıf (`VAR.XP`, sekme "Deneysel"): `EMP`, `GRAF`, `MOTH`, `BAL`; hepsi `proto:1`, fırlatmada %12 arıza (`PROTO_FAIL`, `failAt` → `protoFail`).
  - EMP: çarpışmada 6 km (`emp:120`) içindeki düşman sitelerine `empT` (30 sn) → sense/engage/jammedAt/launchersFor/powerDefense bunları yok sayar.
  - GRAF: `grafBurst` → varlıklara `blackT` (60 sn, gelir ×.2, gece ışığı yok); PWR vurulursa `G.blackS[side]` (taraf geliri ×.85, kasaba ışıkları söner).
  - MOTH: yolun yarısında `motherSplit` → 8 DRN.
  - BAL: yeni `kind:'balloon'`, 30 km irtifa, 120 sn loiter, 800 u (40 km) keşif; yalnızca LRAD vurur (PK .75).
  - YZ ara sıra satın alır; paketin başına koyar (rampaları önce onlar alır).
- GÖREV 5: `</style>` öncesindeki "v5" bloğu oyun içi arayüzü ana menü diline çeker (düz yüzey, köşe 0, gölge yok, mono başlıklar, tek soluk vurgu, kırmızı sadece tehlike). Sınıf adları ve data-* değişmedi.

## GÖREV 6 (Claude, doğrudan uygulandı)
- HD harita: GPT'nin 6 karosu = duo haritasının batı yarısı (2×3). SIFT+homografi ile hizalandı (kalıntı <1 px), m0'ın düşük frekans tonuna eşitlendi → `public/img/m0hw.webp` (2497×3139, m0 piksel x 0–1086 × 2.3). Shader: `tH`, `uHR`, `uHd`; açılıştan 1,5 sn sonra tembel yüklenir, menüdeyken GPU'ya `preHD` ile yüklenir. GLMAX<3200 ise devre dışı. Doğu yarısı ve quad için aynı yöntem (araç: scratchpad warp.py/finish.py mantığı).
- Kamera: `VPAD` (konsol/ray/tehdit paneli payları), `camAxis`, contain `minZ`; `fitAll()` (F / #fitbtn), `camTick` tween, minimap görünür alana ortalar. Uzak zoom'da tesis adları gizli.
- Menzil: `DENS` satırı (yoğunluk; R=önleyici, G=radar, B=bilinen düşman sayımı, 1/3 çözünürlükte), lejant, `#dens-tip`. Uydu görünümünde seçili irtifa halkası `LIFT(h)` kadar yukarıda; silah kubbeleri tel kafes (`paintDomes`).
- Uluslar: `NAT.IL`; `NPROF` 6 eksen (toplam 19), `AXF/axV/axOf`; costOf, rngOf, sensOf, pk, dolum, CEP, manevra, seyir hızı/RCS, İHA EH dayanımı, keşif süresi, uydu bekleme bunlardan türer. Eski cost/cheap/pk/range/evade/ew alanları artık kullanılmıyor. YZ `aiBuildList` + stok ağırlıkları. Denge (Orta, YZ×YZ, taraf değişimli 87 maç): US %50, RU %58, TR %52, CN %50, IL %40.
- İHA: DLN silahlarında `.gcs` yer kontrol paneli (GÖREVİ YÜKLE → KALKIŞ, Enter/Esc), `gcsLaunch()`; füzelerde eski kapak/düğme.
- Ses: reverb (sentetik dış mekân IR), mesafe low-pass + gecikme, yeni sentezler (patlama katmanları, çatırtılı roket, CIWS, iki zamanlı İHA motoru, jet geçişi), ortam (rüzgâr + yakındaki İHA uğultusu). `public/sfx/manifest.json` ile kayıtlı ses dosyaları sentezin yerine geçer: {"boom":["boom1.ogg",...]}.
