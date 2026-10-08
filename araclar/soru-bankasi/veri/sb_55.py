# Soru Bankası — Bölüm 55: Kaçakçılık Mahkûmiyetlerinin İlanı ve Milli Savunma/İç Güvenlik Eşyası (20 soru)
# Gümrük Koçu - Ufuk Çetintaş
IY = "kacakcilik_turleri_ile_ilgili_mahkumiyet_hukmu_kesinlesenlerin_kamuoyuna_ilan_edilmesine_dair_yonetmelik.txt"
TY = "milli_savunma_veya_ic_guvenlik_hizmetleriyle_dogrudan_ilgili_silah_muhimmat_arac_ve_gerec_ile_sarf_malzem.txt"
K5607 = "5607_sayili_kacakcilikla_mucadele_kanunu.txt"
IYN = "Kaçakçılık Türleri ile İlgili Mahkûmiyet Hükmü Kesinleşenlerin Kamuoyuna İlan Edilmesine Dair Yönetmelik"
TYN = "Millî Savunma veya İç Güvenlik Hizmetleriyle Doğrudan İlgili Silah, Mühimmat, Araç ve Gereç ile Sarf Malzemesinin Tahsisine İlişkin Yönetmelik"
KONU = "Kaçakçılık Mahkûmiyetlerinin İlanı ve Milli Savunma/İç Güvenlik Eşyası"
Q = [

# 1 ---------------- İlan Yön. md. 4/1, 6/3: ilan şartı = mahkûmiyet hükmünün kesinleşmesi (2021/91) ----------------
dict(
konu=KONU, blok="SB55",
kalip="ŞART",
z="O",
madde=IYN + " md. 4, 6",
cek="Sayılan kaçakçılık fiillerinden ancak mahkûmiyet hükmü kesinleşenler ilan edilebilir; uyuşturucuda miktar veya gümrüklenmiş değer aranmaz.",
kok=[IYN + "'e göre, uyuşturucu kaçakçılığı fiilini işleyen kişilerin Bakanlık tarafından kamuoyuna ilan edilebilmesi için aşağıdakilerden hangisi gereklidir?"],
d="Haklarında verilen mahkûmiyet hükmünün kesinleşmiş olması",
c=["Kaçakçılığa konu uyuşturucunun gümrüklenmiş değerinin 500.000 Türk Lirasından az olmaması",
   "Suçun bir tüzel kişinin faaliyeti çerçevesinde veya yararına işlenmiş olması",
   "Suçun en az üç kişi tarafından birlikte işlenmiş olması",
   "İlan edileceklerin Bakanlık bünyesinde oluşturulan Komisyonca belirlenmiş olması"],
sirali=False,
g="Yönetmeliğe göre tütün ve tütün mamulleri, alkollü içkiler, akaryakıt, uyuşturucu, silah ve mühimmat gibi sayılan kaçakçılık fiillerinden mahkûmiyet hükmü kesinleşenler, kamuoyunun bilgilendirilmesi amacıyla Bakanlık tarafından ilan edilebilir. İlanın ön şartı kişi hakkındaki mahkûmiyet hükmünün kesinleşmiş olmasıdır; soruşturma veya kovuşturması süren kişi ilan edilemez. Uyuşturucu kaçakçılığı, miktar veya eşyanın gümrüklenmiş değerine bakılmaksızın ilan edilebilecek fiiller arasında sayılmıştır; 500.000 Türk Lirası sınırı yalnızca ayrıca sayılmayan diğer eşya türleri için aranır. Üç veya daha fazla kişiyle birlikte işleme cezayı yarı oranında artıran, tüzel kişinin faaliyeti çerçevesinde veya yararına işleme ise ayrıca güvenlik tedbirine hükmedilmesini gerektiren nitelikli hâllerdir; ikisi de 5607 sayılı Kanun'da ceza ve tedbire ilişkindir, ilan şartı değildir. İlan edilecekleri belirleyen Komisyon 10.04.2019 tarihli değişiklikle kaldırılmıştır. En güçlü çeldirici 500.000 Türk Lirası sınırıdır: uyuşturucu bu sınırdan bağımsız olarak ilan edilebilen fiillerdendir. Bu nedenle doğru cevap 'Haklarında verilen mahkûmiyet hükmünün kesinleşmiş olması' seçeneğidir. (MD 4, 6; 5607 md. 4)",
kanit=IY + " | fikri ve sınai mülkiyet hakları, sahte para, altın, maden kaçakçılığı, hayali ihracat, göçmen kaçakçılığı fiillerinden mahkûmiyet hükmü kesinleşenler kamuoyunun bilgilendirilmesi amacıyla Bakanlık tarafından ilan edilebilir || "
      + IY + " | uyuşturucu ile silah ve mühimmat, sahte para, altın, maden kaçakçılığı ve göçmen kaçakçılığı fiilleri, miktar veya eşyanın gümrüklenmiş değerine bakılmaksızın kamuoyuna ilan edilebilir || "
      + IY + " | kamuoyuna ilan edilecekler, Bakanlık bünyesinde oluşturulan Komisyon tarafından belirlenir || "
      + K5607 + " | tüzel kişinin faaliyeti çerçevesinde veya yararına olarak işlenmesi halinde, ayrıca bunlara özgü güvenlik tedbirlerine hükmolunur",
yuva=["İlana esas miktar veya değerler: diğer eşya türleri için gümrüklenmiş değerin 500.000 TL'den az olmaması (uyuşturucu bu sınırdan bağımsız listede)",
      "5607 sayılı Kanun nitelikli hâller (Yönetmeliğin dayanak maddesi): tüzel kişinin faaliyeti çerçevesinde işlemede güvenlik tedbirleri",
      "5607 sayılı Kanun nitelikli hâller (Yönetmeliğin dayanak maddesi): üç veya daha fazla kişiyle birlikte işleme cezayı yarı oranında artırır",
      "Mülga Komisyon hükmü (10.04.2019 öncesi): ilan edilecekleri Komisyon belirlerdi"],
yakinlik="PARAFRAZ",
tuzak=["TERİM", "KOMŞU", "İSTİSNA"], duzey=["AYIRT"], profil=[1, 3],
olumsuz=False, vaka=False, baslangic=False, eksen=0, ayna="", guncellik="",
cikmis="2021/91", kapsamli=False,
),

# 2 ---------------- İlan Yön. md. 1/2: 18 yaş suçun işlendiği tarihe göre — vaka ----------------
dict(
konu=KONU, blok="SB55",
kalip="OLAY",
z="Z",
madde=IYN + " md. 1, 6",
cek="Yönetmelik suçun işlendiği tarihte 18 yaşını doldurmamış olanlara uygulanmaz; yaş, mahkûmiyetin kesinleştiği tarihe göre belirlenmez.",
kok=["(M) 16 Mayıs 2007 doğumludur. (M)'nin 10 Mart 2025 tarihinde işlediği 600 kilogram şeker kaçakçılığı fiilinden dolayı verilen mahkûmiyet hükmü 19 Haziran 2026 tarihinde kesinleşmiştir.",
     IYN + "'e göre (M) hakkında aşağıdakilerden hangisi doğrudur?"],
d="Suçun işlendiği tarihte 18 yaşını doldurmadığı için Yönetmelik hükümleri uygulanmaz.",
c=["Mahkûmiyet hükmünün kesinleştiği tarihte 18 yaşını doldurduğu için Bakanlık tarafından ilan edilebilir.",
   "Şeker için aranan 500 kilogram sınırı aşıldığından ilan edilebilir.",
   "Kaçakçılık suçuna ve (M)'ye ilişkin bilgiler üç ay süreyle Bakanlık resmî internet sitesinde yayımlanır.",
   "Şeker kaçakçılığı miktara bakılmaksızın ilan edilebilecek fiillerden olduğundan Bakanlık tarafından ilan edilebilir."],
sirali=False,
g="Yönetmelik hükümleri, suçun işlendiği tarihte 18 yaşını doldurmamış olanlar için uygulanmaz. (M) 16 Mayıs 2007 doğumlu olduğundan 18 yaşını 16 Mayıs 2025'te doldurur; şeker kaçakçılığı fiilini işlediği 10 Mart 2025 tarihinde 17 yaşındadır. Mahkûmiyet hükmünün kesinleştiği 19 Haziran 2026'da 18 yaşını doldurmuş olması sonucu değiştirmez; yaş, kesinleşme tarihine göre değil suçun işlendiği tarihe göre belirlenir. 'Suçun işlendiği tarihte' ibaresi Yönetmeliğe 10.04.2019 tarihli değişiklikle eklenmiştir. Şeker için aranan 500 kilogram sınırı aşılmış olsa da yaş istisnası nedeniyle Yönetmelik uygulanmaz; bu yüzden üç aylık internet yayını da söz konusu olmaz. Ayrıca şeker, miktar veya değere bakılmaksızın ilan edilebilecek fiiller arasında yer almaz. En güçlü çeldirici, yaşı mahkûmiyetin kesinleştiği tarihe göre belirleyen seçenektir. Bu nedenle doğru cevap 'Suçun işlendiği tarihte 18 yaşını doldurmadığı için Yönetmelik hükümleri uygulanmaz.' seçeneğidir. (MD 1, 6, 7)",
kanit=IY + " | Bu Yönetmelik hükümleri suçun işlendiği tarihte … 18 yaşını doldurmamış olanlar için uygulanmaz || "
      + IY + ' | ibaresi 10.04.2019 / 30741 RG ile eklenmiştir || '
      + IY + " | Şeker için 500 kilogramdan",
yuva=["Yaş istisnası hükmünün eski hâli: 10.04.2019 öncesinde 'suçun işlendiği tarihte' ibaresi yoktu; yaş için referans tarih belirtilmemişti",
      "İlana esas miktarlar: şeker için 500 kilogramdan az olmama şartı (sınır aşılmış ama yaş istisnası öncelikli)",
      "İlanın yayımlanması: bilgiler üç ay süreyle Bakanlık resmî internet sitesinde yayımlanır (Yönetmelik uygulanırsa)",
      "Miktar veya değere bakılmaksızın ilan edilebilecek fiiller listesi (şeker bu listede değildir)"],
yakinlik="ÇIKARIM",
tuzak=["İSTİSNA", "KOMŞU", "TERİM"], duzey=["UYGULAMA"], profil=[1],
olumsuz=False, vaka=True, baslangic=False, eksen=0, ayna="", guncellik="",
cikmis="", kapsamli=False,
),

# 3 ---------------- İlan Yön. md. 3, 4/2: ilan kararı Gümrükler Muhafaza GM, icra Bakan Onayı ----------------
dict(
konu=KONU, blok="SB55",
kalip="YETKİ",
z="O",
madde=IYN + " md. 3, 4",
cek="İlan edileceklere dair kararı Genel Müdürlük (Gümrükler Muhafaza Genel Müdürlüğü) verir; karar Bakan Onayı ile icra edilir.",
kok=[IYN + "'e göre, mahkûmiyet hükmü kesinleşenlerden ilana esas olacak miktar veya değerlere ilişkin hükümlere göre kamuoyuna ilan edileceklere dair karar hangi merci tarafından verilir ve nasıl icra edilir?"],
d="Gümrükler Muhafaza Genel Müdürlüğünce verilir, Bakan Onayı ile icra edilir.",
c=["Bakanlık bünyesinde oluşturulan Komisyonca verilir, Bakan Onayı ile icra edilir.",
   "Gümrükler Muhafaza Genel Müdürlüğünce verilir, Hazine ve Maliye Bakanlığının onayı ile icra edilir.",
   "Hâkim veya mahkemece verilir, başsavcılık aracılığıyla icra edilir.",
   "Gümrükler Muhafaza Genel Müdürlüğünce verilir, ayrıca bir onay aranmaksızın icra edilir."],
sirali=False,
g="Yönetmeliğe göre mahkûmiyet hükmü kesinleşenlerden, ilana esas miktar veya değerlere ilişkin hükümlere göre ilan edileceklere dair karar Genel Müdürlükçe verilir ve Bakan Onayı ile icra edilir. Yönetmelikte Genel Müdürlük, Gümrükler Muhafaza Genel Müdürlüğünü ifade eder. Bu karar 10.04.2019 öncesinde Bakanlık bünyesinde oluşturulan Komisyon tarafından veriliyordu; Komisyon o tarihte kaldırılmış ve karar yetkisi Genel Müdürlüğe verilmiştir, Bakan Onayı şartı ise korunmuştur. Hazine ve Maliye Bakanlığı yalnızca diğer eşya türleri için öngörülen tutarın her yıl artırılmasında esas alınan yeniden değerleme oranını belirler. Hâkim veya mahkeme kararı ve Cumhuriyet başsavcılığı aracılığı, el konulan silah ve mühimmatın kurumlara tahsisine ilişkin Yönetmelikteki usule aittir. En güçlü çeldirici, kaldırılan Komisyon düzenlemesidir. Bu nedenle doğru cevap 'Gümrükler Muhafaza Genel Müdürlüğünce verilir, Bakan Onayı ile icra edilir.' seçeneğidir. (MD 3, 4)",
kanit=IY + " | Mahkûmiyet hükmü kesinleşenlerden, … ilan edileceklere dair karar Genel Müdürlükçe verilir ve Bakan Onayı ile icra edilir || "
      + IY + " | Genel Müdürlük: Gümrükler Muhafaza Genel Müdürlüğünü || "
      + IY + " | Komisyon kararı, Bakan Onayı ile icra edilir",
yuva=["Mülga Komisyon hükmü (10.04.2019 öncesi): Komisyon kararı Bakan Onayı ile icra edilirdi",
      "İlana esas değerler: diğer eşya türleri için tutar Hazine ve Maliye Bakanlığınca belirlenen yeniden değerleme oranında artırılır",
      "Silah, mühimmat tahsisi Yönetmeliği: tahsis talebi Cumhuriyet başsavcılığı aracılığıyla hâkim veya mahkemeden istenir",
      "Aynı hüküm: karar Genel Müdürlükçe verilir; Bakan Onayı unsuru düşürülmüş"],
yakinlik="PARAFRAZ",
tuzak=["MAKAM", "UNSUR", "KOMŞU"], duzey=["AYIRT"], profil=[1],
olumsuz=False, vaka=False, baslangic=False, eksen=0, ayna="", guncellik="",
cikmis="", kapsamli=False,
),

# 4 ---------------- İlan Yön. md. 6/1: eşya–asgari miktar eşleştirmesi (yanlış olan) ----------------
dict(
konu=KONU, blok="SB55",
kalip="EŞLEŞTİRME",
z="O",
madde=IYN + " md. 6",
cek="İlan için akaryakıtta 5.000 litre, alkollü içkide 150 litre, zeytinyağında 250 litre, ette ve tütünde 500 kilogramdan az olmama aranır.",
kok=[IYN + "'te kaçakçılık fiiline konu mahkûmiyet kararının kamuoyuna ilan edilmesi için eşya türlerine göre aranan asgari miktarlarla ilgili aşağıdaki eşleştirmelerden hangisi yanlıştır?"],
d="Tütün – 150 kilogram",
c=["Akaryakıt ve türevleri – 5.000 litre",
   "Alkollü içki – 150 litre",
   "Zeytinyağı – 250 litre",
   "Et – 500 kilogram"],
sirali=False,
g="Yönetmeliğe göre kaçakçılık fiiline konu mahkûmiyet kararının kamuoyuna ilan edilmesi için eşya türüne göre belirli miktarlardan az olmama şartı aranır: akaryakıt ve türevleri için 5.000 litre, sigara için 5.000 paket, tütün için 500 kilogram, alkollü içki için 150 litre, canlı hayvan için 50 baş, et için 500 kilogram, çay için 150 kilogram, şeker için 500 kilogram, zeytin için 250 kilogram, zeytinyağı için 250 litre; diğer eşya türleri için gümrüklenmiş değerin 500.000 Türk Lirası. Tütün için aranan miktar 150 kilogram değil 500 kilogramdır; 150 kilogram çay için öngörülen sınırdır. Akaryakıt, alkollü içki, zeytinyağı ve et eşleştirmeleri doğrudur. En güçlü tuzak, alkollü içkide de 150 sayısının bulunmasıdır: 150 alkollü içkide litre, çayda kilogram olarak geçer; tütünde geçmez. Bu nedenle doğru cevap 'Tütün – 150 kilogram' seçeneğidir. (MD 6)",
kanit=IY + " | Tütün için 500 kilogramdan || " + IY + " | Çay için 150 kilogramdan || "
      + IY + " | Akaryakıt ve türevleri için 5.000 litreden || " + IY + " | Alkollü içki için 150 litreden || "
      + IY + " | Zeytinyağı için 250 litreden || " + IY + " | Et için 500 kilogramdan",
yuva=["İlana esas miktarlar: akaryakıt ve türevleri için 5.000 litre (doğru eşleştirme)",
      "İlana esas miktarlar: alkollü içki için 150 litre (doğru eşleştirme)",
      "İlana esas miktarlar: zeytinyağı için 250 litre (doğru eşleştirme)",
      "İlana esas miktarlar: et için 500 kilogram (doğru eşleştirme)"],
yakinlik="BİREBİR",
tuzak=["YAKIN-SAYI", "KOMŞU"], duzey=["AYIRT"], profil=[2, 4],
olumsuz=True, vaka=False, baslangic=False, eksen=0, ayna="", guncellik="",
cikmis="", kapsamli=False,
),

# 5 ---------------- İlan Yön. md. 6/1: "az olmama şartı" — eşiğe eşit miktar şartı karşılar (uygulama) ----------------
dict(
konu=KONU, blok="SB55",
kalip="OLAY",
z="Z",
madde=IYN + " md. 6",
cek="İlan için sayılan miktarlardan az olmama şartı aranır; eşiğe eşit miktar (150 kilogram çay) şartı karşılar, eşiğin altındakiler karşılamaz.",
kok=[IYN + "'e göre, mahkûmiyet hükmü kesinleşmiş aşağıdaki kaçakçılık olaylarından hangisinde yakalanan eşyanın miktarı, mahkûmiyet kararının kamuoyuna ilan edilmesi için aranan şartı karşılar?"],
d="150 kilogram çay",
c=["45 baş canlı hayvan", "240 kilogram zeytin", "450 kilogram şeker", "4.900 paket sigara"],
sirali=True,
siklar=["45 baş canlı hayvan", "150 kilogram çay", "240 kilogram zeytin", "450 kilogram şeker", "4.900 paket sigara"],
g="Yönetmeliğe göre mahkûmiyet kararının kamuoyuna ilan edilmesi için eşya türüne göre belirlenen miktarlardan az olmama şartı aranır. Çay için sınır 150 kilogramdır; 150 kilogram çay bu sınırdan az olmadığı için şartı karşılar. Sınır 'az olmama' biçiminde konduğundan eşiğe eşit miktar yeterlidir, eşiği aşmak gerekmez. Diğer olaylarda miktarlar eşiğin hemen altındadır: canlı hayvanda sınır 50 baş, zeytinde 250 kilogram, şekerde 500 kilogram, sigarada 5.000 pakettir. En güçlü tuzak, sınırın 'üzerinde olma' şeklinde okunmasıdır; bu okuma eşiğe eşit olan çayı da elerdi. Bu nedenle doğru cevap '150 kilogram çay' seçeneğidir. (MD 6)",
kanit=IY + " | Çay için 150 kilogramdan || " + IY + " | az olmama şartı aranır || "
      + IY + " | Canlı hayvan için 50 baştan || " + IY + " | Zeytin için 250 kilogramdan || "
      + IY + " | Şeker için 500 kilogramdan || " + IY + " | Sigara için 5.000 paketten",
yuva=["İlana esas miktarlar: canlı hayvan için 50 baş (45 baş eşiğin altında)",
      "İlana esas miktarlar: zeytin için 250 kilogram (240 kilogram eşiğin altında)",
      "İlana esas miktarlar: şeker için 500 kilogram (450 kilogram eşiğin altında)",
      "İlana esas miktarlar: sigara için 5.000 paket (4.900 paket eşiğin altında)"],
yakinlik="ÇIKARIM",
tuzak=["YAKIN-SAYI", "İSTİSNA"], duzey=["UYGULAMA"], profil=[2],
olumsuz=False, vaka=True, baslangic=False, eksen=0, ayna="", guncellik="",
cikmis="", kapsamli=False,
),

# 6 ---------------- İlan Yön. md. 6/1-ı, 6/2: 500.000 TL ve Hazine ve Maliye Bakanlığı — boşluk ----------------
dict(
konu=KONU, blok="SB55",
kalip="BOŞLUK",
z="O",
madde=IYN + " md. 6",
cek="Diğer eşya türlerinde gümrüklenmiş değerin 500.000 TL'den az olmaması aranır; tutar her yıl Hazine ve Maliye Bakanlığınca belirlenen yeniden değerleme oranında artar.",
kok=[IYN + "'te ilana esas olacak miktar veya değerlere ilişkin olarak aşağıdaki düzenleme yer almaktadır:",
     "\"Kaçakçılık fiiline konu mahkûmiyet kararının kamuoyuna ilan edilmesi için diğer eşya türlerinde gümrüklenmiş değerin (……) Türk Lirasından az olmaması şartı aranır. Bu tutar, her yıl (……) belirlenen yeniden değerleme oranında artırılır.\"",
     "Yukarıdaki boşluklara sırasıyla aşağıdakilerden hangisi gelmelidir?"],
d="500.000 – Hazine ve Maliye Bakanlığınca",
c=["250.000 – Hazine ve Maliye Bakanlığınca", "250.000 – Ticaret Bakanlığınca",
   "500.000 – Gümrükler Muhafaza Genel Müdürlüğünce", "500.000 – Ticaret Bakanlığınca"],
sirali=True,
siklar=["250.000 – Hazine ve Maliye Bakanlığınca", "250.000 – Ticaret Bakanlığınca",
        "500.000 – Gümrükler Muhafaza Genel Müdürlüğünce", "500.000 – Hazine ve Maliye Bakanlığınca",
        "500.000 – Ticaret Bakanlığınca"],
g="Yönetmeliğe göre akaryakıt, sigara, tütün, alkollü içki, canlı hayvan, et, çay, şeker, zeytin ve zeytinyağı dışında kalan diğer eşya türlerinde ilan için gümrüklenmiş değerin 500.000 Türk Lirasından az olmaması şartı aranır. Bu tutar her yıl Hazine ve Maliye Bakanlığınca belirlenen yeniden değerleme oranında artırılır. Tutar 10.04.2019 tarihli değişiklikle 250.000 Türk Lirasından 500.000 Türk Lirasına çıkarılmış, aynı değişiklikle 'Maliye Bakanlığınca' ibaresi 'Hazine ve Maliye Bakanlığınca' olarak değiştirilmiştir. Ticaret Bakanlığı Yönetmelikte ilanı yapan Bakanlıktır; Gümrükler Muhafaza Genel Müdürlüğü ise ilan edileceklere dair kararı veren ve yayım süresini artırabilen birimdir, yeniden değerleme oranını belirlemez. En güçlü çeldirici eski tutar olan 250.000 Türk Lirasıdır. Bu nedenle doğru cevap '500.000 – Hazine ve Maliye Bakanlığınca' seçeneğidir. (MD 6)",
kanit=IY + " | Diğer eşya türleri için gümrüklenmiş değerinin 500.000 || "
      + IY + " | gümrüklenmiş değer tutarı, her yıl Hazine ve Maliye Bakanlığınca … belirlenen yeniden değerleme oranında artırılır || "
      + IY + ' | "250.000" ibaresi "500.000" olarak 10.04.2019 / 30741 RG ile değiştirilmiştir || '
      + IY + ' | ibaresi "Hazine ve Maliye Bakanlığınca" şeklinde 10.04.2019 / 30741 RG ile değiştirilmiştir',
yuva=["Tutarın eski hâli: 10.04.2019 öncesi 250.000 TL; makam doğru",
      "Tutarın eski hâli (250.000 TL) ile Yönetmelikte 'Bakanlık' olarak tanımlanan Ticaret Bakanlığı",
      "İlan kararını veren ve yayım süresini artıran Genel Müdürlük (Gümrükler Muhafaza Genel Müdürlüğü)",
      "Yönetmelikte 'Bakanlık' tanımı: Ticaret Bakanlığı (ilanı yapan Bakanlık)"],
yakinlik="BİREBİR",
tuzak=["YAKIN-SAYI", "MAKAM"], duzey=["HATIRLAMA"], profil=[2, 1],
olumsuz=False, vaka=False, baslangic=False, eksen=0, ayna="", guncellik="",
cikmis="", kapsamli=False,
),

# 7 ---------------- İlan Yön. md. 6/3 (↔ md. 4/1): miktar/değer aranmaksızın ilan listesi — hayali ihracat yok ----------------
dict(
konu=KONU, blok="SB55",
kalip="KAPSAM_DIŞI",
z="Z",
madde=IYN + " md. 4, 6",
cek="Göçmen, tarihi eser, sahte para, maden kaçakçılığı miktar ve değere bakılmaksızın ilan edilebilir; hayali ihracat ilan kapsamında olup bu listede değildir.",
kok=[IYN + "'e göre, aşağıdaki kaçakçılık fiillerinden hangisi miktar veya eşyanın gümrüklenmiş değerine bakılmaksızın kamuoyuna ilan edilebilecek fiiller arasında yer almaz?"],
d="Hayali ihracat",
c=["Göçmen kaçakçılığı", "Tarihi eser kaçakçılığı", "Sahte para kaçakçılığı", "Maden kaçakçılığı"],
sirali=False,
g="Yönetmeliğe göre genetiği değiştirilmiş organizmalı ürünler, radyoaktif ve kimyasal maddeler, çevre veya toplum sağlığını tehdit eden ürünler, fikri ve sınai mülkiyet hakları, nesli tükenmekte olan yabani hayvan ve bitki türleri, tarihi eser, uyuşturucu ile silah ve mühimmat, sahte para, altın, maden kaçakçılığı ve göçmen kaçakçılığı fiilleri, miktar veya eşyanın gümrüklenmiş değerine bakılmaksızın kamuoyuna ilan edilebilir. Hayali ihracat bu listede yer almaz. Tuzak şudur: hayali ihracat, mahkûmiyet hükmü kesinleşenlerin ilan edilebileceği fiiller listesinde sayılmıştır; ancak miktar veya değerden bağımsız ilan listesine alınmamıştır. Bu nedenle hayali ihracatta ilan için diğer eşya türlerine ilişkin gümrüklenmiş değer şartı aranır. Ağır bir fiil olduğu için sağduyuyla bu listeye eklenmesi, aranan şartı göz ardı ettirir. Bu nedenle doğru cevap 'Hayali ihracat' seçeneğidir. (MD 4, 6)",
kanit=IY + " | tarihi eser, uyuşturucu ile silah ve mühimmat, sahte para, altın, maden kaçakçılığı ve göçmen kaçakçılığı fiilleri, miktar veya eşyanın gümrüklenmiş değerine bakılmaksızın kamuoyuna ilan edilebilir || "
      + IY + " | maden kaçakçılığı, hayali ihracat, göçmen kaçakçılığı fiillerinden mahkûmiyet hükmü kesinleşenler",
yuva=["Miktar veya değere bakılmaksızın ilan listesi: göçmen kaçakçılığı (listede)",
      "Miktar veya değere bakılmaksızın ilan listesi: tarihi eser (listede)",
      "Miktar veya değere bakılmaksızın ilan listesi: sahte para (listede)",
      "Miktar veya değere bakılmaksızın ilan listesi: maden kaçakçılığı (listede)"],
yakinlik="BİREBİR",
tuzak=["LİSTE-DIŞI", "KOMŞU", "SAĞDUYU"], duzey=["AYIRT"], profil=[3, 1],
olumsuz=True, vaka=False, baslangic=False, eksen=0, ayna="", guncellik="",
cikmis="", kapsamli=False,
),

# 8 ---------------- İlan Yön. md. 7: yayım süresi, artırım, diğer vasıtalar, ilan içeriği — önermeli ----------------
dict(
konu=KONU, blok="SB55",
kalip="ÖNERMELİ",
z="Z",
madde=IYN + " md. 7",
cek="Bilgiler üç ay internet sitesinde yayımlanır; süre Genel Müdürlükçe bir katına kadar artırılabilir; diğer vasıtalarla duyuru şarta bağlı değildir.",
kok=[IYN + "'in ilanın yayımlanmasına ve ilan metninde belirtilecek hususlara ilişkin hükümleri çerçevesinde aşağıdaki ifadeler veriliyor:",
     "I. Suçun mahiyetine göre yayımlanma süresi, Genel Müdürlükçe üç katına kadar artırılabilir.",
     "II. Kamuoyuna ilan edilecek kaçakçılık suçları ve hükümlülerine ilişkin bilgiler üç ay süre ile Bakanlık resmî internet sitesinde yayımlanır.",
     "III. Bilgilerin diğer iletişim vasıtalarıyla kamuoyuna duyurulabilmesi, Komisyon kararında yer alması şartına bağlıdır.",
     "IV. İlan edilecek bilgilerin içeriğinde, kaçakçılık olayına dair yakalanan eşyanın cinsi ve miktarına ilişkin bilgiler yer alır.",
     "Yukarıdaki ifadelerden hangileri doğrudur?"],
d="II ve IV",
c=["I ve II", "I ve III", "II ve III", "I, II ve IV"],
sirali=False,
g="Yönetmeliğe göre kamuoyuna ilan edilecek kaçakçılık suçları ve hükümlülerine ilişkin bilgiler üç ay süre ile Bakanlık resmî internet sitesinde yayımlanır (II doğru). İlan metninde kaçakçılık olayına dair yakalanan eşyanın cinsi ve miktarına ilişkin bilgiler; mahkûm olanların adı soyadı, baba adı, doğum tarihi, doğum yeri ve mesleği; yayımlanma süresi ve gerekli görülen diğer hususlar yer alır (IV doğru). Suçun mahiyetine göre üç aylık süre Genel Müdürlükçe üç katına değil bir katına kadar artırılabilir; yani süre en fazla altı aya çıkar (I yanlış). Bilgiler diğer iletişim vasıtalarıyla da duyurulabilir ve bu bir şarta bağlı değildir; 'Komisyon kararında yer alması şartıyla' kaydı, Komisyon kaldırıldığında 10.04.2019 tarihli değişiklikle metinden çıkarılmıştır (III yanlış). En güçlü tuzak III'tür; eski metinden çalışan aday bu önermeyi doğru sanır. Bu nedenle doğru cevap 'II ve IV' seçeneğidir. (MD 7)",
kanit=IY + " | kaçakçılık suçları ve hükümlülerine ilişkin bilgiler üç ay süre ile Bakanlık resmî internet sitesinde yayımlanır || "
      + IY + " | Suçun mahiyetine göre birinci fıkradaki süre, Genel Müdürlükçe bir katına kadar artırılabilir || "
      + IY + " | Kaçakçılık suçları ve hükümlülerine ilişkin bilgiler diğer iletişim vasıtalarıyla da kamuoyuna duyurulabilir || "
      + IY + " | Komisyon kararında yer alması şartıyla || "
      + IY + " | Kaçakçılık olayına dair yakalanan eşyanın cinsi ve miktarına ilişkin bilgiler",
yuva=["I ve II: I'deki 'üç katına' ifadesi hükümde 'bir katına'dır",
      "I ve III: III, 10.04.2019 öncesindeki 'Komisyon kararında yer alması şartıyla' kaydıdır",
      "II ve III: II doğru; III mülga Komisyon şartı",
      "I, II ve IV: I'deki artırım sınırı yanlış (bir katı yerine üç katı)"],
yakinlik="BİREBİR",
tuzak=["SAYI", "ŞART", "KOMŞU"], duzey=["AYIRT"], profil=[2, 1],
olumsuz=False, vaka=False, baslangic=False, eksen=0, ayna="", guncellik="",
cikmis="", kapsamli=False,
),

# 9 ---------------- İlan Yön. md. 7/4-b: hükümlü bilgileri — anne adı sayılmamış ----------------
dict(
konu=KONU, blok="SB55",
kalip="KAPSAM_DIŞI",
z="O",
madde=IYN + " md. 7",
cek="İlan metninde hükümlünün adı soyadı, baba adı, doğum tarihi, doğum yeri ve mesleği yer alır; anne adı sayılmamıştır.",
kok=[IYN + "'e göre, kamuoyuna ilan edilecek bilgilerin içeriğinde kaçakçılık suçundan mahkûm olanlara ilişkin olarak yer alacak bilgiler arasında aşağıdakilerden hangisi sayılmamıştır?"],
d="Anne adı",
c=["Baba adı", "Doğum yeri", "Doğum tarihi", "Mesleği"],
sirali=False,
g="Yönetmeliğe göre kamuoyuna ilan edilecek kaçakçılık suçları ve hükümlülerine ilişkin bilgilerin içeriğinde, kaçakçılık suçundan mahkûm olanların adı soyadı, baba adı, doğum tarihi, doğum yeri ve mesleği yer alır. Anne adı bu bilgiler arasında sayılmamıştır. Kimlik bilgisi denince akla birlikte gelen anne ve baba adından yalnızca baba adı sayılmıştır; aday sağduyuyla anne adını da ekleyebilir. Hükümlünün mesleğinin de ilan metninde yer alması, adayın dışarıda bırakabileceği bir unsurdur. Bu nedenle doğru cevap 'Anne adı' seçeneğidir. (MD 7)",
kanit=IY + " | Kaçakçılık suçundan mahkûm olanların adı soyadı, baba adı, doğum tarihi, doğum yeri ve mesleği",
yuva=["İlan içeriği, hükümlü bilgileri: baba adı (sayılmış)",
      "İlan içeriği, hükümlü bilgileri: doğum yeri (sayılmış)",
      "İlan içeriği, hükümlü bilgileri: doğum tarihi (sayılmış)",
      "İlan içeriği, hükümlü bilgileri: mesleği (sayılmış)"],
yakinlik="BİREBİR",
tuzak=["LİSTE-DIŞI", "UNSUR", "SAĞDUYU"], duzey=["TANIMA"], profil=[3, 4],
olumsuz=True, vaka=False, baslangic=False, eksen=0, ayna="", guncellik="",
cikmis="", kapsamli=False,
),

# 10 ---------------- Her iki Yönetmeliğin dayanağı: 5607 ↔ 6136 (2021/99 alanı) ----------------
dict(
konu=KONU, blok="SB55",
kalip="DAYANAK",
z="O",
madde=IYN + " md. 2; " + TYN + " md. 2",
cek="İlan Yönetmeliği 5607 sayılı Kaçakçılıkla Mücadele Kanunu'na, silah ve mühimmat tahsisi Yönetmeliği 6136 sayılı Kanun'a dayanır.",
kok=[IYN + " ile " + TYN + "'in dayanağını oluşturan kanunlar sırasıyla aşağıdakilerden hangisinde doğru olarak verilmiştir?"],
d="5607 sayılı Kaçakçılıkla Mücadele Kanunu – 6136 sayılı Ateşli Silahlar ve Bıçaklar ile Diğer Aletler Hakkında Kanun",
c=["5607 sayılı Kaçakçılıkla Mücadele Kanunu – 5607 sayılı Kaçakçılıkla Mücadele Kanunu",
   "6136 sayılı Ateşli Silahlar ve Bıçaklar ile Diğer Aletler Hakkında Kanun – 5607 sayılı Kaçakçılıkla Mücadele Kanunu",
   "4458 sayılı Gümrük Kanunu – 6136 sayılı Ateşli Silahlar ve Bıçaklar ile Diğer Aletler Hakkında Kanun",
   "4458 sayılı Gümrük Kanunu – 5607 sayılı Kaçakçılıkla Mücadele Kanunu"],
sirali=False,
g="Kaçakçılık türleri ile ilgili mahkûmiyet hükmü kesinleşenlerin kamuoyuna ilan edilmesine dair Yönetmelik, 5607 sayılı Kaçakçılıkla Mücadele Kanunu'nun nitelikli hâlleri düzenleyen ve ilan yetkisini veren hükmüne dayanılarak hazırlanmıştır. Millî savunma veya iç güvenlik hizmetleriyle doğrudan ilgili silah, mühimmat, araç ve gereç ile sarf malzemesinin tahsisine ilişkin Yönetmelik ise 6136 sayılı Ateşli Silahlar ve Bıçaklar ile Diğer Aletler Hakkında Kanun'a dayanır. En güçlü çeldirici iki Yönetmeliği de 5607 sayılı Kanun'a bağlayan seçenektir: tahsis Yönetmeliği, 5607 sayılı Kanun kapsamındaki suçlar sebebiyle el konulan eşyayı da kapsadığı için bu Kanun'a dayandığı sanılır; oysa kapsamındaki suçlar ile dayanak kanun ayrı şeylerdir. Gümrük Kanunu ise iki Yönetmeliğin de dayanağı değildir. Bu nedenle doğru cevap '5607 sayılı Kaçakçılıkla Mücadele Kanunu – 6136 sayılı Ateşli Silahlar ve Bıçaklar ile Diğer Aletler Hakkında Kanun' seçeneğidir. (MD İlan Yön. 2; Tahsis Yön. 1, 2)",
kanit=IY + " | Bu Yönetmelik, 21/3/2007 tarihli ve 5607 sayılı Kaçakçılıkla Mücadele Kanununun 4 üncü maddesine dayanılarak hazırlanmıştır || "
      + TY + " | Bu Yönetmelik, 10/7/1953 tarihli ve 6136 sayılı Ateşli Silahlar ve Bıçaklar ile Diğer Aletler Hakkında Kanunun Ek 12 nci maddesine dayanılarak hazırlanmıştır || "
      + TY + " | sayılı Kaçakçılıkla Mücadele Kanunu kapsamındaki suçlar sebebiyle el konulan veya adli emanette bulunan",
yuva=["Tahsis Yönetmeliğinin kapsamı: 5607 sayılı Kanun kapsamındaki suçlar sebebiyle el konulan eşya (dayanak değil kapsam)",
      "İki Yönetmeliğin dayanakları yer değiştirilmiş (ayna)",
      "Gümrük Kanunu: ilan Yönetmeliğini çıkaran eski Gümrük ve Ticaret Bakanlığının temel kanunu; dayanak değil",
      "Gümrük Kanunu ile tahsis Yönetmeliğinin kapsamındaki 5607 sayılı Kanun"],
yakinlik="BİREBİR",
tuzak=["KOMŞU", "TERİM"], duzey=["AYIRT"], profil=[1],
olumsuz=False, vaka=False, baslangic=False, eksen=0, ayna="DAYANAK: ilan 5607 ↔ tahsis 6136", guncellik="",
cikmis="2021/99", kapsamli=False,
),

# 11 ---------------- Tahsis Yön. md. 1: tahsis edilebilecek kurumlar — Gümrükler Muhafaza yok ----------------
dict(
konu=KONU, blok="SB55",
kalip="KAPSAM_DIŞI",
z="O",
madde=TYN + " md. 1",
cek="El konulan veya adli emanetteki silah, mühimmat, araç-gereç ve sarf malzemesi TSK, EGM, JGK veya Sahil Güvenlik Komutanlığına tahsis edilir.",
kok=[TYN + "'e göre, terör veya örgüt faaliyeti çerçevesinde işlenen ya da 5607 sayılı Kaçakçılıkla Mücadele Kanunu kapsamındaki suçlar sebebiyle el konulan veya adli emanette bulunan eşyanın tahsis edilebileceği kuruluşlar arasında aşağıdakilerden hangisi yer almaz?"],
d="Gümrükler Muhafaza Genel Müdürlüğü",
c=["Türk Silahlı Kuvvetleri", "Emniyet Genel Müdürlüğü", "Jandarma Genel Komutanlığı", "Sahil Güvenlik Komutanlığı"],
sirali=False,
g="Yönetmelik, terör veya örgüt faaliyeti çerçevesinde işlenen ya da 5607 sayılı Kaçakçılıkla Mücadele Kanunu kapsamındaki suçlar sebebiyle el konulan veya adli emanette bulunan, millî savunma veya iç güvenlik hizmetleriyle doğrudan ilgili silah, mühimmat, araç ve gereç ile sarf malzemesinin Türk Silahlı Kuvvetleri, Emniyet Genel Müdürlüğü, Jandarma Genel Komutanlığı veya Sahil Güvenlik Komutanlığına tahsis edilmesine ilişkin usul ve esasları kapsar. Gümrükler Muhafaza Genel Müdürlüğü bu kurumlar arasında sayılmamıştır. Tuzak şudur: kaçakçılıkla mücadelede görevli olduğu ve kaçakçılık mahkûmiyetlerinin ilanına ilişkin kararı veren Genel Müdürlük olduğu için gümrük teşkilatının da tahsisten yararlanacağı sanılabilir; oysa tahsis yalnızca sayılan dört kuruluşa yapılır. Yönetmelikte 'Kurumlar' terimi ise bu merkez teşkilatlarını değil il garnizon komutanlığı, emniyet müdürlüğü, jandarma komutanlığı ve sahil güvenlik komutanlığını ifade eder. Bu nedenle doğru cevap 'Gümrükler Muhafaza Genel Müdürlüğü' seçeneğidir. (MD 1)",
kanit=TY + " | Türk Silahlı Kuvvetleri, Emniyet Genel Müdürlüğü, Jandarma Genel Komutanlığı veya Sahil Güvenlik Komutanlığına tahsis edilmesi || "
      + IY + " | Genel Müdürlük: Gümrükler Muhafaza Genel Müdürlüğünü",
yuva=["Kapsam hükmü: Türk Silahlı Kuvvetleri (tahsis edilebilir)",
      "Kapsam hükmü: Emniyet Genel Müdürlüğü (tahsis edilebilir)",
      "Kapsam hükmü: Jandarma Genel Komutanlığı (tahsis edilebilir)",
      "Kapsam hükmü: Sahil Güvenlik Komutanlığı (tahsis edilebilir)"],
yakinlik="BİREBİR",
tuzak=["LİSTE-DIŞI", "SAĞDUYU", "KOMŞU"], duzey=["TANIMA"], profil=[3],
olumsuz=True, vaka=False, baslangic=False, eksen=0, ayna="KURUM: tahsis edilen merkez kurumlar ↔ 'Kurumlar' tanımındaki il birimleri", guncellik="",
cikmis="", kapsamli=False,
),

# 12 ---------------- Tahsis Yön. md. 3: sarf malzemesi — tanımdan ad ----------------
dict(
konu=KONU, blok="SB55",
kalip="TANIM",
z="K",
madde=TYN + " md. 3",
cek="Belirli bir hizmetin üretiminde kullanılan, kullanımıyla tükenen veya özelliğini kaybederek kullanılamaz hâle gelen malzeme sarf malzemesidir.",
kok=[TYN + "'te \"belirli bir hizmetin üretilmesinde kullanılan, kullanımı sonucunda tükenen veya bir süre kullanıldıktan sonra ilk özelliklerini kısmen veya tamamen kaybederek bir daha kullanılamayacak duruma gelen malzemeler\" şeklinde tanımlanan kavram aşağıdakilerden hangisidir?"],
d="Sarf malzemesi",
c=["Mühimmat", "Araç ve gereç", "Eşya", "Silah"],
sirali=False,
g="Yönetmelikte sarf malzemesi; belirli bir hizmetin üretilmesinde kullanılan, kullanımı sonucunda tükenen veya bir süre kullanıldıktan sonra ilk özelliklerini kısmen veya tamamen kaybederek bir daha kullanılamayacak duruma gelen malzemeler olarak tanımlanmıştır. Mühimmat; ateşli silahlarda kullanılan fişek kovanı, falya, barut tozu, kurşun veya mermiler dâhil cephanenin kendisi veya bunu meydana getiren unsurlar ile her türlü patlayıcı maddedir. Araç ve gereç; nakil vasıtaları, silaha ait yedek parça ve bakım malzemeleri, dürbün, insansız hava aracı, gece görüş sistemleri, haberleşmeyi sağlayan ve engelleyen cihazlar gibi her türlü malzemedir. Eşya ise Yönetmelik kapsamındaki silah, mühimmat, araç ve gereç ile sarf malzemesinin hepsini ifade eden üst kavramdır. En güçlü çeldirici mühimmattır: kullanıldıkça tükendiği için sarf malzemesiyle karıştırılır, fakat ayrı ve kapalı bir tanımı vardır. Bu nedenle doğru cevap 'Sarf malzemesi' seçeneğidir. (MD 3)",
kanit=TY + " | Sarf malzemesi: Belirli bir hizmetin üretilmesinde kullanılan, kullanımı sonucunda tükenen veya bir süre kullanıldıktan sonra ilk özelliklerini kısmen veya tamamen kaybederek bir daha kullanılamayacak duruma gelen malzemeleri || "
      + TY + " | Eşya: Bu Yönetmelik kapsamındaki silah, mühimmat, araç ve gereç ile sarf malzemesini",
yuva=["Tanımlar: mühimmat (cephane ve unsurları ile patlayıcı madde)",
      "Tanımlar: araç ve gereç (nakil vasıtaları, yedek parça, dürbün, insansız hava aracı vb.)",
      "Tanımlar: eşya (Yönetmelik kapsamındaki tüm malzemeyi kapsayan üst kavram)",
      "Tanımlar: silah (canlıları öldürebilen, yaralayan, etkisiz hâle getiren ateşli veya ateşsiz silahlar)"],
yakinlik="BİREBİR",
tuzak=["TERİM", "KOMŞU"], duzey=["TANIMA"], profil=[1],
olumsuz=False, vaka=False, baslangic=False, eksen=0, ayna="", guncellik="",
cikmis="", kapsamli=False,
),

# 13 ---------------- Tahsis Yön. md. 3 (↔ md. 1, 6, 13): "Kurumlar" — addan tanım ----------------
dict(
konu=KONU, blok="SB55",
kalip="KAVRAM",
z="Z",
madde=TYN + " md. 1, 3",
cek="Yönetmelikte 'Kurumlar' il garnizon komutanlığı, emniyet müdürlüğü, jandarma komutanlığı ve sahil güvenlik komutanlığıdır; merkez teşkilatları değildir.",
kok=[TYN + "'te geçen \"Kurumlar\" ifadesi aşağıdakilerden hangisini ifade eder?"],
d="İl garnizon komutanlığı, emniyet müdürlüğü, jandarma komutanlığı ve sahil güvenlik komutanlığı",
c=["Türk Silahlı Kuvvetleri, Emniyet Genel Müdürlüğü, Jandarma Genel Komutanlığı ve Sahil Güvenlik Komutanlığı",
   "Adalet, İçişleri, Millî Savunma ve Maliye Bakanlıkları",
   "İl valisi, garnizon komutanı, emniyet müdürü, jandarma komutanı, sahil güvenlik komutanı ve sorumlu vali yardımcısı",
   "Valilik, il jandarma komutanlığı ve Cumhuriyet başsavcılığı"],
sirali=False,
g="Yönetmelikte Kurumlar; il garnizon komutanlığı, emniyet müdürlüğü, jandarma komutanlığı ve sahil güvenlik komutanlığı olarak tanımlanmıştır. Güncel listeler bu il birimlerine bildirilir ve tahsis taleplerini bu birimler Komisyona iletir. Türk Silahlı Kuvvetleri, Emniyet Genel Müdürlüğü, Jandarma Genel Komutanlığı ve Sahil Güvenlik Komutanlığı ise Yönetmeliğin kapsam hükmünde eşyanın tahsis edileceği merkez teşkilatlar olarak sayılmıştır; 'Kurumlar' tanımı değildir. Adalet, İçişleri, Millî Savunma ve Maliye Bakanlıkları Yönetmeliği birlikte yürüten bakanlıklardır. İl valisi başkanlığında garnizon komutanı, emniyet müdürü, jandarma komutanı, sahil güvenlik komutanı ve sorumlu vali yardımcısından oluşan yapı tahsis komisyonudur. Valilik, il jandarma komutanlığı ve Cumhuriyet başsavcılığı ise listelerin bildirimi ve tahsis talebinin iletilmesi sürecinde görev alan makamlardır. En güçlü çeldirici merkez teşkilatlarını sayan seçenektir. Bu nedenle doğru cevap 'İl garnizon komutanlığı, emniyet müdürlüğü, jandarma komutanlığı ve sahil güvenlik komutanlığı' seçeneğidir. (MD 1, 3, 6, 13)",
kanit=TY + " | Kurumlar: İl garnizon komutanlığı, emniyet müdürlüğü, jandarma komutanlığı ve sahil güvenlik komutanlığını || "
      + TY + " | Türk Silahlı Kuvvetleri, Emniyet Genel Müdürlüğü, Jandarma Genel Komutanlığı veya Sahil Güvenlik Komutanlığına tahsis edilmesi || "
      + TY + " | Bu Yönetmelik hükümlerini Adalet, İçişleri, Milli Savunma ve Maliye Bakanları birlikte yürütür || "
      + TY + " | İl valisinin başkanlığında, garnizon komutanı, emniyet müdürü, jandarma komutanı, sahil güvenlik komutanı ve sorumlu vali yardımcısından oluşan tahsis komisyonu kurulur",
yuva=["Kapsam hükmü: eşyanın tahsis edileceği merkez teşkilatlar",
      "Yürütme hükmü ve Yönetmeliği çıkaran bakanlıklar",
      "Tahsis komisyonunun oluşumu",
      "Listelerin valilik kanalıyla il jandarma komutanlığınca bildirimi; tahsis talebinin Cumhuriyet başsavcılığı aracılığıyla yapılması"],
yakinlik="BİREBİR",
tuzak=["TERİM", "KOMŞU"], duzey=["AYIRT"], profil=[1],
olumsuz=False, vaka=False, baslangic=False, eksen=0, ayna="KURUM: tahsis edilen merkez kurumlar ↔ 'Kurumlar' tanımındaki il birimleri", guncellik="",
cikmis="", kapsamli=False,
),

# 14 ---------------- Tahsis Yön. md. 4: kriminal inceleme vb. işlemler — ele geçirmeden itibaren 15 gün ----------------
dict(
konu=KONU, blok="SB55",
kalip="SÜRE",
z="O",
madde=TYN + " md. 4",
cek="Tahsise konu olabilecek eşyada kriminal inceleme, bilirkişi raporu, durum tespiti gibi işlemler zorunlu hâller hariç ele geçirmeden itibaren 15 günde yapılır.",
kok=[TYN + "'e göre, tahsise konu olabilecek nitelikteki eşya hakkında kriminal inceleme, bilirkişi raporu veya durum tespiti gibi yargılama için yapılması gerekli olduğu değerlendirilen işlemler, zorunlu hâller haricinde ne kadar süre içinde yerine getirilir?"],
d="Ele geçirme tarihinden itibaren 15 gün içinde",
c=["Ele geçirme tarihinden itibaren 5 gün içinde",
   "Ele geçirme tarihinden itibaren 3 iş günü içinde",
   "Güncel listelerin kurumlara bildirildiği tarihten itibaren 15 gün içinde",
   "Tahsis talebinin Komisyona ulaştığı tarihten itibaren 15 gün içinde"],
sirali=False,
g="Yönetmeliğe göre tahsise konu olabilecek nitelikteki eşya hakkındaki kriminal inceleme, bilirkişi raporu veya durum tespiti gibi yargılama için yapılması gerekli olduğu değerlendirilen işlemler, ele geçirme tarihinden itibaren, zorunlu hâller haricinde, 15 gün içerisinde yerine getirilir. Süre listelerin bildiriminden veya tahsis talebinden değil eşyanın ele geçirildiği tarihten başlar; çünkü bu işlemler eşyanın tahsise hazır hâle gelmesinden önce tamamlanmalıdır. 5 gün, Yönetmeliğin yürürlüğe girmesinden itibaren ilk listelerin bildirilmesi için öngörülen geçiş süresidir. 3 iş günü ise kurumların tahsis taleplerini listelerin bildirim tarihini müteakip Komisyona iletme süresi ve çok sayıda eşya ele geçirildiğinde Komisyonun karar süresidir. En güçlü çeldiriciler süreyi doğru verip başlangıç anını değiştiren seçeneklerdir. Bu nedenle doğru cevap 'Ele geçirme tarihinden itibaren 15 gün içinde' seçeneğidir. (MD 4, 5, Geçici 1)",
kanit=TY + " | ele geçirme tarihinden itibaren, zorunlu haller haricinde, 15 gün içerisinde yerine getirilir || "
      + TY + " | Bu Yönetmeliğin yürürlüğe girmesinden itibaren en geç 5 gün içinde || "
      + TY + " | Kurumlar tarafından tahsis talepleri bildirim tarihini müteakip 3 iş günü içerisinde Komisyona iletilir",
yuva=["Geçiş hükmü: yürürlükten itibaren en geç 5 gün içinde ilk listelerin bildirimi",
      "Listelerin bildiriminden itibaren 3 iş günü (kurumların talep iletme süresi) ve çok sayıda eşyada Komisyonun 3 iş günlük karar süresi",
      "Listelerin ayda bir bildirimi ve bildirim tarihine bağlanan talep süresi (başlangıç anı kaydırılmış)",
      "Tahsis talebinin Komisyona ulaşmasına bağlanan karar süreleri (başlangıç anı kaydırılmış)"],
yakinlik="BİREBİR",
tuzak=["BAŞLANGIÇ", "SAYI", "KOMŞU"], duzey=["AYIRT"], profil=[2, 1],
olumsuz=False, vaka=False, baslangic=True, eksen=0, ayna="", guncellik="",
cikmis="", kapsamli=False,
),

# 15 ---------------- Tahsis Yön. md. 5/2 (↔ 6/3, 5/1): çok sayıda eşyada 3 iş günü, talebin ulaşmasından sonra ----------------
dict(
konu=KONU, blok="SB55",
kalip="SÜRE",
z="Z",
madde=TYN + " md. 5, 6",
cek="Çok sayıda eşya ele geçirilip listeler ivedilikle güncellendiğinde Komisyon, talep kendisine ulaştıktan sonra en geç 3 iş günü içinde toplanıp karar verir.",
kok=[TYN + "'e göre, bir seferde veya olayda çok sayıda eşya ele geçirilmesi ve bu eşyalara Kurumlarca ihtiyaç duyulması üzerine ivedilikle güncellenen listelere istinaden yapılan tahsis talebi hakkında Komisyonun en geç toplanıp karar vermesi gereken süre ve bu sürenin başlangıcı aşağıdakilerden hangisidir?"],
d="3 iş günü – talebin Komisyona ulaşmasından sonra",
c=["3 iş günü – listelerin kurumlara bildirildiği tarihten itibaren",
   "5 iş günü – talebin Komisyona ulaşmasından sonra",
   "5 iş günü – listelerin kurumlara bildirildiği tarihten itibaren",
   "15 gün – eşyanın ele geçirildiği tarihten itibaren"],
sirali=True,
siklar=["3 iş günü – listelerin kurumlara bildirildiği tarihten itibaren",
        "3 iş günü – talebin Komisyona ulaşmasından sonra",
        "5 iş günü – talebin Komisyona ulaşmasından sonra",
        "5 iş günü – listelerin kurumlara bildirildiği tarihten itibaren",
        "15 gün – eşyanın ele geçirildiği tarihten itibaren"],
g="Yönetmeliğe göre bir seferde veya olayda çok sayıda eşya ele geçirilmesi ve bu eşyalara Kurumlarca ihtiyaç duyulması durumunda listeler ivedilikle güncellenip kurumlara bildirilir; bu bildirime istinaden yapılan tahsis talebi Komisyona ulaştıktan sonra en geç 3 iş günü içinde Komisyon toplanır ve karar verir. Genel kural farklıdır: güncel listede yer alan eşyayla ilgili talepler Komisyona ulaştıktan sonra Komisyon en geç 5 iş günü içinde toplanır ve karar verir; ihtiyaç hâlinde gecikmeksizin derhal toplanır. Listelerin bildirim tarihini müteakip işleyen 3 iş günü ise kurumların taleplerini Komisyona iletme süresidir; Komisyonun karar süresi değildir. 15 gün, kriminal inceleme ve bilirkişi raporu gibi işlemlerin ele geçirme tarihinden itibaren tamamlanma süresidir. En güçlü çeldirici genel kuraldaki 5 iş günüdür; soru, çok sayıda eşya ele geçirilmesine ilişkin özel hâli soruyor. Bu nedenle doğru cevap '3 iş günü – talebin Komisyona ulaşmasından sonra' seçeneğidir. (MD 4, 5, 6)",
kanit=TY + " | Bu kapsamda yapılan tahsis talebi Komisyona ulaştıktan sonra en geç 3 iş günü içinde Komisyon toplanır ve karar verir || "
      + TY + " | Listede yer alan eşyayla ilgili talepler Komisyona ulaştıktan sonra en geç 5 iş günü içinde Komisyon toplanır ve karar verir || "
      + TY + " | Kurumlar tarafından tahsis talepleri bildirim tarihini müteakip 3 iş günü içerisinde Komisyona iletilir || "
      + TY + " | ele geçirme tarihinden itibaren, zorunlu haller haricinde, 15 gün içerisinde yerine getirilir",
yuva=["Kurumların tahsis taleplerini liste bildirim tarihini müteakip 3 iş günü içinde Komisyona iletmesi (iletme süresi, karar süresi değil)",
      "Genel kural: listede yer alan eşyaya ilişkin talepte Komisyon talebin ulaşmasından sonra en geç 5 iş günü içinde karar verir",
      "Genel kuraldaki 5 iş günü ile kurumların talep iletme süresinin başlangıcı (liste bildirimi) birleştirilmiş",
      "Kriminal inceleme, bilirkişi raporu gibi işlemlerin ele geçirme tarihinden itibaren 15 günlük süresi"],
yakinlik="BİREBİR",
tuzak=["YAKIN-SAYI", "BAŞLANGIÇ", "İSTİSNA"], duzey=["AYIRT"], profil=[2],
olumsuz=False, vaka=False, baslangic=True, eksen=0, ayna="", guncellik="",
cikmis="", kapsamli=False,
),

# 16 ---------------- Tahsis Yön. md. 5/1 (↔ 9/2, Geçici 1): listeler ayda bir, valilik kanalıyla il jandarma ----------------
dict(
konu=KONU, blok="SB55",
kalip="YETKİ",
z="O",
madde=TYN + " md. 5",
cek="Tahsise konu olabilecek eşyanın güncel listeleri ayda bir valilik kanalıyla il jandarma komutanlığınca garnizon, emniyet ve sahil güvenliğe bildirilir.",
kok=[TYN + "'e göre, tahsise konu olabilecek eşyaya ilişkin güncel listelerin garnizon komutanlığı, emniyet müdürlüğü ve sahil güvenlik komutanlığına bildirilmesine ilişkin aşağıdakilerden hangisi doğrudur?"],
d="Listeler ayda bir valilik kanalıyla il jandarma komutanlığınca bildirilir.",
c=["Listeler üç ayda bir Jandarma Genel Komutanlığınca hazırlanarak İçişleri Bakanlığınca bildirilir.",
   "Listeler on beş günde bir il jandarma komutanlığınca bildirilir.",
   "Listeler ayda bir Cumhuriyet başsavcılığı aracılığıyla il emniyet müdürlüğünce bildirilir.",
   "Listeler eşyanın ele geçirildiği tarihten itibaren en geç 5 gün içinde il valisince bildirilir."],
sirali=False,
g="Yönetmeliğe göre tahsise konu olabilecek millî savunma veya iç güvenlik hizmetleriyle doğrudan ilgili silah, mühimmat, araç ve gereç ile sarf malzemesine ilişkin güncel listeler ayda bir valilik kanalıyla il jandarma komutanlığınca garnizon komutanlığı, emniyet müdürlüğü ve sahil güvenlik komutanlığına bildirilir. Üç ayda bir Jandarma Genel Komutanlığınca hazırlanıp İçişleri Bakanlığınca gönderilen listeler, tahsise konu olabilecek eşyanın değil tahsis edilmiş eşyanın listeleridir ve Başbakanlık, ilgili bakanlıklar, Emniyet Genel Müdürlüğü ile Sahil Güvenlik Komutanlığına gönderilir. Cumhuriyet başsavcılığı aracılığı, Valinin hâkim veya mahkemeden tahsis talebinde bulunmasına aittir. 5 günlük süre yalnızca Yönetmeliğin yürürlüğe girmesinden itibaren ilk listelerin bildirilmesi için öngörülmüş geçiş süresidir. 15 gün ise kriminal inceleme gibi işlemlerin ele geçirmeden itibaren tamamlanma süresidir, liste bildirim aralığı değildir. En güçlü çeldirici tahsis edilen eşyaya ilişkin üç aylık listedir. Bu nedenle doğru cevap 'Listeler ayda bir valilik kanalıyla il jandarma komutanlığınca bildirilir.' seçeneğidir. (MD 5, 7, 9, Geçici 1)",
kanit=TY + " | güncel listeler ayda bir valilik kanalıyla il jandarma komutanlığınca; garnizon komutanlığı, emniyet müdürlüğü ve sahil güvenlik komutanlığına bildirilir || "
      + TY + " | Tahsis edilen eşyalara ilişkin güncel listeler Jandarma Genel Komutanlığı tarafından hazırlanarak İçişleri Bakanlığınca üç ayda bir || "
      + TY + " | Bu Yönetmeliğin yürürlüğe girmesinden itibaren en geç 5 gün içinde",
yuva=["Tahsis kararının bildirilmesi: tahsis edilen eşya listeleri JGK'ca hazırlanır, İçişleri Bakanlığınca üç ayda bir gönderilir",
      "Ele geçirmeden itibaren 15 günlük kriminal inceleme süresi sıklık olarak kaydırılmış; il jandarma komutanlığı doğru",
      "Mülki amirin tahsis talebi: Vali talebini Cumhuriyet başsavcılığı aracılığıyla yapar",
      "Geçiş hükmü: yürürlükten itibaren en geç 5 gün içinde ilk listelerin bildirimi"],
yakinlik="BİREBİR",
tuzak=["MAKAM", "YAKIN-SAYI", "KOMŞU"], duzey=["AYIRT"], profil=[1, 2],
olumsuz=False, vaka=False, baslangic=False, eksen=0, ayna="", guncellik="",
cikmis="", kapsamli=False,
),

# 17 ---------------- Tahsis Yön. md. 6/1, 6/3: tahsis komisyonu — önermeli (yanlıştır) ----------------
dict(
konu=KONU, blok="SB55",
kalip="ÖNERMELİ",
z="Z",
madde=TYN + " md. 6",
cek="Komisyon vali başkanlığında kurulur, sekretaryası il jandarma komutanlığındadır, Cumhuriyet başsavcısı üye değildir; ihtiyaç hâlinde derhal toplanır.",
kok=[TYN + "'te düzenlenen tahsis komisyonuna ilişkin aşağıdaki ifadeler veriliyor:",
     "I. Komisyon, il valisinin başkanlığında kurulur.",
     "II. Cumhuriyet başsavcısı, Komisyonun üyeleri arasında yer alır.",
     "III. Komisyon sekretaryası il emniyet müdürlüğünce yürütülür.",
     "IV. Komisyon, ihtiyaç hâlinde gecikmeksizin derhal toplanır.",
     "Yukarıdaki ifadelerden hangileri yanlıştır?"],
d="II ve III",
c=["I ve II", "III ve IV", "I, II ve III", "II, III ve IV"],
sirali=False,
g="Yönetmeliğe göre tahsis komisyonu il valisinin başkanlığında; garnizon komutanı, emniyet müdürü, jandarma komutanı, sahil güvenlik komutanı ve sorumlu vali yardımcısından oluşur (I doğru). Cumhuriyet başsavcısı Komisyonun üyesi değildir; Cumhuriyet başsavcılığı, Valinin hâkim veya mahkemeden tahsis talebinde bulunurken aracı olduğu makamdır, Cumhuriyet savcısı ise tahsis kararlarına itiraz edebilir (II yanlış). Komisyon sekretaryası il emniyet müdürlüğünce değil il jandarma komutanlığınca yürütülür (III yanlış). Talepler Komisyona ulaştıktan sonra Komisyon en geç 5 iş günü içinde toplanıp karar verir ve ihtiyaç hâlinde gecikmeksizin derhal toplanır (IV doğru). Soru yanlış olanları istediği için cevap II ve III'tür. En güçlü tuzak II'dir: el konulan eşya adli emanette bulunduğundan savcılığın Komisyonda yer alacağı sanılır. Bu nedenle doğru cevap 'II ve III' seçeneğidir. (MD 6, 7, 8)",
kanit=TY + " | İl valisinin başkanlığında, garnizon komutanı, emniyet müdürü, jandarma komutanı, sahil güvenlik komutanı ve sorumlu vali yardımcısından oluşan tahsis komisyonu kurulur || "
      + TY + " | Komisyon sekretaryası il jandarma komutanlığınca yürütülür || "
      + TY + " | Komisyon ihtiyaç hâlinde gecikmeksizin derhal toplanır || "
      + TY + " | ilgili Vali tarafından derhâl hâkim veya mahkemeden Cumhuriyet başsavcılığı aracılığıyla tahsis talebinde bulunulur",
yuva=["I ve II: I doğru önerme (vali başkanlığı) yanlışlar arasına katılmış",
      "III ve IV: IV doğru önerme (derhal toplanma) yanlışlar arasına katılmış",
      "I, II ve III: I doğru önermedir",
      "II, III ve IV: IV doğru önermedir"],
yakinlik="BİREBİR",
tuzak=["KOMŞU", "MAKAM", "LİSTE-DIŞI"], duzey=["AYIRT"], profil=[4, 3],
olumsuz=True, vaka=False, baslangic=False, eksen=0, ayna="", guncellik="",
cikmis="", kapsamli=False,
),

# 18 ---------------- Tahsis Yön. md. 7, 8, 9: talep, itiraz, bildirim — önermeli ----------------
dict(
konu=KONU, blok="SB55",
kalip="ÖNERMELİ",
z="Z",
madde=TYN + " md. 7, 8, 9",
cek="Vali, başsavcılık aracılığıyla hâkimden tahsis ister; itirazı Vali, savcı ve taraflar yapar; tahsis listeleri üç ayda bir gönderilir.",
kok=[TYN + "'in tahsis talebi, tahsis kararı ve kararın bildirilmesine ilişkin hükümleri çerçevesinde aşağıdaki ifadeler veriliyor:",
     "I. Komisyonun tahsisi için talepte bulunulmasını uygun bulduğu eşya hakkında ilgili Vali tarafından derhâl hâkim veya mahkemeden, Cumhuriyet başsavcılığı aracılığıyla tahsis talebinde bulunulur.",
     "II. Hâkim veya mahkemenin tahsis talebinin kabulü veya reddi kararlarına karşı yalnızca talepte bulunan Vali itiraz edebilir.",
     "III. Tahsis kararları, valilik kanalıyla il jandarma komutanlığı tarafından talepte bulunan kuruma ve Jandarma Genel Komutanlığına derhal bildirilir.",
     "IV. Tahsis edilen eşyalara ilişkin güncel listeler Jandarma Genel Komutanlığınca hazırlanarak İçişleri Bakanlığınca ayda bir gönderilir.",
     "Yukarıdaki ifadelerden hangileri doğrudur?"],
d="I ve III",
c=["I ve II", "II ve IV", "III ve IV", "I, III ve IV"],
sirali=False,
g="Yönetmeliğe göre Komisyonun tahsisi için talepte bulunulmasını uygun bulduğu eşya hakkında ilgili Vali, derhâl hâkim veya mahkemeden Cumhuriyet başsavcılığı aracılığıyla tahsis talebinde bulunur (I doğru). Hâkim veya mahkemenin tahsis talebinin kabulü veya reddi kararlarına karşı yalnızca Vali değil; talepte bulunan Vali, Cumhuriyet savcısı ve dosyanın tarafları itiraz edebilir ve itirazlar hakkında ivedilikle karar verilir (II yanlış). Tahsis kararları valilik kanalıyla il jandarma komutanlığı tarafından talepte bulunan kuruma ve Jandarma Genel Komutanlığına derhal bildirilir (III doğru). Tahsis edilen eşyalara ilişkin güncel listeler Jandarma Genel Komutanlığınca hazırlanarak İçişleri Bakanlığınca ayda bir değil üç ayda bir gönderilir (IV yanlış). En güçlü tuzak IV'tür: ayda bir aralık, tahsise konu olabilecek eşyanın güncel listelerinin il jandarma komutanlığınca bildirilmesine aittir. Bu nedenle doğru cevap 'I ve III' seçeneğidir. (MD 5, 7, 8, 9)",
kanit=TY + " | Komisyonun tahsisi için talepte bulunulmasını uygun bulduğu eşya hakkında ilgili Vali tarafından derhâl hâkim veya mahkemeden Cumhuriyet başsavcılığı aracılığıyla tahsis talebinde bulunulur || "
      + TY + " | talebinin kabulü veya reddi kararlarına karşı talepte bulunan Vali, Cumhuriyet savcısı ve dosyanın tarafları itiraz edebilir || "
      + TY + " | kararları valilik kanalıyla il jandarma komutanlığı tarafından tahsis işleminin gerçekleştirilmesi için talepte bulunan kuruma ve Jandarma Genel Komutanlığına derhal bildirilir || "
      + TY + " | Jandarma Genel Komutanlığı tarafından hazırlanarak İçişleri Bakanlığınca üç ayda bir",
yuva=["I ve II: II'de itiraz edebilecekler yalnız Vali'ye indirilmiş (Cumhuriyet savcısı ve taraflar düşürülmüş)",
      "II ve IV: iki yanlış önerme; IV'teki 'ayda bir' tahsise konu olabilecek eşya listelerinin bildirim aralığıdır",
      "III ve IV: IV'te tahsis edilen eşya listelerinin üç aylık aralığı ayda bire çevrilmiş",
      "I, III ve IV: IV yanlış önermedir"],
yakinlik="PARAFRAZ",
tuzak=["KOMŞU", "YAKIN-SAYI", "UNSUR"], duzey=["AYIRT"], profil=[1, 2],
olumsuz=False, vaka=False, baslangic=False, eksen=0, ayna="", guncellik="",
cikmis="", kapsamli=False,
),

# 19 ---------------- Tahsis Yön. md. 6/4: Komisyonun dikkate alacağı hususlar — rayiç değer yok ----------------
dict(
konu=KONU, blok="SB55",
kalip="KAPSAM_DIŞI",
z="O",
madde=TYN + " md. 6",
cek="Komisyon; eşyanın cinsini, ele geçirildiği olayın niteliğini, kurumların ihtiyaç derecesini ve ihtiyacı karşılama durumunu dikkate alır; rayiç değer sayılmamıştır.",
kok=[TYN + "'e göre, tahsis komisyonunun kurumların tahsis talepleri hakkında karar verirken dikkate alacağı hususlar arasında aşağıdakilerden hangisi sayılmamıştır?"],
d="Eşyanın rayiç değeri",
c=["Eşyanın cinsi", "Eşyanın ele geçirildiği olayın niteliği", "Kurumların ihtiyaç dereceleri", "Kurumların ihtiyacı karşılama durumu"],
sirali=False,
g="Yönetmeliğe göre Komisyon; eşyanın cinsi, ele geçirildiği olayın niteliği, kurumların ihtiyaç dereceleri ve ihtiyacı karşılama durumunu da dikkate alarak karar verir. Eşyanın rayiç değeri bu hususlar arasında sayılmamıştır. Rayiç değer Yönetmelikte tahsis kararının değil, soruşturma veya kovuşturma sonunda iadesine karar verilen eşyanın bedelinin hesaplanmasının ölçüsüdür: kurumların tabi olduğu taşınır mal yönetmeliği hükümlerine göre envantere kayıt sırasında izlenen usulle tespit edilir ve bedel tahsis yapılan kurumun bütçesinden eşya sahibine ödenir. Aday, tahsis kararında eşyanın değerinin de tartılacağını sağduyuyla varsayabilir. Bu nedenle doğru cevap 'Eşyanın rayiç değeri' seçeneğidir. (MD 6, 11)",
kanit=TY + " | Komisyon, eşyanın cinsi, ele geçirildiği olayın niteliği, kurumların ihtiyaç derecelerini, ihtiyacı karşılama durumunu da dikkate alarak karar verir || "
      + TY + " | usule göre rayiç değeri tespit edilir",
yuva=["Komisyonun dikkate alacağı hususlar: eşyanın cinsi (sayılmış)",
      "Komisyonun dikkate alacağı hususlar: ele geçirildiği olayın niteliği (sayılmış)",
      "Komisyonun dikkate alacağı hususlar: kurumların ihtiyaç dereceleri (sayılmış)",
      "Komisyonun dikkate alacağı hususlar: ihtiyacı karşılama durumu (sayılmış)"],
yakinlik="BİREBİR",
tuzak=["LİSTE-DIŞI", "KOMŞU", "SAĞDUYU"], duzey=["TANIMA"], profil=[3],
olumsuz=True, vaka=False, baslangic=False, eksen=0, ayna="", guncellik="",
cikmis="", kapsamli=False,
),

# 20 ---------------- Tahsis Yön. md. 10, 11: tahsis edilen eşyada iade kararı → rayiç bedel kurum bütçesinden — vaka ----------------
dict(
konu=KONU, blok="SB55",
kalip="SONUÇ",
z="ÇZ",
madde=TYN + " md. 10, 11",
cek="Tahsis edilen eşya için iade kararı kesinleşirse rayiç değer üzerinden belirlenen bedel, tahsis yapılan kurumun bütçesinden eşya sahibine ödenir.",
kok=["Kaçakçılık suçu sebebiyle el konulan ve adli emanette bulunan bir gece görüş sistemi, hâkim kararıyla il jandarma komutanlığına tahsis edilmiştir. Kovuşturma sonunda eşyanın sahibine iadesine karar verilmiş ve bu karar kesinleşmiştir.",
     TYN + "'e göre bu durumda aşağıdakilerden hangisi yapılır?"],
d="Rayiç değer üzerinden belirlenen bedel, tahsis yapılan kurumun bütçesinden karşılanarak eşya sahibine ödenir.",
c=["Eşya, tahsis edildiği kurumun malı olarak işlem görmeye devam eder ve sahibine herhangi bir ödeme yapılmaz.",
   "Eşya, kurumdan geri alınarak adli emanete teslim edilir ve buradan sahibine iade edilir.",
   "Bedel, el koyma tarihinden kararın kesinleştiği tarihe kadar kanuni faiz eklenerek Maliye Bakanlığınca aktarılan ödenekten ödenir.",
   "Eşyanın gümrüklenmiş değeri üzerinden hesaplanan bedel, Gümrükler Muhafaza Genel Müdürlüğü bütçesinden eşya sahibine ödenir."],
sirali=False,
g="Yönetmeliğe göre tahsise konu eşyanın soruşturma veya kovuşturma sonunda iadesine karar verilirse kesinleşmiş karar, tahsis kararı da eklenerek ödeme ve kayıt güncelleme işlemleri için eşyanın tahsis edildiği kuruma gönderilir. İadesine karar verilen eşyanın rayiç değeri, kurumun tabi olduğu taşınır mal yönetmeliği hükümleri uyarınca kurum envanterine kaydedilmesi sırasında izlenen usule göre tespit edilir; rayiç değer üzerinden belirlenen bedel, tahsis yapılan kurumun bütçesinden karşılanarak eşya sahibine ödenir. Vakada saklı nokta şudur: iade kararı, tahsis edilmiş eşyanın kendisinin geri verilmesi sonucunu doğurmaz; sahibine bedel ödenir. Eşyanın kurumun malı olarak işlem görmesi müsadere kararı verilmesi hâline aittir. Kanuni faiz eklenmesi ve Maliye Bakanlığınca ödenek aktarılması, 5607 sayılı Kanun'da tahsis edilen kaçak akaryakıt sahibinin lehine sonuçlanan yargılamaya ilişkin düzenlemedir. Gümrüklenmiş değer 5607 sayılı Kanun'da kaim değerin ölçüsüdür; bu Yönetmelikte bedel rayiç değer üzerinden ve tahsis yapılan kurumca ödenir. En güçlü çeldirici akaryakıta ilişkin faizli ödeme düzenlemesidir. Bu nedenle doğru cevap 'Rayiç değer üzerinden belirlenen bedel, tahsis yapılan kurumun bütçesinden karşılanarak eşya sahibine ödenir.' seçeneğidir. (MD 10, 11; 5607 md. 16/A)",
kanit=TY + " | Soruşturma veya kovuşturma sonunda el konulan eşyadan iadesine karar verilenlerin, ilgili kurumların tabi olduğu taşınır mal yönetmeliği hükümleri uyarınca kurum envanterine kaydedilmesi sırasında izlenen usule göre rayiç değeri tespit edilir || "
      + TY + " | Tahsis yapılan kurum tarafından rayiç değer üzerinden belirlenen bedel, kurum bütçesinden karşılanmak suretiyle eşya sahibine ödenir || "
      + TY + " | Müsadere kararı verilmesi halinde tahsis edilen eşya tahsis edilen kurumun malı olarak işlem görür || "
      + K5607 + " | kanuni faiz ilave edilerek ilgili kurum bütçesinden hak sahibine ödenir. Gerekli ödenek, Maliye Bakanlığınca ilgili kurumlara aktarılır",
yuva=["Müsadere kararı hâli: tahsis edilen eşya tahsis edilen kurumun malı olarak işlem görür",
      "İade veya müsadere kararlarının kuruma gönderilmesiyle mahkeme ve başsavcılığa ait adli emanet kayıtları kapatılır (eşya emanete dönmez)",
      "5607 sayılı Kanun kaçak akaryakıt tasfiyesi: lehe sonuçlanan yargılamada kanuni faizli bedel, Maliye Bakanlığınca aktarılan ödenekle",
      "5607 sayılı Kanun kaim değer = gümrüklenmiş değer; ilan Yönetmeliğindeki Genel Müdürlük (Gümrükler Muhafaza)"],
yakinlik="ÇIKARIM",
tuzak=["İSTİSNA", "KOMŞU", "SAĞDUYU"], duzey=["UYGULAMA"], profil=[1, 3],
olumsuz=False, vaka=True, baslangic=False, eksen=0, ayna="", guncellik="",
cikmis="", kapsamli=False,
),

]
