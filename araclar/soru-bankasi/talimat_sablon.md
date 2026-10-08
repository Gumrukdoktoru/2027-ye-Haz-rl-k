# GÖREV: Soru bankası bölümü — "{BASLIK}" konusundan 20 özgün GMY mevzuat sorusu

Gümrük Koçu - Ufuk Çetintaş için kaynak klasördeki her konudan 20'şer soruluk bir **soru bankası kitabı** hazırlanıyor. Sen **Bölüm {NO}: {BASLIK}** için 20 soru yazacaksın.

## Önce oku (zorunlu)

1. **Prompt:** `/home/user/2027-ye-Haz-rl-k/promptlar/prompt-5-gmy-mevzuat-sorusu-hazirlama.md`. Tamamını oku ve eksiksiz uygula. Soru sayısı kullanıcı tarafından **20** olarak verildi; promptun bölüm 3'teki "sayı verildiğinde" öncelik sırasını uygula.
2. **Depo kuralları:** `/home/user/2027-ye-Haz-rl-k/CLAUDE.md`.
   - **Karar kökü kuralı:** 2009/15481 sayılı Karara dayanan soruda kök şu kalıbı **aynen** içerir: `2009/15481 sayılı "4458 sayılı Gümrük Kanununun Bazı Maddelerinin Uygulanması Hakkında Karar"a göre …`
   - Diğer kökler dayanağın türünü (Kanun/Yönetmelik/Tebliğ/Karar) açıkça gösterir.
3. **Üretim hafızası:** `/home/user/2027-ye-Haz-rl-k/sorular/hafiza/URETIM-HAFIZASI.md`. Konunu grep'le. Önceki setlerin çekirdeğini (aynı hüküm, aynı yön) tekrar etme; aynı hükmü soracaksan farklı yönden ölç.
4. **Çıkmış soru envanteri:** `/home/user/2027-ye-Haz-rl-k/araclar/gmy-deneme2/cikmis_envanter.tsv`. Sütunlar: YIL, SORU_NO, KONU, ÖLÇÜLEN_BİLGİ, KAYNAK_DOSYA, resmî CEVAP. Bu konunun kaynak dosyasına (KAYNAK_DOSYA sütunu) ve konu adına göre grep'le.
   - Bu konunun çıkmış sorularındaki bilgi alanlarının **hepsi** setinde ölçülür.
   - Çıkmış soru metni, şık yapısı ve kurgu kopyalanmaz; aynı bilgi farklı biçimde sorulur.
5. **Yazarın sonraki hamleleri:** `/home/user/gmy-ikmislar/analiz/SONRAKI-HAMLELER.md`. Konunla ilgili satırları grep'le; sorulmamış komşu fıkralar öncelikli hedefin.
6. **Örnek veri:** `/home/user/2027-ye-Haz-rl-k/araclar/gmy-deneme3/batch_A.py`. Biçim, dil ve gerekçe üslubu için örnek.

## Tek bilgi kaynağı

- Bu bölümün kaynağı: `{METIN}/{DOSYA}`.
- Bu dosyayı **baştan sona** oku ve önce sınav değeri taşıyan bilgi alanlarını çıkar (prompt bölüm 2).
- Konu dosyası küçükse, aynı konuyu doğrudan düzenleyen hükümler `{METIN}/` klasöründeki başka dosyalarda da varsa kullanılabilir. Örnek: Kanun maddesinin Yönetmelikteki karşılığı. Ama başka bir konunun bölümüne ait hükümlere kayma.
- Web araştırması yok; kaynakta olmayan bilgiyle soru yok.
- Her soru en az bir birebir alıntıyla kanıtlanır.
- Tarife pozisyonu veya GTİP sınıflandırma sorusu yazılmaz. Usul hükümleri sorulabilir.

## 20 soruluk set profili (prompt bölüm 13'ün 20 soruya ölçeklenmiş hâli)

**Metne yakınlık:**
- Kilit cümle madde metninden birebir: 13–14 soru.
- Gerçek parafraz: **3–4 soru**. Doğru şık ya da kilit cümle, anlamı birebir korunarak kurum diliyle yeniden ifade edilir.
- Tek adımlı çıkarım: en fazla 3 soru.

**Biçim (2021–2025 sınav dağılımına göre; kullanıcı tercihi, Prompt 5 kotasının önüne geçer):**
- Olumsuz kök (önermeli dışı): 7–8 soru.
- Önermeli: 2 soru, en az 3 önerme. En kapsamlı şıkla ya da "yanlıştır" köküyle cevaplanan en fazla 1 olur.
- Vaka, uygulama ya da hesap: 1 soru (kıymet, ceza, tahakkuk ve teminat konularında en fazla 2). Vakaya tek bir istisna saklanır.
- Tanımdan ad / addan tanım: 2 soru (konu tanım içeriyorsa).
- Boşluk doldurma ve eşleştirme toplam en fazla 1 soru; boşluk tercih edilir.
- Kalan sorular klasik: "hangisidir / hangisinde doğru olarak verilmiştir / kaç gündür".
- Gerekçe şıklara içerikle atıf yapar, harf ya da sıra bildirmez; doğru cevabı "çeldirici" diye anmaz.

**Sayısal ve süre soruları:**
- Sayısal şıklar `sirali=True` ile küçükten büyüğe dizilir; doğru değer 2., 3. ya da 4. sıradadır.
- Süre sorularının en az üçte birinde başlangıç anı ölçülür.

**Zorunlu kapsam:**
- Metinde ikiz kavram ekseni varsa (prompt bölüm 8) en az biri ölçülür, uygunsa ayna çiftle.
- Beş aday profilinin her biri en az bir soruyla yakalanır. Profil 5 yalnızca kaynakta güncellik varsa aranır.
- Kaynakta son 12 ayda (Ekim 2025 – Ekim 2026) değişen hüküm varsa en az 1 güncellik sorusu kurulur; değişiklik tarihi dipnot satırlarından okunur.
- Meslek konularında ya da konu elveriyorsa 1 meslek yanlılığı sorusu kurulur.
- Uydurma çeldirici en aza indirilir. Her çeldiricinin metindeki gerçek yuvası `yuva` alanına yazılır.

**Küçük konu kuralı:** Kaynak 20 farklı sınav noktası taşımıyorsa aynı hükmün **gerçekten farklı ölçme boyutlarını** kullan:
- tanımdan ada ve addan tanıma,
- olandan olmayana,
- ayna soru,
- vaka.

Aynı bilgiyi aynı yönden iki kez sorma. Yine de 20'ye ulaşamazsan en az 16 soru yaz ve nedenini raporda belirt.

## Veri biçimi (deneme 3 ile aynı)

Çıktı dosyan `{CIKTI}`; içinde `Q = [ dict(...), ... ]` ve 20 soru olur. Alanlar:

```python
dict(
konu="{BASLIK}", blok="SB{NO}",
kalip="KAPSAM_DIŞI",   # TANIM KAVRAM KAPSAM KAPSAM_DIŞI DOĞRU YANLIŞ ÖNERMELİ SÜRE ORAN-TUTAR YETKİ BELGE ŞART HESAP BOŞLUK EŞLEŞTİRME MÜEYYİDE OLAY TABİ ZORUNLULUK MATRAH DAYANAK SONUÇ MUAFİYET KISA_AD
z="O",                 # ÇK K O Z ÇZ
madde="Gümrük Yönetmeliği md. 55",   # sorunun üstündeki madde satırı (kökte ve şıkta madde/fıkra/bent numarası YASAK)
cek="≤25 kelimelik çekirdek bilgi",
kok=["… aşağıdakilerden hangisi … ?"],   # önermelide öncüller ayrı satır: "I. …"; vakada veri satırları "- …"
d="doğru şık", c=["çeldirici 1","çeldirici 2","çeldirici 3","çeldirici 4"],
sirali=False,          # True ise siklar=[5 şık nihai sırasıyla] (sayısal şıklar ZORUNLU, önermeli doğal sıra isteğe bağlı)
g="Gerekçe … En güçlü çeldiricinin metindeki yeri bir cümle. Bu nedenle doğru cevap '<d ile birebir aynı>' seçeneğidir. (MD 55)",
kanit="dosya.txt | kaynaktan BİREBİR alıntı",   # birden çok alıntı " || " ile
yuva=["çeldirici 1'in metindeki gerçek yeri", "…", "…", "…"],
yakinlik="BİREBİR",    # BİREBİR PARAFRAZ ÇIKARIM (dürüst etiketle: vaka/hesap = ÇIKARIM)
tuzak=["KOMŞU"], duzey=["AYIRT"], profil=[2],
olumsuz=False, vaka=False, baslangic=False, eksen=0, ayna="", guncellik="", cikmis="2024/28", kapsamli=False,
),
```

Biçim kuralları:
- **Harf yok.** Cevap harflerini ben dağıtacağım; gerekçe "Bu nedenle doğru cevap '<d metni>' seçeneğidir. (MD …)" ile biter.
- **Gerekçe içeriği:**
  - Öğrenci maddeyi okumadan anlayacak açıklıkta olur.
  - Şıklara harfle değil içerikle atıf yapar.
  - Güncellik sorusunda değişiklik tarihini yazar.
- **Kanıt alıntısı:** Kaynaktan karakter karakter kopyalanır. Gerekirse "…" ile parçalanır; her parça en az 13 karakter olur.

## Kontrol (zorunlu)

Şu komutla kendi dosyanı denetle:

```
python3 -I /home/user/2027-ye-Haz-rl-k/araclar/gmy-deneme3/kontrol5.py {METIN} {CIKTI}
```

- "Hatalı soru: 0" olana kadar düzelt.
- Ardından prompt bölüm 16'daki 30 maddelik kontrolü her soruya uygula.
- Özellikle şu noktalara bak:
  - tek ve tartışmasız doğru cevap,
  - hiçbir çeldiricinin metne göre de doğru olmaması,
  - kökteki mevzuat türünün kaynakla aynı olması,
  - önermelide her önermenin doğru/yanlış niteliğinin metinle teyit edilmesi.

## Rapor dosyası

`{RAPOR}` dosyasına JSON yaz:

```json
{"bulunamayan": ["2024/41: … (metinde yok)"], "giremeyen": "tek cümle: sete giremeyen önemli soru alanları", "notlar": ["kısa notlar: kota sapması, küçük konu durumu vb."]}
```

## Dönüş mesajın

En fazla 8 satır olsun:
- soru sayısı,
- kontrol sonucu,
- yakınlık / olumsuz / önermeli / vaka sayıları,
- karşılanamayan kota ve nedeni.

Depo dosyalarına dokunma; yalnız `{CIKTI}` ve `{RAPOR}` dosyalarını yaz.
