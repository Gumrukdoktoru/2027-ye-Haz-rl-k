import json,re,itertools,os
HAFIZA=os.path.join(os.path.dirname(os.path.abspath(__file__)),'../../sorular/hafiza/URETIM-HAFIZASI.md')
def tok(s):
    s=s.lower().replace('İ','i').replace('I','ı')
    return set(w for w in re.findall(r'\w+',s) if len(w)>3)
def jac(a,b): return len(a&b)/max(1,len(a|b))
yeni=[]
for S in (3,4,5):
    for q in json.load(open(f'set{S}.json')):
        yeni.append((q['id'],q['cek'],q.get('kok',''),tok(q['cek'])))
eski=[]
for l in open(HAFIZA):
    p=[x.strip() for x in l.split('|')]
    if len(p)>=8 and re.match(r'(KAR|GMY)',p[0]): eski.append((p[0],p[3],tok(p[3])))
print('eski',len(eski),'yeni',len(yeni))
n=0
for y in yeni:
    for e in eski:
        j=jac(y[3],e[2])
        if j>=0.4: n+=1;print(f'ESKİ {j:.2f} {y[0]} ~ {e[0]}\n   Y: {y[1]}\n   E: {e[1]}')
for a,b in itertools.combinations(yeni,2):
    j=jac(a[3],b[3])
    if j>=0.4: n+=1;print(f'YENİ {j:.2f} {a[0]} ~ {b[0]}\n   1: {a[1]}\n   2: {b[1]}')
print('toplam aday',n)
