# CLAUDE.md — 2027'ye Hazırlık (Gümrük Koçu)

GM / GMY sınavlarına hazırlık için Word kaynaklarından **ders notu** ve **test sorusu** üretim deposu.

## Yapı
- `kaynaklar/` — kullanıcının yüklediği Word dosyaları (değiştirilmez). `kaynaklar/metin/` düz metin çıktıları, `KAYNAK-LISTESI.md` dizin.
- `promptlar/prompt-1-akilli-test-soru-motoru.md` — test sorusu üretim kuralları (Prompt 1).
- `promptlar/prompt-2-ders-notu-motoru.md` — ders notu üretim kuralları (Prompt 2).
- `sorular/` — üretilen soru setleri; `sorular/hafiza/URETIM-HAFIZASI.md` üretim hafızası.
- `notlar/` — üretilen ders notları (Ders_Notu_{KONU}.docx).

## Çalışma kuralları
- Soru isteğinde Prompt 1'i, ders notu isteğinde Prompt 2'yi eksiksiz uygula.
- Tek bilgi kaynağı `kaynaklar/` içeriğidir; web araştırması yok, kaynakta olmayan bilgi yok.
- Her soru setinden önce `URETIM-HAFIZASI.md` okunur, set bitince yeni satırlar eklenip commit edilir.
- Marka yalnızca "Gümrük Koçu - Ufuk Çetintaş".
- Kullanıcı kök klasöre yeni dosya yüklerse: `kaynaklar/`a taşı, metnini `kaynaklar/metin/`e çıkar, `KAYNAK-LISTESI.md`yi güncelle.
