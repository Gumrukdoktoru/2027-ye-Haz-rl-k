"""Deneme 6-10 soru denetimi (Prompt 4 master + Prompt 3 + CLAUDE.md).
Kullanım: python3 kontrol.py batch_K01.py [batch_K02.py ...]
Her hata satırı '!!', her uyarı '??' ile başlar. Son satır: GENEL SONUÇ: TEMİZ / n hata."""
import sys, re, json, unicodedata, pathlib, collections, os
HERE = os.path.dirname(os.path.abspath(__file__))
PLAN = {p['id']: p for p in json.load(open(os.path.join(HERE, 'plan.json')))}

def tlower(s):
    return s.replace('İ', 'i').replace('I', 'ı').lower()
def norm(s):
    s = unicodedata.normalize('NFC', s)
    for a, b in (('’', "'"), ('‘', "'"), ('“', '"'), ('”', '"'), ('–', '-'), ('—', '-'), ('\xad', ''), (' ', ' ')):
        s = s.replace(a, b)
    return re.sub(r'\s+', ' ', tlower(s)).strip()
CORPUS = {f.name: norm(f.read_text()) for f in pathlib.Path(HERE, 'metin').glob('*.txt')}
ALLC = ' '.join(CORPUS.values())

STRIP = lambda s: re.sub(r'\[\[|\]\]|\*\*', '', s)
TIPLER = {'T1', 'T2', 'T1+T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10'}
ROMA = {'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5}
KOMBO = re.compile(r'^(?:Yalnız )?((?:I|II|III|IV|V|\d)(?:(?:, (?:I|II|III|IV|V|\d))* ve (?:I|II|III|IV|V|\d))?)\.?$')
MADDE = r'\b\d+\s*[’\']?\s*(inci|ıncı|üncü|uncu|nci|ncı|ncü|ncu|nin|nın|nün|nun)?\s*madde|madde(si(nin|ne)?)?\s*\d|\bfıkra|\bbendi?\b|\b\d{2,3}/\d'
YASAK = r'kaynak metne göre|verilen metinde|yukarıdaki kaynağa göre|kaynakta belirtildiği|verilen kaynağa göre|madde hükmüdür|temel düzenlemedir|madde bunu söylemektedir'
YAPAY = r'temel özellik|temel kural|kritik husus|en önemli düzenleme'
MUTLAK = r'\basla\b|her zaman|hiçbir şekilde|hiçbir surette'
KARAR_KALIP = re.compile(r'2009/15481 sayılı [“"]4458 sayılı Gümrük Kanununun Bazı Maddelerinin Uygulanması Hakkında Karar[”"]')
BIRIM = {'gün': 1, 'iş günü': 1.4, 'hafta': 7, 'ay': 30, 'yıl': 365, 'saat': 1 / 24}

def kombo(o):
    m = KOMBO.match(STRIP(o).strip())
    if not m: return None
    return [ROMA.get(x, int(x) if x.isdigit() else 0) for x in re.findall(r'IV|V|III|II|I|\d', m.group(1))]
def sayi(o):
    t = STRIP(o).strip().rstrip('.')
    m = re.fullmatch(r'(?:%\s*|Yüzde\s*)?(\d{1,3}(?:\.\d{3})+(?:,\d+)?|\d+(?:,\d+)?)\s*(.*)', t)
    if not m: return None
    v = float(m.group(1).replace('.', '').replace(',', '.'))
    u = m.group(2).strip().lower()
    for b, k in BIRIM.items():
        if u == b or u == b + 'dür' or u.startswith(b + ' '): return (('süre', v * k))
    return (u, v)
def bant(n):
    return '≤120' if n <= 120 else '120-350' if n <= 350 else '350-700' if n <= 700 else '>700'
def bant_ok(plan, n):
    lo, hi = {'≤120': (0, 150), '120-350': (100, 400), '350-700': (300, 800), '>700': (600, 99999)}[plan]
    return lo <= n <= hi
def sinif(opts):
    w = [len(STRIP(o).split()) for o in opts]
    if max(w) <= 4: return 'kısa'
    if min(w) >= 20: return 'uzun'
    return 'orta'
def kanit_ok(k):
    if k.strip().startswith('ÖZGÜN'): return True, ''
    bad = []
    for part in k.split('||'):
        if '|' not in part: return False, 'kanit "dosya.txt | alıntı" biçiminde olmalı'
        f, qt = [x.strip() for x in part.split('|', 1)]
        src = CORPUS.get(f)
        if src is None: return False, f'kanit dosyası yok: {f}'
        for p in re.split(r'\.\.\.|…|\[\.\.\.\]', norm(qt)):
            p = p.strip(' .;,:"\'')
            if len(p) > 12 and p not in src:
                bad.append(p[:70])
    return (not bad), ('kanıt alıntısı kaynakta birebir yok: ' + ' / '.join(bad)) if bad else ''
TOK = lambda s: {w for w in re.findall(r'\w+', tlower(s)) if len(w) > 3}
def jac(a, b): return len(a & b) / max(1, len(a | b))
HAF = []
hp = os.path.join(HERE, '../../sorular/hafiza/URETIM-HAFIZASI.md')
for l in open(hp):
    p = [x.strip() for x in l.split('|')]
    if len(p) >= 8 and re.match(r'(KAR|GMY)', p[0]) and not re.match(r'GMY(6|7|8|9|10)-', p[0]): HAF.append((p[0], p[3], TOK(p[3])))

def denetle(Q, ad):
    hata = 0
    for i, q in enumerate(Q, 1):
        E, W = [], []
        qid = q.get('id', f'#{i}')
        miss = [k for k in ('id', 'tip', 'z', 'madde', 'cek', 'kok', 'd', 'c', 'g', 'kanit') if k not in q]
        if miss: print(f'!! {qid}: eksik alan {miss}'); hata += 1; continue
        P = PLAN.get(qid) or q.get('_plan')
        if not P: print(f'!! {qid}: planda yok'); hata += 1; continue
        gk = P['blok'] == 'GK'
        sap = q.get('sapma', '')
        kok = q['kok'] if isinstance(q['kok'], list) else [q['kok']]
        koks = STRIP(' '.join(kok))
        opts = q.get('opts') or ([q['d']] + list(q['c']))
        if len(q['c']) != 4: E.append('4 çeldirici olmalı')
        if q.get('opts'):
            if sorted(q['opts']) != sorted([q['d']] + list(q['c'])): E.append('opts, d+c ile aynı 5 şıktan oluşmalı')
            elif 'ABCDE'[q['opts'].index(q['d'])] != P['harf']: E.append(f"sabit sıralı şıkta doğru cevap {'ABCDE'[q['opts'].index(q['d'])]} konumunda; planlanan harf {P['harf']}")
        if len(set(opts)) != 5: E.append('tekrarlı şık')
        if q['tip'] not in TIPLER: E.append('tip?')
        if not gk and q['tip'] != P['tip'] and not sap: E.append(f"tip planla uyuşmuyor (plan {P['tip']})")
        if q['z'] not in ({'OÜ', 'Z', 'O'} if gk else {'OÜ', 'Z'}): E.append('zorluk OÜ/Z olmalı')
        if len(q['cek'].split()) > 25: E.append('çekirdek >25 kelime')
        if re.search(MADDE, ' '.join(kok + opts), re.I): E.append('kökte/şıkta madde-fıkra-bent numarası')
        if re.search(r'\b(hepsi|hiçbiri|tümü)\b', tlower(' '.join(opts))): E.append('yasak şık: hepsi/hiçbiri/tümü')
        if re.search(YASAK, tlower(koks + ' ' + q['g'])): E.append('yasak ifade (kaynak metne göre vb.)')
        if re.search(YAPAY, tlower(koks)): E.append('yapay niteleme kökte')
        if re.search(MUTLAK, tlower(' '.join(opts))): W.append('şıkta mutlak ifade (asla/her zaman/hiçbir şekilde) — sırıtıyor mu?')
        nok = {o.strip().endswith('.') for o in opts}
        if len(nok) > 1: E.append('şık sonu nokta kullanımı 5 şıkta aynı olmalı')
        if not re.search(r'\(MD [^)]*\)\s*$', q['g'].strip()): E.append("açıklama '(MD …)' ile bitmeli")
        if re.search(r'\b[A-E]\)|\b[A-E] (seçeneği|şıkkı)', q['g']): E.append('açıklamada şık harfi var (harfi birleştirici yazar; şıkkı metniyle an)')
        ns = len(re.findall(r'[.!?](\s|$)', re.sub(r'\(MD [^)]*\)\s*$', '', q['g'])))
        if ns > 6: W.append(f'açıklama {ns} cümle (2–4 hedef)')
        ok, msg = kanit_ok(q['kanit'])
        if not ok and not (gk and P.get('ders') == 'Matematik'): E.append(msg)
        # kök kuralları
        neg = re.findall(r'\[\[([^\]]+)\]\]', ' '.join(kok))
        if q['tip'] in ('T1', 'T1+T2') and not neg: E.append('olumsuz kökte olumsuz kelime [[…]] ile işaretlenmeli')
        if neg and q['tip'] not in ('T1', 'T1+T2') and not gk: E.append('[[…]] yalnız T1 / T1+T2 kökünde')
        if not gk:
            if not re.search(r'Kanun|Yönetmeli|Tebliğ|Karar|mevzuat|Sözleşme', koks): E.append('kökte mevzuat adı yok')
            if 'Bazı Maddelerinin Uygulanması Hakkında Karar' in koks and not KARAR_KALIP.search(koks): E.append('Karar kökü kurum kalıbıyla yazılmalı: 2009/15481 sayılı "4458 sayılı Gümrük Kanununun Bazı Maddelerinin Uygulanması Hakkında Karar"a göre …')
            if re.match(r'\s*4458 sayılı(?! Gümrük Kanunu)', koks): E.append('kök "4458 sayılı" ile başlıyor ama Kanun değil')
            n = len(koks)
            if not bant_ok(P['bant'], n) and not sap: E.append(f"kök uzunluğu {n} karakter; planlanan bant {P['bant']}")
            sc = sinif(opts)
            if sc != P['sinif'] and not sap: E.append(f"şık sınıfı {sc}; planlanan {P['sinif']} (kısa: 5 şık ≤4 kelime, uzun: 5 şık ≥20 kelime)")
        # tip özel
        onc = [l for l in kok if re.match(r'^\s*(I|II|III|IV|V)\.\s', l)]
        if q['tip'] in ('T2', 'T1+T2'):
            if not 3 <= len(onc) <= 5: E.append('öncüllü soruda 3–5 öncül olmalı')
            ks = [kombo(o) for o in opts]
            if any(k is None for k in ks): E.append('öncüllü şıklar yalnız "Yalnız I", "I ve III", "I, II ve IV" biçiminde olmalı')
            else:
                if any(max(k) > len(onc) for k in ks): E.append('şıkta olmayan öncül numarası')
                if not q.get('opts'): E.append('öncüllü soruda opts (merdiven sırası) verilmeli')
                elif [ (len(k), k) for k in ks] != sorted((len(k), k) for k in ks): E.append('şık merdiveni artan değil (önce tekli, sonra ikili, üçlü…; aynı sayıda öncülde küçük numara önce)')
                dk = kombo(q['d'])
                if dk and sum(1 for k in ks if k != dk and len(set(k) ^ set(dk)) == 1) < 2: W.append('doğru kombinasyona tek öncül farkla yakın 2 kombinasyon yok')
        if q['tip'] == 'T10':
            rows = [l for l in kok if re.match(r'^\s*\d\.\s', l) or l.strip().startswith('|')]
            if len(rows) < 4: E.append('T10: en az 4 numaralı satır/tablo satırı olmalı')
        if q['tip'] == 'T5' and not re.search(r'…|\.{4,}', ' '.join(kok)): E.append('T5: kökte boşluk (……) yok')
        if q['tip'] == 'T6' and not re.search(r'[“"]', ' '.join(kok)): E.append('T6: tanım tırnak içinde verilmeli')
        if q['tip'] == 'T9' or (q['tip'] == 'T3' and not gk and P.get('sinif') == 'kısa'):
            sv = [sayi(o) for o in opts]
            if all(sv) and len({s[0] for s in sv}) == 1:
                if not q.get('opts'): E.append('sayısal şıklar artan sıralı opts ile verilmeli')
                elif [s[1] for s in sv] != sorted(s[1] for s in sv): E.append('sayısal şıklar artan sıralı değil')
            elif q['tip'] == 'T9': E.append('T9 şıkları sayısal ve aynı birimde olmalı')
            elif q['tip'] == 'T3' and not q.get('opts'): W.append('T3 kısa şıklar sayısal ayrıştırılamadı; artan sırada opts vermen önerilir')
        # uzunluk dengesi
        Lc = len(STRIP(q['d'])); Ld = [len(STRIP(x)) for x in q['c']]
        tol = max(0.10 * Lc, 3)
        bandn = sum(abs(l - Lc) <= tol for l in Ld)
        tz = bool(q.get('tuzak'))
        if not gk and tz != bool(P.get('tuzak')) and not sap: E.append(f"ters tuzak planla uyuşmuyor (plan {P.get('tuzak')})")
        if tz:
            s = sorted(Ld)
            if not (Lc > s[-1] and s[-1] >= 0.9 * Lc and s[-2] >= 0.9 * Lc): E.append(f'ters tuzak: doğru en uzun olmalı, 2. ve 3. en uzun ≥ %90 (doğru {Lc}, çeldiriciler {Ld})')
        else:
            longer = any(l > Lc for l in Ld) if Lc > 15 else any(l >= Lc for l in Ld)
            short = any(l <= Lc for l in Ld)
            if bandn < 2: E.append(f'uzunluk: doğru cevabın ±%10 bandında en az 2 çeldirici yok (doğru {Lc}, çeldiriciler {Ld})')
            if not longer: E.append(f'uzunluk: doğru cevaptan uzun çeldirici yok (doğru {Lc}, çeldiriciler {Ld})')
            if not short: E.append(f'uzunluk: doğru cevap tek başına en kısa (doğru {Lc}, çeldiriciler {Ld})')
        # tekrar
        t = TOK(q['cek'])
        for hid, hc, ht in HAF:
            if jac(t, ht) >= 0.45: W.append(f'hafızadaki {hid} ile benzer çekirdek: {hc[:90]}')
        for q2 in Q[:i - 1]:
            if jac(t, TOK(q2['cek'])) >= 0.45: W.append(f"aynı batch'te {q2.get('id')} ile benzer çekirdek")
        for e in E: print(f'!! {qid}: {e}')
        for w in W: print(f'?? {qid}: {w}')
        if E: hata += 1
    return hata

if __name__ == '__main__':
    toplam = 0; tumu = []
    for f in sys.argv[1:]:
        ns = {}; exec(open(f).read(), ns); Q = ns['Q']; tumu += Q
        print(f'=== {f}: {len(Q)} soru')
        toplam += denetle(Q, f)
    ids = [q.get('id') for q in tumu]
    dup = [k for k, v in collections.Counter(ids).items() if v > 1]
    if dup: print('!! tekrarlı id:', dup); toplam += 1
    C = collections.Counter
    print('Tip:', dict(sorted(C(q.get('tip') for q in tumu).items())), '| Zorluk:', dict(C(q.get('z') for q in tumu)))
    print('GENEL SONUÇ:', 'TEMİZ' if toplam == 0 else f'{toplam} hatalı soru')
