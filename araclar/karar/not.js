const fs = require('fs');
const { d, p, h1, h2, bullet, mono, table, box, pb, doc, coverPage } = require('./gk.js');
const B = [];
const add = (...x) => x.flat().forEach(e => B.push(e));

// ───────── BLOK 1
add(h1('📖 BLOK 1 — DERS NOTU'));
add(h2('1. Tanım ve Kapsam'));
add(h2('1.1. Karar nedir?'));
add(p('Gümrük mevzuatında "karar", sıradan bir yazışma değildir. Gümrük Kanunu kararı; **bağlayıcı tarife ve menşe bilgileri de dahil olmak üzere**, gümrük idaresinin gümrük mevzuatı ile ilgili olarak **belirli bir konuda bir veya daha fazla kişi üzerinde hukuki sonuç doğuracak idari tasarrufu** olarak tanımlar (GK md. 3/5).'));
add(p('Tanımdan üç unsur çıkar:'));
add(bullet('Kararı veren **gümrük idaresidir**.'), bullet('Karar **belirli bir konuya** ilişkindir.'), bullet('Karar **bir veya daha fazla kişi** üzerinde **hukuki sonuç doğurur**.'));
add(h2('1.2. Kim karar talep edebilir?'));
add(p('Gerekli bilgi ve belgelerle başvuran **her kişi**, gümrük mevzuatının uygulanmasına ilişkin bir karar vermesini gümrük idaresinden isteyebilir (GY md. 27/1).'));
add(p('Karar talep eden kişi, kararın verilebilmesi için **gerekli bütün bilgi ve belgeleri** söz konusu idarelere **ibraz etmek zorundadır** (GK md. 6/1). Yani eksiksiz başvuru yükü talep edenin üzerindedir.'));

add(h2('2. Şartlar — Başvurunun Şekli'));
add(p('Karar alınması talebinin **yazılı** olarak yapılması gerekir (GK md. 6/2). Mevzuat sözlü talep öngörmemiştir.'));

add(h2('3. Süreç'));
add(h2('3.1. Karar süresi ve tebliğ'));
add(p('Gümrük idareleri, talebe ilişkin başvurunun **kendilerine ulaştığı tarihten itibaren otuz gün içinde** karar alırlar. Verilen kararlar başvuru sahibine **yazılı olarak tebliğ** edilir (GK md. 6/2).'));
add(p('Mevzuat bu süreyi "otuz gün" olarak belirlemiştir; iş günü olarak nitelememiştir.'));
add(h2('3.2. Sürenin aşılması'));
add(p('Gümrük idareleri tarafından otuz günlük süreye uyulması mümkün değilse **süre aşılabilir**. Bu durumda idare, **süre dolmadan önce** başvuru sahibine şu iki bilgiyi verir (GK md. 6/2):'));
add(bullet('Süre aşımını **haklı kılan gerekçeler**,'), bullet('Talep hakkında karar vermek için **gerekli gördüğü ek süre**.'));
add(h2('3.3. Gerekçe ve itiraz yolu'));
add(p('Gümrük idareleri tarafından gerek **başvuruların reddine** gerekse **muhatabı kişinin aleyhine** olarak verilen yazılı kararlar; Kanunun Onikinci Kısmında belirtilen şekilde **itiraz yolu açık olmak üzere gerekçeli olarak** alınır ve **bu hususlar kararda belirtilir** (GK md. 6/3).'));
add(h2('3.4. Kararın uygulanması'));
add(p('Alınan kararlar gümrük idareleri tarafından **derhal uygulanır** (GK md. 6/4).'));

add(h2('4. Lehe Kararların İptali ve Değiştirilmesi'));
add(p('Temel kural: Gümrük idaresinin ilgilinin lehine olan kararları, **Kanunun 7 nci maddesinde belirtilen hallerde** değiştirilir veya iptal edilir (GY md. 27/2). Kanun iki ayrı durum düzenler.'));
add(h2('4.1. İptal edilir — halleri bir arada bulunan durum (GK md. 7/1)'));
add(p('Lehe karar, aşağıdaki hallerin **bir arada bulunması** durumunda **iptal edilir**:'));
add(bullet('a) Kararın **yanlış veya eksik bilgilere** dayanılarak verilmesi,'),
    bullet('b) Başvuru sahibinin bu yanlışlık veya eksikliği **bilmesi veya bilmesi gerektiği** haller,'),
    bullet('c) Kararın **doğru veya tam bilgilere dayanılarak verilmesinin mümkün olmamasının** tespiti.'));
add(h2('4.2. Değiştirilir veya iptal edilebilir (GK md. 7/2)'));
add(p('Aşağıdaki hallerde ise lehe karar **değiştirilir veya iptal edilebilir**:'));
add(bullet('a) Karara esas teşkil eden bir veya birden fazla koşulun **gerçekleşmemiş veya gerçekleşemez** olması,'),
    bullet('b) Lehine olan bir kararda öngörülen bir **yükümlülüğe ilgilinin uymaması**.'));
add(h2('4.3. İki fıkranın karşılaştırması'));
add(table(['Ölçüt', 'GK md. 7/1', 'GK md. 7/2'], [
  ['Kanunun ifadesi', '"iptal **edilir**"', '"değiştirilir veya iptal **edilebilir**"'],
  ['Mümkün sonuç', 'İptal', 'Değiştirme veya iptal'],
  ['Hallerin yapısı', 'a, b ve c hallerinin **bir arada** bulunması', 'Karara esas koşulun gerçekleşmemesi ya da yükümlülüğe uyulmaması (Kanunda "bir arada bulunma" şartı yer almaz)'],
  ['Yürürlük tarihi', '**İptal kararının verildiği** tarih', 'İptal veya değiştirme kararının **tebliğ** tarihi']], [2, 3, 4]));
add(p(''));
add(h2('4.4. Tebliğ ve yürürlük'));
add(p('Kararın iptali **muhatabına tebliğ edilir** (GK md. 7/3). Birinci fıkraya göre iptal, **iptal kararının verildiği tarihten**; ikinci fıkraya göre verilen iptal veya değiştirme kararı **tebliğ tarihinden** itibaren yürürlüğe girer (GK md. 7/4).'));
add(p('**İleri düzey (GM):** Karar muhatabının **yasal çıkarlarının gerektirdiği istisnai hallerde**, kararın iptalinin veya değiştirilmesinin yürürlük tarihi **yönetmelikle belirlenen koşullar altında ertelenebilir** (GK md. 7/4).'));
add(h2('4.5. Rejime tabi tutulmaya başlanmış eşya'));
add(p('Değiştirme ya da iptal kararları, **yürürlüğe girdikleri tarihte**, iptal edilen ya da değiştirilen kararlar uyarınca **bir gümrük rejimine tabi tutulmaya başlanmış eşya için uygulanmaz** (GY md. 27/3).'));
add(p('Bununla birlikte gümrük idareleri, **belirlenecek bir dönem içinde** bu eşyanın **gümrükçe onaylanmış bir işleme ya da kullanıma** tabi tutulmasını isteyebilir (GY md. 27/4). Gümrükçe onaylanmış işlem veya kullanım; eşyanın bir gümrük rejimine tabi tutulması, serbest bölgeye girmesi, Türkiye Gümrük Bölgesi dışına yeniden ihracı, imhası veya gümrüğe terk edilmesidir (GK md. 3/14).'));

add(h2('5. İtirazların Karara Bağlanması (GY md. 586)'));
add(p('İtirazlar aşağıdaki unsurların incelenmesiyle karara bağlanır:'));
add(bullet('Anlaşmazlığa konu **beyanname** ve sair her türlü belge,'),
    bullet('Eşyadan alınacak **örnek**,'),
    bullet('Örnek alınması mümkün değilse **eşyanın kendisi** veya **fotoğraf, katalog, prospektüs** gibi eşyayı görmeden fikir verecek diğer belgeler,'),
    bullet('Gerek duyulması halinde **ilgili gümrük idaresinin mütalaası**.'));
add(p('İtirazlar **otuz gün içinde** karara bağlanarak ilgili kişiye **tebliğ** edilir. Otuz gün içinde karar alınamadığı durumlarda **Kanunun 6 ncı maddesinin ikinci fıkrası** (süre aşımı usulü) uygulanır (GY md. 586/1).'));

// ───────── BLOK 2
add(pb(), h1('⭐ BLOK 2 — ÖNEMLİ BİLGİLER'));
add(h2('⏱️ Süreler'));
add(box(['⭐ Karar talebi, başvurunun idareye **ulaştığı tarihten itibaren otuz gün** içinde karara bağlanır (GK md. 6/2).',
  '⭐ Süreye uyulamıyorsa idare, **süre dolmadan önce** gerekçeleri ve gerekli **ek süreyi** başvuru sahibine bildirir (GK md. 6/2).',
  '⭐ İtirazlar **otuz gün** içinde karara bağlanıp tebliğ edilir; aşılırsa GK md. 6/2 uygulanır (GY md. 586/1).',
  '⭐ Rejime başlamış eşya için idare, **belirlenecek bir dönem** içinde gümrükçe onaylanmış işlem veya kullanım isteyebilir (GY md. 27/4).'], 'star'));
add(h2('💰 Tutarlar / Oranlar'));
add(box(['⭐ Bu konuda Gümrük Kanunu ve Gümrük Yönetmeliği tutar, oran veya katsayı öngörmemiştir.'], 'star'));
add(h2('🏛️ Makam / Yetki'));
add(box(['⭐ Kararı veren, iptal eden ve değiştiren makam **gümrük idaresidir** (GK md. 6, 7).',
  '⭐ Ret ve aleyhe kararlara karşı **Kanunun Onikinci Kısmında** belirtilen şekilde itiraz yolu açıktır (GK md. 6/3).',
  '⭐ İtiraz incelemesinde gerek duyulursa **ilgili gümrük idaresinin mütalaası** alınır (GY md. 586/1).',
  '⭐ Yürürlük tarihinin ertelenme koşulları **yönetmelikle** belirlenir (GK md. 7/4).'], 'star'));
add(h2('📋 Belgeler'));
add(box(['⭐ Talep eden, kararın verilebilmesi için **gerekli bütün bilgi ve belgeleri** ibraz etmek zorundadır (GK md. 6/1).',
  '⭐ Karar talebi **yazılı** yapılır; verilen karar başvuru sahibine **yazılı** tebliğ edilir (GK md. 6/2).',
  '⭐ Kararın iptali **muhatabına tebliğ** edilir (GK md. 7/3).',
  '⭐ İtirazda örnek alınamazsa **eşyanın kendisi** veya **fotoğraf, katalog, prospektüs** incelenir (GY md. 586/1).'], 'star'));
add(h2('⚖️ Yaptırımlar'));
add(box(['⭐ Bu konuda ceza hükmü yoktur. Kararda öngörülen **yükümlülüğe uyulmaması**, lehe kararın değiştirilmesi veya iptal edilebilmesi sonucunu doğurur (GK md. 7/2-b).'], 'star'));

// ───────── BLOK 3
add(pb(), h1('💊 BLOK 3 — HAP KAVRAMLAR'));
[['Karar', 'Bağlayıcı tarife ve menşe bilgileri dahil, gümrük idaresinin belirli bir konuda bir veya daha fazla kişi üzerinde hukuki sonuç doğuran idari tasarrufu (GK md. 3/5).'],
 ['Karar talebi', 'Gerekli bütün bilgi ve belgelerle, yazılı olarak gümrük idaresine yapılan başvuru (GK md. 6/1-2; GY md. 27/1).'],
 ['Tebliğ', 'Verilen kararın başvuru sahibine yazılı olarak; kararın iptalinin muhatabına bildirilmesi (GK md. 6/2, 7/3).'],
 ['Süre aşımı', 'İdarenin otuz günlük süreye uyamaması halinde, süre dolmadan gerekçe ve ek süre bildirerek süreyi aşabilmesi (GK md. 6/2).'],
 ['Gerekçeli karar', 'Ret ve aleyhe yazılı kararların, itiraz yolu açık olmak üzere gerekçesiyle alınması (GK md. 6/3).'],
 ['İptal edilir', 'Yanlış/eksik bilgi, başvuranın bunu bilmesi veya bilmesi gerekmesi ve doğru bilgiyle karar verilememesi bir aradaysa lehe kararın iptali (GK md. 7/1).'],
 ['Değiştirilir veya iptal edilebilir', 'Karara esas koşul gerçekleşmez ya da yükümlülüğe uyulmazsa lehe karar hakkında öngörülen sonuç (GK md. 7/2).'],
 ['Yürürlüğün ertelenmesi', 'Muhatabın yasal çıkarlarının gerektirdiği istisnai hallerde, yönetmelikteki koşullarla iptal veya değiştirmenin yürürlüğünün ertelenmesi (GK md. 7/4).'],
 ['Rejime başlamış eşya istisnası', 'Değiştirme veya iptal, yürürlük tarihinde rejime tabi tutulmaya başlanmış eşyaya uygulanmaz (GY md. 27/3).'],
 ['Gümrükçe onaylanmış işlem veya kullanım', 'Rejime tabi tutma, serbest bölgeye giriş, yeniden ihraç, imha veya gümrüğe terk (GK md. 3/14).'],
 ['Mütalaa', 'İtiraz incelemesinde gerek duyulduğunda ilgili gümrük idaresinden alınan görüş (GY md. 586/1).']
].forEach(([k, v]) => add(p(`💊 **${k}:** ${v}`)));

// ───────── BLOK 4
add(pb(), h1('🗺️ BLOK 4 — MİNİ ŞEMA / DİYAGRAMLAR'));
add(h2('Şema 1 — Karar süreci akışı'));
add(p('**Yazılı başvuru + bütün bilgi ve belgeler** → **İdareye ulaşma (0. gün)** → **İnceleme** → **Karar (en geç 30. gün)** → **Yazılı tebliğ** → **Derhal uygulama** → (ret/aleyhe ise) **İtiraz** → **İtiraz kararı (30 gün)** → **Tebliğ**'));
add(h2('Şema 2 — Zaman çizelgesi'));
add(table(['An', 'Ne olur?', 'Dayanak'], [
  ['0. gün', 'Yazılı başvuru gümrük idaresine ulaşır; süre başlar.', 'GK md. 6/2'],
  ['30. gün dolmadan', 'Karar alınır ve yazılı tebliğ edilir; ya da süre aşılacaksa gerekçe ve ek süre başvuru sahibine bildirilir.', 'GK md. 6/2'],
  ['Ek süre sonu', 'İdarenin bildirdiği ek süre içinde karar verilir.', 'GK md. 6/2'],
  ['Karar sonrası', 'Karar derhal uygulanır; ret/aleyhe ise itiraz yolu açıktır.', 'GK md. 6/3, 6/4'],
  ['İtirazdan itibaren', 'İtiraz 30 gün içinde karara bağlanıp tebliğ edilir; aşılırsa GK md. 6/2 uygulanır.', 'GY md. 586/1']], [2, 6, 2]));
add(h2('Şema 3 — Lehe kararın akıbeti (karar ağacı)'));
['İLGİLİNİN LEHİNE OLAN KARAR',
 '├── Yanlış/eksik bilgi + başvuran biliyor/bilmesi gerekir',
 '│   + doğru bilgiyle verilemez  (ÜÇÜ BİR ARADA)',
 '│   └── İPTAL EDİLİR  →  yürürlük: iptal kararının verildiği tarih',
 '├── Karara esas koşul gerçekleşmemiş / gerçekleşemez',
 '│   └── DEĞİŞTİRİLİR VEYA İPTAL EDİLEBİLİR  →  yürürlük: tebliğ tarihi',
 '├── Kararda öngörülen yükümlülüğe uyulmamış',
 '│   └── DEĞİŞTİRİLİR VEYA İPTAL EDİLEBİLİR  →  yürürlük: tebliğ tarihi',
 '└── Her durumda',
 '    ├── İptal muhatabına tebliğ edilir',
 '    ├── Yasal çıkar gerektirirse yürürlük ertelenebilir (yönetmelik)',
 '    └── Rejime başlamış eşyaya uygulanmaz; idare belirlenecek',
 '        dönemde gümrükçe onaylanmış işlem/kullanım isteyebilir'].forEach(l => add(mono(l)));

// ───────── BLOK 5
add(pb(), h1('⚠️ BLOK 5 — SINAVDA DİKKAT NOTU'));
add(box([
 '⚠️ **"Bir arada" kelimesini kaçırma!** Lehe kararın iptal edilmesi için üç halin birlikte bulunması gerekir; yalnızca yanlış bilgiye dayanılmış olması yetmez.',
 '⚠️ **"İptal edilir" ile "değiştirilir veya iptal edilebilir"i karıştırma!** Birincisi 7/1 (üç hal bir arada), ikincisi 7/2 (koşulun gerçekleşmemesi, yükümlülüğe uyulmaması).',
 '⚠️ **Yürürlük tarihleri yer değiştirilerek sorulur.** 7/1 → iptal kararının verildiği tarih; 7/2 → tebliğ tarihi.',
 '⚠️ **"Otuz gün" ifadesine dikkat et!** Mevzuat iş günü demez; başlangıç, başvurunun idareye ulaştığı tarihtir. İtirazlarda da süre otuz gündür.',
 '⚠️ **Süre aşımı ret demek değildir.** İdare süreyi aşabilir; ancak süre dolmadan gerekçeyi ve ek süreyi bildirmek zorundadır.',
 '⚠️ **Gerekçe zorunluluğu kimin için?** Ret ve aleyhe yazılı kararlar gerekçeli alınır; itiraz yolunun açık olduğu kararda belirtilir.',
 '⚠️ **Olumsuz kök adayı:** "Değiştirme veya iptal kararları rejime tabi tutulmaya başlanmış eşyaya **uygulanmaz**" — "uygulanır" şeklindeki şık yanlıştır.',
 '⚠️ **Erteleme kimin yararına?** Karar muhatabının yasal çıkarları için ve yönetmelikle belirlenen koşullarla; idarenin çıkarı için değil.',
 '⚠️ **Makam tuzağı:** İtirazda mütalaası alınabilecek merci "ilgili gümrük idaresi"dir; üst makam onayı öngörülmemiştir.',
 '⚠️ **Tanım tuzağı:** Bağlayıcı tarife ve menşe bilgileri de "karar" kapsamındadır.'], 'warn'));

// ───────── BLOK 6
add(pb(), h1('📝 BLOK 6 — DERS ÖZETİ'));
add(h2('Bu dersten aklında kalması gerekenler'));
['Karar, gümrük idaresinin belirli bir konuda kişiler üzerinde hukuki sonuç doğuran idari tasarrufudur; bağlayıcı tarife ve menşe bilgileri de karardır.',
 'Talep yazılı yapılır; gerekli bütün bilgi ve belgeler talep edence ibraz edilir.',
 'İdare, başvurunun ulaştığı tarihten itibaren otuz gün içinde karar alır ve kararı yazılı tebliğ eder.',
 'Süreye uyulamıyorsa süre dolmadan gerekçe ve ek süre bildirilir.',
 'Ret ve aleyhe kararlar gerekçeli alınır, itiraz yolu kararda belirtilir; kararlar derhal uygulanır.',
 'Üç hal bir aradaysa lehe karar iptal edilir (yürürlük: iptal kararının verildiği tarih).',
 'Koşul gerçekleşmezse veya yükümlülüğe uyulmazsa lehe karar değiştirilir veya iptal edilebilir (yürürlük: tebliğ tarihi).',
 'İptal veya değiştirme, rejime tabi tutulmaya başlanmış eşyaya uygulanmaz; idare belirlenecek dönemde gümrükçe onaylanmış işlem veya kullanım isteyebilir.',
 'İtirazlar otuz gün içinde karara bağlanır; aşılırsa süre aşımı usulü uygulanır.'].forEach(t => add(bullet(t)));
add(p(''));
add(p('**Kapanış:** Karar konusu; talebin şekli ve süresiyle başlar, kararın gerekçesi, tebliği ve derhal uygulanmasıyla devam eder, lehe kararların iptal ve değiştirilmesiyle ilerler. Sınavın odak noktası 7. maddedeki iki fıkranın ayrımı ve yürürlük tarihleridir. Otuz günlük süreler hem karar talebinde hem itirazda karşınıza çıkar.'));
add(h2('Süre / Tutar Özet Tablosu'));
add(table(['İşlem', 'Süre', 'Başlangıç / Yürürlük', 'Dayanak'], [
  ['Karar talebinin sonuçlandırılması', '30 gün', 'Başvurunun idareye ulaştığı tarih', 'GK md. 6/2'],
  ['Süre aşımı bildirimi', 'Süre dolmadan önce', 'Gerekçe + ek süre bildirilir', 'GK md. 6/2'],
  ['İtirazın karara bağlanması', '30 gün', 'Aşılırsa GK md. 6/2 uygulanır', 'GY md. 586/1'],
  ['İptal (üç hal bir arada)', '—', 'İptal kararının verildiği tarih', 'GK md. 7/4'],
  ['Değiştirme veya iptal (7/2)', '—', 'Tebliğ tarihi', 'GK md. 7/4'],
  ['Rejime başlamış eşya', 'Belirlenecek dönem', 'İdare GOİK isteyebilir', 'GY md. 27/4']], [4, 2, 4, 2]));

const out = doc({ header: 'GÜMRÜK KOÇU | Karar Ders Notu', footer: "Gümrük Koçu – Ufuk Çetintaş'a aittir | @gumrukkocunuz",
  cover: coverPage('KARAR', 'Gümrük Mevzuatının Uygulanmasına İlişkin Kararlar', 'GM / GMY Sınavlarına Hazırlık Ders Notu'), body: B });
d.Packer.toBuffer(out).then(b => { fs.writeFileSync('Ders_Notu_Karar.docx', b); console.log('ok'); });
