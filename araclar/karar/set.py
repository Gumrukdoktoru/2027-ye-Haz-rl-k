import json, collections
exec(open('sorular.py').read())
S=json.load(open('harfler.json')); L="ABCDE"
out=[]
for i,(q,h) in enumerate(zip(Q,S),1):
    k=L.index(h); dist=list(q['c']); opts=[]
    for j in range(5): opts.append(q['d'] if j==k else dist.pop(0))
    out.append(dict(q, no=i, id=f"KAR-{i:03d}", harf=h, opts=opts))
json.dump(out,open('set.json','w'),ensure_ascii=False)
Z={'ÇK':'Çok Kolay','K':'Kolay','O':'Orta','Z':'Zor','ÇZ':'Çok Zor'}
md=["# Gümrük Koçu - Ufuk Çetintaş","","## Set Kartı","","| Alan | Değer |","|---|---|",
"| Set | S1 |","| Konu | GK/GY – Karar (Gümrük Mevzuatının Uygulanmasına İlişkin Kararlar) |","| Sınıf | GM |",
"| Soru sayısı | 15 |","| Zorluk | Zorlayıcı (0-10-30-40-20) → ÇK 0 · K 1 · O 5 · Z 6 · ÇZ 3 |","| Hafızadaki önceki soru (Karar) | 0 |","| Bu setle toplam | 15 |","","## Sorular",""]
for q in out:
    md.append(f"**{q['no']}.** "+q['kok'][0]); md += ["", *[f"{l}  " for l in q['kok'][1:]]] if len(q['kok'])>1 else [""]
    if len(q['kok'])>1: md.append("")
    md += [f"{L[j]}) {o}  " for j,o in enumerate(q['opts'])]; md.append("")
md += ["## Cevap Anahtarı","","| "+" | ".join(str(q['no']) for q in out)+" |","|"+"---|"*15,"| "+" | ".join(q['harf'] for q in out)+" |","","## Çözümler",""]
for q in out:
    md += [f"**{q['no']}.**","",f"- **Doğru cevap:** {q['harf']}",f"- **Gerekçe:** {q['g']}",f"- **Tuzak nokta şudur:** {q['t']}",f"- **Yasal Dayanak:** {q['madde'].replace('GK','Gümrük Kanunu').replace('GY','Gümrük Yönetmeliği')}",""]
def tab(title,cnt,order):
    r=[f"**{title}**","","| "+" | ".join(order)+" |","|"+"---|"*len(order),"| "+" | ".join(str(cnt.get(o,0)) for o in order)+" |",""]; return r
md += ["## Dağılım Tabloları",""]
md += tab("Tip",collections.Counter(q['tip'] for q in out),["DY","DĞ","ÇI","SÜ","MK","BD","EŞ","UK","UU"])
md += tab("Zorluk",collections.Counter(q['z'] for q in out),["ÇK","K","O","Z","ÇZ"])
md += tab("Doğru cevap harfi",collections.Counter(q['harf'] for q in out),list(L))
tz=["İdare/makam karıştırma","Rejim sınıflandırma","Tanım çiftleri","Belge eşleştirme","Süre kaydırma","Eşik/oran kaydırma","İstisna atlatma"]
md += tab("Tuzak kategorisi",collections.Counter(q['tuzak'] for q in out),tz)
md += ["**Şık uzunluğu:** Protokol A 13 soru (ihlal 0) · Protokol B 2 soru (9, 14) = %13,3.","",
"## Üretim Notu","",
"- Karar kaynağında (GK m.6–7, GY m.27 ve m.586; tanım için GK m.3/5) yaklaşık 22 bağımsız ölçüm noktası tespit edildi; bu sette 15'i kullanıldı.",
"- Kalan boş ölçüm noktaları (yaklaşık 7): kararın tanımı ve bağlayıcı tarife/menşe bilgilerinin kapsama dahil olması (GK m.3/5), \"her kişi\" karar isteyebilir (GY m.27/1), lehe kararların Kanunun 7 nci maddesindeki hallerde değiştirilmesi (GY m.27/2), itiraz incelemesinde beyanname ve örnek unsurları, itiraz kararının tebliği, yükümlülüğe uymama halinin tek başına sorulması, zorunlu iptalin yürürlük anının tek başına sorulması. Bir sonraki Karar setinde en fazla 7 yeni soru üretilebilir; daha fazlası için türev izni gerekir.",
"- Protokol B hedefi %15–18 iken 15 soruluk sette 2 soru %13,3, 3 soru %20 eder; hedefe en yakın alt değer (2 soru) seçildi.",
"- Kaynakta \"otuz gün\" süreleri iş günü olarak nitelenmemiştir; sorularda bu ayrım çeldirici olarak kullanıldı.","",
"## HAFIZA GÜNCELLEMESİ","","```"]
md += [f"{q['id']} | Karar | {q['madde']} | {q['cek']} | {q['tip']} | {q['z']} | {q['harf']} | S1" for q in out]
md += ["Toplam: 15 satır (Karar: 15)","```","","---","**Gümrük Koçu - Ufuk Çetintaş**"]
open('GK_Karar_S1_15soru.md','w').write("\n".join(md)+"\n")
print(len(md))
