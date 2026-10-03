# Üretim Hafızası

Prompt 1 (Akıllı Test Soru Motoru) ile üretilen her soru buraya tek satır olarak eklenir.
Yeni set üretilmeden önce bu dosya okunur; aynı çekirdek tekrar üretilmez.

```
ID | KONU | MADDE | ÇEKİRDEK | TİP | ZORLUK | CEVAP | SET
KAR-001 | Karar | GK m.6/2 | Karar talebi: idare, başvurunun kendisine ulaştığı tarihten itibaren otuz gün içinde karar alır | SÜ | K | C | S1
KAR-002 | Karar | GK m.6/1, 6/2, 6/4; GY m.27/1 | Karar alınması talebinin yazılı olarak yapılması zorunludur | DĞ | O | A | S1
KAR-003 | Karar | GK m.6/2 (ikinci paragraf) | Süre aşımı: süre aşılabilir; süre dolmadan gerekçe ve gerekli ek süre başvuru sahibine bildirilir | ÇI | O | D | S1
KAR-004 | Karar | GK m.6/2, 6/3 | Ret ve aleyhe kararlar gerekçeli alınır, itiraz yolunun açık olduğu kararda belirtilir | UK | Z | D | S1
KAR-005 | Karar | GK m.7/1 | Lehe kararın zorunlu iptali: yanlış/eksik bilgi + başvuranın bilmesi/bilmesi gerekmesi + doğru bilgiyle verilememe, üçü bir arada | ÇI | Z | B | S1
KAR-006 | Karar | GK m.7/2-a | Karara esas koşulun gerçekleşmemesi/gerçekleşemez olması: lehe karar değiştirilir veya iptal edilebilir (ihtiyari) | DY | O | D | S1
KAR-007 | Karar | GK m.7/4 | Yürürlük: zorunlu iptal → iptal kararının verildiği tarih; değiştirme/iptal edilebilir hali → tebliğ tarihi | EŞ | ÇZ | C | S1
KAR-008 | Karar | GK m.7/4 (ikinci cümle) | İstisna: muhatabın yasal çıkarları gerektirirse yönetmelikle belirlenen koşullarda yürürlük tarihi ertelenebilir | DY | Z | C | S1
KAR-009 | Karar | GY m.27/3, 27/4 | Değiştirme/iptal, yürürlük tarihinde rejime tabi tutulmaya başlanmış eşyaya uygulanmaz; idare belirli dönemde GOİK isteyebilir | UK | Z | E | S1
KAR-010 | Karar | GY m.586/1 | İtirazlar otuz gün içinde karara bağlanıp tebliğ edilir; bu sürede karar alınamazsa GK m.6/2 (süre aşımı) uygulanır | SÜ | O | A | S1
KAR-011 | Karar | GY m.586/1 | İtiraz incelemesi: örnek alınamazsa eşyanın kendisi veya fotoğraf, katalog, prospektüs gibi fikir verecek belgeler incelenir | BD | Z | B | S1
KAR-012 | Karar | GY m.586/1 | İtiraz incelemesinde gerek duyulursa ilgili gümrük idaresinin mütalaası alınır | MK | O | E | S1
KAR-013 | Karar | GK m.6/3, 6/4, 7/3, 7/4; GY m.27/3 | Kararın iptali muhatabına tebliğ edilir (diğer kurallarla birlikte değerlendirme) | ÇI | ÇZ | B | S1
KAR-014 | Karar | GK m.6/1 | Karar talep eden kişi kararın verilebilmesi için gerekli bütün bilgi ve belgeleri ibraz etmek zorundadır | UK | Z | E | S1
KAR-015 | Karar | GK m.6/2, 6/4 | Karar başvuru sahibine yazılı tebliğ edilir ve gümrük idarelerince derhal uygulanır; ayrı bir onay ya da bekleme süresi yoktur | UU | ÇZ | A | S1
GMY-001 | Türkçe | Genel kültür – Türkçe | Bağlaç olan de/da ayrı yazılır; bulunma eki olan -de/-da bitişik yazılır | DĞ | ÇK | E | GMY-S1
GMY-002 | Matematik | Genel kültür – Matematik | 4 kalem (15 TL) ve 3 defter (40 TL) toplam 180 TL; 200 TL verilince para üstü 20 TL | HESAP | ÇK | A | GMY-S1
GMY-003 | Tarih | Genel kültür – Tarih | Millî Mücadele'nin gerekçesi, amacı ve yöntemi ilk kez Amasya Genelgesi'nde belirtilmiştir | BD | K | E | GMY-S1
GMY-004 | Anayasa | Anayasa m.77 | TBMM ve Cumhurbaşkanı seçimleri beş yılda bir aynı günde yapılır | SÜ | K | E | GMY-S1
GMY-005 | Türkçe | Genel kültür – Türkçe | 'Ağır' sözcüğünün mecaz anlamı: kırıcı, incitici söz | TN | K | B | GMY-S1
GMY-006 | Matematik | Genel kültür – Matematik | Kız/erkek = 3/5, toplam 32 ise kız sayısı 32·3/8 = 12 | HESAP | K | D | GMY-S1
GMY-007 | Tarih | Genel kültür – Tarih | Sakarya Meydan Muharebesi sonrası TBMM, Mustafa Kemal Paşa'ya Gazi unvanı ve mareşal rütbesi verdi | MK | ÇK | C | GMY-S1
GMY-008 | Anayasa | Anayasa m.75 | TBMM, genel oyla seçilen altı yüz milletvekilinden oluşur | EŞ | ÇK | E | GMY-S1
GMY-009 | Türkçe | Genel kültür – Türkçe | Paragrafın ana düşüncesi: sağlıklı iletişim, karşımızdakini gerçekten dinlemeyi öğrenmekle başlar | UK | O | A | GMY-S1
GMY-010 | Matematik | Genel kültür – Matematik | 800 TL'ye %25 indirim 600 TL; ardından %10 zam 660 TL | HESAP | O | E | GMY-S1
GMY-011 | Tarih | Genel kültür – Tarih | Saltanatın kaldırılması (1922) Cumhuriyet'in ilanından (1923) önce gerçekleşmiştir | DY | O | C | GMY-S1
GMY-012 | Anayasa | Anayasa m.101 | Cumhurbaşkanı: kırk yaş, yükseköğrenim, milletvekili seçilme yeterliliği; TBMM üyeliği şart değil | ÇI | O | D | GMY-S1
GMY-013 | Türkçe | Genel kültür – Türkçe | Ünsüz yumuşaması: kitap + ı → kitabı | TN | O | A | GMY-S1
GMY-014 | Matematik | Genel kültür – Matematik | Anne = 4x; 5 yıl sonra 4x + 5 = 3(x + 5) → x = 10 | HESAP | O | A | GMY-S1
GMY-015 | Tarih | Genel kültür – Tarih | Kronoloji: II. İnönü → Kütahya-Eskişehir → Sakarya → Büyük Taarruz | SÜ | K | E | GMY-S1
GMY-016 | Anayasa | Anayasa m.9 | Yargı yetkisi Türk Milleti adına bağımsız ve tarafsız mahkemelerce kullanılır | MK | K | B | GMY-S1
GMY-017 | Türkçe | Genel kültür – Türkçe | Paragraftan ulaşılamayan yargı: çırağın kendi atölyesinde farklı bir öğretim yöntemi benimsemesi | UU | Z | B | GMY-S1
GMY-018 | Matematik | Genel kültür – Matematik | Doldurma 1/8, boşaltma 1/12; net 1/24 → 24 saat | HESAP | Z | A | GMY-S1
GMY-019 | Tarih | Genel kültür – Tarih | Lozan'da çözülemeyen Musul meselesi, Türkiye ile İngiltere arasındaki sonraki görüşmelere bırakılmıştır | DĞ | Z | C | GMY-S1
GMY-020 | Anayasa | Anayasa m.175 | Beşte üç (360) ile üçte iki (400) arası oyla kabul: Cumhurbaşkanı geri göndermezse halkoyuna sunulur | UK | ÇZ | C | GMY-S1
GMY-021 | Temsil | GK m.226/4 | GMY ve stajyerlerin fiil ve hareketlerinden doğan mali sorumluluk yanında çalıştıkları gümrük müşavirine aittir | MK | ÇK | E | GMY-S1
GMY-022 | Temsil | GK m.225/1 | Gerçek kişinin doğrudan temsille iş takibi: geçerli vekaletname + ticari miktar/mahiyet arz etmeyen eşya ve özel kullanıma mahsus taşıtlar | DY | O | C | GMY-S1
GMY-023 | Gümrük Müşaviri | GK m.230 | Gümrük müşavirleri defter, vekaletname, yazışma, fatura ve makbuzların asıl ve örneklerini beş yıl muhafaza eder ve ibraz eder | SÜ | K | A | GMY-S1
GMY-024 | Temsil | GK m.5, 181/2, 241/4-a | Temsil: yerleşiklik istisnası, yetkisiz temsilde kendi adına-hesabına sayılma, dolaylı temsilcinin sınırlı yükümlülüğü; yetkisiz iş takibi dört kat ceza | ÇI | ÇZ | B | GMY-S1
GMY-025 | YGM | GY m.578/1-b, d, e | YGM yetki belgesi geri alma: asgari ücret altı hizmet 1 yıl; bizzat işi başkasına yaptırma 2 yıl; bilgi-belgeyi amaç dışı kullanma 5 yıl | EŞ | Z | E | GMY-S1
GMY-026 | Yükümlülük | GK m.181/2 | İthalatta yükümlü beyan sahibidir; dolaylı temsilde hesabına beyanda bulunulan da yükümlü, temsilcinin yükümlülüğü bilme/bilmesi gerekme ile sınırlı | TN | O | D | GMY-S1
GMY-027 | Yükümlülük | GK m.191 | Yasak/kısıtlamalı eşyada da yükümlülük doğar; sahte para ve denetlenen ekonomik dolaşıma girmeyen narkotikte kaçak girişte yükümlülük doğmaz | UU | O | D | GMY-S1
GMY-028 | Ödeme | GK m.198/1, 198/2, 198/3 | Ödeme süresi: süre bitmeden yazılı istem + teminatla otuz gün uzatılabilir, kalem bazında da olur, tecil faizi alınır; itiraz süreyi keser | ÇI | Z | B | GMY-S1
GMY-029 | Teminat | GY m.494/1 | Götürü teminat: önceki yıl teminat konusu değerin %10'u; DİR dahilse en az 250.000, değilse 75.000 Avro; üst sınır 2.000.000 Avro | HESAP | O | A | GMY-S1
GMY-030 | Yükümlülük | GK m.208 | Yükümlülüğün sona ermesi: zapt ve müsadere, eşyanın bir gümrük rejimi kapsamında tesliminden ÖNCE olmalıdır | DĞ | O | E | GMY-S1
GMY-031 | Geri Verme | GK m.216/2 | Geri verme kararı tebliğden itibaren dört ay içinde uygulanmazsa talep üzerine kanuni faiz oranında faiz ödenir | SÜ | K | C | GMY-S1
GMY-032 | Geri Verme | GY m.500/1 | Geri verme/kaldırma yetkisi: 4.730.000 TL'ye kadar gümrük müdürlüğü; 47.397.000 TL'ye kadar bölge müdürlüğü; üstü Bakanlık | MK | O | A | GMY-S1
GMY-033 | Cezalar | GK m.234/1-c | Satış birimine göre %5'i geçmeyen miktar farkı ve maddi hesap hatasından doğan noksan kıymet beyanında vergi farkının yarısı ceza | DY | O | B | GMY-S1
GMY-034 | Kıymet | GK m.27/4, 28/e | Satın alma komisyonu: ithalatçının temsilcisine yurtdışında satın almadaki temsil hizmeti için ödediği ücret; kıymete dahil edilmez | TN | ÇK | C | GMY-S1
GMY-035 | Kıymet | GK m.27/1-a-i, 27/1-c, 28/a, 28/b, 28/e | Kıymet hesabı: satış komisyonu ve satış koşulu royalti eklenir; satın alma komisyonu, ithal sonrası montaj ve giriş yeri sonrası nakliye eklenmez | HESAP | Z | C | GMY-S1
GMY-036 | Kıymet | GK m.26/2 | Son yöntemde esas alınamayacaklar: yurtiçi satış fiyatı, iki alternatiften yükseği, ihraç ülkesi iç piyasa fiyatı, üçüncü ülke ihraç fiyatı, asgari/keyfi kıymet | DĞ | O | A | GMY-S1
GMY-037 | Kıymet | GY m.44/1; GK m.25/1 | İndirgeme ve hesaplanmış kıymet yönteminin sırası, beyan sahibinin yazılı talebinin gümrük idaresince uygun bulunmasıyla değiştirilebilir | DY | K | E | GMY-S1
GMY-038 | Kıymet | GY m.43/3, 43/4, 46/4, 48/3 | Aynı/benzer eşya yalnız aynı ülkede üretilmiş olur; indirgemede yakın tarih satış yoksa doksan gün içindeki ilk satış birim fiyatı esas | ÇI | Z | C | GMY-S1
GMY-039 | Gümrüklenmiş Değer | GK m.3/26, 235/1-c, 235/6 | İthalatta belgeye bağlı eşyada belge alınmış gibi beyan: gümrüklenmiş değerin (CIF+gümrük vergileri) iki katı; idareden önce bildirimde yüzde on | HESAP | ÇZ | E | GMY-S1
GMY-040 | Kıymet | GK m.30 | Kıymet TL beyan edilir; yabancı para, yükümlülüğün başladığı tarihte yürürlükteki TCMB döviz satış kuru ile çevrilir | UK | K | B | GMY-S1
GMY-041 | Menşe | GY m.39/1 | Ticari mahiyette olmayan ve CIF kıymeti 430 Avro'yu geçmeyen eşya için menşe şahadetnamesi aranmaz | BD | ÇK | E | GMY-S1
GMY-042 | Tarife | GGT (Tarife) Seri 14 m.13/1 | BTB heyeti: bölge müdür yardımcısı başkanlığında bir gümrük müdürü veya şube müdürü ve üç muayene memuru | MK | K | A | GMY-S1
GMY-043 | Menşe | GY m.38/2 | Menşe şahadetnamesi sonradan ibraz süresi: mücbir sebep saklı, bitiminden önce başvuru kaydıyla idare amirince en fazla otuz gün uzatılır | SÜ | K | C | GMY-S1
GMY-044 | Serbest Dolaşım | GK m.76 | Farklı tarife pozisyonlu taşıma belgesi içeriği: beyan sahibinin talebiyle tamamına en yüksek vergi oranlı eşyanın pozisyonu uygulanabilir | DY | K | A | GMY-S1
GMY-045 | Menşe | GY m.40/1-2 | Menşe şahadetnamesinde gönderen, alıcı, eşyanın cinsi/ağırlığı ve işlem açıklamasındaki noksanlık idare amiri onayıyla işleme konulur | ÇI | Z | D | GMY-S1
GMY-046 | Tarife | GY m.32/1 | Tarife pozisyonu dört rakamlı gruptur; altı rakamlı grup tarife alt pozisyonudur; GTİP on iki rakamdır | EŞ | O | A | GMY-S1
GMY-047 | Menşe | GY m.34/1 | Tekstilde (XI. bölüm) kural pozisyon değişikliği; ek listedeki ürünlerde listedeki işlem gerçekleşmedikçe pozisyon değişse de menşe kazanılmaz | DY | O | D | GMY-S1
GMY-048 | Tarife | GY m.29/6 | Bağlayıcı Menşe Bilgisi, karar için gereken tüm belgelerin temin edildiği tarihten itibaren beş ay içinde bildirilir | SÜ | O | B | GMY-S1
GMY-049 | Serbest Dolaşım | GY m.207/4 | Nihai kullanımda izin süresi sonu müracaatında uygunluk tespiti ve teminat iadesi yetkilendirilmiş gümrük müşaviri raporuna istinaden yapılır | UK | O | D | GMY-S1
GMY-050 | Serbest Dolaşım | GGT (Nihai Kullanım) Seri 1 m.5/1, m.8/1 | Nihai kullanım talebi tescilden önce yazılı; GDY/antrepodaki eşyaya beyanname kapatılmamışsa sonradan izin, TBYBU eşya ve sivil hava taşıtları hariç | ÇI | Z | D | GMY-S1
GMY-051 | Menşe | GY m.36/2 | Fabrika çıkış fiyatı: ürünün fabrika çıkış fiyatından ihracatta geri ödenen/ödenecek yurt içi vergiler tenzil edilerek bulunan fiyat | TN | O | B | GMY-S1
GMY-052 | Serbest Dolaşım | GY m.209/4-b | Mükerrer kullanılabilir nihai kullanım eşyası, ilk tahsis tarihinden itibaren iki yıl geçince nihai kullanıma tahsis edilmiş sayılır | SÜ | O | C | GMY-S1
GMY-053 | Menşe | GY m.41/2-3 | Menşe şahadetnamesinde tereddüt sürerse sonradan kontrol için Müsteşarlığa gönderilir; TPÖ'lü eşya yazılı talep ve teminatla teslim edilebilir | UK | O | C | GMY-S1
GMY-054 | Tarife | GK m.9/7 | Geçerliliğini kaybeden BTB, bağlayıcı sözleşme yapılmışsa yayım/tebligattan itibaren altı ay kullanılabilir; ithalat/ihracat/ön izin belgesi varsa onun süresi esas | DY | Z | E | GMY-S1
GMY-055 | Fikri Haklar | GY m.109, m.110 | FSMH ihlali şüphesiyle durdurulan eşyanın serbest dolaşıma girişine, serbest bölgeye konulmasına, yeniden ihracına izin verilmez; gözetimde depolanır | ÇI | Z | D | GMY-S1
GMY-056 | Fikri Haklar | GY m.107/1-2 | Durdurma sonrası dava ve ihtiyati tedbir için on iş günü; haklı mazerette en fazla on iş günü uzatma; bozulabilirde üç iş günü, uzatılamaz | SÜ | O | B | GMY-S1
GMY-057 | Menşe | GY m.36/3 | Üçüncü ülkede antrepoya konulsa da menşe değişmez; geldiği ülke en son gönderildiği ülke; antrepoya konmadan araç değişimi geldiği ülkeyi değiştirmez | UU | ÇZ | C | GMY-S1
GMY-058 | Serbest Dolaşım | 4458 s.K. Bazı Maddelerinin Uygulanması Hk. Karar m.13, m.14, m.15 | Hava taşıtı TGB'ye getirilmeden serbest dolaşımda işlemler Teknik Uygunluk Belgesi tarihinden itibaren otuz gün içinde sonuçlandırılır | DĞ | Z | E | GMY-S1
GMY-059 | İlave Gümrük Vergisi | İGV Kararı m.2/2, m.4/3-6 | A.TR eşliğinde ithal edilen AB ve Türk menşeli olmayan eşyadan Diğer Ülkeler sütunundaki oranla ilave gümrük vergisi alınır | DY | O | B | GMY-S1
GMY-060 | Menşe | GY m.205/4, 205/7 | Önlem uygulanan ülke menşeli beyan edilen eşyada MŞ aranmaz; birden fazla önlem veya ülkeye göre farklı oran varsa aranır, ibraz edilmezse en yüksek tutar | UU | ÇZ | B | GMY-S1
GMY-061 | Dahilde İşleme | DİR Tebliği (İhracat 2006/12) m.20/1, 20/3 | Belge süresi sektörüne göre azami 12 ay; başlangıç belge tarihi, süre sonu bitimin rastladığı ayın son günü | SÜ | K | A | GMY-S1
GMY-062 | Dahilde İşleme | DİR Tebliği (İhracat 2006/12) m.22/1, 22/2 | Performansa dayalı ek süre: ihracat/taahhüt oranı en az %25 ise belge orijinal süresinin yarısı kadar | HESAP | Z | B | GMY-S1
GMY-063 | Dahilde İşleme | DİR Tebliği (İhracat 2006/12) m.23/1-a, 23/1-b, 23/2 | Haklı sebep müracaatı: belge → 3 ay içinde elektronik ortamda Bakanlığa; izin → 2 ay içinde gümrük idaresine; süresinde yapılmayan değerlendirilmez | UU | ÇZ | D | GMY-S1
GMY-064 | Dahilde İşleme | DİR Tebliği (İhracat 2006/12) m.17/8, 17/9, 17/10 | Döviz kullanım oranı: azami %80, ikincil tarım ürünlerinde %100'e kadar; izinde, bedelsiz ithalatta ve yurt içi alımlarda aranmaz | ÇI | Z | E | GMY-S1
GMY-065 | Dahilde İşleme | DİR Tebliği (İhracat 2006/12) m.25/1-e | Mücbir sebep/fevkalade hal olarak grev ve lokavt: il çalışma müdürlüklerinden alınacak yazı ile tevsik | BD | O | D | GMY-S1
GMY-066 | Dahilde İşleme | DİR Tebliği (İhracat 2006/12) m.13/1 | Geri ödeme sisteminde taahhüt kapatılmasını müteakip 3 ay içinde vergi iadesi için ilgili gümrük idaresine müracaat zorunlu | MK | K | A | GMY-S1
GMY-067 | İhracat | GY m.156/1, 156/2, 156/3 | Kumanya/yağ/yakıt veren ve periyodik basılı yayın ihraç edenler: ticari/idari belge talebi YYS/OKSB koşulları aranmaksızın kabul edilir | DY | O | D | GMY-S1
GMY-068 | İhracat | GY m.416/1-a, 416/1-c | Kara/demiryolu çıkışında TGB'yi terk tarihi: kara sınırından fiilen çıkış veya serbest bölgeye fiilen giriş; taşıtlara teslimde teslim tarihi | TN | O | C | GMY-S1
GMY-069 | İhracat | GY m.417/1 | İhracat amaçlı geçici depolamada eşya bir ay kalır; beyanname tescilinden bağımsız ek süre talebinde en çok üç ay ek süre | UK | O | B | GMY-S1
GMY-070 | Geri Gelen Eşya | GY m.446/1, 446/2, 446/3-b, 446/4 | Geri gelme nedeni yurt dışındaki alıcı/kurum belgesiyle ispat; kusurluda ilk kullanım sınırı; ticari taşıt ve iş makinesine ayniyetle şartsız muafiyet | ÇI | O | A | GMY-S1
GMY-071 | Kumanya | GY m.477/2-3, 479/1, 480/1, 482/2 | Dış seferden dönüp yükünü boşaltan geminin ihraç yükü almak üzere diğer Türk limanına hareketi dış seferin devamı sayılır | DĞ | K | B | GMY-S1
GMY-072 | Transit | GY m.228/1-a, b, c | Telef/kayıp kanıtı: suçüstü hırsızlık → Cumhuriyet Savcılığı belgesi; herkesçe bilinen olay → en büyük mülki amir; trafik kazası → gümrük idare amiri kararı | EŞ | Z | D | GMY-S1
GMY-073 | Transit | GY m.239/1-a | Ulusal transitte eksiklik: uyuşmazlık bildiriminden itibaren 28 gün içinde hareket idaresine ispat; yazılı başvuruyla 28 gün daha | SÜ | O | D | GMY-S1
GMY-074 | Transit | GY m.222/1 | Transitte teminat aranmayan taşımalar: havayolu, boru hattı, denizyolu ve basitleştirilmiş usulde demiryolu | ÇI | O | C | GMY-S1
GMY-075 | Transit | GY m.227/1 | Bir Türk limanından başka bir Türk limanına transit olunacak eşyayı yalnız Türk bandıralı gemiler nakledebilir | DY | ÇK | D | GMY-S1
GMY-076 | Transit | GY m.225/1 | İthali yasaklanan eşyanın transitine izin vermeye gümrük ve ticaret bölge müdürlükleri yetkilidir | MK | K | C | GMY-S1
GMY-077 | Yolcu-Posta | 2009/15481 s. Karar m.52/1 | Çeyiz eşyası muafiyeti: eşya evlilik akdinden iki ay önce veya dört ay sonraki süreler içinde serbest dolaşıma sokulmalı | SÜ | O | A | GMY-S1
GMY-078 | Yolcu-Posta | 2009/15481 s. Karar m.61/1 | Yolcu beraberi hediyelik eşya limiti 430 Avro; 15 yaşından küçük yolcular için 150 Avro | DY | ÇK | D | GMY-S1
GMY-079 | Yolcu-Posta | 2009/15481 s. Karar m.45/1, 62/2, 62/5 | Posta ile gerçek kişiye kitap: 150 Avro'ya kadar muaf; 1500 Avro'ya kadar limiti aşan değere %0 tek ve maktu vergi; brüt 30 kg sınırı | UK | Z | B | GMY-S1
GMY-080 | Tasfiye | GK m.179/1 (üçüncü ve dördüncü cümleler) | İhale ilanından sonra, satıştan önce rejim/yeniden ihraç başvurusu: cezalar, ambarlama-elleçleme ve diğer giderler + CIF değerinin %10'u | HESAP | ÇZ | C | GMY-S1
GMY-081 | Antrepo | GY m.332/2 | Geçici depolamaya girmeden antrepoya gelen eşya: antrepo beyannamesi taşıtın gelişini takip eden iki iş günü içinde tescil; talep üzerine bir gün uzatma | SÜ | K | A | GMY-S1
GMY-082 | Antrepo | GY m.335/1, 335/3-b,c | Elleçleme izni: antrepo içinde → denetleyici gümrük müdürlüğü; antrepo dışında → gümrük müdürlüğü görüşüyle Bölge Müdürlüğü sonuçlandırır | MK | O | D | GMY-S1
GMY-083 | Antrepo | GY m.329/1-b, ç, d, e | Antrepo tipleri: B kullanıcı sorumlu/işletici kiralar; D vergilendirme unsurları rejime giriş tarihine göre; E depolama yeri antrepo addedilir; F gümrükçe işletilen | EŞ | Z | B | GMY-S1
GMY-084 | Antrepo | GY m.333/3-a,b,c; 333/4 | Antrepoda devir: devralan beş iş günü; sorumluluk devralana; beyannamesiz ikinci devir yok; özel antrepoda beş iş günü içinde çıkış, işletici ve devralana ayrı yaptırım | ÇI | Z | E | GMY-S1
GMY-085 | Antrepo | GY m.519/2-3 | Genel antrepo: gümrük müdürlüğüne en fazla 50 km; alan en az %20 kapalı, büyükşehirde 5.000 m², diğer yerlerde 3.000 m² | DY | O | E | GMY-S1
GMY-086 | GSM | GSMY m.4/2 | Hudut kapısında mağaza açma: son on iki ay veya önceki takvim yılında girişte en az 30.000, çıkışta en az 10.000 kişi | BD | O | C | GMY-S1
GMY-087 | Geçici Depolama | GK m.46/2; GY m.76/3 | Özet beyan kapsamı eşya: denizyolu 45, diğer 20 gün; uzatma gümrük müdürlüklerince, bir ayı aşan uzatma talebinde gerekçe şart | SÜ | O | A | GMY-S1
GMY-088 | Geçici Depolama | GY m.85/1 | Kaçak zannıyla el konulup iadesine karar verilen eşya: tebligattan itibaren geçici depolanan eşya; serbest dolaşımda değilse 30 gün işlem, serbest dolaşımdaysa 30 gün teslim | UK | O | D | GMY-S1
GMY-089 | Serbest Bölge | GK m.159/1 | Serbest bölgede faaliyette bulunan kişinin yerine konulan eşya kırk sekiz saat içinde envanter kayıtlarına geçirilir | SÜ | ÇK | C | GMY-S1
GMY-090 | Serbest Bölge | GK m.155/1-2 | Serbest bölgeye girişte gümrüğe sunulması şart eşya: girişle sona eren rejim eşyası (istisna saklı), geri verme/kaldırma sonrası, ihracat kaydıyla, doğrudan TGB dışından gelen | ÇI | O | B | GMY-S1
GMY-091 | Geçici İthalat | GK m.133/3-4 | Kısmi muafiyetli iki kişi arasında aynı ay içinde devir: ayın tamamı vergisini ilk hak sahibi öder; yeni hak sahibi kalan süreyi kullanır | UK | O | C | GMY-S1
GMY-092 | Geçici İthalat | GY m.382/2-3 | ATA karnesinin ibrazı rejim için izin talebi, tescili geçici ithalat rejimine giriş izni sayılır | BD | K | B | GMY-S1
GMY-093 | Geçici İthalat | 2009/15481 s. BKK m.20/1-a, c-3, ç, d | Taşıt izin süreleri: demiryolu on iki ay, kişisel hava altı ay, kişisel deniz on sekiz ay, yurt dışı emeklisi kara taşıtı iki yıl | EŞ | Z | A | GMY-S1
GMY-094 | Geçici İthalat | Kara Taşıtları GGT Seri No:1 m.6/1, 6/8, 8/4, 15/1 | Kara taşıtları tebliği süreleri: ticari 30, otobüs 90, sınır ticareti 15 gün; turistik 730 gün; trafik tescil başvurusu 30 gün; iç gümrükten sevk 7 gün | ÇI | ÇZ | E | GMY-S1
GMY-095 | Geçici İthalat | Kara Taşıtları GGT Seri No:1 m.4/1-p | Yerleşim yeri: Türkiye'ye giriş tarihinden geriye doğru 365 gün içinde en az 185 gün yaşanan yer | TN | K | A | GMY-S1
GMY-096 | Geçici İthalat | GK m.238/1-b, 238/1-d, 238/2 | Özel taşıt rejim ihlali vergilerin dörtte biri; diğer eşyada süre aşımı vergi+faiz, tebligattan altmış gün içinde işlem yoksa ayrıca vergiler tutarında ceza | UU | ÇZ | D | GMY-S1
GMY-097 | YYS-OKSB | GİKY m.4/7, 4/8, 4/9 | YYS: eksik beyan, kısmi teminat ve yeşil hat talepsiz; götürü teminat ve izinli alıcı talep ve ek koşulla | ÇI | O | E | GMY-S1
GMY-098 | YYS-OKSB | GİKY m.4/A-1 | YYS-I: imalatçı + asgari 5 milyon USD ihracat + (ortalama 50 işçi veya asgari 10 milyon USD ihracat) | DY | Z | B | GMY-S1
GMY-099 | YYS-OKSB | GY m.22/1-2, 24/1, 24/3 | OKSB: dış ticaret sermaye şirketleri ve sektörel dış ticaret şirketleri için özel koşullar aranmaz | DĞ | O | D | GMY-S1
GMY-100 | YYS-OKSB | GY m.26/1, 26/4, 26/5 | OKSB iptali: yetkiler belgenin düzenlendiği tarih itibarıyla geçersiz; iptal tarihinden itibaren iki yıl statü verilmez (askı/geri almadan farkı) | UU | ÇZ | E | GMY-S1
GMY2-001 | Türkçe | Genel Kültür Kitabı – Yazım kuralları (Kesme işaretinin sınırı) | Kurum ve kuruluşların açık adlarına gelen eklerde kesme işareti kullanılmaz; kısaltma, rakam ve kanun özel adında kullanılır. | YANLIŞ | K | A | GMY-S2
GMY2-002 | Türkçe | Genel Kültür Kitabı – Noktalama (Noktalı virgül ve iki nokta) | Kendi içinde virgül bulunan gruplar noktalı virgülle ayrılır; açıklama veya örnekten önce iki nokta konur. | BOŞLUK | ÇK | E | GMY-S2
GMY2-003 | Türkçe | Genel Kültür Kitabı – Anlam bilgisi (Neden, amaç ve koşul) | 'İçin' edatı hem neden hem amaç bildirebilir; neden-sonuç cümlesinde bir olay başka durumun gerekçesi olarak verilir. | OLAY | K | A | GMY-S2
GMY2-004 | Türkçe | Genel Kültür Kitabı – Paragraf ve anlatım (Akış ve paragrafı bölme) | Akışı bozan cümle, paragrafta sürdürülen ana düşüncenin gelişimine katkı vermeyen cümledir. | KAPSAM_DIŞI | O | B | GMY-S2
GMY2-005 | Türkçe | Genel Kültür Kitabı – Anlatım bozukluğu (Eksik ögeler ve tamlamalar) | İki yüklemin ortak kullandığı öge her ikisine aynı ekle bağlanamıyorsa nesne eksikliğinden anlatım bozukluğu doğar. | OLAY | Z | D | GMY-S2
GMY2-006 | Matematik | Genel Kültür Kitabı – Zaman ve takvim (Bitiş saati ve gece yarısı) | 22.35'te başlayan 5 saat 40 dakikalık yolculuk gece yarısını aşarak ertesi gün 04.15'te biter. | HESAP | ÇK | E | GMY-S2
GMY2-007 | Matematik | Genel Kültür Kitabı – Fonksiyon ve işlem tanımlama (Özel işlemde kuralı uygula) | Özel işlemde önce parantez içi tanıma göre açılır: a◆b = 3a − 2b + 4 için (2◆5)◆1 = 2. | HESAP | K | B | GMY-S2
GMY2-008 | Matematik | Genel Kültür Kitabı – Veri ve grafik yorumlama (Ağırlıklı ortalama) | Farklı büyüklükteki grupların ortak ortalaması, grup büyüklükleriyle ağırlıklandırılarak bulunur: (15·60 + 25·76)/40 = 70. | HESAP | O | E | GMY-S2
GMY2-009 | Matematik | Genel Kültür Kitabı – Oran ve orantı (Oran paylarıyla paylaşım) | A:B = 3:4 ve B:C = 6:7 oranları B'de eşitlenerek 9:12:14 bulunur; 210 TL paylaşımında en çok ve en az pay farkı 30'dur. | HESAP | O | B | GMY-S2
GMY2-010 | Matematik | Genel Kültür Kitabı – Geometri (Birim dönüşümü ve birleşik uygulama) | Farklı birimlerle verilen dikdörtgende birimler eşitlenir; 2,4 m × 160 cm zemin 40 cm'lik 24 kare karoyla kaplanır, çevresi 8 m'dir. | HESAP | Z | D | GMY-S2
GMY2-011 | Tarih | Genel Kültür Kitabı – Millî Mücadele'ye hazırlık (Erzurum Kongresi) | Erzurum Kongresi'nde kararları takip etmek üzere dokuz kişilik Temsil Heyeti seçildi; başkanlığına Mustafa Kemal getirildi. | DOĞRU | K | B | GMY-S2
GMY2-012 | Tarih | Genel Kültür Kitabı – Ateşkes ve barış (Mudanya) | Mudanya askerî çatışmayı kapatan ateşkestir; saltanatın kaldırılması Mudanya'nın maddesi değil, 1 Kasım 1922 tarihli Meclis kararıdır. | YANLIŞ | O | D | GMY-S2
GMY2-013 | Tarih | Genel Kültür Kitabı – Misak-ı Millî ve Meclis (Misak-ı Millî'nin çerçevesi) | Misak-ı Millî son Osmanlı Meclis-i Mebusanında kabul edildi; Kars-Ardahan-Batum ve Batı Trakya için halk oylaması öngörüldü. | ÖNERMELİ | Z | C | GMY-S2
GMY2-014 | Tarih | Genel Kültür Kitabı – Toplumsal inkılaplar (Gündelik hayat ve kadın hakları) | Kadınlar 1930'da belediye seçimlerine katılma, 5 Aralık 1934'te milletvekili seçme ve seçilme hakkı elde etti. | EŞLEŞTİRME | O | A | GMY-S2
GMY2-015 | Tarih | Genel Kültür Kitabı – Dış politika (Uluslararası ve bölgesel iş birliği) | Balkan Antantı 9 Şubat 1934'te Türkiye, Yunanistan, Yugoslavya ve Romanya arasında kuruldu; Bulgaristan üye değildi. | KAPSAM_DIŞI | ÇK | D | GMY-S2
GMY2-016 | Anayasa | Genel Kültür Kitabı – Anayasa hukuku (Cumhuriyetin temel nitelikleri) | Değiştirilemez hükümler: Cumhuriyet şekli, Devletin nitelikleri, ülke-millet bütünlüğü, Türkçe, bayrak, İstiklal Marşı ve başkent Ankara. | KAPSAM_DIŞI | ÇK | C | GMY-S2
GMY2-017 | Anayasa | Genel Kültür Kitabı – Devlet ve demokrasi; Temel hak ve hürriyetler (Seçim ilkeleri, siyasi haklar) | Seçimlerde oy gizli, sayım ve döküm açıktır; silah altındaki er-erbaş ve askerî öğrenciler oy kullanamaz. | YANLIŞ | K | A | GMY-S2
GMY2-018 | Anayasa | Genel Kültür Kitabı – Yasama (Sorumsuzluk ve dokunulmazlık) | Yasama sorumsuzluğu görev sona erdikten sonra da sürer; dokunulmazlık geçici ve kaldırılabilir niteliktedir. | DOĞRU | O | D | GMY-S2
GMY2-019 | Anayasa | Genel Kültür Kitabı – Yürütme (Cumhurbaşkanlığı kararnamesi); Normlar arasında ilişki | Siyasi haklar CBK ile düzenlenemez, sosyal-ekonomik haklar yasak listede sayılmaz; kanunla çatışmada kanun uygulanır, denetimi AYM yapar. | ÖNERMELİ | ÇZ | C | GMY-S2
GMY2-020 | Uluslararası | Genel Kültür Kitabı – Uluslararası kuruluşlar (NATO ve AGİT; AB, Avrupa Konseyi ve AİHM) | Türkiye NATO'ya 1952'de üye oldu, Avrupa Konseyinin kurucu üyesidir; AB'de 1999'da aday oldu, müzakereler 2005'te başladı. | EŞLEŞTİRME | K | E | GMY-S2
GMY2-021 | Gümrük Kıymeti | GY 51/9 | Navlun/sigorta belgesi ibraz edilemezse, vergi kaybı yoksa ve yükümlü talep ederse FOB kıymetinin %10'u navlun, %3'ü sigorta olarak eklenir. | HESAP | O | B | GMY-S2
GMY2-022 | Gümrük Kıymeti | GK 27/1-a-iii, 27/1-b-iv, 27/1-e, 28/a; GY 43/1-e, 51/6 | Giriş yerinden sonraki noktaya aynı taşıtla taşımada navlun mesafe oranıyla bölünür; ambalaj eklenir, Türkiye'de yapılan çizim hizmeti eklenmez. | HESAP | ÇZ | C | GMY-S2
GMY2-023 | Gümrük Kıymeti | GY 55/1 | İlişki için oy hakkı veren hisse/sermaye paylarının en az %5'inin aynı kişilere ait olması gerekir; %3 yetmez; kontrol ilişkileri ilişki sayılır. | OLAY | Z | D | GMY-S2
GMY2-024 | Gümrük Kıymeti | GK 24/2-a; GY 45/1-b, 45/1-ç, 45/1-d | Satış bedeli yönteminde ilişki tek başına red nedeni değil; ödenmemiş bedelde ödeme tarihindeki bedel; fiyat düzeltmesi bir yıl; ardıl satışta son satış. | ÖNERMELİ | Z | C | GMY-S2
GMY2-025 | Gümrük Kıymeti | Kıymet Tebliği (Seri No:2) md.3/1-a, 5/1, 7/3, 8/1, 10/1 | Marka royaltisinin kıymete eklenmesi için Tebliğde sayılan üç şarttan en az birinin bulunması gerekli ve yeterlidir. | YANLIŞ | O | B | GMY-S2
GMY2-026 | Gümrük Kıymeti | GK 30; GY 57/1, 57/2 | Yabancı paralar yükümlülüğün başladığı tarihteki TCMB döviz satış kuruyla; konvertibl değilse Bilgi Amaçlı Kurlar Listesiyle TL'ye çevrilir. | BOŞLUK | K | E | GMY-S2
GMY2-027 | Gümrük Vergileri | GK 3/26 | Gümrüklenmiş değer: ithal eşyasında CIF kıymeti + gümrük vergileri; ihraç eşyasında FOB kıymeti + gümrük vergileri. | TANIM | ÇK | D | GMY-S2
GMY2-028 | Tahakkuk-Tebliğ-Ödeme | GK 197/2, 197/3 | Beyan ve hesaplanan vergi eşitse teslim tebliğ yerine geçer; noksan vergiler yükümlülüğün doğduğu tarihten itibaren üç yıl içinde tebliğ edilir; dava zamanaşımını durdurur. | OLAY | K | E | GMY-S2
GMY2-029 | Tahakkuk-Tebliğ-Ödeme | GK 198/1, 217, 244/5; Tahsilat Tebliği (Seri No:2) md.18/2 | Noksan vergiler tebliğden itibaren 15 gün içinde ödenir; süre bitmeden yazılı istem ve teminatla ödeme süresi otuz gün daha uzatılabilir. | EŞLEŞTİRME | O | B | GMY-S2
GMY2-030 | Teminat ve Faiz | GK 193/3, 202/2, 206/3; GY 495/1 | Hatalı beyanda yükümlülük başlangıcı–kesinleşme arası gecikme zammı oranında faiz; teminat talep üzerine kısmen çözülür; başkasının teminatı kabul edilebilir. | ÖNERMELİ | Z | E | GMY-S2
GMY2-031 | Gümrük Yükümlülüğü | GK 181/1, 183/2, 185/2, 188/2, 189/2 | Serbest bölgede kanuna aykırı tüketim/kullanımda gümrük yükümlülüğü, eşyanın tüketildiği veya ilk kez kullanıldığı tarihte başlar. | EŞLEŞTİRME | O | C | GMY-S2
GMY2-032 | Geri Verme-Kaldırma | GK 211/2, 213/4, 214; GY 504/2 | Geri verme başvurusu: kanunen ödenmemesi gerekenlerde üç yıl; kusurlu eşya ve uluslararası anlaşmada bir yıl; talep otuz günde karara bağlanır. | ÖNERMELİ | O | D | GMY-S2
GMY2-033 | Geri Verme-Kaldırma | GK 210, 211/1; GY 501/1, 511/2 | Geri verme/kaldırma hükümleri GK kapsamındaki para cezalarına da uygulanır; kasıtlı tahrifat, TPÖ kıymet artırımı ve kusur bilinerek satışta talep kabul edilmez. | KAPSAM | Z | A | GMY-S2
GMY2-034 | Cezalar | GK 241/3-a, 241/3-b, 241/3-j, 241/3-m, 241/4-f | Antrepodaki eşyanın izinsiz elleçlenmesi usulsüzlük cezasının dört katını; ilişki beyan etmeme, yanlış belge, %10 ihracat farkı iki katını gerektirir. | KAPSAM_DIŞI | K | C | GMY-S2
GMY2-035 | Cezalar | GK 238/1, 241/3-l, 241/4-g, 241/5-b | Geçici ithalat eşyası sürenin bitiminden sonra bir ayı aşıp iki ayı aşmayan sürede yeniden ihraç edilirse usulsüzlük cezası dört kat uygulanır. | OLAY | O | A | GMY-S2
GMY2-036 | Cezalar | GK 234/1-b, 234/3, 234/4, 234/6 | Noksan kıymet beyanında vergi farkının üç katı ceza; aykırılık idare tespitinden önce beyan sahibince bildirilirse ceza yüzde on oranında uygulanır. | HESAP | ÇZ | D | GMY-S2
GMY2-037 | Cezalar | GK 235/1-a, 235/1-c, 235/2-a, 235/2-b, 236/1 | İthali yasak eşyada gümrüklenmiş değerin dört katı; ithalatta izin/belge ve ihracı yasak eşyada iki katı; ihracatta belge onda biri; antrepo noksanı iki katı. | EŞLEŞTİRME | O | E | GMY-S2
GMY2-038 | İtiraz-Uzlaşma | GK 242/1, 242/2, 242/3, 244/1; GY 585/4 | Uzlaşma talebinde bulunulması itiraz veya dava açma süresini durdurur; uzlaşma sağlanamazsa süre kaldığı yerden işler. | YANLIŞ | O | C | GMY-S2
GMY2-039 | Temel Tanımlar | GK 3/14, 3/15 | Gümrük kontrolü altında işleme ve hariçte işleme gümrük rejimidir; serbest bölgeye giriş ve yeniden ihraç rejim değil, gümrükçe onaylanmış işlem/kullanım türüdür. | ÖNERMELİ | K | A | GMY-S2
GMY2-040 | Temel Tanımlar | GK 3/14, 3/18 | Rejime tabi tutma, serbest bölgeye giriş, yeniden ihraç, imha ve terk gümrükçe onaylanmış işlem/kullanımdır; eşyanın getirilip idareye bildirilmesi gümrüğe sunmadır. | OLAY | K | D | GMY-S2
GMY2-041 | Kaçakçılık | 5607 2/1-b, 5/2, 5/3 | Etkin pişmanlık: gümrüklenmiş değerin (CIF + gümrük vergileri) iki katı; soruşturma evresinde ödenirse ceza yarı oranında indirilir. | HESAP | ÇZ | E | GMY-S2
GMY2-042 | Kaçakçılık | 5607 3/1, 3/10, 4/1, 4/2, 4/4 | Ceza artırımları: örgüt iki kat; üç veya daha fazla kişi ve görevli/meslek kolaylığı yarı oranında; kapı dışı 1/3–1/2; tütün-alkol-akaryakıt yarısından iki katına. | EŞLEŞTİRME | O | D | GMY-S2
GMY2-043 | Kaçakçılık | 5607 16/1, 18/1, 19/1, 23/2 | Görevliler arasında Kara Kuvvetleri sayılmaz; gümrük idaresi başvurusuyla davaya katılır; tasfiye kararı altı ay; görevlilere muhbir ikramiyesi ödenmez. | ÖNERMELİ | Z | A | GMY-S2
GMY2-044 | Kaçakçılık | 5607 10/2, 10/5 | Alıkonulan taşıt, değeri kadar teminat alıkoymadan itibaren otuz gün içinde verilirse iade edilir; kara taşıtında değer kasko değeridir. | BOŞLUK | K | B | GMY-S2
GMY2-045 | Kaçakçılık | 5607 3/2, 3/3, 3/6, 3/9, 3/22, 3/23 | Transit eşyasını rejime aykırı gümrük bölgesinde bırakma bir-üç yıl hapis ve beş bin güne kadar adli para cezasıdır. | YANLIŞ | O | D | GMY-S2
GMY2-046 | Kaçakçılık | 5607 4/9; İlan Yön. 1/2, 4/1, 6/3, 7/1, 7/3 | İlan süresi üç ay, Bakanlık internet sitesi; suçun mahiyetine göre Genel Müdürlükçe bir katına kadar artırılabilir; 18 yaş altına uygulanmaz. | YANLIŞ | O | A | GMY-S2
GMY2-047 | Gümrük Müşavirliği | GY 563/3 | Müşavir yardımcısı ve stajyerin göreve başlama-ayrılması müşavirce bir hafta içinde derneğe, dernekçe bir hafta içinde başmüdürlüğe bildirilir. | BOŞLUK | K | B | GMY-S2
GMY2-048 | Gümrük Müşavirliği | GK 226/4, 227/3, 229/2; GY 563/3 | Yardımcı izin belgesiyle faaliyete başlar; ayrılana müşavir ilişik kesme belgesi düzenler; yardımcı birden fazla tüzel kişiliğe ortak olamaz; stajyerin mali sorumluluğu müşavirdedir. | ÖNERMELİ | O | E | GMY-S2
GMY2-049 | Gümrük Müşavirliği | GK 227/1-g, 227/3, 229/2; GY 566/1 | Müşavir yardımcılığı sınavı yazılı ve tek aşamalıdır; müşavirlik sınavı yazılı ve sözlü iki aşamalıdır. | YANLIŞ | Z | C | GMY-S2
GMY2-050 | YGM | YGM Tebliği 11/1-a, 11/1-ç, 11/1-f | AN6 özel antrepoya, AN8 genel antrepoya eşya giriş çıkış tespitidir; AN7 altı aylık stok, AN9 elleçleme, OK1 OKSB ön incelemesi. | EŞLEŞTİRME | O | E | GMY-S2
GMY2-051 | YGM | GY 575/4, 575/5, 575/7; YGM Tebliği 13/1-c, 17/2-d | Antrepo giriş-çıkış ve stok tespiti yapan YGM, iki genel antrepoyu geçmemek üzere toplam dört antrepo için rapor düzenleyebilir. | YANLIŞ | Z | A | GMY-S2
GMY2-052 | Disiplin | GK Geçici 6/8 | Uyarma ve kınamayı yetkili gümrük başmüdürü, geçici alıkoymayı Merkez Disiplin Kurulu, meslekten çıkarmayı Yüksek Disiplin Kurulu verir. | YETKİ | K | E | GMY-S2
GMY2-053 | Disiplin | GK Geçici 6/4, 6/5, 6/7, 6/9 | Tedbiren izin belgesinin alındığı süre, sonradan verilen geçici alıkoyma cezasından mahsup edilir. | YANLIŞ | O | B | GMY-S2
GMY2-054 | Temsil | GK 225/1, 225/2; GY 561/4-c, 561/4-ç | Kamu ve özel hukuk tüzel kişisi yetkilileri tüm işlemleri, gerçek kişi ticari olmayan eşyayı, taşıyıcılar yalnız transit işlemlerini doğrudan temsille takip eder. | EŞLEŞTİRME | K | C | GMY-S2
GMY2-055 | Yetkilendirilmiş Yükümlü | GİKY 4/1, 4/2, 16/1, 16/2, 27/1 | YYS sertifikası askı, geri alma ve iptal hükümleri saklı kalmak kaydıyla süresizdir; düzenlendiği tarihten sonraki ilk iş günü geçerli olur. | DOĞRU | O | A | GMY-S2
GMY2-056 | Onaylanmış Kişi | GY 22/1; OKS Tebliği 4/2, 4/3, 4/6, 13/1 | Onaylanmış kişi statüsü için TGB'de yerleşik ve en az iki yıldır fiilen faaliyette bulunmak gerekir; belge süresi iki yıldır. | YANLIŞ | O | B | GMY-S2
GMY2-057 | Beyan | GY 118/1, 131/1 | Beyanname yerine kullanılan belgeler: elçilik ve kurye mektubu, TIR, ATA, CPD karnesi, kumanya listesi, Déclaration en Douane, sergi-fuar ve sözlü beyan formu. | KAPSAM_DIŞI | ÇK | D | GMY-S2
GMY2-058 | Beyan | GK 63, 64/1, 64/5; GY 124/2 | Teslimden sonra düzeltme yok; muayene bildirildiyse sonuç alınmadan iptal yok; yanlış rejimde iptal talebi tescilden itibaren üç ay; iptal cezaya engel değil. | ÖNERMELİ | Z | A | GMY-S2
GMY2-059 | Beyan | GY 180/2 | Sarı hat: muayeneye gerek görülmeksizin beyanname ve eklerinin doğruluğu ile birbiriyle uygunluğunun kontrol edildiği hattır. | EŞLEŞTİRME | K | B | GMY-S2
GMY2-060 | Muayene/Tahlil | GY 130/3, 196/1-a, 196/6 | Dökme gelen 28-29. fasıl eşyası tahlile tabidir; yükümlü OKSB veya YYS sahibiyse tahlil sonuçları alınmadan eşya teslim edilir. | OLAY | ÇZ | A | GMY-S2
GMY2-061 | Menşe | GK 18/2-e, f, g, h, ı; GK 18/3 | Kara suları dışından çıkarılan av ürünü, ancak o ülkede kayıtlı ve o ülke bandıralı araçla çıkarılırsa o ülkede tümüyle elde edilmiş sayılır. | KAPSAM_DIŞI | O | C | GMY-S2
GMY2-062 | Menşe | GY 34/2-a, b, ç, d, e | Yetersiz sayılan işlemlerin iki veya daha fazlasının bir arada yapılması da yetersiz işçilik sayılır; eşyaya menşe kazandırmaz. | YANLIŞ | Z | D | GMY-S2
GMY2-063 | Menşe | GY 38/1, 38/2; GY 40/1, 40/4 | Menşe şahadetnamesi menşe veya ihracatçı ülke makamlarınca düzenlenir; şüphede gümrük idaresi ek kanıt ister; kıymet zorunlu bilgi değil; sonradan ibraz süresi altı ay. | ÖNERMELİ | O | E | GMY-S2
GMY2-064 | Menşe | GK 17/c; GK 19; GK 20; GK 22 | Tek taraflı tercihli tarifeden yararlanan eşyanın tercihli menşe kuralları Cumhurbaşkanı Kararı ile; anlaşma kapsamı eşyanınki anlaşmalarla belirlenir. | DOĞRU | ÇZ | A | GMY-S2
GMY2-065 | Bağlayıcı Bilgi (BTB/BMB) | GK 9/2, 9/4; GY 29/1 | BTB veriliş tarihinden itibaren altı yıl, BMB üç yıl geçerlidir; yanlış veya eksik bilgiye dayanan bağlayıcı bilgi iptal edilir. | YANLIŞ | K | C | GMY-S2
GMY2-066 | Bağlayıcı Bilgi (BTB/BMB) | Tarife Seri No:14 m.7/2, 19, 20; GY 28/10 | Yanlış veya eksik bilgiye dayanan BTB'nin iptali, iptal kararının verildiği tarihten itibaren hüküm ifade eder; tebliğ tarihi esas alınmaz. | EŞLEŞTİRME | Z | A | GMY-S2
GMY2-067 | Tarife | GY 32/1-h, i, j, l, m | Belirli dönemde belli değer/miktar için vergi indirimi ve bu miktarı aşan kısımda indirimin dönem sonuna kadar askıya alınabilmesi tarife tavanıdır. | KAVRAM | O | B | GMY-S2
GMY2-068 | İthalat Rejimi Kararı | İRK (3350) m.9; 2025/10790 s. CK eki listeler | İRK eki listeler: I tarım, III işlenmiş tarım, IV balıkçılık ve su ürünleri, V askıya alınan sanayi, VI sivil hava taşıtı, VII nihai kullanım tarım. | EŞLEŞTİRME | K | D | GMY-S2
GMY2-069 | İthalat Rejimi Kararı | İRK (3350) m.4/3, 9/1, 10/1, 10/2 | TPÖ gözetim, kota ve tarife kontenjanı mevzuatıyla yürütülür; EMY gümrük idarelerince tahsil edilir; II ile V/VI çakışırsa düşük oran; muaf ithalat EMY'ye tabi değil. | ÖNERMELİ | Z | C | GMY-S2
GMY2-070 | Serbest Dolaşıma Giriş | GK 78 | Statü; beyanname iptali, geri ödemeli DİR ihracı, kusurlu/sözleşmeye aykırı eşya ve ihraç-GOİK nedeniyle vergilerin geri verilmesi veya kaldırılmasıyla kaybedilir. | OLAY | O | D | GMY-S2
GMY2-071 | Serbest Dolaşıma Giriş | 2009/15481 s. Karar m.13/1-b | TGB'ye getirilmeden serbest dolaşıma girecek Türk bayraklı gemi için Bayrak Şahadetnamesinden itibaren en geç bir yıl içinde sicile başvurulup kayıt yapılır. | SÜRE | K | E | GMY-S2
GMY2-072 | Nihai Kullanım | GY 208/4, 210/3; Nihai Kullanım Seri No:1 m.6/2-3 | İzinsiz devir izni iptal ettirir; devir başvurusu izni veren idareye ek-31 formla yapılır; ara işlemde sorumluluk izin hak sahibindedir; başka gümrüğe T5 ile gönderilir. | ÖNERMELİ | O | D | GMY-S2
GMY2-073 | Muafiyetler | 2009/15481 s. Karar m.46/1-a, 46/3, 46/4; m.47/1, 47/5 | Taşıt muafiyeti: 24 ay ikamet, son girişten 6 ay önce kayıt, üç yıldan eski olmama; evlilikle vatandaşlıkta ve 5 yıl içinde tekrar yok. | OLAY | ÇZ | E | GMY-S2
GMY2-074 | Muafiyetler | 2009/15481 s. Karar m.58/2, 59/1, 59/2, 60/2 | Ek-9 (A) bölümü sadece yolcu beraberinde; (B) bölümü beraberde veya gelişten bir ay önce ya da üç ay sonra getirilebilir. | YANLIŞ | O | A | GMY-S2
GMY2-075 | Muafiyetler | GY 441/1 | Diplomatik muafiyetle yurda sokulan eşya ve taşıtların her türlü devir veya satışı Dışişleri Bakanlığının önceden iznine tabidir. | YETKİ | ÇK | C | GMY-S2
GMY2-076 | Posta/Hızlı Kargo | Posta ve Hızlı Kargo Tebliği Seri No:1 m.12/1; 2009/15481 s. Karar m.63/3 | Posta/hızlı kargo eşyasında giriş yerine kadar nakliye kıymete eklenir; kıymet fatura/fişe göre, belge yoksa veya düşükse gümrük idaresince belirlenir. | DOĞRU | K | B | GMY-S2
GMY2-077 | Geçici Depolama/GOBİK | GK 46/2-a; GY 76/1 | Uygunluk belgesi gibi belgelerin alınmasında geçen süre durdurulur; işlem sonuçlandığı tarihten itibaren 45 günden kalan süre verilir. | HESAP | Z | C | GMY-S2
GMY2-078 | Geçici Depolama/GOBİK | GK 48/2; GY 79/2 | Yolcu eşyası ambarlarında yolcu eşyası ve taşıtlar üç ay kalır; süre mücbir sebep aranmaksızın gümrük müdürlüğünce üç aya kadar uzatılır. | BOŞLUK | ÇK | E | GMY-S2
GMY2-079 | Özet Beyan | GK 35/A-1, 2, 3; GK 35/B-4, 6 | Özet beyan giriş idaresine, getirilmeden önce, getiren/taşıma sorumlusu tarafından verilir; boşaltma izninden sonra değişiklik yapılamaz. | YANLIŞ | O | C | GMY-S2
GMY2-080 | Fikri-Sınai Haklar | GK 57/2, 57/3, 57/5, 57/6, 57/7 | Hak sahibinin izniyle üretilip onaylanandan farklı şartlarda üretilen eşya kapsam dışıdır; ihtiyati tedbir çabuk bozulabilir eşyada üç, diğerlerinde on işgünü içinde getirilir. | YANLIŞ | O | B | GMY-S2
GMY2-081 | Dahilde İşleme | GK 108 | Teminatla geçici ithal edilip işlem görmüş ürün olarak ihraçta teminat iadesi şartlı muafiyet; tahsil edilen vergilerin geri verilmesi geri ödeme sistemidir. | BOŞLUK | K | A | GMY-S2
GMY2-082 | Dahilde İşleme | DİR Tebliği (İhracat 2006/12) 33 | Telafi edici vergi, ihracat beyannamesinin tescil tarihindeki TCMB döviz satış kuru üzerinden hesaplanarak ihracat esnasında ödenir. | DOĞRU | Z | E | GMY-S2
GMY2-083 | Dahilde İşleme | GK 110; GK 111 | Ticari olmayan DİR ithalatında yurt dışı yerleşiğe izin verilebilir; süre izin tarihinden başlar; önceden ihracatta süre ihracat beyannamesi tescilinden başlar; (c) hallerini Cumhurbaşkanı belirler. | ÖNERMELİ | Z | C | GMY-S2
GMY2-084 | Dahilde İşleme | DİR Tebliği (İhracat 2006/12) 6; GY 352 | Eşdeğer eşya olarak kullanılan tarım ürünlerinde ithal eşyasıyla aynılık tespiti münhasıran on iki'li bazda GTİP'e göre yapılır. | ŞART | O | B | GMY-S2
GMY2-085 | Geçici İthalat | GK 133 | Kısmi muafiyette her ay için tescil tarihindeki vergilerin %3'ü alınır; bir aydan az süreler tam ay sayılır. | HESAP | O | C | GMY-S2
GMY2-086 | Geçici İthalat | Gümrük Kanununun Bazı Maddelerinin Uygulanması Hakkında Karar 36, 39, 40, 43 | Rejim eşyası kiralanamaz/satılamaz (ticari hava taşıtı istisna); tüketilebilir eşya tam/kısmi muafiyetten yararlanamaz; üretim araçlarında süre altı ay; ekonomik etkisiz eşyada üç ay uzatılamaz. | ÖNERMELİ | ÇZ | D | GMY-S2
GMY2-087 | Geçici İthalat | GK 128 | Geçici ithalat: serbest dolaşıma girmemiş eşyanın vergilerden tamamen ya da kısmen muaf kullanılıp olağan yıpranma dışında değişmeden yeniden ihracı. | BOŞLUK | ÇK | B | GMY-S2
GMY2-088 | Geçici İthalat | GK 130 | Özel süreler saklı kalmak üzere geçici ithalatta rejim altında kalma süresi azami yirmi dört aydır; idare ilgilinin kabulüyle daha kısa süre saptayabilir. | SÜRE | K | A | GMY-S2
GMY2-089 | Transit | GY 213/1 | Manifesto yalnız deniz ve havayolunda basitleştirilmiş usulde, Form 302 NATO kuvvetlerinde, sözlü beyan formu ulusal transitte transit beyanıdır. | EŞLEŞTİRME | O | B | GMY-S2
GMY2-090 | Transit | GK 84, 88; GY 213 | Transit rejimi eşya ve belgelerin varış idaresine sunulmasıyla sona erer; karşılaştırma sonrası ibra edilir; 30 günde sunulmayan beyan reddedilir. | YANLIŞ | O | D | GMY-S2
GMY2-091 | TIR | TIR İşlemleri GGT (Seri No: 1) 8 | TIR'da güzergâh katetme süresi Nisan–Eylül azami 120, Ekim–Mart azami 168 saat; süre aşımında GK 241 uyarınca para cezası. | SÜRE | O | E | GMY-S2
GMY2-092 | Antrepo | GY 329 | Genel antrepo A, B, F; özel C, D, E; tarım ürünleri lisanslı deposu yalnız A, C, D, E tipi olabilir. | ÖNERMELİ | ÇZ | D | GMY-S2
GMY2-093 | Antrepo İşleticileri | GY 526, 527 | Götürü/yaygın götürü teminat bölge müdürlüğüne; 5+ antrepoda %75; akaryakıt antreposunda uygulanmaz; alan-hacim değişikliğinde ek teminat bir ay içinde. | YANLIŞ | Z | B | GMY-S2
GMY2-094 | Antrepo | GK 95, 98, 101, 105 | Antrepo kalış süresi sınırsız, idare gerektiğinde süre belirleyebilir; izin Türkiye'de yerleşiklere; işletici hakları izinle devredilebilir; fuar eşyasında teminat aranmaz. | DOĞRU | O | E | GMY-S2
GMY2-095 | Şartlı Muafiyet/EEGR | GK 79 | Şartlı muafiyet: transit, antrepo, şartlı muafiyetli DİR, GKAİR, geçici ithalat; EEGR: antrepo, DİR, GKAİR, geçici ithalat, HİR. Geri ödeme sistemi şartlı muafiyet değildir. | EŞLEŞTİRME | O | B | GMY-S2
GMY2-096 | İhracat | GY 417 | Geçici depolamaya konulmaksızın ihraçta kapatma süresi iki ay, gümrük müdürlüğünce en çok iki ay uzatılır; sürede tamamlanmayan beyanname iptal edilir. | HESAP | K | C | GMY-S2
GMY2-097 | İhracat | GK 151 | İhraç eşyası, tescildeki durum ve niteliğini gümrük kontrolünden çıkarken aynen muhafaza edip TGB'yi terk ederse fiilen ihraç edilmiş sayılır. | ŞART | ÇK | A | GMY-S2
GMY2-098 | Geri Gelen Eşya | GK 168; GY 452, 453 | Üç yıl içinde geri gelen eşya muaf; süre fiili ihraçtan başlar; üç yıl aşılmadan verilen süre aşılırsa usulsüzlük cezası, vergi tahsil edilmez. | YANLIŞ | Z | E | GMY-S2
GMY2-099 | Tasfiye | GK 178 | Tasfiye: ihale, yeniden ihraç amaçlı satış, perakende satış, kamu kuruluşu/vakıf-derneğe tahsis, imha, özel yol; sağlık önlemleri görüş alınarak; usul yönetmelikle. | ÖNERMELİ | O | C | GMY-S2
GMY2-100 | GKAİR | GK 123, 124; GY 370, 372, 373 | GKAİR'de ürün işlenmiş ürün; izin yalnız TGB yerleşiğe; izin azami iki yıl, üç aya kadar uzatma; rejime girişte vergiler teminata bağlanır. | YANLIŞ | O | A | GMY-S2
```

Toplam: 215 satır (Karar: 15 · GMY deneme S1: 100 · GMY deneme S2: 100)
