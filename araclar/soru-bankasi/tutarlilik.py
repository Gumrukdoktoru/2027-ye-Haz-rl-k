"""Soru–cevap–gerekçe tutarlılık taraması (kitap.json üzerinde)."""
import json, re, sys
K = json.load(open(sys.argv[1], encoding='utf-8'))
L = 'ABCDE'
def n(s): return re.sub(r'\s+', ' ', s.replace('İ', 'i').replace('I', 'ı').lower().strip(' .;:'))
ROM = ['I', 'II', 'III', 'IV', 'V']
def rom_set(s):
    s = s.replace('Yalnız ', '')
    return set(re.findall(r'\b(IV|V|I{1,3})\b', s))
sorun = []
for b in K:
    for q in b['sorular']:
        qid, g, opts = q['id'], q['g'], q['opts']
        no = [n(o) for o in opts]
        # 1) gerekçedeki tırnaklı alıntılar şıklarla uyuşuyor mu
        for m in re.finditer(r"['‘\"“]([^'’\"”]{12,300})['’\"”]", g):
            t = n(m.group(1))
            if any(t == o for o in no): continue
            # şık gibi görünen ama hiçbir şıkla aynı olmayan alıntı: başka bir şıkla çok benzerse eski metin olabilir
            from difflib import SequenceMatcher
            best = max(SequenceMatcher(None, t, o).ratio() for o in no)
            if 0.75 <= best < 1.0:
                sorun.append((qid, 'ESKİ ALINTI', m.group(1)[:90]))
        # 2) önermeli: gerekçedeki doğru/yanlış etiketleri ile cevap kombinasyonu
        if q['kalip'] == 'ÖNERMELİ':
            dog, yan = set(), set()
            for r_, d_ in re.findall(r'\(\s*(IV|V|I{1,3})\s*[\.:,]?\s*(?:önerme(?:si)?\s*)?(doğru|yanlış)', g):
                (dog if d_ == 'doğru' else yan).add(r_)
            for r_, d_ in re.findall(r'\b(IV|V|I{1,3})\.?\s*(?:önerme(?:si)?\s*)?(doğrudur|yanlıştır|doğru;|yanlış;|doğru,|yanlış,|doğru\)|yanlış\))', g):
                (dog if d_.startswith('doğru') else yan).add(r_)
            onc = [l.split('.')[0].strip() for l in q['kok'] if re.match(r'^(I|II|III|IV|V)\.\s', l.strip())]
            ys = any(re.search(r'yanlış(tır|lar)', l) for l in q['kok'][-1:]) or 'hangileri yanlış' in ' '.join(q['kok'])
            cev = rom_set(q['d'])
            hedef = yan if ys else dog
            karsi = dog if ys else yan
            if dog & yan:
                sorun.append((qid, 'ÖNERME ÇELİŞKİ', f'doğru={sorted(dog)} yanlış={sorted(yan)}'))
            elif (hedef and not hedef <= cev) or (karsi & cev):
                sorun.append((qid, 'ÖNERME≠CEVAP', f"cevap={q['d']} gerekçe doğru={sorted(dog)} yanlış={sorted(yan)} kök={'yanlış' if ys else 'doğru'}"))
            elif len(onc) and len(dog | yan) == len(onc) and hedef != cev:
                sorun.append((qid, 'ÖNERME≠CEVAP(tam)', f"cevap={q['d']} hedef={sorted(hedef)}"))
        # 3) gerekçe başka soru numarasına atıf yapıyor mu
        if re.search(r'\b(soru|S)\s?\d{1,2}\b|ayna soru|önceki soru|sonraki soru', g):
            sorun.append((qid, 'İÇ ATIF', re.search(r'.{0,40}(\b(soru|S)\s?\d{1,2}\b|ayna soru|önceki soru|sonraki soru).{0,30}', g).group(0)))
        # 4) aynı şık iki kez
        if len(set(no)) < 5:
            sorun.append((qid, 'AYNI ŞIK', ''))
        # 5) gerekçe sonu harf
        if not re.search(rf"doğru cevap {q['harf']} seçeneğidir", g):
            sorun.append((qid, 'HARF', ''))
for s in sorun: print(*s, sep=' | ')
print(len(sorun), 'bulgu')
