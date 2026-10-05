# Görev: Soru–cevap çiftlerinin bağımsız doğrulaması (GMY sınav hazırlığı, Türkçe)

Sana verilen girdi dosyasında (`<calisma>/dogrula/in/<V>.json`) gümrük mevzuatından üretilmiş açık uçlu soru–cevap çiftleri var. Her öğe: key, kaynak (kaynak metin dosyası adı), alt_konu, soru, cevap, dayanak, kanit (kaynaktan birebir kesit), bazen sayi_uyari.
Kaynak metinler: `<calisma>/src/metin/<kaynak>`.

## Her öğe için yap
1. Kaynak dosyada ilgili hükmü bul (kanıt kesitini ve anahtar kelimeleri grep ile ara) ve hükmün TAMAMINI (ilgili fıkra/bent ve istisnaları) oku.
2. Denetle:
   - Cevap kaynaktaki yürürlükteki hükümle birebir uyumlu mu? Sayı, süre (iş günü/takvim günü), oran, tutar, makam (gümrük müdürlüğü / bölge müdürlüğü / Bakanlık / Genel Müdürlük vb.), belge adı, şart ve istisnalar doğru mu?
   - Cevap eksik ya da yanıltıcı mı (ör. hükümdeki önemli bir istisna/ikinci şart atlanmış ve bu yüzden cevap yanlış anlaşılıyor)?
   - Kaynakta olmayan bilgi eklenmiş mi?
   - Soru tek ve tartışmasız cevaplı mı; cevap gerçekten sorulana mı cevap veriyor?
   - Hüküm mülga / dipnottaki eski metin / yürürlükten kaldırılmış bir düzenleme mi? (Kaynakta "değişik. Mülga" gibi başlık ibareleri çoğunlukla eski metne bağlantıdır; madde metni yürürlüktedir. Gerçekten yürürlükten kalkmış hükümden soru olmamalı.)
   - Soruda madde/fıkra/bent numarası var mı (olmamalı)? 2009/15481 sayılı Karara dayanan soru "4458 sayılı ..." ile başlıyorsa düzelt: `2009/15481 sayılı "4458 sayılı Gümrük Kanununun Bazı Maddelerinin Uygulanması Hakkında Karar"a göre ...`
   - dayanak alanı hükmün gerçek maddesini gösteriyor mu?
   - sayi_uyari varsa o sayıyı kaynakta özellikle doğrula.
3. Karar ver:
   - **OK**: doğru ve yeterli.
   - **DUZELT**: düzeltilmiş soru/cevap/dayanak/kanit ver. Yeni kanit kaynaktan BİREBİR kopyalanmış olmalı (her parça ≥25 karakter, parçalar " ... " ile ayrılır). Düzeltmeyi gerekçelendir. Küçük üslup tercihleri için DUZELT verme; yalnız içerik/doğruluk/açıklık sorunu varsa.
   - **SIL**: kaynakta doğrulanamıyor, yürürlükte değil, kaynak kendi içinde çelişkili ya da soru tartışmalı ve düzeltilemiyorsa.
4. Kanıtlarını python3 ile kaynakta (boşlukları normalize ederek) arayıp doğrula.

## Çıktı
python3 ile `json.dump(..., ensure_ascii=False, indent=1)` kullanarak `<calisma>/dogrula/out/<V>.json` dosyasına yaz:
```json
{"chunk": "V01", "toplam": 190, "ok": 175,
 "duzelt": [{"key": "G01|0|5", "soru": "...", "cevap": "...", "dayanak": "...", "kanit": "...", "gerekce": "..."}],
 "sil": [{"key": "G01|1|12", "gerekce": "..."}]}
```
DUZELT öğesinde dört alanın (soru, cevap, dayanak, kanit) hepsini yaz (değişmeyenleri de aynen). Her öğe ya ok sayısına ya duzelt'e ya sil'e girer; toplam tutmalı. Repo dosyalarına dokunma. Son mesajında yalnız kısa özet ver (ok/duzelt/sil sayıları ve en önemli 3–5 düzeltmenin bir cümlelik açıklaması).
