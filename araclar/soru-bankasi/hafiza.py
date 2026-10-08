"""Soru bankası sorularını üretim hafızasına ekler (her bölüm ayrı set: SB-K01 … SB-K56).

Kullanım: python3 hafiza.py KITAP.json URETIM-HAFIZASI.md [--yenile]
Aynı ID zaten varsa satır yeniden eklenmez; --yenile verilirse önce bütün SB-K satırları silinip kitaptan yeniden yazılır.
Toplam satırı yeniden hesaplanır.
"""
import json
import re
import sys

kitap, yol = sys.argv[1:3]
s = open(yol, encoding='utf-8').read()
bas, son = s.index('```\n') + 4, s.rindex('\n```')
satirlar = s[bas:son].split('\n')
if '--yenile' in sys.argv:
    satirlar = [x for x in satirlar if not x.rstrip().endswith(tuple(f'SB-K{i:02d}' for i in range(1, 100)))]
var = {x.split(' | ')[0] for x in satirlar}
yeni = []
for b in json.load(open(kitap, encoding='utf-8')):
    for q in b['sorular']:
        if q['id'] in var:
            continue
        cek = q['cek'].replace('|', '/').replace('\n', ' ')
        yeni.append(f"{q['id']} | {q['konu']} | {q['madde']} | {cek} | {q['kalip']} | {q['z']} | {q['harf']} | SB-K{b['no']:02d}")
satirlar += yeni
veri = [x for x in satirlar[1:] if x.strip()]
say = {'Karar': 0, 'GMY deneme S1': 0, 'GMY deneme S2': 0, 'GMY deneme S3': 0, 'Soru bankası': 0}
for x in veri:
    k = x.split(' | ')[-1]
    say['Karar' if k == 'S1' and x.startswith('KAR') else
        {'GMY-S1': 'GMY deneme S1', 'GMY-S2': 'GMY deneme S2', 'GMY-S3': 'GMY deneme S3'}.get(k, 'Soru bankası')] += 1
toplam = f"Toplam: {len(veri)} satır (" + ' · '.join(f'{k}: {v}' for k, v in say.items() if v) + ')'
kuyruk = re.sub(r'Toplam: \d+ satır \([^)]*\)', toplam, s[son:])
open(yol, 'w', encoding='utf-8').write(s[:bas] + '\n'.join(satirlar) + kuyruk)
print(f'{len(yeni)} satır eklendi. {toplam}')
