# Araçlar

- `metin_cikar.py` — `kaynaklar/` içindeki .docx/.doc dosyalarının düz metnini `kaynaklar/metin/` altına çıkarır.
- `karar/` — Karar konusu ders notu ve S1 soru setinin üretim betikleri (şablon olarak diğer konularda kullanılır).
  - `gk.js` ortak Word tasarımı (lacivert #1B3A5C, altın #B8860B, Arial, A4, 1134 twip).
  - `sorular.py` soru verisi, `kontrol.py` harf dağılımı + Protokol A/B uzunluk denetimi, `set.py` Markdown, `set.js` Word çıktısı.
  - `not.js` ders notu (6 blok).
- `gmy-deneme/` — 2025 GMY sınavı modelinde 100 soruluk deneme: `batch_A..E.py` soru verileri (A genel kültür, B–E gümrük), `kontrol_batch.py` kural denetimi, `birlestir.py` kanıt denetimi + harf dağılımı, `cikti.py`/`cikti.js` Markdown/Word çıktısı.
- `gmy-deneme2/` — Prompt 3 kurallarıyla 100 soruluk deneme 2: `batch_GK/G1–G4.py` soru verileri, `kontrol3.py` Prompt 3 denetimi, `birlestir2.py` kanıt denetimi + harf dağılımı (art arda aynı harf yok) + gerekçeye harf yazımı, `cikti2.py/.js` çıktı; `cikmis_envanter.tsv` ve `cikmis_ozet.md` 2021–2025 GMY sınavlarının bilgi alanı analizi (400 gümrük sorusu).
- `sorulmayan/` — 2021–2025 çıkmış sorularla mevzuatın hüküm bazında karşılaştırması ve sorulmayan hükümlerden 2.679 açık uçlu soru–cevap (SC1): grup çıktıları `json/`, bağımsız doğrulama, birleştirme ve Markdown/Word çıktı betikleri (ayrıntı: `sorulmayan/README.md`).
- `soru-tipi/` — 2021–2025 GMY sınavlarının 500 sorusunun soru tipi kataloğu: kitapçık ayrıştırıcı (`ayristir.py`, 2021–2024 resmî cevaplar kırmızı işaretten okunur), etiket sözlüğü (`TIPOLOJI.md`), 500 satırlık etiket tablosu (`tipler.csv`), cevap anahtarı (`cevap_anahtari.tsv`), sayım (`sayim.py` → `istatistik.json`), alt tip kartları (`kartlar/`) ve katalog çıktısı (`katalog.py`, `katalog_docx.js` → `sorular/GK_GMY_Soru_Tipi_Katalogu.md/.docx`).
