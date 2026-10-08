import glob, runpy, sys, re
S = sys.argv[1]
out = ['# Soru bankasında şimdiye kadar üretilen sorular (bölüm | madde | çekirdek)', '',
       'Bu çekirdekleri aynı yönden tekrar etme. Komşu bölümlerle ortak hükümlerde farklı fıkra ya da farklı ölçme yönü seç.', '']
for f in sorted(glob.glob(f'{S}/sb/batch/sb_[0-9][0-9].py')):
    no = re.search(r'sb_(\d\d)', f).group(1)
    for i, q in enumerate(runpy.run_path(f)['Q'], 1):
        out.append(f"SB{no}-{i:02d} | {q['madde']} | {q['cek']}")
open(f'{S}/sb/uretilen.md', 'w', encoding='utf-8').write('\n'.join(out) + '\n')
print(len(out) - 4, 'satır')
