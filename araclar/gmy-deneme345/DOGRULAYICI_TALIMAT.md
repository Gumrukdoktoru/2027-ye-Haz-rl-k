# Çekişmeli Doğrulama Talimatı (Deneme 3-4-5)

Klasör: araclar/gmy-deneme345
HİÇBİR DOSYAYI DEĞİŞTİRME; yalnızca rapor yaz.

- setN.json (N=3,4,5): 100'er soru. Alanlar: no, kok, opts (A–E), harf (doğru), d (doğru şık metni), c, g (gerekçe; sonu "Bu nedenle doğru cevap X seçeneğidir. (MD …)" ya da harfli benzeri), madde, kanit, cikmis, batch, konu.
- Kaynak: metin/ (gümrük mevzuatı, 5607 ve yönetmelikleri, İthalat Rejimi Kararı + 2025 değişikliği, silah-mühimmat, Canli_7_24_Genel_Kultur_Kitabi.txt). Çıkmış sınavlar: sinav/ (B kitapçıkları), sinavA/2025A.txt. Resmî cevaplar: cikmis_envanter.tsv RESMI_CEVAP sütunu.
- Kurallar: promptlar/prompt-3-nihai-soru-hazirlama-kurallari.md ve CLAUDE.md (Karar dayanaklı kök kuralı).

Her soru için:
1. İşaretli doğru şık kaynağa göre KESİN doğru mu? Hükmü kaynakta bul, çevresini oku (istisnalar, dipnotlu değişiklikler, "mülga" ibareleri, sonradan gelen değişik metinler). Hesap/tarih sorularını Python ile yeniden yap.
2. Başka bir şık da savunulabilir mi (ÇİFT DOĞRU)? Olumsuz kökte tek şık mı yanlış? Önermelide her öncülü ayrı değerlendir.
3. Gerekçe ve içindeki harf doğru şıkla uyumlu mu?
4. Kaynakta olmayan rakam/süre/makam/bilgi (doğru şıkta, gerekçede, kökteki olay verisinde) var mı? Eski-yeni kurum adı rakip şık olmuş mu?
5. Kök kuralları: madde/fıkra numarası kökte/şıkta yok; Karar dayanaklı kök "4458 sayılı …" ile başlamıyor; kök mevzuat adı + hükmün konusu içeriyor.
6. cikmis alanındaki çıkmış soruyu bul: metin/şık/kurgu KOPYASI var mı (aynı bilgi serbest)?
7. Özel riskler (varsa senin aralığında kontrol et):
   - DİR Tebliği (32-DAHİLDE İŞLEME.txt) "Mülga" başlıklı 45. ve 46. maddelere dayanan sorular hâlâ geçerli mi?
   - GK 241/1 yanında AYM 26.03.2026 kararına atıf var; 241/1'in ikincil düzenleme kapsamına veya TL tutarına dayanan soru olmamalı.
   - Posta/hızlı kargo: 2009/15481 Kararının 2026 değişikliği; resmî 2025 cevabı (2025/76) ile güncel metin çelişiyor — soru güncel metne göre doğru mu?
   - "GTS / Hariç Sektörler", "Form A", "Seri No:149", "3351", "Ek-9 sayısal limit" gibi kaynakta OLMAYAN bilgiye dayanan soru var mı?
   - Genel kültür sorularında bilgi kitapta var mı, tek doğru mu?
8. Aynı sette iki sorunun aynı hükmü/çekirdeği ölçüp ölçmediğine bak.

Çıktı: kısa rapor. Yalnız SORUNLU sorular: set/no, tür (YANLIŞ CEVAP / ÇİFT DOĞRU / KAYNAK DIŞI / GÜNCEL DEĞİL / KOPYA / GEREKÇE UYUMSUZ / KÖK KURALI / BELİRSİZ / TEKRAR), kanıt (dosya + birebir alıntı), SOMUT düzeltme (hangi şık/öncül/kök metni nasıl olmalı; doğru cevap değişiyorsa yeni doğru şık metni). Sorunsuzları aralıkla say. Şüpheleri "ŞÜPHE" diye ayrı ver.
