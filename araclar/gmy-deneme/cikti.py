import json, collections
Q=json.load(open('set100.json')); L='ABCDE'; C=collections.Counter
dg=lambda s: s.replace('GK ','Gümrük Kanunu ').replace('GY ','Gümrük Yönetmeliği ')
md=["# Gümrük Koçu - Ufuk Çetintaş","","## Set Kartı","","| Alan | Değer |","|---|---|",
"| Set | GMY-2025 Benzeri Deneme (S1) |","| Model | 2025 Gümrük Müşavir Yardımcılığı Sınavı (B kitapçığı) konu dağılımı |","| Sınıf | GMY |","| Soru sayısı | 100 (20 genel kültür + 80 gümrük mevzuatı) |","| Önerilen süre | 150 dakika |",
"| Zorluk | Dengeli (10-20-40-20-10) → ÇK 10 · K 20 · O 40 · Z 20 · ÇZ 10 |","| Hafızadaki önceki soru | 15 (Karar) |","| Bu setle toplam | 115 |","",
"## Sorular",""]
bol={1:"### Bölüm 1 — Genel Kültür (1–20)",21:"### Bölüm 2 — Gümrük Mevzuatı (21–100)"}
for q in Q:
    if q['no'] in bol: md+= [bol[q['no']],""]
    md.append(f"**{q['no']}.** "+q['kok'][0]); md.append("")
    for l in q['kok'][1:]: md.append(l+"  ")
    if len(q['kok'])>1: md.append("")
    md += [f"{L[j]}) {o}  " for j,o in enumerate(q['opts'])]; md.append("")
md += ["## Cevap Anahtarı",""]
for s in range(0,100,20):
    part=Q[s:s+20]
    md += ["| "+" | ".join(str(q['no']) for q in part)+" |","|"+"---|"*20,"| "+" | ".join(q['harf'] for q in part)+" |",""]
md += ["## Çözümler",""]
for q in Q:
    md += [f"**{q['no']}.**","",f"- **Doğru cevap:** {q['harf']}",f"- **Gerekçe:** {q['g']}",f"- **Tuzak nokta şudur:** {q['t']}",f"- **Yasal Dayanak:** {dg(q['madde'])}",""]
def tab(title,cnt,order):
    return [f"**{title}**","","| "+" | ".join(order)+" |","|"+"---|"*len(order),"| "+" | ".join(str(cnt.get(o,0)) for o in order)+" |",""]
md += ["## Dağılım Tabloları",""]
tips=sorted(C(q['tip'] for q in Q), key=lambda t:-C(q['tip'] for q in Q)[t])
md += tab("Tip",C(q['tip'] for q in Q),tips)
md += tab("Zorluk",C(q['z'] for q in Q),["ÇK","K","O","Z","ÇZ"])
md += tab("Doğru cevap harfi",C(q['harf'] for q in Q),list(L))
tz=["İdare/makam karıştırma","Rejim sınıflandırma","Tanım çiftleri","Belge eşleştirme","Süre kaydırma","Eşik/oran kaydırma","İstisna atlatma"]
md += tab("Tuzak kategorisi",C(q['tuzak'] for q in Q),tz)
kon=C(q['konu'] for q in Q); md += ["**Konu**","","| Konu | Soru |","|---|---|"]+[f"| {k} | {v} |" for k,v in kon.most_common()]+[""]
pb=[str(q['no']) for q in Q if q.get('protB')]
md += [f"**Şık uzunluğu:** Protokol A {100-len(pb)} soru (ihlal 0) · Protokol B {len(pb)} soru (%{len(pb)}): {', '.join(pb)}.",""]
md += ["## Üretim Notu",""]+[f"- {x}" for x in json.load(open('notlar.json'))]+[""]
md += ["## HAFIZA GÜNCELLEMESİ","","```"]
md += [f"{q['id']} | {q['konu']} | {q['madde']} | {q['cek']} | {q['tip']} | {q['z']} | {q['harf']} | GMY-S1" for q in Q]
md += ["Toplam: 115 satır (Karar 15 + GMY deneme 100)","```","","---","**Gümrük Koçu - Ufuk Çetintaş**"]
open('GK_GMY2025_Deneme_S1_100soru.md','w').write("\n".join(md)+"\n"); print('md ok', len(md))
