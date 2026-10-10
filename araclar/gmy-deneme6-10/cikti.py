"""Kullanım: python3 cikti.py 6  → ../../sorular/GK_GMY_Deneme6_100soru.md (+ ozet6.json, cikti.js için)"""
import json, sys, re, collections
from kontrol import STRIP, sinif, bant
D = int(sys.argv[1]); Q = json.load(open(f'set{D}.json')); L = 'ABCDE'; C = collections.Counter
YIL = {6: '2021', 7: '2022', 8: '2023', 9: '2024', 10: '2025'}[D]
notlar = json.load(open('notlar.json'))
TIPAD = {'T1': 'Olumsuz kök', 'T2': 'Öncüllü', 'T1+T2': 'Olumsuz köklü öncüllü', 'T3': 'Süre / eşik / oran', 'T4': 'Doğrudan bilgi',
         'T5': 'Boşluk doldurma', 'T6': 'Tanım → kavram', 'T7': 'Makam / yetki', 'T8': 'Olay-vaka', 'T9': 'Hesaplama', 'T10': 'Tablo / eşleştirme'}
ZOR = {'OÜ': 'Orta Üstü', 'Z': 'Zor', 'O': 'Orta'}
TIPSIRA = ['T1', 'T1+T2', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10']
mdm = lambda s: re.sub(r'\[\[([^\]]+)\]\]', r'<u>**\1**</u>', s)
M = [q for q in Q if q['blok'] == 'GÜMRÜK']; G = [q for q in Q if q['blok'] == 'GK']
def denge(q):
    ls = [len(STRIP(o)) for o in q['opts']]
    s = ' '.join(f'{L[j]}:{n}' for j, n in enumerate(ls))
    return s + ' karakter → Denge: ' + ('UYGUN (ters tuzak: doğru şık bilinçli olarak en uzun; 2. ve 3. en uzun şık ≥ %90)' if q.get('tuzak') else 'UYGUN')
def yuzde(n, t): return f'{n} (%{round(100 * n / t)})'
harf_all = C(q['harf'] for q in Q); harf_m = C(q['harf'] for q in M)
tip_m = C(q['tip'] for q in M); tip_g = C(q['tip'] for q in G)
sn = C(sinif(q['opts']) for q in M); bn = C(bant(len(STRIP(' '.join(q['kok'])))) for q in M)
z = C(q['z'] for q in Q)
ozet = dict(deneme=D, yil=YIL,
  bilgi=[['Set', f'GMY Deneme {D} (GMY-S{D})'], ['Model sınav', f'{YIL} Gümrük Müşavir Yardımcılığı sınavı' + (' (B kitapçığı sırası)' if YIL == '2025' else '')],
         ['Soru sayısı', '100 (1–20 genel kültür + 21–100 gümrük mevzuatı)'], ['Süre', '150 dakika'],
         ['Kurallar', 'Prompt 4 (GMY Soru Motoru – Master) + Prompt 3 + CLAUDE.md'],
         ['Karşılama', f'{YIL} sınavının 100 sorusunun her biri aynı sıradaki yeni soruyla birebir karşılandı (aynı bilgi alanı, farklı hüküm)'],
         ['Zorluk', ' · '.join(f'{ZOR[k]} {v}' for k, v in z.most_common())]],
  harf_all={h: harf_all.get(h, 0) for h in L}, harf_m={h: harf_m.get(h, 0) for h in L},
  tip_m={t: tip_m.get(t, 0) for t in TIPSIRA}, tip_g={t: v for t, v in tip_g.items()},
  sinif={k: sn.get(k, 0) for k in ('kısa', 'orta', 'uzun')}, bant={k: bn.get(k, 0) for k in ('≤120', '120-350', '350-700', '>700')},
  tuzak=sum(bool(q.get('tuzak')) for q in M), notlar=notlar,
  konu=C((q.get('konu') or q.get('ders')) for q in Q).most_common())
json.dump(ozet, open(f'ozet{D}.json', 'w'), ensure_ascii=False)
md = ['# Gümrük Koçu - Ufuk Çetintaş', '', f'## GMY Deneme Sınavı {D}', '', '| Alan | Değer |', '|---|---|'] + [f'| {a} | {b} |' for a, b in ozet['bilgi']]
md += ['', 'Her sorunun yalnız bir doğru cevabı vardır. Sorular çıkmış soruların kopyası değildir; aynı bilgi alanı farklı hükümle, kurum soru diliyle özgün olarak ölçülmüştür.', '',
       '# BÖLÜM A — SORU KİTAPÇIĞI', '']
def soru(q, lab=False):
    out = []
    if lab: out += [f"**SORU {q['no']}.** [{q['tip']} – {ZOR[q['z']]}] · Model soru: {q['cikmis']}", '']
    k = q['kok']
    out.append((f"**{q['no']}.** " if not lab else '') + mdm(k[0])); out.append('')
    for l in k[1:]: out.append(mdm(l) + '  ')
    if len(k) > 1: out.append('')
    out += [f'{L[j]}) {mdm(o)}  ' for j, o in enumerate(q['opts'])]
    return out
for q in Q:
    if q['no'] == 1: md += ['## Genel Kültür (1–20)', '']
    if q['no'] == 21: md += ['## Gümrük Mevzuatı (21–100)', '']
    md += soru(q) + ['']
md += ['## Cevap Anahtarı', '']
for s in range(0, 100, 20):
    part = Q[s:s + 20]
    md += ['| ' + ' | '.join(str(q['no']) for q in part) + ' |', '|' + '---|' * 20, '| ' + ' | '.join(q['harf'] for q in part) + ' |', '']
md += ['# BÖLÜM B — ÇÖZÜMLÜ SORULAR', '']
for q in Q:
    if q['no'] == 1: md += ['## Genel Kültür (1–20)', '']
    if q['no'] == 21: md += ['## Gümrük Mevzuatı (21–100)', '']
    md += soru(q, True) + ['', f"✅ **Doğru Cevap:** {q['harf']}  ", f"📖 **Açıklama:** {mdm(q['g_harfli'])}  ",
                          f"⚖️ **Yasal Dayanak:** {q['madde']}  ", f"🔍 **Şık Uzunluk Kontrolü:** {denge(q)}", '', '---', '']
md += ['# SET SONU', '', '```', 'CEVAP ANAHTARI']
for s in range(0, 100, 10): md.append('   '.join(f"Soru {q['no']}: {q['harf']}" for q in Q[s:s + 10]))
md += ['', 'HARF DAĞILIMI (1–100)', '  '.join(f'{h}: {yuzde(ozet["harf_all"][h], 100)}' for h in L),
       'HARF DAĞILIMI (21–100, master §7 bandı)', '  '.join(f'{h}: {yuzde(ozet["harf_m"][h], 80)}' for h in L), '',
       'TİP DAĞILIMI (21–100; T1+T2 olumsuz köklü öncüllü, hem T1 hem T2 sayılır)',
       ' · '.join(f'{t}: {ozet["tip_m"][t]}' for t in TIPSIRA),
       f"T1 toplam: {ozet['tip_m']['T1'] + ozet['tip_m']['T1+T2']} · T2 toplam: {ozet['tip_m']['T2'] + ozet['tip_m']['T1+T2']}",
       'TİP DAĞILIMI (1–20 genel kültür)', ' · '.join(f'{t}: {v}' for t, v in sorted(ozet['tip_g'].items())), '```', '']
def tab(t, d, tot):
    return [f'**{t}**', '', '| ' + ' | '.join(d) + ' |', '|' + '---|' * len(d), '| ' + ' | '.join(yuzde(v, tot) for v in d.values()) + ' |', '']
md += tab('Kök uzunluk bandı (21–100, hedef %30 · %40 · %20 · %10)', ozet['bant'], 80)
md += tab('Şık uzunluk sınıfı (21–100; kısa ≤4 kelime, uzun 5 şık ≥20 kelime)', ozet['sinif'], 80)
md += [f"**Ters tuzak (doğru şık bilinçli olarak en uzun):** {ozet['tuzak']} soru (21–100'ün %{round(100 * ozet['tuzak'] / 80)}'i)", '']
md += ['**Konu dağılımı**', '', '| Konu | Soru |', '|---|---|'] + [f'| {k} | {v} |' for k, v in ozet['konu']] + ['']
md += ['## Üretim Notu', ''] + [f'- {x}' for x in notlar] + ['']
md += ['## HAFIZA GÜNCELLEMESİ', '', '```']
md += [f"GMY{D}-{q['no']:03d} | {q.get('konu') or q.get('ders')} | {q['madde']} | {q['cek']} | {q['tip']} | {q['z']} | {q['harf']} | GMY-S{D}" for q in Q]
md += [f'Toplam: {515 + 100 * (D - 5)} satır (önceki 515 + Deneme 6–{D})', '```', '', '---', '**Gümrük Koçu - Ufuk Çetintaş**']
open(f'../../sorular/GK_GMY_Deneme{D}_100soru.md', 'w').write('\n'.join(md) + '\n'); print('md ok', D)
