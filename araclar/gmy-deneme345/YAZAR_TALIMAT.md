# GMY Deneme 3-4-5 — Soru Yazarı Ortak Talimatı

Çalışma klasörü: araclar/gmy-deneme345

## Görev
Sana verilen konu kümesinde **30 soru** yaz: Deneme 3, Deneme 4 ve Deneme 5 için **her birine 10'ar soru** (dict'te `set` alanı: 3, 4 veya 5). Aynı bilgi (çekirdek) üç sette ve önceki setlerde tekrar etmez.

## Kurallar (tamamını oku, harfiyen uygula)
- promptlar/prompt-3-nihai-soru-hazirlama-kurallari.md — özellikle §5 bilgi türü→kurum kalıbı, §7 madde/fıkra/bent no kökte ve şıkta yok, §8 kök = MEVZUAT ADI + HÜKMÜN KONUSU + KALIP, §11–13 çeldirici ve önermeli standardı (en az 3, tercihen 4 önerme; doğru kombinasyonlar farklı; "hepsi doğru" yok), §14 çıkmış bilgi alanı atlanmaz ama metin/şık/kurgu kopyalanmaz, §17 eski-yeni kurum adı rakip şık yapılmaz, §20 gerekçe.
- CLAUDE.md "Kullanıcı tercihleri" bölümü — özellikle: Karar dayanaklı sorularda kök "4458 sayılı …" ile BAŞLAMAZ; `2009/15481 sayılı "4458 sayılı Gümrük Kanununun Bazı Maddelerinin Uygulanması Hakkında Karar"a göre …` kalıbı kullanılır. Kök, dayanağın türünü (Kanun/Karar/Yönetmelik/Tebliğ) baştan açık göstermeli.
- KAYNAKTA YOKSA ÜRETME: tek bilgi kaynağı `metin/` (gümrük mevzuatı, 5607 ve yönetmelikleri, İthalat Rejimi Kararı 2020/3350 + 2025 değişikliği, silah-mühimmat kararı, Canli_7_24_Genel_Kultur_Kitabi.txt). Web yok, hafıza yok.

## 2024–2025 ESASLI ÜRETİM (kullanıcının özel isteği)
- `cikmis_envanter.tsv` sütunları: YIL, SORU_NO, KONU, ÖLÇÜLEN_BİLGİ, KALIP, KAYNAK_DOSYA, CEVAP (tahmini), RESMI_CEVAP (**resmî anahtar** — bunu esas al).
- Konu kümendeki **2024 ve 2025** satırlarının HER BİRİNİN bilgi alanı üç setin en az birinde mutlaka ölçülmeli (KAYNAK_DOSYA=YOK olanlar hariç; onları raporda listele). Aynı hükmü kopyalamadan farklı soru tekniğiyle sor (ör. çıkmışta "değildir" ise sen olay/eşleştirme/boşluk/önermeli kurabilirsin).
- Kalan kontenjanı 2021–2023'te sık sorulan bilgi alanlarıyla ve kaynaktaki diğer sınavlık hükümlerle doldur.
- Ham sınav metinleri: `sinav/` (2021–2025 B kitapçığı), `sinavA/2025A.txt` (2025 A kitapçığı). Kurum dilini ve 2024–2025 kalıplarını buradan gör: 2024–2025'te "değildir/kapsam dışı" (%17), süre (%14), önermeli (%13), yanlış bulma (%13) kökleri ağır basıyor; olay ve hesap soruları arttı. Kalıp dağılımını buna yakın tut.
- Önceki setlerin hafızası (aynı ÇEKİRDEĞİ tekrar etme; aynı bilgi alanı gerekiyorsa gerçekten farklı bir ölçme boyutu seç): sorular/hafiza/URETIM-HAFIZASI.md (KAR-, GMY-, GMY2- satırları).

## Set başına dağılım (her set için ayrı ayrı)
- 10 soru; zorluk tam olarak: ÇK 1, K 2, O 4, Z 2, ÇZ 1.
- Doğru şıkkın en uzun şık olduğu soru set başına en çok 2.
- Kümendeki konu kontenjanı (aşağıda prompt'ta verilir) her sette aynen sağlansın.

## Format
Dosya: `batch_<KÜME>.py`, içinde `Q = [dict(...), ...]` (30 eleman). Örnek: `ornek_format.py`. Alanlar:
set (3/4/5), konu, kalip (TANIM KAVRAM KAPSAM KAPSAM_DIŞI DOĞRU YANLIŞ ÖNERMELİ SÜRE ORAN-TUTAR YETKİ BELGE ŞART HESAP BOŞLUK EŞLEŞTİRME MÜEYYİDE OLAY TABİ ZORUNLULUK MATRAH DAYANAK SONUÇ MUAFİYET KISA_AD), z (ÇK/K/O/Z/ÇZ), madde (yalnız bu alanda, ör. "GK 241/1; GY 500"), cek (≤25 kelime, ölçülen hüküm), kok (liste; önermeli ise "I. …" satırları ve son satır kökün devamı; paragraf/olay metni ayrı eleman olabilir), d (doğru şık), c (4 çeldirici), g (gerekçe §20; doğru şıkkı harfle değil şık metniyle an — harfi ben yerleştireceğim; sonu "(MD GK 241/1)" biçiminde), kanit ("dosya.txt | kaynaktan BİREBİR alıntı ≤40 kelime"), cikmis ("2024/45, 2025/31" ya da boş).
- Önermeli şıklarında yalnız "I ve III" gibi kombinasyonlar. Somut olaylarda firma/kişi etiketleri şık harfleriyle karışmasın: (A)-(E) yerine (K), (L), (M), (X), (Y) vb. kullan.
- Hesapları Python ile doğrula. Yıllık yeniden değerlenen TL tutarlarını sorma (ya da kökte esas tutarı ver).

## Denetim
1. `python3 kontrol4.py batch_<KÜME>.py` → "GENEL SONUÇ: TEMİZ" olana kadar düzelt. "?? benzer çekirdek" uyarılarını incele; gerçekten aynı bilgiyse birini değiştir.
2. Her kanit alıntısını metin/ içinde (boşluk normalize ederek) birebir ara.
3. Yazdığın her soruyu cikmis alanındaki çıkmış soruyla karşılaştır: metin/şık/kurgu kopyası olmasın.

## Rapor (bitince kısa)
Set başına konu dağılımı; karşılanan 2024–2025 çıkmış soru numaraları; kaynakta olmadığı için karşılanamayan 2024–2025 soruları; emin olmadığın noktalar. Git işlemi yapma, başka dosyaya dokunma.
