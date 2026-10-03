import json, random, re, unicodedata, collections, pathlib
MET=pathlib.Path('metin')
Q=[]
for b in ['GK','G1','G2','G3','G4']:
    ns={}; exec(open(f'batch_{b}.py').read(), ns)
    for q in ns['Q']: q['batch']=b; Q.append(q)
norm=lambda s: re.sub(r'\s+',' ',unicodedata.normalize('NFC',s)).strip().lower()
allc=' '.join(norm(f.read_text()) for f in MET.glob('*.txt'))
kotu=[]
for i,q in enumerate(Q,1):
    k=q['kanit']; body=k.split('|',1)[1] if '|' in k else k.split(':',1)[-1]
    quotes=re.findall(r'[“"«]([^”"»]{15,})[”"»]',body) or [body]
    ok=False
    for qt in quotes:
        parts=[p.strip(' .…;,') for p in re.split(r'\.\.\.|…|\[\.\.\.\]|\n',norm(qt)) if len(p.strip())>12]
        if parts and all(p in allc for p in parts): ok=True
    if not ok and q['konu']!='Matematik': kotu.append(i)
L='ABCDE'; r=random.Random(2027)
def dizi():
    while True:
        kalan={h:20 for h in L}; s=[]
        for _ in range(100):
            ad=[h for h in L if kalan[h] and (not s or h!=s[-1])]
            if not ad: break
            m=max(kalan[h] for h in ad); ad2=[h for h in ad if kalan[h]>=m-3]
            h=r.choice(ad2); s.append(h); kalan[h]-=1
        if len(s)==100: return s
s=dizi()
assert all(s[i]!=s[i+1] for i in range(99)) and all(s.count(h)==20 for h in L)
for i,(q,h) in enumerate(zip(Q,s),1):
    k=L.index(h); dist=list(q['c']); q['opts']=[q['d'] if j==k else dist.pop(0) for j in range(5)]
    q['harf']=h; q['no']=i; q['id']=f'GMY2-{i:03d}'
def harfle(q):
    g=q['g']
    for kw in ('seçeneğidir','şıkkıdır'):
        idx=g.rfind(kw)
        if idx<0: continue
        seg=g[:idx].rstrip()
        if not seg or seg[-1] not in "'’”\"": continue
        body=seg[:-1]
        for jj,o in sorted(enumerate(q['opts']),key=lambda x:-len(x[1])):
            for v in (o, o.rstrip('.')):
                if body.endswith(v) and len(body)>len(v) and body[-len(v)-1] in "'‘“\"":
                    return body[:-len(v)-1]+f"{L[jj]} "+g[idx:]
    h=q['harf']; md=g.rfind('(MD')
    bas, son = g[:md].rstrip(), g[md:]
    k=bas.rfind('Bu nedenle')
    if k>=0: bas=bas[:k].rstrip()
    return f"{bas} Bu nedenle doğru cevap {h} seçeneğidir. {son}"
eksik=[]
for q in Q:
    q['g']=harfle(q)
    if not re.search(r'\b[A-E] (seçeneğidir|şıkkıdır)',q['g']): eksik.append(q['no'])
print('gerekçede harf yazılamayan:',eksik)
json.dump(Q,open('set2.json','w'),ensure_ascii=False,indent=0)
C=collections.Counter
print('toplam',len(Q),'| kanıtı bulunamayan:',kotu)
print('zorluk',dict(C(q['z'] for q in Q)),'| harf',dict(C(s)))
print('çıkmış karşılayan:',sum(1 for q in Q if q.get('cikmis')),'| doğru en uzun:',sum(len(q['d'])>max(map(len,q['c'])) for q in Q))
