# GMY kitapçıklarını (pdftohtml -xml çıktısı) soru/şık/resmî cevap olarak ayrıştırır.
# Resmî cevap: 2021–2024 kitapçıklarında doğru şık kırmızı (#ff0000) yazılmıştır.
# Kullanım: python3 ayristir.py <xml_klasoru> <cikti_klasoru>
import re, sys, json, html, pathlib, collections
XML, OUT = pathlib.Path(sys.argv[1]), pathlib.Path(sys.argv[2]); OUT.mkdir(parents=True, exist_ok=True)
KIR = '⟦', '⟧'   # kırmızı metin işaretleri ⟦ ⟧
ALTBILGI = re.compile(r'sayfaya geçiniz|MÜŞAVİR YARDIMCILI|Kitapçığı\s*$|TEST BİTTİ', re.I)
KUYRUK = re.compile(r'\s*(GÜMRÜK MÜŞAVİR\b.*|YARDIMCILI\S*.*|TEST BİTTİ.*|[AB] Kitapçığı.*)$')
TXT = re.compile(r'<text top="(-?\d+)" left="(-?\d+)" width="(\d+)" height="(\d+)" font="(\d+)">(.*?)</text>', re.S)

def satirlar(xml):
    fonts = {m.group(1): m.group(2).lower() for m in re.finditer(r'<fontspec id="(\d+)"[^>]*color="(#[0-9a-fA-F]+)"', xml)}
    out = []
    sayfalar = re.split(r'<page ', xml)[1:]
    for page in sayfalar[1:-1]:                     # ön ve arka kapak (talimatlar) atlanır
        W = int(re.search(r'width="(\d+)"', page).group(1)); H = int(re.search(r'height="(\d+)"', page).group(1))
        items = []
        for m in TXT.finditer(page):
            top, left, w, h, f, t = int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), m.group(5), m.group(6)
            t = html.unescape(re.sub(r'<[^>]+>', '', t))
            if not t.strip() or top < 75 or top > H - 80: continue      # başlık / sayfa altı
            if ALTBILGI.search(t): continue
            if re.fullmatch(r'\s*\d{1,2}\s*', t) and top > H * 0.85 and abs(left + w / 2 - W / 2) < 40: continue  # sayfa no
            col = 0 if left < W / 2 - 10 else 1
            red = fonts.get(f) == '#ff0000'
            items.append((col, top, left, t, red))
        items.sort(key=lambda z: (z[0], z[1], z[2]))
        lines = []
        for col, top, left, t, red in items:     # aynı satır: ilk öğenin üst kenarına 7 px'ten yakın
            if lines and lines[-1]['col'] == col and abs(lines[-1]['top'] - top) <= 7:
                lines[-1]['parts'].append((left, t, red))
            else:
                lines.append({'col': col, 'top': top, 'parts': [(left, t, red)]})
        for L in lines:
            s = ''
            for left, t, red in sorted(L['parts']):
                s += (KIR[0] + t + KIR[1]) if red else t
            out.append(s.rstrip())
    return out

SORU = re.compile(r'^\s*(\d{1,3})\s*[.\-]\s*(.*)$')
SIK = re.compile(r'(?:(?<=^)|(?<=\s)|(?<=' + KIR[0] + r'))([A-E])\s*\)')

def ayir(lines, yil):
    Q, cur, beklenen = [], None, 1
    for l in lines:
        plain = l.replace(KIR[0], '').replace(KIR[1], '')
        m = SORU.match(plain)
        if m and int(m.group(1)) == beklenen:
            cur = {'yil': yil, 'no': beklenen, 'satirlar': [l[l.find(m.group(1)) + len(m.group(1)) + 1:] if False else l]}
            Q.append(cur); beklenen += 1
        elif cur: cur['satirlar'].append(l)
    for q in Q:
        metin = '\n'.join(q.pop('satirlar'))
        metin = re.sub(r'^\s*' + KIR[0] + r'?\s*' + str(q['no']) + r'\s*[.\-]\s*', '', metin, 1)
        # şıkları bul (A)…E) sırayla)
        poz, bas = [], 0
        for h in 'ABCDE':
            mm = None
            for c in re.finditer(r'(?<![A-Za-zÇĞİÖŞÜçğıöşü(])(' + h + r')\s*\)', metin[bas:]):
                mm = c; break
            if not mm: break
            poz.append((h, bas + mm.start(1))); bas = bas + mm.end()
        if len(poz) == 5:
            kok = metin[:poz[0][1]].rstrip(' ' + KIR[0])
            sik = {}
            for i, (h, p) in enumerate(poz):
                son = poz[i + 1][1] if i < 4 else len(metin)
                sik[h] = metin[p + 2:son].strip()
        else:
            kok, sik = metin, {}
        temiz = lambda s: re.sub(r'\s+', ' ', s.replace(KIR[0], '').replace(KIR[1], '')).strip()
        kirmizi = [h for h, s in sik.items() if re.search(KIR[0] + r'[^' + KIR[1] + r']*\S', s) or
                   re.search(KIR[0] + r'\s*' + h + r'\s*\)', metin)]
        # şık harfi kırmızıysa (⟦C) ⟧) şık gövdesinde işaret kalmayabilir
        for h in 'ABCDE':
            if re.search(KIR[0] + r'\s*' + h + r'\s*\)', metin) and h not in kirmizi: kirmizi.append(h)
        q['kok'] = re.sub(r'[ \t]+', ' ', kok.replace(KIR[0], '').replace(KIR[1], '')).strip()
        q['siklar'] = {h: KUYRUK.sub('', temiz(s)).strip() for h, s in sik.items()}
        q['kirmizi'] = sorted(set(kirmizi))
        q['kirmizi_kokte'] = KIR[0] in kok and bool(re.search(KIR[0] + r'[^' + KIR[1] + r']*\w', kok))
    return Q

for f in sorted(XML.glob('20*.xml')):
    yil = f.stem
    Q = ayir(satirlar(f.read_text(encoding='utf-8', errors='replace')), yil)
    json.dump(Q, open(OUT / f'{yil}_sorular.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    c = collections.Counter(len(q['kirmizi']) for q in Q)
    eksik = [q['no'] for q in Q if len(q['siklar']) != 5]
    print(yil, 'soru:', len(Q), '| 5 şıklı olmayan:', eksik, '| kırmızı şık sayısı dağılımı:', dict(c),
          '| tek olmayan:', [q['no'] for q in Q if len(q['kirmizi']) != 1][:20])
