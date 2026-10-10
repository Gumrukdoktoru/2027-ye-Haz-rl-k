# Çekişmeli Doğrulama Talimatı (Deneme 6–10)

Klasör: `araclar/gmy-deneme6-10`. **HİÇBİR DOSYAYI DEĞİŞTİRME**; yalnız rapor yaz.

Veri: `setN.json` (N = 6…10), her biri 100 soru. Alanlar: `id`, `no`, `blok` (GK / GÜMRÜK), `cikmis` (karşılanan çıkmış soru), `tip`, `kok` (liste; `[[…]]` koyu+altı çizili olumsuz kelime, `**…**` koyu), `opts` (A–E gösterim sırası), `harf` (doğru cevap), `d` (doğru şık metni), `g_harfli` (açıklama), `madde` (yasal dayanak), `kanit` (dosya | alıntı), `cek` (çekirdek).
Kaynak: `metin/` (gümrük mevzuatı, 5607 ve yönetmelikleri, İthalat Rejimi Kararı + 2025 değişikliği, `Canli_7_24_Genel_Kultur_Kitabi.txt`). Çıkmış sınav metinleri: `sinav/<yıl>_duz.txt` (2025: `sinav/2025B_duz.txt`).
Kurallar: `../../promptlar/prompt-4-gmy-soru-motoru-master.md`, `../../promptlar/prompt-3-nihai-soru-hazirlama-kurallari.md`, `../../CLAUDE.md`, `YAZAR_TALIMAT.md`.

Sana verilen aralıktaki HER soru için:
1. **Doğru cevap kesin mi?** Hükmü kaynakta bul ve çevresini oku (istisnalar, dipnotlu değişiklikler, "mülga" ibareleri, sonradan gelen değişik metinler). Hesap sorularını Python ile yeniden yap. Matematik sorularını yeniden çöz.
2. **Çift doğru var mı?** Diğer 4 şıktan biri de kaynağa göre savunulabilir mi? Olumsuz kökte (T1) yalnız bir şık mı yanlış? Öncüllüde her öncülü ayrı ayrı kaynağa göre değerlendir ve doğru kombinasyonu kendin bul.
3. **Açıklama** doğru şıkla ve harfle uyumlu mu; çeldiricileri doğru gerekçeyle mi eliyor?
4. **Kaynak dışı bilgi** (doğru şıkta, çeldiricide iddia olarak, açıklamada, olay verisinde) veya uydurma madde/seri numarası, eşik var mı? `madde` alanındaki madde numaraları kaynakla tutarlı mı?
5. **Kök kuralları:** mevzuat adı + hükmün konusu var mı (gümrük soruları); madde/fıkra/bent numarası kökte/şıkta yok; 2009/15481 Karar kökü "4458 sayılı …" ile başlamıyor ve kurum kalıbını kullanıyor; olumsuz kelime işaretli; dil kurum diline yakın, yapay ifade yok.
6. **Kapsam:** GMY gümrük bölümü yalnız Gümrük Kanunu ve ikincil düzenlemeleri, 5607 ve ikincil düzenlemeleri, İthalat Rejimi Kararı, DİR Tebliği, Sınır Ticareti Kararı; dış ticaret/kambiyo mevzuatı (bedelsiz ihracat, İhracat Yönetmeliği vb.) sorulmaz.
7. **Kopya kontrolü:** `cikmis` alanındaki çıkmış soruyu ham metinde bul; yeni soru onun metnini/şıklarını/kurgusunu kopyalıyor mu, ya da aynı hükmü mü soruyor (aynı konu serbest, aynı hüküm değil)?
8. **Şık kalitesi:** bariz yanlış veya saçma çeldirici, kategori dışı şık, eski-yeni kurum adı rakipliği, mutlak ifadelerin sırıtması, dilbilgisel uyumsuzluk.
9. Aralığındaki iki soru aynı hükmü/çekirdeği ölçüyor mu?

Çıktı (kısa rapor): yalnız SORUNLU sorular. Her biri için: `id`, tür (YANLIŞ CEVAP / ÇİFT DOĞRU / KAYNAK DIŞI / GÜNCEL DEĞİL / KOPYA / AYNI HÜKÜM / GEREKÇE UYUMSUZ / KÖK KURALI / KAPSAM DIŞI / ZAYIF ÇELDİRİCİ / BELİRSİZ / TEKRAR), kanıt (dosya + birebir alıntı), **somut düzeltme** (hangi şık/öncül/kök metni nasıl olmalı; doğru cevap değişiyorsa yeni doğru şık metni). Düzeltme önerirken şık uzunluk dengesini (doğru şıkkın ±%10 bandında 2 çeldirici, en az biri daha uzun) bozma. Sorunsuz soruları aralıkla say ("D6-021…D6-040 sorunsuz"). Şüpheleri "ŞÜPHE" başlığıyla ayrı ver.
