# Sorulmayan konular — karşılaştırma ve soru–cevap

2021–2025 GMY çıkmış sorularıyla depodaki mevzuat hüküm hüküm karşılaştırılır; hiç ya da kısmen sorulmamış hükümlerden açık uçlu soru–cevap üretilir.

Akış:
1. `GOREV.md` — 19 konu grubunu işleyen ajanlara verilen görev: kaynağı alt konulara bölme, her alt konuyu çıkmış envanterle karşılaştırıp SORULDU / KISMEN / SORULMADI işaretleme, sorulmayanlardan soru–cevap + kaynaktan birebir kanıt kesiti.
2. `DOGRULA.md` — 15 bağımsız doğrulama ajanının görevi: her çifti kaynak hükmün tamamıyla karşılaştırıp OK / DUZELT / SIL kararı.
3. `dogrulama_uygula.py <ham_grup_klasörü> <doğrulama_klasörü>` — doğrulama kararlarını ve `elle_duzeltmeler.json`'u uygular, düzeltilmiş grupları `json/G01…G19.json` olarak yazar, `dogrulama_ozeti.json` (her düzeltmenin eski/yeni hâli ve gerekçesi) üretir.
4. `birlestir.py <metin_klasörü> <cikmis_envanter.tsv>` — grupları birleştirir; kanıt kesitlerini kaynak metinde arar (bulunamayan çift elenir), madde numarası / Karar kökü / tekrar denetimi yapar; konu bazında çıkmış soru sayısını hesaplar (ajanların "ilişkili / çapraz / dolaylı / bu dosyada değil" diye işaretlediği sorular sayılmaz); `sc.json` üretir.
5. `cikti.py` — `sorular/GK_Cikmis_vs_Sorulmayan_Analiz.md`, `sorular/GK_Sorulmayan_Konular_SoruCevap.md` ve hafıza satırları (`hafiza_satirlari.txt`).
6. `cikti.js` — `sorular/GK_Sorulmayan_Konular_SoruCevap.docx` (`../karar/gk.js` tasarımı; `NODE_PATH=$(npm root -g) node cikti.js`).

Yardımcı veriler: `kisa_adlar.json` (tablolarda konu kısa adları), `notlar.json` (yöntem, gözlem, uyarı, kaynakta karşılığı olmayan çıkmışlar).
Metin klasörü `araclar/metin_cikar.py` ile kaynak dosyalardan üretilir (depoya eklenmez); `sc.json` ve `hafiza_satirlari.txt` ara çıktıdır.
