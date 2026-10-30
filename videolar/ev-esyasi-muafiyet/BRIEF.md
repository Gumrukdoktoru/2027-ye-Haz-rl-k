---
workflow: faceless-explainer
flow: automation
storyboard: yes
message: "Kullanılmış ev eşyası muafiyeti üç sayıyla akılda kalır: 24 ay dışarıda, yılda en çok 6 ay içeride, gelişten sonra 6 ay içinde beyan"
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

Gümrük Koçu serisinin 4. videosu: Gümrük Muafiyeti Tebliği (Seri No: 2), Üçüncü Bölüm — kullanılmış ev eşyasının
serbest dolaşıma girişi (md. 10–13, 15, 16). Fikir: "Taşınma kolileri + karar ağacı" — kişiler koli etiketleri olarak
gelir; şartlar bir karar ağacında açılır (24 ay → takvim yılında 6 ay / 45 gün → 10 yılda 5 yıl istisnası → yeniden 24 ay);
istisnalar damga; süreler zaman çizgisi; md. 15 akış şeması; md. 16 BİLGE kontrolü. Kullanıcı: "konuya göre backgroundu,
anlatımı, şekil şemaları ve yazıları değiştirebilirsin" — zemin sıcak kraft karton, koli bandı şeritleri.

## Assets

- public/logo-ufuk-cetintas.png — kapanışta kendi renkleriyle (beyaz zemin); video boyunca ortada %10 filigran (kendi renkleri).
- capture/extracted/kaynak-metinleri.txt — depodan çıkarılan hüküm metni (39-muafiyetler.docx, Üçüncü Bölüm md. 10–16).

## Customizations

- Şablon gumruk-kocu-ders: Cem (eleven_v4), Bold Poster yazı tipleri, 16:9, logo kapanışı, müzik yok, altyazı yok.
- Bu videoya özel zemin: kraft karton (#E6D5B8), koyu mürekkep; kırmızı dolgu (#D8000F) ve kırmızı yazı (#A8000B); etiketler beyaz kâğıt.
- Kullanıcının metni esas: md. 14 (belgeler) kapsam dışı (kullanıcı tercihi).
- 4 okuma üretilir, kullanıcı seçer.

## Notes

- Tek bilgi kaynağı depodaki mevzuat (39-muafiyetler.docx); kaynak dışı bilgi yok.
- Marka yalnızca "Gümrük Koçu - Ufuk Çetintaş".
- →, ✓, ✗ gibi işaretler yazı tiplerinde yok; SVG çizilir. İçerik y ≤ 900 px.
