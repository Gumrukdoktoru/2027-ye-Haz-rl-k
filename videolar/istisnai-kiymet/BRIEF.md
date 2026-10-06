---
workflow: faceless-explainer
flow: automation
storyboard: yes
message: "İstisnai kıymetle beyanın bütün kuralları iki tarih arasında geçer: tescil ve tamamlayıcı beyan"
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

Gümrük Koçu serisinin 2. videosu: "İstisnai kıymetle beyan" (GY md. 53, md. 150/3). Fikir: "İki tarih arası" —
açılışta beş eşya (a–d), sonra tek bir zaman çizgisi: TESCİL (mevcut belgelerdeki kıymetle tahakkuk) → eksik unsur
tahakkuk eder / muhasebeye geçer → takip eden ayın 26. günü akşamı TAMAMLAYICI BEYAN (+ ödeme) → yüksek/düşük
sonuçları, zamanaşımı beyandan, gecikme faizi oku geriye tescile. Karar videosuyla aynı görsel dil (kullanıcı:
"yaptığına bayıldım").

## Assets

- public/logo-ufuk-cetintas.png — kullanıcının logosu; yalnızca kapanışta, kendi renkleriyle.
- capture/extracted/kullanici-metni.txt — kullanıcının paylaştığı ders metni (özet); hükümler depodaki kaynakla doğrulandı.

## Customizations

- Şablon gumruk-kocu-ders: Cem (eleven_v4), Bold Poster, 16:9, logo kapanışı, müzik yok, altyazı yok.
- 4 okuma üretilir, kullanıcı seçer.

## Notes

- Tek bilgi kaynağı depodaki mevzuat (12-KIYMET VE KAPLAR.docx, 17-BEYAN.docx); kaynak dışı bilgi yok.
- Kullanıcı metnindeki başka kuruma ait sayfa notu kullanılmaz; marka yalnızca "Gümrük Koçu - Ufuk Çetintaş".
- Logo filigranı: ortada, %10 opaklık, video boyunca (tools/watermark.py; kapanış logosunda söner).
- →, ≠, ⇄ gibi işaretler yazı tiplerinde yok; SVG çizilir. İçerik y ≤ 900 px.
