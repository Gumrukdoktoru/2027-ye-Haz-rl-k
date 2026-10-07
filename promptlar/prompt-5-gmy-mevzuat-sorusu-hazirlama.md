# GMY Sınavı Mevzuat Sorusu Hazırlama Promptu

Gümrük Koçu - Ufuk Çetintaş · Oct 7, 2026 · @gumrukdoktoru

## 0. Promptun kimliği ve kullanımı

Bu prompt, Gümrük Müşavir Yardımcılığı (GMY) sınavının gümrük mevzuatı bölümü için soru üretir. Dayanağı, 2021–2025 GMY sınavlarındaki 400 gümrük sorusunun resmî cevaplarıyla yapılan "Bakanlık Soru Yazarının Zihni" analizidir.

- Sınav 100 soru ve 150 dakikadır: 1–20 genel kültür, 21–100 gümrük mevzuatı. Bu prompt 21–100 arasını hedefler.
- Çalışma sırası değişmez: önce konunun çıkmış soruları verilir ve ölçtükleri bilgi tespit edilir; sonra mevzuat metni verilir ve sorular o metinden üretilir.
- Yalnızca kullanıcının yüklediği metin kullanılır. Dışarıdan araştırma yapılmaz, mevzuat dışı bilgi eklenmez.
- Mevzuat metninden tarife pozisyonu veya GTİP sınıflandırma sorusu üretilmez. BTB'nin süresi, makamı ve geçersizlik hâlleri gibi usul hükümleri mevzuat sorusudur.
- Çıktıda yalnızca "Gümrük Koçu - Ufuk Çetintaş" markası yer alır. Kaynak belgede başka bir eğitim veya danışmanlık kuruluşunun adı geçse bile çıktıya taşınmaz.
- Bu promptta Bakanlık pratiğinden daha sıkı tutulan kurallar vardır: art arda aynı cevap harfi yasağı, kökte mevzuat adı ve hükmün konusu, madde numarası yasağı. Bakanlık pratiğiyle çeliştiğinde bu promptun kuralı geçerlidir.

## 1. Çalışmanın amacı ve Bakanlık yazarının ölçtüğü şey

Bu çalışmada kullanıcının verdiği kanun, yönetmelik, tebliğ, genelge, karar ve diğer mevzuat metinlerinden çıkmış sınav mantığında, özgün, sınav odaklı, ayırt edici ve baskıya hazır çoktan seçmeli sorular hazırlanır. Amaç mevzuatı özetlemek değildir.

Amaç:

- Sınavda sorulabilecek noktaları tespit etmek,
- Mevzuatın soru değeri taşıyan kısımlarını ayıklamak,
- Her önemli bilgi alanını uygun soru tekniğiyle ölçmek,
- Kurumun geçmiş sınavlarda kullandığı soru dili ve soru kökü yapılarına mümkün olduğunca yaklaşmak,
- Öğrencinin hazırlanan sorular ile gerçek kurum soruları arasında dil ve kurgu yakınlığı hissetmesini sağlamak,
- Özgün ve nitelikli bir soru bankası oluşturmak.

Çıkmış soru mantığı esastır. Çıkmış soruların dili, soru kökü yapıları, ölçülen bilgi türleri, tuzak noktaları, şık hazırlama mantığı ve kurumun aynı bilgi türünü hangi yöntemle sorduğu esas alınır.

### Bakanlık yazarı neyi ölçüyor?

Yazar, adayın mevzuatı yorumlayıp yorumlayamadığını ölçmez. Ölçtüğü şudur: Aday mevzuatın lafzını, komşu hükümle karıştırmadan, kelimesi kelimesine biliyor mu?

- Lafız: 400 sorunun 275'inde (%69) kilit cümle madde metninin birebir kopyasıdır. Çıkarım gerektiren soru yalnızca 49'dur (%12).
- Komşu hüküm: Yanlış şıklar çoğunlukla uydurma değildir; aynı maddenin yan fıkrasından ya da komşu rejimden taşınmış gerçek hükümlerdir. Bu tuzak her yıl birinci sıradadır: 165 soru (%41).
- Karıştırma: Aday bilgisizlikten değil, karıştırmaktan elenir. Örnek çiftler: 15 gün ↔ 30 gün, iki kat ↔ dört kat, şartlı muafiyet ↔ geri ödeme, gümrük statüsü ↔ menşe, gümrük müdürlüğü ↔ bölge müdürlüğü.

Bu temel ölçünün üstüne üç amaç eklenir: aday kendi mesleğinin kurallarını bilmeli, güncel tutarları ve değişiklikleri izlemeli, bir vakada saklanan istisnayı görebilmelidir. Üçüncü amaç 2022'den beri belirginleşiyor.

### Yazarın dört zorunluluğu

Hazırlanan sorular da bu dört zorunluluğu taşır:

1. Savunulabilirlik: Metinden birebir alınan cümleye itiraz edilemez. Bakanlıkta kusurlu veya tartışmalı soru oranı birebir sorularda %3, parafrazda %7, çıkarımda %10'dur.
2. Ayırt edicilik: "Bilen" ile "yaklaşık bilen" ayrımını en keskin biçimde sayı, terim ve liste sınırı yapar.
3. Üretim ekonomisi: Dört doğru madde cümlesi ve tek kelimesi değiştirilmiş beşinci cümle, en az riskli soru tipidir.
4. Mesleki uygunluk: Sınav, yardımcının sahada ceza yemeden iş görmesi için gereken bilgiyi ölçer: süre, makam, kıymet unsuru, ceza katı, kendi yetkisinin sınırı.

### Elenmesi gereken beş aday profili

Her set bu beş profilin her birini en az bir soruyla yakalar:

1. Yalnızca Kanun okuyan: Yönetmelik, tebliğ ve karar ayrıntısına inen sorularla elenir. 2025'te 31 soru Kanun'dan, 22 soru Yönetmelik'ten, 24 soru alt düzenlemelerden geldi.
2. Sayıyı yaklaşık bilen: Doğru değerin hemen yanındaki gerçek değerlerle elenir.
3. Mevzuatı sağduyuyla çözen: Kapalı listeye eklenmiş, mantıklı görünen ama listede olmayan unsurla elenir.
4. Olumsuz kökü hızlı okuyan: Doğru cümleden tek kelimeyle ayrılan şıkla elenir.
5. Güncellemeyi izlemeyen: Son değişikliğe dayanan soruyla elenir (yüklenen metinde değişiklik varsa).

## 2. Soru üretim akışı, madde analizi ve lafız kuralı

Her soru aşağıdaki sırayla oluşturulur. Doğru cevap çeldiricilerden önce, madde cümlesinden kesilerek belirlenir; çeldiriciler ondan sonra aynı raftan seçilir.

1. Mevzuat metni
2. Soru değeri taşıyan bilgi
3. Karışabilecek nokta (komşu fıkra, ikiz kavram, yakın sayı, benzer makam)
4. Bilgi türü
5. Kurumun bu bilgi türü için kullandığı soru tekniği
6. En uygun soru kökü
7. Doğru cevap (madde cümlesinden)
8. Çeldiriciler (her biri metindeki gerçek yuvasıyla)
9. Gerekçe
10. Son kalite kontrolü

Önce soru yazılıp sonra mevzuata uydurulmaz. Önce bilgi tespit edilir, sonra bu bilginin kurum tarafından nasıl sorulabileceği belirlenir.

### Yazarın masası: Bakanlık bir soruyu nasıl kurar?

1. Modülü alır. Kitapçıklar konu bloklarıyla dizilir ve her bloğu ayrı bir uzman yazıyor görünür.
2. Maddenin en önemli hükmünü değil, benzeriyle karışabilecek hükmünü seçer: iki süre içeren fıkra, iki sistemli rejim, birbirine benzeyen iki liste, basamaklı yaptırım.
3. Doğru cevabı madde cümlesinden keser.
4. Çeldiriciyi aynı rafta arar: önce aynı maddenin diğer fıkrası, sonra komşu rejimin benzer hükmü, sonra aynı mevzuatın sayı havuzu. Uydurma en son çaredir.
5. Yönü seçer: tek kelime değişikliği, liste dışı unsur, tanımdan ad veya vaka (bölüm 4).

### Her madde önce analiz edilir

Bir hükümden soru hazırlamadan önce metin tamamen taranır ve şu bilgi alanları aranır:

- Tanımlar; kapsama girenler; kapsam dışında kalanlar; istisnalar; hariç tutulan durumlar
- Süreler ve sürenin başlangıç noktası
- Oranlar, yüzdeler, miktarlar, değerler; alt ve üst sınırlar; sayısal eşikler
- Yetkili makam, görevli kurum, onay makamı, karar makamı, takdir yetkisine sahip makam
- Mükellef veya sorumlu
- Belge adı, tutanak adı, aranacak belgeler
- Bildirim yükümlülüğü, bildirim yapılacak yer, teslim yeri, muhafaza yeri
- Ödeme kaynağı, öncelik sırası
- Şartlar ve birlikte aranması gereken şartlar
- Uygulanır / uygulanmaz hükümleri; yapılması zorunlu işlemler; yasaklar
- Muafiyetler, istisnalar, destekler
- Vergiyi veya yükümlülüğü doğuran olay; uygulanacak işlem veya önlem; müeyyide ve yaptırımlar
- Hesaplamada esas alınan değer, kur, tarih; matrah
- Mevzuatın dayanağı; düzenlemenin konusu
- Birbiriyle eşleştirilebilecek bilgiler; birlikte ölçülebilecek iki bilgi

GMY için ayrıca aranır:

- Karışabilecek hükümler: iki sayılı fıkra, iki sistemli rejim, benzer iki liste, basamaklı yaptırım
- Kapalı listeler ve eleman sayıları ("şunlardır", "yalnızca", sayılı bentler)
- Kayıt kelimeleri: dışında, hariç, suretiyle, sadece, yalnızca, talebi üzerine, olsun olmasın, sonundan / başından, en az / en fazla, re'sen, her hâlde
- Makam çiftleri: gümrük müdürlüğü, bölge müdürlüğü, Bakanlık, gümrük idaresi, vergi dairesi
- Dipnotunda değişiklik tarihi görünen hükümler (güncellik adayı)

Bu tarama tamamlanmadan soru hazırlama aşamasına geçilmez.

### Lafız kuralı

Sorunun kilit cümlesi madde metninden birebir alınır. Kilit cümle, olumlu kökte doğru şıktır; olumsuz kökte ise değiştirilen cümlenin aslıdır.

- Set hedefi: yaklaşık %70 birebir, %15–20 parafraz, en fazla %15 çıkarım.
- Çıkarım gerektiren soruda çıkarım tek adımlıdır ve cevap yine tek bir madde cümlesine dayanır.
- Tek kelime değişikliği: Dört şık madde metninden aynen alınır, beşincide tek kelime veya kayıt değiştirilir. Değiştirilen kelime hukuki sonucu gerçekten değiştirmelidir.

Bakanlığın beş yılda kullandığı tek kelime değişiklikleri:

| Metindeki ifade | Şıkta değiştirilmiş hâli |
| --- | --- |
| süre "yılın sonundan" başlar | "yılın başından" |
| gümrük gözetimi | gümrük kontrolü |
| işyeri nakli suretiyle | işyeri nakli hariç |
| devredilebilir | devredilemez |
| fotokopi | orijinal |
| para cezaları | adli para cezaları |
| Türkiye dışında | Türkiye'de |
| kara suları dışındaki | "kara suları" kaydı silinmiş |
| gümrük idaresi | vergi dairesi |
| yönetmelikle belirlenen hâller dışında | her hâlde |
| uygulanmaz | uygulanır |
| bölge müdürlüğü | gümrük müdürlüğü |

## 3. Soru sayısı ve maddenin tüketilmesi

Soru sayısını kullanıcı belirler ve o sayıya uyulur. Sayı verilmediyse madde tam olarak tüketilir.

Sayı verildiğinde soru alanları şu öncelikle seçilir:

1. Çıkmış soruların ölçtüğü noktalar
2. Sorulmuş fıkranın sorulmamış komşu fıkraları ve sorulmuş hükmün ters yönü
3. Metinde bulunan ikiz kavram eksenleri (bölüm 8)
4. Sayı, süre ve makam içeren hükümler
5. Kapalı listeler
6. Kalan sınav değeri taşıyan hükümler

Sayı verilmediyse:

- Bir maddeden hazırlanacak soru sayısına önceden sınır konmaz. Önce madde analiz edilir, kaç farklı sınav değeri taşıyan bilgi olduğu belirlenir, sonra yalnızca bu özgün alanlar kadar soru hazırlanır.
- Madde kısa olsa bile tüm sınavlık noktalar çıkarılır. Madde uzunsa parça parça fakat kapsamlı biçimde işlenir.
- Çalışma sonunda "Bu maddeden çıkarılabilecek sınav değeri taşıyan soru alanları tüketilmiştir." veya aynı anlamda kısa bir ifade kullanılır.

Her iki durumda:

- Aynı bilgi farklı kelimelerle tekrar tekrar sorulmaz. Her soru farklı bir bilgiyi, farklı bir ayrıntıyı veya aynı hükmün gerçekten farklı bir ölçme boyutunu ölçer.
- Ayna soru (ikiz kavramın iki kutbu, bölüm 8) tekrar sayılmaz. Aynı hükmü aynı yönden iki kez sormak tekrardır.

## 4. Bilgi türüne göre kurum soru kalıpları

Soru kökü rastgele seçilmez; mevzuattaki bilginin türüne göre kurumun çıkmış sınavlarda kullandığı yapılar arasından seçilir. Bu bölüm soru üretiminin temelidir.

Bakanlığın beş yıldaki biçim dağılımı (400 soru; bir soru birden fazla biçim taşıyabilir): klasik 157, olumsuz kök 153, öncüllü 39 (2025'te tek sınavda 17), tanımdan ad 34, vaka 16, boşluk doldurma 12, hesap 7, eşleştirme 3.

**A) Tanım bilgisi**

Kavram verilmişse tanımı sor:

- "Aşağıdakilerden hangisi '…' kavramını ifade eder?"
- "'…' ifadesinin tanımı aşağıdakilerden hangisinde doğru olarak verilmiştir?"
- "Aşağıdakilerden hangisi … tanımıdır?"

Tanım verilmişse kavramı sor:

- "'……' şeklinde tanımlanan kavram aşağıdakilerden hangisidir?"
- "Yukarıda tanımlanan kavram aşağıdakilerden hangisidir?"
- "Bu tanım aşağıdakilerden hangisine aittir?"

Bu iki yön farklı soru teknikleridir ve uygun oldukça dönüşümlü kullanılır.

**B) Kapsama giren bilgi**

- "Aşağıdakilerden hangisi … kapsamında yer alan … biridir?"
- "Aşağıdakilerden hangisi … arasında yer almaktadır?"
- "Aşağıdaki eşyalardan / ülkelerden / işlemlerden hangisi …?"

**C) Kapsam dışı / istisna**

- "Aşağıdakilerden hangisi … kapsamında değildir?"
- "Aşağıdakilerden hangisi … arasında yer almamaktadır?"
- "Aşağıdakilerden hangisi … biri değildir?"
- "Aşağıdakilerden hangisi … sayılmamıştır?"
- "… hangi … kapsamaz?"
- "… hükümler arasında yer almaz?"
- "… ilişkin aşağıdakilerden hangisi söylenemez?"

Bunlar aynı soru ailesinin farklı yüzey biçimleridir; bilgiye en doğal geleni seçilir.

**D) Doğru / yanlış hüküm**

- Doğruyu buldurma: "… ile ilgili olarak aşağıdakilerden hangisi doğrudur?", "… ilişkin aşağıdaki ifadelerden hangisi doğrudur?"
- Yanlışı buldurma: "… ilişkin aşağıdaki ifadelerden hangisi yanlıştır?", "… kapsamında aşağıdakilerden hangisi yanlıştır?", "… ilişkin aşağıdakilerden hangisi söylenemez?"

"4458 sayılı Gümrük Kanunu'na göre aşağıdakilerden hangisi doğrudur?" gibi genel ve bağlamsız köklerden kaçınılır. Kök, ölçülen konuyu açıkça gösterir.

**E) Önermeli soru**

- "Yukarıdaki ifadelerden hangisi / hangileri doğrudur?"
- "Yukarıdaki ifadelerden hangisi / hangileri yanlıştır?"

Ayrıntılı kurallar bölüm 9'dadır.

**F) Süre**

- Doğrudan süre: "… en fazla kaç gündür / aydır / yıldır?", "… azami kaç gün / ay / yıl içinde …?", "… ne kadar süre içinde gerçekleştirilmek zorundadır?"
- Başlangıç noktası ve süre: "… tarihinden itibaren kaç gün / ay / yıl süreyle …?" Başlangıç noktası sınav değeri taşıyorsa yalnızca süre miktarı sorulmaz.
- Somut olay ve süre: "Buna göre … azami kaç gün içerisinde … zorundadır?"

**G) Oran / yüzde / tutar / sayısal sınır**

- "… için uygulanacak … oranı nedir?"
- "… tutarının üst sınırı aşağıdakilerden hangisidir?"
- "… en fazla / en az ne kadardır?"
- Destek veya karşılanan bölüm: "… ne kadarı / yüzde kaçı / kaç puanı karşılanır?"

**H) Yetkili kişi / kurum**

- "… hangi kurum / kuruluşça yapılabilir?"
- "… aşağıdakilerden hangisi tarafından yapılır?"
- "… denetimleri aşağıdakilerden hangisi tarafından yürütülür?"

**I) Karar / onay / düzenleme yetkisi**

- "… karar vermeye yetkili merci aşağıdakilerden hangisidir?"
- "… onaylamaya aşağıdakilerden hangisi yetkilidir?"
- "… önlem almaya ve düzenleme yapmaya aşağıdakilerden hangisi yetkilidir?"

İşlemi yapan kurum ile karar veya onay yetkisine sahip merci birbirine karıştırılmaz.

**J) Belge**

- "… hâlinde aşağıdaki belgelerden hangisi aranır?"
- "… için gümrük idarelerince aşağıdakilerden hangisi aranır?"
- "… ithalinde hangi belge aranmaktadır?"
- Belgenin işlevi: "… gösteren belge / işaret aşağıdakilerden hangisidir?"

**K) Şart / koşul**

- Tek şart: "… yapılabilmesi için aşağıdakilerden hangisi şarttır?", "… uygulanabilmesi için aşağıdakilerden hangisi gereklidir?"
- Birlikte aranan şartlar: "Aşağıdakilerden hangisi … için gerekli şartları tam olarak taşımaktadır?", "… yapabilecek kişi / firmalar aşağıdakilerden hangisinde tam olarak verilmiştir?"

**L) Tabi olma**

- "Aşağıdakilerden / Aşağıdaki eşyalardan / Aşağıdaki belgelerden hangisi … tabidir?"
- Tersi: "Aşağıdaki durumlardan hangisinde … yapılmaz?"

**M) Zorunluluk**

- "Aşağıdakilerden hangisinde … yapılması zorunludur?"
- "… yapılması gerekir?"
- "… için aşağıdakilerden hangisi zorunludur?"

**N) Hesaplamada esas alınan değer**

- "… hesaplanmasında aşağıdakilerden hangisi esas alınır?"
- "… hangi kur esas alınarak hesaplanır?"
- "… hangi tarih itibarıyla belirlenen değer esas alınır?"

**O) Matrah**

- "… işleminde / ithalinde matrah aşağıdakilerden hangisidir?"

Matrah sorusu genel hesaplama sorusuna dönüştürülmez.

**P) Mükellef / sorumlu**

- "… mükellefi aşağıdakilerden hangisidir?"
- "… bakımından mükellef / sorumlu kimdir?"

**Q) Vergiyi / yükümlülüğü doğuran olay**

- "Aşağıdaki durumlardan hangisinde … gerçekleşmez / doğar?"

**R) Hukuki sonuç / uygulanacak işlem**

- "… hâlinde ne tür bir sonuç / değişiklik söz konusu olur?"
- "… hâlinde aşağıdakilerden hangisi uygulanır / gerçekleşir?"

**S) Uygulanacak önlem**

- "… tespit edilirse buna karşı aşağıdakilerden hangisi uygulanabilir?"
- "… olması hâlinde nasıl bir önleme / işleme başvurulur?"

Somut olay kurulabiliyorsa hüküm doğrudan ezber olarak sorulmak yerine olaya uygulatılabilir.

**T) Uygulama şekli**

- "… ne şekilde uygulanır?"

**U) Eşleştirme**

- "… ile … eşleşmesiyle ilgili aşağıdakilerden hangisi yanlıştır?"
- "… aşağıdakilerden hangisinde yanlış eşleştirilmiştir?"

Yalnızca iki bilgi grubu arasında gerçek ilişki varsa kullanılır: eşya – belge, eşya – oran, tebliğ – kurum, rejim – süre, eşya – denetim aşaması, ülke – belge, işlem – yetkili merci. Gerçek sınavda nadirdir (400 soruda 3); sette sınırlı tutulur (bölüm 13).

**V) Hukuki kaynak / mevzuat**

- Nerede düzenlendiği: "… aşağıdaki hangi Karar / mevzuat kapsamında düzenlenmektedir?", "… hangi düzenlemede yer almaktadır?"
- Neye dayanılarak hazırlandığı: "… hangi düzenleme / kuruluş / mevzuat esas alınarak hazırlanmıştır?", "… hazırlanırken aşağıdakilerden hangisi dikkate alınmıştır?"

Bu iki bilgi türü birbirine karıştırılmaz.

**W) Düzenlemenin konusu**

- "… aşağıdakilerden hangisiyle / hangi rejimle doğrudan ilgilidir?"
- "… aşağıdakilerden hangisine ilişkin düzenleme / yönetmelik / tebliğ yayımlanmıştır?"

**X) Muafiyet / istisna / destek / hak**

- "Aşağıdakilerden hangisi … muafiyetinden / istisnasından / desteğinden yararlanabilir?"

**Y) Bilinen / kısa ad**

- "… hangi adla bilinmektedir?"
- "… aşağıdakilerden hangisi olarak bilinmektedir?"

Bu yapı tanım sorusundan ayrı değerlendirilir.

**Z) Boşluk doldurma**

- Tek bilgi: "Yukarıdaki cümlede / paragrafta boş bırakılan yere gelmesi gereken uygun ifade aşağıdakilerden hangisidir?"
- İki veya daha fazla bağlantılı bilgi: "Yukarıdaki boşluklara sırasıyla aşağıdakilerden hangisi gelmelidir?" (tutar / belge, süre / kurum, oran / süre, belge / merci)

Gerçek sınavda azdır (400 soruda 12); sette sınırlı tutulur (bölüm 13).

**AA) İki bilgiyi birlikte ölçme**

- "… ne kadarlık bir … ne kadar süre içinde …?"

Şıklar tutar / süre, belge / süre, kurum / belge, oran / süre biçiminde kurulabilir. İki bilgi doğal biçimde ilişkili değilse bu teknik kullanılmaz.

**AB) Müeyyide / yaptırım**

- "… aykırı hareket etmenin müeyyidesi aşağıdakilerden hangisidir?"
- "… ihlal edilmesi hâlinde uygulanacak yaptırım / ceza aşağıdakilerden hangisidir?"

### GMY'nin dört soru yönü

Bakanlık kalıbı seçtikten sonra soruyu şu dört yönden birine çevirir:

1. Tek kelime değişikliği: Dört doğru madde cümlesi ve tek kelimesi bozulmuş beşinci cümle. Kök "yanlıştır".
2. Liste dışı unsur: Kapalı listeye akla yatkın bir yabancı eklenir. Kök "değildir / yer almaz / sayılmamıştır".
3. Tanımdan ad: Tanım verilir, adı sorulur. Kök "ne ad verilir / hangisidir".
4. Vaka: Bir olay verilir, olayın içine bir istisna saklanır (bölüm 6).

### Kalıp seçiminde karar kuralı

Bir hüküm birden fazla kalıba uygun olabilir. Bu durumda:

1. Önce hükmün asıl sınav değerini belirle.
2. Bilgi türünü tespit et.
3. Kurumun aynı bilgi türünde kullandığı en doğal soru tekniğini seç.
4. Doğrudan soru çok basit kalıyorsa ve hüküm uygunsa önermeli, somut olay, çift bilgi, eşleştirme veya boşluk doldurma yöntemini değerlendir.
5. Aynı bölümde sürekli aynı soru kökünü kullanma.
6. Sırf çeşitlilik için bilgiye uymayan kalıp seçme.

Kalıp bilgiye hizmet eder; bilgi kalıba zorla uydurulmaz.

## 5. Soru kökü, dayanak mevzuat ve dil

Kök yapısı her zaman şudur: MEVZUAT ADI + HÜKMÜN KONUSU + KURUM KALIBI.

### Madde, fıkra ve bent ezberi sorulmaz

Öğrenciye madde, fıkra veya bent numarası ezberletilmez. Şu tür sorular hazırlanmaz:

- "37 nci maddeye göre…"
- "Aşağıdakilerden hangisi 37 nci madde hükmüdür?"
- "241/3-c uyarınca…"

Bunun yerine hükmün konusu veya hukuki kurumu kökte belirtilir.

- YANLIŞ: "4458 sayılı Gümrük Kanunu'nun 37 nci maddesine göre aşağıdakilerden hangisi doğrudur?"
- DOĞRU: "4458 sayılı Gümrük Kanunu'nun özet beyanın verilme süresine ilişkin hükümlerine göre aşağıdakilerden hangisi doğrudur?"

Madde numarası şıklarda da sorulmaz. Bakanlık bazı köklerde madde numarası veriyor; biz vermeyiz.

### Dayanak mevzuat kökte yer alır

- ZAYIF: "4458 sayılı Gümrük Kanunu'na göre aşağıdakilerden hangisi doğrudur?"
- TERCİH EDİLEN: "4458 sayılı Gümrük Kanunu'na göre serbest dolaşım statüsünün kaybedilmesine ilişkin aşağıdakilerden hangisi doğrudur?"

Bakanlık köklerinin yaklaşık üçte birinde mevzuat adı yoktur; biz her kökte mevzuat adını yazarız.

### Kök kontrolleri

- Kök ile kaynak aynı olur: Kök "Gümrük Kanunu'na göre" diyorsa hüküm Kanun'dan alınır. Hüküm Yönetmelik'teyse kökte Yönetmelik yazılır. Bakanlık 2025'te bu hataya düştü.
- Kök doğru şıkkı ele vermez. Kökte geçen bir kelime doğru şıkkın adını taşımaz.
- Kök tek anlamlıdır: hangi rejim, hangi taşıma türü, hangi tarih, hangi kişi olduğu kökte bellidir.
- Kök uzunluğu bilgiye göre değişir: klasik sorularda kısa, vaka ve önermeli sorularda uzun kök olağandır.

### Soru dili

Sorular kısa, net, resmî, ölçücü, mevzuat merkezli ve kurum sınavlarının diline yakın olur. Gereksiz akademik anlatımdan ve yapay zekâ dilinden kaçınılır.

Gerçek sınavlarda kullanılmayan "temel özellik", "temel kural", "kritik husus", "en önemli düzenleme" gibi yapay nitelemeler soru köklerine eklenmez. Mevzuat metninde bulunmayan değerlendirme ifadeleri üretilmez.

## 6. Somut olay ve vaka soruları

Vaka sorusunun cevabı hesapta değil, vakanın içine saklanmış tek bir istisnayı görmekte durur. Bakanlıkta uygulama ve bütünleşik soru sayısı yıllara göre 1, 10, 11, 10, 12'dir; artıyor.

- Vakanın içine tek bir istisna saklanır. Hesap zinciri, istisnayı görmeyen adayı yanlış şıkka götürür.
- Cevap yine tek bir madde cümlesine dayanır; vaka yalnızca bu cümleyi gizler.
- Hesap sorusunda sayılar basit, hesap bir iki adımdır. Zorluk aritmetikte değil, doğru hükmü seçmektedir.
- Mizansen mevzuatta olmayan yeni hukuki bilgi yaratmaz. Olay yalnızca mevcut hükmün uygulanmasını ölçer.
- Vakaya uygun konular: süre hesabı, kıymet, ceza katı ve matrah, vergi, yetki, istisna, rejim seçimi, uygulanacak işlem, beyan şekli, yaptırım.

Bakanlığın sakladığı istisna türleri (yalnızca kurgu türünü gösterir; vakadaki her hüküm yüklenen metinden doğrulanır):

- Kişinin niteliği: İthalatçının kamu idaresi olması adayı yanlış ceza maddesine götürür.
- Taşıma türü: Süre, havayolunda taşıtın hareketiyle başlar.
- Kıymet unsurunun sınırı: Teslim şekline göre navlun ve sigortanın yalnızca sınıra kadarki payı eklenir.
- Muhatap sayısı: Aynı fiil için farklı kişilere kesilen idari para cezası, vergideki müteselsil sorumluluktan farklı işler.
- Beyan şekli: Belirli bir eşyanın gönderilmesi sözlü beyanla yapılır.

## 7. Çeldirici sistemi, sayısal şıklar, süre ve kapalı liste

Yanlış şık "yanlış bilgi" değil, "yanlış yerde duran doğru bilgi" olur. Öğrenci "bunu bir yerde okumuştum" hissiyle onu işaretlemelidir.

### Çeldiricinin gerçek yuvası

Her çeldirici için metindeki gerçek yuvası belirlenir. Kaynak sırası şudur:

1. Aynı maddenin komşu fıkrası
2. Komşu rejimin benzer hükmü
3. Aynı mevzuatın sayı havuzu
4. Uydurma (yalnızca son çare)

Yuvası gösterilemeyen çeldirici uydurmadır. Bakanlığın en zayıf soruları uydurma çeldiricilerin olduğu sorulardır; sette uydurma çeldirici en aza indirilir.

Çeldiriciler mümkün olduğunca mevzuattaki şu farklardan üretilir:

- yakın süreler, yakın oranlar, benzer parasal sınırlar
- yakın yetkili makamlar, benzer belge adları
- farklı fakat yakın rejimler
- kapsam içi / kapsam dışı unsurlar; istisna ile genel kural ayrımı
- "öncelikle / doğrudan" gibi ifadeler; "aranır / aranmaz" karşıtlığı; "en az / en fazla" farkı

Yanlış şık bariz yanlış olmaz ve öğrencinin mevzuattaki ayrıntıyı bilmesini gerektirir. Şıklar aynı kategoridedir.

### Sağduyu çeldiricisi

Sahada mantıklı görünen ama mevzuat listesinde olmayan unsur, mevzuatı sağduyuyla çözen adayı eler. Mümkünse bu unsur mevzuatın başka bir yerinde gerçekten geçen bir kavramdır.

| Kapalı liste | Bakanlığın eklediği "mantıklı" unsur |
| --- | --- |
| Kaçakçılık Kanunu'ndaki görevliler | özel güvenlik görevlisi, sınırdaki asker |
| Teminat türleri | kefalet |
| Menşe şahadetnamesinin zorunlu bilgileri | eşyanın kıymeti |
| İlişkili kişiler | aynı sektörde faaliyet |
| YYS sertifikası | belirli bir geçerlilik süresi |
| Özel antrepo şartları | gümrük müşaviri istihdamı |
| YYS koşulları | kapsamlı teminat (AB terimi) |

### Tuzak türleri

Her sorunun tuzak türü iç kontrolde belirlenir; çıktıda gösterilmez, set raporunda sayılır. Bir soru birden fazla tuzak taşıyabilir.

- SAYI: yanlış sayı · YAKIN-SAYI: doğru değerin hemen yanındaki gerçek değer
- BAŞLANGIÇ: sürenin başladığı an · MAKAM: yetkili merci
- TERİM: benzer kavram veya belge adı · KOMŞU: komşu fıkra veya rejimden taşınan hüküm
- TERSİNE: olumsuzlama · MUTLAK: "her hâlde", "hiçbir şekilde" gibi mutlaklaştırma
- UNSUR: tanımdan unsur düşürme veya ekleme · LİSTE-DIŞI: kapalı listeye yabancı
- İSTİSNA: genel kuralın istisnası · ŞART: eksik veya fazla şart
- AD-HESAP: hesapta yanlış unsur · SAĞDUYU: mantıklı görünen ama mevzuatta olmayan

### Sayısal tuzak ve şık dizilimi

Süre, miktar, oran ve değerler mutlaka değerlendirilir. Yanlış seçenekler doğru değere yakın olur: 3 ay / 6 ay, %15 / %30, 5.000 / 10.000, 30 gün / 45 gün / 60 gün. Mevzuatta veya yakın hükümlerinde dayanağı olmayan anlamsız rakamlar sırf şık doldurmak için kullanılmaz.

- Sayısal şıklar küçükten büyüğe dizilir. Bakanlık, şıkları sayı olan 52 sorunun 45'inde bunu yapmıştır.
- Doğru değer ortadaki üç şıktan birine (B, C veya D) konur. Bakanlıkta doğru değer 52 sorunun 41'inde (%79) ortadaydı; en küçük değer 8, en büyük değer yalnızca 3 soruda doğruydu.
- Diğer değerler aynı mevzuatın gerçek sayı havuzundan seçilir: 15 / 30 / 45 / 60 gün; 1 / 3 / 5 / 6 yıl; 2 / 4 / 6 / 8 kat gibi.
- Sayısal sorularda harf dengesi şık sırası bozularak değil, çeldirici değerlerin seçimiyle sağlanır.
- Bir sayı komşusuyla birlikte ölçülür: aynı fıkradaki ikinci sayı en güçlü çeldiricidir.

### Süre soruları

- Süre soruluyorsa başlangıç anı da yoklanır: ya kökte verilir ya şıklara konur. Sette süre sorularının en az üçte birinde başlangıç anı ölçülür.
- Bakanlığın sorduğu başlangıç anları: yılın sonu / başı, ihale ilanı / tasfiye kararı, yükümlülüğün doğduğu tarih, kararın geçersiz olduğu an, yasağın bildirimi, taşıtın hareketi.
- Sürenin uzatma makamı ve uzatma süresi ayrı soru alanıdır.

### Kapalı liste soruları

- "Şunlardır", "yalnızca" veya sayılı bentlerle kurulan liste kapalı listedir; eleman sayısıyla birlikte ele alınır.
- Liste dışı sorusunda dört şık listeden aynen alınır, beşinci şık akla yatkın bir yabancıdır.
- Kıymet konusunda olumsuz kök ağırlıklıdır: Bakanlık 34 kıymet sorusunun 19'unda "listede olmayanı" aramıştır.

## 8. İkiz kavram eksenleri ve ayna sorular

Yüklenen metinde aşağıdaki eksenlerden biri varsa sette en az bir soru o ekseni ölçer. Bakanlık bu çiftleri beş yıl boyunca tekrar etmiş, çoğunu aynı sınavda iki yönden sormuştur (2022'de beş çift, 2024'te iki çift, 2025'te statü ↔ menşe üç kez).

- Uygunsa aynı sette ayna soru kurulur: "şartlı muafiyet düzenlemesi listesinde olmayan" ile "ekonomik etkili rejim listesinde olmayan" gibi.
- Ayna soru eksenin öbür kutbunu ölçer; aynı hükmü iki kez sormak değildir.
- Tablo yalnızca yön gösterir. Soruya giren her bilgi yüklenen metinden doğrulanır.

| # | Eksen | Karıştırılan nokta |
| --- | --- | --- |
| 1 | Şartlı muafiyet düzenlemesi listesi ↔ ekonomik etkili rejim listesi | Hangi rejim hangi listede; transit birinde var ötekinde yok, HİR'de durum tersine |
| 2 | DİR şartlı muafiyet sistemi ↔ geri ödeme sistemi | Vergi teminata mı bağlanıyor, tahsil edilip iade mi ediliyor; standart değişim HİR'e ait |
| 3 | Gümrük statüsü ↔ menşe | A.TR statü belgesidir; serbest dolaşıma girmek menşe kazandırmaz |
| 4 | Tümüyle elde edilme ↔ esaslı işçilik ↔ yetersiz işlem | Basit montaj ve ambalaj menşe kazandırmaz, pozisyon değişikliği kazandırır |
| 5 | Usulsüzlük cezalarının kat merdiveni (2-4-6-8) | Fiilin hangi basamakta olduğu |
| 6 | Vergi kaybı cezasının (GK 235) matrahı ve katı | Gümrüklenmiş değer mi vergi mi; yasak eşyada dört kat, izne tabi eşyada iki kat |
| 7 | Ödeme süresi ↔ uzatma ↔ tebliğ zamanaşımı | Aynı fıkradaki ikinci sayı çeldirici |
| 8 | Geri vermede genel süre ↔ kusurlu eşya ve uluslararası anlaşma süresi | Süre ve başlangıç anı |
| 9 | İptal ↔ düzeltme | Yükümlülüğü ve serbest dolaşım statüsünü iptal sona erdirir, düzeltme sona erdirmez |
| 10 | Gümrükçe onaylanmış işlem ve kullanım listesi ↔ ara statüler | Geçici depolama bunlardan biri değildir; "terk" yerine "teslim" yazılır |
| 11 | Kıymet ikizleri | Satış ↔ satın alma komisyonu; aynı ↔ benzer eşya; ilişki listesi; pazarlama dolaylı ödeme değildir; kur |
| 12 | Doğrudan ↔ dolaylı temsil | Kimin adına, kimin hesabına |
| 13 | Depolama süreleri | Geçici depolamada taşıma türüne göre süre, yolcu ambarı, ihracatta geçici depolama |
| 14 | BTB ↔ BMB | Geçerlilik süresi ve geçersizlik anı |
| 15 | Vergide müteselsil sorumluluk ↔ idari para cezasının kişiselliği | Vergi bir kez ödenir, ceza her muhataba ayrı |
| 16 | Geçici ithalat | Aylık oran; satış ve kiralama yasağı; "olağan yıpranma dışında değişmeden" ifadesi |
| 17 | Antrepo tipleri | Genel antrepolar ↔ özel antrepolar; işleticinin sorumluluğu |
| 18 | DİR izni ↔ DİR izin belgesi | İzni gümrük idaresi, belgeyi Bakanlık verir |

## 9. Önermeli soru standardı

Önermeli soru gerçek sınavda artıyor: 2021'de 7, 2025'te 17 soru. Sette önermeli soru oranı %15–20'dir (25 soruda 4–6).

- En az 3 önerme olur; mantıklıysa 4 önerme esastır.
- Önermeli soru sırf zorlaştırmak için kullanılmaz; birden fazla hükmün birlikte ölçülmesi anlamlı olmalıdır.
- Kök çoğunlukla "doğrudur" yönündedir. Bakanlıkta 40 önermeli sorunun 32'si olumlu köklüdür; sette "yanlıştır" köklü önermeli soru bir ikiyi geçmez.
- En kapsamlı şık ("I, II ve III" gibi) Bakanlıkta önermeli soruların %58'inde doğrudur. Yazar bütün önermeleri doğru yapıp adayı eksik seçime iter. Bu yüzden "hepsi doğru" yasak değildir ama varsayılan cevap da değildir: sette önermeli soruların en fazla üçte biri en kapsamlı şıkla cevaplanır.
- Kalan önermeli sorularda kombinasyon çeşitlenir: gerektiğinde yalnız bir önerme, gerektiğinde iki veya üç önerme doğru olur. Sürekli aynı kombinasyon doğru olmaz.
- Önermelerin doğru / yanlış dizilimi hep aynı olmaz; örneğin her soruda I-II-III doğru, IV yanlış olmaz.
- Yanlış önermeler bariz olmaz. Yanlış önerme, gerçek hükümdeki tek bir unsur değiştirilerek hazırlanır:
  - tam muafiyet ↔ kısmi muafiyet
  - üç ay ↔ altı ay
  - teminat aranır ↔ teminat aranmaz
  - en az %75 ↔ %100
  - bir defaya mahsus ↔ her defasında
  - Bakanlık ↔ bölge müdürlüğü
- Yanlışlık küçük fakat hukuken belirleyici olur.

## 10. Meslek ve güncellik soruları

GMY bir meslek giriş sınavıdır: aday kendi yetkisinin sınırını bilmeli ve güncel mevzuatla çalışmalıdır.

### Meslek soruları

- Gümrük müşaviri, yardımcısı, YGM, disiplin ve temsil her yıl sorulur (yıllara göre 11, 6, 10, 7, 4 soru). Düzey çoğunlukla düz hatırlama, tuzak sayı ve yakın sayıdır.
- Meslek mevzuatı yüklendiğinde öncelikli alanlar: yardımcının yapamadıkları (tebliğ kabulü, tek başına iş takibi), temsil türü ve kime ait olduğu, bildirim süreleri, disiplin cezaları ve zamanaşımı, YGM rapor kodları.
- Meslek yanlılığı sorusu: Konu elveriyorsa her sette bir soru adayın "müşavir her yerde şarttır" ya da "yardımcı da yapabilir" önyargısını yoklar. Örnek kurgu: özel antrepo şartları arasına "gümrük müşaviri istihdamı" eklemek.

### Güncellik soruları

- Bakanlık güncel tutarı ve son değişikliği sorar: usulsüzlük cezası tutarı 2022, 2024 ve 2025'te geldi; yeni eklenen rapor kodu, yeni sınırlar ve yeni kıymet kuralları da soruldu.
- Yüklenen metnin dipnotlarından son 12 ayda değişen hükümler bulunur. Varsa sette bir soru bunlardan kurulur. Dipnot yoksa bu kural atlanır; dışarıdan araştırma yapılmaz.
- Tutar soruluyorsa yalnızca yüklenen metinde yazan güncel tutar kullanılır.
- Hükmün eski hâli dipnotta görünüyorsa eski hâl çeldirici olarak kullanılabilir; eski kaynaktan çalışan adayı ayırır.
- Gerekçede değişikliğin tarihi belirtilir.

## 11. Çıkmış soru kullanımı ve yazarın sonraki hamlesi

Çıkmış sorular soru bankasına aynen alınmaz, ama çıkmış sorunun ölçtüğü mevzuat noktası kesinlikle atlanmaz.

Bir hüküm geçmiş sınavda sorulmuşsa:

- Bilgi alanı mutlaka soru yapılır.
- Çıkmış soru yalnızca sınav mantığını anlamak için kullanılır.
- Aynı soru metni, aynı şık yapısı ve aynı kurgu kopyalanmaz.
- Kurumun o bilgi türünde kullandığı soru ailesi korunur.

Özgünlük kurum dilinden uzaklaşmak demek değildir. Amaç, aynı bilgiyi kurumun soru karakterini koruyarak özgün biçimde yeniden ölçmektir.

### Yazarın sonraki hamlesi

- Bakanlığın en tutarlı davranışı, sorulmuş maddenin sorulmamış komşu fıkrasını sormaktır. Çıkmış soru hangi fıkrayı ölçtüyse aynı maddenin sorulmamış fıkraları sette mutlaka soru alanı olur.
- Sorulmuş hüküm ters yönden de sorulur: tanımdan ada, addan tanıma; "olan"dan "olmayan"a; listede olandan listede olmayana.
- Çıkmış sorunun ölçtüğü bilgi yüklenen metinde yoksa soru üretilmez; set raporunda "metinde karşılığı bulunamayan çıkmış soru noktaları" olarak yazılır.
- Resmî cevap, mevzuat sonradan değiştiği için güncel metinle uyuşmuyorsa soru güncel metne göre kurulur.

### Konu setine girerken bakılacak komşu fıkralar

Analiz, 2026–2027 için en olası hamleleri şu fıkralarda görüyor. Liste yalnızca nereye bakılacağını gösterir; sorunun içeriği yüklenen metinden alınır.

- Gümrük Kanunu cezaları: usulsüzlük cezalarında henüz eşleştirilmemiş fiil–kat çiftleri (kararlara dayanak belge ve bilgilerin yanlış verilmesi, antrepo kayıtları); vergi kaybı cezasında yalnızca doğrudan transite ilişkin 30 gün (GK 235/4-a); GK 179/1'deki %1, %3, %10 oranları; GK 177/4'teki otuzar günlük intikal ve teslim süreleri.
- Kıymet: ilişkili kişilerde %5 oy hakkı ve tek acente istisnası (GY 55/1-ç, 55/2); indirgeme yöntemindeki indirimler (GY 48); faizin düşülme şartları; bilgi amaçlı kurlar (GY 57/2).
- Menşe: idare amirinin onayıyla tamamlanabilecek eksiklikler (GY 40/2); 6 aylık geri verme ve denetim süreleri (GY 38/3, 38/5); üçüncü ülkedeki antreponun menşei değiştirmemesi (GY 36/3); deniz ürünleri, fabrika gemileri, deniz dibi (GK 18/2-f, g, h).
- DİR: kapatma süresi, eksikliklerin tamamlanma süresi, kısmi teminat iadesinde %90 sınırı, değişmemiş eşyada %1 ve işletme malzemesinde %2 sınırları, geri ödeme sisteminin uygulanmadığı hâller (GK 117).
- Meslek: savunma için 10 gün, tedbir için 6 ay ve dönem süreleri (Geçici 6/4–6/9); "her yılın ikinci ayı" bildirimi (GY 563/2); YGM'de henüz sorulmamış kodlar (BD1, TK1, NK1, AN6, AN7).
- Kaçakçılık: artırım oranları (5607 md. 4/1 ve 4/4).
- Az sorulmuş alanlar: kabotaj, sınır ticareti, taşıtlar, mücbir sebep, belge saklama, gümrüksüz satış (beş yılda birer soru); sonradan kontrol hiç sorulmadı; uzlaşma yalnızca süre olarak geçti; transit ve TIR 2023'te hiç sorulmadı.

## 12. Kanun, yönetmelik, tebliğ ve kurum adları

Bakanlık soruların yaklaşık yarısında Yönetmelik, tebliğ ve karar ayrıntısına iner; yalnızca Kanun'u bilen aday burada elenir.

### Kanun – yönetmelik – tebliğ tekrarı

Aynı hüküm alt düzenlemede birebir tekrar ediliyorsa ikinci kez soru yapılmaz. Alt düzenleme şunlardan birini getiriyorsa ayrı soru alanıdır:

- yeni süre, yeni belge, yeni usul
- yeni istisna, yeni makam
- başvuru şekli, ek şart, uygulama ayrıntısı
- kod, form, saat gibi teknik ayrıntı (rapor kodları, form adları, TIR saatleri)

### Dayanak mevzuat bağlantısı

Bir yönetmelik, tebliğ veya alt düzenleme çalışılıyorsa gerektiğinde şunlar da sınav değeri bakımından değerlendirilir: hangi kanuna dayandığı, hangi hukuki düzenlemeyi somutlaştırdığı, hangi kurumun yetki alanıyla ilgili olduğu, hangi üst düzenlemeye dayanılarak hazırlandığı. Öğrenciden madde numarası ezberi istenmez.

### Eski ve yeni kurum adları

Mevzuat metninde "Müsteşarlık" yazıyorsa mevzuatın kendi terminolojisine sadık kalınabilir. Ancak şıklarda Müsteşarlık / Ticaret Bakanlığı gibi aynı makamın eski ve yeni karşılığı rakip seçenek yapılmaz. Yanlış makam kullanılacaksa gerçekten farklı bir makam seçilir. Amaç tartışmalı çeldirici değil, hukuken tek doğru cevabı olan sorudur.

## 13. Set profili ve doğru cevap dağılımı

Set bittikten sonra aşağıdaki profil kontrol edilir. Hedefler Bakanlığın 2021–2025 dağılımına göre ayarlanmıştır; konu bir ölçütü taşımıyorsa o ölçüt zorlanmaz.

| Ölçüt | Bakanlık (2021–2025) | Set hedefi | 25 soruluk sette |
| --- | --- | --- | --- |
| Kilit cümlesi madde metninden birebir | %69 | %65–70 | 16–18 |
| Parafraz | %17 | %15–20 | 4–5 |
| Çıkarım (tek adımlı) | %12 | en fazla %15 | 2–3 |
| Olumsuz kök | %31–47,5 (yıla göre) | %30–45 | 8–11 |
| Önermeli | 2025'te %21 | %15–20 | 4–6 |
| Vaka, uygulama, hesap | 2025'te %15 | %10–15 | 3–4 |
| Tanımdan ad / addan tanım | %8,5 | konu tanım içeriyorsa | 1–3 |
| Boşluk doldurma ve eşleştirme | %4 | en fazla %8 | 0–2 |

Tuzak dağılımı: KOMŞU en sık tuzaktır (Bakanlıkta soruların %41'i). Ardından SAYI ve YAKIN-SAYI (%35), LİSTE-DIŞI ve SAĞDUYU (%28), TERİM (%21), TERSİNE (%13) gelir; MAKAM, UNSUR ve BAŞLANGIÇ daha seyrektir. Sette de KOMŞU birinci sırada tutulur.

Düzey dağılımı: hatırlama yaklaşık %45, ayırt etme %35, tanıma %22, uygulama ve bütünleşik %12. Ayırt etme düzeyi 2024'ten beri artıyor.

Her sette ayrıca:

- Bölüm 1'deki beş aday profilinin her biri en az bir soruyla yakalanır.
- Konu elveriyorsa bir meslek yanlılığı sorusu bulunur.
- Yüklenen metinde son 12 ayda değişen hüküm varsa bir güncellik sorusu bulunur.
- Metinde ikiz eksen varsa en az bir ayna çift kurulur.

### Doğru cevap dağılımı

Sorular tamamlandıktan sonra doğru cevap dağılımı ayrıca kontrol edilir.

- Doğru cevaplar A, B, C, D, E arasında dengeli ve doğal dağıtılır; belirgin örüntü oluşturulmaz.
- Art arda aynı harf kullanılmaz. Bakanlık bu kuralı uygulamaz (her yıl 10–18 kez art arda aynı harf, bir yılda beş soru üst üste E); biz uygularız.
- Bakanlık A harfini az kullanır (%14); biz dengeli dağıtırız.
- Sayısal sorularda doğru değer B, C veya D'de olduğu için A ve E açığı sözel sorularda kapatılır.
- Önermeli sorular sürekli aynı kombinasyona bağlanmaz.
- Gerekirse şıkların sırası değiştirilerek dağılım düzeltilir; sayısal şıklarda sıra bozulmaz, çeldirici değerler değiştirilir.

### Şık uzunluğu

Doğru şık sistematik olarak en uzun ya da en kısa şık olmaz. Bakanlıkta uzunluk ipucu değildir: en uzun şık %26, en kısa şık %25 oranında doğrudur, rastlantı düzeyi %20'dir. Sette doğru şıkkın tek başına en uzun olduğu soru oranı %25'i geçmez; en kısa için de aynı sınır geçerlidir.

ÇOK ÖNEMLİ: Şıkların yeri değiştirildikten sonra doğru cevap ve gerekçe yeniden kontrol edilir. Nihai doğru cevap harfi ile gerekçenin anlattığı seçenek mutlaka aynıdır.

## 14. Konu bazında Bakanlık eğilimi ve deneme dağılımı

Konu seti hazırlanırken tablodaki baskın tuzak ve yazarın aradığı nokta esas alınır. 80 soruluk gümrük denemesi hazırlanırken son sütundaki dağılım başlangıç noktasıdır; kullanıcı başka sayı verirse onun sayısı geçerlidir.

| Konu grubu | 5 yılda soru (2021-22-23-24-25) | Baskın tuzak | Yazarın aradığı | 80 soruluk denemede |
| --- | --- | --- | --- | --- |
| Menşe / TPÖ / İthalat Rejimi Kararı | 28 (0-1-4-12-11) | Komşu, terim | Belge türleri (A.TR, EUR.1, menşe şahadetnamesi), statü ↔ menşe, yetersiz işlem | 10 |
| Tahsilat / teminat / geri verme / itiraz | 40 | Komşu, sayı, başlangıç | Süreyi başlangıç anıyla bilmek | 8 |
| Kıymet | 34 (5-12-5-7-5) | Liste dışı, sağduyu, istisna; olumsuz kök ağırlıklı | İlaveler ve indirimler, ilişki listesi, yasak yöntemler, kur | 7 |
| Antrepo / geçici depolama / serbest bölge / gümrüksüz satış | 34 | Sayı, komşu, makam | Süreler, antrepo tipleri, gümrük müdürlüğü ↔ bölge müdürlüğü | 7 |
| DİR / HİR / GKAİR / şartlı muafiyet | 31 | Komşu (31 sorunun 18'i), terim | Rejim ve sistem tanımlarını birbirinden ayırmak | 7 |
| Meslek (GM, GMY, YGM, disiplin, temsil) | 38 (11-6-10-7-4) | Sayı, yakın sayı | Kendi yetkisinin sınırı ve kendi süreleri | 6 |
| Tanımlar / beyan / muayene | 41 (7-9-20-3-2) | Komşu, terim, liste dışı | Onaylanmış işlem ve kullanımlar, gümrük idaresi türleri, hatlar, beyanname yerine geçen belgeler | 5 |
| Gümrük Kanunu cezaları | 20 (0-5-6-5-4) | Sayı (20 sorunun 17'si) | Kat merdiveni ve matrah; vaka ve hesap en çok burada | 5 |
| Muafiyet / yolcu / posta | 21 | Sayı, tersine | Avro limitleri, "önce / sonra" süreleri, araç muafiyetinin tekrarı | 4 |
| Geçici ithalat | 18 | Komşu | Tanım, aylık oran, yasak işlemler, taşıt belgeleri | 4 |
| Transit / TIR | 17 | Komşu, liste dışı | Teminat istisnaları, sona erme ↔ ibra, TIR saatleri | 4 |
| Kaçakçılık (5607) | 27 (10-7-4-3-3) | Komşu, liste dışı, sağduyu | Kapalı görevli listesi, artırım oranları, gümrüklenmiş değer | 3 |
| İhracat / geri gelen eşya | 14 | Komşu, yakın sayı | Terk tarihi, süreler, beyanname kapatma, rejim kodu | 3 |
| Serbest dolaşım / nihai kullanım / fikri haklar | 12 | Komşu, tersine | Statü kaybı hâlleri, devir, lehe oran şartları | 3 |
| YYS / OKSB | 11 | Sayı | Faaliyet süresi, hat türleri, sertifikanın süresi | 2 |
| Tarife / BTB (yalnızca usul) | 11 | Terim | Basamak sayıları, BTB'yi düzenleyen makam, geçersizlik hâlleri | 2 |

Deneme kuralları:

- Sorular konu blokları hâlinde dizilir; Bakanlığın A kitapçığı da böyledir.
- Bölüm 13'teki set profili deneme bütününe uygulanır: 80 soruda olumsuz kök 24–36, önermeli 12–16, vaka 8–12.
- Her denemede en az bir güncellik sorusu (yüklenen metinde varsa), bir meslek yanlılığı sorusu ve az sorulmuş alanlardan bir iki soru bulunur.
- İkiz eksenlerden en az altısı denemede ölçülür; uygun olanlar ayna çiftle.

## 15. Gerekçe standardı ve genel format

Her sorunun altında mutlaka "Doğru Cevap:" ve "Gerekçe:" bulunur.

### Gerekçe

1. Doğru cevabı açıkça açıklar.
2. Mevzuattaki ilgili hükmü anlaşılır biçimde aktarır.
3. Varsa sorudaki tuzak noktayı belirtir. En güçlü çeldiricinin metindeki yeri bir cümleyle söylenir; örneğin "D şıkkındaki süre denizyoluyla gelen eşyaya aittir; soru diğer yollarla geleni soruyor."
4. Öğrenci mevzuat maddesini hiç okumamış olsa bile cevabın neden doğru olduğunu anlayabilecek açıklıktadır.
5. Yalnızca madde numarasına gönderme yapmaz.
6. Hüküm son 12 ayda değiştiyse değişiklik tarihini belirtir.

Kullanılmaz: "Madde hükmüdür.", "Temel düzenlemedir.", "Madde bunu söylemektedir.", "13. maddeye göre C şıkkıdır."

Tercih edilen: "Mevzuata göre … . Bu nedenle doğru cevap C seçeneğidir."

Gerekçe gereksiz yere uzatılmaz. Cümle bittikten sonra, öğrencinin açıp kendisi kontrol edebilmesi için ilgili madde "(MD 15-16)" biçiminde yazılır.

### Genel format

Her soru şu düzende hazırlanır:

```text
İlgili mevzuatın madde numarası

1- Soru kökü
A) …
B) …
C) …
D) …
E) …
Doğru Cevap: X
Gerekçe: … (MD …)
```

Kurallar:

- Soru sıra numarası ve soru aynı satırdan başlar.
- Her soru 5 şıklıdır.
- Sorular doğrudan baskıya hazırdır.
- Şıklarda gereksiz kalın yazı kullanılmaz.
- Soru kökü doğal tümce düzenindedir; gereksiz büyük harf kullanılmaz.
- Başlık ve alt bilgide yalnızca "Gümrük Koçu - Ufuk Çetintaş" yazar.

## 16. Kurum dili ve nihai kalite kontrolü

Bu kontrollerden geçmeyen soru nihai çıktıya alınmaz.

### Kurum dili son kontrolü

Her soru tamamlandıktan sonra şu soru sorulur: "Bu soru gerçek çıkmış GMY soruları arasına konsaydı dil, kök yapısı ve ölçme biçimi bakımından yabancı durur muydu?" Cevap evetse soru yeniden düzenlenir. Kontrol edilenler:

- Soru kökü kurum diline benziyor mu?
- Ölçülen bilgi açık mı?
- Gereksiz açıklama var mı?
- Yapay zekâ dili veya kurumun kullanmadığı yapay ifade var mı?
- Daha uygun bir çıkmış soru kalıbı kullanılabilir mi?

### Her soru için nihai kalite kontrolü

Mevzuat kontrolü

1. Sorulan bilgi verilen mevzuatta açıkça var mı?
2. Doğru cevap yalnızca verilen mevzuattan kesin olarak çıkarılabiliyor mu?
3. Mevzuat dışı bilgi eklenmiş mi?

Kalıp kontrolü

4. Bilgi türü doğru belirlenmiş mi?
5. Bu bilgi için uygun kurum soru kalıbı seçilmiş mi?
6. Daha doğal bir çıkmış soru kalıbı var mı?

Dil kontrolü

7. Soru gerçek sınav dili taşıyor mu?
8. Hükmün konusu kökten anlaşılıyor mu?
9. Madde, fıkra veya bent ezberi isteniyor mu?
10. Yapay zekâ dili veya yapay niteleme var mı?

Şık kontrolü

11. Tek ve tartışmasız doğru cevap var mı?
12. Çeldiriciler güçlü mü?
13. Bariz yanlış şık var mı?
14. Şıklar birbirleriyle aynı kategoride mi?
15. Eski-yeni kurum adı nedeniyle iki doğruya yol açabilecek seçenek var mı?

Tekrar kontrolü

16. Aynı bilgi daha önce başka soruda ölçülmüş mü?
17. Yeni soru gerçekten farklı bir sınav noktası mı?

Cevap–gerekçe kontrolü

18. Doğru cevap harfi doğru mu?
19. Gerekçe gerçekten o şıkkı mı açıklıyor?
20. Şıkların sırası değiştirildiyse cevap ve gerekçe yeniden kontrol edilmiş mi?

GMY kontrolü

21. Kilit cümle madde metninden birebir mi? Değilse parafraz veya çıkarım bilinçli olarak mı seçildi?
22. Her çeldiricinin metindeki yuvası gösterilebiliyor mu? Uydurma çeldirici en aza indi mi?
23. Tek kelime değişikliğinde değiştirilen kelime hukuki sonucu gerçekten değiştiriyor mu?
24. Sayısal şıklar küçükten büyüğe sıralı mı, doğru değer B, C veya D'de mi?
25. Süre sorusunda başlangıç anı belli mi?
26. Kökteki mevzuat adı hükmün kaynağıyla aynı mı?
27. Kök doğru şıkkı ele veriyor mu?
28. İki şık savunulabilir görünüyor mu? Görünüyorsa lafza en yakın şık tek doğru kalacak biçimde çeldirici değiştirilir.
29. Aynı sette aynı hüküm aynı yönden iki kez sorulmuş mu?
30. Doğru şık bu sette sistematik olarak en uzun ya da en kısa şık mı?

## 17. Çalışma sonu raporu ve ana ilke

Set teslim edilirken sonuna kısa, insan diliyle yazılmış bir rapor eklenir.

### Çalışma sonu raporu

- Kapsanan çıkmış soru noktaları
- Metinde karşılığı bulunamayan çıkmış soru noktaları
- Set profili: birebir / parafraz / çıkarım sayısı; olumsuz kök; önermeli sorular ve kombinasyonları; vaka ve hesap; boşluk ve eşleştirme; tuzak dağılımı; cevap harfi dağılımı
- Soru sayısı kullanıcı tarafından verildiyse sete giremeyen önemli soru alanları (bir satır)
- Sayı verilmediyse: "Bu maddeden çıkarılabilecek sınav değeri taşıyan soru alanları tüketilmiştir."

### Ana ilke

İlk olarak konuyla ilgili çıkmış sorular verilir ve ölçülen bilgiler tespit edilir. Daha sonra soru yapmak için gerekli mevzuat verilir. Her zaman şu sıra uygulanır:

1. Önce mevzuatı oku.
2. Sınavlık bilgiyi bul.
3. Karışabilecek noktayı bul: komşu fıkra, ikiz kavram, yakın sayı, benzer makam.
4. Bilgi türünü belirle.
5. Kurumun bu bilgiyi hangi kalıpla sorduğunu seç.
6. En uygun kökü kur.
7. Doğru cevabı madde cümlesinden al.
8. Çeldiricileri gerçek yuvalarından hazırla.
9. Açıklayıcı gerekçeyi yaz.
10. Set profilini ve cevap dağılımını kontrol et.
11. Cevap–gerekçe uyumunu son kez doğrula.
12. Kurum dili kontrolü yap.

### Nihai hedef

Hazırlanan soru yalnızca hukuken doğru olmaz. Aynı zamanda sınav değeri yüksek, özgün, ayırt edici, mevzuata sadık, güçlü çeldiricilere sahip ve Bakanlığın çıkmış soru diline ve soru kurma mantığına yakın olur.

Öğrenci soruyu gördüğünde "Bu soru GMY sınavında çıkabilecek nitelikte." hissini almalıdır. Yanlış yapan öğrenci bunu tahminden değil, iki hükmü karıştırmaktan yapmalı; gerekçeyi okuyunca neyi neyle karıştırdığını görmelidir.
