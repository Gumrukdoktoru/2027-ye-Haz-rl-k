"""Üç setli batch denetimi. Kullanım: python3 kontrol4.py batch_X.py
Her soru dict'inde ek alan: set (3, 4 veya 5). Her sette 10 soru; set içi zorluk ÇK1 K2 O4 Z2 ÇZ1."""
import sys, subprocess, tempfile, os, re, collections
ns={}; exec(open(sys.argv[1]).read(), ns); Q=ns['Q']
here=os.path.dirname(os.path.abspath(__file__)); err=0
for s in (3,4,5):
    sub=[q for q in Q if q.get('set')==s]
    with tempfile.NamedTemporaryFile('w',suffix='.py',delete=False) as f: f.write('Q='+repr(sub)); tmp=f.name
    out=subprocess.run([sys.executable,os.path.join(here,'kontrol3.py'),tmp],capture_output=True,text=True).stdout
    os.unlink(tmp)
    print(f'--- SET {s} ---'); print(out.strip())
    if 'Hatalı: 0' not in out: err+=1
    z=collections.Counter(q['z'] for q in sub)
    if len(sub)!=10: print(f'!! set {s}: 10 soru olmalı ({len(sub)})'); err+=1
    if dict(z)!={'ÇK':1,'K':2,'O':4,'Z':2,'ÇZ':1}: print(f'!! set {s}: zorluk ÇK1 K2 O4 Z2 ÇZ1 olmalı -> {dict(z)}'); err+=1
    lg=sum(len(q['d'])>max(map(len,q['c'])) for q in sub)
    if lg>2: print(f'!! set {s}: doğru şık en uzun {lg} (≤2)'); err+=1
# setler arası çekirdek benzerliği
W=lambda t:set(re.findall(r'\w{4,}',t.lower()))
for i in range(len(Q)):
    for j in range(i+1,len(Q)):
        a,b=W(Q[i]['cek']),W(Q[j]['cek'])
        if a and b and len(a&b)/min(len(a),len(b))>=0.7: print(f'?? benzer çekirdek: {i+1} ↔ {j+1}: {Q[i]["cek"][:60]} | {Q[j]["cek"][:60]}')
miss=[i+1 for i,q in enumerate(Q) if q.get('set') not in (3,4,5)]
if miss: print('!! set alanı eksik:',miss); err+=1
print('GENEL SONUÇ:', 'TEMİZ' if err==0 else f'{err} sorun')
