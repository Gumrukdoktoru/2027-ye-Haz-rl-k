"""Bölümler arası çekirdek çakışması: çekirdek + doğru şık kelime kümesi Jaccard benzerliği."""
import glob, runpy, sys, re, itertools
S = sys.argv[1]; esik = float(sys.argv[2]) if len(sys.argv) > 2 else 0.45
DUR = set('ve veya ile bir bu için olan olarak ise de da ki göre her ancak hâlinde halinde gibi daha en kadar içinde sonra önce tarafından'.split())
def kel(s):
    s = s.replace('İ', 'i').replace('I', 'ı').lower()
    return {w for w in re.findall(r'[a-zçğıöşü0-9]+', s) if len(w) > 2 and w not in DUR}
Q = []
for f in sorted(glob.glob(f'{S}/sb/batch/sb_[0-9][0-9].py')):
    no = re.search(r'sb_(\d\d)', f).group(1)
    for i, q in enumerate(runpy.run_path(f)['Q'], 1):
        Q.append((f'SB{no}-{i:02d}', no, kel(q['cek'] + ' ' + q['d']), q['cek']))
n = 0
for a, b in itertools.combinations(Q, 2):
    if a[1] == b[1]: continue
    j = len(a[2] & b[2]) / max(1, len(a[2] | b[2]))
    if j >= esik:
        n += 1; print(f'{j:.2f} {a[0]} ↔ {b[0]}\n   {a[3]}\n   {b[3]}')
print(n, 'olası çakışma')
