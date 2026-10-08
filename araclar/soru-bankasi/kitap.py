"""Ortak Mevzuat Soru Bankası kitabı: her konudan 20 soru, soru bölümleri çift sütun (test kâğıdı), çözümler tek sütun.

Kullanım:
  python3 kitap.py METIN_KLASORU BOLUMLER.json VERI_KLASORU CIKTI_ADI [SAYFA_HARITASI.json] [--cozumsuz]

VERI_KLASORU: sb_XX.py (soru verisi) ve sb_XX_rapor.json (bulunamayan, giremeyen, notlar) dosyaları.
CIKTI_ADI: CIKTI_ADI.html ve CIKTI_ADI.json yazılır; md dosyaları CIKTI_ADI_md/ klasörüne yazılır.
SAYFA_HARITASI: {"bölüm no": test sayfası, "c<no>": çözüm sayfası, "EkA", "EkB"} — verilirse içindekiler sayfa
  numaralarıyla basılır (iki geçişli üretim).
Kitap: ön kapak, bu kitap hakkında, içindekiler (tıklanabilir), bölümler, ekler, arka kapak (arka_kapak_reklam.jpg).
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
BASLIK = 'Ortak Mevzuat Soru Bankası'


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
    k.append("@page icindekiler { @top-center { content: 'İçindekiler'; font: bold 8pt 'Liberation Sans', Arial; color: #333; } }")
    bos = '@top-left { content: none; } @top-center { content: none; } @top-right { content: none; } @bottom-center { content: none; }'
    k.append(f'@page onkapak {{ margin: 0; {bos} }}')
    k.append(f'@page arkakapak {{ margin: 0; {bos} }}')
    return '\n'.join(k)


def gomulu(dosya, tur):
    """Klasördeki görseli data URI olarak döndürür; dosya yoksa boş."""
    import base64
    yol = pathlib.Path(__file__).resolve().parent / dosya
    if not yol.exists():
        return ''
    return f'data:{tur};base64,' + base64.b64encode(yol.read_bytes()).decode()


def filigran_html():
    """Sayfa ortasında %10 opaklıkta logo (CAN'LI 7/24 Eğitim Merkezi); dosya yoksa boş."""
    logo = gomulu('filigran_canli.png', 'image/png')
    return f'<div class="filigran"><img src="{logo}" alt=""></div>' if logo else ''


def on_kapak(toplam, bolum_sayisi, cozumsuz):
    """Tam sayfa ön kapak: lacivert zemin, başlık, optik form deseni, altta logo ve marka."""
    # süs: optik cevap formu satırları (kitaptaki hiçbir cevap anahtarıyla ilgisi yok)
    desen = ''.join(
        '<div class="s"><i>' + str(i + 1) + '</i>'
        + ''.join(f'<span class="{"d" if h == dolu else ""}">{h}</span>' for h in L) + '</div>'
        for i, dolu in enumerate('CAEBDBECAD'))
    logo = gomulu('filigran_canli.png', 'image/png')
    return ''.join([
        '<section class="onkapak"><div class="ok-desen">', desen, '</div><div class="ok-ic">',
        '<div class="ok-etiket">GÜMRÜK MÜŞAVİR YARDIMCILIĞI SINAVINA HAZIRLIK</div>',
        '<div class="ok-buyuk">Ortak<br>Mevzuat</div><div class="ok-baslik">Soru Bankası</div><div class="ok-cizgi"></div>',
        f'<p class="ok-alt">Gümrük mevzuatı · {bolum_sayisi} konu · {toplam} soru<br>Test kâğıdı düzeninde, '
        + ('cevap anahtarlı' if cozumsuz else 'gerekçeli çözümlü') + '</p>',
        f'<div class="ok-rozet">{"CEVAP ANAHTARLI SÜRÜM" if cozumsuz else "ÇÖZÜMLÜ SÜRÜM"}</div></div>',
        f'<div class="ok-rakam"><div><b>{toplam}</b>SORU</div><div><b>{bolum_sayisi}</b>KONU</div>'
        + ('<div><b>1,5 dk</b>SORU BAŞINA SÜRE</div></div>' if cozumsuz else '<div><b>%100</b>GEREKÇELİ ÇÖZÜM</div></div>'),
        '<div class="ok-taban">' + (f'<img src="{logo}" alt="">' if logo else '<span></span>'),
        '<div class="ok-marka"><b>Gümrük Koçu</b><span>Ufuk Çetintaş</span></div></div></section>'])


def arka_kapak():
    """Tam sayfa arka kapak: kullanıcının verdiği ilan (arka_kapak_reklam.jpg) ve altta marka."""
    ilan = gomulu('arka_kapak_reklam.jpg', 'image/jpeg')
    logo = gomulu('filigran_canli.png', 'image/png')
    return ''.join([
        '<section class="arkakapak">', f'<img class="ak-ilan" src="{ilan}" alt="">' if ilan else '',
        '<div class="ak-taban">', f'<div class="ak-logo"><img src="{logo}" alt=""></div>' if logo else '',
        f'<div class="ak-yazi"><b>{BASLIK}</b><span>Gümrük Koçu · Ufuk Çetintaş</span></div></div></section>'])


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
  @top-center { content: 'Ortak Mevzuat Soru Bankası'; font: bold 8pt 'Liberation Sans', Arial; color: #333; }
  @top-right { content: 'Ufuk Çetintaş'; font: bold 8pt 'Liberation Sans', Arial; color: #1B3A5C; }
  @bottom-center { content: counter(page); font: bold 8.5pt 'Liberation Sans', Arial; color: #333; } }
@page :first { @top-left { content: none; } @top-center { content: none; } @top-right { content: none; } @bottom-center { content: none; } }
.filigran { position: fixed; top: 0; left: 0; width: 100%; height: 100%; display: flex; align-items: center;
  justify-content: center; z-index: -1; pointer-events: none; }
.filigran img { width: 130mm; opacity: .10; }
body { font-family: 'Liberation Sans', Arial, sans-serif; font-size: 9.4pt; line-height: 1.36; color: #1d1d1f; margin: 0; }
h1 { font-size: 16pt; color: #1B3A5C; border-bottom: 1.2mm solid #B8860B; padding-bottom: 1.5mm; margin: 0 0 4mm; break-before: page; }
h2 { font-size: 11.5pt; color: #1B3A5C; border-left: 1.4mm solid #B8860B; padding-left: 2.5mm; margin: 5mm 0 3mm; break-after: avoid; }
/* ön kapak (tam sayfa) */
.onkapak { page: onkapak; width: 210mm; height: 297mm; overflow: hidden; position: relative; break-after: page;
  display: flex; flex-direction: column; color: #fff; font-family: 'Inter', 'Liberation Sans', Arial;
  background: #10263d linear-gradient(165deg, #1F4268 0%, #10263d 62%); }
.ok-ic { padding: 30mm 20mm 0; position: relative; }
.ok-etiket { font: 600 9.5pt 'Inter'; letter-spacing: .22em; color: #D9A83E; }
.ok-buyuk { font: 900 56pt/1.02 'Inter Display', 'Inter'; color: #D9A83E; margin: 16mm 0 4mm; letter-spacing: -.01em; }
.ok-baslik { font: 800 35pt/1.08 'Inter Display', 'Inter'; color: #fff; }
.ok-cizgi { width: 42mm; height: 1.6mm; background: #D9A83E; margin: 10mm 0 7mm; }
.ok-alt { font: 400 13pt/1.5 'Inter'; color: #d7e0ea; margin: 0; }
.ok-rozet { display: inline-block; margin-top: 10mm; border: 1pt solid #D9A83E; color: #D9A83E; font: 700 9pt 'Inter';
  letter-spacing: .16em; padding: 2mm 4mm; border-radius: 1mm; }
.ok-desen { position: absolute; right: 20mm; top: 60mm; display: flex; flex-direction: column; gap: 3.4mm; }
.ok-desen .s { display: flex; gap: 2.4mm; align-items: center; }
.ok-desen .s i { font: normal 600 7pt 'Inter'; color: #6f86a0; width: 5mm; text-align: right; margin-right: 1mm; }
.ok-desen .s span { width: 6.4mm; height: 6.4mm; border-radius: 50%; border: .7pt solid #4d6a8a; font: 600 6.5pt 'Inter';
  color: #6f86a0; display: flex; align-items: center; justify-content: center; box-sizing: border-box; }
.ok-desen .s span.d { background: #D9A83E; border-color: #D9A83E; color: #10263d; }
.ok-rakam { margin-top: auto; display: flex; padding: 0 20mm 12mm; }
.ok-rakam div { flex: 1; border-left: .8mm solid #D9A83E; padding-left: 3.5mm; font: 600 8pt 'Inter'; color: #b9c6d4; letter-spacing: .08em; }
.ok-rakam b { display: block; font: 800 22pt/1.15 'Inter Display', 'Inter'; color: #fff; letter-spacing: 0; }
.ok-taban { background: #fff; height: 50mm; display: flex; align-items: center; justify-content: space-between; padding: 0 20mm;
  border-top: 2.2mm solid #D9A83E; }
.ok-taban img { height: 28mm; }
.ok-marka { text-align: right; color: #1B3A5C; }
.ok-marka b { display: block; font: 800 18pt 'Inter Display', 'Inter'; }
.ok-marka span { font: 600 12pt 'Inter'; color: #B8860B; letter-spacing: .05em; }
/* arka kapak (tam sayfa) */
.arkakapak { page: arkakapak; break-before: page; width: 210mm; height: 297mm; overflow: hidden; display: flex;
  flex-direction: column; background: #182747; font-family: 'Inter', 'Liberation Sans', Arial; }
.ak-ilan { width: 210mm; display: block; }
.ak-taban { flex: 1; display: flex; align-items: center; justify-content: center; gap: 9mm; border-top: 1.2mm solid #D9A83E; }
.ak-logo { background: #fff; border-radius: 2.5mm; padding: 3.5mm 5mm; }
.ak-logo img { height: 17mm; display: block; }
.ak-yazi b { display: block; font: 800 14pt 'Inter Display', 'Inter'; color: #fff; }
.ak-yazi span { font: 600 11pt 'Inter'; color: #D9A83E; letter-spacing: .05em; }
/* bu kitap hakkında */
.tanitim .giris { font-size: 10.5pt; line-height: 1.5; color: #333; margin: 0 0 6mm; }
.tanitim .rakam { display: flex; gap: 4mm; margin: 0 0 7mm; }
.tanitim .rakam div { flex: 1; border-top: 1mm solid #B8860B; padding-top: 2mm; font-size: 8.5pt; color: #555; }
.tanitim .rakam b { display: block; font-size: 20pt; color: #1B3A5C; }
.tanitim li { font-size: 10pt; line-height: 1.45; margin-bottom: 2mm; }
.tanitim .imza { margin-top: 10mm; padding-top: 3mm; border-top: .8pt solid #ccc; color: #1B3A5C; font-weight: bold; font-size: 11pt; }
/* içindekiler */
.icindekiler { page: icindekiler; break-before: page; }
.icindekiler h1 { break-before: auto; }
.ic-sat { display: flex; align-items: baseline; padding: 1.25mm 0; font-size: 9.6pt; break-inside: avoid; }
.ic-sat a { color: inherit; text-decoration: none; }
.ic-no { width: 9mm; flex: none; font-weight: bold; color: #fff; background: #1B3A5C; text-align: center; border-radius: .8mm;
  font-size: 8.4pt; padding: .3mm 0; margin-right: 3mm; }
.ic-no.ek { background: #B8860B; }
.ic-ad { flex: none; max-width: 128mm; color: #1d1d1f; }
.ic-nokta { flex: 1; border-bottom: 1pt dotted #9aa7b5; margin: 0 2mm; min-width: 4mm; }
.ic-sf { width: 13mm; flex: none; text-align: right; font-weight: bold; color: #1B3A5C; }
.ic-bas { display: flex; justify-content: flex-end; font: bold 7.5pt 'Liberation Sans', Arial; color: #777; letter-spacing: .06em;
  border-bottom: .8pt solid #1B3A5C; padding-bottom: 1mm; margin-bottom: 1mm; }
.ic-bas span { width: 13mm; text-align: right; }
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
         filigran_html(), on_kapak(toplam, len(kitap), cozumsuz)]
    # Bu kitap hakkında ve kullanım
    b.append('<section class="tanitim"><h1>Bu Kitap Hakkında</h1>'
             '<p class="giris">Her bölüm bir konunun mevzuat metninden hazırlanmış bir testtir; kaynağı dar birkaç konu dışında testler 20 sorudur. '
             'Sorular 2021–2025 GMY sınavlarının soru mantığıyla yazılmıştır: kilit cümle madde metninden, çeldiriciler komşu hükümlerden. '
             'Soru tiplerinin dağılımı (klasik, olumsuz kök, önermeli, tanım, vaka, boşluk, hesap, eşleştirme) bu sınavlardaki gümrük sorularına göre ayarlanmıştır. '
             'Çıkmış soruların metni ve kurgusu kopyalanmamıştır.</p>'
             f'<div class="rakam"><div><b>{toplam}</b>soru</div><div><b>{len(kitap)}</b>konu bölümü</div>'
             '<div><b>1,5</b>dakika / soru</div>'
             + (f'<div><b>{len(kitap)}</b>cevap anahtarı</div></div>' if cozumsuz else '<div><b>%100</b>gerekçeli çözüm</div></div>')
             + '<h2>Kitap Nasıl Kullanılır?</h2><ul>')
    if cozumsuz:
        b.append('<li>Her bölüm bir testtir. Test sayfaları sınav kitapçığı gibi çift sütunludur; soru başına 1,5 dakika ayırın (20 soru için 30 dakika).</li>'
                 '<li>Cevaplarınızı Ek B\'deki cevap formuna işaretleyin.</li>'
                 '<li>Testi bitirince cevaplarınızı Ek A\'daki cevap anahtarlarıyla kontrol edin. Anahtarlar, test sırasında göz ucuyla görülmesin diye kitabın sonunda toplanmıştır.</li>')
    else:
        b.append('<li>Her bölüm bir testle başlar. Test sayfaları sınav kitapçığı gibi çift sütunludur; soru başına 1,5 dakika ayırın (20 soru için 30 dakika).</li>'
                 '<li>Cevaplarınızı Ek B\'deki cevap formuna işaretleyin, sonra bölümün cevap anahtarıyla kontrol edin.</li>'
                 '<li>Çözümler testin hemen arkasındadır ve tek sütundur. Her çözümde doğru şık, dayanak madde ve gerekçe vardır. Gerekçe, '
                 'en güçlü çeldiricinin mevzuattaki yerini de söyler: yanlış yaptığınız soruda neyi neyle karıştırdığınızı görürsünüz.</li>'
                 '<li>Her bölümün set profili ve kaynakta karşılığı bulunamayan çıkmış soru noktaları Ek A\'dadır.</li>')
    b.append(f'<li>İçindekiler sayfasındaki satırlar tıklanabilir; PDF\'te ilgili teste{"" if cozumsuz else " ya da çözüme"} doğrudan gidilir.</li></ul>'
             f'<div class="imza">{MARKA}</div></section>')
    # İçindekiler: bölüm başına test (ve çözüm) sayfası; satırlar iç bağlantı
    def ic_sat(etiket, ad, hedef, hucreler, ek=False):
        """hedef: başlığın bağlantısı; hucreler: (bağlantı, harita anahtarı) — ikisi de boşsa boş hücre."""
        sf = ''.join(f'<span class="ic-sf"><a href="#{h}">{harita.get(k, "")}</a></span>' if h else '<span class="ic-sf"></span>'
                     for h, k in hucreler)
        return (f'<div class="ic-sat"><span class="ic-no{" ek" if ek else ""}">{etiket}</span>'
                f'<span class="ic-ad"><a href="#{hedef}">{e(ad)}</a></span><span class="ic-nokta"></span>{sf}</div>')
    b.append('<section class="icindekiler"><h1>İçindekiler</h1><div class="ic-bas">'
             + ('<span>SAYFA</span>' if cozumsuz else '<span>TEST</span><span>ÇÖZÜM</span>') + '</div>')
    for no, baslik, kaynak, Q, R in kitap:
        hucre = [(f'b{no:02d}', str(no))] + ([] if cozumsuz else [(f'c{no:02d}', f'c{no}')])
        b.append(ic_sat(f'{no:02d}', baslik, f'b{no:02d}', hucre))
    for ek, ek_ad in (('A', 'Cevap anahtarları' if cozumsuz else 'Set raporları'), ('B', 'Cevap formu')):
        hucre = ([] if cozumsuz else [('', '')]) + [(f'ek{ek}', f'Ek{ek}')]
        b.append(ic_sat(f'Ek {ek}', ek_ad, f'ek{ek}', hucre, ek=True))
    b.append('</section>')
    for no, baslik, kaynak, Q, R in kitap:
        b.append(f'<section class="test" id="b{no:02d}" style="page: t{no:02d}">')
        b.append(f'<div class="bas"><b>BÖLÜM {no:02d} · {e(tr_upper(baslik))}</b><span>{len(Q)} soru · {round(len(Q) * 1.5)} dakika</span></div>')
        b += [test_soru(q) for q in Q]
        b.append('<div class="bitti">TEST BİTTİ. CEVAPLARINIZI KONTROL EDİNİZ.</div></section>')
        if cozumsuz:
            continue
        b.append(f'<section class="cozum" id="c{no:02d}" style="page: c{no:02d}"><h2 class="ust">Bölüm {no:02d} · {e(baslik)} — Cevap Anahtarı ve Çözümler</h2>')
        b.append('<table class="anahtar"><tr>' + ''.join(f'<th>{q["no"]}</th>' for q in Q) + '</tr><tr>'
                 + ''.join(f'<td>{q["harf"]}</td>' for q in Q) + '</tr></table>')
        b += [cozum_soru(q) for q in Q]
        b.append('</section>')
    if cozumsuz:
        # Ek A: toplu cevap anahtarları
        b.append('<section id="ekA" style="page: ekA"><h1>Ek A — Cevap Anahtarları</h1>')
        for no, baslik, kaynak, Q, R in kitap:
            b.append(f'<div class="ekanahtar"><h3>Bölüm {no:02d} · {e(baslik)}</h3>'
                     '<table class="anahtar"><tr>' + ''.join(f'<th>{q["no"]}</th>' for q in Q) + '</tr><tr>'
                     + ''.join(f'<td>{q["harf"]}</td>' for q in Q) + '</tr></table></div>')
        b.append('</section>')
    # Ek A: set raporları
    if not cozumsuz:
        b.append('<section id="ekA" style="page: ekA"><h1>Ek A — Set Raporları</h1>')
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
    b.append('<section id="ekB" style="page: ekB"><h1>Ek B — Cevap Formu</h1><p>Bu sayfayı çoğaltarak her test için kullanabilirsiniz. Bölüm: ______  '
             'Adı Soyadı: ____________________  Doğru sayısı: ______</p><div class="form-izgara">')
    for kol in range(4):
        b.append('<div>')
        for i in range(kol * 5 + 1, kol * 5 + 6):
            b.append(f'<div class="form-sat"><span class="n">{i}</span>' + ''.join(f'<span class="b">{h}</span>' for h in L) + '</div>')
        b.append('</div>')
    b.append('</div></section>')
    b.append(arka_kapak())
    b.append('</body></html>')
    pathlib.Path(f'{ad}.html').write_text('\n'.join(b), encoding='utf-8')
    json.dump([{'no': no, 'baslik': baslik, 'kaynak': kaynak, 'sorular': Q, 'rapor': R} for no, baslik, kaynak, Q, R in kitap],
              open(f'{ad}.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
    print(f'{len(kitap)} bölüm, {toplam} soru → {ad}.html')


if __name__ == '__main__':
    main()
