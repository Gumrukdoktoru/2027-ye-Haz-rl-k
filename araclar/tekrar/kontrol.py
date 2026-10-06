"""Hızlı tekrar seti denetimi: python3 -I araclar/tekrar/kontrol.py 02
- Her sorunun 5. alanı (kanıt) kaynak metinde birebir geçmeli (boşluk/tırnak/büyük-küçük harf farkı yok sayılır).
- Kanıt tek metin ya da metin listesi olabilir. 01 numaralı set kanıtsızdır (elle doğrulandı).
- Yinelenen soru, boş alan ve dayanak eksikliği raporlanır."""
import sys, json, subprocess, pathlib, re, zipfile, xml.etree.ElementTree as ET
KOK = pathlib.Path(__file__).resolve().parents[2]
W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

def para(p):
    s = []
    for n in p.iter():
        if n.tag == W + 't' and n.text: s.append(n.text)
        elif n.tag == W + 'tab': s.append('\t')
        elif n.tag in (W + 'br', W + 'cr'): s.append('\n')
    return ''.join(s)

def kaynak_metin(no):
    f = next(f for f in KOK.glob(f'{int(no)}-*.docx'))
    root = ET.fromstring(zipfile.ZipFile(f).read('word/document.xml'))
    o = []
    for el in root.find(W + 'body'):
        if el.tag == W + 'p': o.append(para(el))
        elif el.tag == W + 'tbl':
            for tr in el.iter(W + 'tr'):
                o.append(' | '.join(' '.join(para(p) for p in tc.iter(W + 'p')) for tc in tr.findall(W + 'tc')))
    return f.name, '\n'.join(o)

def norm(s):
    s = s.replace('İ', 'i').replace('I', 'ı').lower()
    s = re.sub(r'[“”„"«»]', '"', s); s = re.sub(r"[‘’`´]", "'", s)
    s = s.replace('\xad', '').replace('​', '')
    return re.sub(r'\s+', ' ', s).strip()

no = sys.argv[1]
v = json.loads(subprocess.check_output(['node', '-e', f"console.log(JSON.stringify(require('{KOK}/araclar/tekrar/veri_{no}.js')))"]))
ad, metin = kaynak_metin(no)
M = norm(metin)
hata, sorular, n = [], set(), 0
for b in v['bolumler']:
    for q in b['sorular']:
        n += 1
        if len(q) < 4 or not all(isinstance(x, str) for x in q[:4]) or not q[0].strip() or not q[1].strip() or not q[2].strip():
            hata.append(f'{n}: eksik alan'); continue
        if norm(q[0]) in sorular: hata.append(f'{n}: yinelenen soru')
        sorular.add(norm(q[0]))
        if no == '01': continue
        k = q[4] if len(q) > 4 else None
        if not k: hata.append(f'{n}: kanıt yok'); continue
        for parca in (k if isinstance(k, list) else [k]):
            if len(norm(parca)) < 15: hata.append(f'{n}: kanıt çok kısa: {parca!r}')
            elif norm(parca) not in M: hata.append(f'{n}: kanıt kaynakta yok: {parca[:90]!r}')
print(f'{ad}: {n} soru, {len(v["bolumler"])} bölüm, {len(v.get("tuzaklar", []))} tuzak')
print('\n'.join(hata) if hata else 'TAMAM: tüm kanıtlar kaynakta bulundu.')
sys.exit(1 if hata else 0)
