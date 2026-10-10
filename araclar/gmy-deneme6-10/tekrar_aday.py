"""Aynı madde/fıkraya dayanan soru çiftlerini listeler (tekrar denetimi için aday).
Çıktı: dogrulama/aday_yeni_yeni.txt (Deneme 6-10 kendi arasında), dogrulama/aday_yeni_hafiza.txt (önceki 515 hafıza satırıyla)."""
import glob, re, itertools
A = {}
for f in sorted(glob.glob('batch_*.py')):
    ns = {}; exec(open(f).read(), ns)
    for q in ns['Q']: q['b'] = f[6:-3]; A[q['id']] = q
def norm(m):
    for a, b in (('4458 sayılı Gümrük Kanunu', 'GK'), ('Gümrük Kanunu', 'GK'), ('Gümrük Yönetmeliği', 'GY'), ('5607 sayılı Kaçakçılıkla Mücadele Kanunu', '5607'), ('5607 sayılı Kanun', '5607')):
        m = m.replace(a, b)
    return m
def refs_full(m):  # yeni-yeni: her mevzuat adı + madde/fıkra
    out = set()
    for seg in norm(m).split(';'):
        seg = seg.strip(); law = re.match(r'^(.*?)(?:\s+m\.|\s+\d)', seg)
        name = (law.group(1) if law else seg)[:40].strip()
        for x in re.findall(r'(\d+(?:/[\w\-]+)+)', seg): out.add((name, x))
    return out
def refs_gkgy(m):  # hafıza: yalnız GK/GY/5607 madde/fıkra
    out = set()
    for seg in norm(m).split(';'):
        seg = seg.strip(); mm = re.match(r'^(GK|GY|5607)\b', seg)
        if not mm: continue
        for x in re.findall(r'(\d+(?:/[\w\-]+)?)', seg[len(mm.group(1)):]):
            if '/' in x: out.add((mm.group(1), x.split('/')[0] + '/' + x.split('/')[1].split('-')[0]))
    return out
R = {i: refs_full(q['madde']) for i, q in A.items()}
L = []
for a, b in itertools.combinations(A, 2):
    s = R[a] & R[b]
    if s: L.append(f"{a}({A[a]['b']}) ~ {b}({A[b]['b']}): {sorted(s)}\n   A: {A[a]['cek'][:170]}\n   B: {A[b]['cek'][:170]}")
open('dogrulama/aday_yeni_yeni.txt', 'w').write(f'{len(L)} çift ortak madde/fıkra\n' + '\n'.join(L) + '\n')
H = []
for l in open('../../sorular/hafiza/URETIM-HAFIZASI.md'):
    p = [x.strip() for x in l.split('|')]
    if len(p) >= 8 and re.match(r'(KAR|GMY)', p[0]) and not re.match(r'GMY(6|7|8|9|10)-', p[0]): H.append((p[0], p[2], p[3]))
L2 = []
for i, q in A.items():
    r = refs_gkgy(q['madde'])
    for hid, hm, hc in H:
        s = r & refs_gkgy(hm)
        if s: L2.append(f"{i}({q['b']}) ~ HAFIZA {hid}: {sorted(s)}\n   Y: {q['cek'][:170]}\n   H: {hc[:170]}")
open('dogrulama/aday_yeni_hafiza.txt', 'w').write(f'{len(L2)} çift\n' + '\n'.join(L2) + '\n')
print(len(L), len(L2))
