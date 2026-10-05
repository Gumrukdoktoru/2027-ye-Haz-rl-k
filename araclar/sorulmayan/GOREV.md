# Görev: Sorulmayan hükümlerin tespiti + Soru–Cevap üretimi (Gümrük Koçu - Ufuk Çetintaş)

## Girdi dosyaları (hepsi scratchpad'de)
- Kaynak mevzuat metinleri: `<calisma>/src/metin/*.txt` (SP = /tmp/claude-0/-home-user/7f6b7410-3ed4-5b89-a875-19fe112f5a9c/scratchpad)
- 2021–2025 GMY çıkmış soruların bilgi alanı envanteri (400 gümrük sorusu): `<calisma>/cikmis_envanter.tsv`
  Sütunlar: YIL, SORU_NO, KONU, ÖLÇÜLEN_BİLGİ, KALIP, KAYNAK_DOSYA, CEVAP
- Çıkmış sınavların ham metinleri (gerekirse soru metnine bakmak için): `<calisma>/pdf/2021.txt … 2025.txt` (sorular 21–100 gümrük)

## Yapılacaklar (sana verilen kaynak dosyaların HER BİRİ için)
1. **Çıkmışları topla:** Envanterde KAYNAK_DOSYA = bu dosya olan satırları ve KONU'su bu dosyanın konusuna giren (KAYNAK_DOSYA farklı/YOK olsa bile) satırları al. Gerekirse `<calisma>/pdf/YIL.txt` içinde soru metnine bak. Bu satırlar = o dosyadan **sorulmuş bilgi noktaları**.
2. **Dosyayı alt konulara böl:** Kaynağı baştan sona oku; hüküm/madde gruplarını sınav değeri taşıyan alt konulara ayır (ör. "Özet beyanın verilme süreleri", "Kabotajda yükleme izni"). Her alt konu için durum belirle:
   - `SORULDU` — alt konunun asıl bilgi noktası çıkmış soruda ölçülmüş (çıkmış soru numaralarını yaz: "2023-39").
   - `KISMEN` — maddeden bir ayrıntı sorulmuş, diğer sınav değeri taşıyan ayrıntıları sorulmamış (nelerin sorulmadığını `not` alanında yaz).
   - `SORULMADI` — beş yılda hiç ölçülmemiş.
   Salt şekli maddeleri (amaç, kapsam cümlesi, yürürlük, yürütme, mülga) alt konu yapma; ama dayanak/kapsam bilgisi sınav değeri taşıyorsa (ör. tebliğin hangi Kararı uyguladığı) alt konu yapabilirsin.
3. **Soru–Cevap üret:** `SORULMADI` alt konuların tamamı ve `KISMEN` alt konuların sorulmamış ayrıntıları için açık uçlu soru–cevap çiftleri yaz. Sorulmuş bilgi noktasını tekrar sorma.
   - Her çift TEK bir sınav değeri taşıyan bilgiyi ölçer (süre + başlangıç noktası, oran, tutar, eşik, makam, belge, şart, istisna, kapsam, tanım, yaptırım, hesaplama esası…). Aynı bilgiyi iki kez sorma.
   - **Soru**: kısa, resmî, kurum dili; mevzuat adı + hükmün konusu ile başlar. Ör. "Gümrük Yönetmeliğine göre kabotaj taşımalarında … kaç gün içinde …?", "4458 sayılı Gümrük Kanununa göre … hangi makam yetkilidir?". Kökte/soruda madde, fıkra, bent numarası YOK. 2009/15481 sayılı Karara dayanan soruda "4458 sayılı" ile başlama; `2009/15481 sayılı "4458 sayılı Gümrük Kanununun Bazı Maddelerinin Uygulanması Hakkında Karar"a göre …` kalıbını kullan. Tebliğ/yönetmelikte adını yaz (ör. "Gümrük Genel Tebliği (Transit Rejimi) (Seri No: 8)'e göre …", "5607 sayılı Kaçakçılıkla Mücadele Kanununa göre elkonulan eşyaya ilişkin Uygulama Yönetmeliğine göre …").
   - **Cevap**: 1–3 cümle, net ve eksiksiz; sayıları, makamları, istisnaları mevzuattaki gibi ver; varsa tuzak ayrımını ekle (iş günü/takvim günü, gümrük müdürlüğü/bölge müdürlüğü, "aranmaz", "en az/en fazla" vb.). Cevapta madde numarası yazma (o `dayanak` alanına gider).
   - **dayanak**: kısaltma + madde/fıkra: "GK md. 33/1", "GY md. 52/2", "2009/15481 Karar md. 24", "Seri No 8 Tebliğ md. 7/3", "5607 md. 19/2", "Kabotaj Tebliği md. 6", "İthalat Rejimi Kararı md. 7" vb.
   - **kanit**: kaynak metinden BİREBİR kopyalanmış, cevabı destekleyen 40–300 karakterlik kesit (yazım/noktalama aynen; kendi kelimeni ekleme, kısaltma yapma). Gerekirse birden fazla kesiti ` ... ` ile ayır (her kesit ≥25 karakter ve birebir). Bu kesitler otomatik olarak kaynakta aranacak; bulunamayan çift elenecek.
   - Yalnızca kaynak metinde bulunan bilgi; web/hafıza bilgisi YOK. Dipnotlarda verilen eski/mülga metinleri ([123] gibi dipnot atıfları, "değişik", "mülga" açıklamaları) değil, yürürlükteki metni esas al. Mülga hükümden soru yazma.
   - Eski kurum adları (Müsteşarlık vb.) metinde nasılsa öyle kullanılabilir.
   - Hacim: sınav değeri taşıyan her sorulmamış bilgi için bir çift. Kaba ölçü: kaynak dosya < 20 KB → 8–20 çift; 20–60 KB → 20–40; 60–120 KB → 35–60; > 120 KB → 50–80. Önemsiz ayrıntı (form kutusu doldurma tarifi, adres, başvuru dilekçesinin kaçıncı nüsha olduğu gibi) için çift yazma; şişirme yapma.
4. **Öz-denetim:** Her çiftte sayı/süre/makam/oran kanıt kesitiyle aynı mı? Soru tek ve tartışmasız cevaplı mı? Cevap soruyla örtüşüyor mu? Çıkmış soru tekrarı var mı? Kanıt kesitlerini `python3` ile kaynak metinde (boşluklar normalize edilerek) arayıp doğrula; bulunamayanları düzelt.

## Çıktı
Python ile `json.dump(..., ensure_ascii=False, indent=1)` kullanarak `<calisma>/out/<GRUP>.json` dosyasına yaz (elle JSON yazma). Biçim:
```json
{"grup": "G03",
 "dosyalar": [
  {"kaynak": "13-TAŞITLAR.txt",
   "konu": "Taşıtlar (Türkiye Gümrük Bölgesine giriş-çıkış)",
   "mevzuat": "GK md. 33-34; GY md. …",
   "cikmis_sayisi": 1,
   "cikmis": ["2021-58: <ölçülen bilgi kısaca>"],
   "alt_konular": [
     {"baslik": "Gümrük kapıları ve izlenecek yollar", "dayanak": "GK md. 33", "durum": "SORULMADI", "cikmis": [], "not": ""}
   ],
   "soru_cevap": [
     {"alt_konu": "Gümrük kapıları ve izlenecek yollar",
      "soru": "4458 sayılı Gümrük Kanununa göre Türkiye Gümrük Bölgesine giriş ve çıkış nereden yapılır?",
      "cevap": "Giriş ve çıkış gümrük kapılarından yapılır; giriş noktalarındaki gümrük kapıları ile içerideki gümrük kapıları arasında belirli yolların takip edilmesi zorunludur.",
      "dayanak": "GK md. 33",
      "kanit": "Türkiye Gümrük Bölgesine giriş ve çıkış, gümrük kapılarından yapılır."}
   ]
  }
 ]}
```
`alt_konular` sırası kaynak metindeki sıradır; `soru_cevap` de alt konu sırasını izler. Son mesajında yalnızca kısa bir özet ver: dosya başına alt konu sayısı (SORULDU/KISMEN/SORULMADI) ve çift sayısı, kanıt doğrulama sonucu. JSON içeriğini mesajda tekrar etme.
