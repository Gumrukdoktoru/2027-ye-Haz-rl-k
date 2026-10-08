# GÖREV: Soru tipi dağılımını gerçek sınavlara yaklaştır — Bölüm {BOLUMLER}

Kullanıcı kitabın soru tiplerinin 2021–2025 GMY sınavlarına yakın olmasını istedi. Bu iş Prompt 5'teki tip kotalarının (önermeli 3–4, vaka 2–3) önüne geçer. Prompt 5'in diğer bütün kuralları aynen geçerlidir.

## Gerçek sınav dağılımı

Kaynak: `/home/user/gmy-ikmislar/analiz/BAKANLIK-SORU-YAZARI-ANALIZI.md`, "Beş yılın kod toplamları". 400 gümrük sorusu:

| Format | Oran |
|---|---|
| Klasik (doğrudan "hangisidir / doğru olarak verilmiştir / kaç gün") | %39 |
| Olumsuz kök ("hangisi değildir / sayılmamıştır / yer almaz / yanlıştır") | %38 |
| Öncüllü (önermeli) | %10 |
| Tanımdan ad / addan tanım | %8,5 |
| Vaka | %4 |
| Boşluk | %3 |
| Hesap | %2 |
| Eşleştirme | %1 |

## Bu bölümler için hedef (20 soruluk bölümde; 18 soruluk Bölüm 06'da orantılı)

| Tip | Hedef |
|---|---|
| Önermeli (kalip="ÖNERMELİ") | **2** |
| Vaka + hesap (vaka=True veya kalip OLAY/HESAP) | **1**; Bölüm 11, 44, 45 ve 47'de en fazla 2 |
| Tanımdan ad / addan tanım (kalip TANIM veya KAVRAM) | **2**; kaynakta tanım hükmü yoksa 1, o da yoksa 0 |
| Olumsuz kök, önermeli dışı (olumsuz=True) | **7–8** |
| Boşluk + eşleştirme | en fazla **1**; eşleştirme yerine boşluk tercih et |
| Klasik | kalan sorular (yaklaşık 7–8) |

Mevcut durum:
{DURUM}

## Nasıl yapacaksın

1. Prompt 5'i oku: `/home/user/2027-ye-Haz-rl-k/promptlar/prompt-5-gmy-mevzuat-sorusu-hazirlama.md`. Kök kalıbı, kanıt, gerekçe, sayısal sıra, madde numarası yasağı ve Karar kökü kuralları aynen geçerli.
2. Her bölümde `{S}/sb/batch/sb_XX.py` dosyasını oku. Önce `python3 -I /home/user/2027-ye-Haz-rl-k/araclar/gmy-deneme3/kontrol5.py {S}/mevzuat/metin {S}/sb/batch/sb_XX.py` ile profili gör.
3. Fazla önermeli ve vaka sorularını **aynı bilgi alanını ölçen** başka tiplere çevir: olumsuz kök, klasik, tanımdan ad / addan tanım. Hangilerini koruyacağını şöyle seç:
   - Önermeli: ayna çiftin parçası olanı, çıkmış sorunun önermeli kurgusunu karşılayanı ve en çok ayırt edeni koru.
   - Vaka: içinde saklı istisna olanı ya da hesap gerektireni koru.
   - Boşluk/eşleştirme hedefi aşıyorsa fazlayı da çevir.
4. Çevirirken:
   - **Çıkmış kapsamı düşürme.** `cikmis` alanı dolu bir soru çevrilirse yeni soru aynı bilgi alanını ölçmeli; `cikmis` alanı korunur.
   - Doğru şık kaynaktan birebir ya da anlamı birebir korunan parafraz olur.
   - Olumsuz köklerde Bakanlık kalıbını kullan: "… aşağıdakilerden hangisi … değildir / sayılmamıştır / … arasında yer almaz?" Liste-dışı tipte çeldiriciler listenin gerçek unsurlarıdır, doğru şık listede olmayan ama komşu hükümden gelen unsurdur.
   - Tanımdan ad kalıbı: "… Kanunu'na göre, '…' biçiminde tanımlanan kavram aşağıdakilerden hangisidir?" Addan tanım kalıbı: "… göre '…' deyimi aşağıdakilerden hangisini ifade eder?"
   - Bütün alanları güncelle:
     - kalip, z, kok, d, c (sayısal ise sirali=True ve siklar),
     - g; gerekçe şıkları içerikle anar, harf ya da sıra bildirmez ("son seçenek" yazma) ve "Bu nedenle doğru cevap '<d>' seçeneğidir. (MD …)" ile biter,
     - kanit (birebir alıntı), yuva, yakinlik, tuzak, duzey, profil,
     - olumsuz, vaka, baslangic, eksen, ayna (ayna çiftini bozduysan karşı soruda da ayna alanını güncelle), cek.
   - Gerekçe hiçbir yerde doğru cevabı "çeldirici" diye anmamalı. Önermeli sorularda "en güçlü tuzak III. önermedir" gibi yaz.
   - Yeni soru setteki diğer sorularla ve `{S}/sb/uretilen.md`'deki başka bölümlerin sorularıyla aynı çekirdeği aynı yönden sormamalı.
   - Tarih kullanırsan hafta içine denk getir: `python3 -c "import datetime;print(datetime.date(Y,M,G).strftime('%A'))"`.
   - Türkçe yazıma dikkat: ı/i, ekler, kesme işareti.
5. Her yeni soruyu kaynak metne göre kendin çöz: tek ve tartışmasız doğru cevap olmalı ve hiçbir çeldirici metne göre doğru sayılmamalı.
6. Değiştirmediğin sorulara dokunma. Soru sayısını değiştirme.
7. kontrol5.py "Hatalı soru: 0" vermeli ve profil yukarıdaki hedeflere uymalı.

## Rapor

Her bölüm için `{S}/sb/denge_rapor/sb_XX.md` dosyasına yaz:
- değiştirilen her soru tek satır: dosyadaki sıra (Q3 gibi), eski tip → yeni tip, ölçülen bilgi;
- son profil: önermeli, vaka/hesap, tanım, olumsuz, boşluk+eşleştirme.

## Dönüş mesajın

En fazla 6 satır:
- bölüm başına değişen soru sayısı ve son profil,
- kontrol5 sonucu,
- hedefe ulaşılamayan yer ve nedeni.
