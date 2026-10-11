"""Bir batch dosyasındaki her soru için Deneme 1–5 hafızasında ve 2021–2025 çıkmış soru envanterinde
aynı konudaki / aynı maddeli eski soruları listeler (tam örtüşme denetimi için okuma listesi).
Kullanım: python3 eski_ilgili.py batch_K08.py
Eski soru metni: GMY-xxx → ../../sorular/GK_GMY2025_Deneme_S1_100soru.md; GMYn-xxx → ../../sorular/GK_GMY_Deneme{n}_100soru.md;
çıkmış: sinav/<yıl>_duz.txt (2025: sinav/2025B_duz.txt)."""
import sys, re, csv
from kontrol import tlower
def maddeler(s):
    s = re.sub(r'seri(?: no)?:? ?\d+|\d{4}/\d+|\d+ sayılı', ' ', tlower(s))
    return set(re.findall(r'\b(\d{1,3})(?=/|\b)', s))
def aile(s):
    s = tlower(s); a = set()
    if re.search(r'\bgk\b|gümrük kanunu|4458 sayılı gümrük kanunu m', s): a.add('GK')
    if re.search(r'\bgy\b|gümrük yönetmeliği', s): a.add('GY')
    if '5607' in s or 'kaçakçılık' in s: a.add('5607')
    if '15481' in s or 'karar m' in s: a.add('KARAR')
    if re.search(r'tebliğ|seri|ggt', s): a.add('TEB')
    if 'ithalat rejimi' in s or 'irk' in s: a.add('IRK')
    return a
def konu_k(s): return tlower(s).split('(')[0].strip()
HAF = []
for l in open('../../sorular/hafiza/URETIM-HAFIZASI.md'):
    m = re.match(r'(GMY\d?-\d{3}) \| ([^|]+) \| ([^|]+) \| ([^|]+) \|', l)
    if m and not re.match(r'GMY(6|7|8|9|10)-', m.group(1)): HAF.append((m.group(1), m.group(2).strip(), m.group(3), m.group(4).strip()))
ENV = list(csv.DictReader(open('cikmis_envanter.tsv'), delimiter='\t'))
ns = {}; exec(open(sys.argv[1]).read(), ns)
for q in ns['Q']:
    km = maddeler(q['madde']); kk = konu_k(q.get('konu') or '')
    print(f"\n## {q['id']} [{q['tip']}] {q.get('konu')} | {q['madde']}\n   çekirdek: {q['cek']}")
    sec = []
    for i, k, md, c in HAF:
        ort = km & maddeler(md) if aile(q['madde']) & aile(md) else set()
        ayni = bool(kk) and konu_k(k) == kk
        if ort or ayni: sec.append((len(ort) + ayni, i, k, md, c))
    for o, i, k, md, c in sorted(sec, reverse=True)[:14]:
        print(f"   {'*' if o else ' '} {i} | {md} | {c[:150]}")
    for e in ENV:
        if konu_k(e['KONU']) == kk: print(f"   ç {e['YIL']}/{e['SORU_NO']} | {e['ÖLÇÜLEN_BİLGİ'][:150]}")
