# Sorulmayan konular — karşılaştırma ve soru–cevap

2021–2025 GMY çıkmış sorularıyla depodaki mevzuat hüküm hüküm karşılaştırılır; hiç ya da kısmen sorulmamış hükümlerden açık uçlu soru–cevap üretilir.

- `GOREV.md` — konu gruplarını işleyen ajanlara verilen görev tanımı (alt konu çıkarma, durum işaretleme, soru–cevap + birebir kanıt kesiti).
- `json/G01…G19.json` — grup çıktıları (alt konular, durumlar, soru–cevaplar, kanıt kesitleri).
- `birlestir.py <metin_klasörü> <cikmis_envanter.tsv>` — grupları birleştirir, kanıt kesitlerini kaynak metinde arar (bulunamayan çift elenir), madde numarası / Karar kökü / tekrar denetimi yapar, `sc.json` üretir.
- `cikti.py` — `sorular/GK_Cikmis_vs_Sorulmayan_Analiz.md`, `sorular/GK_Sorulmayan_Konular_SoruCevap.md` ve hafıza satırlarını (`hafiza_satirlari.txt`) üretir.
- `cikti.js` — `sorular/GK_Sorulmayan_Konular_SoruCevap.docx` (Word; `../karar/gk.js` tasarımı).

Metin klasörü `araclar/metin_cikar.py` ile kaynak dosyalardan üretilir (depoya eklenmez).
