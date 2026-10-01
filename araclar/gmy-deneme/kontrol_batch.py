"""Kullanım: python3 kontrol_batch.py batch_X.py
Her soru dict alanları: konu, tip, z, tuzak, madde, cek, kok(list), d, c(list 4), g, t, protB(opsiyonel bool)"""
import sys, re
ns={}; exec(open(sys.argv[1]).read(), ns); Q=ns['Q']
TIP={'DY','DĞ','ÇI','SY','SÜ','MK','TN','BD','EŞ','UK','UU','HESAP'}
Z={'ÇK','K','O','Z','ÇZ'}
TZ={"İdare/makam karıştırma","Rejim sınıflandırma","Tanım çiftleri","Belge eşleştirme","Süre kaydırma","Eşik/oran kaydırma","İstisna atlatma"}
err=0; prev=None
for i,q in enumerate(Q,1):
    e=[]
    for k in ['konu','tip','z','tuzak','madde','cek','kok','d','c','g','t']:
        if k not in q: e.append('eksik alan '+k)
    if e: print(i,e); err+=1; continue
    if q['tip'] not in TIP: e.append('tip?')
    if q['z'] not in Z: e.append('zorluk?')
    if q['tuzak'] not in TZ: e.append('tuzak kategorisi?')
    if len(q['c'])!=4: e.append('4 çeldirici olmalı')
    if q['tip']==prev: e.append('aynı tip ardışık')
    prev=q['tip']
    if len(q['cek'].split())>25: e.append('çekirdek >25 kelime')
    alls=' '.join(q['kok']+[q['d']]+q['c'])
    if re.search(r'\b(hepsi|hiçbiri)\b',alls,re.I): e.append('yasak şık')
    if re.search(r'kaynak metne|madde hükmüdür',alls+q['g'],re.I): e.append('yasak ifade')
    if re.search(r'\d+\s*(inci|ıncı|üncü|uncu|nci|ncı|ncü|ncu|’?\s*(n?[ıiuü]n?c[ıiuü]))?\s*madde|madde(si(nin)?)?\s*\d|fıkra|\bbend',' '.join(q['kok']+[q['d']]+q['c']),re.I): e.append('kökte/şıkta madde no')
    if len(set([q['d']]+q['c']))!=5: e.append('tekrarlı şık')
    if q['tip']!='SY':
        d=len(q['d']); cl=[len(x) for x in q['c']]
        near=sum(1 for x in cl if x>=0.92*d); longest=d>max(cl)
        if near<2: e.append(f'Protokol: ≥2 çeldirici doğru şıkkın %92si olmalı (doğru={d}, çeld={cl})')
        if longest and not q.get('protB'): e.append(f'Protokol A: doğru şık en uzun olamaz (doğru={d}, çeld={cl})')
    if e: err+=1; print(f'{i}:', '; '.join(e))
from collections import Counter
print('Soru:',len(Q),'Hatalı:',err)
print('Zorluk:',dict(Counter(q['z'] for q in Q)),'ProtB:',sum(1 for q in Q if q.get('protB')))
print('Tip:',dict(Counter(q['tip'] for q in Q)))
print('Tuzak:',dict(Counter(q['tuzak'] for q in Q)))
