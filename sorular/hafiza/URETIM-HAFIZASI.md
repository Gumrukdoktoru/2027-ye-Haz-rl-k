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
```

Toplam: 115 satır (Karar: 15 · GMY-2025 deneme S1: 100)
