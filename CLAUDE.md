# CLAUDE.md — 2027'ye Hazırlık (Gümrük Koçu)

GM / GMY sınavlarına hazırlık için Word kaynaklarından **ders notu** ve **test sorusu** üretim deposu.

## Yapı
- Kaynak mevzuat dosyaları (Word/.doc/PDF) **depo kökünde** durur (kullanıcı 3 Ekim 2026'da `kaynaklar/` klasörünü kaldırıp kaynakları köke yükledi; düzen değiştirilmez). Çıkmış sınavlar: `2021–2024-gmy-sinavi-cevapli.pdf`, `2025_..._CEVAPSIZ.pdf`.
- `promptlar/prompt-1-akilli-test-soru-motoru.md` — test sorusu üretim kuralları (Prompt 1).
- `promptlar/prompt-2-ders-notu-motoru.md` — ders notu üretim kuralları (Prompt 2).
- `promptlar/prompt-3-nihai-soru-hazirlama-kurallari.md` — kullanıcının nihai soru hazırlama kuralları (Prompt 3). Soru üretiminde Prompt 1 ile çelişirse **Prompt 3 geçerlidir** (çıkmış soruların bilgi alanları atlanmaz, kök = mevzuat adı + hükmün konusu + kurum kalıbı, önermeli en az 3 önerme, gerekçe sonunda (MD …), art arda aynı cevap harfi yok).
- `sorular/` — üretilen soru setleri; `sorular/hafiza/URETIM-HAFIZASI.md` üretim hafızası.
- `notlar/` — üretilen ders notları (Ders_Notu_{KONU}.docx).
- `tekrar/` — hızlı tekrar kısa soru-cevap setleri (Tekrar_{NO}_{KONU}.md/.docx); konu sırası kökteki numaralı Word dosyalarıdır. Veri `araclar/tekrar/veri_{NO}.js`, çıktı `node araclar/tekrar/cikti.js {NO}`.

## Çalışma kuralları
- Soru isteğinde Prompt 1'i, ders notu isteğinde Prompt 2'yi eksiksiz uygula.
- Tek bilgi kaynağı depoya yüklenen mevzuat dosyalarıdır; web araştırması yok, kaynakta olmayan bilgi yok.
- Her soru setinden önce `URETIM-HAFIZASI.md` okunur, set bitince yeni satırlar eklenip commit edilir.
- Marka yalnızca "Gümrük Koçu - Ufuk Çetintaş".
- Kullanıcı yeni kaynak yüklerse dosyaları taşımadan metnini çıkar (araclar/metin_cikar.py) ve çalışmada kullan.

## Kullanıcı tercihleri
- **Konu kapsamı serbest:** Sınav kitapçığı modelinde set üretilirken kitapçıktaki konu dağılımıyla sınırlı kalınmaz; `kaynaklar/` içindeki diğer konulardan da (ör. kabotaj, özet beyan, sınır ticareti, ihracat sayılan satış ve teslimler, e-ihracat, dış ticaret sermaye şirketi, fuar tebliği, bedelsiz ihracat, telafi edici vergi) soru sorulabilir. Kaynakta olmayan bilgi kuralı değişmez.
- Kitapçık soruları kopyalanmaz; aynı konu sorulursa farklı hüküm seçilir.
- **Karar kaynaklı sorularda kök:** 2009/15481 sayılı Bakanlar Kurulu Kararına dayanan sorularda kök "4458 sayılı …" ile başlamaz (Kanun sanılır). Kurum kalıbı kullanılır: `2009/15481 sayılı "4458 sayılı Gümrük Kanununun Bazı Maddelerinin Uygulanması Hakkında Karar"a göre …`. Diğer kararlar ve yönetmelikler için de kök, dayanağın türünü (Kanun/Karar/Yönetmelik/Tebliğ) baştan açıkça göstermelidir.
