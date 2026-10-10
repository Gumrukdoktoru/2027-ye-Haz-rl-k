"""Doğrulama başlangıcından (bb2ef37) bu yana kökü, şıkları veya doğru cevabı değişen soruları listeler."""
import subprocess, glob, json, sys
ref = sys.argv[1] if len(sys.argv) > 1 else 'bb2ef37'
def yukle(src):
    ns = {}; exec(src, ns); return {q['id']: q for q in ns['Q']}
deg = []
for f in sorted(glob.glob('batch_*.py')):
    try: eski = yukle(subprocess.run(['git', 'show', f'{ref}:araclar/gmy-deneme6-10/{f}'], capture_output=True, text=True, check=True).stdout)
    except subprocess.CalledProcessError: eski = {}
    yeni = yukle(open(f).read())
    for i, q in yeni.items():
        e = eski.get(i)
        if not e or any(e.get(k) != q.get(k) for k in ('kok', 'd', 'c', 'opts')): deg.append((i, f[6:-3]))
deg.sort(key=lambda x: (int(x[0].split('-')[0][1:]), x[0]))
json.dump(deg, open('dogrulama/degisen.json', 'w'))
print(len(deg)); from collections import Counter; print(Counter(b for _, b in deg))
