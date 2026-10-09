# istatistik.json + etiketler_tam.json + kartlar/*.md + bulgular.md → sorular/GK_GMY_Soru_Tipi_Katalogu.md
import json, re, math, pathlib, collections
HERE = pathlib.Path(__file__).parent; OUT = HERE.parent.parent / 'sorular' / 'GK_GMY_Soru_Tipi_Katalogu.md'
st = json.load(open(HERE / 'istatistik.json', encoding='utf-8'))
E = json.load(open(HERE / 'etiketler_tam.json', encoding='utf-8'))
C = collections.Counter
YIL = ['2021', '2022', '2023', '2024', '2025']
ANA = ['O', 'D', 'Ö', 'G', 'V', 'K', 'B', 'E', 'S', 'H', 'T', 'M']
GM_PAY = {'O': 36, 'D': 21, 'Ö': 13, 'H': 12, 'G': 7, 'V': 3, 'E': 3, 'K': 2, 'B': 2, 'S': 1}   # kullanıcının GM kataloğu (1.1)
GRUP = {'GK': ('TÜRKÇE', 'MATEMATİK', 'TARİH', 'HUKUK'), 'TEMEL': ('TEMEL',), 'ALT': ('ALT',), 'KAÇ': ('KAÇAKÇILIK',), 'HESAP': ('HESAP',)}
pct = lambda a, b: f'%{round(100 * a / b)}' if b else '–'
A = []
add = A.extend

add(['# 12 — SORU TİPİ KATALOĞU (GMY)', '', '## Gümrük Müşavir Yardımcılığı Sınavı 2021–2025: 500 sorunun alt tip haritası', '',
     '**Bu dosyada ne var?** 2021–2025 GMY sınavlarındaki 500 sorunun her biri tek tek etiketlendi: bir ana tip (12 tip), bir alt tip ve dokuz biçim bayrağı. '
     'Bu dosya o etiketlerin sayımını, her alt tip için gerçek sınavdan aynen alınmış örneği ve o tipte soru üretme tarifini verir. '
     'Etiket sistemi, Gümrük Müşavirliği sınavı için hazırlanmış "12 — Soru Tipi Kataloğu"ndan GMY\'ye uyarlandı.', '',
     '**Kimin işine yarar?**', '',
     '- Soru üreten (insan ya da yapay zekâ): Prompt 1 ve Prompt 3 ile set üretirken alt tip hedefleri bu dosyadaki kodlara dayanır (bkz. Bölüm 5–6).',
     '- Ders notu hazırlayan: Bir konunun hangi tiple sorulduğunu bilir, tuzak notunu o tipe göre yazar.',
     '- Öğrenci: Soruyu görünce tipini tanır, o tipin adayı nerede yakaladığını bilir.', '',
     '**Okuma kuralları**', '',
     '- Tipi, kökün son yüklemi ve şıkların biçimi belirler. Kök "yanlıştır" dese bile şıklar bir listenin kısa öğeleriyse soru O1\'dir, O2 değildir. Sınır durumlar Bölüm 4\'te.',
     '- "5 yıl" = 2021–2025 toplamı (500 soru). "24–25" = 2024 ve 2025 toplamı (200 soru); son eğilimi gösterir.',
     '- Alanlar: genel kültür (1–20) TÜRKÇE · MATEMATİK · TARİH · HUKUK (her biri 25); gümrük (21–100) TEMEL (GK, GY, 2009/15481 Karar) 311 · ALT (tebliğ, genelge, diğer yönetmelik/karar) 58 · KAÇAKÇILIK (5607 ve yönetmelikleri) 26 · HESAP 5.',
     '- Cevap anahtarı: 2021–2024 kitapçıklarında doğru şık kırmızıyla işaretli (resmî anahtar, 400 soru). 2025 kitapçığı cevapsızdır; 2025 cevapları mevzuattan türetildi (100 soru: 86 yüksek, 11 orta, 3 düşük güven). Harf istatistikleri yalnız resmî anahtarla, doğru şık uzunluk konumu 2025 dahil 500 soru üzerinden hesaplandı.',
     '- Örnekler kitapçıktan aynen alındı; yalnız satır sonları birleştirildi. Doğru şık ✔ ile işaretlendi.', ''])
add(['### Kod sözlüğü (özet)', '', '| Ana tip | Alt tipler |', '|---|---|',
     '| O Olumsuz kök | O1 Liste dışı eleman · O2 Bozuk cümle · O3 Çift olumsuz / ters kurgu · O4 Tarife olumsuz |',
     '| D Düz (tek bilgi) | D1 Tek değer · D2 Ad/kimlik · D3 Liste içi eleman · D4 Farklı olanı bul · D5 Yer tespiti · D6 Tek cevaplı usul/sonuç |',
     '| Ö Öncüllü | Ö1 Hangileri doğrudur · Ö2 Hangileri yanlıştır · Ö3 Liste öncüllü · Ö4 Koşul öncüllü · Ö5 Vaka öncüllü |',
     '| G "Hangisi doğrudur" | G1 Beş cümleden doğru · G2 Normatif güç merdiveni · G3 Ters kurgu · G4 Örnek seçme |',
     '| V Vaka (hesapsız) | V1 Tarihli vaka · V2 Olaylı vaka · V3 Emsal seçme · V4 Tarife tanım vakası |',
     '| K Kavram | K1 Tanım → kavram |', '| B Boşluk | B1 İki boşluk · B2 Üç-dört boşluk |',
     '| E Eşleştirme | E1 Beş çiftten yanlış/doğru olan · E2 Tablo eşleştirme · E3 Doğru sıralama (permütasyon) |',
     '| S Sıralama | S1 Süreç/öncelik sırası · S2 Numara/büyüklük sırası |',
     '| H Hesap | H1 Kalem listeli kıymet · H2 Bağlı soru · H3 Vergi tutarı · H4 Ceza/uzlaşma · H5 Kıymet yöntemi · H6 Özel kıymet durumu · H7 Hesapsız hesap · H8 Diğer sayısal |',
     '| T Türkçe (GMY eki) | T1 Sözcük ve cümle anlamı · T2 Dil bilgisi · T3 Yazım ve noktalama · T4 Anlatım bozukluğu · T5 Paragraf |',
     '| M Matematik (GMY eki) | M1 Sayı ve işlem · M2 Problem · M3 Geometri ve ölçü · M4 Örüntü ve mantık |', '',
     '| Bayrak | Anlamı |', '|---|---|',
     '| F_MATRIS | Şıklar iki ya da üç boyutun çapraz kombinasyonu |', '| F_MUTLAK | Doğru cevapta ya da kilit çeldiricide mutlak ifade (sadece, yalnızca, her türlü, hiçbir) |',
     '| F_TUZAKVERI | Kökte, çözümde kullanılmaması gereken veri |', '| F_TUMU | Doğru cevap tüm öncüller |', '| F_YALNIZ | Doğru cevap "Yalnız X" |',
     '| F_DAYANAK | Kökte mevzuatın adı açıkça geçiyor (gümrük) |', '| F_MADDENO | Kökte ya da şıkta madde/fıkra/bent numarası geçiyor |',
     '| F_SERI | Önceki ya da sonraki soru aynı konuda (seri blok) |', '| F_GUNCEL | O yıl ya da bir önceki yıl yürürlüğe giren ya da yıllık güncellenen düzenleme/tutar |', ''])

# 1. BÜYÜK RESİM
add(['## 1. BÜYÜK RESİM', '', '### 1.1 Ana tip × yıl', '', '| Ana tip | ' + ' | '.join(YIL) + ' | 5 yıl | Pay | GM kataloğunda pay |', '|---|' + '---|' * 8])
for a in sorted(ANA, key=lambda a: -st['ana'][a]['n']):
    v = st['ana'][a]
    if not v['n'] and a not in GM_PAY: continue
    add([f"| {a} {v['ad']} | " + ' | '.join(map(str, v['yil'])) + f" | {v['n']} | {pct(v['n'], 500)} | {('%' + str(GM_PAY[a])) if a in GM_PAY else '–'} |"])
add(['', '> T ve M yalnız GMY\'de vardır (genel kültür, her yıl 5 + 5). Gümrüğün 400 sorusunda: O 140 (%35) · D 129 (%32) · K 44 (%11) · Ö 39 (%10) · G 27 (%7) · B 11 · H 5 · E 3 · V 2.', ''])
add(['### 1.2 Alt tip × yıl × alan (500 sorunun tamamı)', '', '| Alt tip | ' + ' | '.join(YIL) + ' | 5 yıl | GK | TEMEL | ALT | KAÇ | HESAP | 24–25 |', '|---|' + '---|' * 12])
for a, v in st['alt'].items():
    g = {k: sum(v['alan'].get(x, 0) for x in xs) for k, xs in GRUP.items()}
    add([f"| {a} | " + ' | '.join(map(str, v['yil'])) + f" | {v['n']} | {g['GK']} | {g['TEMEL']} | {g['ALT']} | {g['KAÇ']} | {g['HESAP']} | {v['son2']} |"])
gorulmeyen = [a for a in 'O4 D4 D5 G2 V1 V3 V4 S1 S2 H1 H2 H3 H5'.split() if a not in st['alt']]
add(['', f"> GMY'de hiç görülmeyen alt tipler: {', '.join(gorulmeyen)}. Tarife sınıflandırma (O4, D5, V4) ve kalem listeli hesap (H1–H3) GM'ye özgü kalıyor.", ''])
add(['### 1.3 Her alanın tip imzası (alan içindeki pay; 5 yıl / 24–25)', '', '| Alan | İlk beş alt tip | Bu beşin alan içindeki payı |', '|---|---|---|'])
for al, v in st['alan'].items():
    add([f"| {al} ({v['n']}) | " + ' · '.join(f"{a} %{p5}/{p2}" for a, n, p5, p2 in v['ilk5']) + f" | %{v['ilk5_pay']} |"])
add(['', '**Okuma:** Gümrük TEMEL\'in dili "listede olmayanı bul" (O1) ile "çıplak değer" (D1); bozuk cümle (O2) üçüncü. ALT mevzuatta O1 ve D1\'in yanında tanım → kavram (K1) ve ad (D2) öne çıkıyor. Tarih sorularının yarısı ad/kimlik (D2); hukukta D2, O1 ve liste içi eleman (D3). Türkçede anlam (T1), matematikte geometri-ölçü (M3) en sık.', ''])
add(['### 1.4 Bayraklar × yıl', '', '| Bayrak | ' + ' | '.join(YIL) + ' | 5 yıl | 100 soruda ort. |', '|---|' + '---|' * 7])
for b, v in sorted(st['bayrak'].items(), key=lambda x: -x[1]['n']):
    add([f"| {b} | " + ' | '.join(map(str, v['yil'])) + f" | {v['n']} | {round(v['n'] / 5)} (24–25: {round(v['son2'] / 2)}) |"])
add(['', '> F_DAYANAK yalnız gümrük sorularında sayıldı (400 soru içinde). F_DAYANAK ve F_MADDENO kök/şık metninden kuralla, F_SERI komşu sorunun konusundan kuralla hesaplandı.', ''])
b = st['bicim']
fmt = lambda d: ' · '.join(f'{k} {v}' for k, v in d.items())
uzt = lambda d: (lambda n: f"orta %{round(100 * d.get('orta', 0) / n)} · en uzun %{round(100 * d.get('en_uzun', 0) / n)} · en kısa %{round(100 * d.get('en_kisa', 0) / n)} (n={n})")(sum(d.values()) or 1)
oc = b['oncul_cevap']; ocn = sum(oc.values())
add(['### 1.5 Biçimsel ölçümler (cevap anahtarının "parmak izi")', '', '| Ölçü | Bulgu | Soru üretiminde karşılığı |', '|---|---|---|',
     f"| Doğru harf (resmî anahtar, 2021–2024, 400 soru) | {fmt(b['harf_resmi'])} | A az (%15,5). Deneme setinde harf dağılımı N/5 ± 2; A'yı bilinçli olarak eksik bırakma |",
     f"| Doğru harf yıl yıl | " + ' / '.join(f"{y}: {fmt(v)}" for y, v in b['harf_resmi_yil'].items()) + " | Yıllar arası oynaklık büyük; tek yılın dağılımını hedef alma |",
     f"| Art arda aynı doğru harf (99 komşu çift) | " + ' · '.join(f"{y}: {n}" for y, n in b['ardisik_ayni_harf_resmi'].items()) + " | Gerçek sınavda olağan; Prompt 3 bunu yasaklıyor (bkz. Bölüm 6) |",
     f"| Doğru şık uzunluğu, cümle/eşleşme şıklı sorular | {uzt(b['uzunluk_tum'])} | Doğru şıkkı çoğunlukla orta uzunlukta yaz |",
     f"| Olumsuz kökte bozuk şık (O2, O3) | {uzt(b['uzunluk_O2O3'])} | Bozuk şık en kısa olma eğiliminde (%28); her seferinde kısa yazma |",
     f"| Olumlu kökte doğru şık (G1–G4) | {uzt(b['uzunluk_G'])} | En uzun şıkkı doğru yapma eğilimi hafif |",
     f"| Öncüllü cevap (Ö + E2, n={ocn}) | ara kombinasyon {oc.get('ara', 0)} (%{round(100 * oc.get('ara', 0) / ocn)}) · Yalnız X {oc.get('yalniz', 0)} (%{round(100 * oc.get('yalniz', 0) / ocn)}) · tüm öncüller {oc.get('tumu', 0)} (%{round(100 * oc.get('tumu', 0) / ocn)}) | Bu oranlara yakın dağıt |",
     f"| Liste öncüllüde \"hepsi\" (Ö3) | {b['O3_tumu'][0]}/{b['O3_tumu'][1]} soru (%{round(100 * b['O3_tumu'][0] / b['O3_tumu'][1])}); resmî Ö3'te doğru harf E 10/14 | Ö3'te \"tümü\" cevabını kullan, ama E'ye sabitleme |",
     f"| Öncül sayısı (Ö, n={sum(b['oncul_sayisi'].values())}) | " + ' · '.join(f"{k} öncül {v}" for k, v in b['oncul_sayisi'].items()) + " | Varsayılan 4 öncül; 3 öncül de sık (Prompt 3: en az 3) |",
     f"| Tek değer (D1, resmî) | {fmt(st['alt']['D1']['harf_resmi'])} | Sıralı sayı şıklarında doğru değeri B–D arasına yığma |",
     f"| O1 doğru harf (resmî) | {fmt(st['alt']['O1']['harf_resmi'])} | Yabancı öğeyi sona koyma alışkanlığı belirgin; denemede yay |",
     f"| Matematik doğru harf (resmî) | {fmt(b['mat_harf_resmi'])} | – |",
     f"| Mutlak ifade (F_MUTLAK, n={st['bayrak']['F_MUTLAK']['n']}) | O2 7, G1 6, Ö1/Ö2 4, O1 2 | \"Mutlak = yanlış\" sezgisini kıran soru da yaz |",
     f"| Madde numarası (F_MADDENO, n={st['bayrak']['F_MADDENO']['n']}) | 2021: 3 → 2024: 13 → 2025: 11; çoğu kökte dayanak gösterimi | Prompt 3 gereği kökte madde numarası kullanma; mevzuat adı + hükmün konusu yaz |",
     f"| Güncellik (F_GUNCEL, n={st['bayrak']['F_GUNCEL']['n']}) | 241/1 tutarı (2022, 2024, 2025), asgari ücret tarifesi, posta-kargo eşiği | Yıllık güncellenen tutarı soruyorsan yılı yaz |", ''])

# 2. BULGULAR
add(['## 2. KATALOGDAN ÇIKAN 12 BULGU', ''] + (HERE / 'bulgular.md').read_text(encoding='utf-8').strip().splitlines() + [''])

# 3. KARTLAR
add(['## 3. ALT TİP KARTLARI', '', 'Her kartta aynı başlıklar: Sayı · Tanım · Kök kalıpları · Gerçek örnek · Doğru cevap nasıl kuruluyor · Çeldiriciler · Biçim verisi · Üretim tarifi · Kaçın. Az kullanılan alt tiplerin kartları kısadır.', ''])
sinir = []
for k in ('K1', 'K2', 'K3', 'K4'):
    t = (HERE / 'kartlar' / f'{k}.md').read_text(encoding='utf-8')
    if '<!-- SINIR -->' in t:
        t, s = t.split('<!-- SINIR -->', 1)
        sinir += [l for l in s.splitlines() if l.startswith('|') and not re.match(r'^\|\s*-', l) and 'Tereddüt' not in l]
    t = re.sub(r'^# [^\n]*\n', '', t.strip())          # dosya başlığı varsa at
    t = re.sub(r'^## ', '### ', t, flags=re.M) if not re.search(r'^### ', t, re.M) else t
    add([t.strip(), ''])

# 4. SINIR DURUMLAR
add(['## 4. SINIR DURUMLAR: HANGİ TİP HANGİSİ?', '', 'Karar ölçütü her zaman kökün son yüklemi + şıkların biçimidir.', '',
     '| Tereddüt | Karar ölçütü | Örnek |', '|---|---|---|'])
tip = (HERE / 'TIPOLOJI.md').read_text(encoding='utf-8').split('## 5. Sınır durumlar', 1)[1]
for l in tip.splitlines():
    if l.startswith('|') and 'Tereddüt' not in l and not l.startswith('|---'):
        add([l.rstrip('|').rstrip() + ' | – |'])
add(sinir + [''])

# 5. DENEME REÇETESİ
def dagit(pay, toplam):
    ham = {k: toplam * v for k, v in pay.items()}; tam = {k: math.floor(x) for k, x in ham.items()}
    for k in sorted(ham, key=lambda k: -(ham[k] - tam[k]))[:toplam - sum(tam.values())]: tam[k] += 1
    return {k: v for k, v in tam.items() if v}
def agirlikli(xs):
    c5, c2 = C(e['alt_tip'] for e in xs), C(e['alt_tip'] for e in xs if e['yil'] >= 2024)
    n5, n2 = len(xs), max(1, sum(c2.values()))
    return {a: 0.4 * c5[a] / n5 + 0.6 * c2.get(a, 0) / n2 for a in c5}
g = [e for e in E if e['alan'] == 'GÜMRÜK']
alan_pay = {al: 0.4 * sum(1 for e in g if e['alt_alan'] == al) / len(g) + 0.6 * sum(1 for e in g if e['alt_alan'] == al and e['yil'] >= 2024) / sum(1 for e in g if e['yil'] >= 2024)
            for al in ('TEMEL', 'ALT', 'KAÇAKÇILIK', 'HESAP')}
alan_n = dagit(alan_pay, 80)
add(['## 5. DENEME SINAVI ALT TİP REÇETESİ (100 soru)', '',
     'Hedefler 5 yıllık pay (%40 ağırlık) ile 2024–25 payının (%60 ağırlık) birleşimidir; en büyük kalan yöntemiyle tam sayıya yuvarlandı. Genel kültür her yıl sabit (5 Türkçe, 5 matematik, 5 tarih, 5 hukuk).', '',
     '### 5.1 Alan × alt tip', '', '| Alan (soru) | Alt tip hedefi |', '|---|---|'])
for al, n in [('TÜRKÇE', 5), ('MATEMATİK', 5), ('TARİH', 5), ('HUKUK', 5)] + list(alan_n.items()):
    xs = [e for e in E if e['alt_alan'] == al]
    hedef = dagit(agirlikli(xs), n)
    add([f"| {al} ({n}) | " + ' · '.join(f"{a} {v}" for a, v in sorted(hedef.items(), key=lambda x: -x[1])) + ' |'])
gh = dagit(agirlikli(g), 80)
anah = C()
for a, v in gh.items(): anah[a[0]] += v
add(['', f"**Gümrük 80 soru, ana tip toplamı (yaklaşık):** " + ' · '.join(f'{a} {v}' for a, v in anah.most_common()) + '.', ''])
add(['### 5.2 Bayrak hedefleri (100 soruluk deneme)', '', '| Bayrak | Hedef | Not |', '|---|---|---|'])
notlar = {'F_DAYANAK': 'Gümrük kökünde mevzuatın adı ("Gümrük Yönetmeliğine göre …"); Prompt 3 zaten bunu istiyor',
          'F_SERI': '2–6 soruluk konu blokları; blok içinde alt tip değişsin', 'F_MADDENO': 'Prompt 3 gereği hedef 0; numara ezber sorusu yok',
          'F_MATRIS': 'D6, D1, B1 ve G1\'in bir kısmı', 'F_MUTLAK': 'Bir kısmı doğru ifadede olsun', 'F_TUMU': 'Öncüllülerin ~%25\'i; çoğu Ö3',
          'F_YALNIZ': 'Öncüllülerin ~%20\'si', 'F_GUNCEL': 'Yılı yazılmış güncel tutar (241/1, eşikler)', 'F_TUZAKVERI': 'Yalnız hesap sorularında'}
for bb, v in sorted(st['bayrak'].items(), key=lambda x: -x[1]['n']):
    h = round(0.4 * v['n'] / 5 + 0.6 * v['son2'] / 2)
    if bb == 'F_MADDENO': h = 0
    add([f"| {bb} | ~{h} | {notlar.get(bb, '')} |"])
add(['', '### 5.3 Dağıtım kuralları', '',
     '- Aynı alt tip üst üste en fazla 3 kez. Seri blok içinde alt tip değişsin: önce kural (O2/G1), sonra öncüllü (Ö1/Ö3), sonra değer (D1) ya da kavram (K1).',
     '- Öncüllülerde cevap: ~%50 ara kombinasyon, ~%22 "Yalnız X", ~%28 tüm öncüller; "tüm öncüller"i her seferinde E\'ye koyma.',
     '- O1\'de yabancı öğeyi A–E arasında yay (gerçek sınavda D/E\'ye yığılıyor; deneme bunu kopyalamasın, ama A\'yı da dışlamasın).',
     '- O2\'lerde hiçbir bozma tekniği %40\'ı geçmesin; polarite dışında süre/sayı, etiket ve makam kaydırma da kullanılsın.',
     '- Cümle şıklı sorularda doğru şık ~%55 orta uzunlukta; bozuk şıkkı her seferinde en kısa yazma.', ''])

# 6. PROMPTLAR
add(['## 6. PROMPTLARDA KULLANIM', '',
     'Prompt 1 (set isteği) ve Prompt 3 (nihai soru kuralları) ile set istenirken bir **ALT TİP** satırı eklenebilir:', '',
     '```', 'ALT TİP: OTOMATİK          → Bölüm 5 reçetesi', 'ALT TİP: O1×3, D1×2, Ö3×2   → Yalnız bu alt tiplerden, bu sayılarda',
     'ALT TİP: KARMA-24-25        → 2024–25 paylarına göre (son eğilim)', '```', '',
     'Her üretilen sorunun altındaki madde satırına alt tip kodu da yazılabilir; örneğin: `GK md. 79 — O2 (polarite tersi)`.', '',
     '**Prompt 3 ile uyum notları:**', '',
     '- Prompt 3\'ün kalıp ailesi (A–AB) bu katalogla örtüşüyor: tanım ↔ K1, kapsam dışı ↔ O1, doğru/yanlış hüküm ↔ G1/O2, önermeli ↔ Ö1–Ö3, süre/oran ↔ D1, yetkili makam ↔ D2, boşluk ↔ B1/B2, eşleştirme ↔ E1.',
     '- Prompt 3 "art arda aynı cevap harfi yok" diyor; gerçek GMY\'de art arda aynı harf yılda 12–19 kez var. Kural kullanıcı tercihi olarak korunur; yalnız bilinçli bir fark olduğu bilinsin.',
     '- Prompt 3 kökte madde numarasını yasaklıyor; gerçek sınavda 38 soruda dayanak gösterimi olarak geçiyor. Prompt 3 kuralı geçerlidir.',
     '- Öncüllü sorularda Prompt 3\'ün "en az 3 önerme" kuralı gerçek veriyle uyumlu (3 öncül 15, 4 öncül 17, 5 öncül 7).', ''])

# 7. YÖNTEM
tar = b['tartismali']; ef = b['envanter_fark']
add(['## 7. YÖNTEM NOTU', '',
     '- Kitapçıklar PDF\'teki koordinatlı metinden (pdftohtml -xml) soru, öncül ve şık olarak ayrıştırıldı (`araclar/soru-tipi/ayristir.py`). 2021–2024 kitapçıklarında kırmızı yazılmış şık resmî doğru cevap olarak okundu; 400 sorunun her birinde tek kırmızı şık bulundu.',
     '- 2025 kitapçığı cevapsız (B kitapçığı). 2025 cevapları gümrükte mevzuat metninden, genel kültürde çözülerek türetildi: 86 yüksek, 11 orta, 3 düşük güven. Düşük güvenliler: 2025/34 (kullanılmış taşıt kıymet kuralı kaynakta yok), 2025/68 (rejim kodu listesi kaynakta yok), 2025/86.',
     '- 500 sorunun her biri `TIPOLOJI.md` sözlüğüyle tek tek etiketlendi (yıl başına bir etiketleyici). Her soru için alan, konu, dayanak, ana/alt tip, bayraklar, kökün son yüklemi, şık türü, öncül sayısı, doğru harf, teknik kodu ve "doğru cevap nasıl kurulmuş" notu kaydedildi (`araclar/soru-tipi/tipler.csv`).',
     '- F_DAYANAK, F_MADDENO ve F_SERI etiketleyiciler arası tutarlılık için metinden kuralla yeniden hesaplandı. O2 bozma tekniği ve O1 yabancı öğe kaynağı dağılımları kurulum notlarından sınıflandırmadır; sayılar yaklaşık kabul edilmelidir.',
     '- Alt tip kartları etiketlenmiş verinin üzerine yazıldı; kartlardaki sayılar `istatistik.json`dan alındı.', '',
     '**Resmî anahtar ile önceki çıkmış soru envanteri karşılaştırması.** `araclar/gmy-deneme2/cikmis_envanter.tsv` CEVAP sütunu (mevzuattan türetilmişti) 2021–2024\'ün 320 gümrük sorusunun 313\'ünde resmî anahtarla aynı. Farklı olan 7 soru (envanter → resmî): ' +
     '; '.join(f"{y}/{n}: {a} → {r}" for y, n, a, r in ef) + '. Bu soruların envanterdeki "ölçülen bilgi" notları da gözden geçirilmeli (ör. 2024/47 çıkış değil ihracat gümrük idaresi; 2024/85 iştirak hâlinde ceza her birine ayrı uygulanır). Tam liste: `araclar/soru-tipi/cevap_anahtari.tsv`.', '',
     '**Anahtarı tartışmalı ya da yoruma açık sorular** (örnek olarak kullanılmadı):', ''] +
    [f"- {y}/{n}: {t}" for y, n, t in tar] + [
     '- 2021/95: resmî cevap sınav tarihine göre doğru; 18.01.2024 değişikliğiyle Hazine ve Maliye Bakanlığı çıkarıldığından güncel metne göre cevap değişir.',
     '- 2021/86: resmî cevap sınav tarihindeki asgari ücret tarifesi indirim oranına göre; kaynaktaki güncel oran farklı.',
     '- 2025/61, 2025/76: önceki envanter notları mevzuat metniyle çelişiyor (GY 155/1 ek süre üç ay; Karar 63/3 nakliye kıymete eklenir).', '',
     '---', '**Gümrük Koçu - Ufuk Çetintaş**'])
OUT.write_text('\n'.join(A) + '\n', encoding='utf-8')
print('md ok', OUT, len('\n'.join(A)))
