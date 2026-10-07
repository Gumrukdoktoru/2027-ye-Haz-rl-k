# Araçlar

- `metin_cikar.py` — `kaynaklar/` içindeki .docx/.doc dosyalarının düz metnini `kaynaklar/metin/` altına çıkarır.
- `karar/` — Karar konusu ders notu ve S1 soru setinin üretim betikleri (şablon olarak diğer konularda kullanılır).
  - `gk.js` ortak Word tasarımı (lacivert #1B3A5C, altın #B8860B, Arial, A4, 1134 twip).
  - `sorular.py` soru verisi, `kontrol.py` harf dağılımı + Protokol A/B uzunluk denetimi, `set.py` Markdown, `set.js` Word çıktısı.
  - `not.js` ders notu (6 blok).
- `gmy-deneme/` — 2025 GMY sınavı modelinde 100 soruluk deneme: `batch_A..E.py` soru verileri (A genel kültür, B–E gümrük), `kontrol_batch.py` kural denetimi, `birlestir.py` kanıt denetimi + harf dağılımı, `cikti.py`/`cikti.js` Markdown/Word çıktısı.
- `gmy-deneme2/` — Prompt 3 kurallarıyla 100 soruluk deneme 2: `batch_GK/G1–G4.py` soru verileri, `kontrol3.py` Prompt 3 denetimi, `birlestir2.py` kanıt denetimi + harf dağılımı (art arda aynı harf yok) + gerekçeye harf yazımı, `cikti2.py/.js` çıktı; `cikmis_envanter.tsv` ve `cikmis_ozet.md` 2021–2025 GMY sınavlarının bilgi alanı analizi (400 gümrük sorusu).
- `gmy-deneme3/` — Prompt 5 kurallarıyla 50 soruluk karışık deneme 3:
  - `batch_A–E.py`: soru verileri; her soru kaynaktan birebir kanıt alıntısı, çeldirici yuvaları ve set profili alanları taşır.
  - `kontrol5.py`: Prompt 5 denetimi; kanıt alıntısını kaynakta arar, sayısal şık sırasını ve Karar kökü kalıbını kontrol eder.
  - `birlestir5.py`: konu bloklarına dizer, harf dağıtır (sayısal soruların harfi sabit, art arda aynı harf yok), gerekçeye harfi yazar.
  - `cikti5.py`, `cikti5.js`, `pdf5.mjs`: Markdown, Word ve PDF çıktısı.
  - Üretim: `python3 birlestir5.py <metin> set3.json batch_*.py`, ardından `python3 cikti5.py set3.json notlar3.json <ad>`, `node cikti5.js …` ve `node pdf5.mjs <ad>.html <ad>.pdf`.

