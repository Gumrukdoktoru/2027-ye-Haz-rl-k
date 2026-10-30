# GM Soru Bankası — M59: Türk Parası Kıymetini Koruma Mevzuatı (1567 sayılı Kanun, 32 sayılı Karar, Tebliğler, İthalat ve Nakit Kontrolleri Genelgeleri) (16 soru)
# Gümrük Koçu - Ufuk Çetintaş
K = "59-tpkk-doviz-nakit.txt"
KAN = "1567 sayılı Türk Parası Kıymetini Koruma Hakkında Kanun"
KAR = "Türk Parası Kıymetini Koruma Hakkında 32 sayılı Karar"
TEB = "Türk Parası Kıymetini Koruma Hakkında 32 sayılı Karara İlişkin Tebliğ (Tebliğ No: 2008-32-34)"
TEB48 = (
    "32 sayılı Karara İlişkin İhracat Bedelleri Hakkında Tebliğ (Tebliğ No: 2018-32-48)"
)
NKG = "1567 sayılı Kanun ve 5549 sayılı Kanun çerçevesinde gümrük giriş-çıkış noktalarında uygulanan Nakit Kontrolleri Genelgesine (2024/1)"


def s(**k):
    base = dict(
        konu="Türk Parası Kıymetini Koruma Mevzuatı",
        blok="M59",
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
    # 1 ---------------- 1567 sayılı Kanun: idari para cezası (olumsuz; makam) ----------------
    s(
        kalip="YANLIŞ",
        z="O",
        madde="1567 sayılı Kanun md. 3",
        cek="Süresinde getirilmeyen alacak: rayiç bedelin %5'i; yabancı parada TCMB döviz satış kuru; tüzel kişiye aynı ceza; 5 yılda tekerrür iki kat; karar mercii Cumhuriyet savcısı.",
        kok=[
            f"{KAN}un idari yaptırımlara ilişkin hükümlerine göre aşağıdakilerden hangisi yanlıştır?"
        ],
        d="Kanunda öngörülen idari para cezalarına karar vermeye, kıymetin yurttan çıkarıldığı yerdeki gümrük idaresi yetkilidir.",
        c=[
            "Alacaklarını kararlarda tayin edilen süreler içinde yurda getirmeyenlere, yurda getirmekle yükümlü oldukları kıymetlerin rayiç bedelinin yüzde beşi kadar idari para cezası verilir.",
            "Kabahatin konusunu yabancı para oluşturuyorsa, idari para cezasının hesaplanmasında fiilin işlendiği tarihteki Türkiye Cumhuriyet Merkez Bankası döviz satış kuru esas alınır.",
            "Kabahatin bir tüzel kişinin yararına işlenmesi halinde, ilgili tüzel kişiye de aynı miktarda idari para cezası verilir.",
            "Kabahatlerin, aynı kabahate ilişkin idari yaptırım kararının kesinleştiği tarihi izleyen beş yıl içinde tekerrürü halinde cezalar iki kat uygulanır.",
        ],
        g="1567 sayılı Kanuna göre alacaklarını kararlarda tayin edilen süreler içinde yurda getirmeyenler, yurda getirmekle yükümlü oldukları kıymetlerin rayiç bedelinin yüzde beşi kadar idari para cezasıyla cezalandırılır; karar kesinleşinceye kadar alacağını getirenlere 3.000–25.000 Türk lirası arası ceza verilir, ancak bu ceza getirilmesi gereken paranın yüzde iki buçuğunu aşamaz. Kabahat bir tüzel kişinin yararına işlenmişse tüzel kişiye de aynı miktarda ceza verilir; kabahatin konusu yabancı para ise fiil tarihindeki Merkez Bankası döviz satış kuru esas alınır; aynı kabahate ilişkin kararın kesinleştiği tarihi izleyen beş yıl içinde tekerrürde cezalar iki kat uygulanır. Bu idari para cezalarına karar vermeye ise gümrük idaresi değil Cumhuriyet savcısı yetkilidir; Nakit Kontrolleri Genelgesi de gümrük idaresinin bu hallerde konuyu Cumhuriyet Savcılığına bildirmesini öngörür. En güçlü tuzak döviz kuruna ilişkin ifadedir: 32 sayılı Kararda mahsup işlemlerinde döviz alış kuru uygulandığı için cezada da alış kurunun esas alındığı sanılabilir. Bu nedenle doğru cevap 'Kanunda öngörülen idari para cezalarına karar vermeye, kıymetin yurttan çıkarıldığı yerdeki gümrük idaresi yetkilidir.' seçeneğidir. (MD 1567 sayılı Kanun md. 3)",
        kanit=f"{K} | Bu madde hükmüne göre idarî para cezasına karar vermeye CUMHURİYET SAVCISI YETKİLİDİR. || {K} | Yurda getirmekle yükümlü oldukları kıymetlerin RAYİÇ BEDELİNİN YÜZDE BEŞİ (%5) kadar idarî para || {K} | fiilin işlendiği tarih itibarıyla TÜRKİYE CUMHURİYET MERKEZ BANKASININ bu paraya ilişkin || {K} | İlgili tüzel kişiye de AYNI MİKTARDA idarî para cezası verilir. || {K} | YIL İÇİNDE TEKERRÜRÜ HALİNDE verilecek cezalar İKİ (2) KAT olarak uygulanır. || {K} | İşlem tarihindeki DÖVİZ ALIŞ KURLARI uygulanır. || {K} | uyarınca konu Cumhuriyet Savcılığına bildirilir ve alınacak talimata göre hareket edilir.",
        yuva=[
            "1567 sayılı Kanun: süresinde getirilmeyen alacakta %5 ceza (doğru)",
            "1567 sayılı Kanun: yabancı parada döviz satış kuru (doğru)",
            "1567 sayılı Kanun: tüzel kişiye aynı miktar ceza (doğru)",
            "1567 sayılı Kanun: beş yıl içinde tekerrürde iki kat (doğru)",
        ],
        yakinlik="BİREBİR",
        tuzak=["MAKAM", "KOMŞU"],
        duzey=["AYIRT"],
        profil=[3],
        olumsuz=True,
    ),
    # 2 ---------------- 1567 sayılı Kanun: genel hükümler (önermeli) ----------------
    s(
        kalip="ÖNERMELİ",
        z="O",
        madde="1567 sayılı Kanun md. 1, 2, 4, Ek md. 1, Ek md. 3",
        cek="Kararlara Cumhurbaşkanı yetkili; yürürlük tarihi yoksa yayımın ertesi günü; ihbar ikramiyesi %45'i geçemez; ticari döviz alım satımı HMB iznine tabi; denetim çok merciili.",
        kok=[
            f"{KAN} hakkında;",
            "I. Türk parasının kıymetinin korunması amacıyla kararlar almaya Cumhurbaşkanı yetkilidir.",
            "II. Kanun uyarınca alınan kararlar, metinlerinde yürürlük tarihi yoksa Resmî Gazete'de yayımlandıkları gün yürürlüğe girer.",
            "III. Kanuna aykırı fiilleri ihbar edenlere verilecek ikramiyenin miktarı, hükmolunacak para cezalarından tahsil edilecek miktarın yüzde kırk beşini geçemez.",
            "IV. Ticari amaçla döviz alım satımında bulunmak için Hazine ve Maliye Bakanlığından izin alınması zorunludur.",
            "V. Kanun hükümlerine aykırı hareket edenler hakkında tetkikat ve tahkikat yapmaya yalnızca kambiyo murakabe mercileri yetkilidir.",
            "ifadelerinden hangileri doğrudur?",
        ],
        d="I, III ve IV",
        c=["I ve III", "II, IV ve V", "I, II, III ve IV", "I, III, IV ve V"],
        sirali=True,
        siklar=[
            "I ve III",
            "I, III ve IV",
            "II, IV ve V",
            "I, II, III ve IV",
            "I, III, IV ve V",
        ],
        g="1567 sayılı Kanuna göre kambiyo, kıymetli maden ve taşlar ile ödemeyi sağlayan vasıtaların ithal ve ihracının düzenlenmesine ve Türk parasının kıymetinin korunması amacıyla kararlar almaya Cumhurbaşkanı yetkilidir (I doğru). Kararlar Resmî Gazete'de yayımlanır; metinlerinde yürürlük tarihi varsa o tarihte, yoksa yayımlandığı günün ertesi gününden itibaren yürürlüğe girer (II yanlış). Kanuna aykırı fiilleri ihbar edenlere verilecek ikramiye Cumhurbaşkanı kararıyla belirlenir ve tahsil edilecek para cezalarının yüzde kırk beşini geçemez (III doğru). Ticari amaçla döviz alım satımı, Borsa İstanbul Kıymetli Madenler Piyasasında üye olarak faaliyet, kıymetli maden rafinajı ve Kimberley Süreci kapsamındaki faaliyetler Hazine ve Maliye Bakanlığı iznine tabidir (IV doğru). Tetkikat ve tahkikat yetkisi yalnız kambiyo murakabe mercilerine değil, vergi müfettişleri ve yardımcılarına, hazine kontrolörleri ve stajyer hazine kontrolörlerine de verilmiştir (V yanlış). En güçlü tuzak II. önermedir: yürürlük kuralında yayım günü ile ertesi gün ayrımı gözden kaçabilir. Bu nedenle doğru cevap 'I, III ve IV' seçeneğidir. (MD 1567 sayılı Kanun md. 1, 2, 4, Ek md. 1, Ek md. 3)",
        kanit=f"{K} | Türk Parasının kıymetinin korunması zımnında kararlar ittihazına || {K} | RESMİ GAZETE İLE NEŞREDİLDİĞİNİN ERTESİ GÜNÜNDEN İTİBAREN || {K} | edilecek miktarın YÜZDE KIRKBEŞİNİ (%45) ini GEÇEMEZ. || {K} | a) Ticari amaçla döviz alım satımında bulunmak. || {K} | Hazine ve Maliye Bakanlığından İZİN ALINMASI ZORUNLUDUR || {K} | VERGİ MÜFETTİŞLERİ ve Vergi MÜFETTİŞ YARDIMCILARI, HAZİNE KONTROLÖRLERİ ve STAJYER HAZİNE || {K} | KONTROLÖRLERİ ve KAMBİYO MURAKABE MERCİLERİ bu kanun hükümlerine aykırı hareket edenler hakkında",
        yuva=[
            "I ve III: izin hükmünü bilmeyen aday (eksik seçim)",
            "II, IV ve V: yürürlük ve denetim kurallarını yanlış bilen aday",
            "I, II, III ve IV: yürürlüğü yayım günü sanan aday",
            "I, III, IV ve V: 'yalnızca' sınırlamasını fark etmeyen aday",
        ],
        yakinlik="PARAFRAZ",
        tuzak=["BAŞLANGIÇ", "MUTLAK"],
        duzey=["AYIRT", "BÜTÜNLEŞİK"],
        profil=[2, 3],
        olumsuz=False,
    ),
    # 3 ---------------- Tanımdan ad: çekili kıymetli maden ----------------
    s(
        kalip="TANIM",
        z="K",
        madde="32 sayılı Karar md. 2",
        cek="Çekili kıymetli maden: çekilip ince şerit haline getirilen veya şeridin çeşitli şekil ve ağırlıklarda kesilmesiyle oluşan, herhangi bir saflık ayarındaki kıymetli maden.",
        kok=[
            f"{KAR}a göre, “kıymetli madenin çekilip ince bir şerit haline getirilerek veya şeridin çeşitli şekil ve ağırlıklarda kesilmesi suretiyle oluşturulan, herhangi bir saflık ayarını haiz kıymetli madenler” aşağıdakilerden hangisidir?"
        ],
        d="Çekili kıymetli maden",
        c=[
            "Basılı kıymetli maden",
            "Standart dışı işlenmemiş kıymetli maden",
            "İşlenmiş kıymetli maden",
            "Darphane üretimi kıymetli maden",
        ],
        g="32 sayılı Kararın tanımlar maddesi kıymetli madenleri biçimine göre ayırır. Çekili kıymetli maden, kıymetli madenin çekilip ince bir şerit haline getirilmesiyle veya şeridin çeşitli şekil ve ağırlıklarda kesilmesiyle oluşturulan, herhangi bir saflık ayarını haiz kıymetli madendir; Ticaret Bakanlığınca yetkilendirilmiş kuyum işletmeleri ve vergi levhasında kıymetli maden üretimi veya ticareti yazılı gerçek kişiler dışındaki Türkiye'de yerleşik gerçek kişilere satışı yapılamaz. Basılı kıymetli maden, erimiş madenin kalıba dökülüp el veya pres ile işaretlenmesi ya da düz şeritten çıkarılan parçaların darp yöntemiyle işaretlenmesiyle Bakanlıkça belirlenen şekil, ağırlık ve saflıkta üretilir. Standart dışı işlenmemiş kıymetli maden, standart saflığın altındaki külçe, bar, dore bar, granül, toz veya hurdadır; işlenmiş kıymetli maden işçilik uygulanarak ziynet veya süs eşyasına dönüştürülmüş madendir; Darphane üretimi kıymetli madenler ise Cumhuriyet altın sikkeleri, ziynet altınları ve Darphanenin ürettiği diğer kıymetli madenlerdir. En güçlü tuzak basılı kıymetli madendir: onun tanımında da kıymetli maden şeridi geçer, ancak ayırıcı unsur darp yöntemiyle işaretleme ve belirli saflıktır. Bu nedenle doğru cevap 'Çekili kıymetli maden' seçeneğidir. (MD 32 sayılı Karar md. 2)",
        kanit=f"{K} | ÇEKİLİ KIYMETLİ MADEN: Kıymetli madenin çekilip ince bir şerit haline getirilerek veya şeridin çeşitli şekil ve || {K} | ağırlıklarda kesilmesi suretiyle oluşturulan herhangi bir saflık ayarını haiz kıymetli madenleri, || {K} | düz bir kıymetli maden şeridinden belirli boyutlarda çıkarılan kıymetli || {K} | maden şeritlerinin darp yöntemiyle işaretlenmesi yoluyla || {K} | İŞLENMİŞ ALTIN: İşçilik uygulanarak ziynet veya süs eşyası haline dönüştürülmüş altını, || {K} | Darphane tarafından basılan Cumhuriyet altın sikkeleri ile Cumhuriyet || {K} | kişilere ÇEKİLİ KIYMETLİ MADENLERİN SATIŞI YAPILAMAZ.",
        yuva=[
            "Komşu tanım: basılı kıymetli maden (şerit + darp)",
            "Komşu tanım: standart dışı işlenmemiş (saflık eşiği altı)",
            "Komşu tanım: işlenmiş (ziynet/süs eşyası)",
            "Komşu tanım: Darphane üretimi (sikke, ziynet altını)",
        ],
        yakinlik="BİREBİR",
        tuzak=["TERİM", "KOMŞU"],
        duzey=["TANIMA"],
        profil=[1],
        olumsuz=False,
        ayna="çekili kıymetli maden ↔ basılı kıymetli maden",
        cikmis="2024/37",
    ),
    # 4 ---------------- 32 sayılı Karar: Türk parası ve döviz giriş-çıkışı (olumsuz) ----------------
    s(
        kalip="YANLIŞ",
        z="O",
        madde="32 sayılı Karar md. 3, 4",
        cek="TL, TL ile ödeme belgeleri ve döviz giriş-çıkışı serbest; 185.000 TL ve 10.000 Avro üstü çıkış Bakanlık esasıyla; dışarıda yerleşiklerin TL tevdiatı serbest.",
        kok=[
            f"{KAR}a göre Türk parası ve dövizin yurda girişi ile yurttan çıkışına ilişkin aşağıdaki ifadelerden hangisi yanlıştır?"
        ],
        d="Dışarıda yerleşik kişilerin Türkiye'de Türk parası ile ödeme, tahsilat ve tevdiatta bulunmaları Hazine ve Maliye Bakanlığının iznine bağlıdır.",
        c=[
            "Türk parası ve Türk parasıyla ödemeyi sağlayan belgelerin yurttan ihracı ve yurda ithali serbesttir.",
            "185.000 Türk lirasını aşan Türk parasının yurt dışına çıkarılması Bakanlıkça belirlenecek esaslar dahilinde yapılır.",
            "Yurda döviz ithali ve yurttan döviz ihracı serbesttir.",
            "10.000 Avro veya eşitini aşan efektifin yurt dışına çıkarılması Bakanlıkça belirlenecek esaslar dahilinde yapılır.",
        ],
        g="32 sayılı Kararın Türk parasına ilişkin maddesine göre Türk parası ve Türk parasıyla ödemeyi sağlayan belgelerin yurttan ihracı ve yurda ithali serbesttir; dışarıda yerleşik kişilerin Türkiye'de Türk parası ile ödeme, tahsilat ve tevdiatta bulunmaları da serbesttir, yani Bakanlık iznine bağlı değildir. 185.000 Türk lirasını aşan Türk parasının yurt dışına çıkarılması Bakanlıkça belirlenecek esaslar dahilinde yapılır. Dövize ilişkin maddeye göre yurda döviz ithali ve yurttan döviz ihracı serbesttir; 10.000 Avro veya eşitini aşan efektifin çıkarılması Bakanlıkça belirlenecek esaslara bağlıdır. Bu sınırların üstündeki yolcu beraberi çıkışlarda gümrük idaresine Nakit Beyan Formu ile beyanda bulunulur. En güçlü tuzak Türk parası tutarına ilişkin ifadedir: kaynaktaki Nakit Kontrolleri Genelgesi metninde Türk parası için 25.000 Türk lirası sınırı geçtiğinden tutar yanlış sanılabilir; Kararın 15.03.2025 tarihli değişikliğiyle sınır 185.000 Türk lirasıdır. Bu nedenle doğru cevap 'Dışarıda yerleşik kişilerin Türkiye'de Türk parası ile ödeme, tahsilat ve tevdiatta bulunmaları Hazine ve Maliye Bakanlığının iznine bağlıdır.' seçeneğidir. (MD 32 sayılı Karar md. 3, 4)",
        kanit=f"{K} | TÜRK PARASI ve Türk parasıyla ödemeyi sağlayan belgelerin yurttan ihracı ve yurda ithali SERBESTTİR, || {K} | Dışarıda yerleşik kişilerin Türkiye'de Türk parası ile ödeme, tahsilat ve tevdiatta bulunmaları SERBESTTİR. || {K} | TÜRK PARASININ yurt dışına çıkarılması Bakanlıkça belirlenecek esaslar dahilinde yapılır. || {K} | Yurda DÖVİZ ithali ve yurttan döviz ihracı SERBESTTİR. || {K} | 10.000 AVRO veya EŞİTİNİ aşan efektifin yurt dışına çıkarılması Bakanlıkça belirlenecek esaslar dahilinde yapılır. || {K} | Bunun dışında kalan TÜRK PARASI ve Türk parası ile ödemeyi sağlayan belgelerde 25.000 TÜRK LİRASI,",
        yuva=[
            "32 sayılı Karar: Türk parası giriş-çıkışı serbest (doğru)",
            "32 sayılı Karar: 185.000 TL sınırı (doğru; Genelgedeki eski tutarla karışma)",
            "32 sayılı Karar: döviz giriş-çıkışı serbest (doğru)",
            "32 sayılı Karar: 10.000 Avro efektif sınırı (doğru)",
        ],
        yakinlik="BİREBİR",
        tuzak=["TERSİNE", "YAKIN-SAYI"],
        duzey=["AYIRT"],
        profil=[3],
        olumsuz=True,
        cikmis="2022/19",
    ),
    # 5 ---------------- Sermaye ihracı: banka ve gümrük idaresinin bildirimi ----------------
    s(
        kalip="SÜRE",
        z="O",
        madde="32 sayılı Karar md. 13; 2008-32-34 sayılı Tebliğ md. 10",
        cek="Bankalar ve gümrük idareleri sermaye ihraç edenleri her işlemden itibaren 30 gün içinde HMB ve Ticaret Bakanlığına bildirir; kişinin kendi bilgi formu üç ay.",
        kok=[
            f"{KAR}a göre bankalar ve gümrük idareleri, yurt dışında yatırım veya ticari faaliyette bulunmak üzere sermaye ihraç eden Türkiye'de yerleşik kişileri hangi süre içinde ve hangi kurumlara bildirir?"
        ],
        d="Her bir işlem tarihinden itibaren 30 gün içinde Hazine ve Maliye Bakanlığı ile Ticaret Bakanlığına",
        c=[
            "Her bir işlem tarihinden itibaren 30 gün içinde yalnız Türkiye Cumhuriyet Merkez Bankasına",
            "İlk sermaye ihracını müteakip üç ay içinde Hazine ve Maliye Bakanlığı ile Ticaret Bakanlığına",
            "Her takvim yılını müteakip üç ay içinde yalnız Ticaret Bakanlığına",
            "Her bir işlem tarihinden itibaren 10 gün içinde Hazine ve Maliye Bakanlığı Kamu Finansmanı Genel Müdürlüğüne",
        ],
        g="32 sayılı Karara göre Türkiye'de yerleşik kişilerin yurt dışında şirket kurmaları, ortaklığa katılmaları ve şube açmaları için nakdi sermayeyi bankalar aracılığıyla, ayni sermayeyi gümrük mevzuatı hükümleri çerçevesinde ihraç etmeleri serbesttir. Bankalar ve gümrük idareleri sermaye ihraç eden bu kişileri her bir işlem tarihinden itibaren 30 gün içinde Hazine ve Maliye Bakanlığı ile Ticaret Bakanlığına bildirir. Üç aylık süreler sermayeyi ihraç eden kişinin kendi yükümlülüğüdür: Tebliğe göre kişi ilk sermaye ihracını müteakip üç ay içinde bilgi formunu iki Bakanlığa gönderir, her takvim yılını müteakip üç ay içinde formu güncelleyerek Ticaret Bakanlığına gönderir. On günlük süre ise kamu kurum ve kuruluşlarının dış kredi kullanım ve geri ödeme bilgilerinin Kamu Finansmanı Genel Müdürlüğüne gönderilmesine aittir. En güçlü tuzak ilk sermaye ihracını müteakip üç aylık süredir: kurumlar doğrudur, ancak süre ve yükümlü farklıdır. Bu nedenle doğru cevap 'Her bir işlem tarihinden itibaren 30 gün içinde Hazine ve Maliye Bakanlığı ile Ticaret Bakanlığına' seçeneğidir. (MD 32 sayılı Karar md. 13; 2008-32-34 sayılı Tebliğ md. 10)",
        kanit=f"{K} | Bankalar ve gümrük idareleri yurt dışında yatırım veya ticari faaliyette bulunmak üzere SERMAYE İHRAÇ EDEN || {K} | her bir işlem tarihinden itibaren 30 GÜN içinde Hazine ve Maliye Bakanlığı ve Ticaret || {K} | AYNİ SERMAYEYİ ise gümrük mevzuatı hükümleri çerçevesinde İHRAÇ ETMELERİ SERBESTTİR. || {K} | yaptıkları ilk nakdi ve/veya ayni sermaye ihracını müteakip ÜÇ (3) AY İÇİNDE || {K} | HER TAKVİM YILINI MÜTEAKİP ÜÇ (3) AY İÇİNDE || {K} | gerçekleşme tarihinden itibaren 10 gün içinde bankalar ile kredi borçlusu",
        yuva=[
            "Süre doğru, kurum yanlış (Merkez Bankası)",
            "Tebliğ: kişinin ilk bildirim formu (üç ay)",
            "Tebliğ: yıllık güncelleme (üç ay, Ticaret Bakanlığı)",
            "Tebliğ: kamu kredilerinde 10 günlük bildirim",
        ],
        yakinlik="BİREBİR",
        tuzak=["BAŞLANGIÇ", "MAKAM", "KOMŞU"],
        duzey=["HATIRLAMA", "AYIRT"],
        profil=[1, 3],
        olumsuz=False,
        baslangic=True,
    ),
    # 6 ---------------- Yurt dışından kredi temini (olumsuz) ----------------
    s(
        kalip="YANLIŞ",
        z="O",
        madde="32 sayılı Karar md. 17",
        cek="Yurt dışından TL kredi serbest, bankalar aracılığıyla; gerçek kişiler döviz kredisi kullanamaz; dövize endeksli kredi yasak; 15 milyon dolar bakiyede döviz geliri şartı aranmaz.",
        kok=[
            f"{KAR}a göre Türkiye'de yerleşik kişilerin yurt dışından kredi temin etmesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?"
        ],
        d="Türkiye'de yerleşik gerçek kişiler, döviz gelirlerini tevsik etmek kaydıyla yurt dışından döviz kredisi kullanabilir.",
        c=[
            "Türkiye'de yerleşik kişilerin yurt dışından Türk lirası kredi temin etmeleri serbesttir; temin edilen kredilerin bankalar aracılığıyla kullanılması zorunludur.",
            "Türkiye'de yerleşik kişilerce yurt dışından dövize endeksli kredi kullanılamaz.",
            "Kullanım tarihinde kredi bakiyesi 15 milyon ABD doları veya üzerinde olan Türkiye'de yerleşik kişilerin kullanacakları döviz kredilerinde döviz geliri olması şartı aranmaz.",
            "Yurt dışından temin edilen kredilere ait anapara geri ödemeleri ile faiz ve diğer ödemelerin transferleri bankalar aracılığıyla yapılır.",
        ],
        g="32 sayılı Karara göre Türkiye'de yerleşik kişilerin yurt dışından Türk lirası kredi temin etmeleri serbesttir ve krediler bankalar aracılığıyla kullanılır. Döviz kredisinde kural, döviz geliri olmayanların kredi temin edememesidir; kullanım tarihinde kredi bakiyesi 15 milyon ABD doları veya üzerinde olanlar, kamu kurumları ve bankalar, teşvik belgeli yatırımcılar gibi sayılan hallerde bu şart aranmaz. Döviz geliri olan ve bakiyesi 15 milyon ABD dolarının altında olanlarda kullanılacak kredi ile mevcut bakiye toplamı son üç mali yılın döviz gelirleri toplamını aşamaz. Türkiye'de yerleşik gerçek kişiler ise döviz gelirleri olsa bile yurt dışından döviz kredisi kullanamaz; dövize endeksli kredi de kullanılamaz. Kredilere ait anapara, faiz ve diğer ödemelerin transferleri bankalar aracılığıyla yapılır. En güçlü tuzak 15 milyon ABD doları eşiğine ilişkin ifadedir: döviz geliri şartının bir istisnası olduğu için kuralın kendisi sanılabilir. Bu nedenle doğru cevap 'Türkiye'de yerleşik gerçek kişiler, döviz gelirlerini tevsik etmek kaydıyla yurt dışından döviz kredisi kullanabilir.' seçeneğidir. (MD 32 sayılı Karar md. 17)",
        kanit=f"{K} | Türkiye'de yerleşik GERÇEK KİŞİLERCE yurt dışından DÖVİZ KREDİSİ KULLANILAMAZ. || {K} | TÜRKİYE'DE YERLEŞİK KİŞİLERİN YURT DIŞINDAN TÜRK LİRASI KREDİ temin etmeleri SERBESTTİR. || {K} | Temin edilen kredilerin BANKALAR ARACILIĞIYLA KULLANILMASI ZORUNLUDUR. || {K} | Türkiye'de yerleşik kişilerce yurt dışından DÖVİZE ENDEKSLİ KREDİ KULLANILAMAZ. || {K} | Kullanım tarihinde kredi bakiyesi 15 milyon ABD doları veya üzerinde olan Türkiye'de yerleşik kişilerce || {K} | Yurt dışından temin edilen kredilere ait anapara geri ödemeleri ile faiz ve diğer ödemelerin transferleri bankalar || {K} | kullanılmak istenen kredi tutarı ile mevcut kredi bakiyesi toplamı son üç malî yılın döviz gelirleri toplamını",
        yuva=[
            "32 sayılı Karar: TL kredi serbest, bankalar aracılığıyla (doğru)",
            "32 sayılı Karar: dövize endeksli kredi yasağı (doğru)",
            "32 sayılı Karar: 15 milyon dolar istisnası (doğru)",
            "32 sayılı Karar: geri ödeme transferleri bankalarca (doğru)",
        ],
        yakinlik="BİREBİR",
        tuzak=["İSTİSNA", "ŞART"],
        duzey=["AYIRT"],
        profil=[3],
        olumsuz=True,
    ),
    # 7 ---------------- Döviz cinsinden sözleşme yasağı ve istisnaları (olumsuz) ----------------
    s(
        kalip="KAPSAM_DIŞI",
        z="Z",
        madde="2008-32-34 sayılı Tebliğ md. 8",
        cek="Yerleşikler arası yurt içi gayrimenkul satış ve kiralamada döviz bedel yasak; taşıt dışı menkul satışı, dövizli maliyetli eser, yazılım, gümrüksüz mağaza kirası istisna.",
        kok=[
            f"{TEB} hükümlerine göre, Türkiye'de yerleşik ve Türk vatandaşı olan kişilerin kendi aralarında akdettikleri aşağıdaki sözleşmelerden hangisinde sözleşme bedelinin döviz cinsinden veya dövize endeksli olarak kararlaştırılması mümkün değildir?"
        ],
        d="Konusu yurt içinde yer alan bir konut olan gayrimenkul kiralama sözleşmesi",
        c=[
            "Taşıt satış sözleşmeleri dışında kalan menkul satış sözleşmesi",
            "Döviz cinsinden maliyet içeren eser sözleşmesi",
            "Yurt dışında üretilen yazılımlara ilişkin satış sözleşmesi",
            "Gümrüksüz satış mağazasının kiralanmasına ilişkin gayrimenkul kiralama sözleşmesi",
        ],
        g="32 sayılı Karar Türkiye'de yerleşik kişilerin kendi aralarındaki sözleşmelerde bedelin döviz cinsinden veya dövize endeksli kararlaştırılmasını Bakanlıkça belirlenen haller dışında yasaklar; Tebliğ bu halleri sayar. Konusu yurt içindeki gayrimenkuller olan, konut ve çatılı iş yeri dâhil gayrimenkul satış ve kiralama sözleşmelerinde döviz bedel kararlaştırılamaz; bu yasağın istisnaları vatandaşlık bağı bulunmayan alıcı veya kiracılar, belgeli konaklama tesislerinin işletilmek üzere kiralanması ve gümrüksüz satış mağazalarının kiralanmasıdır. Taşıt satışı dışındaki menkul satış sözleşmeleri, döviz cinsinden maliyet içeren eser sözleşmeleri ve yurt dışında üretilen yazılımlara ilişkin satış sözleşmelerinde ise döviz bedel kararlaştırılabilir. Soruda taraflar Türk vatandaşı olduğundan ve konut kiralaması bu istisnalardan hiçbirine girmediğinden döviz bedel mümkün değildir. En güçlü tuzak gümrüksüz satış mağazası kirasıdır: gayrimenkul kiralaması olduğu için yasak kapsamında sanılır, oysa Tebliğde açıkça istisna edilmiştir. Bu nedenle doğru cevap 'Konusu yurt içinde yer alan bir konut olan gayrimenkul kiralama sözleşmesi' seçeneğidir. (MD 2008-32-34 sayılı Tebliğ md. 8)",
        kanit=f"{K} | çatılı iş yeri dâhil gayrimenkul kiralama sözleşmelerinde sözleşme bedelini || {K} | Gümrüksüz satış mağazalarının kiralanmasına ilişkin gayrimenkul kiralama sözleşmelerinde || {K} | TAŞIT SATIŞ SÖZLEŞMELERİ DIŞINDA kalan menkul satış || {K} | döviz cinsinden maliyet içeren eser sözleşmelerinde || {K} | yazılımlara ilişkin satış sözleşmeleri ile yurt dışında üretilen donanım || {K} | Kültür ve Turizm Bakanlığından belgeli konaklama tesislerinin işletilmesi amacıyla kiralanmasıyla ilgili gayrimenkul",
        yuva=[
            "Tebliğ istisnası: taşıt dışı menkul satışı",
            "Tebliğ istisnası: dövizli maliyetli eser sözleşmesi",
            "Tebliğ istisnası: yurt dışında üretilen yazılım satışı",
            "Tebliğ istisnası: gümrüksüz satış mağazası kirası (gayrimenkul kirası içinde)",
        ],
        yakinlik="PARAFRAZ",
        tuzak=["İSTİSNA", "LİSTE-DIŞI"],
        duzey=["AYIRT", "UYGULAMA"],
        profil=[3, 4],
        olumsuz=True,
    ),
    # 8 ---------------- İşlenmemiş kıymetli maden: Borsaya teslim ve bilgi (olumsuz) ----------------
    s(
        kalip="YANLIŞ",
        z="Z",
        madde="32 sayılı Karar md. 7",
        cek="Aracı kuruluş ithal ettiği işlenmemiş madeni 3 iş gününde Borsaya teslim eder; DİR'de teslim yok, 3 iş gününde bilgi; antrepo ve serbest bölgede de bilgi.",
        kok=[
            f"{KAR}a göre standart ve standart dışı işlenmemiş kıymetli madenlerin ithali ile Borsa İstanbul A.Ş.'ye teslim ve bilgi verme yükümlülüklerine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?"
        ],
        d="Kıymetli madenler aracı kuruluşlarınca Dahilde İşleme Rejimi kapsamında ithal edilen işlenmemiş kıymetli madenlerin üç iş günü içinde Borsa İstanbul A.Ş.'ye teslimi zorunludur.",
        c=[
            "Kıymetli madenler aracı kuruluşları, ithal ettikleri standart ve standart dışı işlenmemiş kıymetli madenleri kural olarak üç iş günü içinde Borsa İstanbul A.Ş.'ye teslim etmek zorundadır.",
            "İşlenmemiş kıymetli madenlerin gümrük antrepolarına konulmasında, kıymetli madenler aracı kuruluşunca üç iş günü içinde Borsaya yazılı olarak bilgi verilmesi zorunludur.",
            "İşlenmemiş kıymetli madenleri yurt dışından serbest bölgeye getirenler tarafından üç iş günü içinde Borsaya yazılı olarak bilgi verilmesi zorunludur.",
            "Standart ve standart dışı işlenmemiş kıymetli madenlerin ithal ve ihracında gümrük idarelerine beyan verilmesi yeterli olup ithalat ve ihracat rejim, karar ve yönetmelikleri uygulanmaz.",
        ],
        g="32 sayılı Karara göre standart ve standart dışı işlenmemiş kıymetli madenlerin ithal ve ihracında gümrük idarelerine beyan verilmesi yeterlidir; ithalat ve ihracat rejim, karar ve yönetmelikleri uygulanmaz. İthali, Dahilde İşleme Rejimi kapsamındaki standart dışı ithalat gibi istisnalar dışında yalnızca Merkez Bankası ile kıymetli madenler aracı kuruluşlarınca yapılır ve aracı kuruluşlar ithal ettikleri bu madenleri üç iş günü içinde Borsa İstanbul A.Ş.'ye teslim etmek zorundadır. Aracı kuruluşlarca Dahilde İşleme Rejimi kapsamında yapılan işlenmemiş kıymetli maden ithalatında ise Borsaya teslim şartı yoktur; yalnızca üç iş günü içinde Borsaya yazılı bilgi verilir. Gümrük antrepolarına konulmada ve yurt dışından serbest bölgeye getirilmede de üç iş günü içinde Borsaya yazılı bilgi verilmesi zorunludur. En güçlü tuzak genel teslim kuralıdır: aynı üç iş günü süresi hem teslim hem bilgi yükümlülüğünde geçtiği için Dahilde İşleme Rejimi istisnası gözden kaçar. Bu nedenle doğru cevap 'Kıymetli madenler aracı kuruluşlarınca Dahilde İşleme Rejimi kapsamında ithal edilen işlenmemiş kıymetli madenlerin üç iş günü içinde Borsa İstanbul A.Ş.'ye teslimi zorunludur.' seçeneğidir. (MD 32 sayılı Karar md. 7)",
        kanit=f"{K} | ARACI KURULUŞLARI ithal ettikleri standart ve standart dışı işlenmemiş kıymetli || {K} | İthal edilen standart ve standart dışı İŞLENMEMİŞ kıymetli madenlerin Borsa İstanbul || {K} | TESLİM ŞARTI BULUNMAYIP, || {K} | ÜÇ (3) İŞ GÜNÜ içinde kıymetli madenler aracı kuruluşu tarafından Borsaya yazılı olarak bilgi verilmesi || {K} | Gümrük Antrepolarına konulmasında ÜÇ (3) İŞ GÜNÜ içinde kıymetli || {K} | madenler aracı kuruluşu tarafından BORSAYA YAZILI OLARAK BİLGİ VERİLMESİ ZORUNLUDUR. || {K} | İŞLENMEMİŞ kıymetli madenleri yurt dışından serbest bölgeye getirenler tarafından ÜÇ (3) İŞ GÜNÜ içinde || {K} | gümrük idarelerine BEYAN VERİLMESİ YETERLİ OLUP, ithalat ve ihracat rejim, karar ve yönetmelikleri UYGULANMAZ.",
        yuva=[
            "32 sayılı Karar: genel kural, Borsaya teslim (doğru)",
            "32 sayılı Karar: antrepoda bilgi verme (doğru)",
            "32 sayılı Karar: serbest bölgede bilgi verme (doğru)",
            "32 sayılı Karar: beyan yeterli, rejim mevzuatı uygulanmaz (doğru)",
        ],
        yakinlik="BİREBİR",
        tuzak=["İSTİSNA", "KOMŞU"],
        duzey=["AYIRT"],
        profil=[3],
        olumsuz=True,
        cikmis="2023/50",
    ),
    # 9 ---------------- DİR kapsamında aracı kuruluş olmayanlarca altın ve gümüş ithali ----------------
    s(
        kalip="ORAN-TUTAR",
        z="O",
        madde="2008-32-34 sayılı Tebliğ md. 6",
        cek="DİR kapsamında aracı kuruluş olmayan yerleşikler her ithalatta en fazla 40 kg standart işlenmemiş altın veya 200 kg gümüş ithal edebilir.",
        kok=[
            f"{TEB} hükümlerine göre, Dahilde İşleme Rejimi Kararı kapsamında kıymetli madenler aracı kuruluşu olmayan Türkiye'de yerleşik kişilerce her bir ithalat işleminde ithal edilebilecek standart işlenmemiş altın ve gümüş miktarının üst sınırları aşağıdakilerden hangisinde doğru verilmiştir?"
        ],
        d="Altın 40 kilogram, gümüş 200 kilogram",
        c=[
            "Altın 5 kilogram, gümüş 40 kilogram",
            "Altın 40 kilogram, gümüş 100 kilogram",
            "Altın 200 kilogram, gümüş 40 kilogram",
            "Altın 50 kilogram, gümüş 200 kilogram",
        ],
        g="Tebliğe göre Dahilde İşleme Rejimi Kararı kapsamında, kıymetli madenler aracı kuruluşu olmayan Türkiye'de yerleşik kişilerce her bir ithalat işleminde 40 kilogramı aşmamak üzere standart işlenmemiş altın veya 200 kilogramı aşmamak üzere standart işlenmemiş gümüş ithal edilebilir. Bu ithalatta ithalatçı, standart işlenmemiş kıymetli madenin formunu (külçe, bar, granül), cinsini, ağırlığını, adedini, rafinerisini ve rafineri ülkesini gümrük idaresine beyan etmek zorundadır. Beş kilogram, Dahilde İşleme Rejimi kapsamındaki standart dışı kıymetli maden ithalatında özel ayar evlerince düzenlenen ayar raporlarının kabul edilebildiği üst sınırdır. En güçlü tuzak altın ve gümüş sınırlarının yer değiştirdiği seçenektir: iki sayı doğrudur, fakat madenlere ters bağlanmıştır. Bu nedenle doğru cevap 'Altın 40 kilogram, gümüş 200 kilogram' seçeneğidir. (MD 2008-32-34 sayılı Tebliğ md. 6)",
        kanit=f"{K} | 40 KİLOGRAMI AŞMAMAK üzere standart işlenmemiş ALTIN veya 200 KİLOGRAMI AŞMAMAK üzere || {K} | DAHİLDE İŞLEME REJİMİ KARARI KAPSAMINDA, kıymetli madenler aracı kuruluşu olmayan Türkiye'de yerleşik || {K} | BEŞ (5) KİLOGRAMA KADAR olan || {K} | STANDART İŞLENMEMİŞ KIYMETLİ MADENİN FORMU (külçe/bar/granül), külçe/bar cinsi, ağırlığı, adedi, rafinerisi, rafineri",
        yuva=[
            "Ayar raporundaki 5 kg sınırıyla karıştırma",
            "Altın doğru, gümüş eksik",
            "Altın ve gümüş sınırlarının yer değiştirmesi",
            "Gümüş doğru, altın fazla",
        ],
        yakinlik="BİREBİR",
        tuzak=["TERSİNE", "YAKIN-SAYI"],
        duzey=["HATIRLAMA"],
        profil=[1],
        olumsuz=False,
        cikmis="2025/37",
    ),
    # 10 ---------------- Kıymetli maden ithalatında ödeme şekli, ayar raporu, bedelsiz ithalat (önermeli) ----------------
    s(
        kalip="ÖNERMELİ",
        z="Z",
        madde="2008-32-34 sayılı Tebliğ md. 6",
        cek="İşlenmemiş: yalnız peşin, mal mukabili, bedelsiz; işlenmiş: vesaik mukabili ve vadeli akreditif dahil; standart dışı ithalde ayar raporu; mahsupta fiili ihracat önce.",
        kok=[
            f"{TEB} hükümlerine göre kıymetli madenlerin ithalatı hakkında;",
            "I. İşlenmemiş kıymetli madenlerin vadeli akreditifli ödeme şekliyle ithalatı mümkündür.",
            "II. İşlenmiş kıymetli madenlerin vesaik mukabili ödeme şekliyle ithalatı mümkün değildir.",
            "III. Standart dışı işlenmemiş kıymetli madenlerin ithalinde gümrük idarelerine ayar raporu ibraz edilmesi zorunludur.",
            "IV. Kamu kurum ve kuruluşları ile Türk Silahlı Kuvvetlerini Güçlendirme Vakfı şirketlerince standart dışı işlenmemiş kıymetli maden ithal edilmesi mümkündür.",
            "V. İhracat bedellerinden mahsup edilmek üzere bedelsiz ödeme şekliyle yapılan işlenmemiş kıymetli maden ithalatında, mahsup edilecek bedele ilişkin fiili ihracatın kıymetli madenlerin ithalinden önce gerçekleştirilmiş olması zorunludur.",
            "ifadelerinden hangileri doğrudur?",
        ],
        d="III, IV ve V",
        c=["I ve II", "III ve V", "I, II ve IV", "I, III, IV ve V"],
        sirali=True,
        siklar=[
            "I ve II",
            "III ve V",
            "III, IV ve V",
            "I, II ve IV",
            "I, III, IV ve V",
        ],
        g="Tebliğe göre işlenmemiş kıymetli madenlerin yalnızca peşin, mal mukabili ve bedelsiz ödeme şekilleri ile ithalatı mümkündür; vadeli akreditifli ödeme bu sayımda yoktur (I yanlış). İşlenmiş kıymetli madenlerin ise peşin, mal mukabili, vadeli akreditifli, kabul kredili, vesaik mukabili ve bedelsiz ödeme şekilleriyle ithalatı mümkündür (II yanlış). Standart dışı işlenmemiş kıymetli madenlerin ithalinde gümrük idarelerine ayar raporu ibrazı zorunludur ve bu rapor kural olarak yalnız Darphane ve Damga Matbaası Genel Müdürlüğünce düzenlenir (III doğru). Kamu kurum ve kuruluşları ile Türk Silahlı Kuvvetlerini Güçlendirme Vakfı şirketlerince standart dışı işlenmemiş kıymetli maden ithal edilebilir (IV doğru). İhracat bedellerinden mahsup edilmek üzere aracı kuruluşlar aracılığıyla bedelsiz ithalatta, mahsup edilecek bedele ilişkin fiili ihracatın kıymetli madenlerin ithalinden önce gerçekleştirilmiş olması zorunludur (V doğru). En güçlü tuzak I. önermedir: vadeli akreditifli ödeme işlenmiş kıymetli madenler için sayıldığından işlenmemişlere de uygulanabileceği sanılır. Bu nedenle doğru cevap 'III, IV ve V' seçeneğidir. (MD 2008-32-34 sayılı Tebliğ md. 6)",
        kanit=f"{K} | İŞLENMEMİŞ kıymetli madenlerin yalnızca ... PEŞİN ... MAL MUKABİLİ ... ödeme şekilleri ile ithalatı || {K} | İŞLENMİŞ kıymetli madenlerin ... VADELİ AKREDİTİFLİ ... KABUL KREDİLİ ... VESAİK || {K} | Standart dışı işlenmemiş kıymetli madenlerin ithalinde Gümrük İdarelerine ayar raporu ibraz edilmesi zorunlu || {K} | Türk Silahlı Kuvvetlerini Güçlendirme Vakfı şirketlerince standart dışı işlenmemiş || {K} | mahsup edilecek bedele ilişkin fiili ihracatın kıymetli madenlerin ithal edilmesinden önce || {K} | AYAR RAPORLARI yalnızca Darphane ve Damga Matbaası Genel Müdürlüğünce düzenlenebilir.",
        yuva=[
            "I ve II: ödeme şekli listelerini ters bilen aday",
            "III ve V: kamu kurumu istisnasını bilmeyen aday (eksik seçim)",
            "I, II ve IV: ödeme şekillerini karıştıran aday",
            "I, III, IV ve V: vadeli akreditifi işlenmemişe de uygulayan aday",
        ],
        yakinlik="PARAFRAZ",
        tuzak=["KOMŞU", "LİSTE-DIŞI"],
        duzey=["AYIRT", "BÜTÜNLEŞİK"],
        profil=[2, 3],
        olumsuz=False,
        eksen=1,
        ayna="işlenmemiş kıymetli maden ödeme şekilleri ↔ işlenmiş kıymetli maden ödeme şekilleri",
        cikmis="2025/31",
    ),
    # 11 ---------------- Kapatılmayan ihracat hesabı: ihbar ve ihtarname süreleri ----------------
    s(
        kalip="SÜRE",
        z="O",
        madde="2018-32-48 sayılı Tebliğ md. 8",
        cek="Süresinde kapatılmayan ihracat hesabını banka 5 iş gününde vergi dairesine ihbar eder; vergi dairesi 10 iş gününde 90 gün süreli ihtarname gönderir.",
        kok=[
            f"{TEB48} uyarınca, bedeli süresi içinde yurda getirilmediği için kapatılmayan ihracat hesabına ilişkin işlemlerden hangisi doğru verilmiştir?"
        ],
        d="Aracı banka hesabı beş iş günü içinde ilgili vergi dairesine ihbar eder; vergi dairesi ihbarı müteakip on iş günü içinde 90 gün süreli ihtarname gönderir.",
        c=[
            "Aracı banka hesabı on iş günü içinde ilgili vergi dairesine ihbar eder; vergi dairesi ihbarı müteakip beş iş günü içinde 90 gün süreli ihtarname gönderir.",
            "Aracı banka hesabı beş iş günü içinde Hazine ve Maliye Bakanlığına ihbar eder; Bakanlık 180 gün süreli ihtarname gönderir.",
            "Aracı banka hesabı beş iş günü içinde ilgili vergi dairesine ihbar eder; vergi dairesi ihbarı müteakip on iş günü içinde 30 gün süreli ihtarname gönderir.",
            "Aracı banka hesabı 30 gün içinde ilgili gümrük idaresine ihbar eder; gümrük idaresi 90 gün süreli ihtarname gönderir.",
        ],
        g="İhracat Bedelleri Hakkında Tebliğe göre bedelleri yurda getirilme süresi içinde gelen ihracat hesaplarını aracı bankalar kapatır ve İhracat Bedeli Kabul Belgesi düzenler. Süresi içinde kapatılmayan hesaplar aracı bankalarca beş iş günü içinde, muamelenin safhalarını gösterecek şekilde ilgili Vergi Dairesi Başkanlığına veya Vergi Dairesi Müdürlüğüne yazılı olarak ihbar edilir. Vergi dairesi ihbarı müteakip on iş günü içinde ilgililere hesapların kapatılması için 90 gün süreli ihtarname gönderir; bu süre içinde hesap kapatılmalı ya da mücbir sebep veya haklı durum belgelenmelidir. Mücbir sebepte altışar aylık dönemler itibarıyla, haklı durumda altı aya kadar üçer aylık devreler halinde vergi dairesince ek süre verilir. En güçlü tuzak beş ve on iş günü sürelerinin yer değiştirdiği seçenektir: iki süre de hükümde geçer, fakat ilki bankanın ihbarına, ikincisi vergi dairesinin ihtarnamesine aittir. Bu nedenle doğru cevap 'Aracı banka hesabı beş iş günü içinde ilgili vergi dairesine ihbar eder; vergi dairesi ihbarı müteakip on iş günü içinde 90 gün süreli ihtarname gönderir.' seçeneğidir. (MD 2018-32-48 sayılı Tebliğ md. 8)",
        kanit=f"{K} | SÜRESİ İÇİNDE KAPATILMAYAN ihracat hesapları aracı bankalarca 5 İŞ GÜNÜ içinde muamelenin safhalarını || {K} | ihbarı müteakip 10 İŞ GÜNÜ içinde ilgililere || {K} | hesapların kapatılmasını teminen 90 GÜN SÜRELİ ihtarname gönderilir. || {K} | ALTIŞAR AYLIK dönemler itibarıyla || {K} | ilişkin ALTI AYA KADAR OLAN ek süre talepleri",
        yuva=[
            "Banka ve vergi dairesi sürelerinin yer değiştirmesi",
            "Merci (Bakanlık) ve ihtarname süresi yanlış",
            "İhtarname süresi yanlış (30 gün)",
            "Merci (gümrük idaresi) ve ihbar süresi yanlış",
        ],
        yakinlik="BİREBİR",
        tuzak=["TERSİNE", "MAKAM", "SAYI"],
        duzey=["HATIRLAMA", "AYIRT"],
        profil=[1, 3],
        olumsuz=False,
        cikmis="2023/34",
    ),
    # 12 ---------------- Mücbir sebep hali – tevsik belgesi eşleştirmesi (yanlış eşleştirme) ----------------
    s(
        kalip="EŞLEŞTİRME",
        z="Z",
        madde="2018-32-48 sayılı Tebliğ md. 9",
        cek="Mücbir sebep tevsiki: iflas ve dava yetkili mercilerden; grev ve afet resmi makam veya oda onaylı firma belgesinden (harp-abluka hariç); kayıp sigortadan.",
        kok=[
            f"{TEB48} uyarınca, ihracat bedellerinin yurda getirilmesinde ileri sürülen mücbir sebep hali ile bu halin tevsik edileceği belge eşleştirmelerinden hangisi yanlıştır?"
        ],
        d="Harp ve abluka hali – Mahalli odaca tasdik edilmiş olmak kaydıyla alıcı veya ithalatçı firmadan alınan belge",
        c=[
            "Malların kaybı, hasara uğraması veya imha edilmesi – Sigorta şirketlerinden alınmış belge",
            "Grev, lokavt ve avarya hali – İthalatçının bulunduğu memleketin resmi makamlarından alınmış belge",
            "İhtilaf nedeniyle dava açılması veya tahkime başvurulması – Yetkili mercilerden alınmış belge",
            "Muhabir bankaların muameleleri dolayısıyla hesapların kapatılmasının imkânsız hale gelmesi – Muhabir bankalardan alınmış belge",
        ],
        g="İhracat Bedelleri Hakkında Tebliğ mücbir sebep hallerini ve her birinin nasıl tevsik edileceğini sayar. Firmanın iflası veya infisahı gibi haller ile ihtilaf nedeniyle dava açılması veya tahkime başvurulması yetkili mercilerden alınan belgelerle; grev, lokavt ve avarya ile tabii afet, harp ve abluka halleri ithalatçının bulunduğu memleketin resmi makamlarından veya mahalli odaca tasdik edilmiş olmak kaydıyla alıcı ya da ithalatçı firmadan alınan belgelerle tevsik edilir; ancak harp ve abluka hali firma belgesiyle tevsik edilemez. Resmi makam kararları veya muhabir bankaların muameleleri nedeniyle hesabın kapatılamaması resmi makamlarımızdan, ithalatçı ülkenin resmi makamlarından veya muhabir bankalardan; malların kaybı, hasarı veya imhası sigorta şirketlerinden, uluslararası gözetim şirketlerinden veya ilgili ülke resmi makamlarından alınan belgelerle tevsik edilir. Yurt dışından alınan belgeler dış temsilciliklerimizce veya Lahey Sözleşmesine göre onaylanmış olmalıdır. En güçlü tuzak grev, lokavt ve avarya eşleştirmesidir: harp ve abluka ile aynı grupta sayıldığı için resmi makam belgesinin de geçersiz olduğu sanılabilir. Bu nedenle doğru cevap 'Harp ve abluka hali – Mahalli odaca tasdik edilmiş olmak kaydıyla alıcı veya ithalatçı firmadan alınan belge' seçeneğidir. (MD 2018-32-48 sayılı Tebliğ md. 9)",
        kanit=f"{K} | (a) ve (e) halinin yetkili mercilerden, (b) ve (ç) halinin, ithalatçının bulunduğu memleketin resmi makamlarından || {K} | veya mahalli odaca tasdik edilmiş olmak kaydıyla alıcı veya ithalatçı firmadan (harp ve abluka hali hariç), (c) || {K} | halinin resmi makamlarımızdan, ithalatçının bulunduğu memleketin resmi makamlarından veya muhabir || {K} | bankalardan, (d) halinin ise sigorta şirketlerinden, uluslararası gözetim şirketlerinden veya ilgili ülke resmi || {K} | b) Grev, lokavt ve avarya hali, || {K} | ç) Tabii afet, harp ve abluka hali, || {K} | d) Malların kaybı, hasara uğraması veya imha edilmesi, || {K} | e) İhtilaf nedeniyle dava açılması veya tahkime başvurulması,",
        yuva=[
            "Tebliğ: kayıp-hasar ↔ sigorta şirketi (doğru)",
            "Tebliğ: grev-lokavt-avarya ↔ ithalatçı ülke resmi makamı (doğru)",
            "Tebliğ: dava-tahkim ↔ yetkili merciler (doğru)",
            "Tebliğ: muhabir banka ↔ muhabir banka belgesi (doğru)",
        ],
        yakinlik="BİREBİR",
        tuzak=["İSTİSNA", "KOMŞU"],
        duzey=["AYIRT"],
        profil=[3],
        olumsuz=True,
    ),
    # 13 ---------------- Terkin: 200.000 ABD dolarını aşan noksanlık ----------------
    s(
        kalip="YETKİ",
        z="O",
        madde="2018-32-48 sayılı Tebliğ md. 10",
        cek="Beyanname başına 200.000 dolara kadar ve %10'a kadar açık hesabı vergi dairesi terkin eder; 200.000 doları aşan noksanlıkta terkin talebini HMB sonuçlandırır.",
        kok=[
            f"{TEB48} uyarınca, her bir gümrük beyannamesi itibarıyla 200.000 ABD dolarını aşan noksanlığı olan açık ihracat hesaplarına ilişkin terkin talepleri, mücbir sebep ve haklı durumlar göz önünde bulundurularak hangi merci tarafından incelenip sonuçlandırılır?"
        ],
        d="Hazine ve Maliye Bakanlığı",
        c=[
            "İhracata aracılık eden banka",
            "İlgili Vergi Dairesi Başkanlığı veya Vergi Dairesi Müdürlüğü",
            "Ticaret Bakanlığı",
            "Türkiye Cumhuriyet Merkez Bankası",
        ],
        g="İhracat Bedelleri Hakkında Tebliğ terkin yetkisini noksanlık tutarına göre kademelendirir. Düşük tutarlı noksanlıklarda açık hesaplar doğrudan bankalarca ödeme şekline bakılmaksızın terkin edilerek kapatılır; 200.000 ABD doları veya eşitini aşmamak üzere, beyanname veya formdaki bedelin yüzde onuna kadar olan açık hesaplar mücbir sebep ve haklı durumlar dikkate alınarak ilgili Vergi Dairesi Başkanlığınca veya Vergi Dairesi Müdürlüğünce terkin edilir. Her bir gümrük beyannamesi itibarıyla 200.000 ABD doları veya eşitini aşan noksanlığı olan açık hesaplara ilişkin terkin talepleri ise Hazine ve Maliye Bakanlığınca incelenip sonuçlandırılır. Ticaret Bakanlığı ve Merkez Bankası terkin kademelerinde yer almaz. En güçlü tuzak vergi dairesidir: 200.000 ABD doları vergi dairesi yetkisinin üst sınırı olduğu için bu tutarı aşan noksanlıkta da yetkili sanılır. Bu nedenle doğru cevap 'Hazine ve Maliye Bakanlığı' seçeneğidir. (MD 2018-32-48 sayılı Tebliğ md. 10)",
        kanit=f"{K} | 200.000 ABD DOLARI VEYA EŞİTİNİ AŞAN NOKSANLIĞI olan açık || {K} | hesaplara ilişkin terkin talepleri bu Tebliğin 9. maddesinde belirtilen mücbir sebepler ile haklı durumlar göz || {K} | önünde bulundurulmak suretiyle HAZİNE VE MALİYE BAKANLIĞI tarafından incelenip SONUÇLANDIRILIR. || {K} | 200.000 ABD DOLARI VEYA EŞİTİNİ AŞMAMAK ÜZERE, || {K} | hesaplar ilgili VERGİ DAİRESİ BAŞKANLIĞINCA veya VERGİ DAİRESİ MÜDÜRLÜĞÜNCE, || {K} | ihracat hesapları doğrudan BANKALARCA ÖDEME ŞEKLİNE BAKILMAKSIZIN,",
        yuva=[
            "Tebliğ: düşük tutarlarda banka terkini",
            "Tebliğ: 200.000 dolara kadar vergi dairesi terkini (sınır komşusu)",
            "Dış ticaret mercii (kademede yok)",
            "Kambiyo mercii (kademede yok)",
        ],
        yakinlik="BİREBİR",
        tuzak=["MAKAM", "YAKIN-SAYI"],
        duzey=["HATIRLAMA"],
        profil=[1],
        olumsuz=False,
    ),
    # 14 ---------------- İthalat Genelgesi 2020/1: ithalat bedellerinin ödenmesi (olumsuz) ----------------
    s(
        kalip="YANLIŞ",
        z="O",
        madde="İthalat Genelgesi 2020/1 md. 3, 5, 6",
        cek="İthalat bedeli için bankalarca çek düzenlenemez; ihracatçının Türkiye'deki hesabına ödenebilir; mal mukabilinde beyanname tarih-numarası; faktoring peşin sayılır; transit ticaret ithalat kurallarıyla.",
        kok=[
            f"{KAR} çerçevesinde Hazine ve Maliye Bakanlığınca yayımlanan İthalat Genelgesine (2020/1) göre ithalat bedellerinin ödenmesine ilişkin aşağıdaki ifadelerden hangisi yanlıştır?"
        ],
        d="İthalat bedelinin ödenmesini teminen bankalarca çek düzenlenebilir.",
        c=[
            "İthalat bedeli, ihracatçı adına Türkiye'de açılan döviz tevdiat hesabına veya Türk lirası mevduat hesabına yatırılmak suretiyle ödenebilir.",
            "Mal mukabili ithalatta firmaların mal bedelinin transferine ilişkin talepleri, firmanın yazılı olarak beyan edeceği gümrük beyannamesi tarih ve numarasına istinaden bankalarca yerine getirilir.",
            "Faktoring kuruluşunca ithalden önce ithalatçı firma adına yurt dışına transfer edilen tutarlar, faktoring sözleşmelerinin transferi gerçekleştiren bankaya ibrazı kaydıyla peşin ödeme olarak dikkate alınır.",
            "Transit ticaret alış bedellerinin ödenmesinde ithalat bedellerinin ödenmesinde esas olan kurallar geçerlidir.",
        ],
        g="İthalat Genelgesine göre ithalat bedelleri sözleşmeye, uluslararası kurallara ve bankacılık teamüllerine göre bankalar aracılığıyla döviz veya Türk lirası olarak ödenir; banka kaynaklarından, ithalatçının döviz tevdiat hesabından, kredi kartından, mahsup koşulları sağlanmışsa alışı yapılmamış ihracat bedelinden veya sermaye hareketleri kapsamındaki kredilerden karşılanabilir. İthalat bedeli ihracatçı adına Türkiye'de açılan döviz tevdiat hesabına veya Türk lirası mevduat hesabına yatırılarak ödenebilir; mal mukabili ithalatta transfer talepleri firmanın yazılı olarak beyan edeceği gümrük beyannamesi tarih ve numarasına istinaden bankalarca yerine getirilir. Faktoring kuruluşunun ithalden önce yurt dışına transfer ettiği tutarlar sözleşmelerin bankaya ibrazı kaydıyla peşin ödeme sayılır; transit ticaret alış bedellerinde de ithalat bedellerine ilişkin kurallar uygulanır. Buna karşılık bankalarca ithalat bedelinin ödenmesini teminen çek düzenlenemez. En güçlü tuzak mal mukabili ithalata ilişkin ifadedir: transferin gümrük beyannamesine bağlanması gümrük idaresinin onayı gibi algılanıp yanlış sanılabilir. Bu nedenle doğru cevap 'İthalat bedelinin ödenmesini teminen bankalarca çek düzenlenebilir.' seçeneğidir. (MD İthalat Genelgesi 2020/1 md. 3, 5, 6)",
        kanit=f"{K} | Bankalarca ithalat bedelinin ödenmesini teminen ÇEK DÜZENLENEMEZ. || {K} | veya TL mevduat hesabına yatırılmak suretiyle || {K} | MAL MUKABİLİ İTHALATTA firmaların mal bedelinin transferine ilişkin talepleri firmanın yazılı olarak beyan || {K} | edeceği gümrük beyannamesi tarih ve numarasına istinaden bankalarca yerine getirilir. || {K} | faktoring kuruluşu tarafından ithalden önce ithalatçı firma adına yurt dışına transferi gerçekleştirilen tutarlar, || {K} | transferi gerçekleştiren bankaya ibrazı kaydıyla peşin ödeme olarak || {K} | Transit ticaret alış bedellerinin ödenmesinde ithalat bedellerinin ödenmesinde esas olan kurallar geçerlidir.",
        yuva=[
            "Genelge: ihracatçının Türkiye'deki hesabına ödeme (doğru)",
            "Genelge: mal mukabilinde beyanname tarih-numarası (doğru)",
            "Genelge: faktoring transferi peşin ödeme (doğru)",
            "Genelge: transit ticarette ithalat kuralları (doğru)",
        ],
        yakinlik="BİREBİR",
        tuzak=["TERSİNE", "SAĞDUYU"],
        duzey=["AYIRT"],
        profil=[3],
        olumsuz=True,
    ),
    # 15 ---------------- Nakit Kontrolleri Genelgesi: beyan usulü (önermeli) ----------------
    s(
        kalip="ÖNERMELİ",
        z="Z",
        madde="Nakit Kontrolleri Genelgesi 2024/1 bölüm 2, 3, 4",
        cek="Sürücüler yolcu sayılır; kabin bagajındaki nakit ilk indiği havalimanında beyan; sayım kamera önünde; resen beyanda form, açıklamada tutanak; gizli nakit girişte 5607.",
        kok=[
            f"{NKG} göre yolcu beraberindeki nakdin beyanı ve kontrolü hakkında;",
            "I. Nakil vasıtalarının sürücü ve yardımcıları Genelge hükümlerinin uygulanması bakımından yolcu olarak kabul edilir.",
            "II. Dış hatlardan gelerek iç hatlara transfer olan yolcu, kabin bagajındaki nakdin beyanını indiği son havalimanında yapar.",
            "III. Beyanda bulunulan veya açıklanan nakdin cins ve miktarının fiziki tespiti kamera önünde sayılarak yapılır.",
            "IV. Resen beyan edilen nakit için Nakit Açıklama Tutanağı, gümrük idaresince açıklama istenen nakit için Nakit Beyan Formu düzenlenir.",
            "V. Yolcu beraberinde değerlendirilmeyen eşya içinde gizlenmiş nakdin ülkeye giriş yönünde tespitinde 5607 sayılı Kaçakçılıkla Mücadele Kanunu uyarınca Cumhuriyet savcısına suç duyurusunda bulunulur.",
            "ifadelerinden hangileri doğrudur?",
        ],
        d="I, III ve V",
        c=["I ve III", "II ve IV", "II, III ve V", "I, II, III ve V"],
        sirali=True,
        siklar=[
            "I ve III",
            "II ve IV",
            "I, III ve V",
            "II, III ve V",
            "I, II, III ve V",
        ],
        g="Nakit Kontrolleri Genelgesine göre nakil vasıtalarının sürücü ve yardımcıları Genelgenin uygulanmasında yolcu sayılır (I doğru). Dış hatlardan gelip iç hatlara transfer olan yolcu kabin bagajındaki nakdi ilk indiği havalimanında beyan eder; nakit uçak altı bagajındaysa beyan indiği son havalimanında yapılır (II yanlış). Beyan edilen veya açıklanan nakdin cins ve miktarı kamera önünde sayılarak fiziken tespit edilir (III doğru). Belgeler ters bağlanmıştır: resen beyan edilen nakit için Nakit Beyan Formu, gümrük idaresince açıklama istenen nakit için Nakit Açıklama Tutanağı düzenlenir (IV yanlış). Yolcu beraberinde değerlendirilmeyen eşya içinde gizlenmiş nakit tespit edilirse ülkeye giriş yönünde 5607 sayılı Kaçakçılıkla Mücadele Kanunu, çıkış yönünde 1567 sayılı Kanun uyarınca Cumhuriyet savcısına suç duyurusunda bulunulur (V doğru). En güçlü tuzak II. önermedir: kabin bagajı ile uçak altı bagajı için öngörülen havalimanları birbirinin tersidir. Bu nedenle doğru cevap 'I, III ve V' seçeneğidir. (MD Nakit Kontrolleri Genelgesi 2024/1 bölüm 2, 3, 4)",
        kanit=f"{K} | Nakil vasıtalarının sürücü ve yardımcıları bu genelge hükümlerinin uygulanması bakımından YOLCU OLARAK || {K} | DIŞ HATLARDAN GELEREK İÇ HATLARA TRANSFER OLAN YOLCULARIN beraberindeki kabin bagajında || {K} | bulunan nakdin beyanını ilk indiği havalimanında yapması gerekmektedir. || {K} | Transfer olan yolcunun NAKDİNİN UÇAK ALTI BAGAJINDA OLMASI DURUMUNDA İNDİĞİ SON || {K} | nakdin cins ve miktarının FİZİKİ TESPİTİ KAMERA ÖNÜNDE SAYILARAK YAPILIR. || {K} | RESEN BEYAN edilen nakitle ilgili olarak || {K} | GÜMRÜK İDARESİ TARAFINDAN AÇIKLAMA yapılması istenen nakitle ilgili olarak ise || {K} | ÜLKEYE GİRİŞ YÖNÜNDE 5607 sayılı Kaçakçılıkla Mücadele Kanunu uyarınca, || {K} | CUMHURİYET SAVCISINA SUÇ DUYURUSUNDA BULUNULUR.",
        yuva=[
            "I ve III: gizli nakit hükmünü bilmeyen aday (eksik seçim)",
            "II ve IV: transfer ve belge kurallarını ters bilen aday",
            "II, III ve V: kabin bagajında son havalimanını seçen aday",
            "I, II, III ve V: bagaj türlerini karıştıran aday",
        ],
        yakinlik="PARAFRAZ",
        tuzak=["TERSİNE", "KOMŞU"],
        duzey=["AYIRT", "BÜTÜNLEŞİK"],
        profil=[2, 3],
        olumsuz=False,
        eksen=2,
        ayna="kabin bagajı: ilk indiği havalimanı ↔ uçak altı bagajı: indiği son havalimanı",
        cikmis="2025/59",
    ),
    # 16 ---------------- Hesap: açıklanmayan nakdin %10'u idari para cezası ----------------
    s(
        kalip="HESAP",
        z="O",
        madde="Nakit Kontrolleri Genelgesi 2024/1 bölüm 3; 5549 sayılı Kanun md. 16",
        cek="Açıklama istenen yolcu yanlış açıklarsa açıklanmayan miktarın %10'u idari para cezası; tüm nakit muhafazaya alınır, tutanak MASAK'a gönderilir.",
        kok=[
            "5549 sayılı Kanun ve Nakit Kontrolleri Genelgesine (2024/1) göre aşağıdaki bilgiler veriliyor:",
            "- Yurt dışına çıkmak üzere gümrük kapısına gelen bir yolcudan, gümrük idaresince beraberindeki nakdin miktarını açıklaması istenmiştir.",
            "- Yolcu beraberinde 12.000 Avro bulunduğunu açıklamış; yapılan kontrolde 40.000 Avro taşıdığı tespit edilmiştir.",
            "Buna göre gümrük idaresince uygulanacak idari para cezası kaç Avro tutarındadır?",
        ],
        d="2.800",
        c=["1.200", "3.000", "4.000", "28.000"],
        sirali=True,
        siklar=["1.200", "2.800", "3.000", "4.000", "28.000"],
        g="Nakit Kontrolleri Genelgesine göre gümrük idaresince ülkeye giren veya ülkeden çıkan yolcudan açıklama istendiğinde hiç açıklama yapılmaması ya da yanlış veya yanıltıcı açıklama yapıldığının tespiti halinde, 5549 sayılı Kanun gereğince açıklanmayan miktarın yüzde onu tutarında idari para cezası uygulanır; yolcu beraberindeki tüm nakit muhafaza altına alınır, Nakit Açıklama Tutanağının bir örneği Mali Suçları Araştırma Kurulu Başkanlığına gönderilir ve konu Cumhuriyet Savcılığına bildirilir. Vakada açıklanmayan miktar 40.000 − 12.000 = 28.000 Avrodur; ceza 28.000 × %10 = 2.800 Avro tutarındadır. 1.200 açıklanan miktarın, 4.000 taşınan nakdin tamamının yüzde onudur; 3.000 ise 10.000 Avroluk beyan sınırını aşan kısmın yüzde onu alınarak bulunur; 28.000 açıklanmayan miktarın kendisidir. En güçlü tuzak 3.000'dir: yüzde on, beyan sınırını aşan kısma değil açıklanmayan miktara uygulanır. Bu nedenle doğru cevap '2.800' seçeneğidir. (MD Nakit Kontrolleri Genelgesi 2024/1 bölüm 3; 5549 sayılı Kanun md. 16)",
        kanit=f"{K} | GÜMRÜK İDARESİNCE ÜLKEYE GİREN YA DA ÜLKEDEN ÇIKAN YOLCUDAN AÇIKLAMA İSTENİLDİĞİ DURUMDA, || {K} | herhangi bir açıklama yapılmaması veya yanlış ya da yanıltıcı açıklama yapıldığının tespiti halinde, || {K} | AÇIKLANMAYAN MİKTARIN % 10 || {K} | Yolcu beraberindeki TÜM NAKİT MUHAFAZA ALTINA ALINIR ve || {K} | DÖVİZDE ise 10.000 AVRO VE EŞİTİ EFEKTİF ÜZERİ yolcu beraberi nakdin yurt dışına çıkışta gümrük idaresine beyan",
        yuva=[
            "Açıklanan miktarın %10'u",
            "Beyan sınırını aşan kısmın %10'u",
            "Taşınan nakdin tamamının %10'u",
            "Açıklanmayan miktarın tamamı",
        ],
        yakinlik="ÇIKARIM",
        tuzak=["AD-HESAP", "YAKIN-SAYI"],
        duzey=["UYGULAMA"],
        profil=[4],
        olumsuz=False,
        vaka=True,
    ),
]
