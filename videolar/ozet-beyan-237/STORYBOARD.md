---
format: 1920x1080
duration: 128s
message: "Özet beyan ile boşaltma listesi tutmazsa: noksan kapta vergi kadar ceza, fazla kapta el koyma ve CIF kadar ceza"
arc: concept-explainer (karşılaştırma → iki dal → istisnalar → sorumlu)
audience: GM / GMY sınavına hazırlanan adaylar
mode: collaborative
music: none
language: tr
---

## Video direction

- **palette:** Bold Poster yazı ve çizgi dili, bu videoya özel liman zemini: lacivert (#0E2640), alt bantta koyu deniz (#0A1D33) ve ince dalga çizgileri. Belgeler (iki liste, kartlar) kırık beyaz kâğıt (#F5F2EF) üstüne mürekkep. Vurgular: EKSİK kırmızı (dolgu #D8000F, lacivert üstünde yazı #FF4A3D), FAZLA kehribar (#FFB21E). 11. sahne tam kırmızı panel; 12. sahne beyaz zeminde logo kendi renkleriyle. Filigran: ortada %10, lacivertte beyaz silüet.
- **motion grammar:** power3.out uzun kuyruklu yerleşme, zıplama yok; her parça seslendirmede adı geçtiği an gelir (kelime zamanları); damgalar tek dönüşlü (−4°); konteyner kapları soldan sırayla yerleşir; eksik kap kesik çizgili boş yuvaya döner, fazla kap kehribar yanıp oturur.
- **stage:** 1–2 aynı iki liste (sol ÖZET BEYAN, sağ BOŞALTMA LİSTESİ, aynı satırlar); 3–4 aynı boş kap yuvası (solda); 5 ve 9 aynı sonuç şeridi (EL KONUR → MÜLKİYET KAMUYA → TASFİYE → + CIF); geçişlerde sahne kıpırdamaz.
- **rhythm:** 1 sahne kurulur, 2 karşılaştırma, 3 sayım, 4 merdiven (en yoğun), 5 sonuç şeridi, 6 gösterge, 7 kısa istisna, 8 madde değişimi, 9 tekrar eden şerit, 10 iki adres, 11 tutulan özet, 12 sakin imza.
- **negative list:** zıplama/elastik, nefes alan kartlar, slayt gibi baştan dökme, fotoğraf ya da gerçekçi gemi; üçüncü vurgu rengi, yuvarlak köşe, gölge (kırmızı panel yazısı hariç); fontta olmayan işaretler (→ ✓ ✗) SVG; içerik y ≤ 900 px. Yerleşim tools/scenes.py (taslakla ortak), hareket tools/build_frames.py.

## Frame 1 — İki liste

- scene: Lacivert gece limanı; altta deniz bandında sade bir gemi silüeti ve üstünde konteyner kapları. Sağda iki kâğıt liste yan yana iner: "ÖZET BEYAN" ve "BOŞALTMA LİSTESİ". Solda başlık: "İki liste tutmazsa…" ve altında "GK md. 237".
- voiceover: "Gemi limana yanaştı. Elimizde iki liste var: özet beyan ve boşaltma listesi. İkisi tutmazsa, Gümrük Kanununun iki yüz otuz yedinci maddesi devreye girer."
- duration: 10.1s
- transition_in: cut
- status: animated
- src: compositions/frames/01-iki-liste.html
- type: hook
- persuasion: Concrete scene
- beat: curiosity
- cite: GK md. 237 · GY md. 75

narrativeRole: Somut sahne: gemi, iki liste, karşılaştırma.
keyMessage: Özet beyan ile boşaltma listesi karşılaştırılır; tutmazsa GK 237.

## Frame 2 — Eksik mi, fazla mı?

- scene: Aynı iki liste büyür; satırlarda kap ikonları. Özet beyanda olup boşaltma listesinde olmayan satır kırmızı "EKSİK" damgası alır; boşaltma listesinde olup özet beyanda olmayan satır kehribar "FAZLA" damgası alır.
- voiceover: "Özet beyanda kayıtlı olup boşaltma listesinde olmayan kap, EKSİK. Boşaltma listesinde olup özet beyanda olmayan kap ise FAZLA."
- duration: 8.32s
- transition_in: crossfade
- status: animated
- src: compositions/frames/02-eksik-fazla.html
- type: concept
- persuasion: Side-by-side comparison
- beat: clarity
- cite: GY md. 75/3

narrativeRole: Eksik ve fazlanın tanımı, iki listenin farkıyla.
keyMessage: Özet beyanda var, listede yok = eksik; listede var, özet beyanda yok = fazla.

## Frame 3 — Noksan kap: kanıt

- scene: Solda kesik çizgili boş bir kap yuvası (kırmızı). Sağda dört sebep kartı sırayla: mahrecinden yüklenmedi · yanlışlıkla başka yere çıkarıldı · kaza / avarya ile yok oldu · çalındı. Altta kum saati: "gümrük idaresince belirlenecek süre". Köşede küçük not: "TIR karnesinde: 3 ay · talep → +3 ay · haklı sebep → +1 ay (TIR Seri No: 6)".
- voiceover: "Noksan kapta, eşyanın mahrecinden yüklenmediği, yanlışlıkla başka yere çıkarıldığı, kaza ve avarya sonucu yok olduğu ya da çalındığı, gümrük idaresinin belirleyeceği süre içinde kanıtlanmalıdır."
- duration: 11.76s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/03-kanit.html
- type: feature_showcase
- persuasion: Numbered enumeration
- beat: orientation
- cite: GK md. 237/1

narrativeRole: Noksanın cezadan kurtulma yolu: dört sebepten birinin süresinde kanıtı.
keyMessage: Dört sebep, idarenin belirleyeceği sürede kanıtlanmalı.

## Frame 4 — Ceza merdiveni

- scene: Boş kap yuvası yerinde kalır; sağda üç basamaklı merdiven yukarıdan aşağı açılır: 1) TARİFE POZİSYONU → gümrük vergileri kadar ceza; 2) POZİSYON YOKSA → faslın en yüksek vergili pozisyonu; 3) O DA OLMAZSA → noksan her kap için 241/1'deki miktar. Her basamakta kırmızı numara.
- voiceover: "Kanıtlanamazsa, eşyanın tarife pozisyonuna göre hesaplanan gümrük vergileri kadar para cezası alınır. Pozisyon tespit edilemiyorsa, dahil olduğu faslın en yüksek vergili pozisyonu esas alınır. Bu da mümkün değilse, noksan her kap için iki yüz kırk birinci maddenin birinci fıkrasındaki ceza."
- duration: 17.14s
- transition_in: crossfade
- status: animated
- src: compositions/frames/04-ceza-merdiveni.html
- type: process
- persuasion: Step ladder
- beat: depth
- cite: GK md. 237/1–2

narrativeRole: Noksanda cezanın üç basamaklı hesabı.
keyMessage: Pozisyon → fasıl en yüksek → her kap için 241/1.

## Frame 5 — Fazla kap

- scene: Solda kehribar renkli fazla kap ve "yanlışlıkla fazla yüklendi mi?" sorusu. Sağda sonuç şeridi soldan sağa dolar: EL KONUR → MÜLKİYET KAMUYA → TASFİYE (md. 177–180) → + CIF KIYMETİ KADAR CEZA (kırmızı damga).
- voiceover: "Fazla kapta ise, yanlışlıkla mahrecinden fazla yüklendiği kanıtlanmalıdır. Kanıtlanamazsa eşyaya el konur, mülkiyeti kamuya geçer, tasfiye edilir; üstelik CIF kıymeti kadar para cezası alınır."
- duration: 12.08s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/05-fazla-kap.html
- type: process
- persuasion: Consequence chain
- beat: tension
- cite: GK md. 237/3

narrativeRole: Fazla kapın ağır sonucu: el koyma + tasfiye + CIF cezası.
keyMessage: Fazla kapta kanıt yoksa eşya gider, üstüne CIF kadar ceza.

## Frame 6 — Dökme eşya

- scene: Dökme yük yığını (tahıl tepesi gibi sade çizim). Yanında yatay gösterge: 0–%3 arası açık bant "TAKİBAT YOK" (oranı eşya cinsine göre Cumhurbaşkanı kararı belirler), ötesi kırmızı. Altta ikinci gösterge: "Doğalgaz ürünleri: ≤ %6 (boru hattıyla ithal hariç)". Küçük not: "takibat yalnızca aşan kısım için (GY md. 75/7)".
- voiceover: "Dökme eşyada, yüzde üçü aşmamak üzere, eşya cinsine göre Cumhurbaşkanı kararıyla belirlenen oranlardaki eksik ve fazlalar için takibat yapılmaz. Doğalgaz ürünlerinde, boru hattıyla ithal edilenler hariç, bu oran yüzde altıyı aşamaz."
- duration: 14.54s
- transition_in: blur-crossfade
- status: animated
- src: compositions/frames/06-dokme.html
- type: data
- persuasion: Threshold gauge
- beat: clarity
- cite: GK md. 237/4 · GY md. 75/7

narrativeRole: Dökme eşyada tolerans sınırları.
keyMessage: Dökmede %3'e kadar (doğalgaz ürünlerinde %6'ya kadar) takibat yok.

## Frame 7 — Kap tamam, ağırlık farklı

- scene: Beş kap yan yana, hepsinde tik; sayaç "5 = 5". Altında bir kantar ekranı "ağırlık farklı". Kırmızı çerçeveli damga: "TAKİBAT YOK".
- voiceover: "Kap adedi tamam, ama sayı, baş ya da ağırlıkta fark var mı? Bunun için takibat yapılmaz."
- duration: 5.7s
- transition_in: crossfade
- status: animated
- src: compositions/frames/07-kap-tamam.html
- type: exception
- persuasion: Quick contrast
- beat: relief
- cite: GY md. 583/2

narrativeRole: Sık sorulan istisna: kap tamamsa ölçü farkına takibat yok.
keyMessage: Kap adedi tamamsa sayı, baş, ağırlık farkına takibat yapılmaz.

## Frame 8 — Belgedeki miktar

- scene: Kâğıt bir rejim beyanı: "miktar: belgelerdeki miktar" satırı; yanında "gümrük tespiti yok" etiketi. Fark ok ile "ÖZET BEYAN EKSİĞİ / FAZLASI" kutusuna akar. Altta iki madde etiketi: "md. 234" üstü çizilir, "md. 237" kırmızı çerçeveyle kalır.
- voiceover: "Miktarı gümrük tespit etmemiş, rejim beyanı belgelerdeki miktara göre yapılmışsa; çıkan fark özet beyan eksiği ya da fazlası sayılır. Ceza gerekirse, iki yüz otuz dördüncü madde değil, yalnızca bu madde uygulanır."
- duration: 13.04s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/08-belgedeki-miktar.html
- type: rule
- persuasion: Swap (234 ✗ → 237 ✓)
- beat: depth
- cite: GK md. 237/5

narrativeRole: Hangi maddenin uygulanacağını netleştirir.
keyMessage: Belgedeki miktarla yapılan beyanda fark özet beyan aykırılığıdır; yalnız 237 uygulanır.

## Frame 9 — Özet beyansız eşya

- scene: Gemide listede olmayan tek kehribar kap. İki tetik etiketi: "gümrükçe belirlendi" ve "boşaltma izninden sonra bildirildi · hiçbir özet beyanla ilişkisi yok". 5. sahnedeki sonuç şeridi aynı yerde tekrar dolar: EL KONUR → MÜLKİYET KAMUYA → TASFİYE → + CIF.
- voiceover: "Taşıtta, hiç özet beyan verilmeden getirilmiş eşya çıkarsa da sonuç aynıdır: fazla yükleme kanıtlanamazsa el koyma, tasfiye ve CIF kıymeti kadar para cezası."
- duration: 10.08s
- transition_in: crossfade
- status: animated
- src: compositions/frames/09-ozet-beyansiz.html
- type: rule
- persuasion: Callback (same chain)
- beat: recognition
- cite: GK md. 237/6

narrativeRole: Özet beyansız eşyayı fazla kapla aynı sonuca bağlar.
keyMessage: Özet beyansız eşya = fazla kap sonucu.

## Frame 10 — Ceza kimden alınır?

- scene: İki adres kartı. Sol: "1., 2., 3. fıkra → ÖZET BEYANI VEREN". Sağ: "6. fıkra → ÖZET BEYANI VERMEKLE YÜKÜMLÜ KİŞİ", altında kesik çizgiyle "tespit edilemezse → EŞYAYI GETİREN".
- voiceover: "Peki ceza kimden alınır? Birinci, ikinci ve üçüncü fıkralarda özet beyanı verenden. Altıncı fıkrada, özet beyanı vermekle yükümlü kişiden; o tespit edilemezse, eşyayı getirenden."
- duration: 11.58s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/10-kimden.html
- type: summary
- persuasion: Two addresses
- beat: closure
- cite: GK md. 237/7

narrativeRole: Sorumlu kişiyi fıkraya göre ayırır.
keyMessage: 1–3 → özet beyanı veren; 6 → yükümlü, yoksa getiren.

## Frame 11 — Kısacası

- scene: Tam kırmızı panel; üç satır: "Noksan → vergi kadar ceza", "Fazla → el koyma + CIF", "Dökme → %3'e kadar takibat yok".
- voiceover: "Kısacası: noksan kapta vergi kadar ceza; fazla kapta el koyma ve CIF kadar ceza; dökme eşyada yüzde üçe kadar farka takibat yok."
- duration: 9.3s
- transition_in: blur-crossfade
- status: animated
- src: compositions/frames/11-kisacasi.html
- type: cta
- persuasion: Three-line recap
- beat: recall
- cite: GK md. 237

narrativeRole: Üç satırlık akılda kalan özet.
keyMessage: Noksan / fazla / dökme.

## Frame 12 — Gümrük Koçu

- scene: Beyaz zemin, logo tek ve sakin hareketle oturur; altında @gumrukkocunuz.
- voiceover: "Gümrük Koçu… Ufuk Çetintaş."
- duration: 4.6s
- transition_in: blur-crossfade
- status: animated
- src: compositions/frames/12-kapanis.html
- type: brand
- beat: signature

narrativeRole: İmza.
keyMessage: Gümrük Koçu - Ufuk Çetintaş.
