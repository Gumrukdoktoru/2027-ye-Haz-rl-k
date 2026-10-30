# GM Soru Bankası — M57: İthalatta Haksız Rekabetin Önlenmesi (3577 sayılı Kanun, Karar ve Yönetmelik) (10 soru)
# Gümrük Koçu - Ufuk Çetintaş
K = "57-haksiz-rekabet-damping.txt"
KAN = "3577 sayılı İthalatta Haksız Rekabetin Önlenmesi Hakkında Kanun"
YON = "İthalatta Haksız Rekabetin Önlenmesi Hakkında Yönetmelik"


def s(**k):
    base = dict(
        konu="İthalatta Haksız Rekabetin Önlenmesi",
        blok="M57",
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
    # 1 ---------------- Görev – merci eşleştirmesi (Genel Müdürlük, Kurul, Bakanlık) ----------------
    s(
        kalip="EŞLEŞTİRME",
        z="Z",
        madde="3577 sayılı Kanun md. 5, 6, 12, 13",
        cek="Genel Müdürlük: ön inceleme, soruşturmayı yürütme, sekreterya; Kurul: soruşturma açma/durdurma, taahhüt; geçici ve kesin önlem Bakanlık onayıyla.",
        kok=[
            f"{KAN}'a göre, görev ile bu görevi yerine getiren merci eşleştirmelerinden hangisi doğrudur?"
        ],
        d="Soruşturma açılıp açılmamasına karar vermek – İthalatta Haksız Rekabeti Değerlendirme Kurulu",
        c=[
            "Şikâyet üzerine veya re'sen ön incelemeyi yapmak – İthalatta Haksız Rekabeti Değerlendirme Kurulu",
            "Kesin önlem kararını onaylamak – İthalatta Haksız Rekabeti Değerlendirme Kurulu",
            "Kurulun sekreterlik hizmetlerini yürütmek – Bakanlık",
            "Geçici önlem kararını onaylamak – İthalat Genel Müdürlüğü",
        ],
        g="3577 sayılı Kanun görevleri üç merci arasında paylaştırır. İthalat Genel Müdürlüğü şikâyet üzerine veya re'sen ön incelemeyi yapar, soruşturma açılıp açılmayacağı konusunda Kurula teklif sunar, açılan soruşturmayı yürütür ve Kurulun sekreterlik hizmetlerini görür. İthalatta Haksız Rekabeti Değerlendirme Kurulu soruşturma açılıp açılmamasına veya açılmış soruşturmanın durdurulmasına karar verir, yeterli delil varsa geçici önlem kararını ve soruşturma sonucunda kesin önlem kararını Bakanlığın onayına sunar, taahhüt önerir ve taahhüdü kabul edip etmemeye karar verir. Geçici ve kesin önlemleri onaylayan merci ise Bakanlıktır. En güçlü tuzak kesin önlem eşleştirmesidir: kesin önlem kararını Kurul belirler, fakat onaylamaz; onay Bakanlığa aittir. Bu nedenle doğru cevap 'Soruşturma açılıp açılmamasına karar vermek – İthalatta Haksız Rekabeti Değerlendirme Kurulu' seçeneğidir. (MD 3577 sayılı Kanun md. 5, 6)",
        kanit=f"{K} | Soruşturma açılıp açılmamasına veya açılmış bir soruşturmanın durdurulmasına karar vermek, || {K} | Şikâyet üzerine veya gerektiğinde re'sen, verilen bilgi ve belgeler veya mevcut diğer bilgilerin ışığı altında ön incelemeyi yapmak, || {K} | Kurulun sekreterlik hizmetlerini yürütmek ve Kurulca verilecek diğer görevleri yapmak. || {K} | Soruşturma sırasında yeterli delil olması halinde geçici önlem kararını Bakanlığın onayına sunmak, || {K} | kesin önlem kararını Bakanlığın onayına sunmak,",
        yuva=[
            "Genel Müdürlüğün görevi (ön inceleme) Kurula verilmiş",
            "Kurul kesin önlemi önerir; onay Bakanlığın",
            "Sekreterlik Genel Müdürlüğün görevi",
            "Geçici önlem Bakanlık onayıyla",
        ],
        yakinlik="BİREBİR",
        tuzak=["MAKAM", "KOMŞU"],
        duzey=["AYIRT"],
        profil=[3],
        olumsuz=False,
        cikmis="2021/65",
    ),
    # 2 ---------------- Geçici önlem: 60 gün içinde uygulanmaz, 4 ay geçerli ----------------
    s(
        kalip="SÜRE",
        z="O",
        madde="3577 sayılı Kanun md. 7, 12; Yönetmelik md. 20",
        cek="Geçici önlem soruşturmanın açılmasından itibaren 60 gün içinde uygulanmaz; geçerliliği 4 ay (ihracatçı talebiyle 6, daha düşük önlem incelemesinde 6 ve 9 ay).",
        kok=[
            f"{KAN}'a göre, geçici önlemin uygulanamayacağı süre ile geçici önlemin geçerlilik süresi aşağıdakilerden hangisinde doğru olarak verilmiştir?"
        ],
        d="Soruşturmanın açılması tarihinden itibaren 60 gün içinde uygulanmaz; geçerlilik süresi 4 aydır.",
        c=[
            "Şikâyetin yapıldığı tarihten itibaren 60 gün içinde uygulanmaz; geçerlilik süresi 4 aydır.",
            "Soruşturmanın açılması tarihinden itibaren 45 gün içinde uygulanmaz; geçerlilik süresi 4 aydır.",
            "Soruşturmanın açılması tarihinden itibaren 60 gün içinde uygulanmaz; geçerlilik süresi 9 aydır.",
            "Soruşturmanın açılması tarihinden itibaren 90 gün içinde uygulanmaz; geçerlilik süresi 6 aydır.",
        ],
        g="3577 sayılı Kanuna göre soruşturma sırasında dampingli veya sübvansiyonlu ithalatın varlığı ve zarara neden olduğu konusunda ön belirlemeler yapılırsa, Bakanlık onayıyla damping marjı veya sübvansiyon miktarı kadar ya da zararı gidermeye yetecek daha az oranda teminat şeklinde geçici önlem uygulanabilir. Ancak soruşturmanın açılması tarihinden itibaren 60 gün içinde geçici önlem uygulanmaz; süre şikâyet tarihinden değil soruşturmanın açılmasından başlar. Geçici önlemlerin geçerlilik süresi 4 aydır; ihracatın önemli kısmını yapan ihracatçıların talebiyle 6 aya kadar çıkarılabilir; damping marjından düşük bir önlemin yeterliliği incelenecekse süreler 6 ve 9 ay olarak belirlenebilir. 45 gün, Genel Müdürlüğün ön inceleme süresidir; 90 gün ise vergilerin geriye dönük uygulanabileceği azami süredir. En güçlü tuzak şikâyet tarihinden başlayan 60 gündür: sayı doğrudur, fakat başlangıç anı soruşturmanın açılmasıdır. Bu nedenle doğru cevap 'Soruşturmanın açılması tarihinden itibaren 60 gün içinde uygulanmaz; geçerlilik süresi 4 aydır.' seçeneğidir. (MD 3577 sayılı Kanun md. 12)",
        kanit=f"{K} | Soruşturmanın açılması tarihinden itibaren ALTMIŞ (60) GÜN içerisinde GEÇİCİ ÖNLEM UYGULANMAZ. || {K} | Geçici önlemlerin geçerlilik süresi (4) DÖRT AYDIR. || {K} | Kurulun kararı üzerine Bakanlık onayı ile (6) ALTI AYA KADAR ÇIKARILABİLİR. || {K} | Bu süreler sırasıyla ALTI (6) ve DOKUZ (9) AY olarak belirlenebilir. || {K} | incelemeyi azami 45 GÜN İÇİNDE tamamlayarak || {K} | Geçici önlemlerin alındığı tarihten itibaren DOKSAN (90) GÜNÜ GEÇEMEZ.",
        yuva=[
            "Aynı süre, yanlış başlangıç anı (şikâyet tarihi)",
            "Yönetmelik: ön inceleme için 45 gün",
            "Kanun: daha düşük önlem incelemesinde 9 aya kadar uzayan süre",
            "Kanun: geriye dönük uygulama 90 gün ve ihracatçı talebiyle 6 ay",
        ],
        yakinlik="BİREBİR",
        tuzak=["BAŞLANGIÇ", "YAKIN-SAYI"],
        duzey=["AYIRT"],
        profil=[3],
        olumsuz=False,
        baslangic=True,
        eksen=1,
    ),
    # 3 ---------------- Soruşturma süreleri (önermeli) ----------------
    s(
        kalip="ÖNERMELİ",
        z="Z",
        madde="İthalatta Haksız Rekabetin Önlenmesi Hakkında Yönetmelik md. 20, 21, 30; Karar md. 6, 7",
        cek="Ön inceleme 45 gün; soru formu bir haftada alınmış sayılır, 30 gün cevap; soruşturma 1 yıl + 6 ay; geriye dönük 90 gün; gözden geçirme en az 1 yıl sonra.",
        kok=[
            f"{YON} ile İthalatta Haksız Rekabetin Önlenmesi Hakkında Karara göre;",
            "I. Genel Müdürlük, şikâyet üzerine veya re'sen yapacağı incelemeyi azami 45 gün içinde tamamlayarak soruşturma açılıp açılmaması hususunda Kurula teklifte bulunur.",
            "II. Soruşturmada gönderilen soru formlarının gönderildikleri tarihten itibaren bir hafta içinde alındığı kabul edilir ve cevaplandırılmaları için 30 günlük süre tanınır.",
            "III. Soruşturma, özel durumlar dışında bir yıl içinde sonuçlandırılır; bu süre gerektiğinde Kurulca bir yılı geçmemek üzere uzatılabilir.",
            "IV. Vergilerin geriye dönük uygulanması, soruşturmanın başlangıç tarihinden öncesine gitmemek kaydıyla geçici önlemlerin alındığı tarihten itibaren geriye 90 gün ile sınırlıdır.",
            "V. Kesin önlemler, yürürlüğe girdikleri tarihten itibaren en az bir yıl sonra ilgili taraflardan birinin talebi üzerine veya re'sen gözden geçirilebilir.",
            "ifadelerinden hangileri doğrudur?",
        ],
        d="I, II, IV ve V",
        c=["I ve II", "II, III ve V", "I, III ve IV", "I, II, III, IV ve V"],
        sirali=True,
        siklar=[
            "I ve II",
            "II, III ve V",
            "I, III ve IV",
            "I, II, IV ve V",
            "I, II, III, IV ve V",
        ],
        g="Yönetmeliğe göre Genel Müdürlük şikâyet üzerine veya re'sen yaptığı incelemeyi azami 45 gün içinde tamamlayarak soruşturma açılıp açılmaması konusunda Kurula teklifte bulunur (I doğru). Soruşturma açılınca bilinen ithalatçı ve ihracatçılara (sübvansiyon soruşturmasında ihracatçı ülkeye de) soru formları gönderilir; formların bir hafta içinde alındığı kabul edilir ve cevap için 30 gün tanınır (II doğru). Soruşturma özel durumlar dışında bir yıl içinde sonuçlandırılır; süre Kurulca bir yılı değil, altı ayı geçmemek üzere uzatılabilir (III yanlış). Karara göre geriye dönük uygulama, soruşturmanın başlangıç tarihinden öncesine gitmemek kaydıyla geçici önlemlerin alındığı tarihten itibaren geriye 90 gün ile sınırlıdır (IV doğru). Kesin önlemler yürürlüğe girdikleri tarihten en az bir yıl sonra taraflardan birinin talebiyle veya re'sen gözden geçirilebilir (V doğru). En güçlü tuzak III. önermedir: soruşturmanın asıl süresi bir yıl olduğu için uzatmanın da bir yıl olduğu sanılır. Bu nedenle doğru cevap 'I, II, IV ve V' seçeneğidir. (MD Yönetmelik md. 20, 21, 30; Karar md. 6, 7)",
        kanit=f"{K} | incelemeyi azami 45 GÜN İÇİNDE tamamlayarak, soruşturma açılıp || {K} | Bu formların gönderildikleri tarihten itibaren BİR HAFTA İÇİNDE ALINDIĞI KABUL EDİLİR ve cevaplandırılmaları için 30 GÜNLÜK SÜRE TANINIR. || {K} | Soruşturma, özel durumlar dışında BİR (1) YIL içinde SONUÇLANDIRILIR. || {K} | Bu süre, gerektiğinde, Kurulca ALTI (6) AYI GEÇMEMEK üzere UZATILABİLİR. || {K} | Geçici önlemlerin alındığı tarihten itibaren geriye 90 GÜN İLE SINIRLI OLUP, || {K} | yürürlüğe girdikleri tarihten itibaren EN AZ BİR (1) YIL SONRA ilgili taraflardan birinin talebi",
        yuva=[
            "I ve II: geriye dönük uygulama ve gözden geçirme sürelerini bilmeyen aday",
            "II, III ve V: uzatma süresini bir yıl sanan, 45 günü bilmeyen aday",
            "I, III ve IV: uzatmayı bir yıl sanan aday",
            "I, II, III, IV ve V: uzatma süresini bir yıl sanan aday",
        ],
        yakinlik="PARAFRAZ",
        tuzak=["YAKIN-SAYI", "SAYI"],
        duzey=["HATIRLAMA", "BÜTÜNLEŞİK"],
        profil=[2, 3],
        olumsuz=False,
        cikmis="2022/26",
    ),
    # 4 ---------------- Önlem gerektiren haller ve vergiler (önermeli, yanlış yönlü) ----------------
    s(
        kalip="ÖNERMELİ",
        z="O",
        madde="3577 sayılı Kanun md. 3, 9, 13",
        cek="Önlem: maddi zarar, maddi zarar tehdidi, üretim dalı kurulmasının fiziki gecikmesi; damping ve telafi edici vergi birlikte uygulanamaz, ithalatı engellemez, ayrı tahsil edilir.",
        kok=[
            f"{KAN}'a göre önlem alınmasını gerektiren haller ve alınan vergiler hakkında;",
            "I. Dampinge veya sübvansiyona konu ithalatın Türkiye'de bir üretim dalının kurulmasını fiziki olarak geciktirmesi, önlem alınmasını gerektiren haller arasındadır.",
            "II. Sübvansiyona konu ithalata karşı önlem alınabilmesi için sübvansiyonun, Sübvansiyonlar ve Telafi Edici Tedbirler Anlaşması çerçevesinde bir firma veya firma grubuna ya da bir üretim dalı veya üretim dalı grubuna yönelik olduğunun tespit edilmesi gerekir.",
            "III. Soruşturma konusu mal için hem damping yapılmış hem sübvansiyon verilmiş olması halinde, aynı durumun telafisi için dampinge karşı vergi ve telafi edici vergi birlikte uygulanabilir.",
            "IV. Dampinge karşı vergi veya telafi edici vergi konulmuş olması, ilgili malın ithalatını engeller.",
            "V. Dampinge karşı vergi veya telafi edici vergi, gümrük idarelerince ithalde alınan diğer vergilerden ayrı olarak tahsil olunur veya teminata bağlanır.",
            "ifadelerinden hangileri yanlıştır?",
        ],
        d="III ve IV",
        c=["I ve III", "II ve V", "III, IV ve V", "I, III ve IV"],
        sirali=True,
        siklar=["I ve III", "II ve V", "III ve IV", "I, III ve IV", "III, IV ve V"],
        g="3577 sayılı Kanuna göre önlem alınmasını gerektiren haller, dampinge veya sübvansiyona konu ithalatın Türkiye'de bir üretim dalında maddi zarara yol açması, maddi zarar tehdidi oluşturması veya bir üretim dalının kurulmasını fiziki olarak geciktirmesidir (I doğru). Sübvansiyona karşı önlem için ayrıca sübvansiyonun bir firma/firma grubu veya üretim dalı/üretim dalı grubuna yönelik olduğunun tespiti gerekir (II doğru). Mal için hem damping yapılmış hem sübvansiyon verilmişse aynı durumun telafisi için dampinge karşı vergi ve telafi edici vergi birlikte uygulanamaz (III yanlış). Bu vergilerin konulmuş olması ilgili malın ithalatını engellemez (IV yanlış). Vergiler gümrük idarelerince ithalde alınan diğer vergilerden ayrı olarak tahsil olunur veya teminata bağlanır (V doğru). En güçlü tuzak IV. önermedir: önlem ithalatı caydırmaya yöneldiği için yasaklayıcı sanılır, oysa yalnız ek vergi doğurur. Bu nedenle doğru cevap 'III ve IV' seçeneğidir. (MD 3577 sayılı Kanun md. 3, 9, 13)",
        kanit=f"{K} | BİR ÜRETİM DALININ KURULMASINI FİZİKİ OLARAK GECİKTİRMESİDİR. || {K} | bir firma/firma grubu veya bir üretim dalı/üretim dalı grubuna yönelik olduğunun da tespit edilmiş olması gerekir. || {K} | Aynı durumun telafisi için dampinge karşı vergi ve telafi edici vergi BİRLİKTE UYGULANAMAZ. || {K} | Dampinge karşı vergi veya telafi edici vergi konulmuş olması, İLGİLİ MALIN İTHALATINI ENGELLEMEZ. || {K} | İthalde alınan diğer vergilerden AYRI OLARAK tahsil olunur veya teminata bağlanır.",
        yuva=[
            "I ve III: fiziki gecikmeyi zarar saymayan aday",
            "II ve V: doğru önermeleri yanlış sanan aday",
            "III, IV ve V: ayrı tahsil kuralını bilmeyen aday",
            "I, III ve IV: fiziki gecikmeyi zarar saymayan aday",
        ],
        yakinlik="PARAFRAZ",
        tuzak=["TERSİNE", "SAĞDUYU"],
        duzey=["AYIRT", "BÜTÜNLEŞİK"],
        profil=[2, 3],
        olumsuz=True,
        cikmis="2021/58",
    ),
    # 5 ---------------- İhmal edilebilir oranlar: %3 / %7 (damping) ----------------
    s(
        kalip="ORAN-TUTAR",
        z="Z",
        madde="İthalatta Haksız Rekabetin Önlenmesi Hakkında Yönetmelik md. 28",
        cek="Damping: marj %2, ülke payı %3; birden çok ülkede tek tek %3 altındakilerin toplamı %7'yi geçmemeli. Sübvansiyon: %1; gelişmekte olanlarda %2, %4 ve %9.",
        kok=[
            f"{YON}'e göre, birden fazla ülkenin soruşturmaya konu olduğu bir damping soruşturmasında ithalat miktarının ihmal edilebilir kabul edilebilmesi için aşağıdaki koşullardan hangisi aranır?"
        ],
        d="İthalat payı tek tek %3'ün altında olan ülkelerin toplam paylarının %7'yi geçmemesi",
        c=[
            "İthalat payı tek tek %4'ün altında olan ülkelerin toplam paylarının %9'u geçmemesi",
            "İthalat payı tek tek %2'nin altında olan ülkelerin toplam paylarının %7'yi geçmemesi",
            "İthalat payı tek tek %3'ün altında olan ülkelerin toplam paylarının %9'u geçmemesi",
            "İthalat payı tek tek %1'in altında olan ülkelerin toplam paylarının %3'ü geçmemesi",
        ],
        g="Yönetmelik ihmal edilebilir oranları damping ve sübvansiyon soruşturmaları için ayrı ayrı belirler. Damping soruşturmasında damping marjının ihraç fiyatının yüzde 2'sinden düşük olması ya da soruşturma konusu ülkeden dampingli ithalatın benzer mal ithalatının yüzde 3'ünden düşük olması ihmal edilebilir sayılır; birden fazla ülke soruşturmaya konu ise ithalat payı tek tek yüzde 3'ün altında olan ülkelerin toplam payının yüzde 7'yi geçmemesi gerekir. Sübvansiyon soruşturmasında sübvansiyon miktarı mal değerinin yüzde 1'inden düşük olmalı; gelişmekte olan ülkelerde bu oran yüzde 2, ülke ithalat payı yüzde 4, birden fazla ülkede toplam pay yüzde 9'dur. Damping marjı, sübvansiyon miktarı ya da ithalat miktarı ihmal edilebilir düzeyin altındaysa soruşturma açılmaz, açılmışsa kapatılır. En güçlü tuzak yüzde 4 ve yüzde 9 ikilisidir: yapı aynıdır, fakat bu oranlar gelişme yolundaki ülkelere karşı sübvansiyon soruşturmasına aittir. Bu nedenle doğru cevap 'İthalat payı tek tek %3'ün altında olan ülkelerin toplam paylarının %7'yi geçmemesi' seçeneğidir. (MD Yönetmelik md. 28)",
        kanit=f"{K} | TEK TEK %3'ÜN ALTINDA OLAN ÜLKELERİN TOPLAM PAYLARININ %7'Yİ GEÇMEDİĞİ, haller. || {K} | %4'ÜN ALTINDA OLAN ÜLKELERİN TOPLAM PAYLARININ %9'U GEÇMEDİĞİ, haller. || {K} | DAMPİNG MARJININ %2 ORANINDAN DÜŞÜK OLDUĞU || {K} | Sübvansiyon miktarının soruşturma konusu mal değerinin %1'İNDEN DÜŞÜK OLDUĞU || {K} | Damping marjı, sübvansiyon miktarı ya da ithalat miktarının ihmal edilebilir düzeylerin altında olması halinde, soruşturma açılmaz.",
        yuva=[
            "Yönetmelik: gelişmekte olan ülkelere sübvansiyon soruşturmasında %4 ve %9",
            "Yönetmelik: damping marjının %2 eşiğiyle karıştırma",
            "Damping %3 ile sübvansiyon %9 karışımı",
            "Yönetmelik: sübvansiyon miktarı %1 ile ülke payı %3 karışımı",
        ],
        yakinlik="BİREBİR",
        tuzak=["YAKIN-SAYI", "KOMŞU"],
        duzey=["AYIRT"],
        profil=[3],
        olumsuz=False,
        eksen=2,
        ayna="damping %3/%7 ↔ sübvansiyon %4/%9",
    ),
    # 6 ---------------- Taahhütler (olumsuz) ----------------
    s(
        kalip="YANLIŞ",
        z="O",
        madde="3577 sayılı Kanun md. 11; Yönetmelik md. 32, 33",
        cek="Taahhüt kendiliğinden veya Kurul önerisiyle; Kurul önerisini kabul zorunlu değil; sübvansiyonda ülke onayı; ihlalde mevcut verilerle önlem; geçici önlem tahsilatı engellenmez.",
        kok=[
            f"{KAN} ve {YON}'e göre taahhütler hakkında aşağıdakilerden hangisi yanlıştır?"
        ],
        d="Taahhüdün kabulü üzerine soruşturmanın sonuçlandırılması, taahhüdün yürürlüğe girmesine kadar uygulanmış geçici önlemlerin gerekli kıldığı tahsilatı engeller.",
        c=[
            "Menşe ülke, ihracatçı ülke veya ihracatçı, kendiliğinden veya Kurulun önerisi üzerine taahhütte bulunabilir.",
            "Kurulca önerilen taahhüdün ihracatçı veya ihracatçı ülke tarafından kabul edilmesi zorunlu değildir.",
            "Sübvansiyon soruşturmasında ihracatçının taahhüdü ilgili ülkenin onayı alındıktan sonra kabul edilebilir.",
            "Taahhütlerin ihlal edilmesi halinde mevcut verilere dayalı olarak geçici veya kesin önlem alınabilir.",
        ],
        g="3577 sayılı Kanuna göre soruşturma sırasında menşe ülke, ihracatçı ülke veya ihracatçı, dampingli veya sübvansiyonlu ithalattan kaynaklanan zararı ortadan kaldıracak şekilde kendiliğinden veya Kurulun önerisi üzerine taahhütte bulunabilir; Kurul taahhüdü kabul ederse soruşturma geçici veya kesin önlem alınmaksızın durdurulabilir veya sonuçlandırılabilir. Yönetmeliğe göre Kurulca önerilen taahhüdün kabulü zorunlu değildir; sübvansiyon soruşturmasında ihracatçının taahhüdü ilgili ülkenin onayı alındıktan sonra kabul edilebilir; taahhüt ihlal edilirse mevcut verilere dayalı olarak geçici veya kesin önlem alınabilir. Soruşturmanın taahhütle sonuçlandırılmış olması ise taahhüdün yürürlüğe girmesine kadar uygulanmış geçici önlemlerin gerektirdiği tahsilatı engellemez. En güçlü tuzak taahhüdün kabulünün zorunlu olmadığı ifadesidir: öneriyi Kurul yaptığı için karşı tarafın kabule mecbur olduğu sanılır. Bu nedenle doğru cevap 'Taahhüdün kabulü üzerine soruşturmanın sonuçlandırılması, taahhüdün yürürlüğe girmesine kadar uygulanmış geçici önlemlerin gerekli kıldığı tahsilatı engeller.' seçeneğidir. (MD 3577 sayılı Kanun md. 11; Yönetmelik md. 32, 33)",
        kanit=f"{K} | Kendiliğinden veya Kurulun önerisi üzerine taahhütte bulunabilir. || {K} | Kurulca önerilen taahhüdün ihracatçı veya ihracatçı ülke tarafından kabul edilmesi zorunlu değildir. || {K} | Sübvansiyon soruşturmasında ihracatçının taahhüdü ilgili ülkenin onayı alındıktan sonra kabul edilebilir. || {K} | Taahhütlerin ihlal edilmesi halinde, mevcut verilere dayalı olarak, geçici veya kesin önlem alınabilir. || {K} | SORUŞTURMANIN SONUÇLANDIRILMIŞ OLMASI, taahhüdün yürürlüğe girmesine kadar uygulanmış olan geçici önlemlerin gerekli kıldığı tahsilatı engellemez.",
        yuva=[
            "Kanun: taahhüdün kendiliğinden veya Kurul önerisiyle verilmesi (doğru)",
            "Yönetmelik: Kurul önerisinin kabulü zorunlu değil (doğru)",
            "Yönetmelik: sübvansiyonda ülke onayı (doğru)",
            "Yönetmelik: taahhüt ihlalinde önlem (doğru)",
        ],
        yakinlik="BİREBİR",
        tuzak=["TERSİNE", "SAĞDUYU"],
        duzey=["AYIRT"],
        profil=[3],
        olumsuz=True,
    ),
    # 7 ---------------- Kesin vergi > teminat: fark tahsil edilmez ----------------
    s(
        kalip="SONUÇ",
        z="Z",
        madde="3577 sayılı Kanun md. 13, 14, 15",
        cek="Kesinleşen vergi teminattan yüksekse fark tahsil edilmez, düşükse fark geri ödenir; soruşturma kapatılırsa teminat iade edilir.",
        kok=[
            f"{KAN}'a göre, maddi zarar tespitine dayanan bir soruşturma sonucunda kesinleşen dampinge karşı verginin soruşturma sırasında geçici önlem olarak alınan teminattan yüksek olması halinde aşağıdakilerden hangisi uygulanır?"
        ],
        d="Aradaki fark tahsil edilmez.",
        c=[
            "Aradaki fark gümrük idarelerince ayrıca tahsil edilir.",
            "Aradaki fark 6183 sayılı Kanun hükümlerine göre gümrük idarelerince kovuşturulur.",
            "Teminatın tamamı iade edilir ve kesinleşen vergi ayrıca tahsil edilir.",
            "Aradaki fark mükellefe geri ödenir.",
        ],
        g="3577 sayılı Kanuna göre soruşturma sonunda kesin önlem alınmasına karar verilirse daha önce alınan geçici önlemler kesin önleme dönüştürülür ve teminatlar hakkında Kanunun geri ödeme hükmü uygulanır. Bu hükme göre kesinleşen dampinge karşı vergi veya telafi edici vergi daha önce alınan teminattan yüksekse aradaki fark tahsil edilmez; düşükse fark geri ödenir. Soruşturma kapatılırsa geçici önlemler kaldırılır ve teminatlar iade edilir. Maddi zarar tehdidine veya üretim dalının kurulmasının fiziki gecikmesine dayanan kesin önlemlerde ise teminatın tahsili için Kurulun ayrıca bir belirleme yapması gerekir. 6183 sayılı Kanun ödenmeyen dampinge karşı verginin takibine ilişkindir. En güçlü tuzak farkın geri ödenmesidir: hüküm teminatın vergiden yüksek olduğu ters duruma aittir. Bu nedenle doğru cevap 'Aradaki fark tahsil edilmez.' seçeneğidir. (MD 3577 sayılı Kanun md. 13, 14)",
        kanit=f"{K} | Daha önce alınan teminattan YÜKSEK ise FARK TAHSİL EDİLMEZ. || {K} | Daha önce alınan teminattan DÜŞÜK ise FARK GERİ ÖDENİR. || {K} | Soruşturmanın kapatılmasına karar verilmesi halinde geçici önlemler kaldırılır ve alınan teminatlar iade edilir. || {K} | 6183 sayılı Amme Alacaklarının Tahsil Usulü Hakkında Kanun hükümlerine göre gümrük idarelerince || {K} | geçici önlem alınmış ise, bunlar kesin önleme dönüştürülür. || {K} | soruşturma sırasında alınan teminatın tahsil edilebilmesi için Kurulun",
        yuva=[
            "Ters sonuç: fark tahsili",
            "Kanun: ödenmeyen verginin 6183 ile kovuşturulması",
            "Kanun: soruşturma kapatılınca teminat iadesi",
            "Kanun: kesinleşen vergi teminattan düşükse fark geri ödenir",
        ],
        yakinlik="BİREBİR",
        tuzak=["TERSİNE", "KOMŞU"],
        duzey=["UYGULAMA"],
        profil=[4],
        olumsuz=False,
    ),
    # 8 ---------------- Kesin önlemlerin süresi, gözden geçirme, askıya alma (olumsuz) ----------------
    s(
        kalip="YANLIŞ",
        z="Z",
        madde="İthalatta Haksız Rekabetin Önlenmesi Hakkında Karar md. 7, 9; Yönetmelik md. 35",
        cek="Kesin önlem 5 yıl; gözden geçirme uygulamayı engellemez; nihai gözden geçirme sona ermeden 3 ay önce; askı: 1 yıl yürürlük, 9 ay + 1 yıl; mücbir sebepte 1 yıl şartı yok.",
        kok=[
            f"İthalatta Haksız Rekabetin Önlenmesi Hakkında Karar ve {YON}'e göre kesin önlemlerin süresi, gözden geçirilmesi ve askıya alınması hakkında aşağıdakilerden hangisi yanlıştır?"
        ],
        d="Pazar koşullarındaki değişme savaş hali, doğal afet veya grev gibi mücbir sebeplerden kaynaklansa da önlemin askıya alınabilmesi için en az bir yıl yürürlükte bulunması şartı aranır.",
        c=[
            "Kesin önlemler, yürürlüğe girdikleri veya damping ya da sübvansiyon ile zarar incelemesini birlikte kapsayan en son gözden geçirme soruşturmasının sonuçlandığı tarihten itibaren beş yıl süreyle yürürlükte kalır.",
            "Gözden geçirme soruşturması açılması, yürürlükte bulunan kesin önlemlerin uygulanmasını engellemez.",
            "Yerli üreticiler, kesin önlemin yürürlük süresinin sona ermesinden en geç üç ay önce nihai gözden geçirme soruşturması açılmasını talep edebilir.",
            "En az bir yıl yürürlükte bulunan önlemlerin uygulanması, Kurulun kararı ve Bakanlık onayıyla dokuz ay süreyle geçici olarak durdurulabilir.",
        ],
        g="Karara göre kesin önlemler, yürürlüğe girdikleri veya damping/sübvansiyon ile zarar incelemesini birlikte kapsayan en son gözden geçirme soruşturmasının sonuçlandığı tarihten itibaren beş yıl yürürlükte kalır; gözden geçirme soruşturması açılması yürürlükteki önlemlerin uygulanmasını engellemez ve bu hükümler taahhütlere de uygulanır. Yönetmeliğe göre yerli üreticiler yürürlük süresinin sona ermesinden en geç üç ay önce nihai gözden geçirme soruşturması talep edebilir. Pazar koşullarının geçici değişmesi halinde, en az bir yıl yürürlükte bulunan önlemlerin uygulanması Kurul kararı ve Bakanlık onayıyla dokuz ay durdurulabilir ve bu süre en fazla bir yıl daha uzatılabilir. Değişme savaş hali, doğal afet, yangın, grev, lokavt gibi mücbir sebeplerden kaynaklanıyorsa önlemin bir yıl yürürlükte bulunması koşulu aranmaz; bu nedenle mücbir sebepte de bir yıl şartı arandığı ifadesi yanlıştır. En güçlü tuzak üç aylık süredir: nihai gözden geçirme talebinin son günü yürürlük sonundan geriye doğru hesaplandığı için yanlış sanılır. Bu nedenle doğru cevap 'Pazar koşullarındaki değişme savaş hali, doğal afet veya grev gibi mücbir sebeplerden kaynaklansa da önlemin askıya alınabilmesi için en az bir yıl yürürlükte bulunması şartı aranır.' seçeneğidir. (MD Karar md. 7, 9; Yönetmelik md. 35)",
        kanit=f"{K} | 5 (BEŞ) YIL SÜREYLE YÜRÜRLÜKTE KALIR. || {K} | YÜRÜRLÜKTE BULUNAN KESİN ÖNLEMLERİN UYGULANMASINI ENGELLEMEZ. || {K} | Yürürlük süresinin sona ermesinden en geç 3 ay önce önleme konu olan ürünün yerli üreticileri || {K} | En az BİR (1) YIL YÜRÜRLÜKTE BULUNAN önlemlerin uygulanması, || {K} | Kurulun kararı ve Bakanlık onayı ile DOKUZ (9) AY süresince GEÇİCİ OLARAK DURDURULABİLİR. || {K} | önlemin BİR YIL YÜRÜRLÜKTE BULUNMASI KOŞULU ARANMAZ.",
        yuva=[
            "Karar: beş yıllık yürürlük (doğru)",
            "Karar: gözden geçirme uygulamayı engellemez (doğru)",
            "Yönetmelik: nihai gözden geçirme talebi üç ay önce (doğru)",
            "Karar: askıya alma dokuz ay (doğru)",
        ],
        yakinlik="BİREBİR",
        tuzak=["İSTİSNA", "TERSİNE"],
        duzey=["AYIRT"],
        profil=[3],
        olumsuz=True,
    ),
    # 9 ---------------- İade soruşturması: 6 ay başvuru, 12 ay karar ----------------
    s(
        kalip="SÜRE",
        z="O",
        madde="İthalatta Haksız Rekabetin Önlenmesi Hakkında Yönetmelik md. 37",
        cek="Fazla ödenen verginin iadesi: önlemlerin tahsilinden itibaren 6 ay içinde başvuru; 12 ay içinde karar (18 aya kadar uzar); karardan sonra 90 gün içinde ödeme.",
        kok=[
            f"{YON}'e göre, gerçek damping marjından daha fazla ödenmiş dampinge karşı verginin iadesini talep eden ithalatçının başvuru süresi ile başvuru üzerine kararın verilme süresi aşağıdakilerden hangisinde doğru olarak verilmiştir?"
        ],
        d="Önlemlerin tahsili tarihinden itibaren 6 ay içinde başvurulur; yeterli delilleri içeren başvuruyu müteakip 12 ay içinde karar verilir.",
        c=[
            "Önlemlerin tahsili tarihinden itibaren 12 ay içinde başvurulur; başvuruyu müteakip 6 ay içinde karar verilir.",
            "Kesin önlemin yürürlüğe girdiği tarihten itibaren 6 ay içinde başvurulur; başvuruyu müteakip 12 ay içinde karar verilir.",
            "Önlemlerin tahsili tarihinden itibaren 6 ay içinde başvurulur; başvuruyu müteakip 90 gün içinde karar verilir.",
            "Önlemlerin tahsili tarihinden itibaren 1 yıl içinde başvurulur; başvuruyu müteakip 18 ay içinde karar verilir.",
        ],
        g="Yönetmeliğe göre kesin önleme esas damping marjı veya sübvansiyon miktarının ortadan kalkması ya da azalması nedeniyle fazla ödenen verginin iadesini isteyen ithalatçı, önlemlerin tahsili tarihinden itibaren 6 ay içinde, delilleriyle birlikte, yazılı olarak Genel Müdürlüğe başvurur. Yeterli delilleri içeren başvuruyu müteakip 12 ay içinde karar verilir; bu süre gerekli hallerde 18 aya kadar uzatılabilir. İade kararını izleyen 90 gün içinde de ödeme yapılır. Başvuru süresinin başlangıcı kesin önlemin yürürlüğe girdiği tarih değil, önlemlerin tahsili tarihidir; 90 gün karar değil ödeme süresidir; 18 ay ise ancak uzatma halinde ulaşılan azami süredir. En güçlü tuzak kesin önlemin yürürlük tarihinden başlayan 6 aydır: süre doğrudur, başlangıç anı yanlıştır. Bu nedenle doğru cevap 'Önlemlerin tahsili tarihinden itibaren 6 ay içinde başvurulur; yeterli delilleri içeren başvuruyu müteakip 12 ay içinde karar verilir.' seçeneğidir. (MD Yönetmelik md. 37)",
        kanit=f"{K} | önlemlerin tahsili tarihinden itibaren 6 AY İÇİNDE, delilleriyle birlikte, yazılı olarak || {K} | İade talebi hakkında yeterli delilleri içeren bir başvuruyu müteakip, ONİKİ (12) AY içinde karar verilir. || {K} | Gerekli görülen hallerde bu süre ON SEKİZ (18) AYA kadar uzatılabilir. || {K} | İade kararının verilmesini izleyen DOKSAN (90) GÜN içerisinde ise gerekli ödeme yapılır.",
        yuva=[
            "Başvuru ve karar sürelerinin yer değiştirmesi",
            "Aynı süreler, yanlış başlangıç anı (kesin önlemin yürürlüğü)",
            "Yönetmelik: 90 gün ödeme süresidir",
            "Yönetmelik: 18 ay uzatmalı azami karar süresi",
        ],
        yakinlik="BİREBİR",
        tuzak=["BAŞLANGIÇ", "YAKIN-SAYI"],
        duzey=["AYIRT"],
        profil=[3],
        olumsuz=False,
        baslangic=True,
    ),
    # 10 ---------------- Şikâyet ve soruşturmanın açılması (olumsuz): %50 / %25 ----------------
    s(
        kalip="YANLIŞ",
        z="Z",
        madde="İthalatta Haksız Rekabetin Önlenmesi Hakkında Yönetmelik md. 19, 20",
        cek="Üretim dalı adına şikâyet: destekleyenler, destekleyen+karşı çıkanların %50'sinden fazla ve Türkiye üretiminin %25'inden az olmamalı; ihmal edilebilir düzeyde soruşturma açılmaz.",
        kok=[
            f"{YON}'e göre şikâyet ve soruşturmanın açılması hakkında aşağıdakilerden hangisi yanlıştır?"
        ],
        d="Şikâyetin üretim dalı adına yapılmış sayılabilmesi için şikâyeti destekleyen üreticilerin üretiminin, destekleyen ve karşı çıkan üreticilerin toplam üretiminin %25'inden fazla, toplam Türkiye benzer mal üretiminin ise %50'sinden az olmaması gerekir.",
        c=[
            "Damping marjı, sübvansiyon miktarı ya da ithalat miktarının ihmal edilebilir düzeylerin altında olması halinde soruşturma açılmaz.",
            "Kurulca soruşturma açılmasına karar verilirse ilgili ülkeye bildirimde bulunulur ve Resmî Gazete'de yayımlanacak bir tebliğle soruşturma başlatılır.",
            "Soruşturma başlatılıncaya kadar başvuru hakkında herhangi bir bilgi ifşa edilemez.",
            "İnceleme süresi içerisinde şikâyetin geri çekilmesi halinde şikâyet yapılmamış sayılır.",
        ],
        g="Yönetmeliğe göre bir şikâyetin üretim dalı tarafından veya adına yapılmış sayılabilmesi için şikâyeti destekleyen üreticilerin toplam benzer mal üretiminin, şikâyeti destekleyen ve karşı çıkan üreticilerin toplam üretiminin yüzde 50'sinden fazla olması ve toplam Türkiye benzer mal üretiminin yüzde 25'inden az olmaması gerekir; seçenekte bu iki oran yer değiştirmiştir. Damping marjı, sübvansiyon miktarı ya da ithalat miktarı ihmal edilebilir düzeyin altındaysa soruşturma açılmaz. Kurul soruşturma açılmasına karar verirse ilgili ülkeye bildirimde bulunulur ve Resmî Gazete'de yayımlanan bir tebliğle soruşturma başlatılır; soruşturma başlatılıncaya kadar başvuru hakkında bilgi ifşa edilemez. İnceleme süresi içinde şikâyet geri çekilirse şikâyet yapılmamış sayılır. En güçlü tuzak bilgi ifşa yasağıdır: şeffaflık beklentisi nedeniyle yanlış sanılır, oysa yasak soruşturmanın başlatılmasına kadar sürer. Bu nedenle doğru cevap 'Şikâyetin üretim dalı adına yapılmış sayılabilmesi için şikâyeti destekleyen üreticilerin üretiminin, destekleyen ve karşı çıkan üreticilerin toplam üretiminin %25'inden fazla, toplam Türkiye benzer mal üretiminin ise %50'sinden az olmaması gerekir.' seçeneğidir. (MD Yönetmelik md. 19, 20)",
        kanit=f"{K} | Şikâyeti destekleyen üreticiler ile şikâyete karşı çıkan üreticilerin toplam benzer mal üretiminin %50'SİNDEN || {K} | FAZLA OLMASI ve toplam Türkiye benzer mal üretiminin %25'İNDEN AZ OLMAMASI gerekir. || {K} | Damping marjı, sübvansiyon miktarı ya da ithalat miktarının ihmal edilebilir düzeylerin altında olması halinde, soruşturma açılmaz. || {K} | Resmî Gazete'de yayımlanacak bir tebliğ ile soruşturma başlatılır. || {K} | Soruşturma başlatılıncaya kadar başvuru hakkında herhangi bir bilgi ifşa edilemez. || {K} | halinde, şikâyet yapılmamış sayılır.",
        yuva=[
            "Yönetmelik: ihmal edilebilir düzeyde soruşturma açılmaz (doğru)",
            "Yönetmelik: tebliğle başlatma (doğru)",
            "Yönetmelik: ifşa yasağı (doğru)",
            "Yönetmelik: şikâyetin geri çekilmesi (doğru)",
        ],
        yakinlik="BİREBİR",
        tuzak=["SAYI", "TERSİNE"],
        duzey=["AYIRT"],
        profil=[3],
        olumsuz=True,
    ),
]
