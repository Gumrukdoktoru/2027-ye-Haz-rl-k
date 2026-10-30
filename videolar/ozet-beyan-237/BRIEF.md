---
workflow: faceless-explainer
flow: automation
storyboard: yes
message: "Özet beyan ile boşaltma listesi tutmazsa: noksan kapta vergi kadar ceza, fazla kapta el koyma ve CIF kadar ceza"
destination: youtube
aspect: 1920x1080
language: tr
audience: "GM / GMY sınavına hazırlanan adaylar"
length: 120s
angle: concept
style_preset: bold-poster
voice: "ElevenLabs Cem (D1xRw7f8ZHedI7xJgfvz), model eleven_v4"
recipe: gumruk-kocu-ders
---

## Intent

Gümrük Koçu serisinin 3. videosu: "Özet beyanda aykırılıklar" (GK md. 237; GY md. 75, 583). Fikir: "Liman" —
gemi yanaşır, iki liste karşılaştırılır (özet beyan ↔ boşaltma listesi). Eksik kap kırmızı, fazla kap kehribar
yanar; her fıkranın sonucu damga olarak basılır. Kullanıcı: "konuya göre backgroundu değiştirebilirsin" —
zemin beyaz yerine lacivert liman gecesi; belgeler (listeler, kartlar) kırık beyaz kâğıt.

## Assets

- public/logo-ufuk-cetintas.png — kullanıcının logosu; kapanışta kendi renkleriyle (beyaz zeminde), video boyunca ortada %10 filigran (lacivert zeminde beyaz silüet).
- capture/extracted/kaynak-metinleri.txt — depodan çıkarılan hüküm metinleri (GK 237, GY 75, GY 583, TIR Seri No: 6).

## Customizations

- Şablon gumruk-kocu-ders: Cem (eleven_v4), Bold Poster yazı tipleri, 16:9, logo kapanışı, müzik yok, altyazı yok.
- Bu videoya özel zemin: lacivert (#0E2640), alt bantta koyu deniz; vurgu kırmızı (eksik), kehribar (fazla).
- 4 okuma üretilir, kullanıcı seçer.

## Notes

- Tek bilgi kaynağı depodaki mevzuat (48-cezalar.docx: GK 237, GY 582–583; 15-ÖZET BEYAN.docx: GY 75; 21-TIR SÖZLEŞMESİ.docx: TIR Seri No: 6); kaynak dışı bilgi yok.
- "3 ay + 3 ay + 1 ay" yalnızca TIR karnesi için (TIR Seri No: 6) küçük not olarak gösterilir; ana kural "gümrük idaresince belirlenecek süre" (kullanıcı onayı).
- 241/1 tutarı yazılmaz (yeniden değerleme ve AYM kararı notu var); "241/1'deki miktar" denir.
- Marka yalnızca "Gümrük Koçu - Ufuk Çetintaş".
- →, ≠, ✓, ✗ gibi işaretler yazı tiplerinde yok; SVG çizilir. İçerik y ≤ 900 px.
