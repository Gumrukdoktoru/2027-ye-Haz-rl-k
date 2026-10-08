"""Sayılardan sonra gelen eklerde ünlü/ünsüz uyumu taraması (2026'de → 2026'da gibi)."""
import glob, re, runpy, sys
S = sys.argv[1]
BIR = ['', 'bir', 'iki', 'üç', 'dört', 'beş', 'altı', 'yedi', 'sekiz', 'dokuz']
ON = ['', 'on', 'yirmi', 'otuz', 'kırk', 'elli', 'altmış', 'yetmiş', 'seksen', 'doksan']
def son_kelime(n):
    if n == 0: return 'sıfır'
    if n % 10: return BIR[n % 10]
    if n % 100: return ON[(n // 10) % 10]
    if n % 1000: return 'yüz'
    if n % 1000000: return 'bin'
    if n % 1000000000: return 'milyon'
    return 'milyar'
KALIN = set('aıou'); INCE = set('eiöü'); SERT = set('çfhkpsşt')
def beklenen(kelime, ek):
    v = [c for c in kelime if c in KALIN | INCE][-1]
    kalin = v in KALIN; yuv = v in 'ouöü'
    sert = kelime[-1] in SERT; unlu = kelime[-1] in KALIN | INCE
    e = ek
    hata = []
    # ilk ünsüz d/t
    if e[0] in 'dt':
        if (e[0] == 't') != sert: hata.append('d/t')
        rest = e[1:]
    elif e[0] in 'ny' or e[0] in 'eaıiuü':
        rest = e
    else:
        return []
    m = re.search(r'[aeıioöuü]', rest)
    if not m: return hata
    ch = m.group(0)
    if ch in 'ae':
        if (ch == 'a') != kalin: hata.append('ünlü')
    elif ch in 'ıiuü':
        doğru = ('u' if yuv else 'ı') if kalin else ('ü' if yuv else 'i')
        if ch != doğru: hata.append('ünlü')
    # ünlüyle biten sayıya kaynaştırma: 'e/'a yerine 'ye/'ya, 'i yerine 'yi
    if unlu and e[0] in 'eaıiuü' and not e.startswith(('in', 'ın', 'un', 'ün', 'ıncı', 'inci', 'uncu', 'üncü')): hata.append('kaynaştırma')
    if not unlu and e[0] == 'y': hata.append('kaynaştırma')
    return hata
pat = re.compile(r"\b(\d{1,3}(?:\.\d{3})*|\d+)['’]([a-zçğıöşü]{1,8})")
for f in sorted(glob.glob(f'{S}/sb/batch/sb_[0-9][0-9].py')):
    no = re.search(r'sb_(\d\d)', f).group(1)
    for i, q in enumerate(runpy.run_path(f)['Q'], 1):
        for a in ('kok', 'd', 'c', 'siklar', 'g'):
            v = q.get(a)
            if not v: continue
            t = ' '.join(v) if isinstance(v, list) else v
            for m in pat.finditer(t):
                n = int(m.group(1).replace('.', ''))
                h = beklenen(son_kelime(n), m.group(2))
                if h: print(f"SB{no} Q{i} {a}: {m.group(0)} {h} | …{t[max(0,m.start()-30):m.end()+15]}…")
