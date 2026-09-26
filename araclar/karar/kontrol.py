import random, sys, json
exec(open('sorular.py').read())
L="ABCDE"
def seq(seed):
    r=random.Random(seed)
    while True:
        s=list(L*3); 
        for i in range(len(s)-1,0,-1):
            j=r.randint(0,i); s[i],s[j]=s[j],s[i]
        if all(not(s[i]==s[i+1]==s[i+2]) for i in range(len(s)-2)): return s
S=seq(2027)
bad=0
for i,q in enumerate(Q,1):
    d=len(q['d']); cl=[len(x) for x in q['c']]
    longest = d>max(cl)
    near=sum(1 for x in cl if x>=0.92*d)
    ok = near>=2 and (q.get('protB') or not longest) and (q.get('protB') is None or longest or True)
    if not ok: bad+=1
    print(f"{i:2} {q['tip']:3} {q['z']:2} {S[i-1]} dogru={d} celd={cl} yakin={near} enUzun={'E' if longest else 'H'} {'B' if q.get('protB') else 'A'} {'OK' if ok else 'HATA'}")
print("harf:",''.join(S),"hatali:",bad)
json.dump(S,open('harfler.json','w'))
