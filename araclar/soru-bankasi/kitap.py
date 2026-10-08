"""GMY Soru Bankası kitabı: her konudan 20 soru, soru bölümleri çift sütun (test kâğıdı), çözümler tek sütun.

Kullanım:
  python3 kitap.py METIN_KLASORU BOLUMLER.json VERI_KLASORU CIKTI_ADI [SAYFA_HARITASI.json] [--cozumsuz]

VERI_KLASORU: sb_XX.py (soru verisi) ve sb_XX_rapor.json (bulunamayan, giremeyen, notlar) dosyaları.
CIKTI_ADI: CIKTI_ADI.html ve CIKTI_ADI.json yazılır; md dosyaları CIKTI_ADI_md/ klasörüne yazılır.
SAYFA_HARITASI: {"bölüm no": sayfa} — verilirse içindekiler sayfa numaralarıyla basılır (iki geçişli üretim).
--cozumsuz: çözümler ve set raporları basılmaz; testler + kitabın sonunda toplu cevap anahtarları (Ek A) + cevap formu (Ek B).
"""
import html
import json
import pathlib
import re
import sys
from collections import Counter

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent.parent / 'gmy-deneme3'))
from birlestir5 import harf_plan, harfle  # noqa: E402
from kontrol5 import denetle, yukle  # noqa: E402

L = 'ABCDE'
MARKA = 'Gümrük Koçu - Ufuk Çetintaş'
BASLIK = 'GMY Gümrük Mevzuatı Soru Bankası'


def css_str(s):
    return "'" + str(s).replace('\\', '\\\\').replace("'", "\\'") + "'"


SAG_SOL = ("@top-left { content: 'Gümrük Koçu'; font: bold 8pt 'Liberation Sans', Arial; color: #1B3A5C; BORDER }"
           "@top-right { content: 'Ufuk Çetintaş'; font: bold 8pt 'Liberation Sans', Arial; color: #1B3A5C; BORDER }")
CIZGI = 'border-bottom: .8pt solid #1B3A5C; vertical-align: bottom; padding-bottom: 1.5mm;'


def sayfa_kurallari(kitap, cozumsuz):
    """Her bölüm için adlandırılmış sayfa: test (t07) ve çözüm (c07); orta başlıkta konu adı."""
    k = []
    for no, baslik, *_ in kitap:
        k.append(f"@page t{no:02d} {{ margin: 19mm 13mm 16mm 13mm; " + SAG_SOL.replace('BORDER', CIZGI)
                 + f"@top-center {{ content: {css_str(baslik)}; font: bold 9pt 'Liberation Serif', serif; color: #000; {CIZGI} }}"
                 "@bottom-center { content: counter(page); font: bold 9pt 'Liberation Serif', serif; color: #000; } }")
        k.append(f"@page c{no:02d} {{ @top-center {{ content: {css_str(baslik + ' · Çözümler')}; "
                 "font: bold 8pt 'Liberation Sans', Arial; color: #333; } }")
    k.append(f"@page ekA {{ @top-center {{ content: {css_str('Cevap Anahtarları' if cozumsuz else 'Set Raporları')}; "
             "font: bold 8pt 'Liberation Sans', Arial; color: #333; } }")
    k.append("@page ekB { @top-center { content: 'Cevap Formu'; font: bold 8pt 'Liberation Sans', Arial; color: #333; } }")
    return '\n'.join(k)


def filigran_html():
    """Sayfa ortasında %10 opaklıkta logo (CAN'LI 7/24 Eğitim Merkezi); dosya yoksa boş."""
    import base64
    yol = pathlib.Path(__file__).resolve().parent / 'filigran_canli.png'
    if not yol.exists():
        return ''
    veri = base64.b64encode(yol.read_bytes()).decode()
    return f'<div class="filigran"><img src="data:image/png;base64,{veri}" alt=""></div>'


def tr_upper(s):
    """Türkçe büyük harf: i → İ, ı → I."""
    return s.replace('i', 'İ').replace('ı', 'I').upper()


def e(s):
    return html.escape(str(s), quote=False)


def onerme_mi(satir):
    return re.match(r'^(I|II|III|IV|V)\.\s', satir.strip())


def bolum_hazirla(no, Q):
    """Harfleri dağıtır, şıkları dizer, gerekçeye harfi yazar."""
    # aynı sabit harfli iki sıralı soru art arda gelirse ikincisini bir sonraki serbest soruyla yer değiştir
    def sabit(q):
        return q['siklar'].index(q['d']) if q.get('sirali') else None
    for i in range(len(Q) - 1):
        if sabit(Q[i]) is not None and sabit(Q[i]) == sabit(Q[i + 1]):
            j = next((j for j in range(i + 2, len(Q)) if sabit(Q[j]) is None), None)
            if j is not None:
                Q[i + 1], Q[j] = Q[j], Q[i + 1]
    plan = None
    for tohum in range(1, 20000):
        plan = harf_plan(Q, tohum + no * 100)
        if plan:
            break
    if not plan:
        raise SystemExit(f'Bölüm {no}: harf planı kurulamadı')
    for i, (q, h) in enumerate(zip(Q, plan), 1):
        q['no'], q['harf'], q['id'] = i, h, f'SB{no:02d}-{i:02d}'
        if q.get('sirali'):
            q['opts'] = list(q['siklar'])
        else:
            k = L.index(h)
            dist = list(q['c'])
            q['opts'] = [q['d'] if j == k else dist.pop(0) for j in range(5)]
        assert q['opts'][L.index(h)] == q['d']
        q['g'] = harfle(q)
        q.pop('_dosya', None)
    return Q


def profil(Q):
    n = len(Q)
    yk = Counter(q['yakinlik'] for q in Q)
    on = [q for q in Q if q['kalip'] == 'ÖNERMELİ']
    hf = Counter(q['harf'] for q in Q)
    return [
        ('Birebir / parafraz / çıkarım', f"{yk['BİREBİR']} / {yk['PARAFRAZ']} / {yk['ÇIKARIM']}"),
        ('Olumsuz kök', str(sum(q['olumsuz'] for q in Q))),
        ('Önermeli', f"{len(on)} ({', '.join(q['d'] for q in on) or '—'})"),
        ('Vaka, uygulama, hesap', str(sum(q['vaka'] for q in Q))),
        ('Tuzaklar', ', '.join(f'{k} {v}' for k, v in Counter(t for q in Q for t in q['tuzak']).most_common(6))),
        ('İkiz eksen / ayna', (', '.join(str(x) for x in sorted({q['eksen'] for q in Q if q['eksen']})) or '—')
         + ' / ' + (', '.join(sorted({q['ayna'] for q in Q if q['ayna']})) or '—')),
        ('Güncellik', '; '.join(q['guncellik'] for q in Q if q['guncellik']) or '—'),
        ('Çıkmış bilgi alanı karşılayan', str(sum(bool(q['cikmis']) for q in Q))),
        ('Cevap harfleri', ' · '.join(f'{h} {hf[h]}' for h in L)),
    ]


CSS = """
@page { size: A4; margin: 19mm 15mm 17mm 15mm;
  @top-left { content: 'Gümrük Koçu'; font: bold 8pt 'Liberation Sans', Arial; color: #1B3A5C; }
  @top-center { content: 'GMY Gümrük Mevzuatı Soru Bankası'; font: bold 8pt 'Liberation Sans', Arial; color: #333; }
  @top-right { content: 'Ufuk Çetintaş'; font: bold 8pt 'Liberation Sans', Arial; color: #1B3A5C; }
  @bottom-center { content: counter(page); font: bold 8.5pt 'Liberation Sans', Arial; color: #333; } }
@page :first { @top-left { content: none; } @top-center { content: none; } @top-right { content: none; } @bottom-center { content: none; } }
.filigran { position: fixed; top: 0; left: 0; width: 100%; height: 100%; display: flex; align-items: center;
  justify-content: center; z-index: -1; pointer-events: none; }
.filigran img { width: 130mm; opacity: .10; }
body { font-family: 'Liberation Sans', Arial, sans-serif; font-size: 9.4pt; line-height: 1.36; color: #1d1d1f; margin: 0; }
h1 { font-size: 16pt; color: #1B3A5C; border-bottom: 1.2mm solid #B8860B; padding-bottom: 1.5mm; margin: 0 0 4mm; break-before: page; }
h2 { font-size: 11.5pt; color: #1B3A5C; border-left: 1.4mm solid #B8860B; padding-left: 2.5mm; margin: 5mm 0 3mm; break-after: avoid; }
/* kapak */
.kapak { height: 252mm; width: calc(100% - 2mm); margin: 0 auto; box-sizing: border-box; display: flex; flex-direction: column;
  break-after: page; border: 1.2pt solid #1B3A5C; }
.kapak .bant { background: #1B3A5C; color: #fff; padding: 34mm 14mm 14mm; border-bottom: 3mm solid #B8860B; }
.kapak .ust { color: #B8860B; font: bold 10pt 'Liberation Sans', Arial; letter-spacing: .18em; margin-bottom: 7mm; }
.kapak h1 { font-size: 30pt; line-height: 1.12; margin: 0 0 4mm; color: #fff; border: 0; padding: 0; break-before: auto; }
.kapak .alt { font-size: 13pt; color: #dbe4ee; }
.kapak .orta { padding: 12mm 14mm 0; font-size: 10.5pt; color: #333; }
.kapak .rakam { display: flex; gap: 4mm; padding: 8mm 14mm 0; }
.kapak .rakam div { flex: 1; border-top: 1mm solid #B8860B; padding-top: 2mm; font-size: 8.5pt; color: #555; }
.kapak .rakam b { display: block; font-size: 20pt; color: #1B3A5C; }
.kapak .imza { margin-top: auto; padding: 4mm 14mm; border-top: .8pt solid #ccc; color: #1B3A5C; font-weight: bold; font-size: 12pt; }
/* içindekiler */
.icindekiler { width: 100%; border-collapse: collapse; }
.icindekiler td { padding: 1.1mm 2mm; border-bottom: .6pt dotted #bbb; font-size: 9.2pt; }
.icindekiler td.no { width: 14mm; white-space: nowrap; font-weight: bold; color: #1B3A5C; }
.icindekiler td.sf { width: 14mm; text-align: right; font-weight: bold; }
.icindekiler td.kaynak { color: #666; font-size: 8pt; }
/* test bölümü: çift sütun */
.test { page: test; break-before: page; column-count: 2; column-gap: 9mm; column-rule: .7pt solid #222;
  font-family: 'Liberation Serif', 'Times New Roman', serif; font-size: 10.2pt; line-height: 1.3; color: #000; }
.test .bas { column-span: all; border: .8pt solid #1B3A5C; margin: 0 0 4.5mm; padding: 2mm 3mm; display: flex;
  justify-content: space-between; align-items: baseline; font-family: 'Liberation Sans', Arial; }
.test .bas b { font-size: 11.5pt; color: #1B3A5C; letter-spacing: .02em; }
.test .bas span { font-size: 8.5pt; color: #333; }
.test .soru { break-inside: avoid; margin: 0 0 5.5mm; }
.test .kok { margin: 0 0 1.5mm; font-weight: bold; text-align: left; }
.test .kok .no { margin-right: 1mm; }
.test .veri { margin: 0 0 1.1mm; font-weight: normal; text-align: left; }
.test .onc { margin: 0 0 1.1mm; padding-left: 6mm; text-indent: -6mm; font-weight: normal; text-align: left; }
.test .sik { margin: 0 0 .9mm; padding-left: 6mm; text-indent: -6mm; }
.test .sik b { display: inline-block; width: 6mm; text-indent: 0; }
.test .bitti { column-span: all; text-align: center; font: bold 10.5pt 'Liberation Serif', serif; margin-top: 3mm;
  padding-top: 2.5mm; border-top: .8pt solid #222; }
/* çözümler: tek sütun */
.cozum { page: cozum; break-before: page; }
.cozum h2.ust { font-size: 13pt; border-left: 0; padding-left: 0; border-bottom: 1mm solid #B8860B; padding-bottom: 1.2mm; margin-top: 0; }
.anahtar { border-collapse: collapse; width: 100%; margin: 1mm 0 4mm; font-size: 8.8pt; }
.anahtar th { background: #1B3A5C; color: #fff; padding: 1.2mm; text-align: center; }
.anahtar td { text-align: center; font-weight: bold; color: #1B3A5C; padding: 1.2mm; border-bottom: 1px solid #dde2e8; }
.cozum .soru { break-inside: avoid; margin: 0 0 2.6mm; }
.cozum .cbas { margin: 0 0 .8mm; display: flex; align-items: baseline; gap: 2mm; }
.cozum .cbas .no { color: #1B3A5C; font-size: 10pt; min-width: 7mm; }
.cozum .cbas .harf { background: #1B3A5C; color: #fff; font-weight: bold; padding: 0 1.6mm; border-radius: .8mm; font-size: 9pt; }
.cozum .cbas .dsik { font-weight: bold; flex: 1; }
.cozum .cbas .madde { font-style: italic; color: #8a6508; font-size: 8pt; max-width: 62mm; text-align: right; }
.cozum .gerekce { border-left: .8mm solid #c9d3de; padding: .4mm 0 .4mm 2.6mm; margin-left: 9mm; font-size: 8.7pt; line-height: 1.34; }
/* ekler */
.rapor { border-collapse: collapse; width: 100%; font-size: 8.4pt; margin: 0 0 3mm; }
.rapor td { padding: .9mm 2mm; border-bottom: 1px solid #e3e6ea; vertical-align: top; }
.rapor td:first-child { width: 34%; font-weight: bold; color: #10263d; }
.ekrapor { break-inside: avoid; margin-bottom: 4mm; }
.ekanahtar { break-inside: avoid; margin-bottom: 2.5mm; }
.ekanahtar h3 { font-size: 9.5pt; color: #1B3A5C; margin: 0 0 .8mm; }
.ekanahtar .anahtar { margin: 0; }
.ekrapor h3 { font-size: 10pt; color: #1B3A5C; margin: 0 0 1mm; }
.ekrapor p, .ekrapor li { font-size: 8.4pt; margin: 0 0 .8mm; }
.ekrapor ul { margin: 0 0 1mm; padding-left: 5mm; }
.form-izgara { display: grid; grid-template-columns: repeat(4, auto); justify-content: space-between; border: .8pt solid #1B3A5C;
  padding: 3mm; width: calc(100% - 2mm); box-sizing: border-box; }
.form-sat { display: flex; align-items: center; gap: 1mm; padding: 1.4mm 0; font: 9pt 'Liberation Sans', Arial; }
.form-sat .n { width: 6mm; text-align: right; font-weight: bold; color: #1B3A5C; margin-right: 1mm; }
.form-sat .b { width: 4.4mm; height: 4.4mm; border: .7pt solid #333; border-radius: 50%; font-size: 6.3pt; display: flex;
  align-items: center; justify-content: center; color: #555; }
ul { padding-left: 6mm; } li { margin: 0 0 1mm; }
"""


def test_soru(q):
    h = ['<div class="soru">', f'<p class="kok"><span class="no">{q["no"]}-</span>{e(q["kok"][0])}</p>']
    for l in q['kok'][1:]:
        if onerme_mi(l):
            h.append(f'<p class="onc">{e(l)}</p>')
        elif l.lstrip().startswith(('-', '•')):
            h.append(f'<p class="veri">{e(l)}</p>')
        else:
            h.append(f'<p class="kok">{e(l)}</p>')
    h += [f'<p class="sik"><b>{L[j]})</b>{e(o)}</p>' for j, o in enumerate(q['opts'])]
    h.append('</div>')
    return '\n'.join(h)


def cozum_soru(q):
    """Çözüm: soru tekrar basılmaz; madde, doğru şık ve gerekçe."""
    return '\n'.join([
        '<div class="soru">',
        f'<p class="cbas"><b class="no">{q["no"]}.</b><span class="harf">{q["harf"]}</span>'
        f'<span class="dsik">{e(q["d"])}</span><span class="madde">{e(q["madde"])}</span></p>',
        f'<div class="gerekce">{e(q["g"])}</div>', '</div>'])


def md_bolum(no, baslik, kaynak, Q, R):
    m = [f'# {MARKA}', '', f'## Bölüm {no:02d} — {baslik}', '', f'Kaynak: {kaynak} · {len(Q)} soru', '',
         '### Sorular', '']
    for q in Q:
        m += [f"**{q['no']}-** {q['kok'][0]}", '']
        m += [l + '  ' for l in q['kok'][1:]] + ([''] if len(q['kok']) > 1 else [])
        m += [f'{L[j]}) {o}  ' for j, o in enumerate(q['opts'])] + ['']
    m += ['### Cevap Anahtarı', '', '| ' + ' | '.join(str(q['no']) for q in Q) + ' |', '|' + '---|' * len(Q),
          '| ' + ' | '.join(q['harf'] for q in Q) + ' |', '', '### Çözümler', '']
    for q in Q:
        m += [f"*{q['madde']}*", '', f"**{q['no']}-** {q['kok'][0]}", '']
        m += [l + '  ' for l in q['kok'][1:]] + ([''] if len(q['kok']) > 1 else [])
        m += [f'{L[j]}) {o}  ' for j, o in enumerate(q['opts'])]
        m += ['', f"**Doğru Cevap:** {q['harf']}  ", f"**Gerekçe:** {q['g']}", '']
    m += ['### Set Raporu', '', '| Ölçüt | Değer |', '|---|---|'] + [f'| {a} | {b} |' for a, b in profil(Q)] + ['']
    if R.get('bulunamayan'):
        m += ['Metinde karşılığı bulunamayan çıkmış soru noktaları:', ''] + [f'- {x}' for x in R['bulunamayan']] + ['']
    if R.get('giremeyen'):
        m += [f"Sete giremeyen alanlar: {R['giremeyen']}", '']
    m += ['---', f'**{MARKA}**']
    return '\n'.join(m) + '\n'


def main():
    cozumsuz = '--cozumsuz' in sys.argv
    arg = [a for a in sys.argv[1:] if not a.startswith('--')]
    metin, bolum_yolu, veri, ad = arg[:4]
    harita = json.load(open(arg[4])) if len(arg) > 4 else {}
    veri = pathlib.Path(veri)
    bolumler = json.load(open(bolum_yolu, encoding='utf-8'))
    kitap = []
    for no, baslik, kaynak in bolumler:
        yol = veri / f'sb_{no:02d}.py'
        if not yol.exists():
            continue
        Q = yukle([str(yol)])
        hata = denetle(Q, metin)
        if hata:
            raise SystemExit(f'Bölüm {no}: {hata} soru denetimden geçmedi')
        rp = veri / f'sb_{no:02d}_rapor.json'
        R = json.load(open(rp, encoding='utf-8')) if rp.exists() else {}
        kitap.append((no, baslik, kaynak, bolum_hazirla(no, Q), R))
    toplam = sum(len(b[3]) for b in kitap)
    # Markdown (bölüm başına)
    if not cozumsuz:
        mdk = pathlib.Path(f'{ad}_md')
        mdk.mkdir(exist_ok=True)
        for no, baslik, kaynak, Q, R in kitap:
            (mdk / f'Bolum_{no:02d}.md').write_text(md_bolum(no, baslik, kaynak, Q, R), encoding='utf-8')
    # HTML
    b = [f'<!doctype html><html lang="tr"><head><meta charset="utf-8"><title>{BASLIK}</title><style>{CSS}\n{sayfa_kurallari(kitap, cozumsuz)}</style></head><body>',
         filigran_html(),
         '<section class="kapak"><div class="bant"><div class="ust">GÜMRÜK MÜŞAVİR YARDIMCILIĞI SINAVINA HAZIRLIK</div>',
         f'<h1>{BASLIK}</h1><div class="alt">Konu konu {toplam} soru · {len(kitap)} bölüm · test kâğıdı düzeninde, '
         + ('cevap anahtarlı</div></div>' if cozumsuz else 'cevap anahtarlı ve gerekçeli çözümlü</div></div>'),
         '<div class="orta">Her bölüm bir konunun mevzuat metninden hazırlanmış bir testtir; kaynağı dar birkaç konu dışında testler 20 sorudur. Sorular 2021–2025 '
         'GMY sınavlarının soru mantığıyla yazılmıştır: kilit cümle madde metninden, çeldiriciler komşu hükümlerden. '
         'Çıkmış soruların metni ve kurgusu kopyalanmamıştır.</div>',
         f'<div class="rakam"><div><b>{toplam}</b>soru</div><div><b>{len(kitap)}</b>konu bölümü</div>'
         '<div><b>1,5</b>dakika / soru</div>'
         + (f'<div><b>{len(kitap)}</b>cevap anahtarı</div></div>' if cozumsuz else '<div><b>%100</b>gerekçeli çözüm</div></div>'),
         f'<div class="imza">{MARKA}</div></section>']
    # Kullanım ve içindekiler
    if cozumsuz:
        b.append('<h1>Kitap Nasıl Kullanılır?</h1><ul>'
                 '<li>Her bölüm bir testtir. Test sayfaları sınav kitapçığı gibi çift sütunludur; soru başına 1,5 dakika ayırın (20 soru için 30 dakika).</li>'
                 '<li>Cevaplarınızı Ek B\'deki cevap formuna işaretleyin.</li>'
                 '<li>Testi bitirince cevaplarınızı Ek A\'daki cevap anahtarlarıyla kontrol edin. Anahtarlar, test sırasında göz ucuyla görülmesin diye kitabın sonunda toplanmıştır.</li></ul>')
    else:
        b.append('<h1>Kitap Nasıl Kullanılır?</h1><ul>'
                 '<li>Her bölüm bir testle başlar. Test sayfaları sınav kitapçığı gibi çift sütunludur; soru başına 1,5 dakika ayırın (20 soru için 30 dakika).</li>'
                 '<li>Cevaplarınızı Ek B\'deki cevap formuna işaretleyin, sonra bölümün cevap anahtarıyla kontrol edin.</li>'
                 '<li>Çözümler testin hemen arkasındadır ve tek sütundur. Her çözümde doğru şık, dayanak madde ve gerekçe vardır. Gerekçe, '
                 'en güçlü çeldiricinin mevzuattaki yerini de söyler: yanlış yaptığınız soruda neyi neyle karıştırdığınızı görürsünüz.</li>'
                 '<li>Her bölümün set profili ve kaynakta karşılığı bulunamayan çıkmış soru noktaları Ek A\'dadır.</li></ul>')
    b.append('<h2>İçindekiler</h2><table class="icindekiler"><tbody>')
    for no, baslik, kaynak, Q, R in kitap:
        sf = harita.get(str(no), '')
        b.append(f'<tr><td class="no">{no:02d}</td><td>{e(baslik)}</td><td class="sf">{sf}</td></tr>')
    sfA, sfB = harita.get('EkA', ''), harita.get('EkB', '')
    b.append(f'<tr><td class="no">Ek A</td><td>{"Cevap anahtarları" if cozumsuz else "Set raporları"}</td><td class="sf">{sfA}</td></tr>'
             f'<tr><td class="no">Ek B</td><td>Cevap formu</td><td class="sf">{sfB}</td></tr></tbody></table>')
    for no, baslik, kaynak, Q, R in kitap:
        b.append(f'<section class="test" style="page: t{no:02d}">')
        b.append(f'<div class="bas"><b>BÖLÜM {no:02d} · {e(tr_upper(baslik))}</b><span>{len(Q)} soru · {round(len(Q) * 1.5)} dakika</span></div>')
        b += [test_soru(q) for q in Q]
        b.append('<div class="bitti">TEST BİTTİ. CEVAPLARINIZI KONTROL EDİNİZ.</div></section>')
        if cozumsuz:
            continue
        b.append(f'<section class="cozum" style="page: c{no:02d}"><h2 class="ust">Bölüm {no:02d} · {e(baslik)} — Cevap Anahtarı ve Çözümler</h2>')
        b.append('<table class="anahtar"><tr>' + ''.join(f'<th>{q["no"]}</th>' for q in Q) + '</tr><tr>'
                 + ''.join(f'<td>{q["harf"]}</td>' for q in Q) + '</tr></table>')
        b += [cozum_soru(q) for q in Q]
        b.append('</section>')
    if cozumsuz:
        # Ek A: toplu cevap anahtarları
        b.append('<section style="page: ekA"><h1>Ek A — Cevap Anahtarları</h1>')
        for no, baslik, kaynak, Q, R in kitap:
            b.append(f'<div class="ekanahtar"><h3>Bölüm {no:02d} · {e(baslik)}</h3>'
                     '<table class="anahtar"><tr>' + ''.join(f'<th>{q["no"]}</th>' for q in Q) + '</tr><tr>'
                     + ''.join(f'<td>{q["harf"]}</td>' for q in Q) + '</tr></table></div>')
        b.append('</section>')
    # Ek A: set raporları
    if not cozumsuz:
        b.append('<section style="page: ekA"><h1>Ek A — Set Raporları</h1>')
    for no, baslik, kaynak, Q, R in ([] if cozumsuz else kitap):
        b.append(f'<div class="ekrapor"><h3>Bölüm {no:02d} · {e(baslik)}</h3><table class="rapor"><tbody>')
        b.append(f'<tr><td>Kaynak</td><td>{e(kaynak.replace(".txt", ""))}</td></tr>')
        b += [f'<tr><td>{e(a)}</td><td>{e(v)}</td></tr>' for a, v in profil(Q)]
        b.append('</tbody></table>')
        if R.get('bulunamayan'):
            b.append('<p><b>Metinde karşılığı bulunamayan çıkmış soru noktaları:</b></p><ul>'
                     + ''.join(f'<li>{e(x)}</li>' for x in R['bulunamayan']) + '</ul>')
        if R.get('giremeyen'):
            b.append(f'<p><b>Sete giremeyen alanlar:</b> {e(R["giremeyen"])}</p>')
        b.append('</div>')
    if not cozumsuz:
        b.append('</section>')
    # Ek B: cevap formu
    b.append('<section style="page: ekB"><h1>Ek B — Cevap Formu</h1><p>Bu sayfayı çoğaltarak her test için kullanabilirsiniz. Bölüm: ______  '
             'Adı Soyadı: ____________________  Doğru sayısı: ______</p><div class="form-izgara">')
    for kol in range(4):
        b.append('<div>')
        for i in range(kol * 5 + 1, kol * 5 + 6):
            b.append(f'<div class="form-sat"><span class="n">{i}</span>' + ''.join(f'<span class="b">{h}</span>' for h in L) + '</div>')
        b.append('</div>')
    b.append('</div></section></body></html>')
    pathlib.Path(f'{ad}.html').write_text('\n'.join(b), encoding='utf-8')
    json.dump([{'no': no, 'baslik': baslik, 'kaynak': kaynak, 'sorular': Q, 'rapor': R} for no, baslik, kaynak, Q, R in kitap],
              open(f'{ad}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print(f'{len(kitap)} bölüm, {toplam} soru → {ad}.html')


if __name__ == '__main__':
    main()
