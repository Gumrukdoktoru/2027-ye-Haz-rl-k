# Sağlamlaştırma Talimatı (Deneme 6–10, ikinci geçiş)

Klasör: `araclar/gmy-deneme6-10` (bütün yollar buna göre). Görev dosyan `gorev/G<n>.md`: hangi soruların sana ait olduğunu, hangi batch dosyalarını düzenleyebileceğini ve her sorunun değişmez plan kısıtlarını gösterir. **Yalnız kendi batch dosyalarını düzenle**; `set*.json`, `plan.json`, `kontrol.py` ve başka ajanların batch dosyalarına dokunma. Git işlemi yapma.

## 0. Neden bu geçiş?
Kullanıcı Deneme 6'nın 53. sorusunda iki zayıflık buldu:
1. **Deneme 1–5 ile örtüşme:** doğru cevabın dayandığı cümle Deneme 5'in 83. sorusunda E şıkkı olarak (olumsuz kökte doğru ifade) neredeyse aynen geçiyor. Önceki tekrar denetimi (`dogrulama/T2.md` §C) bunu “eşik altı” sayıp bırakmıştı.
2. **Cevap ipucu (yakınsama):** şıklar “süre + sonraki işlem” ikilisi; “dokuz ay” B ve D'de, “yeni izinle azami yirmi dört ay” A ve D'de geçiyor. Sınav kurnazı öğrenci, iki popüler yarıyı birleştiren tek şık olan D'yi hükmü bilmeden seçer. Kök de ilk okumada kendi kendisiyle çelişiyor gibi okunuyor.

Bu geçişte aynı türden zayıflıkları giderip soruları sağlamlaştırıyoruz. Soruları yeniden yazmak amaç değil; gerektiği kadar değiştir.

## 1. Kaynaklar
- **Birincil kaynak `metin/`** (kanıt alıntıları buradan, `kontrol.py` burada arar).
- Kullanıcının GitHub kaynağı `/home/user/gumrukdoktoru/2027gmynot/`:
  - `GUMRUK_MEVZUATI_TUMU.md`, 0–51 konu dosyalarının derlemesi. `metin/` ile **aynı mevzuat sürümü** (değişiklik tarihleri birebir aynı). Farklar dönüştürmede düşen bağlantılı kelimelerden ibaret, yani hüküm farkı yok. Gerekirse çapraz kontrol için kullan.
  - İRK Markdown'ları: `metin/` ile aynı içerik.
  - `kaçakçılık.md`: 5607 sayılı Kanunun **sunum notları**. İkincil kaynaktır; Kanun metniyle çelişirse Kanun metni (`metin/5607_sayili_kacakcilikla_mucadele_kanunu.txt`) esastır.
- Web yok, hafızadan bilgi yok.

## 2. Her soru için üç kontrol
### A. Deneme 1–5 örtüşmesi (T2 §C sütunu doluysa)
Eski soruyu aç:
- `GMY-xxx` → `../../sorular/GK_GMY2025_Deneme_S1_100soru.md`
- `GMYn-xxx` → `../../sorular/GK_GMY_Deneme{n}_100soru.md`

Soruyu numarasıyla bul; şıklar, öncüller ve gerekçe birlikte okunur. Eski sorunun çekirdekleri ayrıca `../../sorular/hafiza/URETIM-HAFIZASI.md` dosyasında da var.
- **GÜÇLÜ örtüşme:** yeni sorunun doğru cevabı ya da cevabı belirleyen hüküm, eski soruda öğrencinin **doğru diye okuduğu** bir yerde geçiyorsa. Bu yerler: eski sorunun cevabı, doğru öncül, olumsuz kökte doğru ifade olan şık, kökte verilen bilgi, eşleştirmede doğru çift. Bu durumda **kilidi değiştir**: aynı bilgi alanında (aynı rejim / bölüm / mümkünse komşu madde) kullanılmamış başka bir hükmü sor. Bu hüküm hafızada (`URETIM-HAFIZASI.md`), diğer D6–10 sorularında (`set6.json` … `set10.json` içinde `grep`) ve çıkmış sorunun (`sinav/<yıl>_duz.txt`) ölçtüğü hükümde bulunmamalı.
- **ZAYIF örtüşme:** hüküm eski soruda yalnız **yanlış çeldirici** olarak geçiyorsa soru kalır. İfade eski soruyla neredeyse aynıysa yalnız ifadeyi farklılaştır.

### B. Cevap ipucu (sınav kurnazlığı)
- **Yakınsama:** doğru şık, öteki şıklarda en sık geçen bileşenleri birleştiren tek şıksa. İki ya da üç bileşenli şıklarda değer kümelerini dengele: doğru şıkkın her bileşeni, rakip değerlerle eşit sıklıkta geçmeli; doğru kombinasyon “en popüler yarıların birleşimi” olmamalı. Gerekirse bir çeldiriciyi yakınsama noktası yap.
- **Kök–şık kelime ortaklığı:** doğru şık kökteki kelimeleri tekrar ederken çeldiriciler etmiyorsa çeldiricilere de kökle aynı ölçüde bağ kur ya da doğru şıkkı farklı kelimelerle ifade et.
- **Otomatik bayrak** (`YAKINSAMA`, `BİLEŞEN`, `KÖK-ORTAK`) yalnız bir aday listesidir. Boşluk doldurma (T5) ve kısa sayısal şıklarda (T3) benzerlik doğaldır; çoğu yanlış alarm olabilir. Gerçek bir ipucu yoksa dokunma ve raporda bir cümleyle gerekçelendir. Bayraksız sorularda da bu iki ipucuna bak.

### C. Kök ve tek doğru
- Kök ilk okumada anlaşılır mı, kendi kendisiyle çelişiyor gibi mi okunuyor (D6-053 örneği), dolambaçlı mı? Gerekirse sadeleştir.
- Tek ve tartışmasız doğru cevap var mı? Her çeldirici için “neden yanlış” cümlesi kurulabiliyor mu?
- Açıklama (`g`) doğru şıkla ve çeldiricilerle uyumlu mu?

## 3. Değişiklik kuralları
- `YAZAR_TALIMAT.md` §2–§6 aynen geçerli: kök kuralları (mevzuat adı + hükmün konusu + kalıp; madde/fıkra numarası kökte ve şıkta yok; 2009/15481 Karar kalıbı; olumsuz kelime `[[…]]`), kapsam (GMY: Gümrük Kanunu ve ikincil düzenlemeleri, 5607 ve ikincil düzenlemeleri, İRK, DİR Tebliği, Sınır Ticareti Kararı), şık uzunluk dengesi ve alanlar.
- Plan kısıtları **değişmez:** tip, şık sınıfı, ters tuzak, kök bandı, harf (görev dosyasındaki “plan” sütunu). Sabit sıralı şıklarda (`opts`) doğru şık planlanan harfin konumunda kalır.
- Kilit değişirse `cek`, `madde`, `g`, `kanit` alanlarını da güncelle. `kanit` alıntıları `metin/` içinden birebir olmalı; `id` ve `cikmis` aynı kalır.
- Her düzenlemeden sonra `python3 kontrol.py batch_<X>.py` çalıştır; sonuç “GENEL SONUÇ: TEMİZ” olmalı. `??` uyarılarını oku: hafızadaki bir çekirdekle aynı hükmü soruyorsan başka hüküm seç.
- Bir batch dosyasında bir soruyu değiştirirken aynı dosyadaki öteki soruların metnini bozma (Python dict sözdizimi; tırnak türüne dikkat).
- Genel kültür sorusu (GTA) için kaynak `metin/Canli_7_24_Genel_Kultur_Kitabi.txt`; aynı ders ve soru türü korunur.

## 4. Rapor
Raporu `dogrulama/<G>.md` dosyasına yaz. Kesinti olursa iş kaybolmasın diye her soru bitince dosyaya ekle. Her soru için tek satır:

`D6-053 — DEĞİŞTİ (kilit + çeldirici + kök) — gerekçe … — eski: … → yeni: …`
ya da
`D7-043 — AYNI — gerekçe (ör. T5 boşluklarında ortak kelime doğal; gerçek ipucu yok)`

Sonda bir özet ver: değişen soru sayısı, kilidi değişenler, `kontrol.py` sonucu. Son mesajında da aynı özeti ver.

## 5. 5607 sunum notları karşılaştırması (yalnız G5)
Görev dosyandaki 28 sorunun her birinde doğru şıkkı, çeldiricileri ve açıklamayı `kaçakçılık.md` ile karşılaştır.
- Notlar soruyla **çelişiyorsa** önce Kanun metnini oku.
  - Soru Kanuna aykırıysa düzelt.
  - Notlar Kanunun eski hâlini ya da hatalı bir özetini veriyorsa soru değişmez; raporda “NOT FARKI” diye yaz, alıntıları ver.
- Notlar bir çeldiriciyi savunulabilir kılıyorsa (ör. kurum uygulaması ya da istisna) ve Kanun da buna izin veriyorsa çeldiriciyi değiştir.
- Notlarda soruyla ilgili ek bir istisna ya da şart varsa ve bu, sorunun tek doğru cevabını tehlikeye atıyorsa düzelt.
