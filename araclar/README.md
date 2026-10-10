# Araçlar

- `metin_cikar.py` — `kaynaklar/` içindeki .docx/.doc dosyalarının düz metnini `kaynaklar/metin/` altına çıkarır.
- `karar/` — Karar konusu ders notu ve S1 soru setinin üretim betikleri (şablon olarak diğer konularda kullanılır).
  - `gk.js` ortak Word tasarımı (lacivert #1B3A5C, altın #B8860B, Arial, A4, 1134 twip).
  - `sorular.py` soru verisi, `kontrol.py` harf dağılımı + Protokol A/B uzunluk denetimi, `set.py` Markdown, `set.js` Word çıktısı.
  - `not.js` ders notu (6 blok).
- `gmy-deneme/` — 2025 GMY sınavı modelinde 100 soruluk deneme: `batch_A..E.py` soru verileri (A genel kültür, B–E gümrük), `kontrol_batch.py` kural denetimi, `birlestir.py` kanıt denetimi + harf dağılımı, `cikti.py`/`cikti.js` Markdown/Word çıktısı.
- `gmy-deneme2/` — Prompt 3 kurallarıyla 100 soruluk deneme 2: `batch_GK/G1–G4.py` soru verileri, `kontrol3.py` Prompt 3 denetimi, `birlestir2.py` kanıt denetimi + harf dağılımı (art arda aynı harf yok) + gerekçeye harf yazımı, `cikti2.py/.js` çıktı; `cikmis_envanter.tsv` ve `cikmis_ozet.md` 2021–2025 GMY sınavlarının bilgi alanı analizi (400 gümrük sorusu).
- `gmy-deneme345/` — 2024–2025 sınavları esas alınarak hazırlanan 100'er soruluk deneme 3, 4 ve 5: `batch_GKA/GKB.py` (genel kültür) ve `batch_G1–G8.py` (gümrük) soru verileri, `kontrol4.py` set bazlı Prompt 3 denetimi (zorluk dağılımı, çekirdek benzerliği; `kontrol3.py`'yi kullanır), `birlestir3.py` kanıt denetimi + harf dağılımı (her harf 20, art arda aynı harf yok; sayı/Romen/saat/tarih şıkları doğal sırada) + 2024–2025 kapsam raporu, `tekrar.py` önceki setlerle çekirdek karşılaştırması, `cikti3.py/.js S` Markdown/Word çıktısı, `set3/4/5.json` birleşik setler; `YAZAR_TALIMAT.md`, `DOGRULAYICI_TALIMAT.md`, `DUZELTME_LISTESI.md` üretim ve çekişmeli doğrulama kayıtları.
  - `anahtar.py` cevaplı sınav PDF'lerindeki kırmızı işaretten resmî cevapları çıkarır (pymupdf); `anahtarlar/` 2021–2025 resmî cevap anahtarları (2025 için A kitapçığı ve B numaralı eşleme).
  - `cikmis_envanter.tsv` 2021–2025 GMY sınavlarının 400 gümrük sorusunun bilgi alanı analizi, `RESMI_CEVAP` sütunuyla.
- `gmy-deneme6-10/` — Prompt 4 (GMY Soru Motoru – Master) ile 2021–2025 GMY sınavlarının 500 sorusunu birebir karşılayan Deneme 6–10 (her biri 20 genel kültür + 80 gümrük; Deneme 6 ← 2021 … Deneme 10 ← 2025 B kitapçığı sırası).
  - `kumeler.py` 15 gümrük konu kümesi + 4 genel kültür dersi; `plan.py` → `plan.json` soru soru plan (çıkmış soru, tip T1–T10, şık sınıfı, ters tuzak, kök bandı, cevap harfi).
  - `YAZAR_TALIMAT.md`, `gorev/<küme>.md`, `hafiza/<küme>.txt` yazar girdileri; `batch_<küme>.py` soru verileri.
  - `kontrol.py` master prompt + Prompt 3 denetimi (kanıt alıntısı kaynakta birebir, uzunluk dengesi, ters tuzak, tip/kök kuralları, Karar kalıbı); `birlestir.py` → `set6–10.json` (harf yerleşimi, deneme düzeyi dağılım); `tekrar_aday.py` aynı madde/fıkra tekrar adayları; `degisen.py` doğrulama sonrası değişen sorular.
  - `cikti.py`/`cikti.js N` Markdown/Word çıktısı (kitapçık + çözümlü sorular, master §10 formatı); `hafiza_ekle.py` üretim hafızasına 500 satır ekler.
  - `DOGRULAYICI_TALIMAT.md`, `dogrulama/` (V1–V10 çekişmeli doğrulama, T1–T2 tekrar denetimi, S1–S3 son doğrulama raporları), `DUZELTME_LISTESI.md` düzeltme kaydı.

