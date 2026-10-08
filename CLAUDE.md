# CLAUDE.md — 2027'ye Hazırlık (Gümrük Koçu)

GM / GMY sınavlarına hazırlık için Word kaynaklarından **ders notu** ve **test sorusu** üretim deposu.

## Yapı
- Kaynak mevzuat dosyaları (Word/.doc/PDF) **depo kökünde** durur (kullanıcı 3 Ekim 2026'da `kaynaklar/` klasörünü kaldırıp kaynakları köke yükledi; düzen değiştirilmez). Çıkmış sınavlar: `2021–2024-gmy-sinavi-cevapli.pdf`, `2025_..._CEVAPSIZ.pdf`.
- `promptlar/prompt-1-akilli-test-soru-motoru.md` — test sorusu üretim kuralları (Prompt 1).
- `promptlar/prompt-2-ders-notu-motoru.md` — ders notu üretim kuralları (Prompt 2).
- `promptlar/prompt-3-nihai-soru-hazirlama-kurallari.md` — kullanıcının nihai soru hazırlama kuralları (Prompt 3). Soru üretiminde Prompt 1 ile çelişirse **Prompt 3 geçerlidir** (çıkmış soruların bilgi alanları atlanmaz, kök = mevzuat adı + hükmün konusu + kurum kalıbı, önermeli en az 3 önerme, gerekçe sonunda (MD …), art arda aynı cevap harfi yok).
- `promptlar/prompt-4-bakanlik-yazar-profili.md` — 2021–2025 çıkmış soruların tersine mühendisliğinden çıkan Bakanlık soru yazarı profili (yazarın hedefleri, çeldirici üretimi, ikiz kavram eksenleri). Soru üretiminde Prompt 3'ün üstüne uygulanır; çelişirse Prompt 3 geçerlidir. Tam rapor ve resmî cevap anahtarı: `gmy-ikmislar` deposu `analiz/`.
- `promptlar/prompt-5-gmy-mevzuat-sorusu-hazirlama.md` — kullanıcının 7 Ekim 2026'da verdiği GMY Sınavı Mevzuat Sorusu Hazırlama Promptu (Prompt 3 ve Prompt 4'ün birleşik, genişletilmiş hâli). Kullanıcı bu promptla soru istediğinde eksiksiz uygulanır; ilk set: `sorular/GK_GMY_Deneme3_50soru` (üretim hattı `araclar/gmy-deneme3/`).
- `sorular/GK_GMY_Soru_Bankasi.pdf` — Prompt 5 ile her kaynak dosyadan 20 soruluk, 56 bölümlük soru bankası kitabı (1118 soru; Bölüm 06 kaynağı dar olduğu için 18 soru). Soru tipi dağılımı 2021–2025 sınavlarına göre ayarlandı; bütün sorular cevap anahtarı görülmeden kör çözümle doğrulandı (araclar/soru-bankasi/kor_cozum*). Bölüm md'leri `sorular/soru-bankasi/`, soru verisi ve doğrulama raporları `araclar/soru-bankasi/`. Hafızadaki set kodu `SB-KXX`, soru kimliği `SBXX-YY`.
- `sorular/` — üretilen soru setleri; `sorular/hafiza/URETIM-HAFIZASI.md` üretim hafızası.
- `notlar/` — üretilen ders notları (Ders_Notu_{KONU}.docx).

## Çalışma kuralları
- Soru isteğinde Prompt 1'i, ders notu isteğinde Prompt 2'yi eksiksiz uygula.
- Tek bilgi kaynağı depoya yüklenen mevzuat dosyalarıdır; web araştırması yok, kaynakta olmayan bilgi yok.
- Her soru setinden önce `URETIM-HAFIZASI.md` okunur, set bitince yeni satırlar eklenip commit edilir.
- Marka yalnızca "Gümrük Koçu - Ufuk Çetintaş".
- Kullanıcı yeni kaynak yüklerse dosyaları taşımadan metnini çıkar (araclar/metin_cikar.py) ve çalışmada kullan.

## Kullanıcı tercihleri
- **Konu kapsamı serbest:** Sınav kitapçığı modelinde set üretilirken kitapçıktaki konu dağılımıyla sınırlı kalınmaz; `kaynaklar/` içindeki diğer konulardan da (ör. kabotaj, özet beyan, sınır ticareti, ihracat sayılan satış ve teslimler, e-ihracat, dış ticaret sermaye şirketi, fuar tebliği, bedelsiz ihracat, telafi edici vergi) soru sorulabilir. Kaynakta olmayan bilgi kuralı değişmez.
- Kitapçık soruları kopyalanmaz; aynı konu sorulursa farklı hüküm seçilir.
- **Soru tipi dağılımı sınavlara yakın olur** (kullanıcı 8 Ekim 2026; Prompt 5'teki tip kotalarının önüne geçer). Dayanak: 2021–2025 GMY'deki 400 gümrük sorusu (`gmy-ikmislar/analiz/BAKANLIK-SORU-YAZARI-ANALIZI.md`). Oranlar: klasik %39, olumsuz kök %38, önermeli %10, tanımdan ad/addan tanım %8,5, vaka %4, boşluk %3, hesap %2, eşleştirme %1. 20 soruluk sette hedef: önermeli 2, vaka+hesap 1, tanım 2, olumsuz kök 7–8, boşluk/eşleştirme en fazla 1, kalanı klasik.
- **Gerekçe dili:** Gerekçe şıklara harf ya da sırayla ("son seçenek") değil içerikle atıf yapar. Doğru cevabı "çeldirici" diye anmaz. Önermeli sorularda en güçlü tuzak "III. önerme" diye anılır. Vaka tarihleri hafta içine denk gelir. Büyük harfe çevirmede Türkçe kuralı uygulanır (i → İ).
- **Test PDF düzeni:** Soru kitapçığı bölümü gerçek test kâğıdı gibi **çift sütunlu** basılır (sütun arası çizgi, kalın soru kökü, sonda "TEST BİTTİ", ardından cevap formu). Cevap anahtarı, cevaplı-gerekçeli bölüm ve set raporu tek sütun kalır. Üretici: `araclar/gmy-deneme3/cikti5.py` + `pdf5.mjs`.
- **Karar kaynaklı sorularda kök:** 2009/15481 sayılı Bakanlar Kurulu Kararına dayanan sorularda kök "4458 sayılı …" ile başlamaz (Kanun sanılır). Kurum kalıbı kullanılır: `2009/15481 sayılı "4458 sayılı Gümrük Kanununun Bazı Maddelerinin Uygulanması Hakkında Karar"a göre …`. Diğer kararlar ve yönetmelikler için de kök, dayanağın türünü (Kanun/Karar/Yönetmelik/Tebliğ) baştan açıkça göstermelidir.
