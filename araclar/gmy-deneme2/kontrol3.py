"""Prompt 3 denetimi. Kullanım: python3 kontrol3.py batch_X.py
Soru alanları: konu, kalip, z (ÇK/K/O/Z/ÇZ), madde (ör. "GK 6/2; GY 27"), cek (≤25 kelime), kok (list; önermeli ise öncül satırları "I. ..." ile),
d (doğru şık), c (4 çeldirici), g (gerekçe; '(MD ...)' ile biter), kanit (dosya | birebir alıntı), cikmis (opsiyonel: '2023/45' gibi)"""
import sys, re
from collections import Counter
ns={}; exec(open(sys.argv[1]).read(), ns); Q=ns['Q']
KAL={'TANIM','KAVRAM','KAPSAM','KAPSAM_DIŞI','DOĞRU','YANLIŞ','ÖNERMELİ','SÜRE','ORAN-TUTAR','YETKİ','BELGE','ŞART','HESAP','BOŞLUK','EŞLEŞTİRME','MÜEYYİDE','OLAY','TABİ','ZORUNLULUK','MATRAH','DAYANAK','SONUÇ','MUAFİYET','KISA_AD'}
YAPAY=r'temel özellik|temel kural|kritik husus|en önemli düzenleme'
GYASAK=r'madde hükmüdür|temel düzenlemedir|madde bunu söylemektedir|kaynak metne göre|verilen kaynağa göre|kaynakta belirtildiği'
MADDE=r'\b\d+\s*[’\']?\s*(inci|ıncı|üncü|uncu|nci|ncı|ncü|ncu|nin|nın|nün|nun)?\s*madde|madde(si(nin|ne)?)?\s*\d|\bfıkra|\bbendi?\b|\b\d{2,3}/\d'
err=0; longest=0; onerme_all=0
for i,q in enumerate(Q,1):
    e=[]
    miss=[k for k in ['konu','kalip','z','madde','cek','kok','d','c','g','kanit'] if k not in q]
    if miss: print(i,'eksik alan',miss); err+=1; continue
    if q['kalip'] not in KAL: e.append('kalip?')
    if q['z'] not in {'ÇK','K','O','Z','ÇZ'}: e.append('zorluk?')
    if len(q['c'])!=4: e.append('4 çeldirici olmalı')
    if len(set([q['d']]+q['c']))!=5: e.append('tekrarlı şık')
    if len(q['cek'].split())>25: e.append('çekirdek >25 kelime')
    metin=' '.join(q['kok']+[q['d']]+q['c'])
    if re.search(MADDE,metin,re.I): e.append('kökte/şıkta madde-fıkra-bent no')
    if re.search(r'\b(hepsi|hiçbiri)\b',' '.join([q['d']]+q['c']),re.I): e.append('yasak şık hepsi/hiçbiri')
    if re.search(YAPAY,' '.join(q['kok']),re.I): e.append('yapay niteleme kökte')
    if re.search(GYASAK,q['g'],re.I): e.append('gerekçede yasak ifade')
    if not re.search(r'\(MD[^)]*\)\s*$',q['g'].strip()): e.append("gerekçe '(MD …)' ile bitmeli")
    if re.match(r'^[^.?]{0,70}(Kanunu?\'?[nN]?[ae]? göre|Yönetmeliğine göre|Kararına göre),? aşağıdakilerden hangisi (doğrudur|yanlıştır)\?$',q['kok'][0].strip()): e.append('bağlamsız genel kök (konu yok)')
    on=[l for l in q['kok'] if re.match(r'^(I|II|III|IV|V)\.\s',l.strip())]
    if q['kalip']=='ÖNERMELİ' and len(on)<3: e.append('önermeli en az 3 önerme')
    if on and len(on)>=3:
        allr=['I','II','III','IV','V'][:len(on)]
        tok=set(re.findall(r'\b[IV]+\b',q['d']))
        if re.fullmatch(r'[IV, ve]+',q['d']) and tok==set(allr): onerme_all+=1
    if len(q['d'])>max(len(x) for x in q['c']): longest+=1
    if '|' not in q['kanit'] and ':' not in q['kanit']: e.append('kanit "dosya | alıntı" biçiminde olmalı')
    if e: err+=1; print(f'{i}:', '; '.join(e))
print('Soru:',len(Q),'Hatalı:',err)
print('Zorluk:',dict(Counter(q['z'] for q in Q)),'| Kalıp:',dict(Counter(q['kalip'] for q in Q)))
print(f'Doğru şık en uzun: {longest} (≤%25 olmalı: {"OK" if longest<=len(Q)*0.25 else "FAZLA"}) | Tüm öncüller doğru: {onerme_all}')
print('Çıkmış bilgi alanı karşılayan:',sum(1 for q in Q if q.get('cikmis')))
