# Menzil · Gök — GÖREV 6

Ekteki `menzil_proje.zip` oyunun **şu anki canlı hâli** (commit 37a97ab). Önce `HANDOFF.md`'yi oku; GÖREV 4–5 orada özetli. Tek dosyalık oyun `index.html`, görseller `public/img/`.

Teslim biçimi her zamanki gibi:
1. `GOREV6_BUL_DEGISTIR.md` — her değişiklik için birebir BUL / DEĞİŞTİR blokları; BUL metni dosyada tek bir yerde geçmeli.
2. Değişikliklerin uygulanmış tam `index.html`.
3. Yeni görseller ve betikler ayrı dosyalar olarak, nereye konacağını yazarak.

Kurallar (değişmedi):
- Sınıf adlarını ve `data-*` özelliklerini koru.
- Yeni arayüz parçaları GÖREV 5'teki "v5" diline uymalı: düz yüzey, köşe 0, gölge yok, mono küçük büyük harf başlık, tek soluk vurgu (#a9c3c6), kırmızı yalnızca tehlike için.
- Kare başına yeni ağır iş ekleme. Pahalı çizimleri önbelleğe al, yalnızca girdi değişince yeniden üret. `ctx.filter` kullanma.
- `window.__gok` test kancasını bozma. Yeni fonksiyonları oraya ekle.

---

## 1 · Tek tuşla tüm harita

**Sorun:**
- `camClamp()` içinde `cam.minZ = max(CW/MW, CH/MH)`. Bu yüzden harita ekranı "kaplar", hiçbir zaman tamamı görünmez.
- Alt sınır `MH-hh+20`. Konsol (`--conH`) haritanın altını örtüyor; oyuncu kendi bölgesinin en altını göremiyor.

**İstenen:**
- Sol rayda, `#rng` panelinin hemen üstünde `#fitbtn` düğmesi olsun: "TÜM HARİTA", kısayolu `F`.
- İlk basış: kamera 0,35 sn'lik yumuşak geçişle haritanın tamamını gösteren zoom'a gider (contain, kenarlarda boşluk kalabilir). Önceki kamera hatırlanır.
- İkinci basış (ya da `F`): önceki kameraya döner. Düğme açıkken `.on` durumunda olsun (beyaz zemin, siyah yazı).
- Contain zoom'da harita dışında kalan alan düz `#060708` olsun. Shader'ın `far` dalı ve Canvas2D katmanları dünya dışını boyamamalı ya da tekrar etmemeli.
- `minZ` artık `min(CW/MW, CHvis/MH) * 0.96` olsun. `CHvis = CH - konsol yüksekliği` (konsol açıksa).
- Kaydırma sınırları ekranda açık duran panelleri hesaba katsın. Dünyanın her kenarı şu panellerin dışına, 24 px boşlukla getirilebilmeli:
  - alt: `--conH`
  - sol: `#rng` genişliği + 12 px (panel küçültülmüşse daha az)
  - sağ: `#threats` görünüyorsa onun genişliği
- Minimap tıklaması, kamerayı konsolun üstünde kalan görünür alanın ortasına göre ortalasın.
- Fare tekerleği ile en uzağa çıkınca da aynı contain zoom'a varılabilsin.

**Kabul ölçütü:**
- 1280×720 ve 1920×1080'de, konsol açıkken iki harita (duo, quad) için de oyuncunun kendi bölgesindeki her tesis ekranın görünür kısmına getirilebiliyor.
- `F` iki kez basınca kamera aynı yere dönüyor.

## 2 · Harita netliği (görsel üret + yükleyici yaz)

**Gerçek durum:**
- `m0.webp`: 2048×1365 px, 360 km'yi kaplıyor (piksel başına ≈176 m).
- `m4.webp`: 3000×3000 px, 300 km'yi kaplıyor (piksel başına ≈100 m).
- Yakınlaşınca bulanıklık bundan geliyor. Uzaktaki dokular (g1–g5) bunu kapatamıyor.

**Hedef:** Oyuncunun en çok baktığı yakın zoom'da (1 ekran ≈ 20–60 km) piksel başına ≈40 m.

**Yöntem:** karo karo yeniden çizim.
1. `tools/tile_cut.py` yaz. Haritayı örtüşmeli karolara böler:
   - duo için 4×3 = 12 karo;
   - quad için 4×4 = 16 karo;
   - her karo kendi alanının %12'si kadar komşusuna taşar;
   - her karo 1024 px'e ölçeklenip `tiles/<map>/r<row>c<col>.png` olarak yazılır, yanına bir `manifest.json`.
2. Her karoyu kendi görsel üretme yeteneğinle **giriş görseli olarak kullanıp** 2048×2048 (ya da karonun oranında) yeniden çiz. Her karoda şu prompt kullanılsın:

   > Redraw this exact satellite tile at 2048 px with real high-resolution detail. Keep every coastline, lake shape, river, road, field boundary, forest edge and town footprint in exactly the same position and shape — this tile must line up with its neighbours pixel for pixel. Nordic late-afternoon light, low sun from the south-west, muted natural colors matching the input; no haze, no text, no labels, no vignette, no borders, no new objects. Top-down orthographic view.

   Karoların hepsi aynı sohbette, sırayla üretilsin. İlkinden sonra her birine şu cümle eklensin: "Match the previous tile exactly in color grade, sun direction and texture scale."
3. `tools/tile_merge.py` yaz:
   - üretilen karoları geri hizalar;
   - kaymayı düzeltir (her karo, kaynak karonun küçültülmüş hâliyle faz korelasyonu ya da ORB ile hizalanır; ±%3 ölçek, ±2° açı);
   - örtüşen bantlarda 64 px'lik yumuşak geçişle birleştirir;
   - renkleri kaynak haritanın ortalama ve sapmasına eşitler;
   - çıktı: `public/img/hd/<map>/r<row>c<col>.webp` (kalite 82, her biri en fazla ≈900 KB).
4. `index.html` tarafında:
   - HD karolar **yalnızca yakın zoom'da ve ekranda görünen karolar için tembel (lazy) yüklensin**. Açılış süresi değişmesin.
   - Shader'da `uWorld` koordinatıyla karo seçimi yapılsın. En fazla 6 karo aynı anda GPU'da tutulsun (LRU).
   - Karo yüklenene kadar mevcut `m0`/`m4` gösterilsin; karo gelince 0,3 sn'de belirsin.
   - `webglcontextlost` geri dönüş yolu ve düşük donanımdaki GLQ ayarı korunsun.
   - Karo yoksa (dosya eksikse) oyun hatasız eski hâliyle çalışsın.
5. Bu tek seferde bitmezse önce yalnızca duo haritasının **oyuncu tarafındaki (batı) yarısını** yap ve kodu karo eksik olsa da çalışacak şekilde teslim et.

**Kabul ölçütü:**
- Yakın zoom'da kıyı, yol ve tarla sınırları keskin.
- Karo dikişleri 1 ekran genişliğinde fark edilmiyor.
- Açılış süresi en fazla %10 uzuyor.
- Karolar kapalıyken FPS düşmüyor.

## 3 · Taktik görünümde katmanlı radar/savunma yoğunluğu

**Şimdiki durum:** `tacRanges()` her bataryaya ayrı çember ve .025 dolgu çiziyor. Üst üste binen yerler okunmuyor.

**İstenen:**
- Taktik görünümde (ve uydu görünümünde menzil katmanı açıkken) **seçili hedef irtifasında** (`RALT[RG.ai]`, `reachAt`) bir noktayı kaç sistemin koruduğunu gösteren yoğunluk katmanı.
  - 1 sistem: çok açık.
  - 2 sistem: belirgin.
  - 3 sistem: güçlü.
  - 4 ve üstü: en koyu ve hafif tarama dokulu.
  - Renk tek ton (#a9c3c6 ailesi), yalnız opaklık ve tarama artar. Düşman bilinen savunmaları için aynı katman kırmızı tonla ve ayrı.
- Radarlar (görüş) ile önleyiciler (vuruş) ayrı sayılır. Bir nokta "görülüyor ama vurulamıyor" ise kesikli tarama, "vuruluyor ama radar yok" ise noktalı tarama alsın. Bu, mevcut `powerDefense` mantığıyla tutarlı olmalı.
- Performans:
  - Katmanı dünya koordinatında, en fazla 512 px'lik ekran dışı bir kanvasta üret.
  - Her sistemi bu kanvasa `lighter` modunda sabit küçük alfa ile çiz, sonra bir kez `getImageData` ile sayıyı renge çevir.
  - Sonucu `rangeCache` gibi önbellekle; yalnızca site listesi, irtifa ya da görünüm değişince yenile. Kamera kaydırması yeniden üretim gerektirmesin; dünya koordinatında olduğu için sadece `drawImage` ile konumlanır.
- `#rng` paneline "YOĞUNLUK" satırı eklensin (aç/kapa). Altına küçük bir lejant konsun: `×1 ×2 ×3 ×4+`.
- İmleç bir noktanın üstünde dururken `#selection-label` benzeri küçük etiketle "×3 · 2 radar" yazsın. Hesap hafif olmalı, 10 Hz yeter.

**Kabul ölçütü:**
- 20 bataryalık bir savunmada katman açıkken FPS kaybı %5'i geçmiyor.
- İrtifa kaydırıcısı değişince katman 100 ms içinde güncelleniyor.

## 4 · İsrail'i ekle

- `NAT.IL`: ad "İsrail".
- `trait`: Katmanlı savunmada dünyanın en sık denenmiş ağı; keşif ve sensörde çok güçlü; kamikaze ve anti-radar İHA'da ileri; balistik saldırısı sınırlı ve pahalı.
- `names` (kamuya açık gerçek adlar):

  | Anahtar | Ad |
  |---|---|
  | RAD | EL/M-2084 |
  | SHORAD | Demir Kubbe |
  | MRAD | Davud'un Sapanı |
  | LRAD | Arrow 2 |
  | UPPER | Arrow 3 |
  | LASER | Demir Işın |
  | CIWS | Kurgusal yakın savunma (gerçek kara CIWS'i yok, adı "Yakın savunma topu" kalsın) |
  | IDR | Önleyici İHA |
  | EW | EW Birliği |
  | DRN | Hero-120 |
  | ARMD | Harop |
  | MALD | Aldatıcı İHA |
  | RCN | Skylark |
  | CM | Delilah |
  | BM | LORA |
  | HGV | Kurgusal ad, sonuna "(prototip)" |
  | FTR | F-35I Adir |
  | ICP_SHORAD | Tamir |
  | ICP_MRAD | Stunner |
  | ICP_LRAD | Arrow 2 |
  | ICP_UPPER | Arrow 3 |

- Ulus seçim ekranına (`.ts-nat`) eklensin. Dört kişilik modda rastgele rakip havuzuna girsin. `SCOL` / `SHEX` taraf renkleri değişmez; renk ulusa değil tarafa bağlı.
- `SPEC`'te İsrail'e özgü ad farkları için ek gerekmez; mevcut tablo kullanılsın.

## 5 · Uluslar her alanda eşit olmasın — açık güç profili

**İstenen:** Her ulusun 6 eksende 1–5 arası puanı olsun. Toplamlar eşit (her ulus 19), dağılım farklı. Bu puanlar mevcut `cost` / `cheap` / `pk` / `range` / `evade` / `stealth` / `ew` alanlarının **yerine** tek bir tablodan türetilsin.

| Eksen | US | RU | TR | CN | IL |
|---|---|---|---|---|---|
| Balistik | 3 | 5 | 3 | 5 | 2 |
| Seyir + hipersonik | 4 | 4 | 2 | 4 | 3 |
| İHA | 3 | 3 | 5 | 2 | 4 |
| Hava savunma | 4 | 4 | 3 | 3 | 5 |
| Sensör + keşif | 3 | 1 | 2 | 2 | 4 |
| Elektronik harp | 2 | 2 | 4 | 3 | 1 |

(Toplamları kendin kontrol et ve eşitle; tablo yön göstermek için.)

**Eksenin oyun etkisi:** puan 3 nötr, her puan farkı yaklaşık %8. Uç değerler oyunu bozmasın.
- **Balistik:** BM / GRAF fiyatı, CEP ve son evre manevrası.
- **Seyir + hipersonik:** CM / HGV / EMP fiyatı, hız ve radar kesit alanı.
- **İHA:** DRN / ARMD / MOTH / JAM fiyatı, sürü boyu ve EH'ye dayanım.
- **Hava savunma:** HS bataryalarının PK'sı, şarjör ve dolum süresi.
- **Sensör + keşif:** radar menzili, RCN / BAL süresi, uydu bekleme süresi.
- **Elektronik harp:** EW yarıçapı ve karıştırma etkisi.

**Görünür olsun:** Ulus seçim ekranında her ulusun altında 6 eksenli küçük çubuk tablo. Rakam yok, 5 bölmeli çubuk; v5 dili. Bilgi kartında ve güç barometresi detayında da aynı çubuklar dursun.

**YZ ulusunun güçlü yanına göre oynasın:**
- RU / CN balistik ağırlıklı paket kurar.
- TR İHA sürüsü ve EH kullanır.
- IL ve US savunmaya daha çok yatırır.
- `AI_BUILD` ve paket ağırlıkları bu tablodan türesin.

**Denge testi:** `__gok` üzerinden başsız bir betikle her ulus çiftini (Orta zorluk, YZ'ye karşı YZ, `autoW`) 10'ar maç oynat. Kazanma oranları %35–65 dışına çıkan ulus varsa çarpanları ayarla. Sonuç tablosunu teslim notuna yaz.

## 6 · İHA fırlatmada dijital panel

**Sorun:** İHA ailesindeki silahlarda da (DLN rampalı her şey: DRN*, ARMD, JAM, RCN, MALD, MOTH, BAL) füze gibi emniyet kapağı kaldırıp kırmızı düğmeye basılıyor. Bu yanlış: İHA bir yer kontrol istasyonundan göreve yüklenip kaldırılır.

**İstenen:** `C.w` İHA ailesinden bir silahsa 4. sütunda (`.fc` / `#cC`) emniyet kapağı ve kırmızı düğme yerine bir **yer kontrol paneli** (`.gcs`) çıksın. Füzeler için mevcut kapak ve düğme aynen kalır.
- **Üstte durum satırları** (mono, tablo hizalı):
  - hazır rampa sayısı / toplam;
  - seçili adet;
  - tahmini varış (`flightTime`);
  - rota: düz ya da dolambaçlı (`routeAround` ya da kullanıcı ara noktası);
  - EH riski: hedef bölgede bilinen EW varsa "yüksek".
- **Altta iki adımlı tek düğme:**
  1. "GÖREVİ YÜKLE": rota ve adet kilitlenir.
  2. Düğme "KALKIŞ" olur, tek tıkla fırlatır. Basılı tutmak gerekmez.
- Esc ya da hedef değişince 1. adıma döner. `Enter` kısayolu çalışsın.
- Kalkışta kısa bir "KALKTI · 6/6" geri bildirimi, ardından panel boşa döner.
- Görünüş: düz koyu yüzey, ince çizgi, yeşil yok. Hazır durumu soluk vurgu rengiyle. Kırmızı yalnızca "rampa yok" ya da "kasa yetersiz" uyarısında.
- `FCS.armed`, `holdStart`, `doFire` gibi mevcut akış füzeler için değişmesin. İHA için yeni bir `gcsLaunch()` yaz ve `__gok`'a ekle.

---

## Teslimden önce

- Mevcut fuzz betiğini (`tools/fuzz.py`) iki mod için çalıştır, sayfa hatası 0 olsun.
- Ekran görüntüleri:
  - tüm harita görünümü;
  - yakın zoom'da HD karo ile eski hâlin karşılaştırması;
  - taktik görünümde yoğunluk katmanı;
  - ulus seçim ekranı (çubuklarla);
  - İHA seçiliyken yer kontrol paneli.
- Değişiklik notunda, kabul ölçütlerinin her birini ölçtüğün değerle yaz.
