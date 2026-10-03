import json, collections
Q=json.load(open('set2.json')); L='ABCDE'; C=collections.Counter
notlar=json.load(open('notlar2.json'))
mdlabel=lambda q: q['madde']
md=["# Gümrük Koçu - Ufuk Çetintaş","","## GMY Deneme Sınavı 2","",
"| Alan | Değer |","|---|---|","| Set | GMY Deneme 2 (S2) |","| Model | 2021–2025 GMY sınavları (çıkmış soru bilgi alanları + kurum dili) |","| Soru sayısı | 100 (20 genel kültür + 80 gümrük mevzuatı) |","| Süre | 150 dakika |",
f"| Zorluk | ÇK {C(q['z'] for q in Q)['ÇK']} · K {C(q['z'] for q in Q)['K']} · O {C(q['z'] for q in Q)['O']} · Z {C(q['z'] for q in Q)['Z']} · ÇZ {C(q['z'] for q in Q)['ÇZ']} |",
f"| Çıkmış bilgi alanı karşılayan soru | {sum(1 for q in Q if q.get('cikmis'))} |","",
"# BÖLÜM A — SORU KİTAPÇIĞI",""]
for q in Q:
    if q['no']==1: md+=["## Genel Kültür (1–20)",""]
    if q['no']==21: md+=["## Gümrük Mevzuatı (21–100)",""]
    md.append(f"**{q['no']}-** "+q['kok'][0]); md.append("")
    for l in q['kok'][1:]: md.append(l+"  ")
    if len(q['kok'])>1: md.append("")
    md += [f"{L[j]}) {o}  " for j,o in enumerate(q['opts'])]; md.append("")
md += ["## Cevap Anahtarı",""]
for s0 in range(0,100,20):
    part=Q[s0:s0+20]
    md += ["| "+" | ".join(str(q['no']) for q in part)+" |","|"+"---|"*20,"| "+" | ".join(q['harf'] for q in part)+" |",""]
md += ["# BÖLÜM B — CEVAPLI VE GEREKÇELİ SORULAR",""]
for q in Q:
    md += [f"*{mdlabel(q)}*","",f"**{q['no']}-** "+q['kok'][0],""]
    for l in q['kok'][1:]: md.append(l+"  ")
    if len(q['kok'])>1: md.append("")
    md += [f"{L[j]}) {o}  " for j,o in enumerate(q['opts'])]
    md += ["",f"**Doğru Cevap:** {q['harf']}  ",f"**Gerekçe:** {q['g']}",""]
md += ["## Dağılım",""]
def tab(t,cnt,order): return [f"**{t}**","","| "+" | ".join(order)+" |","|"+"---|"*len(order),"| "+" | ".join(str(cnt.get(o,0)) for o in order)+" |",""]
md += tab("Doğru cevap harfi",C(q['harf'] for q in Q),list(L))
md += tab("Zorluk",C(q['z'] for q in Q),["ÇK","K","O","Z","ÇZ"])
kal=C(q['kalip'] for q in Q); md += tab("Soru kalıbı",kal,[k for k,_ in kal.most_common()])
kon=C(q['konu'] for q in Q); md += ["**Konu**","","| Konu | Soru |","|---|---|"]+[f"| {k} | {v} |" for k,v in kon.most_common()]+[""]
md += ["## Üretim Notu",""]+[f"- {x}" for x in notlar]+[""]
md += ["## HAFIZA GÜNCELLEMESİ","","```"]
md += [f"{q['id']} | {q['konu']} | {q['madde']} | {q['cek']} | {q['kalip']} | {q['z']} | {q['harf']} | GMY-S2" for q in Q]
md += ["Toplam: 215 satır (Karar 15 + GMY-S1 100 + GMY-S2 100)","```","","---","**Gümrük Koçu - Ufuk Çetintaş**"]
open('GK_GMY_Deneme2_100soru.md','w').write("\n".join(md)+"\n"); print('md ok')
