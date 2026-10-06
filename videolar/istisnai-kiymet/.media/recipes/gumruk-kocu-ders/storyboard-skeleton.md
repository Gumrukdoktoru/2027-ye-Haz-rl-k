---
format: 1920x1080
duration: 86s
arc: how-to-process (takvim sahnesi) → contrast payoff
music: none
language: tr
---

## Video direction

- **palette:** frame.md Bold Poster — beyaz zemin, mürekkep (#1C1410) yazı ve ızgara çizgileri, tek vurgu domates kırmızısı (#D8000F: halkalar, sayılar, eğik kahraman kelime, ilerleme çubuğu), açık kırık beyaz (#F5F2EF) geçen günlerin dolgusu. 9. sahne tam kırmızı panel. Logo yalnızca 10. sahnede kendi renkleriyle.
- **motion grammar:** power3.out uzun kuyruklu yerleşme; zıplama yok. Her parça seslendirme onu söylediğinde gelir (kelime zamanları audio_meta.json'dan). Halkalar SVG çizimiyle (svg-path-draw), kahraman kelime tek damga hareketiyle (dönerek oturma, −4°/−6° eğim), gün dolguları sayaçla kilitli kademeli.
- **stage:** 1–5 aynı takvim ızgarası, aynı konum ve ölçüde (x 900, 7×5 hücre); 6 ayrı "İTİRAZ" sayfası; 7–8 aynı "LEHE KARAR" şeridi. Kesişen sahnelerde takvim kıpırdamaz.
- **rhythm:** 1 hızlı damga; 2–5 takvimde birikim; 6 üç kısa kural; 7 en uzun (üç şart tek tek); 9 tutulan özet (halkalar çizildikten sonra durgun); 10 sakin imza.
- **negative list:** zıplayan/elastik giriş yok, nefes alan kartlar yok, arka yarıda kaydırma/yaklaşma yok, slayt gibi her şeyi baştan dökmek yok, ekran koruyucu gibi bağımsız süzülen öğeler yok; ikinci vurgu rengi, yuvarlak köşe, gölge (kırmızı paneldeki yazı hariç) yok; →, ≠, ⇄ gibi işaretler yazı tipinde olmadığı için SVG çizilir; içerik y ≤ 900 px.

## Frame 1 — Otuz gün ne zaman başlar?

- duration: 6.06s
- transition_in: cut
- status: outline
- src: compositions/frames/01-otuz-gun.html
- type: hook
- persuasion: Rhetorical question
- beat: curiosity
- blueprint: kinetic-type-beats
- cite: GK md. 6/2

<fill in: this video's content for the "Otuz gün ne zaman başlar?" beat — keep the layout role, replace the words.>

- blueprint: kinetic-type-beats (Adapt)
- focal: kırmızı eğik "30"
- roles: "30" + "GÜN" = foreground subject · boş takvim ızgarası = supporting (sağ) · soru satırı = supporting
- sfx: none

## Frame 2 — İdareye ulaştığı gün

- duration: 7.42s
- transition_in: crossfade
- status: outline
- src: compositions/frames/02-ulastigi-gun.html
- type: product_intro
- persuasion: Common-belief vs reality + Frame-then-fill
- beat: clarity
- blueprint: grid-card-assemble
- cite: GK md. 6/2

<fill in: this video's content for the "İdareye ulaştığı gün" beat — keep the layout role, replace the words.>

- blueprint: grid-card-assemble (Adapt)
- focal: kırmızı eğik "ulaştığı gün."
- roles: takvim = foreground diagram (sağ) · "gönderdiğin gün" = supporting (çizilir) · 0. gün halkası = accent
- sfx: none

## Frame 3 — 0. gün: yazılı talep

- duration: 8.14s
- transition_in: crossfade
- status: outline
- src: compositions/frames/03-yazili-talep.html
- type: feature_showcase
- persuasion: Progressive disclosure
- beat: comprehension
- cite: GK md. 6/1, 6/2

<fill in: this video's content for the "0. gün: yazılı talep" beat — keep the layout role, replace the words.>

- blueprint: compose
- focal: "Başvurunun şekli" kartı
- roles: kart = foreground subject (sol) · takvim (0. gün halkalı) = supporting (sağ, sabit)
- sfx: none

## Frame 4 — 30. gün: karar ve tebliğ

- duration: 7.18s
- transition_in: crossfade
- status: outline
- src: compositions/frames/04-otuzuncu-gun.html
- type: feature_showcase
- persuasion: Demonstration (sayaç) + Counterexample
- beat: "aha"
- blueprint: dataviz-countup
- cite: GK md. 6/2

<fill in: this video's content for the "30. gün: karar ve tebliğ" beat — keep the layout role, replace the words.>

- blueprint: dataviz-countup (Adapt)
- focal: sayaç "30"
- roles: sayaç = foreground subject (sol) · takvim günleri = diagram (sağ) · "iş günü" = supporting
- sfx: none

## Frame 5 — Süre aşımı ret değildir

- duration: 9.42s
- transition_in: crossfade
- status: outline
- src: compositions/frames/05-sure-asimi.html
- type: feature_showcase
- persuasion: Signposting + Common-belief vs reality
- beat: unease → clarity
- cite: GK md. 6/2

<fill in: this video's content for the "Süre aşımı ret değildir" beat — keep the layout role, replace the words.>

- blueprint: compose
- focal: taralı "EK SÜRE" bandı
- roles: takvim = diagram (sağ) · kart = supporting (sol) · "aşım ≠ ret" = foreground payoff
- sfx: none

## Frame 6 — Gerekçe, derhal uygulama, itiraz

- duration: 9.12s
- transition_in: push-slide LEFT
- status: outline
- src: compositions/frames/06-itiraz.html
- type: feature_showcase
- persuasion: Rule of three (gerekçe · derhal · itiraz)
- beat: momentum
- cite: GK md. 6/3, 6/4 · GY md. 586/1

<fill in: this video's content for the "Gerekçe, derhal uygulama, itiraz" beat — keep the layout role, replace the words.>

- blueprint: compose
- focal: "İTİRAZ · 30 GÜN" takvimi
- roles: üç kural = foreground list (sol) · iki damga = accent (üst) · itiraz takvimi = diagram (sağ)
- sfx: none

## Frame 7 — 7/1: üçü bir aradaysa iptal

- duration: 16.7s
- transition_in: push-slide LEFT
- status: outline
- src: compositions/frames/07-yedi-bir.html
- type: feature_showcase
- persuasion: Numbered enumeration + Progressive disclosure
- beat: focus
- cite: GK md. 7/1, 7/4

<fill in: this video's content for the "7/1: üçü bir aradaysa iptal" beat — keep the layout role, replace the words.>

- blueprint: compose
- focal: "ÜÇÜ BİR ARADA" köşeli parantezi
- roles: üç şart kartı = foreground list (sol) · parantez = accent · yürürlük şeridi = diagram (sağ üst) · "verildiği gün" = payoff
- sfx: none

## Frame 8 — 7/2: tebliğ günü

- duration: 10.28s
- transition_in: crossfade
- status: outline
- src: compositions/frames/08-yedi-iki.html
- type: feature_showcase
- persuasion: Comparison of two options
- beat: comprehension
- cite: GK md. 7/2, 7/4

<fill in: this video's content for the "7/2: tebliğ günü" beat — keep the layout role, replace the words.>

- blueprint: compose
- focal: ikinci halka "TEBLİĞ GÜNÜ"
- roles: iki koşul kartı = foreground list (sol) · şerit = diagram (sağ üst) · "tebliğ günü" = payoff
- sfx: none

## Frame 9 — İki halka

- duration: 7.5s
- transition_in: blur-crossfade
- status: outline
- src: compositions/frames/09-iki-halka.html
- type: branding
- persuasion: Distillation + Callback (takvim)
- beat: "now I get it"
- blueprint: comparison-split
- cite: GK md. 7/4

<fill in: this video's content for the "İki halka" beat — keep the layout role, replace the words.>

- blueprint: comparison-split (Adapt)
- focal: iki beyaz halka
- roles: halkalar = foreground pair · etiketler = supporting · çift yönlü ok = accent
- sfx: none

## Frame 10 — Gümrük Koçu

- duration: 4.34s
- transition_in: blur-crossfade
- status: outline
- src: compositions/frames/10-kapanis.html
- type: cta
- persuasion: Brand sign-off
- beat: resolve
- blueprint: titlecard-reveal

<fill in: this video's content for the "Gümrük Koçu" beat — keep the layout role, replace the words.>

- blueprint: titlecard-reveal (Reproduce)
- focal: kullanıcı logosu
- roles: logo = foreground subject (orta) · @gumrukkocunuz = supporting
- sfx: none
