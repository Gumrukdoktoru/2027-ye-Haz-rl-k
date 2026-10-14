"""set11-15.json'dan 500 hafıza satırını URETIM-HAFIZASI.md'ye ekler (varsa eski GMY11-15 satırlarını yeniler)."""
import json, re
P = '../../sorular/hafiza/URETIM-HAFIZASI.md'
s = open(P).read()
lines = s.split('\n')
lines = [l for l in lines if not re.match(r'GMY(11|12|13|14|15)-\d{3} \|', l)]
yeni = []
for d in range(11, 16):
    for q in json.load(open(f'set{d}.json')):
        cek = q['cek'].replace('|', '/'); madde = q['madde'].replace('|', '/')
        yeni.append(f"GMY{d}-{q['no']:03d} | {q.get('konu') or q.get('ders')} | {madde} | {cek} | {q['tip']} | {q['z']} | {q['harf']} | GMY-S{d}")
# kod bloğunun kapanışından önce ekle
kap = max(i for i, l in enumerate(lines) if l.strip() == '```')
lines = lines[:kap] + yeni + lines[kap:]
txt = '\n'.join(lines)
txt = re.sub(r'Toplam: \d+ satır \(.*?\)', 'Toplam: 1515 satır (Karar: 15 · GMY deneme S1: 100 · S2: 100 · S3: 100 · S4: 100 · S5: 100 · S6: 100 · S7: 100 · S8: 100 · S9: 100 · S10: 100 · S11: 100 · S12: 100 · S13: 100 · S14: 100 · S15: 100)', txt)
open(P, 'w').write(txt)
print(len(yeni), 'satır eklendi')
