---
format: 1920x1080
duration: 120s
message: "Kullanılmış ev eşyası muafiyeti üç sayıyla akılda kalır: 24 ay dışarıda, yılda en çok 6 ay içeride, gelişten sonra 6 ay içinde beyan"
arc: concept-explainer (kişiler → karar ağacı → istisnalar → süre → özel akış → kontrol)
audience: GM / GMY sınavına hazırlanan adaylar
mode: collaborative
music: none
language: tr
---

## Video direction

- **palette:** Bold Poster yazı ve çizgi dili, bu videoya özel taşınma zemini: kraft karton (#E6D5B8), üst ve alt kenarda koli bandı şeritleri (#CDB48C). Mürekkep #1C1410; kırmızı dolgu #D8000F (beyaz yazıyla), kırmızı yazı #A8000B; etiketler beyaz kâğıt. 11. sahne tam kırmızı panel; 12. sahne beyaz zeminde logo. Filigran ortada %10, logonun kendi renkleri.
- **motion grammar:** power3.out uzun kuyruklu yerleşme, zıplama yok; parçalar seslendirmede adı geçtiği an gelir; etiketler hafif eğik (−2° / +2°) oturur; karar ağacının dalları SVG çizgi olarak uzar; damgalar tek dönüşlü (−4°).
- **stage:** 2–3 aynı dört koli etiketi; 4–6 aynı karar ağacı (düğüm konumları sabit); 8 zaman çizgisi; 9 akış şeması; geçişlerde sahne kıpırdamaz.
- **rhythm:** 1 merak, 2 dörtlü sayım, 3 gruplama, 4–6 ağaç büyür, 7 damgalar, 8 iki süre, 9 akış, 10 kontrol, 11 üç sayı, 12 imza.
- **negative list:** zıplama/elastik, fotoğraf, gerçekçi ev çizimi, üçüncü vurgu rengi, yuvarlak köşe, gölge (kırmızı panel yazısı hariç); fontta olmayan işaretler SVG; içerik y ≤ 900 px. Yerleşim tools/scenes.py (taslakla ortak), hareket tools/build_frames.py.

## Frame 1 — Kesin dönüş

- scene: Kraft zemin, solda üst üste üç koli (bantlı, "KULLANILMIŞ EV EŞYASI" etiketli). Sağda başlık "Kesin dönüş" ve eğik kırmızı "muaf mı?". Altta künye: "Gümrük Muafiyeti Tebliği (Seri No: 2) · md. 10–16".
- voiceover: "Yurt dışından kesin dönüş yapıyorsunuz. Kolilerdeki kullanılmış ev eşyası, gümrük vergilerinden muaf girebilir mi?"
- duration: 6.84s
- transition_in: cut
- status: animated
- src: compositions/frames/01-kesin-donus.html
- type: hook
- cite: Muafiyet Tebliği (Seri No: 2) md. 10–16

## Frame 2 — Dört kişi

- scene: Dört koli etiketi yan yana, sırayla yapışır: a) 24 AY YURT DIŞI → kesin nakil; b) KAMU GÖREVLİSİ → sürekli görevden dönüş; c) VATANDAŞLIĞA GEÇEN → kesin nakil; ç) MİRASÇI → yurt dışında yerleşik kişinin ölümü. Her etikette büyük harf ve basit simge.
- voiceover: "Dört kişi yararlanır: yurt dışında en az yirmi dört ay ikamet edip yerleşim yerini kesin olarak Türkiye'ye nakleden; yurt dışındaki sürekli görevinden dönen kamu görevlisi; Türk vatandaşlığına geçip yerleşim yerini Türkiye'ye nakleden; ve yurt dışında yerleşik bir kişinin ölümüyle, Türkiye'de yerleşik mirasçıları."
- duration: 18.24s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/02-dort-kisi.html
- type: feature_showcase
- cite: md. 10

## Frame 3 — Aile ünitesi

- scene: Aynı etiketler; a, b, c üstüne kırmızı bir kuşak "AİLE ÜNİTESİ"; altında belge kartı "vukuatlı nüfus kayıt örneği". ç etiketi soluklaşır.
- voiceover: "İlk üç kişide aile ünitesi esas alınır; aile ünitesi, vukuatlı nüfus kayıt örneğine göre belirlenir."
- duration: 6.32s
- transition_in: crossfade
- status: animated
- src: compositions/frames/03-aile-unitesi.html
- type: rule
- cite: md. 11/1-a

## Frame 4 — Altı ay, kırk beş gün

- scene: Karar ağacı açılır. Kök düğüm "Yurt dışında ≥ 24 ay?" (a ve ç'deki ölen kişi). Dal: "Bir takvim yılında Türkiye'de 6 aydan fazla kaldı mı?" Yanında 12 aylık takvim çubuğu: 6. ayda kırmızı çizgi; başta kısa bir dilim "45 güne kadar = yurt dışı sayılır".
- voiceover: "Yirmi dört ay kuralında bir şart daha var: kişi, mirasçılıkta ise ölen kişi, bir takvim yılında Türkiye'de altı aydan fazla kalmamış olmalı. Yılda kırk beş güne kadar kalışlar, yurt dışı ikametten sayılır."
- duration: 12.38s
- transition_in: blur-crossfade
- status: animated
- src: compositions/frames/04-takvim-yili.html
- type: process
- cite: md. 11/1-b

## Frame 5 — On yılda beş yıl

- scene: Aynı ağaç; yandan bir kestirme ok uzanır: "Son 10 yılda ≥ 5 yıl yurt dışı → süre şartı ARANMAZ". Altta küçük çip: "giriş-çıkış kayıtları: elektronik sistem".
- voiceover: "Ama son on yılın en az beşini yurt dışında geçirene bu süre şartı aranmaz. Giriş-çıkış kayıtları elektronik sistemden tespit edilir."
- duration: 8.02s
- transition_in: crossfade
- status: animated
- src: compositions/frames/05-on-yilda-bes.html
- type: exception
- cite: md. 11/1-b, c

## Frame 6 — İkinci kez

- scene: Aynı ağaç; kökten çıkıp geri dönen kırmızı döngü oku: "Tekrar? → yurt dışında YENİDEN ≥ 24 ay".
- voiceover: "Bu muafiyetten bir kez yararlanan, tekrar yararlanmak için yurt dışında yeniden en az yirmi dört ay ikamet etmelidir."
- duration: 6.9s
- transition_in: crossfade
- status: animated
- src: compositions/frames/06-ikinci-kez.html
- type: rule
- cite: md. 11/2

## Frame 7 — Kimler yararlanamaz?

- scene: Üç etiket: "≤ 24 ay GEÇİCİ GÖREVLİ kamu görevlisi" ve "ÇIKMA İZNİYLE Türk vatandaşlığından çıkan" üstüne kırmızı "YARARLANAMAZ" damgası; üçüncü etiket "ÇİFT UYRUKLU" üstünde tik ve "YARARLANIR".
- voiceover: "Kimler yararlanamaz? Yirmi dört ayı aşmayan süreyle geçici görevlendirilen kamu görevlileri. Ve çıkma izni alarak Türk vatandaşlığından çıkanlar. Çift uyruklular ise yararlanır."
- duration: 10.72s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/07-istisnalar.html
- type: exception
- cite: md. 12

## Frame 8 — Ne zaman getirilir?

- scene: İki zaman çizgisi. Üstte "a · b · c": GELİŞ işareti; önce / beraber / sonra 6 AY parantezi. Altta "ç": VERASET İLAMI işareti → 24 AY parantezi. Altta not: "mücbir sebep ve beklenmeyen haller saklı".
- voiceover: "Beyan ne zaman yapılır? İlk üç kişi, gelişlerinden önce, beraberlerinde ya da gelişten sonraki altı ay içinde; mirasçılar, veraset ilamından itibaren yirmi dört ay içinde. Mücbir sebep ve beklenmeyen haller saklıdır."
- duration: 13.84s
- transition_in: blur-crossfade
- status: animated
- src: compositions/frames/08-getirme-suresi.html
- type: process
- cite: md. 13

## Frame 9 — Ülkeden ülkeye atanan

- scene: Akış şeması: KİŞİ → (dilekçe + 4 nüsha liste) → KURUM → (uygun görürse, 3 nüsha) → GÜMRÜK (incele: kullanılmış ev eşyası mı? getirilmesi zorunlu mu?) → onaylı liste örneği → KİŞİ; gümrükten kuruma kesik "bilgi" oku.
- voiceover: "Bir ülkeden başka bir ülkeye sürekli görevle atanan kamu görevlisi, yeni ülkeye götüremediği eşya için de bu hükümlerden yararlanır: dört nüsha listeli dilekçe kurumuna, üç nüsha gümrüğe gider; gümrük inceler ve onaylı listenin bir örneğini kişiye verir."
- duration: 14.96s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/09-ulkeden-ulkeye.html
- type: process
- cite: md. 15

## Frame 10 — Mükerrer kullanım

- scene: Solda "BİLGE" ekran kartı: kişi + aile ünitesi → "mükerrer mi?". Sağda süre bandı içinde üç küçük koli (1. parti, 2. parti, 3. parti) ve damga "MÜKERRER DEĞİL".
- voiceover: "Hak mükerrer kullanıldı mı? Kişi ve aile ünitesi BİLGE sisteminden kontrol edilir. Ama süresi içinde partiler halinde getirmek, mükerrer kullanım sayılmaz."
- duration: 9.56s
- transition_in: crossfade
- status: animated
- src: compositions/frames/10-mukerrer.html
- type: rule
- cite: md. 16

## Frame 11 — Üç sayı

- scene: Tam kırmızı panel; üç dev sayı yan yana: 24 · 6 · 6; altlarında "ay dışarıda", "yılda en çok içeride", "ay içinde beyan".
- voiceover: "Kısacası, üç sayı: yirmi dört ay dışarıda; yılda en çok altı ay içeride; gelişten sonra altı ay içinde beyan."
- duration: 7.92s
- transition_in: blur-crossfade
- status: animated
- src: compositions/frames/11-uc-sayi.html
- type: cta
- cite: md. 10–13

## Frame 12 — Gümrük Koçu

- scene: Beyaz zemin, logo tek ve sakin hareketle oturur; altında @gumrukkocunuz.
- voiceover: "Gümrük Koçu… Ufuk Çetintaş."
- duration: 4.6s
- transition_in: blur-crossfade
- status: animated
- src: compositions/frames/12-kapanis.html
- type: brand
