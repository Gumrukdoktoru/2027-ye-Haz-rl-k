# GÖREV: GM Soru Bankası bölümü — {KOD} "{BASLIK}" ({SORU} soru)

Gümrük Koçu - Ufuk Çetintaş için Gümrük Müşavirliği (GM) sınavına hazırlık soru bankası hazırlanıyor. Banka iki ciltten oluşur: **mevzuat** (M01–M64) ve **tarife-hesap** (T01–T25 tarife, H01–H05 hesaplama). Sen **{KOD}: {BASLIK}** bölümü için **{SORU}** soru yazacaksın. Bölüm türüne göre aşağıdaki üç profilden yalnız birini uygula: M → Profil A, T → Profil B, H → Profil C.

Bu talimat GMY soru bankası talimatından (`araclar/soru-bankasi/talimat_sablon.md`) uyarlanmıştır. Fark, soru tipi kotalarının 2021–2025 **GM** sınavlarına göre ayarlanması, tarife ve hesap profillerinin eklenmesidir.

## 1. Önce oku (zorunlu)

1. **Prompt 5:** `/home/user/2027-ye-Haz-rl-k/promptlar/prompt-5-gmy-mevzuat-sorusu-hazirlama.md`. Kök, kanıt, gerekçe, çeldirici yuvası, sayısal şık sırası, madde numarası yasağı ve kalite kontrolü bölümleri aynen geçerlidir. Prompt 5'teki GMY tip kotaları yerine bu talimattaki GM kotaları uygulanır. "Tarife pozisyonu sorulmaz" kuralı yalnız Profil A için geçerlidir; Profil B'nin konusu tarife sınıflandırmasıdır.
2. **Prompt 4:** `promptlar/prompt-4-bakanlik-yazar-profili.md` (çeldirici üretimi, ikiz kavram eksenleri). Prompt 4, Prompt 5'in üstüne uygulanır; çelişirse Prompt 5 geçerlidir.
3. **Depo kuralları:** `/home/user/2027-ye-Haz-rl-k/CLAUDE.md`. Kullanıcı tercihleri bağlayıcıdır (bölüm 3).
4. **GM sınav analizi:** `{ANALIZ}/GM-SINAV-ANALIZI.md` (tip dağılımı, alan × tip tablosu, tarife ve hesap kurguları) ve `{ANALIZ}/gm_sorular.csv`. Bölümünün konusunu `alan`, `alt_konu`, `tarife_fasil` ve `hesap_turu` sütunlarında grep'le; çıkmış sorunun metnini gerekirse `/home/user/gm_kaynak/gmcikmislar/GM_SINAVLARI_DERLEMESI.md` içinde bul (yalnız oku; bu klasöre yazma).
   - Bu konunun çıkmış GM sorularındaki bilgi alanlarının **hepsi** setinde ölçülür.
   - Çıkmış soru metni, şık kümesi ve kurgu kopyalanmaz. Aynı bilgi farklı yönden, farklı kalıpla ya da farklı örnek eşyayla sorulur (örnek: çıkmış "ahtapot hangi pozisyonda" → set "deniz kestanesi hangi pozisyonda", şık kümesi de farklı).
5. **Örnek veri:** `araclar/gm-soru-bankasi/veri/gm_M44.py` (Profil A), `gm_T03.py` (Profil B), `gm_H02.py` (Profil C) ve bunların `_rapor.json` dosyaları; hesap doğrulaması için `dogrulama/H02_hesap_kontrol.py`.
6. **Üretim hafızası:** `sorular/hafiza/URETIM-HAFIZASI.md`. Konunu grep'le; GMY bankasında aynı hüküm aynı yönden sorulmuşsa GM setinde farklı yönden ölç.

## 2. Tek bilgi kaynağı

- Bu bölümün kaynağı: `{METIN}/{DOSYA}`. Dosyayı **baştan sona** oku; önce sınav değeri taşıyan bilgi alanlarını çıkar (Prompt 5 bölüm 2).
- `{METIN}/` klasöründeki başka bir dosya ancak aynı hükmü doğrudan düzenliyorsa kullanılabilir (örnek: H02'de KDV matrahı için `61-kdv-kanunu-oranlar.txt`, ÖTV matrahı ve KKDF için `62-otv-kkdf-damga.txt`). Başka bir bölümün konusuna kayma.
- `REF-cikmis-*.txt` dosyaları yalnız örnektir; kanıt olarak kullanılmaz, kopyalanmaz (zaten `{METIN}/` içinde değildir).
- Web araştırması yok; kaynakta olmayan bilgiyle soru, şık ya da gerekçe yok.
- Kaynakta boş kalmış madde numarası ya da silinmiş sayı ("sayılı Kanunun  maddesi", "Ağırlığı .dan az olanlar", "sıcaklığı civarına") **tahminle doldurulmaz**; o hüküm o sayı üzerinden sorulmaz.
- Her soru en az bir birebir alıntıyla kanıtlanır (`kanit="DOSYA.txt | birebir alıntı"`, birden çok alıntı " || " ile). Alıntı karakter karakter kopyalanır; sunum notu kaynaklarında bitişik yazılmış kelimeler de ("HAPİSve") olduğu gibi alınır. Gerekirse "…" ile parçalanır; her parça en az 13 karakter olur.

## 3. Ortak kurallar (CLAUDE.md ve GMY hattından)

- **Kök:** mevzuat adı + hükmün konusu + kurum kalıbı. Kökteki mevzuat türü kaynakla aynıdır (Kanun / Yönetmelik / Tebliğ / Karar). Karar kaynaklı soruda kök kalıbı aynen: `2009/15481 sayılı "4458 sayılı Gümrük Kanununun Bazı Maddelerinin Uygulanması Hakkında Karar"a göre …`. Tarife ve hesap köklerindeki istisna bölüm 5 ve 6'dadır.
- Kökte ve şıkta madde, fıkra, bent numarası yok; tarife sorusunda not numarası da kökte sorulmaz ("4. Fasıl notlarına göre" yazılır, "4. Fasılın 6 no.lu notuna göre" yazılmaz).
- **Gerekçe:**
  - öğrenci maddeyi okumadan anlayacak açıklıkta olur;
  - şıklara harf ya da sırayla değil içerikle atıf yapar ("A şıkkı", "son seçenek" yok);
  - doğru cevabı "çeldirici" diye anmaz; en güçlü yanlış şık "En güçlü tuzak … seçeneğidir/önermesidir" diye anılır; önermeli soruda "En güçlü tuzak III. önermedir" biçimi kullanılır;
  - "Bu nedenle doğru cevap '<d ile birebir aynı>' seçeneğidir." cümlesiyle ve ardından `(MD …)` ile biter. MD içeriği: mevzuatta "KMK 5, 13", "KDVK 21", "GK 27"; tarifede "GYK 1 ve 6; Fasıl 4 Notu; 04.10 Açıklama Notu"; hesapta formülün adı ("GV matrahı formülü; GK 27").
  - Hüküm son 12 ayda değiştiyse değişiklik tarihi yazılır.
- **Harf:** Harf yazma; `kitap_gm.py` dağıtır (art arda aynı harf yok, harfler dengeli). `sirali=True` soruların harfi şıktaki konumla sabittir; dosyada iki sıralı soruyu doğru şık konumu aynıyken art arda koyma (ör. iki "C" yan yana gelmesin), arada serbest bir soru bulunsun.
- **Vaka tarihleri** hafta içine denk gelir: `python3 -c "import datetime;print(datetime.date(Y,M,G).strftime('%A'))"`. Kontrol aracı kökteki gg.aa.yyyy tarihlerini denetler.
- Türkçe büyük harfte i → İ (kitap bunu kendisi yapar; veride büyük harfli başlık yazma).
- Marka yalnız "Gümrük Koçu - Ufuk Çetintaş".
- Tek ve tartışmasız doğru cevap; hiçbir çeldirici metne göre doğru sayılmaz; her çeldiricinin metindeki gerçek yuvası `yuva` alanına yazılır (uydurma en son çare).
- Yakınlığı dürüst etiketle: kilit cümle birebir → BİREBİR; anlamı korunarak yeniden ifade → PARAFRAZ; vaka, hesap, birden çok hükmü birleştiren grup sorusu → ÇIKARIM.

## 4. Profil A — Mevzuat bölümleri (M01–M64)

GM 2021–2025 sınavlarının mevzuat soruları (GTİP ve hesap soruları çıkarıldığında 371 soru): olumsuz kök %40, klasik %29, önermeli %18, tanım + boşluk + eşleştirme + vaka %13 (tanım 15, boşluk 11, eşleştirme 11, vaka 9 soru). Kota buna göredir:

| Soru sayısı | Olumsuz kök (önermeli dışı) | Klasik | Önermeli | Diğer (tanım / boşluk / eşleştirme / vaka) |
|---:|---:|---:|---:|---:|
| 8 | 3 | 2 | 2 | 1 |
| 9 | 4 | 2 | 2 | 1 |
| 10 | 4 | 3 | 2 | 1 |
| 11 | 4 | 3 | 2 | 2 |
| 12 | 5 | 3 | 2 | 2 |
| 13 | 5 | 4 | 2 | 2 |
| 14 | 6 | 4 | 2 | 2 |
| 15 | 6 | 4 | 3 | 2 |
| 16 | 6 | 5 | 3 | 2 |
| 18 | 7 | 5 | 3 | 3 |

- Her sütunda **±1** sapma serbesttir; GM analizindeki alan × tip tablosu farklı bir profil gösteriyorsa kaydırma bu yönde yapılır ve raporda gerekçelendirilir. Örnekler: kaçakçılık klasik ve önermeli ağırlıklı (M44 pilotunda 5/3/3/3); menşe bölümlerinde eşleştirme (belge–anlaşma–ülke) diğer sütununda öne alınır; GK genel bölümlerinde olumsuz kök tavana yakın tutulur.
- **Önermeli:** I–IV esastır, gerekirse V'e kadar. Kombinasyonlar çeşitlenir; en kapsamlı şık en fazla önermelilerin üçte birinde doğrudur. "Yanlıştır / yanlış olanlar" yönlü önermeli setteki önermelilerin en fazla üçte biridir (GM'de önermelilerin %31'i olumsuz yönlü). Yanlış önerme gerçek hükmün tek unsuru değiştirilerek kurulur. Önermeli şıklar doğal sırada yazılabilir (`sirali=True`, `siklar=[...]`).
- **Diğer sütunu:** boşluk sorusu GM'de çoğunlukla sayı, oran, süre ya da tutar sorar (11 sorunun 9'u); eşleştirme yalnız gerçek iki bilgi grubu varsa (belge–anlaşma, işlem–merci, rejim–süre). Tanımdan ad / addan tanım konu tanım içeriyorsa.
- **Küçük hesap/vaka serbest:** sayısal eşik, oran ve süre içeren hükümlerde (teminat dilimleri, ceza katları, süre hesabı, muafiyet eşikleri) küçük bir hesap ya da vaka sorusu klasik veya diğer sütunundan sayılır; hesap kuralları Profil C'deki gibidir (sıralı şık, adım adım gerekçe).
- **Kökü olumsuz toplam** (önermeli "yanlış" yönlü dahil) setin yaklaşık %40'ı olur.
- **Yakınlık:** birebir ≈%70, parafraz %15–20, çıkarım en fazla %15.
- **Sayısal ve süre soruları:** sayısal şıklar `sirali=True`, küçükten büyüğe; doğru değer 2., 3. ya da 4. sırada. Süre sorularının en az üçte birinde başlangıç anı ölçülür.
- **Zorunlu kapsam:** çıkmış GM bilgi alanlarının hepsi; metinde ikiz kavram ekseni varsa en az biri (uygunsa ayna çift); beş aday profili; kaynakta son 12 ayda (Ekim 2025 – Ekim 2026) değişen hüküm varsa en az bir güncellik sorusu (tarih dipnottan/parantezden okunur); konu elveriyorsa bir meslek yanlılığı sorusu (gümrük müşaviri, YGM, temsil).
- Mevzuat bölümünde tarife pozisyonu ya da GTİP sınıflandırma sorusu yazılmaz; BTB'nin süresi, makamı, geçersizliği gibi usul hükümleri sorulabilir.

## 5. Profil B — Tarife bölümleri (T01–T25)

GM tarife sorularının %93'ü eşyanın yerini sorar; en sık kurallar GYK 1 + 6 ve GYK 3(b); en çok sorulan fasıllar 84, 85, 87, 04. Kanıt **mutlaka** bölüm metnindeki resmî kısımlardan gelir: Bölüm/Fasıl notları, alt pozisyon notları, AS İzahnamesi genel açıklamaları ve pozisyon açıklama notları, Tarife Sınıflandırma Kararları ve sınıflandırma görüşleri. Bölüm metnindeki "Tarife Kitabı ders notu" ve "sunum notları" blokları anlamak için okunur, kanıt olarak kullanılmaz.

### T03–T24 (fasıl bölümleri)

- **≈%70 eşyanın yeri** (`kalip="GTİP"`): soru sayısı × 0,7 yuvarlanır (18 soruda 12–13). Kalıplar:
  - "Türk Gümrük Tarife Cetveline göre … aşağıdaki tarife pozisyonlarından hangisinde sınıflandırılır?" — şıklar 4 haneli pozisyon ("03.08") ya da fasıl. Pozisyon şıkları sınavdaki gibi **küçükten büyüğe** yazılır ve `sirali=True` olur; doğru pozisyon 2., 3. ya da 4. sıradadır. Çeldiriciler: komşu pozisyon, fasıl notuyla dışlanan pozisyon (örn. 16.02, 05.11), aynı terimi taşıyan başka fasıl pozisyonu.
  - "Aşağıdaki eşyalardan hangisi … pozisyonunda/… Fasılda sınıflandırılır?" ve olumsuz hâli "… sınıflandırılmaz?" — şıklar eşya adı; doğru eşya not ya da İzahname cümlesine dayanır, çeldiriciler aynı İzahnamenin gerçek örnekleridir. Bu sorular serbest harflidir.
  - Grup sorusu: "Aşağıdaki eşya gruplarından hangisinde yer alan eşyanın tamamı … sınıflandırılır?" (olumlu yön; çıkmış olumsuz kurgu kopyalanmaz).
  - Pozisyon şıklı ve eşya şıklı sorular yaklaşık yarı yarıya olsun; sıralı soru sayısı arttıkça A ve E harfleri yalnız serbest sorulara kalır.
- **Kalan ≈%30:** bölüm/fasıl notu ve kapsam soruları: notun kapsadığı ve dışladığı eşya (olumsuz kök dahil), not tanımları (tanımdan ad, boşluk), nottaki sayısal eşikler (sıralı şık; örn. kuru madde %70–85), ayırıcı işlem (örn. 2. Fasıl ↔ 16. Fasıl: pişirme, baharatla işlem).
- **Olumsuz kök** setin yaklaşık %40'ı (GTİP sorularının 7–8'i/18) olur. Önermeli soru yazılmaz ya da en fazla 1 olur (GM'de 76 tarife sorusunda 1).
- **Kök:** "Türk Gümrük Tarife Cetveline göre …" ya da "Türk Gümrük Tarife Cetvelinin 4. Fasıl notlarına göre …"; "Genel Yorum Kuralları" sorularında "Tarifenin Yorumuna İlişkin Genel Kurallar'a göre …". Kontrol aracı tarife kökünde "Tarife Cetveli / Genel Yorum Kuralları / İzahname / Armonize" ifadelerinden birini arar.
- **madde alanı:** "TGTC Fasıl 4 Notu; 04.10 Açıklama Notu" biçiminde. Gerekçe GYK 1 (pozisyon metni ve notlar) ve 6'yı (alt pozisyon) anar, doğru pozisyonun İzahname cümlesini aktarır, her çeldirici pozisyonun neyi kapsadığını söyler.
- **Sorulmaz:** 12 haneli GTİP, KN/milli alt açılım, vergi oranı, ölçü birimi değeri (kaynakta yok). Kaynakta sayısı silinmiş açıklama (ağırlık, sıcaklık) sorulmaz.
- Fasıllar dengeli kullanılır: bölümdeki her fasıldan en az bir soru; GM'de çok sorulan fasıllara (84, 85, 87, 04, 64, 97, 70, 96, 39, 19, 09) ağırlık verilir.

### T01, T02 ve T25 (kendi ağırlığında)

- **T01 (yapı ve sistematik):** GTİP kademeleri (2-4-6-8-10-12 hane), bölüm/fasıl sayıları, saklı fasıl, 98–99. fasıllar, ölçü birimi kısaltmaları, GK 15–16 ve GY 32 tanımları (kota, tarife kotası, tavan), başlıkların göstericiliği. Kökte Kanun/Yönetmelik/Tebliğ adı gerekiyorsa yazılır. Eşyanın yeri kotası uygulanmaz.
- **T02 (GYK 1–6):** soruların çoğu GYK **uygulama vakası** olur: eşya tarif edilir, uygulanacak kural ya da pozisyon sorulur (GYK 3(b) perakende takım, 2(a) demonte/eksik eşya, 1 ve 6 birlikte, fasıl notunun set kuralından önce gelmesi). Kalanı kuralın adı, kuralların uygulanma sırası, kuralın lafzı (boşluk, tek kelime değişikliği). Şıklarda GYK numarası kullanılabilir.
- **T25 (sınıflandırma genelgeleri, BTB yazısı, karar tebliğleri):** genelgenin konusu ve getirdiği sınıflandırma, BTB'ye ilişkin usul, karar tebliğlerinin genel hükümleri; Profil A kotası esas alınır, eşyanın yeri soruları ≈%40'ı geçmez.

## 6. Profil C — Hesaplama bölümleri (H01–H05)

GM hesap soruları sınavın %11,6'sıdır; en baskın kurgu uzun veri listesiyle ticari işlem kıymeti ve aynı veriyle KDV matrahıdır. Diğerleri: vergi zinciri (GV → İGV → ÖTV → KDV), alt-üst sınırlı (MIN/MAX) karma vergi, ÖTV (nispi, maktu, asgari maktu), ceza ve uzlaşma tutarı, kullanılmış taşıt kıymeti, gözetim, teminat ve gecikme zammı.

- **Sayısal soru oranı en az %65** (H01–H04). H05 (beyanname kutuları ve kod listeleri) sözel ağırlıklıdır: kod–anlam eşleştirmesi, kutu içeriği, klasik ve olumsuz kök; sayısal oran şartı H05'e uygulanmaz.
- **Kurgu (çıkmış soruyu taklit et, kopyalama):**
  - Veri kökte madde imli satırlarla verilir (`"- FOB mal bedeli: 20.000 ABD Doları"`); son satır soruyu sorar ve hesaplanan büyüklüğü adlandırır ("… ödenecek KDV tutarı kaç TL'dir?").
  - Rakamlar basit, hesap 2–4 adım; zorluk aritmetikte değil, unsurun matraha girip girmediğini bilmekte.
  - Veride en az bir "tuzak unsur" bulunur: Türkiye'deki iç nakliye, tescilden sonraki gider, damga vergisi, kültür fonu, satın alma komisyonu gibi kurala göre dışarıda kalan kalem.
  - Bölümde en az bir **aynı veriyle çift soru** (önce kıymet / ÖTV, sonra KDV matrahı / KDV) ve en az bir **saklı istisnalı vaka** (örn. dahilde işleme izin belgesi kapsamındaki ithalatta KKDF %0) bulunur. Çift sorunun her biri kendi verisini tekrar eder.
- **Şıklar:** sayısal, küçükten büyüğe, `sirali=True`, doğru değer 2., 3. ya da 4. sırada; bölüm içinde B, C ve D konumları dengeli dağıtılır. Şıkta yalnız sayı yazılır ("12.472"); birim kökte verilir. Binlik ayırıcı nokta, ondalık virgül.
- **Çeldiriciler adlandırılmış tipik hatalardan** üretilir ve `yuva` alanına hata adıyla yazılır: bir ilaveyi (navlun, sigorta, yurt dışı gider) unutmak; indirimi yapmamak; yurt içi gideri GV matrahına eklemek; KDV/ÖTV matrahına önceki vergiyi eklememek; ÖTV'yi kendi matrahına katmak; KDV'yi ÖTV matrahına eklemek; MIN/MAX karşılaştırmasını yapmamak ya da sınırı kg yerine adetle kurmak; yanlış kur (satış ↔ alış); yanlış oran (aynı mevzuattaki komşu oran). Dört çeldiricinin dördü de farklı sayı vermelidir.
- **Gerekçe adım adım hesaplar** ("GV matrahı = 50.000 + 2.000 = 52.000 TL; GV = 52.000 × %8 = 4.160 TL …"), formülün kaynak cümlesini aktarır (kanıtta da yer alır), her çeldiricinin hangi hatadan doğduğunu bir kez söyler, en güçlü tuzağı ayrıca belirtir. Kontrol aracı HESAP gerekçesinde "=" ya da "×" arar.
- **Kaynak sınırı:** formül ve kural kaynakta olmalıdır; kaynakta formülü olmayan hesap sorulmaz. Kaynakta oranı yazmayan yükümlülükte (EMY, kültür fonu, bandrol) oran soruda veri olarak verilir, formül ve matrah kuralı kaynaktan gelir. Kaynakta açık olmayan bir unsur (ör. KKDF'nin KDV matrahına girip girmediği) hiçbir hesapta kullanılmaz.
- **Kök:** hesap kökünde mevzuat adı aranmaz (GM hesap soruları sınavda mevzuat adı taşımaz); kök hesaplanan büyüklüğü adlandırır. Sözel hesap-bölümü sorularında dayanak bir Kanun/Karar/Tebliğ ise kökte yazılır (örn. "3065 sayılı Katma Değer Vergisi Kanunu'na göre ithalatta …").
- `kalip="HESAP"`, `vaka=True`, `yakinlik="ÇIKARIM"`, `duzey=["UYGULAMA"]`, `tuzak` içinde `AD-HESAP`.
- **Sayısal doğrulama zorunlu:** `dogrulama/{KOD}_hesap_kontrol.py` yazılır (şablon: `dogrulama/H02_hesap_kontrol.py`). Betik veri dosyasını okur; her hesap sorusunun doğru sonucunu ve her çeldiriciyi adlandırılmış hatadan Python'da (Decimal) yeniden hesaplar; şıkların bu hesaplarla birebir aynı ve artan sırada olduğunu, beş değerin farklı olduğunu, doğru şıkkın B/C/D'de ve gerekçede geçtiğini denetler; "hata: 0" vermeden bölüm teslim edilmez.

## 7. Veri biçimi

Çıktı dosyan `{CIKTI}`; içinde `Q = [ dict(...), ... ]` ve **{SORU}** soru olur. Alanlar GMY ile aynıdır; `blok` bölüm kodudur:

```python
dict(
konu="Kaçakçılıkla Mücadele Kanunu", blok="{KOD}",
kalip="KAPSAM_DIŞI",   # GMY kümesi + GTİP: TANIM KAVRAM KAPSAM KAPSAM_DIŞI DOĞRU YANLIŞ ÖNERMELİ SÜRE ORAN-TUTAR YETKİ BELGE ŞART HESAP BOŞLUK EŞLEŞTİRME MÜEYYİDE OLAY TABİ ZORUNLULUK MATRAH DAYANAK SONUÇ MUAFİYET KISA_AD GTİP
z="O",                 # ÇK K O Z ÇZ
madde="5607 sayılı Kaçakçılıkla Mücadele Kanunu md. 19",   # çözümde görünen dayanak satırı (kökte ve şıkta numara YASAK)
cek="≤25 kelimelik çekirdek bilgi",
kok=["… aşağıdakilerden hangisi … ?"],   # önermelide "I. …" satırları; vaka/hesapta veri satırları "- …"
d="doğru şık", c=["çeldirici 1","çeldirici 2","çeldirici 3","çeldirici 4"],
sirali=False,          # True ise siklar=[5 şık nihai sırasıyla] (sayısal ve pozisyon şıkları ZORUNLU)
g="Gerekçe … En güçlü tuzak … Bu nedenle doğru cevap '<d ile birebir aynı>' seçeneğidir. (MD KMK 19)",
kanit="44-kacakcilik-kanunu.txt | kaynaktan BİREBİR alıntı",
yuva=["çeldirici 1'in kaynaktaki gerçek yeri ya da hesap hatasının adı", "…", "…", "…"],
yakinlik="BİREBİR", tuzak=["LİSTE-DIŞI"], duzey=["AYIRT"], profil=[3],
olumsuz=True, vaka=False, baslangic=False, eksen=0, ayna="", guncellik="", cikmis="2024/87; 2025/85", kapsamli=False,
),
```

- `cikmis` alanına GM çıkmış sorusunun yıl/no'su yazılır (gm_sorular.csv kimlikleri).
- `tip` etiketi (olumsuz, klasik, önermeli, GTİP, hesap, tanım, boşluk, eşleştirme, vaka) kalıp ve bayraklardan otomatik çıkarılır; kotayı buna göre tut.

## 8. Kontrol (zorunlu)

```
python3 -I /home/user/2027-ye-Haz-rl-k/araclar/gm-soru-bankasi/kontrol_gm.py {METIN} {CIKTI}
```

- "Hatalı soru: 0" olana kadar düzelt. Araç ayrıca tip profilini, Profil A kotasını, tarife "eşyanın yeri" oranını ve sabit harf konumlarını basar.
- Profil C'de `dogrulama/{KOD}_hesap_kontrol.py` "hata: 0" vermelidir.
- Prompt 5 bölüm 16'daki 30 maddelik kontrolü her soruya uygula: tek ve tartışmasız doğru cevap; çeldiricilerin metne göre yanlışlığı; kökteki mevzuat türünün kaynakla aynılığı; önermelerin doğru/yanlış niteliğinin metinle teyidi; tarifede doğru pozisyonun not/İzahname cümlesiyle teyidi ve hiçbir çeldirici pozisyonun aynı eşyayı kapsamaması.

## 9. Kör çözüm (zorunlu)

1. Bölümü kitaba bas: `python3 -I kitap_gm.py {METIN} bolumler.json veri <AD> --cilt {CILT} --bolum {KOD}` → `<AD>.json` harfli ve şıkları dizilmiş soruları içerir.
2. Bu JSON'dan yalnız kök ve şıkları içeren cevapsız metin çıkar. Çözümü yapan, cevap anahtarını, gerekçeyi, kanıtı ve madde satırını görmeden yalnız bu metin ve bölüm kaynağıyla çözer (mümkünse ayrı bir alt ajan; değilse ayrı bir geçişte, veri dosyasını açmadan).
3. Sonucu `kor_cozum/{KOD}.json` dosyasına yaz: `{"{KOD}-01": {"cevap": "C", "emin": "yüksek|orta|düşük", "dayanak": "kaynaktaki cümle", "sorun": ["varsa ikinci savunulabilir şık vb."]}}`.
4. `python3 -I kor_karsilastir_gm.py <AD>.json` ile karşılaştır. Uyuşmayan, "emin" değeri yüksek olmayan ya da sorun bildirilen her soruyu düzelt (çoğunlukla çeldirici değişir) ve yeniden kontrol et; değişiklikleri `dogrulama/{KOD}.md` dosyasına tek satırla yaz.

## 10. Rapor dosyası

`{RAPOR}` dosyasına JSON yaz:

```json
{"bulunamayan": ["2024/41: … (metinde yok)"], "giremeyen": "tek cümle: sete giremeyen önemli soru alanları", "notlar": ["kota sapması ve gerekçesi, çıkmış alan → soru eşlemesi, güncellik durumu, kaynak sorunları"]}
```

## 11. Dönüş mesajın

En fazla 8 satır: soru sayısı; kontrol sonucu (ve Profil C'de hesap kontrolü); tip profili (olumsuz / klasik / önermeli / diğer ya da GTİP / not, hesap / sözel); kör çözüm uyumu; karşılanamayan kota ya da çıkmış alan ve nedeni.

Depo dosyalarına dokunma; yalnız `{CIKTI}`, `{RAPOR}`, `kor_cozum/{KOD}.json`, gerekiyorsa `dogrulama/{KOD}_hesap_kontrol.py` ve `dogrulama/{KOD}.md` dosyalarını yaz.

---

Yer tutucular: `{KOD}` (M44), `{BASLIK}`, `{SORU}`, `{CILT}` (mevzuat | tarife-hesap) ve `{DOSYA}` `bolumler.json`'dan; `{METIN}` bütün bölüm metinlerinin düz klasörü (`…/scratchpad/gm/metin/tum`); `{ANALIZ}` GM sınav analizi klasörü; `{CIKTI}` = `araclar/gm-soru-bankasi/veri/gm_{KOD}.py`; `{RAPOR}` = `araclar/gm-soru-bankasi/veri/gm_{KOD}_rapor.json`.
