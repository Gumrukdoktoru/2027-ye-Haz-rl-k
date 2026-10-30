# GM Soru Bankası — M58: İthalatta Korunma ve Gözetim Önlemleri, Kota ve Tarife Kontenjanı, Ticari Hakların Korunması (8 soru)
# Gümrük Koçu - Ufuk Çetintaş
K = "58-korunma-gozetim-kota.txt"
KYON = "İthalatta Korunma Önlemleri Yönetmeliği"


def s(**k):
    base = dict(
        konu="Korunma, Gözetim, Kota ve Ticari Haklar",
        blok="M58",
        sirali=False,
        vaka=False,
        baslangic=False,
        eksen=0,
        ayna="",
        guncellik="",
        cikmis="",
        kapsamli=False,
    )
    base.update(k)
    return base


Q = [
    # 1 ---------------- Geçici korunma önlemi teminatı: kesin önlem düşükse fark iade ----------------
    s(
        kalip="SONUÇ",
        z="Z",
        madde="İthalatta Korunma Önlemleri Hakkında Karar (2004/7305) md. 5; Yönetmelik md. 9",
        cek="Korunma önlemi alınırsa teminat Hazineye irat; önlem geçiciden düşükse fark iade, yüksekse fark tahsil edilmez; önleme gerek yoksa teminat iade.",
        kok=[
            "İthalatta Korunma Önlemleri Hakkında Karara göre, gümrük vergisinde artış şeklinde uygulanan geçici korunma önlemi sırasında aradaki fark teminata bağlanmış ve soruşturma sonucunda alınan korunma önlemi geçici korunma önleminden daha düşük belirlenmişse aşağıdakilerden hangisi uygulanır?"
        ],
        d="Teminata bağlanan tutar Hazineye irat kaydedilir; aradaki fark ilgiliye iade edilir.",
        c=[
            "Teminata bağlanan tutar Hazineye irat kaydedilir; aradaki fark tahsil edilmez.",
            "Teminata bağlanan tutarın tamamı ilgiliye iade edilir.",
            "Teminata bağlanan tutar Hazineye irat kaydedilir; aradaki fark ilgiliden ayrıca tahsil edilir.",
            "Teminata bağlanan tutarın tamamı Hazineye irat kaydedilir; aradaki fark iade edilmez.",
        ],
        g="İthalatta Korunma Önlemleri Hakkında Karara göre geçici korunma önlemi gümrük vergisinde artış şeklinde uygulanırsa, İthalat Rejimi Kararındaki oran ile geçici önlem oranı arasındaki farka tekabül eden tutar teminata bağlanır. Soruşturma sonunda korunma önlemi alınmasına karar verilirse teminata bağlanan tutar Hazineye irat kaydedilir; korunma önlemi geçici önlemden daha düşük belirlenirse aradaki fark ilgiliye iade edilir, daha yüksekse aradaki fark tahsil edilmez. Korunma önlemine gerek olmadığına karar verilirse geçici önlem yürürlükten kaldırılır ve teminat, teminata bağlanan vergilerin geri verilmesine ilişkin hükümler dahilinde ilgililere iade edilir. En güçlü tuzak farkın tahsil edilmeyeceğini söyleyen seçenektir: aynı hükümde yer alan bu sonuç, korunma önleminin geçici önlemden daha yüksek belirlendiği duruma aittir. Bu nedenle doğru cevap 'Teminata bağlanan tutar Hazineye irat kaydedilir; aradaki fark ilgiliye iade edilir.' seçeneğidir. (MD Korunma Önlemleri Kararı md. 5)",
        kanit=f"{K} | belirlenen gümrük vergisi oranı arasındaki FARKA TEKABÜL EDEN TUTAR gümrük mevzuatının ilgili hükümlerine göre TEMİNATA BAĞLANIR. || {K} | Soruşturma sonucunda KORUNMA ÖNLEMİ ALINMASINA KARAR VERİLMESİ halinde, TEMİNATA BAĞLANAN TUTAR Hazineye İRAT KAYDEDİLİR. || {K} | DAHA DÜŞÜK belirlenmesi halinde ARADAKİ FARK İLGİLİYE İADE EDİLİR. || {K} | DAHA YÜKSEK olması halinde ise ARADAKİ FARK TAHSİL EDİLMEZ. || {K} | vergilerin geri verilmesine ilişkin hükümleri dahilinde İLGİLİLERE İADE EDİLİR.",
        yuva=[
            "Karar: korunma önlemi geçici önlemden yüksekse fark tahsil edilmez",
            "Karar: korunma önlemine gerek olmadığına karar verilirse teminat iadesi",
            "Ters sonuç: farkın tahsili",
            "Ters sonuç: farkın iade edilmemesi",
        ],
        yakinlik="BİREBİR",
        tuzak=["KOMŞU", "TERSİNE"],
        duzey=["UYGULAMA"],
        profil=[4],
        olumsuz=False,
        eksen=1,
        ayna="korunma önlemi geçiciden düşük: fark iade ↔ yüksek: fark tahsil edilmez",
        cikmis="2022/12",
    ),
    # 2 ---------------- Korunma önleminin süresi ve gözden geçirilmesi (önermeli) ----------------
    s(
        kalip="ÖNERMELİ",
        z="Z",
        madde="İthalatta Korunma Önlemleri Yönetmeliği md. 11",
        cek="Önlem geçici dahil 4 yılı aşamaz; 1 yıl üstü liberalize; 3 yıl üstü en geç ortasında gözden geçirme; uzatmada DTÖ için 10 yıl.",
        kok=[
            f"{KYON}'ne göre korunma önleminin süresi ve gözden geçirilmesi hakkında;",
            "I. Korunma önleminin süresi, uzatılmadıkça, geçici önlemler de dahil dört yılı aşamaz.",
            "II. Korunma önleminin süresinin iki yılın üzerinde olduğu durumlarda önlem düzenli aralıklarla liberalize edilir.",
            "III. Süresi uzatılan önlem, başlangıç süresinin sonundaki durumuna kıyasla daha kısıtlayıcı hale getirilebilir.",
            "IV. Süre uzatılması halinde önlemin toplam süresi Dünya Ticaret Örgütü üyesi ülkeler için on yılı aşamaz.",
            "V. Önlem süresinin üç yılı geçtiği durumlarda, en geç önlem süresinin ortasında durum gözden geçirilir.",
            "ifadelerinden hangileri doğrudur?",
        ],
        d="I, IV ve V",
        c=["I ve IV", "II ve III", "II, III ve V", "I, II, IV ve V"],
        sirali=True,
        siklar=["I ve IV", "II ve III", "I, IV ve V", "II, III ve V", "I, II, IV ve V"],
        g="Yönetmeliğe göre korunma önlemi, ciddi zararı önleyecek ve yerli üreticilerin uyumunu kolaylaştıracak süre için uygulanır ve uzatılmadıkça geçici önlemler de dahil dört yılı aşamaz (I doğru). Önlem süresi iki yılın değil, bir yılın üzerindeyse önlem düzenli aralıklarla liberalize edilir (II yanlış). Önlemin süresi yeniden açılacak soruşturma sonucunda uzatılabilir; ancak süresi uzatılan önlem başlangıç süresinin sonundaki durumuna kıyasla daha kısıtlayıcı olmaz ve liberalize edilmeye devam eder (III yanlış). Uzatma halinde toplam süre Dünya Ticaret Örgütü üyesi ülkeler için on yılı aşamaz (IV doğru). Önlem süresi üç yılı geçiyorsa, uygulamanın hâlâ gerekli olup olmadığını tespit etmek veya liberalleştirmeyi hızlandırmak için en geç önlem süresinin ortasında durum gözden geçirilir (V doğru). En güçlü tuzak II. önermedir: liberalizasyon eşiği ile gözden geçirme eşiği farklı sayılara bağlandığı için karıştırılır. Bu nedenle doğru cevap 'I, IV ve V' seçeneğidir. (MD Korunma Önlemleri Yönetmeliği md. 11)",
        kanit=f"{K} | KORUNMA ÖNLEMİNİN SÜRESİ üçüncü fıkra çerçevesinde uzatılmadıkça, geçici önlemler de dahil 4 YILI AŞAMAZ. || {K} | Korunma önleminin SÜRESİNİN 1YILIN ÜZERİNDE olduğu durumlarda önlem düzenli aralıklarla liberalize edilecektir. || {K} | Süresi uzatılan önlem, başlangıç süresinin sonundaki durumuna kıyasla daha kısıtlayıcı olmayacak ve liberalize edilmeye devam edilecektir. || {K} | Bu durumda önlemin toplam süresi DÜNYA TİCARET ÖRGÜTÜ ÜYESİ ÜLKELER için ON (10) YILI AŞAMAZ. || {K} | Önlem süresinin ÜÇ (3) YILI GEÇTİĞİ DURUMLARDA || {K} | ÖNLEM SÜRESİNİN EN GEÇ ORTASINDA durum gözden geçirilecektir.",
        yuva=[
            "I ve IV: gözden geçirme zamanını bilmeyen aday (eksik seçim)",
            "II ve III: liberalizasyon eşiğini ve uzatma kuralını yanlış bilen aday",
            "II, III ve V: dört yıllık sınırı bilmeyen aday",
            "I, II, IV ve V: liberalizasyon eşiğini iki yıl sanan aday",
        ],
        yakinlik="PARAFRAZ",
        tuzak=["YAKIN-SAYI", "TERSİNE"],
        duzey=["AYIRT", "BÜTÜNLEŞİK"],
        profil=[2, 3],
        olumsuz=False,
    ),
    # 3 ---------------- Küçük hesap: yeniden önlem uygulanamayacak süre (4 ÷ 2) ----------------
    s(
        kalip="HESAP",
        z="O",
        madde="İthalatta Korunma Önlemleri Yönetmeliği md. 11",
        cek="DTÖ üyelerinden ithalatta, en az iki yıl uygulanmış önlemin süresinin yarısı kadar yeniden önlem uygulanmaz; istisna 180 gün veya daha kısa önlem.",
        kok=[
            f"{KYON}'ne göre aşağıdaki bilgiler veriliyor:",
            "- Bir ürünün Dünya Ticaret Örgütü üyesi ülkelerden yapılan ithalatına 4 yıl süreyle korunma önlemi uygulanmış ve önlem sona ermiştir.",
            "- Aynı ürüne yeniden uygulanması düşünülen korunma önleminin süresi 180 günden uzundur.",
            "Buna göre, önceki önlemin sona ermesinden itibaren kaç yıl süreyle aynı ürünün Dünya Ticaret Örgütü üyesi ülkelerden ithaline yeniden korunma önlemi uygulanamaz?",
        ],
        d="2",
        c=["1", "3", "4", "10"],
        sirali=True,
        siklar=["1", "2", "3", "4", "10"],
        g="Yönetmeliğe göre korunma önlemine tabi olmuş bir ürünün Dünya Ticaret Örgütü üyesi ülkelerden ithaline, uygulama süresi en az iki yıl olmak şartıyla, daha önce uygulanmış önlem süresinin yarısına eşit bir süre boyunca yeniden korunma önlemi uygulanmaz. Vakada önceki önlem 4 yıl uygulanmıştır ve iki yıllık asgari şart sağlanmıştır: yasak süre = 4 ÷ 2 = 2 yıl. 180 gün veya daha kısa süreli önlemler için tanınan istisna (önlemin yürürlüğünden en az bir yıl geçmiş ve önceki beş yılda aynı ürüne ikiden fazla uygulanmamış olması) burada uygulanmaz, çünkü yeni önlemin süresi 180 günden uzundur. 1 yıl istisnadaki bekleme süresinden, 3 yıl gözden geçirme eşiğinden, 4 yıl önlemin kendi süresinden, 10 yıl ise uzatmadaki azami toplam süreden türetilmiştir. En güçlü tuzak 4 yıldır: yasak süreyi önceki önlem süresinin tamamı sanan aday bu değeri seçer. Bu nedenle doğru cevap '2' seçeneğidir. (MD Korunma Önlemleri Yönetmeliği md. 11)",
        kanit=f"{K} | uygulama süresi EN AZ İKİ (2) YIL OLMAK ŞARTIYLA, || {K} | DAHA ÖNCE UYGULANMIŞ OLAN ÖNLEM SÜRESİNİN YARISINA EŞİT BİR SÜRE BOYUNCA yeniden korunma || {K} | 180 (YÜZ SEKSEN) GÜN veya daha az süreli bir korunma önlemi yeniden uygulanabilir. || {K} | Önlemin yürürlüğe girdiği tarihten önceki 5 (BEŞ) YIL İÇİNDE AYNI ÜRÜNE KARŞI İKİ (2) DEFADAN FAZLA",
        yuva=[
            "180 günlük istisnadaki bir yıllık bekleme süresiyle karıştırma",
            "Üç yıllık gözden geçirme eşiğiyle karıştırma",
            "Yasak süreyi önceki önlem süresinin tamamı sanma (yarıya bölmeme)",
            "DTÖ üyelerinde azami on yıllık toplam süreyle karıştırma",
        ],
        yakinlik="ÇIKARIM",
        tuzak=["AD-HESAP", "YAKIN-SAYI"],
        duzey=["UYGULAMA"],
        profil=[4],
        olumsuz=False,
        vaka=True,
    ),
    # 4 ---------------- Gözetim: gözetim belgesi devredilemez (olumsuz) ----------------
    s(
        kalip="YANLIŞ",
        z="O",
        madde="İthalatta Gözetim Uygulaması Hakkında Karar (2004/7304) md. 4; Yönetmelik md. 3, 4",
        cek="Gözetim ileriye yönelik (belgeyle) veya geçmişe dönük; belge 10 işgününde ücretsiz, devredilemez; %5'e kadar aşım engel değil, Genel Müdürlük %10'a kadar oran belirleyebilir.",
        kok=[
            "İthalatta Gözetim Uygulaması Hakkında Karar ve İthalatta Gözetim Uygulanması Yönetmeliğine göre gözetim uygulaması ve gözetim belgesi hakkında aşağıdakilerden hangisi yanlıştır?"
        ],
        d="Gözetim belgesi, belge sahibinin yazılı muvafakatiyle üçüncü kişilere devredilebilir.",
        c=[
            "Gözetim kararı, gözetim belgesi düzenlenmesi yoluyla ileriye yönelik olarak veya gerçekleşen ithalatı değerlendirmek üzere geçmişe dönük olarak uygulanabilir.",
            "İleriye yönelik gözetime tabi bir malın ithalatında gümrük mevzuatının gerektirdiği belgelerin yanı sıra gözetim belgesi de aranır.",
            "Gözetim belgesi, usulüne uygun başvurunun Genel Müdürlüğe ulaşmasından itibaren 10 işgünü içinde talep edilen tüm miktar üzerinden ücretsiz olarak verilir.",
            "Gümrüklerce tespit ve kabul edilen kıymet veya miktarın belgedekini toplam %5'ten (%5 dâhil) daha az aşması ithalatı engellemez; Genel Müdürlük %10'u aşmamak üzere farklı bir oran tespit edebilir.",
        ],
        g="İthalatta Gözetim Uygulaması Hakkında Karar ve Yönetmeliğe göre bir malın ithalatında gözetim uygulanmasına ilişkin karar başvuru üzerine veya re'sen İthalat Genel Müdürlüğünce verilir; gözetim, gözetim belgesi düzenlenmesi yoluyla ileriye yönelik veya gerçekleşen ithalatı değerlendirmek üzere geçmişe dönük olarak uygulanabilir. İleriye yönelik gözetimde gümrük mevzuatının gerektirdiği belgelerin yanı sıra gözetim belgesi aranır. Gözetim belgesi usulüne uygun başvurunun Genel Müdürlüğe ulaşmasından itibaren 10 işgünü içinde talep edilen tüm miktar üzerinden ücretsiz verilir. Gümrüklerce kabul edilen kıymet veya miktarın belgedekini toplam yüzde 5'ten (dâhil) daha az aşması ithalatı engellemez; Genel Müdürlük yüzde 10'u aşmamak üzere farklı oran belirleyebilir. Gözetim belgeleri ise devredilemez; belgenin üçüncü kişilere devredildiğinin denetim birimlerince belirlenmesi halinde belgeler iptal edilir ve gözetim uygulaması yürürlükte olduğu süre içinde bir daha belge düzenlenmez. En güçlü tuzak geçmişe dönük gözetimdir: gözetimin yalnız belgeyle yürüdüğü sanıldığı için yanlış görünür. Bu nedenle doğru cevap 'Gözetim belgesi, belge sahibinin yazılı muvafakatiyle üçüncü kişilere devredilebilir.' seçeneğidir. (MD Gözetim Kararı md. 4, 7; Gözetim Yönetmeliği md. 3, 4)",
        kanit=f"{K} | Gerçekleşen ithalatı değerlendirmek üzere GEÇMİŞE DÖNÜK olarak uygulanabilir. || {K} | İLERİYE YÖNELİK GÖZETİME TABİ BİR MALIN İTHALATINDA || {K} | 10 (ON) İŞGÜNÜ içinde talep edilen tüm miktar üzerinden, ÜCRETSİZ OLARAK VERİLİR. || {K} | GÖZETİM BELGELERİ DEVREDİLEMEZ. || {K} | Toplam %5'ten (%5 dahil) daha az bir oranda aşması İTHALATIN YAPILMASINI ENGELLEMEZ. || {K} | %10'U AŞMAMAK ÜZERE FARKLI BİR ORAN TESPİT EDEBİLİR. || {K} | Gözetim uygulaması yürürlükte olduğu süre içerisinde BİR DAHA GÖZETİM BELGESİ DÜZENLENMEZ.",
        yuva=[
            "Gözetim Kararı ve Yönetmeliği: ileriye yönelik ve geçmişe dönük gözetim (doğru)",
            "Gözetim Yönetmeliği: gözetim belgesi aranması (doğru)",
            "Gözetim Yönetmeliği: 10 işgünü, ücretsiz (doğru)",
            "Gözetim Yönetmeliği: %5 ve %10 tolerans (doğru)",
        ],
        yakinlik="BİREBİR",
        tuzak=["TERSİNE", "SAĞDUYU"],
        duzey=["AYIRT"],
        profil=[3],
        olumsuz=True,
    ),
    # 5 ---------------- Gözetim Tebliği 2022/1: Kayıt Belgesi 45 gün ----------------
    s(
        kalip="SÜRE",
        z="O",
        madde="İthalatta Gözetim Uygulanmasına İlişkin Tebliğ (Tebliğ No: 2022/1) md. 2, 5, 6",
        cek="Kayıt Belgesi ihracatçı birliklerince en geç 10 iş gününde; 45 gün geçerli; birden fazla beyannamede kullanılamaz, uzatılamaz, devredilemez.",
        kok=[
            "İthalatta Gözetim Uygulanmasına İlişkin Tebliğ (Tebliğ No: 2022/1) kapsamında, kayda alınmak suretiyle gözetime tabi eşyanın ithalatı için düzenlenen Kayıt Belgesinin geçerlilik süresi ve kullanımı hakkında aşağıdakilerden hangisi doğrudur?"
        ],
        d="Kayıt Belgesi 45 gün geçerlidir; birden fazla beyanname için kullanılamaz ve süresi uzatılamaz.",
        c=[
            "Kayıt Belgesi 45 gün geçerlidir; süresi içinde birden fazla beyanname için kullanılabilir.",
            "Kayıt Belgesi 10 iş günü geçerlidir; süresi uzatılamaz.",
            "Kayıt Belgesi 45 gün geçerlidir; Genel Müdürlükçe bir defaya mahsus uzatılabilir.",
            "Kayıt Belgesi 40 gün geçerlidir; birden fazla beyanname için kullanılamaz.",
        ],
        g="İthalatta Gözetim Uygulanmasına İlişkin Tebliğe göre Ek-1'deki ürünleri ithal etmek isteyenler, ithalattan önce bilgilerini Ticaret Bakanlığınca Kayıt Merkezi olarak yetkilendirilen ihracatçı birlikleri genel sekreterliklerine kaydettirir ve elektronik ortamda Kayıt Belgesi düzenlenir; tam ve usulüne uygun başvurular en geç 10 iş günü içinde sonuçlandırılır. Kayıt Belgesinin geçerlilik süresi 45 gündür; bir Kayıt Belgesi birden fazla beyanname için kullanılamaz ve süresi uzatılamaz; belge üçüncü kişilere de devredilemez. Serbest dolaşıma girişte belgenin TPS numarası beyannamenin 44 numaralı hanesine menşe ayrımı yapılmaksızın kaydedilir. 10 iş günü başvurunun sonuçlandırılma süresi, 40 gün ise korunma soruşturmasında ilgili tarafların görüş bildirme süresidir. En güçlü tuzak birden fazla beyannamede kullanılabildiğini söyleyen seçenektir: süre doğrudur, fakat belge tek beyanname içindir. Bu nedenle doğru cevap 'Kayıt Belgesi 45 gün geçerlidir; birden fazla beyanname için kullanılamaz ve süresi uzatılamaz.' seçeneğidir. (MD Gözetim Tebliği 2022/1 md. 2, 5, 6)",
        kanit=f"{K} | Kayıt Belgelerinin GEÇERLİLİK SÜRESİ 45 (KIRKBEŞ) GÜNDÜR. || {K} | Bir Kayıt Belgesi BİRDEN FAZLA BEYANNAME İÇİN KULLANILAMAZ ve SÜRESİ UZATILAMAZ. || {K} | Tam ve usulüne uygun olarak yapılan Kayıt Belgesi başvuruları EN GEÇ 10 (ON) İŞ GÜNÜ içinde sonuçlandırılır. || {K} | Kayıt Merkezi olarak yetkilendirilen ilgili İHRACATÇI BİRLİKLERİ GENEL SEKRETERLİKLERİNE || {K} | Kayıt Belgesi ÜÇÜNCÜ KİŞİLERE DEVREDİLEMEZ. || {K} | ilan tarihinden itibaren KIRK (40) GÜN ile",
        yuva=[
            "Kullanım kuralının ters çevrilmesi",
            "Tebliğ: başvurunun 10 iş gününde sonuçlandırılması",
            "Uzatma yasağının ters çevrilmesi",
            "Korunma Yönetmeliği: soruşturmada 40 günlük görüş süresi",
        ],
        yakinlik="BİREBİR",
        tuzak=["YAKIN-SAYI", "TERSİNE"],
        duzey=["HATIRLAMA", "AYIRT"],
        profil=[1, 3],
        olumsuz=False,
    ),
    # 6 ---------------- Korunma Kurulu: soruşturmayı yürütmek Kurulun görevi değil ----------------
    s(
        kalip="KAPSAM_DIŞI",
        z="O",
        madde="İthalatta Korunma Önlemleri Hakkında Karar (2004/7305) md. 4; Yönetmelik md. 4",
        cek="Korunma Kurulu: soruşturma başlatma, geri çekmede devam, geçici ve kesin önlem türü-süresi, yürürlükteki önlemler, CK önerisi; soruşturmayı Genel Müdürlük yürütür.",
        kok=[
            "İthalatta Korunma Önlemleri Hakkında Karar ve Yönetmeliğe göre aşağıdakilerden hangisi İthalatta Korunma Önlemlerini Değerlendirme Kurulunun görevleri arasında yer almaz?"
        ],
        d="Soruşturmayı yürütmek ve dokuz ay içinde tamamlamak",
        c=[
            "Soruşturma başlatılıp başlatılmamasına karar vermek",
            "Soruşturma süresi içinde başvurunun geri çekilmesi durumunda soruşturmanın sürdürülmesine veya sonuçlandırılmasına karar vermek",
            "Geçici korunma önlemi alınıp alınmamasına, alınırsa önlemin türüne, büyüklüğüne ve süresine karar vermek",
            "Yürürlükteki korunma önlemlerine ilişkin karar almak",
        ],
        g="İthalatta Korunma Önlemleri Hakkında Karara göre Kurulun görevleri; soruşturma başlatılıp başlatılmamasına karar vermek, soruşturma süresi içinde başvurunun geri çekilmesi halinde soruşturmanın sürdürülmesine veya sonuçlandırılmasına karar vermek, geçici korunma önlemi ve korunma önlemi alınıp alınmamasına, önlemin türüne, büyüklüğüne ve süresine karar vermek, yürürlükteki önlemlere ilişkin karar almak ve Cumhurbaşkanı kararı çıkarılması için öneride bulunmaktır. Kurul, Genel Müdürlüğün teklifi üzerine karar alır ve sekretaryası Genel Müdürlükçe yürütülür. Yönetmeliğe göre soruşturma ise Genel Müdürlükçe yürütülerek dokuz ay içinde tamamlanır; gerekli hallerde altı ay uzatılabilir. Soruşturmayı yürütmek bu nedenle Kurulun değil Genel Müdürlüğün görevidir. En güçlü tuzak başvurunun geri çekilmesi halidir: ön inceleme aşamasında işlemlere Genel Müdürlük son verebildiği için soruşturma aşamasında da karar Genel Müdürlüğe aitmiş gibi görünür. Bu nedenle doğru cevap 'Soruşturmayı yürütmek ve dokuz ay içinde tamamlamak' seçeneğidir. (MD Korunma Kararı md. 4; Korunma Yönetmeliği md. 3, 4)",
        kanit=f"{K} | a) Soruşturma başlatılıp başlatılmamasına karar vermek, || {K} | Soruşturma süresi içerisinde başvurunun geri çekilmesi durumunda soruşturmanın sürdürülmesine veya sonuçlandırılmasına karar vermek, || {K} | Geçici korunma önlemi alınıp alınmamasına, önlem alınması halinde önlemin türüne, büyüklüğüne ve süresine karar || {K} | e) Yürürlükteki korunma önlemlerine ilişkin karar almak, || {K} | SORUŞTURMA, Genel Müdürlükçe yürütülerek DOKUZ (9) AY içinde tamamlanır. || {K} | Ön inceleme aşamasında başvurunun geri çekilmesi halinde, Genel Müdürlükçe işlemlere son verilebilir.",
        yuva=[
            "Korunma Kararı Kurul görevleri: soruşturma başlatma (listede)",
            "Aynı liste: başvurunun geri çekilmesinde karar (listede)",
            "Aynı liste: geçici korunma önlemi (listede)",
            "Aynı liste: yürürlükteki önlemler (listede)",
        ],
        yakinlik="BİREBİR",
        tuzak=["MAKAM", "LİSTE-DIŞI"],
        duzey=["AYIRT"],
        profil=[3],
        olumsuz=True,
    ),
    # 7 ---------------- Tanımdan ad: tarife kontenjanı ----------------
    s(
        kalip="TANIM",
        z="K",
        madde="İthalatta Kota ve Tarife Kontenjanı İdaresi Hakkında Karar (2010/339) md. 2",
        cek="Tarife kontenjanı: belirli dönemde gümrük vergisinde ve/veya mali yüklerde indirim ya da muafiyet sağlanan ithalatın miktar veya değeri; kota: izin verilen ithalat.",
        kok=[
            "İthalatta Kota ve Tarife Kontenjanı İdaresi Hakkında Karara göre, “belirli bir dönem itibarıyla gümrük vergisinde ve/veya diğer mali yüklerde indirim yapılan ya da muafiyet sağlanan ithalatın miktar veya değeri” aşağıdakilerden hangisidir?"
        ],
        d="Tarife kontenjanı",
        c=[
            "Kota",
            "Gözetim belgesi",
            "Ek mali mükellefiyet",
            "Miktar/değer kısıtlaması",
        ],
        g="İthalatta Kota ve Tarife Kontenjanı İdaresi Hakkında Karar iki kavramı ayırır: kota, belirli bir dönem itibarıyla yapılmasına izin verilen ithalatın miktar ve/veya değeridir; tarife kontenjanı (tarife kotası) ise belirli bir dönem itibarıyla gümrük vergisinde ve/veya diğer mali yüklerde indirim yapılan ya da muafiyet sağlanan ithalatın miktar veya değeridir. Kotada sınır ithalatın kendisine, tarife kontenjanında sınır indirimli veya muaf ithalata konur. Gözetim belgesi gözetime tabi malların ithali için verilen belgedir; ek mali mükellefiyet getirilmesi ve miktar/değer kısıtlaması ise Korunma Önlemleri Kararında sayılan geçici korunma önlemi biçimleridir. Kota ve tarife kontenjanı belgelerinde tahrifat veya devir gibi aykırılıklar halinde tahsis iptal edilir ve firmaya beş yıl süreyle o tebliğ çerçevesinde tahsis yapılmaz. En güçlü tuzak kotadır: tanımdaki “belirli bir dönem” ve “miktar veya değer” unsurları kota tanımında da vardır; ayırıcı unsur vergi indirimi veya muafiyetidir. Bu nedenle doğru cevap 'Tarife kontenjanı' seçeneğidir. (MD Kota ve Tarife Kontenjanı Kararı md. 2, 6)",
        kanit=f"{K} | Belirli bir dönem itibarıyla gümrük vergisinde ve/veya diğer mali yüklerde indirim yapılan ya da muafiyet sağlanan ithalatın miktar veya değerini, ifade eder. || {K} | KOTA: Belirli bir dönem itibarıyla yapılmasına izin verilen ithalatın miktar ve/veya değerini, || {K} | GÖZETİM BELGESİ: Gözetime tabi malların ithali için Genel Müdürlükçe verilen veya onaylanan belge. || {K} | Kendilerine 5 YIL SÜREYLE söz konusu tebliğ çerçevesinde KOTA VE TARIFE KONTENJANI TAHSIS EDILMEZ.",
        yuva=[
            "Kota tanımı (izin verilen ithalat)",
            "Gözetim Kararı: gözetim belgesi tanımı",
            "Geçici korunma önlemi biçimi: ek mali mükellefiyet",
            "Geçici korunma önlemi biçimi: miktar/değer kısıtlaması",
        ],
        yakinlik="BİREBİR",
        tuzak=["TERİM", "KOMŞU"],
        duzey=["TANIMA"],
        profil=[1],
        olumsuz=False,
        eksen=2,
        ayna="kota ↔ tarife kontenjanı",
    ),
    # 8 ---------------- Ticari Hakların Korunması Kararı (olumsuz) ----------------
    s(
        kalip="YANLIŞ",
        z="O",
        madde="Türkiye'nin Ticari Haklarının Korunması Hakkında Karar md. 5, 6; Yönetmelik md. 6, 12",
        cek="Ticari önlemler: tavizlerin askıya alınması/geri çekilmesi, miktar kısıtlaması ve diğer önlemler; haksız rekabet, korunma, gözetim, kota olaylarına uygulanmaz; ön inceleme 45 gün.",
        kok=[
            "Türkiye'nin Ticari Haklarının Korunması Hakkında Karar ve uygulama Yönetmeliğine göre ticari engellere karşı izlenecek usul ve alınabilecek önlemler hakkında aşağıdakilerden hangisi yanlıştır?"
        ],
        d="Karar kapsamında alınabilecek ticari önlemler arasında dampinge karşı vergi ve telafi edici vergi de sayılmıştır.",
        c=[
            "Karar, ithalatta haksız rekabetin önlenmesi ile gözetim ve korunma önlemleri mevzuatı kapsamında yer alan olaylara uygulanmaz.",
            "Ticari müzakereler çerçevesinde verilen tavizlerin askıya alınması veya geri çekilmesi, Kararda sayılan ticari önlemlerdendir.",
            "Yeterli delil görülmesi halinde ön inceleme 45 gün içinde tamamlanarak inceleme başlatılıp başlatılmayacağına ilişkin Genel Müdürlük önerisi Kurula sunulur.",
            "Genel Müdürlük, inceleme başlatıldığına dair tebliğin Resmî Gazete'de yayımlanmasından itibaren 5 ay içinde raporunu Kurula sunar; bu süre 7 aya kadar uzatılabilir.",
        ],
        g="Türkiye'nin Ticari Haklarının Korunması Hakkında Karar, Türkiye pazarını etkileyen ticari engellere ve diğer ülke pazarlarındaki ticari engellerin olumsuz ticari etkilerine karşılık vermek için alınabilecek ticari önlemleri ve Türkiye'nin Ticari Haklarını Değerlendirme Kurulunu düzenler. Karar kapsamında alınabilecek ticari önlemler iki gruptur: ticari müzakereler çerçevesinde verilen tavizlerin askıya alınması veya geri çekilmesi ile ilgili ülkelere yönelik miktar kısıtlamaları, ithalat veya ihracat koşullarını değiştiren ya da ticareti etkileyen diğer önlemler. Dampinge karşı vergi ve telafi edici vergi bu sayımda yoktur; Karar, ithalatta haksız rekabetin önlenmesi, gözetim ve korunma önlemleri, kota ve tarife kontenjanı ile tekstil mevzuatı kapsamındaki olaylara zaten uygulanmaz. Yönetmeliğe göre ön inceleme 45 gün içinde tamamlanır; inceleme raporu tebliğin Resmî Gazete'de yayımlanmasından itibaren 5 ay içinde Kurula sunulur ve süre 7 aya kadar uzatılabilir. En güçlü tuzak uygulama alanına ilişkin ifadedir: Karar ticaret politikası araçlarından biri olduğu için diğer önlem mevzuatını da kapsadığı sanılır. Bu nedenle doğru cevap 'Karar kapsamında alınabilecek ticari önlemler arasında dampinge karşı vergi ve telafi edici vergi de sayılmıştır.' seçeneğidir. (MD Ticari Haklar Kararı md. 5, 6; Yönetmelik md. 6, 12)",
        kanit=f"{K} | Ticari müzakereler çerçevesinde verilen TAVİZLERİN ASKIYA ALINMASI veya GERİ ÇEKİLMESİ, || {K} | İlgili ülke veya ülkelere yönelik olarak MİKTAR KISITLAMALARININ, İTHALAT veya İHRACAT KOŞULLARINI || {K} | BU KARAR, İthalatta Haksız Rekabetin Önlenmesi, İthalatta Gözetim ve Korunma Önlemleri ile Kota İdaresi ve Tarife || {K} | alan OLAYLARA UYGULANMAZ. || {K} | 45 (KIRKBEŞ) GÜN içinde ön || {K} | inceleme başlatıldığına dair tebliğin Resmi Gazete'de yayımlanmasından itibaren 5 (BEŞ) AY içinde incelemeye ilişkin || {K} | Kurul tarafından 7 (YEDİ) AYA kadar UZATILABİLİR.",
        yuva=[
            "Ticari Haklar Kararı: uygulama alanı dışı olaylar (doğru)",
            "Ticari Haklar Kararı: tavizlerin askıya alınması (doğru)",
            "Ticari Haklar Yönetmeliği: 45 günlük ön inceleme (doğru)",
            "Ticari Haklar Yönetmeliği: 5 ay, 7 aya kadar uzatma (doğru)",
        ],
        yakinlik="BİREBİR",
        tuzak=["LİSTE-DIŞI", "KOMŞU"],
        duzey=["AYIRT"],
        profil=[3],
        olumsuz=True,
    ),
]
