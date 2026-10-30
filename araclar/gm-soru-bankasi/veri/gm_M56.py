# GM Soru Bankası — M56: İthalat Rejimi Kararı, İlave Gümrük Vergisi Kararı ve İthalat Tebliğleri (2026) (16 soru)
# Gümrük Koçu - Ufuk Çetintaş
K = "56-ithalat-rejimi-karari-teblig.txt"
IGV = "İthalatta İlave Gümrük Vergisi Uygulanmasına İlişkin Karar"
GTS = "Genelleştirilmiş Tercihler Sistemine İlişkin Tebliğ (İthalat: 2026/6)"


def s(**k):
    base = dict(
        konu="İthalat Rejimi ve İthalat Tebliğleri",
        blok="M56",
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
    # 1 ---------------- İRK: özel nitelikli eşya (olumsuz) ----------------
    s(
        kalip="KAPSAM_DIŞI",
        z="O",
        madde="İthalat Rejimi Kararı (3350) md. 7, 9",
        cek="Özel nitelikli eşya: eski, kullanılmış, yenileştirilmiş, kusurlu (defolu) ve yatık eşya; ithali izne tabidir. Nihai kullanım ayrı bir uygulamadır.",
        kok=[
            "İthalat Rejimi Kararına göre ithali izne tabi olan “özel nitelikli eşya” arasında aşağıdakilerden hangisi sayılmamıştır?"
        ],
        d="Nihai kullanım kapsamında indirimli gümrük vergisiyle ithal edilen eşya",
        c=[
            "Eski eşya",
            "Yenileştirilmiş eşya",
            "Kusurlu (defolu) eşya",
            "Yatık (zamanla dayanıklılığını yitirmiş) eşya",
        ],
        g="İthalat Rejimi Kararı “özel nitelikli eşya” başlığı altında eski, kullanılmış, yenileştirilmiş, kusurlu (defolu) ve yatık (zamanla dayanıklılığını yitirmiş) eşyanın ithalinin izne tabi olduğunu düzenler. Nihai kullanım kapsamında indirimli gümrük vergisiyle ithal edilen eşya ise bu sayımda yer almaz; Kararın listelerinde “Üretimi Gerçekleştirilecek Nihai Ürün” sütununda gösterilen ürünlerin imalinde kullanılmak kaydıyla ithal edilen eşyaya gösterilen oranda gümrük vergisi uygulanır ve bu eşya gümrük mevzuatının nihai kullanıma ilişkin hükümlerine tabi olur. En güçlü tuzak yatık eşyadır: kelime alışılmadık olduğu için listede yokmuş gibi görünür, fakat zamanla dayanıklılığını yitirmiş eşya Kararda açıkça sayılmıştır. Bu nedenle doğru cevap 'Nihai kullanım kapsamında indirimli gümrük vergisiyle ithal edilen eşya' seçeneğidir. (MD İRK 7, 9)",
        kanit=f"{K} | Eski, kullanılmış, yenileştirilmiş, kusurlu (defolu) ve yatık (zamanla dayanıklılığını yitirmiş) eşyanın ithali izne tabidir. || {K} | Özel Nitelikli Eşya || {K} | ithal edilmesi halinde karşısında gösterilen oranda gümrük vergisi uygulanır ve bu halde gümrük mevzuatının nihai kullanıma ilişkin hükümlerine tabidir.",
        yuva=[
            "İRK özel nitelikli eşya: eski (listede)",
            "Aynı liste: yenileştirilmiş (listede)",
            "Aynı liste: kusurlu (defolu) (listede)",
            "Aynı liste: yatık (listede; terim yabancı geldiği için tuzak)",
        ],
        yakinlik="BİREBİR",
        tuzak=["LİSTE-DIŞI", "TERİM"],
        duzey=["TANIMA"],
        profil=[1, 3],
        olumsuz=True,
        cikmis="2024/4; 2022/21",
    ),
    # 2 ---------------- İRK: VKN aranmayan ithalat (kitap ve yayınlar) ----------------
    s(
        kalip="ŞART",
        z="O",
        madde="İthalat Rejimi Kararı (3350) md. 8, 11, 13",
        cek="VKN şartı aranmaz: özel anlaşmalara dayanan ithalat, kitap ve yayınlar, fuarda perakende satışına izin verilen eşya.",
        kok=[
            "İthalat Rejimi Kararına göre ithalat işlemlerini vergi kimlik numarası verilen kişiler ve hukuki tasarruf yetkisi tanınan kişi ortaklıkları yürütür. Aşağıdaki ithalatlardan hangisinde vergi kimlik numarasına sahip olma şartı aranmaz?"
        ],
        d="Kitap ve diğer yayınların ithalatında",
        c=[
            "Kamu kurum ve kuruluşlarınca serbest dolaşıma giriş rejimi kapsamında yapılan ithalatta",
            "Tarife kontenjanı ve kota uygulamaları kapsamında yapılan ithalatta",
            "Kullanılmış veya yenileştirilmiş eşyanın ithalatında",
            "Türk müteahhitlik firmalarının yurt dışında üstlendikleri işlerle ilgili satın aldıkları makine ve teçhizatın ithalatında",
        ],
        g="İthalat Rejimi Kararına göre Vergi Usul Kanunu uyarınca vergi kimlik numarası verilen her gerçek ve tüzel kişi ile hukuki tasarruf yetkisi tanınan kişi ortaklıkları ithalat yapabilir. Ancak üç halde vergi kimlik numarasına sahip olma şartı aranmaz: özel anlaşmalara dayanan ithalat, kitap ve diğer yayınların ithalatı ve ülkemizde açılan uluslararası fuar ve sergilerde Bakanlıkça perakende satışına izin verilen eşyanın ithalatı. Kamu kurum ve kuruluşlarının serbest dolaşıma giriş rejimi kapsamındaki ithalatında Bakanlığın izni aranır; gözetim, tarife kontenjanı ve kota uygulamalarında ilgili mevzuatta ithalat yapacak kişiler için özel şartlar belirlenebilir; kullanılmış eşya izne tabidir; yurt dışı müteahhitlik makine ve teçhizatının ithali Bakanlığın iznine bağlıdır. Bu hükümlerin hiçbiri vergi kimlik numarası şartını kaldırmaz. En güçlü tuzak tarife kontenjanıdır: bu ithalatta kişiler için özel şartlar konabildiği için genel şartın da kalktığı sanılır. Bu nedenle doğru cevap 'Kitap ve diğer yayınların ithalatında' seçeneğidir. (MD İRK 8, 11, 13)",
        kanit=f"{K} | b) Kitap ve diğer yayınların ithalatında, || {K} | vergi kimlik numarasına sahip olma şartı aranmaz. || {K} | serbest dolaşıma giriş rejimi kapsamında yapılacak ithalata ilişkin gümrük beyannamesinin tescilinde Bakanlığın izni aranır. || {K} | ithalat işlemlerini yapmaya hakkı olacak kişilere ilişkin olarak, gerektiğinde ilgili mevzuatında özel şartlar belirlenebilir. || {K} | satın aldıkları makina ve teçhizatın Türkiye'ye kesin ve geçici ithali ile bunlara ilişkin süre uzatımları Bakanlığın iznine bağlıdır.",
        yuva=[
            "İRK kamu ithalatı: Bakanlık izni aranır",
            "İRK: gözetim, kontenjan, kota için özel şartlar",
            "İRK özel nitelikli eşya: izne tabi",
            "İRK yurt dışı müteahhitlik: Bakanlık izni",
        ],
        yakinlik="BİREBİR",
        tuzak=["İSTİSNA", "KOMŞU"],
        duzey=["AYIRT"],
        profil=[3],
        olumsuz=False,
        cikmis="2021/55",
    ),
    # 3 ---------------- İRK genel esaslar (önermeli) ----------------
    s(
        kalip="ÖNERMELİ",
        z="O",
        madde="İthalat Rejimi Kararı (3350) md. 3, 5",
        cek="Önlem kapsamı dışındaki eşyanın ithali serbest; kanunla kuruma bırakılmış eşya o kurumca; yetki Ticaret Bakanlığında, kısmen devredilebilir.",
        kok=[
            "İthalat Rejimi Kararına göre;",
            "I. Kamu ahlakı, kamu düzeni veya kamu güvenliği, insan, hayvan ve bitki sağlığı ile sınai ve ticari mülkiyetin korunması amaçlarıyla alınan önlemlerin kapsamı dışındaki eşyanın ithali serbesttir.",
            "II. İthalat izinlerinin verilmesi ve ithal eşya fiyatlarının kontrolüne ilişkin görev ve yetkiler, Tebliğ veya talimatla diğer kamu kurumlarına ve/veya ihracatçı birlikleri genel sekreterliklerine kısmen veya tamamen devredilebilir.",
            "III. İthalatı kanunlarla belirli kurum ve kuruluşlara bırakılmış eşya, ancak bu kurum ve kuruluşlar ya da bunlarca yetkilendirilenler tarafından ithal edilebilir.",
            "IV. Kararda yer alan hususlara ilişkin tebliğler çıkarmaya ve özel ve zorunlu durumları inceleyip sonuçlandırmaya Hazine ve Maliye Bakanlığı yetkilidir.",
            "ifadelerinden hangileri doğrudur?",
        ],
        d="I, II ve III",
        c=["I ve II", "I ve IV", "II, III ve IV", "I, II, III ve IV"],
        sirali=True,
        siklar=[
            "I ve II",
            "I ve IV",
            "I, II ve III",
            "II, III ve IV",
            "I, II, III ve IV",
        ],
        g="İthalat Rejimi Kararına göre kamu ahlakı, kamu düzeni veya güvenliği, insan, hayvan ve bitki sağlığı ile sınai ve ticari mülkiyetin korunması amaçlarıyla alınan önlemlerin kapsamı dışındaki eşyanın ithali serbesttir (I doğru). İthalat izinlerinin verilmesi, önlem ve kısıtlamaların uygulanması ve ithal eşya fiyatlarının kontrolüne ilişkin görev ve yetkiler, Bakanlıkça kullanılabileceği gibi Tebliğ veya talimatla diğer kamu kurumlarına ve/veya ihracatçı birlikleri genel sekreterliklerine kısmen veya tamamen devredilebilir (II doğru). İthalatı kanunlarla belirli kurum ve kuruluşlara bırakılmış eşya ancak bu kurum ve kuruluşlar veya bunlarca yetkilendirilenler tarafından ithal edilebilir (III doğru). Kararda yer alan hususlara ilişkin tebliğ çıkarmaya, izin ve talimat vermeye, özel ve zorunlu durumları inceleyip sonuçlandırmaya Hazine ve Maliye Bakanlığı değil, Ticaret Bakanlığı yetkilidir (IV yanlış). En güçlü tuzak IV. önermedir: ithalat bedellerinin ödenmesi kambiyo mevzuatına tabi olduğundan, kambiyoyu yürüten bakanlığın Kararda da yetkili olduğu sanılır. Bu nedenle doğru cevap 'I, II ve III' seçeneğidir. (MD İRK 3, 5)",
        kanit=f"{K} | sınai ve ticari mülkiyetin korunması amaçlarıyla ilgili mevzuat hükümleri çerçevesinde alınan önlemlerin kapsamı dışındaki eşyanın ithali serbesttir. || {K} | bu Karara istinaden yayımlanacak Tebliğ veya verilecek talimatla, diğer kamu kurumları ve/veya ihracatçı birlikleri genel sekreterliklerine de kısmen veya tamamen devredilebilir. || {K} | İthalatı kanunlarla belirli kurum ve kuruluşlara bırakılmış eşya ithali ancak, bu kurum ve kuruluşlar tarafından veya bu kurum ve kuruluşlar tarafından yetkilendirilenler tarafından yapılabilir. || {K} | özel ve zorunlu durumları inceleyip sonuçlandırmaya Ticaret Bakanlığı (Bakanlık) yetkilidir.",
        yuva=[
            "I ve II: kurumlara bırakılmış eşya hükmünü bilmeyen aday",
            "I ve IV: yetkiyi Hazine ve Maliye Bakanlığında sanan aday",
            "II, III ve IV: ithalat serbestisini bilmeyen, yetkili makamı karıştıran aday",
            "I, II, III ve IV: yetkili makamı karıştıran aday",
        ],
        yakinlik="PARAFRAZ",
        tuzak=["MAKAM", "KOMŞU"],
        duzey=["AYIRT", "BÜTÜNLEŞİK"],
        profil=[2, 3],
        olumsuz=False,
        cikmis="2022/21",
    ),
    # 4 ---------------- İRK: ticaret politikası önlemleri mevzuatı (grup) ----------------
    s(
        kalip="KAPSAM",
        z="Z",
        madde="İthalat Rejimi Kararı (3350) md. 4",
        cek="Ticaret politikası önlemleri: haksız rekabet, korunma, kota ve tarife kontenjanı, gözetim, iki tekstil düzenlemesi ve ticari hakların korunması mevzuatıyla yürütülür.",
        kok=[
            "İthalat Rejimi Kararına göre, aşağıdakilerden hangisinde verilen mevzuatın tamamı ticaret politikası önlemlerinin yürütüldüğü mevzuat arasında sayılmıştır?"
        ],
        d="İthalatta Korunma Önlemleri, İthalatta Gözetim Uygulanması, Türkiye'nin Ticari Haklarının Korunması",
        c=[
            "İthalatta Haksız Rekabetin Önlenmesi, kambiyo mevzuatı, İthalatta Kota ve Tarife Kontenjanı İdaresi",
            "Ürün Güvenliği ve Denetimi, İthalatta Gözetim Uygulanması, Belirli Tekstil Ürünleri İthalatında Gözetim ve Korunma Önlemleri",
            "Askıya Alma Sistemi, İthalatta Korunma Önlemleri, İthalatta Haksız Rekabetin Önlenmesi",
            "Kamu İhale mevzuatı, Türkiye'nin Ticari Haklarının Korunması, İthalatta Kota ve Tarife Kontenjanı İdaresi",
        ],
        g="İthalat Rejimi Kararına göre ticaret politikası önlemleri; İthalatta Haksız Rekabetin Önlenmesi, İthalatta Korunma Önlemleri, İthalatta Kota ve Tarife Kontenjanı İdaresi, İthalatta Gözetim Uygulanması, Belirli Tekstil Ürünleri İthalatında Gözetim ve Korunma Önlemleri, belirli ülkeler menşeli tekstil ürünlerinde gözetim ve korunma önlemleri ile Türkiye'nin Ticari Haklarının Korunması hakkındaki hükümler çerçevesinde yürütülür. Yalnız korunma, gözetim ve ticari hakların korunması mevzuatından oluşan grubun tamamı bu listededir. Kambiyo mevzuatı ithalat bedellerinin ödenmesini düzenler; Ürün Güvenliği ve Denetimi mevzuatı ithalat tebliğlerinde izin ve belgelerin ayrıca alınacağı mevzuat olarak anılır; Askıya Alma Sistemi ayrı bir ithalat tebliğiyle düzenlenen gümrük vergisi muafiyetidir; Kamu İhale mevzuatı ise kamu ithalatında izin hükmünde geçer. En güçlü tuzak Askıya Alma Sistemidir: tarife kontenjanıyla birlikte anıldığı için ticaret politikası önlemi sanılır. Bu nedenle doğru cevap 'İthalatta Korunma Önlemleri, İthalatta Gözetim Uygulanması, Türkiye'nin Ticari Haklarının Korunması' seçeneğidir. (MD İRK 4)",
        kanit=f"{K} | Ticaret politikası önlemleri; İthalatta Haksız Rekabetin Önlenmesi Hakkında || {K} | İthalatta Korunma Önlemleri Hakkında || {K} | İthalatta Gözetim Uygulanması Hakkında || {K} | Türkiye'nin Ticari Haklarının Korunması Hakkında hükümleri çerçevesinde yürütülür. || {K} | İthalat bedellerinin ödenmesi, kambiyo mevzuatı hükümlerine tabidir. || {K} | Ürün Güvenliği ve Denetimi mevzuatı ve diğer mevzuat kapsamında alınması gereken izin ve belgelerin yerine geçmez || {K} | ASKIYA ALMA SİSTEMİNE İLİŞKİN TEBLİĞ (İTHALAT: 2026/18) || {K} | Kamu İhale Kanununun 2 nci maddesinde sayılan kamu kurum ve kuruluşları",
        yuva=[
            "Kambiyo mevzuatı: İRK'da ithalat bedellerinin ödenmesine ilişkin",
            "Ürün Güvenliği ve Denetimi: ithalat tebliğlerinde ayrıca alınacak izinler",
            "Askıya Alma Sistemi Tebliği: gümrük vergisi muafiyeti",
            "Kamu İhale mevzuatı: İRK kamu ithalatı hükmü",
        ],
        yakinlik="PARAFRAZ",
        tuzak=["LİSTE-DIŞI", "KOMŞU"],
        duzey=["AYIRT"],
        profil=[3],
        olumsuz=False,
        cikmis="2024/34",
    ),
    # 5 ---------------- İRK: ek mali yükümlülük (olumsuz) ----------------
    s(
        kalip="YANLIŞ",
        z="O",
        madde="İthalat Rejimi Kararı (3350) md. 9, 10",
        cek="EMY: yükümlülüğün doğduğu tarihteki oranla, o tarihte gümrük idaresince tahsil; muaf ithalat EMY'ye tabi değil; 6183 uygulanır; TKF atıfları EMY'ye.",
        kok=[
            "İthalat Rejimi Kararına göre ek mali yükümlülüğün tahakkuk ve tahsiline ilişkin aşağıdaki ifadelerden hangisi yanlıştır?"
        ],
        d="Ek mali yükümlülük, eşyanın serbest dolaşıma girişini izleyen ayın sonuna kadar Ticaret Bakanlığınca tahsil edilir.",
        c=[
            "Ek mali yükümlülük ödenerek ithal edilecek eşya, gümrük yükümlülüğünün doğduğu tarihte geçerli miktar ve oranlar kadar ek mali yükümlülüğe tabidir.",
            "Gümrük Kanunu çerçevesinde gümrük vergilerinden muaf olarak gerçekleştirilecek ithalat ek mali yükümlülüğe tabi değildir.",
            "Süresi içinde yatırılmayan ek mali yükümlülük hakkında Amme Alacaklarının Tahsil Usulü Hakkında Kanun hükümleri uygulanır.",
            "İthalat işlemlerine ilişkin mevzuatta toplu konut fonu ve ilave toplu konut fonuna yapılan atıflar ek mali yükümlülüğe yapılmış sayılır.",
        ],
        g="İthalat Rejimi Kararına göre ek mali yükümlülük ödenerek ithal edilecek eşya, gümrük yükümlülüğünün doğduğu tarihte geçerli miktar ve oranlar kadar ek mali yükümlülüğe tabidir; Gümrük Kanunu çerçevesinde gümrük vergilerinden muaf olarak yapılan ithalat ise ek mali yükümlülüğe tabi değildir. Ek mali yükümlülük gümrük yükümlülüğünün doğduğu tarihte gümrük idarelerince tahsil edilir; süresinde yatırılmazsa 6183 sayılı Kanun hükümleri uygulanır ve hakkında gümrük vergisinin tabi olduğu usul ve hükümler geçerlidir. İthalat mevzuatında toplu konut fonu ve ilave toplu konut fonuna yapılan atıflar ek mali yükümlülüğe yapılmış sayılır. Ek mali yükümlülüğün izleyen ay sonuna kadar Ticaret Bakanlığınca tahsil edildiği ifadesi hem zamanı hem tahsil eden idareyi değiştirdiği için yanlıştır. En güçlü tuzak muafiyet ifadesidir: ek mali yükümlülük ayrı bir yük olduğu için gümrük vergisi muafiyetinin ona etki etmediği sanılır. Bu nedenle doğru cevap 'Ek mali yükümlülük, eşyanın serbest dolaşıma girişini izleyen ayın sonuna kadar Ticaret Bakanlığınca tahsil edilir.' seçeneğidir. (MD İRK 10)",
        kanit=f"{K} | Ek mali yükümlülük ödenerek ithal edilecek eşya, gümrük yükümlülüğünün doğduğu tarihte geçerli miktar ve oranlar kadar ek mali yükümlülüğe tabidir. || {K} | gümrük vergilerinden muaf olarak gerçekleştirilecek ithalat, ek mali yükümlülüğe tabi değildir. || {K} | Ek mali yükümlülük, gümrük yükümlülüğünün doğduğu tarihte gümrük idarelerince tahsil edilir. || {K} | Amme Alacaklarının Tahsil Usulü Hakkında Kanun hükümleri uygulanır. || {K} | toplu konut fonu ve ilave toplu konut fonuna yapılan atıflar, ek mali yükümlülüğe yapılmış sayılır.",
        yuva=[
            "İRK: EMY'nin doğuş anı (doğru)",
            "İRK: muaf ithalat EMY'ye tabi değil (doğru)",
            "İRK: 6183 sayılı Kanunun uygulanması (doğru)",
            "İRK: TKF atıflarının EMY'ye yapılmış sayılması (doğru)",
        ],
        yakinlik="BİREBİR",
        tuzak=["MAKAM", "BAŞLANGIÇ"],
        duzey=["AYIRT"],
        profil=[3],
        olumsuz=True,
    ),
    # 6 ---------------- İRK: II ile V/VI çakışması → en düşük oran ----------------
    s(
        kalip="SONUÇ",
        z="O",
        madde="İthalat Rejimi Kararı (3350) md. 9",
        cek="II sayılı listedeki eşya V veya VI sayılı listede de yer alıyorsa II, V ve VI sayılı listelerdeki oranlardan düşük olanı uygulanır.",
        kok=[
            "İthalat Rejimi Kararına göre, II sayılı liste kapsamında yer alan eşyanın aynı zamanda V veya VI sayılı listede de yer alması halinde uygulanacak gümrük vergisi oranı nasıl belirlenir?"
        ],
        d="II, V ve VI sayılı listelerde belirtilen gümrük vergisi oranlarından daha düşük olanı uygulanır.",
        c=[
            "Yalnız V veya VI sayılı listede belirtilen oran uygulanır.",
            "Yalnız II sayılı listede belirtilen oran uygulanır.",
            "II sayılı listedeki oran ile Avrupa Birliği Ortak Gümrük Tarifesindeki en düşük oran karşılaştırılarak düşük olanı uygulanır.",
            "II, V ve VI sayılı listelerde belirtilen gümrük vergisi oranlarından daha yüksek olanı uygulanır.",
        ],
        g="İthalat Rejimi Kararına göre ithalatta uygulanacak gümrük vergisi oranları ve ek mali yükümlülükler ekli listelerde gösterilir. II sayılı liste kapsamındaki eşyanın aynı zamanda V veya VI sayılı listede de yer alması halinde II, V ve VI sayılı listelerde belirtilen gümrük vergisi oranlarından daha düşük olanı uygulanır. V sayılı liste gümrük vergisi askıya alınan sanayi ürünlerini, VI sayılı liste nihai kullanım kapsamında sivil hava taşıtlarında kullanılacak ürünleri içerir. İthal oranı ile Avrupa Birliği Ortak Gümrük Tarifesindeki en düşük oranın karşılaştırılması ise serbest bölge, antrepo veya dahilde işleme kapsamındaki eşyanın işlem görmüş ürün olarak AB'ye ihracında telafi edici verginin hesaplanmasına ilişkin kuraldır. En güçlü tuzak yalnız V veya VI sayılı listenin uygulanacağını söyleyen seçenektir: bu listeler indirimli oran içerdiği için hep onların uygulanacağı sanılır, oysa Karar üç listenin oranlarını karşılaştırır. Bu nedenle doğru cevap 'II, V ve VI sayılı listelerde belirtilen gümrük vergisi oranlarından daha düşük olanı uygulanır.' seçeneğidir. (MD İRK 9)",
        kanit=f"{K} | II sayılı liste kapsamında yer alan eşyanın aynı zamanda V veya VI sayılı listede yer alması durumunda, II, V ve VI sayılı listelerde belirtilen gümrük vergisi oranlarından daha düşük olanı uygulanır. || {K} | Avrupa Birliği Ortak Gümrük Tarifesinde uygulanan en düşük gümrük vergisi oranı karşılaştırılır ve daha düşük olan vergi oranı tatbik edilir. || {K} | V Sayılı Liste Gümrük Vergisi Askıya Alınan Sanayi Ürünleri",
        yuva=[
            "Kuralın yarısı: V/VI'nın her durumda uygulanacağı sanısı",
            "Kuralın yarısı: II'nin her durumda uygulanacağı sanısı",
            "İRK: AB'ye ihracatta TEV hesabındaki karşılaştırma",
            "Ters çevrilmiş kural (yüksek oran)",
        ],
        yakinlik="BİREBİR",
        tuzak=["KOMŞU", "TERSİNE"],
        duzey=["AYIRT"],
        profil=[3],
        olumsuz=False,
    ),
    # 7 ---------------- İRK değişiklik (2026): geçiş süresi 31 Ocak 2026 ----------------
    s(
        kalip="SÜRE",
        z="Z",
        madde="İthalat Rejimi Kararında Değişiklik Yapılmasına İlişkin Karar (10790) geçici md. 1, 2",
        cek="1/1/2026'da EMY ihdas edilen ya da GV/EMY'si artan eşyada beyanname 31/1/2026'ya (dâhil) kadar tescil edilirse önceki oranlar uygulanır.",
        kok=[
            "31 Aralık 2025 tarihli İthalat Rejimi Kararında Değişiklik Yapılmasına İlişkin Karara göre, 1 Ocak 2026 itibarıyla ek mali yükümlülük ihdas edilen ya da gümrük vergisi ve/veya ek mali yükümlülüğü artırılan eşyanın ithalatında önceki oranların uygulanabilmesi için gümrük beyannamesinin en geç hangi tarihe kadar tescil edilmesi gerekir?"
        ],
        d="31 Ocak 2026 (bu tarih dâhil)",
        c=[
            "28 Şubat 2026 (bu tarih dâhil)",
            "31 Mart 2026 (bu tarih dâhil)",
            "30 Nisan 2026 (bu tarih dâhil)",
            "Kararın yürürlüğe girdiği tarihten itibaren 45 gün içinde",
        ],
        g="31 Aralık 2025 tarihli değişiklik Kararıyla İthalat Rejimi Kararının listeleri 1 Ocak 2026'dan itibaren yenilenmiştir. Kararın geçici hükmüne göre 1 Ocak 2026 itibarıyla ek mali yükümlülük ihdas edilen ya da gümrük vergisi ve/veya ek mali yükümlülüğü artırılan eşyanın ithalatına ilişkin gümrük beyannamesi 31 Ocak 2026 tarihine kadar (bu tarih dâhil) tescil edilirse 1 Ocak 2026'dan önceki gümrük vergisi ve/veya ek mali yükümlülük uygulanır. 31 Mart 2026, A.TR eşliğinde gelen ve Bölgesel Konvansiyona taraf ülkeler menşeli beyan edilen eşyadan tercihli menşe tevsiki aranmaksızın II sayılı listedeki ek mali yükümlülüğün alınmayacağı son tarihtir; 30 Nisan 2026, VII sayılı listedeki bir nihai kullanım oranının bitiş tarihidir; 28 Şubat tarihi 2022 listelerinin geçiş hükmünde, 45 günlük süre ise eski kararlara ilişkin özet beyan geçiş hükmünde yer alır. En güçlü tuzak 31 Mart 2026'dır: aynı değişiklik Kararının bir başka geçici hükmüdür, fakat ek mali yükümlülük alınmayan A.TR'li eşyaya ilişkindir. Bu nedenle doğru cevap '31 Ocak 2026 (bu tarih dâhil)' seçeneğidir. (MD 10790 sayılı CK geçici md. 1, 2)",
        kanit=f"{K} | 1/1/2026 tarihi itibarıyla ek mali yükümlülük ihdas edilen ya da gümrük vergisi ve/veya ek mali yükümlülüğü artırılan eşyanın ithalatına ilişkin gümrük beyannamesinin 31/1/2026 tarihine kadar (bu tarih dâhil) tescil edilmesi hâlinde 1/1/2026 tarihinden önceki gümrük vergisi ve/veya ek mali yükümlülük uygulanır. || {K} | 31/3/2026 tarihine kadar (bu tarih dâhil) 3350 sayılı Kararın eki II sayılı listede belirtilen ek mali yükümlülük alınmaz. || {K} | Söz konusu gümrük vergisi 30 Nisan 2026 tarihine kadar (bu tarih dahil) uygulanır. || {K} | 28/2/2022 tarihine kadar (Bu tarih dahil) || {K} | en geç 45 gün içerisinde gümrüklere sunularak",
        yuva=[
            "İRK 2022 geçiş hükmü: 28 Şubat (2022)",
            "10790 sayılı CK geçici md. 2: A.TR'li eşyada EMY alınmayan son tarih",
            "VII sayılı liste dipnotu: nihai kullanım oranının bitişi",
            "İRK geçici md. 5: özet beyan için 45 gün",
        ],
        yakinlik="BİREBİR",
        tuzak=["YAKIN-SAYI", "KOMŞU"],
        duzey=["HATIRLAMA", "AYIRT"],
        profil=[1, 3],
        olumsuz=False,
        guncellik="31.12.2025 (10790 sayılı CK)",
    ),
    # 8 ---------------- İGV: toplam vergi sınırı 474 sayılı Kanun (boşluk) ----------------
    s(
        kalip="BOŞLUK",
        z="O",
        madde="İthalatta İlave Gümrük Vergisi Uygulanmasına İlişkin Karar (3351) md. 2",
        cek="GV + İGV toplamı 474 sayılı Kanun hadlerinin 50'ye kadar yükseltilmiş ya da %50 artırılmış düzeyini aşamaz; aşarsa bu düzeylerden fazla olan uygulanır.",
        kok=[
            f"{IGV}'a göre; “Her halükarda hesaplanan toplam vergi oranı (İthalat Rejimi Kararına ekli II ve III sayılı listelerde yer alan gümrük vergisi ile bu Karar kapsamında alınacak ilave gümrük vergisi toplamı), 474 sayılı Gümrük Giriş Tarife Cetveli Hakkında Kanunda gösterilen hadlerin (……) kadar yükseltilmiş ya da yüzde (……) artırılmış düzeyini aşamaz. Aşması durumunda bu düzeylerden daha (……) olan uygulanır.”",
            "Yukarıdaki cümlede boş bırakılan yerlere sırasıyla aşağıdakilerden hangisi gelmelidir?",
        ],
        d="50'ye – 50 – fazla",
        c=[
            "50'ye – 50 – az",
            "35'e – 50 – fazla",
            "50'ye – 25 – az",
            "100'e – 50 – fazla",
        ],
        g="İlave Gümrük Vergisi Kararına göre İthalat Rejimi Kararına ekli II ve III sayılı listelerdeki gümrük vergisi ile ilave gümrük vergisinin toplamı, 474 sayılı Gümrük Giriş Tarife Cetveli Hakkında Kanunda gösterilen hadlerin 50'ye kadar yükseltilmiş ya da yüzde 50 artırılmış düzeyini aşamaz. Toplam bu düzeyi aşarsa 474 sayılı Kanunda gösterilen hadlerin 50'ye kadar yükseltilmiş ya da yüzde 50 artırılmış düzeyinden daha fazla olanı uygulanır; hüküm bu biçimiyle 31.12.2023 tarihinde değiştirilmiştir. Sınırın iki yolla hesaplanan düzeyinden daha az olanın uygulanacağı düşüncesi hükmü tersine çevirir; 35, 25 ve 100 değerleri ise kaynakta yer almayan sayılardır. En güçlü tuzak “50'ye – 50 – az” seçeneğidir: iki sayı doğrudur, yalnız iki düzeyden hangisinin uygulanacağı ters çevrilmiştir. Bu nedenle doğru cevap '50'ye – 50 – fazla' seçeneğidir. (MD İGV Kararı md. 2)",
        kanit=f"{K} | 474 sayılı Gümrük Giriş Tarife Cetveli Hakkında Kanunda gösterilen hadlerin 50'ye kadar yükseltilmiş ya da % 50 artırılmış düzeyini aşamaz. || {K} | Aşması durumunda 474 sayılı Kanunda gösterilen hadlerin 50'ye kadar yükseltilmiş ya da % 50 artırılmış düzeyinden daha fazla olan uygulanır. (31.12.2023 / 32416 sayılı 3. Mükerrer R.G. 8044 Karar ile değişik)",
        yuva=[
            "Ters çevrilmiş sonuç (az olanı)",
            "Sayı tuzağı: kaynakta 35 yok",
            "Sayı tuzağı ve ters sonuç",
            "Sayı tuzağı: kaynakta 100 yok",
        ],
        yakinlik="BİREBİR",
        tuzak=["SAYI", "TERSİNE"],
        duzey=["HATIRLAMA"],
        profil=[1],
        olumsuz=False,
    ),
    # 9 ---------------- İGV: hangi halde alınır (güncellik 11.07.2026) ----------------
    s(
        kalip="TABİ",
        z="Z",
        madde="İthalatta İlave Gümrük Vergisi Uygulanmasına İlişkin Karar (3351) md. 2, 4",
        cek="A.TR ile gelen AB ve Türk menşeli olmayan eşyadan DÜ oranıyla İGV alınır; çapraz kümülasyon menşei tevsik edilirse ve Karardaki istisnalarda alınmaz.",
        kok=[
            f"{IGV}'a göre, Karar eki tablolarda yer alan eşya bakımından aşağıdaki hallerin hangisinde ilave gümrük vergisi alınır?"
        ],
        d="A.TR dolaşım belgesi eşliğinde ithal edilen, Avrupa Birliği ve Türk menşeli olmayan ve çapraz menşe kümülasyon sistemine dahil bir ülke menşei de tevsik edilmeyen eşyanın ithalatında",
        c=[
            "İthalat Rejimi Kararı eki listelerdeki oran üzerinden vergi tahsil edilen ve gümrük gözetimi altındayken A.TR dolaşım belgesi düzenlenerek Avrupa Birliği'ne üye ülkelere ihraç edilen eşyada",
            "Aynı zamanda İthalat Rejimi Kararına ekli V veya VI sayılı listede yer alan eşyada",
            "Tarife kontenjanı kapsamında sıfır ya da indirimli gümrük vergisiyle ithal edilen eşyada",
            "Gümrük vergisi muafiyetinden yararlanılarak gerçekleştirilen ithalatta",
        ],
        g="İlave Gümrük Vergisi Kararına göre Karar eki tablolarda yer alan ve A.TR dolaşım belgesi eşliğinde ithal edilen AB ve Türk menşeli olmayan eşyadan “Diğer Ülkeler” sütunundaki oran üzerinden ilave gümrük vergisi alınır; Türkiye'nin taraf olduğu STA'lar çerçevesinde çapraz menşe kümülasyon sistemine dahil ülkeler menşeli eşyanın tercihli menşei tevsik edilirse alınmaz. Karar, uygulanmayacağı halleri ayrıca sayar: dahilde işleme kapsamındaki ürünlerde telafi edici vergi hesabı; İthalat Rejimi Kararı oranıyla vergisi tahsil edilip gümrük gözetimi altındayken A.TR ile AB'ye ihraç edilen eşya; aynı zamanda V veya VI sayılı listede yer alan eşya; nihai kullanımda gümrük vergisi sıfır olan eşyanın aynı amaçla ithali; tarife kontenjanı kapsamında sıfır veya indirimli vergiyle ithal edilen eşya ve gümrük vergisi muafiyetinden yararlanılarak yapılan ithalat. Muafiyet hükmü 11.07.2026 tarihinde değiştirilerek genel muafiyet hallerini kapsayacak biçimde yazılmıştır. En güçlü tuzak AB'ye A.TR'li ihracattır: eşya A.TR ile dolaştığı için İGV alınacağı sanılır, ancak bu ihracat açıkça istisnadır. Bu nedenle doğru cevap 'A.TR dolaşım belgesi eşliğinde ithal edilen, Avrupa Birliği ve Türk menşeli olmayan ve çapraz menşe kümülasyon sistemine dahil bir ülke menşei de tevsik edilmeyen eşyanın ithalatında' seçeneğidir. (MD İGV Kararı md. 2, 4)",
        kanit=f"{K} | A.TR dolaşım belgesi eşliğinde ithal edilen Avrupa Birliği ve Türk menşeli olmayan eşyadan “Diğer Ülkeler” sütununda belirtilen oran üzerinden ilave gümrük vergisi alınır. || {K} | çapraz menşe kümülasyon sistemine dahil ülkeler menşeli eşyadan tercihli menşeinin tevsiki halinde ilave gümrük vergisi alınmaz. || {K} | gümrük gözetimi altındayken A.TR dolaşım belgesi düzenlenerek Avrupa Birliği'ne üye ülkelere ihraç edilmesi halinde, bu Karar kapsamındaki ilave gümrük vergisi uygulanmaz. || {K} | V veya VI sayılı listede yer alması durumunda ilave gümrük vergisi uygulanmaz. || {K} | Tarife kontenjanı kapsamında “0” (sıfır) ya da indirimli gümrük vergisi ile ithal edilen eşyaya ilave gümrük vergisi uygulanmaz. || {K} | Gümrük vergisi muafiyetinden yararlanılarak gerçekleştirilen ithalatta ilave gümrük vergisi uygulanmaz. (11.07.2026 / 33307 sayılı R.G. 11508 Kararla değişik)",
        yuva=[
            "İGV Kararı uygulanmayacak haller: A.TR ile AB'ye ihracat",
            "İGV Kararı uygulanmayacak haller: V veya VI sayılı liste",
            "İGV Kararı uygulanmayacak haller: tarife kontenjanı",
            "İGV Kararı uygulanmayacak haller: gümrük vergisi muafiyeti (11.07.2026)",
        ],
        yakinlik="PARAFRAZ",
        tuzak=["İSTİSNA", "KOMŞU"],
        duzey=["AYIRT", "UYGULAMA"],
        profil=[3, 4],
        olumsuz=False,
        guncellik="11.07.2026 (11508 sayılı Karar)",
    ),
    # 10 ---------------- GTS Tebliği: ilkeler ve indirimler (önermeli, yanlış yönlü) ----------------
    s(
        kalip="ÖNERMELİ",
        z="Z",
        madde="Genelleştirilmiş Tercihler Sistemine İlişkin Tebliğ (İthalat: 2026/6) md. 4, 5",
        cek="GTS: tek taraflı, bağlayıcı olmayan taviz; GYÜ hassas ürün: maktu %30 azaltım, nispi 3,5 puan (50–63'te %20); EAGÜ %0; %1 / 2 Avro altında askı.",
        kok=[
            f"{GTS}'e göre;",
            "I. Sistem, gümrük vergisi tavizlerinin tek taraflı olması ve tavizlerin verilişlerinin bağlayıcı olmaması ilkelerine dayanır.",
            "II. Gelişme yolundaki ülkeler grubunda yer alan ülkeler menşeli hassas ürünlerde maktu gümrük vergileri yüzde 30 oranında azaltılmıştır.",
            "III. Gelişme yolundaki ülkeler grubunda yer alan ülkeler menşeli hassas ürünlerde nispi gümrük vergileri, Diğer Ülkeler sütunundaki hadler üzerinden 5 puan indirilmiştir.",
            "IV. En az gelişmiş ülkeler grubunda yer alan ülkeler menşeli, II ve III sayılı listelerdeki sanayi ve tarım ürünlerinin (AKÇT ürünleri ve 93. fasıldaki eşya hariç) ithalatında gümrük vergisi yüzde 0 olarak uygulanır.",
            "V. Tercihli tarife uygulaması sonucunda nispi vergi oranının yüzde 3 veya daha az olması halinde gelişme yolundaki ülkeler için gümrük vergileri askıya alınmıştır.",
            "ifadelerinden hangileri yanlıştır?",
        ],
        d="III ve V",
        c=["I ve III", "II ve IV", "I, III ve V", "II, III ve V"],
        sirali=True,
        siklar=["I ve III", "II ve IV", "III ve V", "I, III ve V", "II, III ve V"],
        g="GTS Tebliğine göre sistem; tavizlerin tek taraflı olması, bağlayıcı olmaması, tercihlerin kısmen veya tümüyle kaldırılabilmesi ve en çok kayrılan ülke esasına dayalı indirimleri engellememesi ilkelerine dayanır (I doğru). Gelişme yolundaki ülkeler menşeli hassas ürünlerde maktu vergiler yüzde 30 oranında azaltılmıştır (II doğru). Aynı ürünlerde nispi vergiler Diğer Ülkeler sütunundaki hadler üzerinden 5 puan değil, 3,5 puan indirilmiştir; 50–63. fasıllardaki hassas ürünlerde ise yüzde 20 indirim yapılmıştır (III yanlış). En az gelişmiş ülkeler menşeli II ve III sayılı listelerdeki sanayi ve tarım ürünlerinde (AKÇT ürünleri ve 93. fasıl hariç) gümrük vergisi yüzde 0'dır (IV doğru). Tercihli tarife sonucunda nispi vergi oranı yüzde 3 değil, yüzde 1 veya daha az ya da maktu vergi 2 Avro veya daha az olursa gelişme yolundaki ülkeler için gümrük vergileri askıya alınmıştır (V yanlış). En güçlü tuzak III. önermedir: indirim puanla ifade edildiği için oranı hatırlamak zordur ve maktu vergideki yüzde 30 ile karıştırılır. Bu nedenle doğru cevap 'III ve V' seçeneğidir. (MD GTS Tebliği md. 4, 5)",
        kanit=f"{K} | a) Gümrük vergisi tavizlerinin TEK TARAFLI OLMASI, || {K} | b) Tavizlerin verilişlerinin BAĞLAYICI OLMAMASI, || {K} | MAKTU gümrük vergileri % 30 ORANINDA AZALTILMIŞ, || {K} | gümrük vergisi hadleri üzerinden 3,5 PUAN İNDİRİLMİŞTİR. || {K} | DÜ sütununda belirtilen gümrük vergisi hadleri üzerinden % 20 ORANINDA İNDİRİM YAPILMIŞTIR. || {K} | ve tarım ürünlerinin (AKÇT ürünleri ve 93. fasılda bulunan eşya hariç) ithalatında gümrük vergisi %0 OLARAK || {K} | NİSPİ vergi oranlarının % 1 veya DAHA AZ olması, || {K} | MAKTU vergilerin 2 AVRO veya DAHA AZ olması durumunda,",
        yuva=[
            "I ve III: temel ilkeleri yanlış sanan aday",
            "II ve IV: doğru önermeleri yanlış sanan aday",
            "I, III ve V: bağlayıcı olmama ilkesini bilmeyen aday",
            "II, III ve V: maktu indirim oranını yanlış bilen aday",
        ],
        yakinlik="PARAFRAZ",
        tuzak=["SAYI", "YAKIN-SAYI"],
        duzey=["AYIRT", "BÜTÜNLEŞİK"],
        profil=[2, 3],
        olumsuz=True,
    ),
    # 11 ---------------- GTS Tebliği: tavizlerin kaldırılması eşiği (%13,5 miktar) ----------------
    s(
        kalip="ORAN-TUTAR",
        z="Z",
        madde="Genelleştirilmiş Tercihler Sistemine İlişkin Tebliğ (İthalat: 2026/6) md. 8, 9",
        cek="Sektör tavizi kaldırılabilir: ülkeden sektör ithalatı önceki yıla göre miktar bazında %13,5+ artarsa ya da GTS toplamının değer bazında %14,5'ini aşarsa.",
        kok=[
            "Genelleştirilmiş Tercihler Sistemine İlişkin Tebliğe göre, GTS kapsamında tavizden faydalanan bir ülkeden bir sektör kapsamında yapılan ithalat bakımından, o sektördeki ürünlere sağlanan tavizlerin kaldırılabilmesine imkân veren hal aşağıdakilerden hangisidir?"
        ],
        d="Ülkeden sektör kapsamında yapılan ithalatın, aynı sektörde bir önceki yıl yapılan ithalata oranla miktar bazında yüzde 13,5 ve daha fazla oranda artması",
        c=[
            "Ülkeden sektör kapsamında yapılan ithalatın, aynı sektörde bir önceki yıl yapılan ithalata oranla değer bazında yüzde 13,5 ve daha fazla oranda artması",
            "Ülkeden sektör kapsamında yapılan ithalatın, aynı sektörde bir önceki yıl yapılan ithalata oranla miktar bazında yüzde 14,5 ve daha fazla oranda artması",
            "Ülkeden yapılan ithalatın, GTS kapsamındaki ülkelerin tamamından herhangi bir on iki aylık dönemde yapılan ithalatın miktar bazında yüzde 13,5'ini aşması",
            "Ciddi zarar veya zarar tehdidine ilişkin incelemenin altı ay içinde tamamlanamaması",
        ],
        g="GTS Tebliğine göre sektörlerde belirtilen ürünlere sağlanan tavizler iki halde kaldırılabilir: GTS'den yararlanan bir ülkeden bir sektörde yapılan ithalatın, aynı sektörde bir önceki yıl yapılan ithalata oranla miktar bazında yüzde 13,5 ve daha fazla artması ya da sektördeki ürünlerin bir ülkeden ithalatının, GTS ülkelerinin tamamından herhangi bir on iki aylık dönemde yapılan ithalatın değer bazında yüzde 14,5'ini aşması. Birinci ölçüt miktar ve yüzde 13,5, ikinci ölçüt değer ve yüzde 14,5 üzerine kuruludur; ölçütleri birbirine karıştıran seçenekler hükmü bozar. Ciddi zarar incelemesi ise altı ay içinde tamamlanır ve gerekirse uzatılabilir; sürenin aşılması tavizlerin kaldırılma sebebi değildir. En güçlü tuzak değer bazında yüzde 13,5 artıştır: oran doğrudur, ancak bu ölçüt miktar bazındadır. Bu nedenle doğru cevap 'Ülkeden sektör kapsamında yapılan ithalatın, aynı sektörde bir önceki yıl yapılan ithalata oranla miktar bazında yüzde 13,5 ve daha fazla oranda artması' seçeneğidir. (MD GTS Tebliği md. 8, 9)",
        kanit=f"{K} | önceki yıl gerçekleştirilen ithalata oranla MİKTAR bazında % 13,5 VE DAHA FAZLA ORANDA ARTMASI veya, || {K} | yer alan ülkelerin tamamından herhangi bir on iki aylık dönem süresince gerçekleştirilen ithalatın DEĞER bazında || {K} | % 14,5'İNİ AŞMASI HALİNDE, kaldırılabilir. || {K} | İnceleme ALTI (6) AY İÇİNDE tamamlanır. Gerek görülen hallerde bu süre uzatılabilir.",
        yuva=[
            "Ölçüt karışması: miktar yerine değer",
            "Ölçüt karışması: %13,5 yerine %14,5",
            "İkinci ölçüt bozulmuş: değer ve %14,5 yerine miktar ve %13,5",
            "GTS Tebliği: incelemenin altı ay içinde tamamlanması",
        ],
        yakinlik="BİREBİR",
        tuzak=["YAKIN-SAYI", "UNSUR"],
        duzey=["AYIRT"],
        profil=[3],
        olumsuz=False,
        eksen=1,
        ayna="miktar %13,5 ↔ değer %14,5",
    ),
    # 12 ---------------- Kullanılmış eşya Tebliği: izin belgesi uzatılamaz (olumsuz) ----------------
    s(
        kalip="YANLIŞ",
        z="O",
        madde="Kullanılmış veya Yenileştirilmiş Eşya İthalatına İlişkin Tebliğ (İthalat: 2026/9) md. 6, 9, 11",
        cek="İzin belgesi altı ay, uzatılmaz, belge sahibi ithal eder; %5'e kadar aşım engel değil; girişte yeni olan geçici ithal eşyasına ayrıca izin aranmaz.",
        kok=[
            "Kullanılmış veya Yenileştirilmiş Eşya İthalatına İlişkin Tebliğ (İthalat: 2026/9) hükümlerine göre izin belgesi ve ithalat işlemleri hakkında aşağıdakilerden hangisi yanlıştır?"
        ],
        d="İzin belgesi, belge tarihinden itibaren altı ay geçerlidir; Genel Müdürlükçe gerekli görülmesi halinde süresi bir defaya mahsus üç ay uzatılabilir.",
        c=[
            "İzin belgesi kapsamındaki ithalatın belge sahibi tarafından yapılması zorunludur.",
            "Beyanname tescilinde tespit edilen kıymet veya miktarın, başvuruda kayıtlı kıymet veya miktarı toplam yüzde 5'ten (yüzde 5 dâhil) daha az bir oranda aşması ithalatın yapılmasını engellemez.",
            "Geçici olarak yurda girdiği tarihte yeni ve kullanılmamış olup kesin ithali talep edildiğinde kullanılmış durumda olan eşyanın kesin ithali için ayrıca izin belgesi aranmaz.",
            "Başvuruda birim kıymetlere ilişkin yapılan beyanlar, Gümrük Kanunu çerçevesinde yapılan birim kıymet denetim ve kontrollerinin yerine geçmez.",
        ],
        g="Kullanılmış veya Yenileştirilmiş Eşya İthalatına İlişkin Tebliğe göre kullanılmış veya yenileştirilmiş eşyanın serbest dolaşıma girişi izne tabidir. İzin belgesi belge tarihinden itibaren altı ay geçerlidir ve süre uzatımı yapılmaz; belge kapsamındaki ithalatın belge sahibi tarafından yapılması zorunludur. Beyanname tescilinde tespit edilen kıymet veya miktarın başvurudakini toplam yüzde 5'ten (yüzde 5 dâhil) daha az aşması ithalatı engellemez. Teminatla geçici olarak yurda giren eşya, girdiği tarihte yeni ve kullanılmamışsa, kesin ithal talebinde kullanılmış olsa bile ayrıca izin belgesi aranmadan kesin ithal edilebilir. Başvurudaki birim kıymet beyanları Gümrük Kanunu çerçevesindeki kıymet denetimlerinin yerine geçmez ve Tebliğdeki kıymetler gümrük kıymetine esas teşkil etmez. Üç aylık uzatma imkânı ise Tebliğde yoktur. En güçlü tuzak geçici ithalattan kesin ithalata ilişkin ifadedir: eşya kesin ithalde kullanılmış olduğundan izin gerektiği sanılır, oysa belirleyici an yurda giriş tarihidir. Bu nedenle doğru cevap 'İzin belgesi, belge tarihinden itibaren altı ay geçerlidir; Genel Müdürlükçe gerekli görülmesi halinde süresi bir defaya mahsus üç ay uzatılabilir.' seçeneğidir. (MD Kullanılmış Eşya Tebliği md. 6, 9, 11)",
        kanit=f"{K} | İzin Belgesi belge tarihinden itibaren ALTI (6) AY GEÇERLİDİR. || {K} | SÜRE UZATIMI YAPILMAZ. || {K} | İzin Belgesi kapsamındaki İTHALATIN, BELGE SAHİBİ TARAFINDAN YAPILMASI ZORUNLUDUR. || {K} | TOPLAM % 5'TEN (% 5 DÂHİL) DAHA AZ BİR ORANDA AŞMASI İTHALATIN YAPILMASINI || {K} | TARİHTE YENİ VE KULLANILMAMIŞ İSE, kesin ithaline izin verilmiştir. Bu eşyalar için AYRICA İZİN BELGESİ || {K} | KIYMETLERE İLİŞKİN DENETİM VE KONTROLLERİN YERİNE GEÇMEZ.",
        yuva=[
            "Kullanılmış Eşya Tebliği: ithalatın belge sahibince yapılması (doğru)",
            "Kullanılmış Eşya Tebliği: %5 tolerans (doğru)",
            "Kullanılmış Eşya Tebliği: geçici ithalattan kesin ithalata dönüş (doğru)",
            "Kullanılmış Eşya Tebliği: birim kıymet beyanı kıymet denetiminin yerine geçmez (doğru)",
        ],
        yakinlik="BİREBİR",
        tuzak=["SAYI", "BAŞLANGIÇ"],
        duzey=["AYIRT"],
        profil=[3],
        olumsuz=True,
        cikmis="2022/21",
    ),
    # 13 ---------------- Çift kullanımlı malzeme Tebliği: belgeler izin belgesi yerine geçmez ----------------
    s(
        kalip="YANLIŞ",
        z="Z",
        madde="Çift Kullanımlı Malzeme ve Teknolojilere Dair Belgelerin Onaylanmasına İlişkin Tebliğ (İthalat: 2026/12) md. 4, 7, 10",
        cek="İthal Şehadetnamesi altı ay, uzatılamaz; ithalat aynı gümrük idaresinden; kontrol gümrüğün sorumluluğunda değil; belgeler izin belgesi yerine geçmez.",
        kok=[
            "Çift Kullanımlı Malzeme ve Teknolojilere Dair Belgelerin Onaylanmasına İlişkin Tebliğ'e (İthalat: 2026/12) göre İthal Şehadetnamesi ve Nihai Kullanım Sertifikası hakkında aşağıdakilerden hangisi yanlıştır?"
        ],
        d="İthal Şehadetnamesi ve Nihai Kullanım Sertifikası ithalatta izin belgesi yerine geçer ve gümrük işlemlerinin tekemmül ettirilmesine mesnet teşkil eder.",
        c=[
            "İthal Şehadetnamesinin geçerlilik süresi onay tarihinden itibaren altı aydır ve süre uzatılamaz.",
            "İthal Şehadetnamesi kapsamı ithalat aynı gümrük idaresinden yapılır.",
            "Belgeler ithalatçı talebine istinaden ihraç izni alınmasına mesnet olduğundan, belgelerin kontrolü gümrük idaresinin sorumluluğunda değildir.",
            "Tesellüm Teyidi Vesikasının alınmasında İthal Şehadetnamesinin geçerlilik süresi dikkate alınmaz.",
        ],
        g="Çift kullanımlı malzeme ve teknolojilerin ihracatçı ülkelerdeki ihracat kontrolleri nedeniyle Türkiye'deki ithalatçıdan istenen İthal Şehadetnamesi ve Nihai Kullanım Sertifikası Genel Müdürlük onayına tabidir. İthal Şehadetnamesinin geçerlilik süresi onay tarihinden itibaren altı aydır ve uzatılamaz; Tesellüm Teyidi Vesikası alınırken bu süre dikkate alınmaz. İthal Şehadetnamesi kapsamı ithalat aynı gümrük idaresinden yapılır ve belgelerin kontrolü gümrük idaresinin sorumluluğunda değildir. Bu belgeler ihracatçı ülke makamlarının ihraç izni vermesine mesnet teşkil eden belgeler olduğundan ithalatta izin belgesi yerine geçmez ve gümrük işlemlerinin tekemmül ettirilmesine mesnet teşkil etmez; dış ticaret mevzuatı gereği alınması gereken belge ve izinler ayrıca ibraz edilir. En güçlü tuzak gümrük idaresinin kontrol sorumluluğu ifadesidir: ithalat gümrükte yapıldığı için belgelerin kontrolünün de gümrüğe ait olduğu sanılır. Bu nedenle doğru cevap 'İthal Şehadetnamesi ve Nihai Kullanım Sertifikası ithalatta izin belgesi yerine geçer ve gümrük işlemlerinin tekemmül ettirilmesine mesnet teşkil eder.' seçeneğidir. (MD Çift Kullanımlı Malzeme Tebliği md. 4, 7, 10)",
        kanit=f"{K} | İthal Şehadetnamesinin GEÇERLİLİK SÜRESİ onay tarihinden itibaren ALTI (6) AYDIR. Belgelerin SÜRESİ UZATILAMAZ. || {K} | İthal şehadetnamesi kapsamı İTHALAT AYNI GÜMRÜK İDARESİNDEN YAPILIR. || {K} | alınmasına mesnet teşkil eden belgeler olduğu için belgelerin kontrolü gümrük idaresinin sorumluluğunda değildir. || {K} | Tesellüm Teyidi Vesikasının alınmasında İthal Şehadetnamesinin geçerlilik süresi dikkate alınmaz. || {K} | İTHALATTA İZİN BELGESİ YERİNE GEÇMEZ. Gümrük işlemlerinin tekemmül ettirilmesine MESNET TEŞKİL ETMEZ.",
        yuva=[
            "Tebliğ: altı ay, uzatılamaz (doğru)",
            "Tebliğ: aynı gümrük idaresi (doğru)",
            "Tebliğ: kontrol gümrüğün sorumluluğunda değil (doğru)",
            "Tebliğ: Tesellüm Teyidi Vesikasında süre dikkate alınmaz (doğru)",
        ],
        yakinlik="BİREBİR",
        tuzak=["TERSİNE", "MAKAM"],
        duzey=["AYIRT"],
        profil=[3],
        olumsuz=True,
    ),
    # 14 ---------------- Kamu ithalatı Tebliği: izin aranmayan eşya (olumsuz) ----------------
    s(
        kalip="KAPSAM_DIŞI",
        z="Z",
        madde="Kamu Kurum ve Kuruluşları Tarafından Yapılacak İthalatta Alınacak İzin Hakkında Tebliğ (İthalat: 2026/15) md. 5, 6, 9",
        cek="İzin aranmaz: TMO ve ESK'nın 01–24. fasıl ithalatı, MAPEG belgeli petrol eşyası, TCMB banknot kağıdı, yabancı lehine sonuçlanan ihale; yerli malı listeleri için izin düzenlenmez.",
        kok=[
            "Kamu Kurum ve Kuruluşları Tarafından Yapılacak İthalatta Alınacak İzin Hakkında Tebliğ'e (İthalat: 2026/15) göre, ithaline Bakanlıkça izin verilmiş sayılan ve gümrük idarelerince bu Tebliğ kapsamında izin belgesi aranmayan eşya arasında aşağıdakilerden hangisi yer almaz?"
        ],
        d="Kamu alımlarında yerli malı olma şartı getirilen makine ve ekipman listesi ile yapı malzemeleri listesinde belirtilen eşya",
        c=[
            "Toprak Mahsulleri Ofisi Genel Müdürlüğü ile Et ve Süt Kurumu Genel Müdürlüğü tarafından 01–24 arası fasıllar altında ithal edilen eşya",
            "Petrol arama ve üretim faaliyetlerinde kullanılmak üzere Maden ve Petrol İşleri Genel Müdürlüğünün İthal İzin Belgesini haiz eşya",
            "Türkiye Cumhuriyet Merkez Bankası tarafından ithal edilecek banknot vb. kıymetli evraka mahsus kâğıtlar ve banknot mürekkebi",
            "Yerli malı lehine uygulanan en yüksek orandan daha avantajlı teklife sahip yabancı menşeli malların lehine sonuçlanan ihale kapsamı eşya",
        ],
        g="Kamu ithalatı Tebliğine göre kamu kurum ve kuruluşlarının serbest dolaşıma giriş rejimi kapsamındaki ithalatı izne tabidir ve izin belgesi beyannamenin tescilinde aranır; Gümrük Kanunundaki muafiyet halleri kapsamındaki ithalatta Tebliğ uygulanmaz. Tebliğ bazı eşyanın ithaline Bakanlıkça izin verilmiş sayar ve bunlar için izin belgesi aranmaz: Genel Müdürlükçe lisans/izin/uygunluk yazısı düzenlenen eşya, Maden ve Petrol İşleri Genel Müdürlüğü belgeli petrol arama eşyası, TMO ve Et ve Süt Kurumunun 01–24. fasıllardaki ithalatı, yerli malı lehine en yüksek orandan daha avantajlı yabancı teklif lehine sonuçlanan ihale eşyası, belirli enerji ve ilaç pozisyonları ile TCMB'nin banknot kâğıdı ve mürekkebi. Buna karşılık kamu alımlarında yerli malı şartı getirilen makine-ekipman ve yapı malzemeleri listelerindeki eşya ile Negatif Liste kapsamındaki eşya için izin belgesi düzenlenmez; özel ve istisnai durumlarda Genel Müdürlükçe izin verilebilir. İzin belgesi bir yıl geçerlidir ve tekerrüren altı ay uzatılabilir. En güçlü tuzak yabancı lehine sonuçlanan ihale eşyasıdır: yerli malı tercihine aykırı göründüğü için izin gerektirdiği sanılır, oysa Tebliğ bu eşyayı izin verilmiş sayar. Bu nedenle doğru cevap 'Kamu alımlarında yerli malı olma şartı getirilen makine ve ekipman listesi ile yapı malzemeleri listesinde belirtilen eşya' seçeneğidir. (MD Kamu İthalatı Tebliği md. 5, 6, 9)",
        kanit=f"{K} | Aşağıda yer alan eşyanın ithaline BAKANLIKÇA İZİN VERİLMİŞ OLUP, gümrük idarelerince bu Tebliğ kapsamında İZİN BELGESİ ARANMAZ: || {K} | Toprak Mahsulleri Ofisi Genel Müdürlüğü ile Et ve Süt Kurumu Genel Müdürlüğü tarafından 01-24 arası fasıllar || {K} | Petrol arama ve üretim faaliyetlerinde kullanılmak üzere, ithalatta alınan vergi, resim ve harçlardan istisna || {K} | T.C.M.B tarafından ithal edilecek banknot vb. kıymetli evraka mahsus kağıtlar ve banknot mürekkebi. || {K} | yerli malı lehine uygulanan en yüksek orandan daha avantajlı teklife sahip yabancı menşeli malların lehlerine sonuçlanan ihale kapsamı eşya. || {K} | Aşağıda yer alan eşyanın ithalatında bu Tebliğ kapsamında İZİN BELGESİ DÜZENLENMEZ: || {K} | kamu alımlarında yerli malı olma şartı getirilen makine ve ekipman listesi ile yapı malzemeleri listesinde belirtilen eşya. || {K} | İZİN BELGELERİNİN GEÇERLİLİK SÜRESİ BİR (1) YILDIR.",
        yuva=[
            "Tebliğ izin verilmiş sayılan eşya: TMO ve ESK (listede)",
            "Aynı liste: MAPEG belgeli petrol eşyası (listede)",
            "Aynı liste: TCMB banknot kâğıdı (listede)",
            "Aynı liste: yabancı lehine sonuçlanan ihale (listede; ters sanılır)",
        ],
        yakinlik="BİREBİR",
        tuzak=["LİSTE-DIŞI", "TERSİNE"],
        duzey=["AYIRT"],
        profil=[3],
        olumsuz=True,
    ),
    # 15 ---------------- İthalat tebliğleri: belge – kurum eşleştirmesi (doğru yönlü) ----------------
    s(
        kalip="EŞLEŞTİRME",
        z="Z",
        madde="Radyoaktif Maddeler (İthalat: 2026/3), Yüksek Yoğunluklu Tatlandırıcılar (2026/4), Sivil Hava Taşıtları (2026/8), Patlayıcı Maddeler ve Ateşli Silahlar (2026/11), Mushaflar (2026/14) Tebliğleri",
        cek="Radyoaktif: Nükleer Düzenleme Kurumu; tatlandırıcı: Tarım ve Orman; sivil hava taşıtı: UAB SHGM; patlayıcı/ateşli silah: EGM; mushaf: Diyanet.",
        kok=[
            "İthalat Tebliğlerine göre, beyanname tescilinde aranan belge ile bu belgeyi düzenleyen kurum eşleştirmelerinden hangisi doğrudur?"
        ],
        d="Radyoaktif maddeler ile bunların kullanıldığı cihazlar – Nükleer Düzenleme Kurumunun izin veya uygunluk yazısı",
        c=[
            "Yüksek yoğunluklu tatlandırıcılar – Çalışma ve Sosyal Güvenlik Bakanlığının kontrol belgesi",
            "Mushaflar – Kültür ve Turizm Bakanlığının izin belgesi",
            "Sivil hava taşıtları – Milli Savunma Bakanlığının uygunluk belgesi",
            "Bazı patlayıcı maddeler, ateşli silahlar, bıçaklar ve benzeri aletler – Jandarma Genel Komutanlığının uygunluk yazısı",
        ],
        g="İthalat tebliğlerinde beyanname tescilinde aranan belgeler ve düzenleyen kurumlar şöyledir: radyoaktif maddeler ve bunların kullanıldığı cihazlarda Nükleer Düzenleme Kurumunun izin veya uygunluk yazısı; yüksek yoğunluklu tatlandırıcılarda Tarım ve Orman Bakanlığının uygunluk yazısı; mushaflarda Diyanet İşleri Başkanlığının izin belgesi; sivil hava taşıtlarında Ulaştırma ve Altyapı Bakanlığı Sivil Havacılık Genel Müdürlüğünün uygunluk yazısı; bazı patlayıcı maddeler, ateşli silahlar ve bıçaklarda genel güvenlik ve asayiş yönünden İçişleri Bakanlığı Emniyet Genel Müdürlüğünün uygunluk yazısı. Çalışma ve Sosyal Güvenlik Bakanlığının kontrol belgesi iş sağlığı ve güvenliğini etkileyen maddelerde, Milli Savunma Bakanlığının uygunluk belgesi harita içeren eşyada aranır; Kültür ve Turizm Bakanlığı müzelerde sergilenecek eşyanın muafiyetinde, Jandarma Genel Komutanlığı ise harp silahlarını ithal edebilecek kurumlar arasında geçer. En güçlü tuzak patlayıcı ve ateşli silahlar eşleştirmesidir: Jandarma güvenlik birimi olduğu için yetkili sanılır, oysa uygunluk yazısını Emniyet Genel Müdürlüğü düzenler. Bu nedenle doğru cevap 'Radyoaktif maddeler ile bunların kullanıldığı cihazlar – Nükleer Düzenleme Kurumunun izin veya uygunluk yazısı' seçeneğidir. (MD İthalat Tebliğleri 2026/3, 2026/4, 2026/8, 2026/11, 2026/14)",
        kanit=f"{K} | NÜKLEER DÜZENLEME KURUMUNUN düzenleyeceği İZİN veya UYGUNLUK YAZISI ARANIR. || {K} | beyanname tescilinde gümrükçe TARIM VE ORMAN BAKANLIĞININ UYGUNLUK YAZISI aranır. || {K} | DİYANET İŞLERİ BAŞKANLIĞININ İZİN BELGESİNE TABİ EŞYA || {K} | ULAŞTIRMA VE ALTYAPI BAKANLIĞI SİVİL HAVACILIK GENEL MÜDÜRLÜĞÜNÜN fiziksel ya da elektronik || {K} | EMNİYET GENEL MÜDÜRLÜĞÜNÜN UYGUNLUK YAZISINA TABİ EŞYA || {K} | ÇALIŞMA VE SOSYAL GÜVENLİK BAKANLIĞININ KONTROL BELGESİNE TABİ EŞYA || {K} | MİLLİ SAVUNMA BAKANLIĞININ UYGUNLUK BELGESİNE TABİ EŞYA || {K} | Kültür ve Turizm Bakanlığınca belirlenen usul ve esaslar dâhilinde özel veya kamuya ait müzelerde sergilenmek üzere",
        yuva=[
            "İş sağlığı ve güvenliği tebliği: ÇSGB kontrol belgesi",
            "İRK muafiyet: Kültür ve Turizm Bakanlığı (müzeler)",
            "Haritalar tebliği: MSB uygunluk belgesi",
            "Harp silahları tebliği: Jandarma ithal edebilen kurum",
        ],
        yakinlik="BİREBİR",
        tuzak=["MAKAM", "KOMŞU"],
        duzey=["AYIRT"],
        profil=[3],
        olumsuz=False,
        cikmis="2025/30",
    ),
    # 16 ---------------- Askıya Alma Tebliği: uygulanmayacak durumlar (olumsuz) ----------------
    s(
        kalip="KAPSAM_DIŞI",
        z="O",
        madde="Askıya Alma Sistemine İlişkin Tebliğ (İthalat: 2026/18) md. 4, 5, 7",
        cek="Askıya alma uygulanmaz: AB/Türkiye'de üretim, nihai ürün, ayrıcalıklı anlaşma, fikri mülkiyet, yalnız ticari amaçlı ithal, bozucu etki; ürün hammadde, yarı mamul, bileşen olmalı.",
        kok=[
            "Askıya Alma Sistemine İlişkin Tebliğ'e (İthalat: 2026/18) göre, Askıya Alma Sisteminin uygulanmayacağı durumlar arasında aşağıdakilerden hangisi yer almaz?"
        ],
        d="Başvuru konusu ürünün, AB veya Türkiye'deki üreticilerin üretimlerinde kullanacakları hammadde veya yarı mamul olması",
        c=[
            "Başvuru konusu ürünün aynısının, eşdeğerinin veya ikamesinin AB veya Türkiye'de üretiminin olması",
            "Başvuru konusu ürünün nihai ürün olması",
            "Ürünün fikri mülkiyet hakları kapsamında korunuyor olması",
            "Başvuru sahibinin ilgili ürünü sadece ticari amaçla ithal etmesi",
        ],
        g="Askıya Alma Sistemi, Türkiye ve AB'nin ortaklaşa uyguladığı ve sanayicilerin üretimde ihtiyaç duyduğu ürünlere geçici dönem için gümrük vergisi muafiyeti ya da indirimi tanıyan düzenlemedir. Tebliğe göre sistem; ürünün aynısının, eşdeğerinin veya ikamesinin AB veya Türkiye'de üretilmesi, ürünün nihai ürün olması, ayrıcalıklı bir ticari anlaşma kapsamına girmesi, fikri mülkiyet haklarıyla korunması, başvuru sahibinin ürünü sadece ticari amaçla ithal etmesi ve başvurunun dış ticaret politikasını bozucu etkiye sahip olması hallerinin herhangi birinde uygulanmaz. Askıya almaya konu ürünlerin AB veya Türkiye'deki üreticilerin üretimlerinde kullanacakları hammadde, yarı mamul ya da imalat bileşenleri olması ise sistemin aranan şartıdır; ayrıca tahsil edilmeyecek vergi tutarı yıllık 15.000 Avro karşılığı Türk lirasından az olmamalıdır. Askıya alınan ürünler her yıl 1 Ocak ve 1 Temmuz itibarıyla İthalat Rejimi Kararı eki V sayılı listede güncellenir. En güçlü tuzak AB veya Türkiye'de üretim bulunmasıdır: üretim yetersizse talep tarife kontenjanına çevrilebildiği için engel olmadığı sanılır, oysa üretimin varlığı uygulanmama sebebidir. Bu nedenle doğru cevap 'Başvuru konusu ürünün, AB veya Türkiye'deki üreticilerin üretimlerinde kullanacakları hammadde veya yarı mamul olması' seçeneğidir. (MD Askıya Alma Tebliği md. 4, 5, 7)",
        kanit=f"{K} | Başvuru konusu ürünün aynısının, eşdeğerinin veya ikamesinin AB veya TÜRKİYE'DE ÜRETİMİNİN OLMASI, || {K} | b) Başvuru konusu ürünün nihai ürün olması, || {K} | ç) Ürünün fikri mülkiyet hakları kapsamında korunuyor olması, || {K} | d) Başvuru sahibinin ilgili ürünü sadece ticari amaçla ithal etmesi, || {K} | HAMMADDE, YARI MAMUL ya da İMALAT BİLEŞENLERİ olmalıdır. || {K} | YILLIK 15.000 AVRO KARŞILIĞI TÜRK || {K} | AB ile eşzamanlı olarak HER YIL 1 OCAK VE 1 TEMMUZ tarihleri itibarıyla yürürlüğe giren düzenlemeyle || {K} | Askıya alma TALEBİ TARİFE KONTENJANINA ÇEVRİLEBİLİR veya KISMİ ASKIYA ALMA UYGULANABİLİR.",
        yuva=[
            "Askıya Alma Tebliği uygulanmama halleri: AB/Türkiye'de üretim (listede)",
            "Aynı liste: nihai ürün (listede)",
            "Aynı liste: fikri mülkiyet (listede)",
            "Aynı liste: sadece ticari amaçlı ithalat (listede)",
        ],
        yakinlik="BİREBİR",
        tuzak=["LİSTE-DIŞI", "TERSİNE"],
        duzey=["AYIRT"],
        profil=[3],
        olumsuz=True,
    ),
]
