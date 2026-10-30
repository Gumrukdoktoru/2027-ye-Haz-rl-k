# GM Soru Bankası — Tekrar Taraması Raporu

- **Tarih:** 30 Ekim 2026
- **Kapsam:** GM bankası 94 bölüm, 1.164 soru (`araclar/gm-soru-bankasi/veri/gm_<KOD>.py`). Çapraz karşılaştırma için GMY bankası: 56 bölüm, 1.118 soru (`araclar/soru-bankasi/veri/sb_XX.py`).
- **Araç:** `araclar/gm-soru-bankasi/cakisma_gm.py`. Aday çiftler ve ölçüm değerleri `araclar/gm-soru-bankasi/dogrulama/tekrar_adaylari.json` dosyasında. Soru dosyalarına dokunulmadı.
- **Kimlikler:** GM sorusu `KOD-NN` (ör. `M42-01`). GMY sorusu `SBXX-YY`.

## 1. Yöntem

Betik her soru çiftini altı ölçütle tarar. Bir çift en az bir ölçütü sağlarsa aday olur:

| Ölçüt | Tanım |
|---|---|
| (a) Kanıt | Kanıt alıntıları normalize edilir. Kelime kümeleri en az %80 örtüşürse ölçüt sağlanır. Kısa alıntı en az 6 kelime olmalıdır. |
| (b) Çekirdek | Çekirdek ve doğru cevabın kaba kökleri (ilk 5 harf) IDF ağırlıklı Jaccard ile karşılaştırılır; eşik 0,25. Ayrıca doğru cevaplar difflib ile en az 0,85 benzerse ve kök ile çekirdek Jaccard değeri en az 0,30 ise ölçüt sağlanır. |
| (c) Madde | Mevzuat aynıdır, ortak bir madde numarası vardır (tarifede ortak pozisyon) ve doğru cevap aynıdır. Önermeli cevaplar sayılmaz. Sayısal cevapta yalnız tam eşitlik geçerlidir. |
| (t) Tarife | T bölümlerinde ve M09'da aynı eşya tanımı ile ortak pozisyon kodu bulunur. Bu ölçüt "aynı eşya → aynı pozisyon" durumunu yakalar. |
| (s) Şık | Doğru cevap aynıysa en az 3 ortak şık, değilse en az 4 ortak şık gerekir. |
| (k) Kök | Kök metni difflib ile en az 0,80 benzerdir ve en az 3 şık bulanık eşleşir. Ya da metin cevaplı sorularda doğru cevap en az 0,80, kök en az 0,60 benzerdir. |

Adaylar elle okunup sınıflandırıldı:

- **TEKRAR:** Aynı hüküm aynı yönden sorulur. Doğru cevap aynıdır ya da aynı bendin kardeş unsurudur, çeldirici mantığı da aynıdır. Hesap sorularında formül ve belirleyici tuzak aynıysa tekrar sayılır. Tarifede aynı eşya için aynı pozisyon sorulması da tekrardır.
- **KOMŞU (kabul):** Aynı hüküm farklı yönden sorulur. Örnekler: hesap ile hüküm bilgisi, önermeli soru ile tek hükümlü soru, ikiz kavram ya da bilinçli ayna çift. Yalnız ortak bir kanıt cümlesi, ortak formül cümlesi veya ortak sayısal şık (%10, 10, 84.xx gibi) yüzünden aday olan çiftler de bu sınıfa girer.

## 2. Özet

| | Bölüm içi | Bölümler arası | Toplam |
|---|---:|---:|---:|
| Aday çift | 261 | 263 | **524** |
| TEKRAR | 0 | 11 | **11** |
| KOMŞU (kabul) | 261 | 252 | **513** |

Ölçüt dağılımı şöyledir: a 473, b 84, s 18, k 6, t 4, c 3. Bir çift birden çok ölçütü sağlayabilir.

KOMŞU çiftlerin 420'si yalnız ortak kanıt cümlesi yüzünden aday oldu. Bunların 77'sinde ortak cümle KDV md. 21 matrah cümlesi ya da KDV matrahı formülüdür. 14 çift yalnız ortak sayısal şıklar ya da ortak pozisyon şıkları (%10, 10, 84.xx gibi) yüzünden aday oldu ve hepsi ilgisizdir.

GMY ile çapraz taramanın sonucu:

- **15 birebir benzer** soru var: kök ve doğru cevap aynı, çoğunda çeldiriciler de ortak.
- **3** soru aynı unsuru ters kalıpla soruyor: biri doğru ifadeyi, öteki yanlış ifadeyi arıyor.
- **5** soru yakın benzer: kök ve çeldirici seti aynı, doğru cevap farklı.

Ayrıntı 4. bölümde.

## 3. TEKRAR çiftleri (11)

Hepsi bölümler arası. Bölüm içinde tekrar bulunmadı.

| # | Çift | Ortak hüküm | Neden TEKRAR | Değiştirilmesi önerilen | Gerekçe ve öneri |
|---|---|---|---|---|---|
| 1 | **H02-15 ↔ M61-03** | 3065 KDV md. 21: ithalatta matrahı oluşturan unsurlar | Kök birebir aynı. Doğru cevap aynı ("tescil tarihinden sonra yapılan giderler"). 5 şıkkın 4'ü ortak. | **H02-15** | KDV Kanunu hükmünün asıl yeri M61'dir. H02'de KDV matrahı H02-11 ve H02-14'te zaten hesapla ölçülüyor. H02 başlığında ayrı sorusu olmayan bir unsura geçilmeli, ör. dampinge karşı vergi hesabı. |
| 2 | **H02-13 ↔ M62-06** | 4760 ÖTV md. 11: (III) sayılı listenin (B) cetvelinde matrah perakende satış fiyatıdır | Kök neredeyse aynı (difflib 0,90). Doğru cevap birebir aynı. | **H02-13** | ÖTV Kanunu hükmü M62'nin konusudur. ÖTV matrahı H02'de H02-10'da hesapla, (B) cetveli H03-03'te sigara hesabıyla ölçülüyor. H02 başlığında boş kalan bir unsur seçilmeli. 1 numaralı satırdaki değişiklikle çakışmamasına dikkat edilmeli. |
| 3 | **M09-02 ↔ T01-05** | Gümrük Yönetmeliği md. 32: "bölüm başlığı" tanımı | Kök birebir aynı. Doğru cevap aynı. 5 şıkkın 4'ü ortak. | **M09-02** | GY 32 tanımları T01'in kapsamındadır; T01 başlığı GY 32'yi açıkça sayar. M09'da GK 15–22'den ölçülmemiş bir hüküm seçilmeli (tarife, pozisyon ayırma, menşe). |
| 4 | **T08-11 ↔ T17-02** | Ağırlıkça %15'ten fazla fosfor içeren bakır fosfür 28.53'e girer | Aynı eşya, aynı pozisyon, aynı oran (%15). Biri Fasıl 28 notundan, öteki Fasıl 74 notundan aynı sınırı soruyor. | **T17-02** | Sınır Fasıl 28 notunun asıl hükmüdür. T17-02, Fasıl 74 notunun başka bir unsuruna geçmeli, ör. rafine bakır tanımı ya da kuproalyaj tanımının başka bir öğesi. |
| 5 | **T02-13 ↔ T22-14** | Taşıt için şekil verilmiş çerçevesiz emniyet camı, taşıt parçası olarak değil 70.07'de sınıflandırılır | Aynı eşya sınıfı için aynı pozisyon (70.07) soruluyor; biri hava taşıtı, öteki binek otomobili için. | **T22-14** | T02-13, GYK 3(a) açıklama notunun kendi örneğidir. T22-14'te yön çevrilebilir: çerçeveli ya da ısıtma tertibatlı camın 87.08'de sınıflandırıldığı sorulabilir. Ya da doğru cevap 87.08 dışında kalan başka bir eşya olabilir. |
| 6 | **H01-20 ↔ M10-01** | GK 27: fiyata dahil edilmemiş, alıcının üstlendiği giderlerden gümrük kıymetine eklenenler | Kök kalıbı aynı ("…hangisi gümrük kıymetine ilave edilir?"). Doğru cevaplar aynı bendin kardeş unsurları: ambalaj bedeli ile tek eşya muamelesi gören kaplar. 3 çeldirici aynı: giriş sonrası nakliye-sigorta, finansman faizi, satın alma komisyonu. | **H01-20** | H01 hesap bölümüdür; KAPSAM sorusu M10'un işidir. H01-20 hesap sorusuna çevrilebilir: işçilik ve malzeme dahil ambalaj bedelini içeren bir kıymet hesabı. Ya da kalıp ve çeldirici seti değiştirilmeli. |
| 7 | **H03-22 ↔ M26-01** | GK 133–134, GY 386: kısmi muafiyetli geçici ithalatta serbest dolaşıma girişte toplam vergiden ödenmiş aylık %3'ler düşülür; ay kesri tam ay sayılır | Aynı hesap. Toplam vergi aynı (200.000 TL), çeldirici mantığı aynı (ödenen tutar, gün oranı, hiç düşmeme). | **M26-01** | M26-01 ayrıca GMY SB33-04 ile birebir aynıdır (170.000 TL; 30.000, 200.000 ve 230.000 şıkları ortak). Tek değişiklik iki tekrarı birden kaldırır. Hesap tavan kuralıyla kurulabilir: aylık vergiler toplam vergiyi aşamaz (uzun kalış vakası). H03-21 ve H03-22 bilinçli ikiz olarak kalır. |
| 8 | **H04-04 ↔ M42-01** | GK 234/1-b ve 234/3: kıymet noksanlığında vergi farkının üç katı ceza; kendiliğinden bildirimde ceza yüzde on nispetinde | Aynı hesap yönü ve aynı belirleyici tuzak (%10). H04-04 yalnız fark vergiyi kendisi hesaplatıyor. | **M42-01** | H04 başlığı "kendiliğinden bildirim" hesabını açıkça kapsar. Hüküm H04-04'te ve H04-05'te (6 ay istisnası) iki yönden ölçülüyor. M42'de hesap kotası gerekiyorsa H04'te hesabı olmayan bir hüküm seçilmeli, ör. GK 238 rejim ihlalinde gümrüklenmiş değerin iki katı ya da özel taşıtta vergilerin dörtte biri. GK 241'i 9 numaralı satır kullanıyor; çakışmamasına dikkat edilmeli. |
| 9 | **H04-16 ↔ M21-01** | GY 527: antrepo yaygın götürü teminatı (dilimler, kesrin tamamlanması, %75 indirimin yalnız 5 ve daha fazla antrepoya uygulanması) | Aynı formül, aynı yönden hesap. Kanıtı da M21'in kaynak dosyasından (21-antrepo). | **H04-16** | Antrepo teminatı H04'ün kapsamı dışındadır (fark vergi, ceza, uzlaşma, gecikme zammı). Yerine H04 başlığında olup hesabı bulunmayan bir unsur önerilir, ör. GK 241 usulsüzlük cezası hesabı. |
| 10 | **M14-02 ↔ M24-02** *(sınırda)* | Dahilde işleme izninde temel tekstil hammaddeleri (elyaf, iplik, ham mensucat) kapsam dışı, yardımcı maddeler (tela, düğme, fermuar) kapsam içi | Mevzuat metni farklı (GY 171 sözlü beyan; DİR Tebliği md. 14 izin kapsamı) ama ayrım aynı. Kalıp aynı (KAPSAM_DIŞI). Doğru cevap neredeyse aynı cümle. En güçlü çeldirici (yardımcı maddeler) ikisinde de var. | **M14-02** | İzin kapsamı M24'ün asıl hükmüdür. M14-02'de doğru cevap, GY 171 listesine göre sözlü beyan edilemeyen başka bir eşya yapılmalı. Böylece tekstil ayrımı yalnız M24-02'de kalır. |
| 11 | **M25-06 ↔ M30-04** *(sınırda)* | İndirimli teminatlı belge kapsamındaki ithalatta kısmi teminat iadesi yapılmaz | İki soru da YANLIŞ kalıbında. Doğru cevap aynı yanlış ifade ("…kısmi teminat iadesi yapılır"). | **M30-04** | Kural DİR Tebliğinin (M25) asıl hükmüdür. M30-04'te İhracat Sayılan Satış ve Teslimler Tebliğinin başka bir hükmü yanlışa çevrilmeli, ör. taahhüt kapatmada KDV hariç satış fiyatı yerine "KDV dahil". Kısmi teminat ifadesi sorudan çıkarılmalı. |

Makine için liste (çift, değiştirilecek):

```
H02-15|M61-03 -> H02-15
H02-13|M62-06 -> H02-13
M09-02|T01-05 -> M09-02
T08-11|T17-02 -> T17-02
T02-13|T22-14 -> T22-14
H01-20|M10-01 -> H01-20
H03-22|M26-01 -> M26-01   (GMY SB33-04 ile de birebir)
H04-04|M42-01 -> M42-01
H04-16|M21-01 -> H04-16
M14-02|M24-02 -> M14-02   (sınırda)
M25-06|M30-04 -> M30-04   (sınırda)
```

## 4. GMY bankasıyla birebir ve yakın benzerler

GM talimatı (`talimat_gm.md`, madde 6) şöyle der: "GMY bankasında aynı hüküm aynı yönden sorulmuşsa GM setinde farklı yönden ölç." Aşağıdaki çiftler bu kurala aykırıdır. GMY kitabı basılı olduğu için **değiştirilecek taraf her satırda GM sorusudur.**

### 4.1 Birebir benzer (15): kök ve doğru cevap aynı

| # | GM | GMY | Ortak hüküm | Benzerlik | Öneri (GM tarafı) |
|---|---|---|---|---|---|
| 1 | M03-02 | SB30-10 | YGM Tebliği md. 13: genel antrepoda aynı YGM'nin yapması zorunlu tespitler (AN7, AN8, AN9) | kök 0,98; cevap aynı; 3 ortak şık | Aynı maddenin başka bir yönü ya da başka bir tespit grubu |
| 2 | M05-05 | SB03-10 | GİKY: kısmi teminat antrepo, GKAİ ve geçici ithalatta uygulanır | kök 0,90; cevap 0,97 | Kısmi teminatın başka bir unsuru ya da yönü |
| 3 | M11-05 | SB41-19 | GY 482: dış seferden dönen gemi, 3 ay, uzatma yetkisi gümrük ve muhafaza başmüdürlüğünde | cevap 0,92; 3 ortak şık | Makam yönü GMY'de var; GM'de başka bir unsur seçilmeli |
| 4 | M17-01 | SB19-05 | GK 85, GY 222: basitleştirilmiş usul uygulanmayan demiryolu taşımasında teminat zorunlu | cevap 0,96; 5 şık bulanık eşleşiyor (yalnız "-yla/ile" farkı) | Teminattan vazgeçme ya da kapsamlı teminat yönü |
| 5 | M19-05 | SB24-20 | Havayolu ve denizyolu basitleştirme izni (Seri 5 ve Seri 6): üçüncü ihlalde 30 gün askı | cevap aynı; 3 ortak şık (GM vaka, GMY doğrudan) | Müeyyidenin başka bir basamağı (iptal ya da yeniden başvuru süresi) |
| 6 | M19-06 | SB26-05 | Transit Seri 14 md. 4: YYS sahibine izinli gönderici eşiği 1.375 | cevap aynı; 4 ortak şık | Başka bir statü ya da başka bir eşik |
| 7 | M25-04 | SB31-20 | DİR Tebliği md. 45: süre bitiminden sonraki ihracat belge kapsamında sayılır, usulsüzlük cezasının dört katı alınır | cevap aynı; 3 ortak şık | Aynı maddenin başka bir gecikme basamağı |
| 8 | M26-01 | SB33-04 | GK 133–134: kısmi muafiyet hesabı (200.000 TL toplam, 170.000 TL kalan) | cevap aynı; 5 şıktan 4'ü aynı | 3. bölümdeki 7 numaralı satırla birlikte değiştirilmeli (tavan vakası) |
| 9 | M28-09 | SB34-11 | GY 397: önceden ithalatsız standart değişimde süre HİR beyannamesinin tescil tarihinde başlar | kök 0,88; cevap 0,97; 3 ortak şık | Sürenin uzunluğu ya da teminat yönü |
| 10 | M33-01 | SB38-09 | Muafiyet Tebliği md. 7: vatandaşlığa geçenin taşıt muafiyetinde başvuru süresinin başlangıcı (nüfus kağıdı tarihi) | kök 0,83; cevap 0,89; 3 ortak şık | Başka bir kişi grubu ya da süre uzunluğu |
| 11 | M35-01 | SB37-14 | SBUY md. 32: parlayıcı ve patlayıcı maddeler (özel düzenekle) serbest bölgeye getirilebilir | kök 0,86; doğru cevap aynı içerik; 4 ortak şık | Yasak listesinin başka bir yönü |
| 12 | M38-03 | SB42-14 | Tasfiye Yönetmeliği md. 43: gümrük müşavirleri ihaleye katılamayanlar arasında sayılmamıştır | kök 0,86; cevap aynı; 3 ortak şık | Görevden ayrılanların bir yıllık yasağı gibi başka bir unsur |
| 13 | M38-10 | SB42-16 | Tasfiye Yönetmeliği md. 59: özel yolla tasfiye eşleştirmesi; yanlış eşleştirme aynı (geri dönüştürülebilir eşya – MKE) | kök 0,96; cevap aynı; 4 ortak şık | Başka bir yanlış eşleştirme |
| 14 | M41-07 | SB46-08 | GK 211 ve Tahsilat Tebliği: belgelere aykırı ağırlık, adet ya da kıymet yazımında geri verme talebi kabul edilir | kök 0,68; cevap 0,85; 3 ortak şık | Geri verme şartlarının başka bir unsuru |
| 15 | M43-01 | SB48-03 | GK 242: yanlış makama verilen itiraz süresinde yapılmış sayılır | kök 0,70; cevap aynı | İtiraz süresi ya da merci yönü |

### 4.2 Aynı unsur, ters kalıp (3)

Biri doğru ifadeyi, öteki yanlış ifadeyi arıyor; test edilen unsur aynı.

| GM | GMY | Ortak unsur |
|---|---|---|
| M35-12 | SB37-06 | SBUY md. 25: faaliyet ruhsatı ve ek ruhsat muhasebe kayıtları birleştirilemez |
| M38-08 | SB42-13 | Tasfiye Yönetmeliği md. 41: teslim alınmayan eşyanın satış bedelinin %50'si hizmet karşılığıdır |
| M38-09 | SB42-17 | Tasfiye Yönetmeliği md. 61–63: gümrüklenmiş değeri 250.000 TL'yi aşan eşyanın imha izni |

### 4.3 Yakın benzer (5)

Kök ve çeldirici seti aynı, doğru cevap farklı. Değiştirmek zorunlu değil; aynı kitap ailesinde göze batar.

| GM | GMY | Ortak kalıp |
|---|---|---|
| M21-05 | SB27-02 | GY 329 antrepo tipleri, YANLIŞ kalıbı (kök 0,88; 3 ortak şık) |
| M37-06 | SB40-06 | İl Değerlendirme Komisyonu üyeleri (kök 1,00; 3 ortak şık) |
| M43-12 | SB48-08 | GY 587: ihtilaflı eşyanın çekilme şartları (kök 0,95; 3 ortak şık) |
| M45-05 | SB52-04 | Elkonulan eşya teslim eşleştirmesi (kök 0,94; 3 ortak şık) |
| M38-01 | SB42-05 | GK 177 ve 179: tasfiyelik eşyanın rejime tabi tutulması (3 ortak çeldirici) |

Betiğin işaretleyip elle elenen çiftler:

- **M30-05 ↔ SB31-19:** Mevzuat farklı (VRHİ Kararında 60 gün, DİR Tebliğinde bir ay). İkiz eksendir, KOMŞU.
- **H04-08 ↔ SB47-08:** Yalnız sayısal şıklar ortak. İlgisiz.

## 5. KOMŞU (kabul): 513 çift

### Özellikle bakılan bölüm çiftleri

| Bölüm çifti | Aday | TEKRAR | KOMŞU (öne çıkanlar) |
|---|---:|---:|---|
| M44–M45 | 0 | 0 | Kanun ve uygulama yönetmelikleri ayrı hükümler ölçüyor (akaryakıt numunesi, ikramiye oranı, muhafaza ücreti). Çakışma yok. |
| M47–M51 | 2 | 0 | M47-15 ↔ M51-09: uzun dönem tedarikçi beyanı 1 yılken revize kurallarda 2 yıl; bilinçli ikiz eksen. M47-12 ↔ M51-01: yalnız ortak sayısal cevap (10); hükümler farklı (sonradan kontrolde 10 ay, EUR.1 geçerliliği 10 ay). |
| M10–H01 | 13 | 1 (H01-20) | H01-17 ↔ M10-09 royaltide hesap ile önermeli soru. H01-01, -19, -21, -27 ↔ M10-01 aynı GK 27/28 cümlesinin farklı unsurları. |
| M42–H04 | 17 | 1 (H04-04) | H04-08 ↔ M42-02: yasak eşyada dört kat, hesap ile yanlış ifade. H04-09 ↔ M42-09: noksan kap, hesap ile önermeli. H04-02 ve H04-06 ↔ M42-12: yarı oran, hesap ile müeyyide. |
| M61/M62–H02/H03 | 15 | 2 (H02-13, H02-15) | H02-16 ↔ M62-04: KKDF oranı ve kuru, hesap ile bilgi. H02-18 ↔ M62-03: DİİB'de %0. H02-10 ↔ M62-06: ÖTV matrahı hesabı. H03-04 ve H03-07 ↔ M62-07: asgari maktu, maktu ve nispi vergi. H03-09 ↔ M61-03: teminattaki ÖTV KDV matrahına girer. |
| M09–T01 | 2 | 1 (M09-02) | M09-02 ↔ T01-07: yalnız ortak kanıt cümlesi (GY 32); hükümler farklı (bölüm başlığı, izahnamenin dayanağı). |

### Bilinçli ayna ya da ikiz çiftler (KOMŞU)

- **M50-01 ↔ M51-03 (doğru cevap "Tunus"):** Aynı olgunun iki yönetmelikten görünüşü. M51-03'ün `ayna` alanında işaretli.
- **M01-04 ↔ M44-14 (gümrüklenmiş değer):** GK'daki tanım yanlış ifade kalıbında, 5607'deki tanım addan tanım kalıbında soruluyor. H02-08 de aynı kavramı hesapla ölçüyor.
- **T02-04 ↔ T02-05:** GYK 4 benzerlik etkenleri ile 3(b) mümeyyiz vasıf ölçütleri. Ayna çift.
- **M16-01 ↔ M34-01:** Doğru cevap aynı ("Hariçte işleme rejimi") ama hükümler farklı (GK 79 ve GK 157).
- **M07-14 ↔ M08-11:** Askı ve geri almada yetkili bölge müdürlüğü. Mevzuat farklı (YYS ve OKS), hüküm paralel.
- **M29-04 ↔ M36-06:** Konsinye ihracatta kesin satış için bir yıl. M29-04'te doğru ifade çeldirici, yanlış olan başka bir ifade; M36-06'da aynı ifade doğru cevap.
- **T15-07 ↔ T22-14, T03-15 ↔ T12-01, T06-14 ↔ T21-03:** Eşyalar farklı, pozisyon ya da karıştırılan not farklı. Örnekler: tel takviyeli cam ile taşıt camı; fırça başı ile fırça kılı; tek kullanımlık e-sigara ile şarj edilebilir e-sigara.
- **Ek tarife denetimi:** Eşya Jaccard ≥ 0,25 ve ortak pozisyon koşuluyla daha gevşek bir tarama yapıldı. Yalnız T20-01 ↔ T24-01 (dişçilikte vakum cihazı ile dişçi koltuğu, ikisi de 90.18) ve T12-19 ↔ T18-01 (kauçuklu mensucattan kolan ile vulkanize kauçuktan kolan, ikisi de 40.10) çıktı. İkisinde de eşya ve dışlayan not farklı olduğu için KOMŞU sayıldı. Aday listesinde yer almazlar.

### Bölüm içi (261 çift, hepsi KOMŞU)

Talimat gereği "aynı veriyle çift soru" ikizleri bu gruptadır:

- H01-08 ↔ H01-09 ve H01-27 ↔ H01-28: kıymet ile KDV matrahı
- H02-10 ↔ H02-11: ÖTV ile KDV

H03-21 ↔ H03-22 ve H04-03 ↔ H04-04 ikizleri ölçütlere takılmadı; onlar da KOMŞU niteliğindedir.

Önermeli ile hesap çiftleri (ör. M08-05 ↔ M08-07, H03-12 ↔ H03-13) ve aynı kaynak cümlesinden farklı unsur soran çiftler de KOMŞU sayıldı. Ör. H01'deki 20'yi aşkın kıymet hesabı aynı GK 27/28 cümlelerini kanıt olarak kullanıyor. Bölümler arası M41-05 ↔ H04-15 (gecikme zammı, önermeli ile hesap) da aynı türdendir.

### İzlenecek (TEKRAR değil)

- **H01'in KDV ikizleri:** "Tescil sonrası nakliye KDV matrahına girmez" tuzağı üç soruda belirleyici: H01-02, H01-28, H01-32. Her birinde ayrıca başka bir unsur var (EXW, KDV'li müşavirlik, tahliye ücreti), bu yüzden KOMŞU sayıldı. İstenirse birinde tuzak değiştirilebilir.
- **Kısmi muafiyetli geçici ithalat:** H03-21, H03-22 ve H03-23 üçlüsü. M26-01 değiştirilirken yeni sorunun bu üçlüdeki hükümleri (aylık %3, ay kesri, düşüm) tekrarlamaması gerekir.

## 6. Yeniden çalıştırma

```
python3 araclar/gm-soru-bankasi/cakisma_gm.py            # özet + tekrar_adaylari.json
python3 araclar/gm-soru-bankasi/cakisma_gm.py --liste    # GM adaylarının ayrıntısı
python3 araclar/gm-soru-bankasi/cakisma_gm.py --gmy      # GMY çapraz adaylarının ayrıntısı
```

Düzeltmelerden sonra betik yeniden çalıştırılırsa yukarıdaki 11 TEKRAR çiftinden (b), (c), (k) ve (s) ölçütleri kalkmalıdır. Aynı kaynak cümlesi kullanıldığı için yalnız (a) ölçütü kalabilir. GMY tablosunda değiştirilen GM sorusu artık BİREBİR türünde görünmemelidir.
