# Son Doğrulama Talimatı (sağlamlaştırma geçişi sonrası, S4–S7)

Klasör: `araclar/gmy-deneme6-10`. Görev dosyan `gorev/S<n>.md`: doğrulayacağın sorular (sağlamlaştırma geçişinde kökü, şıkları ya da doğru cevabı değişen sorular) ve **düzenleyebileceğin batch dosyaları**. Başka dosyaya dokunma; `set*.json`, `plan.json`, `kontrol.py` değişmez. Git işlemi yapma.

Soruların güncel hâli batch dosyalarında ve `set6.json` … `set10.json` içinde (setler güncel; `opts` gösterim sırası, `harf` doğru cevap). Değişikliğin gerekçesi `dogrulama/G1–G5.md` ve `dogrulama/O1–O5.md` raporlarında; önceki hâli `git show 606cd84:araclar/gmy-deneme6-10/batch_<X>.py` ile görebilirsin. Değişikliğin yalnız şık merdiveni olduğu sorular (öncüllü sorularda çeldirici kombinasyonları `merdiven_dengele.py` ile değişti) için yalnız 1, 2 ve 3. maddeye bak.

Her soru için:
1–9. `DOGRULAYICI_TALIMAT.md`'deki dokuz kontrolün hepsi (doğru cevap kesin mi, çift doğru, açıklama uyumu, kaynak dışı bilgi, kök kuralları, kapsam, çıkmış soru kopyası, şık kalitesi, aynı hüküm). Kaynak `metin/`; Markdown derleme (`/home/user/gumrukdoktoru/2027gmynot/GUMRUK_MEVZUATI_TUMU.md`) aynı sürümdür.
10. **Deneme 1–5 örtüşmesi:** `python3 eski_ilgili.py batch_<X>.py` ile ilgili eski soruları bul. Yeni doğru cevap ya da cevabı belirleyen hüküm, eski bir soruda öğrencinin doğru diye okuduğu yerde (cevap, doğru öncül, olumsuz kökte doğru şık, kök bilgisi, doğru eşleştirme) geçiyorsa sorundur (`SAGLAMLASTIRMA_TALIMAT.md` §2-A).
11. **Cevap ipucu:** doğru şık, öteki şıklarda en sık geçen bileşenlerin tek birleşimi mi; kökün kelimelerini tek başına mı tekrar ediyor (§2-B)?
12. **Deneme içi sızıntı:** aynı denemedeki başka bir soru (kök, şık, öncül veya açıklama) bu sorunun cevabını veriyor mu? Ya da bu soru başka bir sorunun cevabını veriyor mu? (`grep` ile setN.json içinde ara.)

Bulduğun her sorunu **kendi batch dosyalarında düzelt**: plan kısıtları (tip, şık sınıfı, ters tuzak, kök bandı, harf) değişmez, `YAZAR_TALIMAT.md` §2–§6 geçerli, kilit değişirse `cek`, `madde`, `g`, `kanit` de güncellenir, `python3 kontrol.py batch_<X>.py` TEMİZ olmalı. Öncüllü soruda öncülleri değiştirirsen sonunda `python3 merdiven_dengele.py` çalıştırıp çıktıda kendi sorunun için öneri olup olmadığına bak (bu araç `--yaz` olmadan dosyaya yazmaz; önerisi varsa merdiveni elle uygula).

Rapor `dogrulama/S<n>.md`: önce sorunsuz soruları aralıkla say, sonra her sorun için `id` — tür (YANLIŞ CEVAP / ÇİFT DOĞRU / KAYNAK DIŞI / GÜNCEL DEĞİL / KOPYA / AYNI HÜKÜM / GEREKÇE UYUMSUZ / KÖK KURALI / KAPSAM DIŞI / ZAYIF ÇELDİRİCİ / BELİRSİZ / ÖRTÜŞME / İPUCU / SIZINTI) — kanıt (dosya + birebir alıntı) — yaptığın düzeltme. Her batch bitince dosyaya ekle.
