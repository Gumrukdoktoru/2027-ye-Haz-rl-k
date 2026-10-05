# sc.json → sorular/GK_Cikmis_vs_Sorulmayan_Analiz.md + sorular/GK_Sorulmayan_Konular_SoruCevap.md
import json, re, collections, pathlib
HERE = pathlib.Path(__file__).parent; OUT = HERE.parent.parent / 'sorular'
D = json.load(open(HERE / 'sc.json', encoding='utf-8'))
notlar = json.load(open(HERE / 'notlar.json', encoding='utf-8'))
YIL = ['2021', '2022', '2023', '2024', '2025']
TOP = sum(len(x['soru_cevap']) for x in D)
ALT = collections.Counter(); [ALT.update(x['st']) for x in D]
def ycount(x): return collections.Counter(r[:4] for r in x['refs'])
def bas(x): return x['konu']

# ---------------- Analiz ----------------
A = ['# Gümrük Koçu - Ufuk Çetintaş', '', '## 2021–2025 GMY Çıkmış Soruları: Sorulan ve Sorulmayan Konular Karşılaştırması', '',
     '| Alan | Değer |', '|---|---|',
     '| İncelenen sınavlar | 2021, 2022, 2023, 2024, 2025 GMY (her yıl 80 gümrük sorusu, toplam 400) |',
     f'| İncelenen kaynak | Depodaki {len(D)} mevzuat dosyası (Kanun, Yönetmelik, Karar, Tebliğ) |',
     f'| Alt konu (hüküm grubu) | {sum(ALT.values())} — sorulan {ALT["SORULDU"]}, kısmen sorulan {ALT["KISMEN"]}, hiç sorulmayan {ALT["SORULMADI"]} |',
     f'| Sorulmayan hükümlerden üretilen soru–cevap | {TOP} (ayrı dosya: GK_Sorulmayan_Konular_SoruCevap) |', '']
A += ['## 1. Yöntem', '']
A += [f'- {n}' for n in notlar['yontem']] + ['']
A += ['## 2. Konu bazında genel tablo', '',
      '| # | Konu | Kaynak dosya | ' + ' | '.join(YIL) + ' | Toplam | Alt konu | Sorulan | Kısmen | Sorulmayan | S–C |',
      '|---|---|---|' + '---|' * 5 + '---|---|---|---|---|---|']
for i, x in enumerate(D, 1):
    yc = ycount(x); st = x['st']
    A.append(f"| {i} | {bas(x)} | {x['kaynak'].replace('.txt','')[:60]} | " + ' | '.join(str(yc.get(y, 0)) for y in YIL)
             + f" | **{len(x['refs'])}** | {len(x['alt_konular'])} | {st.get('SORULDU',0)} | {st.get('KISMEN',0)} | {st.get('SORULMADI',0)} | {len(x['soru_cevap'])} |")
A += ['', '> Toplam sütunu, o kaynak dosyadaki hükümlere dayanan çıkmış soru sayısıdır. Bir soru birden fazla dosyanın hükmünü ölçüyorsa her iki dosyada da sayılmıştır; bu nedenle sütun toplamı 400 değildir. Kaynakta karşılığı bulunmayan 16 çıkmış soru (rejim kodları, Ek-9 limitleri, Form A vb.) tabloda yer almaz; liste 5. bölümdedir.', '']
sifir = [x for x in D if not x['refs']]
az = [x for x in D if 1 <= len(x['refs']) <= 3]
cok = sorted([x for x in D if len(x['refs']) >= 10], key=lambda x: -len(x['refs']))
A += ['## 3. Özet karşılaştırma', '', '### 3.1 Beş yılda hiç sorulmayan konular', '']
A += [f"- **{bas(x)}** ({x['mevzuat']}) — {len(x['alt_konular'])} alt konu, {len(x['soru_cevap'])} soru–cevap" for x in sifir] + ['']
A += ['### 3.2 Az sorulan konular (5 yılda 1–3 soru)', '']
A += [f"- **{bas(x)}** — {len(x['refs'])} soru ({', '.join(x['refs'])}); sorulmayan alt konu: {x['st'].get('SORULMADI',0)}" for x in az] + ['']
A += ['### 3.3 Çok sorulan konular (5 yılda 10+ soru) ve hâlâ sorulmamış hükümleri', '']
A += [f"- **{bas(x)}** — {len(x['refs'])} soru; buna rağmen {x['st'].get('SORULMADI',0)} alt konu hiç, {x['st'].get('KISMEN',0)} alt konu kısmen sorulmamış" for x in cok] + ['']
A += [f'- {n}' for n in notlar.get('gozlem', [])] + ['']
A += ['## 4. Konu konu karşılaştırma', '']
for i, x in enumerate(D, 1):
    A += [f"### 4.{i} {bas(x)}", '', f"*Kaynak: {x['kaynak'].replace('.txt','')} · Mevzuat: {x['mevzuat']}*", '',
          f"Beş yılda **{len(x['refs'])}** soru" + (f" ({', '.join(x['refs'])})" if x['refs'] else '') + '.', '']
    if x.get('cikmis'):
        A += ['**Sorulan bilgi noktaları**', ''] + [f'- {c}' for c in x['cikmis']] + ['']
    for durum, baslik in (('SORULDU', 'Sorulan alt konular'), ('KISMEN', 'Kısmen sorulan alt konular'), ('SORULMADI', 'Hiç sorulmayan alt konular')):
        al = [a for a in x['alt_konular'] if a['durum'] == durum]
        if not al: continue
        A += [f'**{baslik} ({len(al)})**', '']
        for a in al:
            ek = ''
            if a.get('cikmis'): ek += ' — ' + ', '.join(a['cikmis'])
            if durum == 'KISMEN' and a.get('not'): ek += f" — sorulmayan: {a['not']}"
            A.append(f"- {a['baslik']} ({a['dayanak']}){ek}")
        A.append('')
A += ['## 5. Kaynakta karşılığı bulunmayan çıkmış sorular', ''] + [f'- {n}' for n in notlar['yok']] + ['']
A += ['---', '**Gümrük Koçu - Ufuk Çetintaş**']
(OUT / 'GK_Cikmis_vs_Sorulmayan_Analiz.md').write_text('\n'.join(A) + '\n', encoding='utf-8')

# ---------------- Soru–Cevap ----------------
S = ['# Gümrük Koçu - Ufuk Çetintaş', '', '## Sorulmayan Konular — Soru–Cevap', '',
     '| Alan | Değer |', '|---|---|',
     '| Kapsam | 2021–2025 GMY sınavlarında hiç ya da kısmen sorulmamış hükümler |',
     f'| Soru–cevap sayısı | {TOP} |', f'| Konu sayısı | {sum(1 for x in D if x["soru_cevap"])} |',
     '| Kaynak | Yalnızca depodaki mevzuat metinleri; her cevabın sonunda dayanak madde |', '',
     '> Sorular açık uçludur; cevabı kapatıp kendinizi deneyin. Çıkmış sorularda ölçülen bilgi noktaları bu sette tekrar edilmemiştir; onlar için çıkmış soru envanterine ve deneme setlerine bakın.', '',
     '## İçindekiler', '']
for i, x in enumerate(D, 1):
    if x['soru_cevap']:
        S.append(f"{i}. {bas(x)} — {len(x['soru_cevap'])} soru (S{x['soru_cevap'][0]['no']}–S{x['soru_cevap'][-1]['no']})")
S.append('')
for i, x in enumerate(D, 1):
    if not x['soru_cevap']: continue
    S += [f"## {i}. {bas(x)}", '', f"*{x['mevzuat']} · Beş yılda {len(x['refs'])} soru · Bu bölümde {len(x['soru_cevap'])} soru–cevap*", '']
    son = None
    for q in x['soru_cevap']:
        if q['alt_konu'] != son:
            S += [f"### {q['alt_konu']}", '']; son = q['alt_konu']
        S += [f"**S{q['no']}.** {q['soru']}  ", f"**Cevap:** {q['cevap'].rstrip()} ({q['dayanak']})", '']
S += ['---', '**Gümrük Koçu - Ufuk Çetintaş**']
(OUT / 'GK_Sorulmayan_Konular_SoruCevap.md').write_text('\n'.join(S) + '\n', encoding='utf-8')

# ---------------- Hafıza satırları ----------------
def cek(t):
    w = t.split()
    return ' '.join(w[:25]) + ('…' if len(w) > 25 else '')
H = [f"{q['id']} | {bas(x)} | {q['dayanak']} | {cek(q['cevap'])} | SC | - | - | SC1" for x in D for q in x['soru_cevap']]
(HERE / 'hafiza_satirlari.txt').write_text('\n'.join(H) + '\n', encoding='utf-8')
print('md ok', TOP)
