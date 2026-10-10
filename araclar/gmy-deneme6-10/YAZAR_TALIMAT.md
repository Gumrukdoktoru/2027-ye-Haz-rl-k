# GMY Deneme 6–10 — Soru Yazarı Talimatı

Çalışma klasörü: `araclar/gmy-deneme6-10` (bütün yollar buna göre). Git işlemi yapma; yalnız kendi `batch_<GÖREV>.py` dosyanı yaz.

## 0. Ne üretiyoruz?
Beş deneme, her biri bir çıkmış sınavın **100 sorusunu birebir karşılar**:
Deneme 6 ← 2021 · Deneme 7 ← 2022 · Deneme 8 ← 2023 · Deneme 9 ← 2024 · Deneme 10 ← 2025 (B kitapçığı numaraları).
Denemedeki n. soru, model sınavın n. sorusunun **bilgi alanını** ölçer: 1–20 genel kültür, 21–100 gümrük mevzuatı.
Görev dosyan `gorev/<GÖREV>.md`: her satır yazacağın bir soru. Hepsini yaz (eksik bırakma).

## 1. Okuman gerekenler
- `../../promptlar/prompt-4-gmy-soru-motoru-master.md` (MASTER — tipler, kök, şık uzunluk dengesi, çeldirici teknikleri, yasaklar, 10 maddelik protokol)
- `../../promptlar/prompt-3-nihai-soru-hazirlama-kurallari.md` (kurum kalıpları §5, madde no yasağı §7, kök = MEVZUAT ADI + HÜKMÜN KONUSU + KALIP §8, çeldirici §11–13, çıkmış soru §14, eski-yeni kurum adı §17)
- `../../CLAUDE.md` (kapsam ve Karar kökü kuralı)
- `ornek_format.py` (biçim örneği — içeriğini kopyalama)
Çelişkide öncelik: **bu talimat > Prompt 4 > Prompt 3**.

## 2. Bilgi alanı ve özgünlük (en önemli kural)
- Her satır için çıkmış soruyu ham metinden oku (`sinav/<yıl>_duz.txt` okuma sırasında; `sinav/<yıl>.txt` sayfa düzeninde; 2025 için `sinav/2025B_duz.txt`). Görev satırındaki "ölçtüğü bilgi" envanter özetidir.
- Yeni soru **aynı konuyu ve aynı bilgi alanını** (aynı rejim/kurum/düzenleme bölümü, mümkünse aynı veya komşu madde) ölçer; ama **çıkmış sorunun ölçtüğü hükmün aynısını sormaz** (CLAUDE.md: "aynı konu sorulursa farklı hüküm seçilir"). Metin, şık ve kurgu kopyası yasak.
- `hafiza/<GÖREV>.txt` önceki 500 sorunun çekirdekleridir: bunlarla **aynı çekirdeği** (aynı süre, makam, tanım, eşik, istisna, belge) sorma. Aynı maddenin başka hükmü serbesttir. Kendi batch'inde de aynı hükmü iki kez sorma.
- Çıkmış sorunun kaynağı depoda yoksa (envanterde `YOK`) ya da GMY kapsamı dışındaysa, aynı konudaki en yakın **kaynakta bulunan** hükmü seç.
- **Kapsam (gümrük bölümü):** yalnız Gümrük Kanunu ve ikincil düzenlemeleri, 5607 sayılı Kanun ve ikincil düzenlemeleri; ayrıca GMY'de fiilen sorulan İthalat Rejimi Kararı, Dahilde İşleme Rejimi Tebliği, Sınır Ticareti Kararı. Bedelsiz ihracat, İhracat Yönetmeliği, e-ihracat, kambiyo, fuar tebliği, silah-mühimmat tahsisi **sorulmaz**.
- **Tek bilgi kaynağı `metin/`** (depoya yüklenen dosyalar). Web yok, hafızadan bilgi yok. Kaynakta olmayan rakam, süre, makam, seri no, madde no yazma. Dipnotlu değişikliklere, "mülga" ibarelerine ve sonradan gelen değişik metinlere dikkat et; güncel metni esas al.

## 3. Plan kısıtları (görev satırında: tip · şık sınıfı · ters tuzak · kök bandı · harf)
**Tip** (master §3):
- T1 olumsuz kök ("…hangisi [[değildir]]/[[yanlıştır]]/[[girmez]]…?"); 4 şık mevzuattan doğru, 1 şık tek unsur çevrilerek yanlış.
- T2 öncüllü (3–5 öncül; tercihen 4; "Yukarıdakilerden hangileri doğrudur?"). Öncüllerin doğru/yanlış dağılımı her soruda farklı olsun; "hepsi doğru" istisnai.
- T1+T2 olumsuz köklü öncüllü ("Yukarıdaki ifadelerden hangileri [[yanlıştır]]?").
- T3 süre/eşik/oran ("**kaç gün**…"); çeldiriciler mevzuattaki gerçek başka eşikler. Sınıf **kısa** ise şıklar sayısal ("15 gün", "%10", "2 kat") ve **artan sırada `opts`** ile verilir; sınıf **orta** ise başlangıç noktası + süre birlikte ("Tebliğ tarihinden itibaren 15 gün") ve sıralama serbest.
- T4 doğrudan bilgi / olumlu kök ("…hangisidir / hangisi doğrudur?").
- T5 boşluk doldurma (mevzuat cümlesinde "……" boşluk; "Yukarıda boş bırakılan yerlere **sırasıyla** aşağıdakilerden hangisi gelmelidir?"; çoklu boşlukta çapraz tuzak).
- T6 tanım → kavram/belge (tanım tırnak içinde; "Yukarıda tanımlanan … aşağıdakilerden hangisidir?"; çeldiriciler komşu rejim/belge adları).
- T7 makam/yetki ("…hangi idare / kim tarafından …?").
- T8 olay-vaka (hesapsız; somut senaryo → hukuki sonuç). Kişi/firma etiketleri (K), (L), (M), (X), (Y) — A–E kullanma.
- T9 hesaplama (kıymet/ceza/vergi; Python ile hesapla; çeldiriciler tipik hata sonuçları; TL şıkları **artan `opts`**; her yıl yeniden değerlenen TL tutarlarını sorma ya da esas tutarı kökte ver).
- T10 tablo/eşleştirme (kökte en az 4 numaralı satır "1. … – …"; şıklar "Yalnız 2", "1 ve 3", "2, 3 ve 4" merdiveniyle `opts`).

**Şık sınıfı:** kısa = 5 şıkkın her biri ≤4 kelime; orta = arada (hedef 5–15 kelime); uzun = 5 şıkkın **her biri** ≥20 kelime.

**Ters tuzak = EVET:** doğru şık bilinçli olarak en uzun; 2. ve 3. en uzun şık doğru şıkkın en az %90'ı uzunluğunda.
**Ters tuzak = hayır:** doğru şık tek başına en uzun da en kısa da olamaz; doğru şıkkın ±%10 bandında (en az ±3 karakter) en az 2 çeldirici; en az 1 çeldirici doğru şıktan uzun (≤15 karakterlik şıklarda eşit uzunluk yeter). Uzatma master §5.2 tekniğiyle; anlamsız dolgu yasak.

**Kök bandı:** kökün tüm metni (öncüller, olay, alıntı dahil; şıklar hariç; işaretler hariç) karakter sayısı: ≤120 / 120–350 / 350–700 / >700. Denetleyici biraz tolerans tanır.

**Harf:** Sabit sıralı şıklarda (T2, T1+T2, T10 merdiveni; kısa T3 sayısal; T9 tutarları) `opts` alanında 5 şıkkı gösterim sırasıyla ver; doğru şık **planlanan harfin konumunda** olmalı — bunu çeldirici değerlerini/kombinasyonlarını seçerek sağla (ör. harf A ise doğru değer en küçük olsun; öncüllüde merdiven tekli kombinasyonla başlamak zorunda değil). Diğer bütün sorularda `opts` verme; birleştirici doğru şıkkı planlanan harfe yerleştirir.

Bir plan kısıtı (tip, sınıf, bant, tuzak) o bilgi alanında doğal olarak gerçekten kurulamıyorsa `sapma='kısa gerekçe'` yaz. Batch başına en çok 2 sapma; harf ve uzunluk dengesi için sapma yok.

## 4. Kök
- Gümrük sorularında kök **mevzuat adıyla açılır** veya mevzuat adını içerir; MEVZUAT ADI + HÜKMÜN KONUSU + KALIP: "4458 sayılı Gümrük Kanununa göre, transit rejiminde teminat … ilişkin aşağıdakilerden hangisi [[yanlıştır]]?"
- Yönetmelik/Tebliğ/Karar kökleri dayanağın türünü baştan gösterir: "Gümrük Yönetmeliğine göre …", "Gümrük Genel Tebliği (Transit Rejimi) (Seri No: 4)'e göre …" (seri no kaynakta aynen varsa).
- 2009/15481 sayılı Karar: kök **"4458 sayılı …" ile başlamaz**; kalıp: `2009/15481 sayılı "4458 sayılı Gümrük Kanununun Bazı Maddelerinin Uygulanması Hakkında Karar"a göre …`
- Madde/fıkra/bent numarası kökte ve şıkta yok (madde no yalnız `madde` alanına ve açıklamanın sonundaki (MD …) parantezine).
- Olumsuz kelime `[[değildir]]` biçiminde işaretlenir (çıktıda koyu + altı çizili). Kritik nicelik ifadeleri `**en az**`, `**kaç gün içinde**`, `**sırasıyla**` biçiminde koyu.
- Yasak: "kaynak metne göre", "verilen metinde", "yukarıdaki kaynağa göre", "temel kural/temel özellik/kritik husus" gibi yapay nitelemeler, bağlamsız "…Kanununa göre aşağıdakilerden hangisi doğrudur?".

## 5. Şıklar
5 şık; "hepsi/hiçbiri/tümü" yok; 5 şıkta sonda nokta kullanımı aynı; dilbilgisel paralellik; aynı kategoride şıklar; eski–yeni kurum adı rakip şık değil; "asla / her zaman / hiçbir şekilde" çeldirici işareti gibi sırıtmasın. T1'de doğru 4 ifade mevzuat diline sadık, yanlış ifade tek unsur değişikliğiyle (taraf, yön, kapsam, süre başlangıcı, makam, müeyyide).

## 6. Alanlar (`batch_<GÖREV>.py` içinde `Q = [dict(...), ...]`, deneme ve soru no sırasıyla)
- `id` görev satırındaki id (ör. "D7-074"), `cikmis` (ör. "2022/74"), `konu`
- `tip` (plandaki), `z` "OÜ" (orta üstü) veya "Z" (zor) — hedef yaklaşık %60 OÜ / %40 Z; kolay soru yazma
- `madde` Yasal Dayanak, tam adlarla ve gerçek madde no ile: "4458 sayılı Gümrük Kanunu m.92/1; Gümrük Yönetmeliği m.240"
- `cek` ≤25 kelime: ölçülen hüküm + doğru cevabın özü (hafıza satırı olur)
- `kok` liste: ilk eleman giriş/soru; öncüller ayrı elemanlar "I. …"; tablo satırları "1. …"; son eleman soru cümlesi
- `d` doğru şık, `c` 4 çeldirici (liste), gerekiyorsa `opts` (gösterim sırası, 5 şık)
- `tuzak` True/False (plandaki)
- `g` açıklama: 2–4 cümle; doğru cevabın gerekçesi + en güçlü 2 çeldiricinin neden yanlış olduğu; şıkları **harfle değil metinle** an; "Bu nedenle doğru cevap …" yazma (birleştirici ekler); en sonda kısa atıf: "(MD GK 92/1; GY 240)"
- `kanit` "dosya.txt | kaynaktan birebir alıntı (≤40 kelime)"; birden çok kanıt " || " ile; atlanan kısım "…" ile. Denetleyici alıntıyı dosyada arar (büyük/küçük harf, boşluk, tırnak farkları normalize edilir).
- `sapma` (yalnız gerekirse)

## 7. Denetim ve teslim
1. `python3 kontrol.py batch_<GÖREV>.py` → "GENEL SONUÇ: TEMİZ" olana kadar düzelt. `??` uyarılarını incele: hafızadaki bir çekirdekle gerçekten aynı hükmü soruyorsan soruyu değiştir.
2. Her soru için master §9 protokolünü kendin uygula; özellikle: tek ve tartışmasız doğru cevap var mı, her çeldirici için "neden yanlış" cümlesi kurulabiliyor mu, T1'de yalnız bir şık mı yanlış, T2'de her öncülü ayrı ayrı kaynağa göre değerlendirdin mi, hesapları Python ile yaptın mı.
3. Kısa rapor (en fazla 15 satır): yazılan soru sayısı, sapmalar, kaynakta bulunamadığı için yakın hükümle karşılanan çıkmış sorular, emin olmadığın noktalar.

## 8. Genel kültür görevleri (GTR, GMA, GTA, GAN)
- Her satır, model sınavın aynı numaralı genel kültür sorusunu karşılar: **aynı ders ve aynı soru türü** (ör. yazım/noktalama kuralı, sözcükte anlam, paragrafın ana düşüncesi, cümle türü; problem türü; tarih olayı/kronoloji/antlaşma; anayasal organ, hak, yargı), farklı içerik. Kopya yok; `hafiza/<GÖREV>.txt` çekirdeklerini tekrar etme.
- Bilgi kaynağı `metin/Canli_7_24_Genel_Kultur_Kitabi.txt` (Türkçe kuralları, tarih, anayasa, uluslararası kuruluşlar): `kanit` bu kitaptan birebir alıntı. Matematik ve özgün paragraf/cümle metnine dayanan Türkçe sorularında `kanit='ÖZGÜN – …'` yazılabilir; matematik sonuçlarını Python ile doğrula.
- Gümrük'e özgü kurallar (mevzuat adı, şık sınıfı, kök bandı, ters tuzak) uygulanmaz; uzunluk dengesi kuralı (ters tuzak = hayır) uygulanır — paragraf sorularında gerçekten kurulamıyorsa `sapma`.
- `tip` olarak en uygun kodu seç (T1 olumsuz kök, T2 öncüllü, T4 doğrudan, T5 boşluk, T6 tanım→kavram, T9 hesap vb.); `z` "O", "OÜ" veya "Z"; `madde` alanına "Genel Kültür Kitabı – <ders>: <konu>" yaz; açıklama yine "(MD …)" ile biter (ör. "(MD Genel Kültür Kitabı – Türkçe: Yazım kuralları)").
- Sayısal şıklar artan `opts` ile ve doğru şık planlanan harfte. 2022 sınavının 7–8. matematik soruları görseldir: `pdftoppm -f <sayfa> -l <sayfa> -png ../../2022-gmy-sinavi-cevapli.pdf /tmp/...` ile sayfayı resme çevirip okuyabilirsin.
