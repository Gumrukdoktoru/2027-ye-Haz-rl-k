---
format: 1920x1080
duration: 86s
message: "Karar konusundaki süre ve yürürlük tuzakları tarihlerle akılda kalır"
arc: how-to-process (takvim sahnesi) → contrast payoff
audience: GM / GMY sınavına hazırlanan adaylar
mode: collaborative
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

- scene: Boş takvim sayfası; ortaya kırmızı, eğik "30 GÜN" damgası iner, altına soru belirir
- voiceover: "Gümrük idaresinin karar vermek için otuz günü var. Peki bu otuz gün… ne zaman başlar?"
- duration: 6.06s
- transition_in: cut
- status: animated
- src: compositions/frames/01-otuz-gun.html
- type: hook
- persuasion: Rhetorical question
- beat: curiosity
- blueprint: kinetic-type-beats
- cite: GK md. 6/2

narrativeRole: Sınavın en çok sorduğu sayıyı (30) verip başlangıç anını soru olarak açık bırakır; bilgi boşluğu yaratır.
keyMessage: Otuz günü bilmek yetmez; sürenin hangi gün başladığı sorulur.

- blueprint: kinetic-type-beats (Adapt)
- focal: kırmızı eğik "30"
- roles: "30" + "GÜN" = foreground subject · boş takvim ızgarası = supporting (sağ) · soru satırı = supporting
- sfx: none

Adapt: kelime ritmi korunur; "30" damgası imza hareketi.
Scene 1 (0.0–2.0s): göz atma etiketi ve boş takvim ızgarası (numarasız) yumuşakça belirir — sol boş, sağda ızgara, asimetrik 50/50.
Scene 2 (2.0–3.2s): "otuz" sözünde kırmızı "30" büyükten oturarak damgalanır (−6°), "günü"nde "GÜN" yanına kayar.
Scene 3 (3.2–6.06s): soru satırı kelime kelime seslendirmeyle gelir (Peki… başlar?); sonra durur.

## Frame 2 — İdareye ulaştığı gün

- scene: Takvim ızgarası hücre hücre dolar (0–34. günler); "0" hücresi kırmızı daireyle işaretlenir, yanında "BAŞVURU İDAREYE ULAŞIR"; "gönderdiğin gün" yazısı üstü çizilerek düşer
- voiceover: "Başvuruyu gönderdiğin gün değil — idareye ULAŞTIĞI gün. Bu konunun tuzakları tarihlerde saklı; takvimi açalım."
- duration: 7.42s
- transition_in: crossfade
- status: animated
- src: compositions/frames/02-ulastigi-gun.html
- type: product_intro
- persuasion: Common-belief vs reality + Frame-then-fill
- beat: clarity
- blueprint: grid-card-assemble
- cite: GK md. 6/2

narrativeRole: Hook'un cevabını verir ve videonun tezini koyar: bu konu takvim üzerinden öğrenilir. Takvim sahnesi burada kurulur ve video boyunca sabit kalır.
keyMessage: Süre, başvurunun idareye ulaştığı gün başlar (0. gün).

- blueprint: grid-card-assemble (Adapt)
- focal: kırmızı eğik "ulaştığı gün."
- roles: takvim = foreground diagram (sağ) · "gönderdiğin gün" = supporting (çizilir) · 0. gün halkası = accent
- sfx: none

Adapt: ızgara hücreleri kademeli dolar (gün numaraları 0→34), sonra tek hücre vurgulanır.
Scene 1 (0.0–1.5s): gün numaraları 0'dan 34'e kademeli belirir; "gönderdiğin gün" solda gelir.
Scene 2 (1.5–3.3s): "değil"de kırmızı çizgi "gönderdiğin gün"ün üstünden geçer; "ULAŞTIĞI"da kırmızı "ulaştığı gün." eğik damgalanır.
Scene 3 (3.3–7.42s): "gün."de 0. günün halkası SVG ile çizilir, etiketi ve atıf gelir; "tuzakları"nda alt satır; sonra durur.

## Frame 3 — 0. gün: yazılı talep

- scene: Aynı takvim; 0. gün hücresi büyür, içinde iki etiket: "YAZILI" (sözlü talep çizilir) ve "BÜTÜN BİLGİ VE BELGELER → TALEP EDEN"
- voiceover: "Sıfırıncı gün: talep yazılı yapılır; sözlü talep öngörülmemiş. Gerekli bütün bilgi ve belgeleri ibraz etmek de talep edenin yükü."
- duration: 8.14s
- transition_in: crossfade
- status: animated
- src: compositions/frames/03-yazili-talep.html
- type: feature_showcase
- persuasion: Progressive disclosure
- beat: comprehension
- cite: GK md. 6/1, 6/2

narrativeRole: Sürenin başlayabilmesi için başvurunun şeklini ve kimin yükü olduğunu gösterir.
keyMessage: Talep yazılıdır; eksiksiz bilgi ve belge yükü talep edendedir.

- blueprint: compose
- focal: "Başvurunun şekli" kartı
- roles: kart = foreground subject (sol) · takvim (0. gün halkalı) = supporting (sağ, sabit)
- sfx: none

Scene 1 (0.0–1.1s): takvim aynen durur; "0. GÜN" etiketi ve 0. hücrenin kırmızı çerçevesi gelir.
Scene 2 (1.1–4.2s): "Talep yazılı yapılır." kelime kelime; "sözlü"de kartın kırmızı sol çubuğu çizilir ve ilk madde gelir, "öngörülmemiş"te "sözlü" çizilir.
Scene 3 (4.2–8.14s): "Gerekli"de ikinci madde; "talep edenin"de "talep eden ibraz eder" altı kırmızıyla çizilir; durur.

## Frame 4 — 30. gün: karar ve tebliğ

- scene: Aynı takvim; sayaç 1'den 30'a sayar, günler sırayla taranır, 30. gün kırmızı daire; "KARAR + YAZILI TEBLİĞ"; köşede "iş günü" yazısı üstü çizili
- voiceover: "İdare, otuz gün içinde karar alır ve kararı yazılı olarak tebliğ eder. Dikkat: otuz gün… iş günü değil."
- duration: 7.18s
- transition_in: crossfade
- status: animated
- src: compositions/frames/04-otuzuncu-gun.html
- type: feature_showcase
- persuasion: Demonstration (sayaç) + Counterexample
- beat: "aha"
- blueprint: dataviz-countup
- cite: GK md. 6/2

narrativeRole: Süreyi takvim üzerinde akıtarak somutlaştırır; "iş günü" tuzağını aynı anda kapatır.
keyMessage: Otuz gün içinde karar alınır ve yazılı tebliğ edilir; süre iş günü değildir.

- blueprint: dataviz-countup (Adapt)
- focal: sayaç "30"
- roles: sayaç = foreground subject (sol) · takvim günleri = diagram (sağ) · "iş günü" = supporting
- sfx: none

Adapt: sayaç ile hücre dolgusu kilitli ilerler; halka çizimi imza hareketi.
Scene 1 (0.0–0.6s): "SAYAÇ" etiketi ve "0".
Scene 2 (0.6–2.4s): "otuz gün içinde"de sayaç 0→30 sayar, 1–30. günler aynı ritimle dolar; "karar"da "gün içinde karar" başlığı.
Scene 3 (2.4–4.4s): 30. günün halkası çizilir; "tebliğ"de "KARAR + YAZILI TEBLİĞ" etiketi.
Scene 4 (4.4–7.18s): "Dikkat"te "takvim günü · iş günü" satırı, "iş günü"nde "iş günü" kırmızıyla çizilir; durur.

## Frame 5 — Süre aşımı ret değildir

- scene: Aynı takvim; 30'dan sonraki hücreler (31–34) taralı "EK SÜRE" bandına döner; 30. günden önceki bir hücreye bayrak dikilir: "GEREKÇE + EK SÜRE BİLDİRİLİR"; altta "SÜRE AŞIMI ≠ RET"
- voiceover: "Süreye uyulamıyorsa süre aşılabilir. Ama idare, süre dolmadan, gerekçeyi ve ek süreyi başvuru sahibine bildirir. Yani süre aşımı, ret demek değildir."
- duration: 9.42s
- transition_in: crossfade
- status: animated
- src: compositions/frames/05-sure-asimi.html
- type: feature_showcase
- persuasion: Signposting + Common-belief vs reality
- beat: unease → clarity
- cite: GK md. 6/2

narrativeRole: Sürenin aşılabildiği istisnayı ve bildirimin zamanını (süre dolmadan) takvime yerleştirir.
keyMessage: Süre aşılacaksa, süre dolmadan gerekçe ve ek süre bildirilir; bu bir ret değildir.

- blueprint: compose
- focal: taralı "EK SÜRE" bandı
- roles: takvim = diagram (sağ) · kart = supporting (sol) · "aşım ≠ ret" = foreground payoff
- sfx: none

Scene 1 (0.0–2.3s): "30 GÜNE UYULAMAZSA" etiketi; "süre aşılabilir"de başlık ve 31–34 hücreleri soldan sağa taranır, "EK SÜRE" etiketi.
Scene 2 (2.3–6.9s): "Ama"da kart; "dolmadan"da 26. hücrenin üstüne "SÜRE DOLMADAN BİLDİRİM" bayrağı iner; "gerekçeyi" ve "ek süreyi"de iki madde sırayla.
Scene 3 (6.9–9.42s): "ret"te kırmızı "aşım ≠ ret" eğik damgalanır; durur.

## Frame 6 — Gerekçe, derhal uygulama, itiraz

- scene: Takvim sayfası sola kayar; yeni sayfa "İTİRAZ" başlıklı ikinci bir 30 günlük takvim; üstte iki damga: "GEREKÇELİ (ret / aleyhe)" ve "DERHAL UYGULANIR"
- voiceover: "Ret ve aleyhe kararlar gerekçeli alınır, itiraz yolu kararda belirtilir. Kararlar derhal uygulanır. İtiraz da otuz gün içinde karara bağlanır."
- duration: 9.12s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/06-itiraz.html
- type: feature_showcase
- persuasion: Rule of three (gerekçe · derhal · itiraz)
- beat: momentum
- cite: GK md. 6/3, 6/4 · GY md. 586/1

narrativeRole: Karar sonrasını üç hızlı kuralla bağlar; itirazın da otuz günlük olduğunu ikinci takvimle gösterir.
keyMessage: Ret/aleyhe karar gerekçelidir, karar derhal uygulanır, itiraz da 30 günde karara bağlanır.

- blueprint: compose
- focal: "İTİRAZ · 30 GÜN" takvimi
- roles: üç kural = foreground list (sol) · iki damga = accent (üst) · itiraz takvimi = diagram (sağ)
- sfx: none

Scene 1 (0.0–4.5s): etiket ve boş itiraz takvimi; "Ret"te ilk kural, "gerekçeli"de "GEREKÇELİ" damgası basılır.
Scene 2 (4.5–6.4s): "Kararlar"da ikinci kural, "derhal"de "DERHAL UYGULANIR" damgası.
Scene 3 (6.4–9.12s): "İtiraz"da üçüncü kural; 0. gün halkası, "otuz gün içinde"de 1–30 dolgusu, "bağlanır"da 30. gün halkası ve "KARARA BAĞLANIR"; durur.

## Frame 7 — 7/1: üçü bir aradaysa iptal

- scene: Yeni takvim sayfası "LEHE KARAR"; üç şart kartı tek tek düşer ve bir kelepçe/çerçeveyle birleşir: "ÜÇÜ BİR ARADA"; sonra bir hücre kırmızı daire: "İPTAL KARARININ VERİLDİĞİ GÜN"
- voiceover: "Gelelim lehe kararların iptaline. Gümrük Kanunu yedinci madde, birinci fıkra: yanlış ya da eksik bilgi, başvuranın bunu bilmesi ya da bilmesi gerekmesi, doğru bilgiyle karar verilememesi. Üçü BİR ARADAYSA karar iptal edilir — ve iptal, VERİLDİĞİ gün yürürlüğe girer."
- duration: 16.7s
- transition_in: push-slide LEFT
- status: animated
- src: compositions/frames/07-yedi-bir.html
- type: feature_showcase
- persuasion: Numbered enumeration + Progressive disclosure
- beat: focus
- cite: GK md. 7/1, 7/4

narrativeRole: Sınavın odak noktasının ilk yarısı: üç şartın birlikteliği ve yürürlüğün verildiği gün olması.
keyMessage: 7/1'de üç hal bir aradaysa lehe karar iptal edilir; yürürlük iptal kararının verildiği gündür.

- blueprint: compose
- focal: "ÜÇÜ BİR ARADA" köşeli parantezi
- roles: üç şart kartı = foreground list (sol) · parantez = accent · yürürlük şeridi = diagram (sağ üst) · "verildiği gün" = payoff
- sfx: none

Scene 1 (0.0–4.8s): "lehe"de "LEHE KARAR · YÜRÜRLÜK" şeridi gelir; "Gümrük Kanunu yedinci madde"de "GK MD. 7/1" etiketi.
Scene 2 (4.8–11.6s): üç şart sırasıyla kendi sözlerinde gelir (yanlış · başvuranın · doğru bilgiyle).
Scene 3 (11.6–14.8s): "Üçü BİR ARADAYSA"da parantez çizilir ve etiketi gelir, başlık "Üçü bir aradaysa → iptal edilir" iki parçada.
Scene 4 (14.8–16.7s): "VERİLDİĞİ"de şeritte bir günün halkası çizilir, etiketi gelir; kırmızı "verildiği gün" eğik damgalanır; durur.

## Frame 8 — 7/2: tebliğ günü

- scene: Aynı takvim; iki koşul kartı ("koşul gerçekleşmez" / "yükümlülüğe uyulmaz"), "DEĞİŞTİRİLİR VEYA İPTAL EDİLEBİLİR"; daha ileri bir hücre ikinci kırmızı daire: "TEBLİĞ GÜNÜ"
- voiceover: "İkinci fıkra farklı: karara esas koşul gerçekleşmezse ya da yükümlülüğe uyulmazsa, karar değiştirilir veya iptal edilebilir. Yürürlük bu kez TEBLİĞ günüdür."
- duration: 10.28s
- transition_in: crossfade
- status: animated
- src: compositions/frames/08-yedi-iki.html
- type: feature_showcase
- persuasion: Comparison of two options
- beat: comprehension
- cite: GK md. 7/2, 7/4

narrativeRole: Aynı takvime ikinci yürürlük gününü ekleyerek iki fıkrayı yan yana görünür kılar.
keyMessage: 7/2'de lehe karar değiştirilir veya iptal edilebilir; yürürlük tebliğ günüdür.

- blueprint: compose
- focal: ikinci halka "TEBLİĞ GÜNÜ"
- roles: iki koşul kartı = foreground list (sol) · şerit = diagram (sağ üst) · "tebliğ günü" = payoff
- sfx: none

Scene 1 (0.0–1.4s): şerit 7. sahnedeki gibi durur; "farklı"da 7/1 halkası incelip mürekkep rengine döner, etiketi "7/1 · VERİLDİĞİ GÜN" olur; "GK MD. 7/2" etiketi.
Scene 2 (1.4–5.4s): "karara esas koşul"da birinci, "yükümlülüğe"de ikinci koşul.
Scene 3 (5.4–8.1s): "değiştirilir"de başlık "Değiştirilir veya iptal edilebilir" iki parçada.
Scene 4 (8.1–10.28s): "Yürürlük"te daha ileri bir günün kırmızı halkası çizilir; "TEBLİĞ"de etiket ve kırmızı "tebliğ günü" damgası; durur.

## Frame 9 — İki halka

- scene: Tam kırmızı panel; iki büyük beyaz halka yan yana: "7/1 → VERİLDİĞİ GÜN" ve "7/2 → TEBLİĞ GÜNÜ"; aralarında çift yönlü ok ve "SINAVDA YER DEĞİŞTİRİR"
- voiceover: "Takvimde iki halka: birinci fıkra, verildiği gün; ikinci fıkra, tebliğ günü. Sınavda yerlerini değiştirirler."
- duration: 7.5s
- transition_in: blur-crossfade
- status: animated
- src: compositions/frames/09-iki-halka.html
- type: branding
- persuasion: Distillation + Callback (takvim)
- beat: "now I get it"
- blueprint: comparison-split
- cite: GK md. 7/4

narrativeRole: Videoyu tek bir hatırlanacak görüntüye indirger: iki halka, iki fıkra.
keyMessage: 7/1 → verildiği gün, 7/2 → tebliğ günü; şıklarda yer değiştirilerek sorulur.

- blueprint: comparison-split (Adapt)
- focal: iki beyaz halka
- roles: halkalar = foreground pair · etiketler = supporting · çift yönlü ok = accent
- sfx: none

Adapt: kitap açılır eğimler yerine iki halka simetrik çizilir; ortadaki çift yönlü ok imza.
Scene 1 (0.0–1.5s): etiket; "iki halka"da sol ve sağ halka sırayla çizilir.
Scene 2 (1.5–5.4s): "birinci fıkra"da "7/1", "verildiği gün"de altındaki yazı; "ikinci fıkra"da "7/2", "tebliğ günü"nde altındaki yazı.
Scene 3 (5.4–7.5s): "Sınavda"da çift yönlü ok çizilir, "SINAVDA YER DEĞİŞTİRİR"; tutulan okuma.

## Frame 10 — Gümrük Koçu

- scene: Beyaz zemin; kullanıcının logosu (public/logo-ufuk-cetintas.png) sakin bir girişle ortaya oturur, altında @gumrukkocunuz; alt kenarda kırmızı ilerleme çubuğu tamamlanır
- voiceover: "Gümrük Koçu… Ufuk Çetintaş."
- duration: 4.34s
- transition_in: blur-crossfade
- status: animated
- src: compositions/frames/10-kapanis.html
- type: cta
- persuasion: Brand sign-off
- beat: resolve
- blueprint: titlecard-reveal
- asset_candidates: public/logo-ufuk-cetintas.png — kullanıcının UÇ / UFUK ÇETİNTAŞ / GÜMRÜK EĞİTİM KOÇU logosu, şeffaf zemin, renklerine dokunulmaz

narrativeRole: İmza; içeriğin kime ait olduğunu söyler.
keyMessage: Gümrük Koçu - Ufuk Çetintaş.

- blueprint: titlecard-reveal (Reproduce)
- focal: kullanıcı logosu
- roles: logo = foreground subject (orta) · @gumrukkocunuz = supporting
- sfx: none

Scene 1 (0.0–1.1s): logo tek ve sakin hareketle (aşağıdan yukarı + belirme) oturur.
Scene 2 (1.1–4.34s): "Ufuk"ta alt satırda @GUMRUKKOCUNUZ belirir; ilerleme çubuğu tamamlanır; tutulur.
