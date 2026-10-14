# test1..3.json → sorular/GK_Karma_Test_<t>_50soru.md
import json, pathlib, collections
HERE = pathlib.Path(__file__).parent; OUT = HERE.parent.parent / 'sorular'
C = collections.Counter; L = 'ABCDE'
SIN = {'ÇOK': 'çok çıkan (5 yılda 10+ soru)', 'ORTA': 'orta çıkan (5–9)', 'AZ': 'az çıkan (1–4)', 'HİÇ': 'hiç çıkmayan'}
for t in (1, 2, 3):
    Q = json.load(open(HERE / f'test{t}.json', encoding='utf-8'))
    s = C(q['sinif'] for q in Q)
    md = ['# Gümrük Koçu - Ufuk Çetintaş', '', f'## GMY Karma Test {t} (50 soru)', '',
          '| Alan | Değer |', '|---|---|',
          f'| Set | Karma Test {t} (KT{t}) |',
          '| Kapsam | Gümrük mevzuatı; 2021–2025 GMY sınavlarında çok çıkan konular ağırlıklı |',
          f"| Konu dağılımı | Çok çıkan {s['ÇOK']} · orta çıkan {s['ORTA']} · az çıkan {s['AZ']} · hiç çıkmayan {s['HİÇ']} |",
          f"| İçerik | Çıkmış bilgi alanı {sum(q['tur'] == 'cikmis_alani' for q in Q)} · sorulmamış hüküm {sum(q['tur'] != 'cikmis_alani' for q in Q)} |",
          '| Süre önerisi | 75 dakika |', '',
          '> Sorular 2021–2025 GMY sınavlarının konu sıklığına göre kurgulandı: çok çıkan konulardan 32, orta çıkanlardan 12, az çıkanlardan 5, hiç çıkmayan bir konudan 1 soru. Çıkmış soruların bilgi alanları yeni kurguyla ölçüldü; kitapçık soruları kopyalanmadı. Tek bilgi kaynağı depodaki mevzuat metinleridir.', '',
          '# BÖLÜM A — SORU KİTAPÇIĞI', '']
    for q in Q:
        md.append(f"**{q['no']}-** " + q['kok'][0]); md.append('')
        for l in q['kok'][1:]: md.append(l + '  ')
        if len(q['kok']) > 1: md.append('')
        md += [f"{L[j]}) {o}  " for j, o in enumerate(q['opts'])]; md.append('')
    md += ['## Cevap Anahtarı', '']
    for a in range(0, 50, 25):
        part = Q[a:a + 25]
        md += ['| ' + ' | '.join(str(q['no']) for q in part) + ' |', '|' + '---|' * len(part), '| ' + ' | '.join(q['harf'] for q in part) + ' |', '']
    md += ['# BÖLÜM B — CEVAPLI VE GEREKÇELİ SORULAR', '']
    for q in Q:
        md += [f"*{q['madde']}*", '', f"**{q['no']}-** " + q['kok'][0], '']
        for l in q['kok'][1:]: md.append(l + '  ')
        if len(q['kok']) > 1: md.append('')
        md += [f"{L[j]}) {o}  " for j, o in enumerate(q['opts'])]
        ek = f" · Çıkmış: {q['cikmis']}" if q.get('cikmis') else ''
        md += ['', f"**Doğru Cevap:** {q['harf']}  ", f"**Gerekçe:** {q['gerekce']}", '', f"<sub>{q['konu']} · {SIN[q['sinif']]} · {q['alt_tip']}{ek}</sub>", '']
    md += ['## Dağılım', '']
    def tab(baslik, cnt, sira):
        return [f'**{baslik}**', '', '| ' + ' | '.join(sira) + ' |', '|' + '---|' * len(sira), '| ' + ' | '.join(str(cnt.get(o, 0)) for o in sira) + ' |', '']
    md += tab('Doğru cevap harfi', C(q['harf'] for q in Q), list(L))
    md += tab('Konu sınıfı', C(q['sinif'] for q in Q), ['ÇOK', 'ORTA', 'AZ', 'HİÇ'])
    at = C(q['alt_tip'] for q in Q); md += tab('Alt tip (soru tipi kataloğu kodu)', at, [k for k, _ in at.most_common()])
    md += tab('Zorluk', C(q['z'] for q in Q), ['ÇK', 'K', 'O', 'Z', 'ÇZ'])
    kon = C(q['konu'] for q in Q)
    md += ['**Konu**', '', '| Konu | Sınıf | Soru |', '|---|---|---|'] + [f"| {k} | {next(q['sinif'] for q in Q if q['konu'] == k)} | {v} |" for k, v in kon.most_common()] + ['']
    md += ['## HAFIZA GÜNCELLEMESİ', '', '```'] + [f"{q['id']} | {q['konu']} | {q['madde']} | {q['cek']} | {q['kalip']} | {q['z']} | {q['harf']} | KT{t}" for q in Q] + ['```', '', '---', '**Gümrük Koçu - Ufuk Çetintaş**']
    (OUT / f'GK_Karma_Test_{t}_50soru.md').write_text('\n'.join(md) + '\n', encoding='utf-8')
print('md ok')
