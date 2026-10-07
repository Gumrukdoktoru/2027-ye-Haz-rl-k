"""Deneme 3 çıktıları: Markdown ve PDF için HTML.

Kullanım: python3 cikti5.py set3.json notlar3.json CIKTI_ADI   (CIKTI_ADI.md ve CIKTI_ADI.html yazılır)
notlar3.json: {"baslik": ..., "bulunamayan": [...], "giremeyen": "...", "uretim": [...]}
"""
import html
import json
import re
import sys
from collections import Counter

L = 'ABCDE'
MARKA = 'Gümrük Koçu - Ufuk Çetintaş'


def onerme_mi(satir):
    return re.match(r'^(I|II|III|IV|V)\.\s', satir.strip())


def profil_satirlari(Q):
    C = Counter
    yk = C(q['yakinlik'] for q in Q)
    on = [q for q in Q if q['kalip'] == 'ÖNERMELİ']
    tz = C(t for q in Q for t in q['tuzak'])
    hf = C(q['harf'] for q in Q)
    n = len(Q)
    satir = [
        ('Kilit cümlesi madde metninden birebir', f"{yk['BİREBİR']} (%{round(100 * yk['BİREBİR'] / n)})"),
        ('Parafraz', f"{yk['PARAFRAZ']} (%{round(100 * yk['PARAFRAZ'] / n)})"),
        ('Çıkarım (tek adımlı)', f"{yk['ÇIKARIM']} (%{round(100 * yk['ÇIKARIM'] / n)})"),
        ('Olumsuz kök', f"{sum(q['olumsuz'] for q in Q)} (%{round(100 * sum(q['olumsuz'] for q in Q) / n)})"),
        ('Önermeli', f"{len(on)}; doğru kombinasyonlar: " + ', '.join(q['d'] for q in on)
         + f"; en kapsamlı şık doğru: {sum(bool(q.get('kapsamli')) for q in on)}; yanlıştır köklü: {sum(q['olumsuz'] for q in on)}"),
        ('Vaka, uygulama, hesap', str(sum(q['vaka'] for q in Q))),
        ('Tanımdan ad / addan tanım', str(sum(q['kalip'] in ('TANIM', 'KAVRAM') for q in Q))),
        ('Boşluk doldurma ve eşleştirme', str(sum(q['kalip'] in ('BOŞLUK', 'EŞLEŞTİRME') for q in Q))),
        ('Süre sorularında başlangıç anı ölçülen', str(sum(q['baslangic'] for q in Q))),
        ('Tuzak dağılımı', ', '.join(f'{k} {v}' for k, v in tz.most_common())),
        ('İkiz eksenler', ', '.join(str(e) for e in sorted({q['eksen'] for q in Q if q['eksen']}))
         + ' | ayna çiftler: ' + ', '.join(sorted({q['ayna'] for q in Q if q['ayna']}))),
        ('Aday profilleri (1–5)', ', '.join(f'{k}: {v}' for k, v in sorted(C(p for q in Q for p in q['profil']).items()))),
        ('Güncellik soruları', '; '.join(f"{q['no']}. soru ({q['guncellik']})" for q in Q if q['guncellik'])),
        ('Cevap harfi dağılımı', ' · '.join(f'{h} {hf[h]}' for h in L) + ' (art arda aynı harf yok)'),
    ]
    return satir


def md_yaz(Q, N, ad):
    m = [f'# {MARKA}', '', f"## {N['baslik']}", '',
         '| Alan | Değer |', '|---|---|',
         f'| Soru sayısı | {len(Q)} (gümrük mevzuatı, karışık konu) |',
         f'| Süre | {round(len(Q) * 1.5)} dakika |',
         '| Hazırlama kuralı | GMY Sınavı Mevzuat Sorusu Hazırlama Promptu (Prompt 5) |',
         f"| Çıkmış soru bilgi alanını karşılayan | {sum(1 for q in Q if q['cikmis'])} |", '',
         '# BÖLÜM A — SORU KİTAPÇIĞI', '']
    grup = None
    for q in Q:
        if q['grup'] != grup:
            grup = q['grup']
            m += [f'## {grup}', '']
        m += [f"**{q['no']}-** {q['kok'][0]}", '']
        for l in q['kok'][1:]:
            m.append(l + '  ')
        if len(q['kok']) > 1:
            m.append('')
        m += [f'{L[j]}) {o}  ' for j, o in enumerate(q['opts'])] + ['']
    m += ['## Cevap Anahtarı', '']
    for s in range(0, len(Q), 10):
        part = Q[s:s + 10]
        m += ['| ' + ' | '.join(str(q['no']) for q in part) + ' |', '|' + '---|' * len(part),
              '| ' + ' | '.join(q['harf'] for q in part) + ' |', '']
    m += ['# BÖLÜM B — CEVAPLI VE GEREKÇELİ SORULAR', '']
    for q in Q:
        m += [f"*{q['madde']}*", '', f"**{q['no']}-** {q['kok'][0]}", '']
        for l in q['kok'][1:]:
            m.append(l + '  ')
        if len(q['kok']) > 1:
            m.append('')
        m += [f'{L[j]}) {o}  ' for j, o in enumerate(q['opts'])]
        m += ['', f"**Doğru Cevap:** {q['harf']}  ", f"**Gerekçe:** {q['g']}", '']
    m += ['# SET RAPORU', '', '## Set profili', '', '| Ölçüt | Değer |', '|---|---|']
    m += [f'| {a} | {b} |' for a, b in profil_satirlari(Q)] + ['']
    m += ['## Kapsanan çıkmış soru noktaları', '']
    m += [f"- {q['no']}. soru ({q['konu']}): {q['cikmis']}" for q in Q if q['cikmis']] + ['']
    m += ['## Metinde karşılığı bulunamayan çıkmış soru noktaları', '']
    m += [f'- {x}' for x in N['bulunamayan']] + ['']
    m += ['## Sete giremeyen önemli soru alanları', '', N['giremeyen'], '']
    m += ['## Üretim notu', ''] + [f'- {x}' for x in N['uretim']] + ['']
    m += ['## HAFIZA GÜNCELLEMESİ', '', '```']
    m += [f"{q['id']} | {q['konu']} | {q['madde']} | {q['cek']} | {q['kalip']} | {q['z']} | {q['harf']} | GMY-S3" for q in Q]
    m += ['```', '', '---', f'**{MARKA}**']
    open(f'{ad}.md', 'w', encoding='utf-8').write('\n'.join(m) + '\n')


CSS = """
@page { size: A4; margin: 20mm 17mm 18mm 17mm;
  @top-left { content: 'Gümrük Koçu - Ufuk Çetintaş'; font: bold 7.5pt 'Liberation Sans', Arial; color: #1B3A5C; }
  @top-right { content: '%TITLE%'; font: 7.5pt 'Liberation Sans', Arial; color: #6b7785; }
  @bottom-right { content: counter(page) ' / ' counter(pages); font: 7.5pt 'Liberation Sans', Arial; color: #6b7785; } }
@page :first { @top-left { content: none; } @top-right { content: none; } @bottom-right { content: none; } }
@page kitapcik { margin: 19mm 14mm 17mm 14mm;
  @top-left { content: 'Gümrük Koçu - Ufuk Çetintaş'; font: bold 8pt 'Liberation Sans', Arial; color: #1B3A5C;
    border-bottom: .8pt solid #1B3A5C; vertical-align: bottom; padding-bottom: 1.5mm; }
  @top-center { content: '%TITLE%'; font: bold 9pt 'Liberation Serif', 'Times New Roman', serif; color: #000;
    border-bottom: .8pt solid #1B3A5C; vertical-align: bottom; padding-bottom: 1.5mm; }
  @top-right { content: 'Soru Kitapçığı'; font: 8pt 'Liberation Sans', Arial; color: #444;
    border-bottom: .8pt solid #1B3A5C; vertical-align: bottom; padding-bottom: 1.5mm; }
  @bottom-center { content: counter(page); font: bold 9pt 'Liberation Serif', serif; color: #000; }
  @bottom-right { content: none; } }
body { font-family: 'Liberation Sans', Arial, sans-serif; font-size: 9.6pt; line-height: 1.38; color: #1d1d1f; margin: 0; }
/* kapak: sınav kitapçığı kapağı */
.kapak { height: 250mm; width: calc(100% - 2mm); margin: 0 auto; border: 1.2pt solid #1B3A5C; padding: 12mm 14mm; box-sizing: border-box; display: flex;
  flex-direction: column; break-after: page; font-family: 'Liberation Serif', 'Times New Roman', serif; }
.kapak .marka { text-align: center; color: #B8860B; font: bold 11pt 'Liberation Sans', Arial; letter-spacing: .2em; }
.kapak .ad { text-align: center; font-size: 13pt; font-weight: bold; margin-top: 6mm; color: #1B3A5C; }
.kapak h1 { text-align: center; font-size: 24pt; margin: 3mm 0 1mm; color: #000; border: 0; padding: 0; break-before: auto; }
.kapak .tur { text-align: center; font-size: 12pt; margin-bottom: 9mm; }
.kapak .tur b { border: 1pt solid #000; padding: 1mm 4mm; }
.alanlar { border-collapse: collapse; width: 100%; font-size: 11pt; margin: 0 0 9mm; }
.alanlar td { border: 0; padding: 2.4mm 0; }
.alanlar td:first-child { width: 42mm; font-weight: bold; }
.alanlar td:last-child { border-bottom: .8pt dotted #555; }
.aciklama h3 { text-align: center; font-size: 11.5pt; margin: 0 0 3mm; letter-spacing: .08em; }
.aciklama ol { font-size: 10.5pt; line-height: 1.45; padding-left: 6mm; margin: 0; }
.aciklama li { margin: 0 0 1.6mm; font-size: 10.5pt; }
.kapak .alt { margin-top: auto; border-top: .8pt solid #1B3A5C; padding-top: 3mm; display: flex; justify-content: space-between;
  font: 9pt 'Liberation Sans', Arial; color: #333; }
.kapak .alt b { color: #1B3A5C; }
/* soru kitapçığı: çift sütun */
.kitapcik { page: kitapcik; break-before: page; column-count: 2; column-gap: 9mm; column-rule: .7pt solid #222;
  font-family: 'Liberation Serif', 'Times New Roman', serif; font-size: 10.3pt; line-height: 1.32; color: #000; }
.kitapcik .bas { column-span: all; text-align: center; font: bold 10.5pt 'Liberation Sans', Arial; color: #1B3A5C;
  border: .8pt solid #1B3A5C; padding: 1.6mm; margin: 0 0 5mm; letter-spacing: .05em; }
.kitapcik .soru { break-inside: avoid; margin: 0 0 6mm; }
.kitapcik .kok { margin: 0 0 1.6mm; font-weight: bold; text-align: justify; hyphens: auto; }
.kitapcik .kok .no { margin-right: 1mm; }
.kitapcik .veri { margin: 0 0 1.2mm 0; font-weight: normal; text-align: justify; }
.kitapcik .onc { margin: 0 0 1.2mm 0; padding-left: 6mm; text-indent: -6mm; font-weight: normal; text-align: justify; }
.kitapcik .sik { margin: 0 0 1mm 0; padding-left: 6mm; text-indent: -6mm; text-align: left; }
.kitapcik .sik b { display: inline-block; width: 6mm; text-indent: 0; }
.kitapcik .bitti { column-span: all; text-align: center; font: bold 11pt 'Liberation Serif', serif; margin-top: 4mm;
  padding-top: 3mm; border-top: .8pt solid #222; letter-spacing: .04em; }
/* cevap formu */
.form h1 { margin-bottom: 3mm; }
.form .not { font-size: 9pt; color: #333; margin: 0 0 4mm; }
.form-izgara { display: grid; grid-template-columns: repeat(5, auto); justify-content: space-between; border: .8pt solid #1B3A5C; padding: 3mm 3mm; width: calc(100% - 2mm); box-sizing: border-box; }
.form-sat { display: flex; align-items: center; gap: .9mm; padding: 1.3mm 0; font: 8.5pt 'Liberation Sans', Arial; }
.form-sat .n { width: 5mm; text-align: right; font-weight: bold; color: #1B3A5C; margin-right: .8mm; }
.form-sat .b { width: 4mm; height: 4mm; border: .7pt solid #333; border-radius: 50%; font-size: 6pt; display: flex;
  align-items: center; justify-content: center; color: #555; }
h1 { font-size: 16pt; color: #1B3A5C; border-bottom: 1.2mm solid #B8860B; padding-bottom: 1.5mm; margin: 0 0 4mm; break-before: page; }
h2 { font-size: 11.5pt; color: #1B3A5C; border-left: 1.4mm solid #B8860B; padding-left: 2.5mm; margin: 6mm 0 3mm; break-after: avoid; }
.soru { break-inside: avoid; margin: 0 0 4mm; }
.kok { margin: 0 0 1.5mm; }
.kok b { color: #1B3A5C; }
.onc { margin: 0 0 1mm 6mm; }
.sik { margin: 0 0 .8mm 6mm; padding-left: 5mm; text-indent: -5mm; }
.madde { font-style: italic; color: #B8860B; font-size: 9pt; margin: 0 0 1mm; }
.cevap { margin: 1.5mm 0 1mm; font-weight: bold; }
.cevap span { color: #1B3A5C; }
.gerekce { background: #f6f7f9; border-left: 1mm solid #1B3A5C; padding: 2mm 3mm; font-size: 8.9pt; line-height: 1.35; }
table { border-collapse: collapse; width: 100%; font-size: 8.8pt; margin: 2mm 0 4mm; }
th { background: #1B3A5C; color: #fff; padding: 1.5mm 2mm; text-align: center; }
td { padding: 1.4mm 2mm; border-bottom: 1px solid #dde2e8; vertical-align: top; }
.anahtar td { text-align: center; font-weight: bold; color: #1B3A5C; }
.rapor td:first-child { width: 38%; font-weight: bold; color: #10263d; }
ul { margin: 0 0 3mm; padding-left: 6mm; } li { margin: 0 0 1mm; font-size: 9.3pt; }
"""


def e(s):
    return html.escape(s, quote=False)


def soru_html(q, cevapli):
    """Cevaplı bölüm (tek sütun) için soru bloğu."""
    h = ['<div class="soru">']
    if cevapli:
        h.append(f'<div class="madde">{e(q["madde"])}</div>')
    h.append(f'<p class="kok"><b>{q["no"]}-</b> {e(q["kok"][0])}</p>')
    for l in q['kok'][1:]:
        h.append(f'<p class="onc">{e(l)}</p>' if onerme_mi(l) else f'<p class="kok">{e(l)}</p>')
    h += [f'<p class="sik">{L[j]}) {e(o)}</p>' for j, o in enumerate(q['opts'])]
    if cevapli:
        h.append(f'<p class="cevap">Doğru Cevap: <span>{q["harf"]}</span></p>')
        h.append(f'<div class="gerekce"><b>Gerekçe:</b> {e(q["g"])}</div>')
    h.append('</div>')
    return '\n'.join(h)


def kitapcik_soru(q):
    """Soru kitapçığı (çift sütun) için soru bloğu: kök kalın, öncül ve veri satırları normal, şıklar asılı girintili."""
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


def html_yaz(Q, N, ad):
    n = len(Q)
    sure = round(n * 1.5)
    b = [f'<!doctype html><html lang="tr"><head><meta charset="utf-8"><title>{e(N["baslik"])}</title>',
         f'<style>{CSS.replace("%TITLE%", N["baslik"])}</style></head><body>',
         '<section class="kapak">',
         '<div class="marka">GÜMRÜK KOÇU</div>',
         '<div class="ad">GÜMRÜK MÜŞAVİR YARDIMCILIĞI SINAVINA HAZIRLIK</div>',
         f'<h1>{e(N["baslik"]).upper()}</h1>',
         f'<div class="tur">Gümrük Mevzuatı · {n} Soru · {sure} Dakika &nbsp; <b>SORU KİTAPÇIĞI</b></div>',
         '<table class="alanlar"><tbody>',
         '<tr><td>ADI SOYADI</td><td></td></tr><tr><td>TARİH</td><td></td></tr>',
         '<tr><td>BAŞLAMA – BİTİŞ</td><td></td></tr><tr><td>DOĞRU SAYISI</td><td></td></tr>',
         '</tbody></table>',
         '<div class="aciklama"><h3>GENEL AÇIKLAMALAR</h3><ol>',
         f'<li>Bu kitapçıkta gümrük mevzuatına ilişkin {n} soru bulunmaktadır. Sınav süresi {sure} dakikadır.</li>',
         '<li>Her sorunun yalnız bir doğru cevabı vardır. Bir soru için birden fazla seçenek işaretlenmişse o soru yanlış cevaplanmış sayılır.</li>',
         '<li>Cevaplarınızı kitapçığın sonundaki cevap formuna işaretleyiniz.</li>',
         '<li>Değerlendirme yalnızca doğru cevap sayısı üzerinden yapılır; yanlış cevaplar dikkate alınmaz.</li>',
         '<li>Cevap anahtarı ve gerekçeli çözümler kitapçığın sonundadır; sınavı bitirmeden bu bölüme bakmayınız.</li>',
         '<li>Sorular 2021–2025 GMY sınavlarının soru mantığıyla, yürürlükteki mevzuat metinlerinden özgün olarak hazırlanmıştır.</li>',
         '</ol></div>',
         f'<div class="alt"><b>{MARKA}</b><span>Sınav başlayınca sayfayı çeviriniz.</span></div>',
         '</section>',
         '<section class="kitapcik">',
         f'<div class="bas">GÜMRÜK MEVZUATI — {n} SORU · {sure} DAKİKA</div>']
    b += [kitapcik_soru(q) for q in Q]
    b.append('<div class="bitti">TEST BİTTİ. CEVAPLARINIZI KONTROL EDİNİZ.</div></section>')
    # cevap formu
    b.append('<section class="form"><h1>Cevap Formu</h1>'
             '<p class="not">Her soru için yalnız bir seçeneği tamamen doldurunuz. Adı Soyadı: ______________________________</p>'
             '<div class="form-izgara">')
    satir_say = -(-n // 5)
    for kol in range(5):
        b.append('<div>')
        for i in range(kol * satir_say + 1, min(n, (kol + 1) * satir_say) + 1):
            b.append(f'<div class="form-sat"><span class="n">{i}</span>' + ''.join(f'<span class="b">{h}</span>' for h in L) + '</div>')
        b.append('</div>')
    b.append('</div></section>')
    b.append('<h1>Cevap Anahtarı</h1><table class="anahtar">')
    for s in range(0, n, 10):
        part = Q[s:s + 10]
        b.append('<tr>' + ''.join(f'<th>{q["no"]}</th>' for q in part) + '</tr>')
        b.append('<tr>' + ''.join(f'<td>{q["harf"]}</td>' for q in part) + '</tr>')
    b.append('</table><h1>Bölüm B — Cevaplı ve Gerekçeli Sorular</h1>')
    grup = None
    for q in Q:
        if q['grup'] != grup:
            grup = q['grup']
            b.append(f'<h2>{e(grup)}</h2>')
        b.append(soru_html(q, True))
    b.append('<h1>Set Raporu</h1><h2>Set profili</h2><table class="rapor"><tbody>')
    b.append(f'<tr><td>Kapsam</td><td>{n} gümrük mevzuatı sorusu; konular Bakanlık kitapçığı gibi bloklar hâlinde.</td></tr>')
    b.append('<tr><td>Hazırlama kuralı</td><td>GMY Sınavı Mevzuat Sorusu Hazırlama Promptu: kilit cümle madde metninden, '
             'çeldiriciler komşu hükümlerden, kökte mevzuat adı ve hükmün konusu.</td></tr>')
    b.append(f'<tr><td>Çıkmış soru bilgi alanını karşılayan</td><td>{sum(1 for q in Q if q["cikmis"])} soru '
             '(çıkmış soruların metni ve kurgusu kopyalanmadı)</td></tr>')
    b += [f'<tr><td>{e(a)}</td><td>{e(v)}</td></tr>' for a, v in profil_satirlari(Q)]
    b.append('</tbody></table><h2>Kapsanan çıkmış soru noktaları</h2><ul>')
    b += [f'<li>{q["no"]}. soru ({e(q["konu"])}): {e(q["cikmis"])}</li>' for q in Q if q['cikmis']]
    b.append('</ul><h2>Metinde karşılığı bulunamayan çıkmış soru noktaları</h2><ul>')
    b += [f'<li>{e(x)}</li>' for x in N['bulunamayan']]
    b.append(f'</ul><h2>Sete giremeyen önemli soru alanları</h2><p>{e(N["giremeyen"])}</p>')
    b.append('<h2>Üretim notu</h2><ul>' + ''.join(f'<li>{e(x)}</li>' for x in N['uretim']) + '</ul>')
    b.append('</body></html>')
    open(f'{ad}.html', 'w', encoding='utf-8').write('\n'.join(b))


if __name__ == '__main__':
    Q = json.load(open(sys.argv[1], encoding='utf-8'))
    N = json.load(open(sys.argv[2], encoding='utf-8'))
    md_yaz(Q, N, sys.argv[3])
    html_yaz(Q, N, sys.argv[3])
    print('md + html yazıldı:', sys.argv[3])
