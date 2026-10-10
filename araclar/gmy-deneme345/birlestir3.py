"""Kullanım: python3 birlestir3.py  → set3.json, set4.json, set5.json"""
import json, random, re, unicodedata, collections, pathlib
SIRA=['GKA','GKB','G7','G3','G1','G8','G2','G4','G6','G5']   # 2025 kitapçık sırasına yakın
GK_ALT={'Türkçe':0,'Matematik':1,'Tarih':2,'Anayasa':3,'Uluslararası':3}
norm=lambda s: re.sub(r'\s+',' ',unicodedata.normalize('NFC',s)).strip().lower()
allc=' '.join(norm(f.read_text()) for f in pathlib.Path('metin').glob('*.txt'))
L='ABCDE'
def kanit_ok(q):
    k=q['kanit']; body=k.split('|',1)[1] if '|' in k else k.split(':',1)[-1]
    for qt in (re.findall(r'[“"«]([^”"»]{15,})[”"»]',body) or [body]):
        parts=[p.strip(' .…;,') for p in re.split(r'\.\.\.|…|\[\.\.\.\]|\n',norm(qt)) if len(p.strip())>12]
        if parts and all(p in allc for p in parts): return True
    return q['konu']=='Matematik'
def dizi(seed):
    r=random.Random(seed)
    while True:
        kalan={h:20 for h in L}; s=[]
        for _ in range(100):
            ad=[h for h in L if kalan[h] and (not s or h!=s[-1])]
            if not ad: break
            m=max(kalan[h] for h in ad); h=r.choice([h for h in ad if kalan[h]>=m-3]); s.append(h); kalan[h]-=1
        if len(s)==100: return s

ROMA={'I':1,'II':2,'III':3,'IV':4,'V':5}
AYLAR=['Ocak','Şubat','Mart','Nisan','Mayıs','Haziran','Temmuz','Ağustos','Eylül','Ekim','Kasım','Aralık']
def sayi(t):
    t=t.strip().rstrip('.')
    m=re.fullmatch(r'(\d{1,2}) ('+'|'.join(AYLAR)+r') (\d{4})',t)
    if m: return ('D',int(m.group(3))*10000+(AYLAR.index(m.group(2))+1)*100+int(m.group(1)))
    m=re.fullmatch(r'(\d{1,2})\.(\d{1,2})\.(\d{4})',t)
    if m: return ('D',int(m.group(3))*10000+int(m.group(2))*100+int(m.group(1)))
    m=re.fullmatch(r'(?:Yalnız\s+)?(I|II|III|IV|V)',t)
    if m: return ('R',ROMA[m.group(1)])
    m=re.fullmatch(r'(?:Yüzde\s*|%\s*)?(\d{1,3}(?:\.\d{3})*(?:,\d+)?|\d+(?:,\d+)?)\s*([A-Za-zçğıöşüÇĞİÖŞÜ.%/ ]{0,20})',t)
    if m:
        v=float(m.group(1).replace('.','').replace(',','.')); return ('N:'+m.group(2).strip().lower(),v)
    m=re.fullmatch(r'(\d{1,2})[.:](\d{2})',t)
    if m: return ('T',int(m.group(1))*60+int(m.group(2)))
    return None
def sirala(opts):
    k=[sayi(o) for o in opts]
    if any(x is None for x in k) or len({x[0] for x in k})!=1 or len({x[1] for x in k})<5: return None
    return [o for _,o in sorted(zip([x[1] for x in k],opts))]
def dizi2(seed,sabit):
    r=random.Random(seed)
    for _ in range(20000):
        kalan={h:20 for h in L}
        for h in sabit.values(): kalan[h]-=1
        if min(kalan.values())<0: raise SystemExit('sabit harfler 20yi aşıyor')
        s=[]; ok=True
        for i in range(100):
            if i in sabit:
                h=sabit[i]
                if s and s[-1]==h and (i-1) not in sabit: ok=False; break
                s.append(h); continue
            nxt=sabit.get(i+1)
            ad=[h for h in L if kalan[h] and (not s or h!=s[-1]) and h!=nxt]
            if not ad: ok=False; break
            m=max(kalan[h] for h in ad); h=r.choice([h for h in ad if kalan[h]>=m-3]); s.append(h); kalan[h]-=1
        if ok and len(s)==100: return s
    raise SystemExit('harf dizisi kurulamadı (art arda sabit aynı harf olabilir)')
def harfle(q):
    g=q['g']
    for kw in ('seçeneğidir','şıkkıdır'):
        idx=g.rfind(kw)
        if idx<0: continue
        seg=g[:idx].rstrip()
        if not seg or seg[-1] not in "'’”\"": continue
        body=seg[:-1]
        for jj,o in sorted(enumerate(q['opts']),key=lambda x:-len(x[1])):
            for v in (o,o.rstrip('.')):
                if body.endswith(v) and len(body)>len(v) and body[-len(v)-1] in "'‘“\"":
                    return body[:-len(v)-1]+f"{L[jj]} "+g[idx:]
    md=g.rfind('(MD'); bas,son=g[:md].rstrip(),g[md:]
    k=bas.rfind('Bu nedenle')
    if k>=0: bas=bas[:k].rstrip()
    return f"{bas} Bu nedenle doğru cevap {q['harf']} seçeneğidir. {son}"
B={b:[] for b in SIRA}
for b in SIRA:
    ns={}; exec(open(f'batch_{b}.py').read(),ns)
    for i,q in enumerate(ns['Q'],1): q['batch']=b; q['bidx']=i; B[b].append(q)
for s in (3,4,5):
    Q=[]
    for b in SIRA:
        part=[q for q in B[b] if q['set']==s]
        if b.startswith('GK'): part.sort(key=lambda q:GK_ALT.get(q['konu'],9))
        Q+=part
    gk=[q for q in Q if q['batch'].startswith('GK')]; Q=sorted(gk,key=lambda q:GK_ALT.get(q['konu'],9))+[q for q in Q if not q['batch'].startswith('GK')]
    # sabit-harfli komşu çakışmalarını grup içi yeniden sıralamayla azalt
    import itertools
    def fl(q):
        o=sirala([q['d']]+q['c']); return L[o.index(q['d'])] if o else None
    def cak(Q): return sum(1 for i in range(1,len(Q)) if fl(Q[i]) and fl(Q[i])==fl(Q[i-1]))
    gruplar=[]; i=0
    while i<len(Q):
        k=(Q[i]['batch'],Q[i]['konu'] if Q[i]['batch'].startswith('GK') else '')
        j=i
        while j<len(Q) and (Q[j]['batch'],Q[j]['konu'] if Q[j]['batch'].startswith('GK') else '')==k: j+=1
        gruplar.append((i,j)); i=j
    rr=random.Random(77+s)
    for (i,j) in gruplar:
        if cak(Q)==0: break
        part=Q[i:j]; best=(cak(Q),part)
        aday=itertools.permutations(part) if len(part)<=6 else (rr.sample(part,len(part)) for _ in range(400))
        for p in aday:
            Q2=Q[:i]+list(p)+Q[j:]; c=cak(Q2)
            if c<best[0]: best=(c,list(p))
        Q[i:j]=best[1]
    sabit={}
    for i,q in enumerate(Q):
        o=sirala([q['d']]+q['c'])
        if o: q['opts']=o; sabit[i]=L[o.index(q['d'])]
    hs=dizi2(1000+s,sabit)
    for i,(q,h) in enumerate(zip(Q,hs),1):
        if i-1 not in sabit:
            k=L.index(h); dist=list(q['c']); q['opts']=[q['d'] if j==k else dist.pop(0) for j in range(5)]
        q['harf']=h; q['no']=i; q['id']=f'GMY{s}-{i:03d}'
    print(f'   doğal sıralı şıklı soru: {len(sabit)}')
    for q in Q: q['g']=harfle(q)
    kot=[q['no'] for q in Q if not kanit_ok(q)]
    uyum=[q['no'] for q in Q if re.findall(r'\b([A-E]) (?:seçeneğidir|şıkkıdır)',q['g'])[-1:]!=[q['harf']]]
    ard=[q['no'] for i,q in enumerate(Q[1:],1) if q['harf']==Q[i-1]['harf']]
    C=collections.Counter
    print(f"SET {s}: {len(Q)} soru | kanıt bulunamayan {kot} | gerekçe-harf uyumsuz {uyum} | art arda aynı harf {ard}")
    print('   zorluk',dict(C(q['z'] for q in Q)),'| harf',dict(C(q['harf'] for q in Q)),'| çıkmış karşılayan',sum(1 for q in Q if q.get('cikmis')),'| doğru en uzun',sum(len(q['d'])>max(map(len,q['c'])) for q in Q))
    json.dump(Q,open(f'set{s}.json','w'),ensure_ascii=False,indent=0)
# 2024-2025 kapsama
import csv
rows=[r for r in csv.reader(open('cikmis_envanter.tsv'),delimiter='\t')][1:]
hedef={f"{r[0]}/{r[1]}" for r in rows if r[0] in ('2024','2025') and r[5]!='YOK'}
kars=set()
for b in SIRA:
    for q in B[b]:
        for t in re.findall(r'20\d\d/\d+',q.get('cikmis','') or ''): kars.add(t)
print('2024-2025 kaynakta olan çıkmış soru:',len(hedef),'| karşılanan:',len(hedef&kars),'| karşılanmayan:',sorted(hedef-kars,key=lambda x:(x[:4],int(x[5:]))))
