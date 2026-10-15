# Son Doğrulama Talimatı (Deneme 11–15, V1–V6 sonrası; S1–S2)

Klasör: `araclar/gmy-deneme11-15` (bütün yollar buna göre). Görev dosyan `gorev/S<n>.md`. Orada iki şey var: doğrulayacağın sorular (V1–V6 doğrulaması, koordinatör düzeltmeleri ve merdiven dengelemesi sırasında kökü, şıkları ya da doğru cevabı değişen sorular) ve **düzenleyebileceğin batch dosyaları**.

Başka dosyaya dokunma. `set*.json`, `plan.json` ve `kontrol.py` değişmez. Git işlemi yapma.

## Soruların hâlleri
- **Güncel hâl:** batch dosyalarında ve `set11.json` … `set15.json` içinde. `opts` gösterim sırasıdır, `harf` doğru cevaptır.
- **Değişikliğin gerekçesi:** `dogrulama/V1–V6.md` raporlarında.
- **Önceki hâl:** `git show d96fd4f:araclar/gmy-deneme11-15/batch_<X>.py` ile görebilirsin.

## Her soruda yapılacak kontroller
1. `DOGRULAYICI_TALIMAT.md`'deki on üç kontrolün hepsini uygula. Bunlar:
   - doğru cevap kesin mi; çift doğru var mı;
   - açıklama uyumlu mu; kaynak dışı bilgi var mı;
   - kök kuralları; kapsam;
   - çıkmış soru kopyası;
   - şık kalitesi; aynı hüküm;
   - Deneme 1–10 örtüşmesi; cevap ipucu;
   - deneme içi sızıntı; dilbilgisi.
2. Kaynak `metin/`'dir. Genel kültür için kaynak `metin/Canli_7_24_Genel_Kultur_Kitabi.txt`'dir. Markdown derleme (`/home/user/gumrukdoktoru/2027gmynot/GUMRUK_MEVZUATI_TUMU.md`) aynı mevzuat sürümüdür. Web ve hafızadan bilgi kullanılmaz.
3. **Örtüşme:** `python3 eski_ilgili.py batch_<X>.py` ilgili eski soruları listeler. Eski soruları dosyalarından aç ve oku:
   - `GMY-xxx` → `../../sorular/GK_GMY2025_Deneme_S1_100soru.md`
   - `GMYn-xxx` → `../../sorular/GK_GMY_Deneme{n}_100soru.md`

   Sorun sayılan durum: yeni doğru cevap ya da cevabı belirleyen hüküm, eski bir soruda öğrencinin doğru diye okuduğu bir yerde geçiyorsa. Bu yerler:
   - eski sorunun cevabı;
   - doğru öncül;
   - olumsuz kökte doğru şık;
   - kök bilgisi;
   - doğru eşleştirme;
   - çözümdeki “tuzak nokta” notu.

   Eski soruda yalnız yanlış çeldirici ya da gerekçe olarak geçmesi sorun değildir.

   Çıkmış sınavlar (`sinav/<yıl>_duz.txt`): model alınan soru dışındaki bir çıkmış soruda doğru ifade olarak birebir geçen hükmü aynı açıdan yeniden sormak sorundur.
4. **Sızıntı:** aynı denemedeki öteki sorularda (`setN.json` içinde `grep`) bu sorunun cevabı geçiyor mu, ya da bu soru başkasının cevabını veriyor mu?
5. `(m)` işaretli sorularda değişiklik çoğunlukla yalnız çeldirici kombinasyonlarıdır (`merdiven_dengele.py --yaz`). Doğru kombinasyonu öncüllerden kendin bul ve şıklarda tek olduğunu doğrula.

## Düzeltme kuralları
- Bulduğun her sorunu **kendi batch dosyalarında** düzelt.
- Plan kısıtları değişmez: tip, şık sınıfı, ters tuzak, kök bandı, harf.
- `YAZAR_TALIMAT.md` §2–§6 ve §2A geçerlidir.
- Kilit değişirse `cek`, `madde`, `g` ve `kanit` alanları da güncellenir.
- `python3 kontrol.py batch_<X>.py` sonucu “GENEL SONUÇ: TEMİZ” olmalı.
- Öncüllü bir soruda öncülleri değiştirirsen `python3 merdiven_dengele.py` çalıştır ve kendi sorunun için öneri olup olmadığına bak. Araç `--yaz` olmadan dosyaya yazmaz; öneri varsa merdiveni elle uygula.
- Batch dosyaları Python dict'idir. Tek tırnaklı dizgilerde kesme işareti `\'` olarak yazılır.
- **Değiştirme eşiği:**
  - Değiştir: yanlış cevap, çift doğru, kaynak dışı bilgi, güçlü örtüşme, gerçek ipucu, sızıntı, kök kuralı ihlali, anlaşılmaz kök.
  - Değiştirme: yalnız üslup tercihi.

## Rapor
Raporu `dogrulama/S<n>.md` dosyasına yaz. Kesinti olursa iş kaybolmasın diye her batch bitince dosyaya ekle.

Rapor sırası:
1. Önce sorunsuz soruları aralıkla say.
2. Sonra her sorun için şu biçimde bir satır yaz: `id` — tür — kanıt (dosya + birebir alıntı) — yaptığın düzeltme. Tür şunlardan biridir: YANLIŞ CEVAP / ÇİFT DOĞRU / KAYNAK DIŞI / GÜNCEL DEĞİL / KOPYA / AYNI HÜKÜM / GEREKÇE UYUMSUZ / KÖK KURALI / KAPSAM DIŞI / ZAYIF ÇELDİRİCİ / BELİRSİZ / ÖRTÜŞME / İPUCU / SIZINTI.
3. Sonda şunları ver: değişen soru sayısı ve her dosya için `kontrol.py` sonucu.

Son mesajında da aynı özeti ver.
