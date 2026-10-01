import json, random, re, unicodedata, collections, pathlib, sys
MET=pathlib.Path('/home/user/2027-ye-haz-rl-k/kaynaklar/metin')
Q=[]
for b in 'ABCDE':
    ns={}; exec(open(f'batch_{b}.py').read(), ns)
    for q in ns['Q']: q['batch']=b; Q.append(q)
print('toplam',len(Q))
# --- kanıt denetimi (gümrük)
norm=lambda s: re.sub(r'\s+',' ',unicodedata.normalize('NFC',s)).strip().lower()
corpus={f.name:norm(f.read_text()) for f in MET.glob('*.txt')}
allc=' '.join(corpus.values())
kotu=[]
for i,q in enumerate(Q,1):
    if q['batch']=='A': continue
    k=q.get('kanit','')
    quotes=re.findall(r'[“"«]([^”"»]{15,})[”"»]',k) or [k.split('|',1)[-1] if '|' in k else k.split(':',1)[-1]]
    ok=False
    for qt in quotes:
        frag=norm(qt).strip(' .…')
        parts=[p.strip() for p in re.split(r'\.\.\.|…|\[\.\.\.\]',frag) if len(p.strip())>12]
        if parts and all(p in allc for p in parts): ok=True
    if not ok: kotu.append(i)
print('kanıtı birebir bulunamayan:',kotu)
# --- harf dizisi: her harf 20, ardışık<=2
L='ABCDE'; r=random.Random(2025)
while True:
    s=list(L*20); r.shuffle(s)
    if all(not(s[i]==s[i+1]==s[i+2]) for i in range(98)): break
for i,(q,h) in enumerate(zip(Q,s),1):
    k=L.index(h); dist=list(q['c']); q['opts']=[q['d'] if j==k else dist.pop(0) for j in range(5)]
    q['harf']=h; q['no']=i; q['id']=f'GMY-{i:03d}'
ard=[i for i in range(1,100) if Q[i]['tip']==Q[i-1]['tip']]
print('ardışık aynı tip (1-indeks):',[i+1 for i in ard])
json.dump(Q,open('set100.json','w'),ensure_ascii=False,indent=0)
C=collections.Counter
print('zorluk',C(q['z'] for q in Q),'protB',sum(bool(q.get('protB')) for q in Q))
print('harf',C(s))
