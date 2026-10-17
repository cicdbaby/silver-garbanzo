# Menzil · Gök — telsiz anonsları (ElevenLabs)

Oyunda bir olay olunca arkadan telsizden kısa bir anons gelecek: atış yapıldı, hedef vuruldu, tesisimiz vuruldu gibi. Telsiz efektini (cızırtı, dar bant, bas düşmesi) **oyun kendisi ekliyor**; sen temiz ses ürettir.

## Ses ayarı (hepsinde aynı)

- **Model:** Eleven Multilingual v2 (ya da Turkish destekli v3).
- **Ses:** Erkek, 30–45 yaş, Türkçe anadil gibi; sakin, net, askerî telsiz operatörü. Voice Library'de "Turkish military", "news anchor Turkish" ya da "calm narrator Turkish" ara. Hepsinde **aynı sesi** kullan.
- **Ayarlar:**
  - Stability 50
  - Similarity 75
  - Style 15
  - Speaker boost açık
  - Hız 1.05
- **Çıktı:** MP3 44.1 kHz, 128 kbps ya da üstü.
- **Kayıt:** Her satırı ayrı üret. Başta ve sonda en fazla 0,2 sn sessizlik kalsın.
- **Ton:** "acil" yazanlarda sesi biraz yükselt ama bağırtma. v3 kullanıyorsan başa `[urgent]` ya da `[calm]` etiketi koyabilirsin.
- **Çeşitlilik (isteğe bağlı):** Genel satırların bazılarını iki farklı okumayla üretebilirsin (`hit_enemy_1.mp3`, `hit_enemy_2.mp3`); oyun rastgele seçer.

## Dosya adları

Her dosyanın adı aşağıdaki **anahtar** olsun (`war_start.mp3` gibi). Hepsini tek zip'te getir; manifesti ben yazarım.

| Anahtar | Metin | Ton |
|---|---|---|
| `war_start` | Tüm birimlere: harekât başladı. Ateş serbest. | sakin, kararlı |
| `launch` | Atış yapıldı. Füzeler yolda. | net, kısa |
| `drones_launched` | İHA'lar havalandı, hedefe ilerliyor. | net, kısa |
| `hit_enemy` | Hedef vuruldu. Tam isabet. | memnun ama soğukkanlı |
| `hit_partial` | Hedefte isabet var, hasar kısmi. | raporlayan |
| `destroyed_enemy` | Hedef imha edildi. Tekrar ediyorum, hedef imha edildi. | vurgulu |
| `intercepted_all` | Füzelerimiz önlendi. Hedefe ulaşamadı. | düz, hayal kırıklığı belli etmeden |
| `miss` | Atış boşa gitti. Hedef ayakta. | düz |
| `incoming_bm` | Dikkat! Balistik füze tespit edildi! | acil |
| `incoming_hgv` | Dikkat! Hipersonik füze geliyor! | acil |
| `incoming_cruise` | Alçak irtifada seyir füzesi tespit edildi. | gergin |
| `incoming_drones` | İHA sürüsü yaklaşıyor. | gergin |
| `incoming_jet` | Düşman uçağı radarda. | gergin |
| `intercept_ok` | Tehdit önlendi. | rahatlamış |
| `own_hit` | Tesisimiz vuruldu! Hasar tespiti yapılıyor. | acil |
| `own_destroyed` | Tesisimiz yıkıldı. | ağır |
| `battery_lost` | Bataryamızı kaybettik. | ağır |
| `hit_enemy_HQ` | Düşman komuta merkezi vuruldu. | memnun ama soğukkanlı |
| `destroyed_enemy_HQ` | Düşman komuta merkezi imha edildi. | vurgulu |
| `own_hit_HQ` | Komuta merkezimiz vuruldu! | acil |
| `own_destroyed_HQ` | Komuta merkezimiz yıkıldı. | ağır |
| `hit_enemy_REFN` | Düşman rafinerisi vuruldu. | memnun ama soğukkanlı |
| `destroyed_enemy_REFN` | Düşman rafinerisi imha edildi. | vurgulu |
| `own_hit_REFN` | Rafinerimiz vuruldu! | acil |
| `own_destroyed_REFN` | Rafinerimiz yıkıldı. | ağır |
| `hit_enemy_PWR` | Düşman enerji santrali vuruldu. | memnun ama soğukkanlı |
| `destroyed_enemy_PWR` | Düşman enerji santrali imha edildi. | vurgulu |
| `own_hit_PWR` | Enerji santralimiz vuruldu! | acil |
| `own_destroyed_PWR` | Enerji santralimiz yıkıldı. | ağır |
| `hit_enemy_AIRB` | Düşman hava üssü vuruldu. | memnun ama soğukkanlı |
| `destroyed_enemy_AIRB` | Düşman hava üssü imha edildi. | vurgulu |
| `own_hit_AIRB` | Hava üssümüz vuruldu! | acil |
| `own_destroyed_AIRB` | Hava üssümüz yıkıldı. | ağır |
| `hit_enemy_FAB` | Düşman fabrikası vuruldu. | memnun ama soğukkanlı |
| `destroyed_enemy_FAB` | Düşman fabrikası imha edildi. | vurgulu |
| `own_hit_FAB` | Fabrikamız vuruldu! | acil |
| `own_destroyed_FAB` | Fabrikamız yıkıldı. | ağır |
| `hit_enemy_DEPO` | Düşman cephaneliği vuruldu. | memnun ama soğukkanlı |
| `destroyed_enemy_DEPO` | Düşman cephaneliği imha edildi. | vurgulu |
| `own_hit_DEPO` | Cephaneliğimiz vuruldu! | acil |
| `own_destroyed_DEPO` | Cephaneliğimiz yıkıldı. | ağır |
| `hit_enemy_FUEL` | Düşman yakıt deposu vuruldu. | memnun ama soğukkanlı |
| `destroyed_enemy_FUEL` | Düşman yakıt deposu imha edildi. | vurgulu |
| `own_hit_FUEL` | Yakıt depomuz vuruldu! | acil |
| `own_destroyed_FUEL` | Yakıt depomuz yıkıldı. | ağır |
| `hit_enemy_COMM` | Düşman haberleşme merkezi vuruldu. | memnun ama soğukkanlı |
| `destroyed_enemy_COMM` | Düşman haberleşme merkezi imha edildi. | vurgulu |
| `own_hit_COMM` | Haberleşme merkezimiz vuruldu! | acil |
| `own_destroyed_COMM` | Haberleşme merkezimiz yıkıldı. | ağır |
| `hit_enemy_MIL` | Düşman kışlası vuruldu. | memnun ama soğukkanlı |
| `destroyed_enemy_MIL` | Düşman kışlası imha edildi. | vurgulu |
| `own_hit_MIL` | Kışlamız vuruldu! | acil |
| `own_destroyed_MIL` | Kışlamız yıkıldı. | ağır |
| `hit_enemy_CITY` | Düşman yerleşim bölgesine isabet. | raporlayan |
| `destroyed_enemy_CITY` | Düşman yerleşim bölgesi ağır hasar aldı. | ağır |
| `own_hit_CITY` | Şehrimiz vuruldu! | acil |
| `own_destroyed_CITY` | Şehrimiz ağır hasar aldı. | ağır |

Toplam 57 satır. Önce ilk 17 genel satırı üretsen de olur; tesise özel satırlar yoksa oyun genel satırı çalar.
