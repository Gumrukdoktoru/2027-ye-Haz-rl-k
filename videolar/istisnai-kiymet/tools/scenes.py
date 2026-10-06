#!/usr/bin/env python3
"""İstisnai kıymetle beyan — sahne yerleşimleri (taslak ve video ortak kaynağı).

Her sahne, son (yerleşmiş) halini 1920×1080 piksel koordinatlarla tanımlar. Aynı tanım
hem taslak sayfasında (storyboard.html, hareketsiz) hem de sahne dosyalarında
(compositions/frames/*.html, hareketli) kullanılır; böylece video taslağı birebir giydirir.
"""
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W, H = 1920, 1080
RED, DARK, BG, LIGHT = "#D8000F", "#1C1410", "#FFFFFF", "#F5F2EF"
SHADOW = "2px 2px 0 rgba(28,20,16,.25), 4px 4px 0 rgba(28,20,16,.2), 6px 6px 0 rgba(28,20,16,.15)"
N_FRAMES = 12

FONT_FACES = open(os.path.join(ROOT, "assets/fonts.css")).read().replace("url('fonts/", "url('assets/fonts/")


# ------------------------------------------------------------------ glyphs (missing from fonts → SVG)
def svg_arrow(w, h, stroke, color, pid=None, cls="glyph"):
    idattr = f' id="{pid}"' if pid else ""
    return (f'<svg{idattr} class="{cls}" width="{w}" height="{h}" viewBox="0 0 {w} {h}" aria-hidden="true">'
            f'<path d="M{stroke} {h / 2} H{w - stroke * 1.5} M{w - h * 0.42} {h * 0.14} L{w - stroke} {h / 2} L{w - h * 0.42} {h * 0.86}" '
            f'fill="none" stroke="{color}" stroke-width="{stroke}" stroke-linecap="square"/></svg>')


# ------------------------------------------------------------------ shared CSS
def css_common(p, ground):
    return f"""
{FONT_FACES}
#root {{ position:absolute; inset:0; width:{W}px; height:{H}px; overflow:hidden; color:{DARK};
  font-family:'Libre Baskerville', serif; }}
#{p}-bg {{ position:absolute; inset:0; background:{ground}; }}
#root .{p}-abs {{ position:absolute; }}
.glyph {{ display:inline-block; vertical-align:middle; }}
.{p}-eyebrow {{ position:absolute; font-family:'Space Grotesk'; font-weight:600; font-size:19px; letter-spacing:3.5px;
  text-transform:uppercase; color:{RED}; white-space:nowrap; }}
.{p}-dark {{ color:{DARK}; }}
.{p}-white {{ color:#fff; }}
.{p}-hero {{ position:absolute; font-family:'Shrikhand'; font-size:150px; line-height:.92; color:{DARK};
  transform-origin:left top; white-space:nowrap; }}
.{p}-red {{ color:{RED}; }}
.{p}-sh {{ position:absolute; font-family:'Shrikhand'; font-size:63px; line-height:1.1; color:{DARK}; white-space:nowrap; }}
.{p}-body {{ position:absolute; font-size:30px; line-height:1.5; }}
.{p}-w {{ display:inline-block; }}
.{p}-chip {{ position:absolute; font-family:'Space Grotesk'; font-weight:600; font-size:21px; letter-spacing:2px;
  text-transform:uppercase; border:3px solid {DARK}; padding:12px 18px; background:{BG}; white-space:nowrap; }}
.{p}-chip.{p}-redb {{ border-color:{RED}; color:{RED}; }}
.{p}-chip b {{ color:{RED}; font-weight:600; }}
.{p}-tag {{ position:absolute; font-family:'Space Grotesk'; font-weight:600; font-size:17px; letter-spacing:2px;
  text-transform:uppercase; background:{DARK}; color:#fff; padding:6px 11px; white-space:nowrap; }}
.{p}-tag.{p}-redbg {{ background:{RED}; }}
.{p}-stamp {{ position:absolute; font-family:'Space Grotesk'; font-weight:600; font-size:20px; letter-spacing:2.5px;
  color:{RED}; border:5px solid {RED}; padding:8px 14px; white-space:nowrap; background:rgba(255,255,255,.92); }}
.{p}-cite {{ position:absolute; left:69px; top:836px; font-family:'Space Grotesk'; font-weight:600; font-size:18px;
  letter-spacing:2px; text-transform:uppercase; border:2px solid {DARK}; padding:6px 12px; background:{BG}; white-space:nowrap; }}
.{p}-prog {{ position:absolute; left:0; bottom:0; width:{W}px; height:10px; background:{RED}; transform-origin:left center; }}
.{p}-card {{ position:absolute; border:3px solid {DARK}; background:{BG}; }}
.{p}-cl {{ position:absolute; left:22px; top:14px; font-family:'Shrikhand'; font-size:72px; line-height:1; color:{RED}; }}
.{p}-ci {{ position:absolute; left:0; right:0; top:120px; height:150px; display:flex; justify-content:center; }}
.{p}-ct {{ position:absolute; left:22px; right:18px; top:286px; font-size:27px; line-height:1.42; }}
.{p}-cn {{ position:absolute; left:22px; bottom:16px; font-family:'Space Grotesk'; font-weight:600; font-size:15px;
  letter-spacing:2px; text-transform:uppercase; color:{RED}; }}
"""


def eyebrow(p, text, x=69, y=86, extra=""):
    return f'<div id="{p}-eyebrow" class="{p}-eyebrow{extra}" style="left:{x}px;top:{y}px">{text}</div>'


def cite(p, text):
    return f'<div id="{p}-cite" class="{p}-cite">{text}</div>'


# ------------------------------------------------------------------ five cards (frames 3–4)
CARD_X = [69, 423, 777, 1131, 1485]
CARD_Y, CARD_W, CARD_H = 300, 330, 500
CARDS = [
    ("a", "a)", "Konsinye teslim edilen, <b>çabuk bozulabilir</b> eşya", "GK md. 31/2"),
    ("b", "b)", "Kıymet unsurları yükümlülük başladıktan <b>sonra belli</b> olacak eşya", "sözleşme gereği"),
    ("c", "c)", "Fiyatın <b>sonradan gözden geçirilmesini</b> öngören eşya", "satış sözleşmesi"),
    ("cc", "ç)", "Boru hattı / elektrik teliyle taşınan, <b>sürekli akış</b> halindeki eşya", "depolanamaz"),
    ("d", "d)", "Sıvı gelir, gümrük gözetiminde gaza, limanda <b>boru hattına</b>", "LNG"),
]


def icon(key):
    s = f'stroke="{DARK}" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"'
    r = f'stroke="{RED}" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"'
    if key == "a":   # crate + clock (perishable)
        body = (f'<rect x="20" y="58" width="130" height="78" {s}/><path d="M20 84 H150 M20 110 H150" {s}/>'
                f'<circle cx="168" cy="44" r="30" {r}/><path d="M168 28 V44 L180 52" {r}/>')
    elif key == "b":  # document + later clock
        body = (f'<path d="M40 14 H120 L150 44 V140 H40 Z" {s}/><path d="M120 14 V44 H150" {s}/>'
                f'<path d="M60 72 H128 M60 96 H128" {s}/><circle cx="178" cy="112" r="28" {r}/><path d="M178 98 V112 L189 120" {r}/>')
    elif key == "c":  # price tag + revise arrows
        body = (f'<path d="M24 70 L80 14 H150 V84 L94 140 Z" {s}/><circle cx="124" cy="40" r="9" {s}/>'
                f'<path d="M168 92 A34 34 0 1 1 150 62" {r}/><path d="M146 46 L152 64 L170 58" {r}/>')
    elif key == "cc":  # pipe + lightning
        body = (f'<path d="M10 60 H110 V100 H10" {s}/><path d="M110 50 H126 V110 H110" {s}/>'
                f'<path d="M186 16 L152 80 H182 L156 140" {r}/>')
    else:             # ship waves → gas → pipe
        body = (f'<path d="M10 120 Q30 104 50 120 T90 120" {s}/><path d="M18 96 H84 L74 112 H28 Z" {s}/>'
                f'<path d="M100 92 C112 60 132 60 140 40" {r}/><path d="M118 96 C128 76 142 74 150 58" {r}/>'
                f'<path d="M150 120 H200 V140 H150" {s}/>')
    return f'<svg width="210" height="150" viewBox="0 0 210 150" aria-hidden="true">{body}</svg>'


def cards_html(p, dim=(), stamps=()):
    out = []
    for i, (k, letter, text, note) in enumerate(CARDS):
        op = 0.32 if k in dim else 1
        out.append(
            f'<div id="{p}-card-{k}" class="{p}-card" style="left:{CARD_X[i]}px;top:{CARD_Y}px;width:{CARD_W}px;height:{CARD_H}px;opacity:{op}">'
            f'<div class="{p}-cl">{letter}</div><div class="{p}-ci">{icon(k)}</div>'
            f'<div class="{p}-ct">{text}</div><div class="{p}-cn">{note}</div></div>')
        if k in stamps:
            out.append(f'<div id="{p}-stamp-{k}" class="{p}-stamp" style="left:{CARD_X[i] + 18}px;top:{CARD_Y + 190}px">'
                       f'SÖZLEŞME +<br>ONAYLI ÇEVİRİ</div>')
    return "\n".join(out)


# ------------------------------------------------------------------ timeline stage (frames 5–10)
LINE_Y = 470
TESCIL_X, AY1_X = 220, 760
STRIP_X0, STRIP_D0, STRIP_N, STRIP_W, STRIP_TOP, STRIP_H = 1040, 22, 9, 80, 420, 100


def day_x(d):
    return STRIP_X0 + (d - STRIP_D0) * STRIP_W


def timeline_css(p):
    return f"""
#{p}-line {{ position:absolute; left:120px; top:{LINE_Y - 2}px; width:{STRIP_X0 - 120}px; height:5px; background:{DARK};
  transform-origin:left center; }}
.{p}-mk {{ position:absolute; width:44px; height:44px; margin:-22px 0 0 -22px; border-radius:50%; background:{BG};
  border:6px solid {DARK}; }}
.{p}-mk.{p}-on {{ border-color:{RED}; }}
.{p}-mkl {{ position:absolute; font-family:'Shrikhand'; font-size:46px; line-height:1; white-space:nowrap; }}
.{p}-mks {{ position:absolute; font-size:27px; line-height:1.4; white-space:nowrap; }}
.{p}-strip {{ position:absolute; left:{STRIP_X0}px; top:{STRIP_TOP}px; display:grid;
  grid-template-columns:repeat({STRIP_N},{STRIP_W}px); grid-template-rows:{STRIP_H}px; gap:1.5px; background:{DARK};
  border:3px solid {DARK}; }}
.{p}-sd {{ position:relative; background:{BG}; }}
.{p}-sd span {{ position:absolute; left:8px; top:6px; font-family:'Space Grotesk'; font-weight:600; font-size:18px; }}
.{p}-ring {{ position:absolute; display:flex; align-items:center; justify-content:center; }}
.{p}-ring svg {{ position:absolute; left:0; top:0; overflow:visible; }}
.{p}-ring circle {{ fill:{BG}; stroke:{RED}; stroke-width:6; }}
.{p}-rn {{ position:relative; font-family:'Shrikhand'; font-size:40px; color:{RED}; line-height:1; }}
.{p}-flagpole {{ position:absolute; width:5px; background:{RED}; transform-origin:bottom center; }}
"""


def ring26(p, r=40):
    cx = day_x(26) + STRIP_W / 2 + 3
    cy = STRIP_TOP + STRIP_H / 2 + 3
    import math
    circ = 2 * math.pi * r
    html = (f'<div id="{p}-ring26" class="{p}-ring" style="left:{cx - r - 8:.1f}px;top:{cy - r - 8:.1f}px;'
            f'width:{2 * r + 16}px;height:{2 * r + 16}px"><svg width="{2 * r + 16}" height="{2 * r + 16}">'
            f'<circle id="{p}-ring26c" cx="{r + 8}" cy="{r + 8}" r="{r}" transform="rotate(-90 {r + 8} {r + 8})" '
            f'style="stroke-dasharray:{circ:.1f};stroke-dashoffset:0"/></svg><span id="{p}-ring26n" class="{p}-rn">26</span></div>')
    return html, circ


def timeline_html(p, tescil_on=True, ay1=True, strip=True, ring=True, flag=True, ay1_label=None, tescil_dim=False):
    """Static timeline stage. Returns (html, ring_circumference)."""
    out = [f'<div id="{p}-line"></div>']
    tes_op = 0.35 if tescil_dim else 1
    out.append(f'<div id="{p}-mk-tescil" class="{p}-mk{" " + p + "-on" if tescil_on else ""}" style="left:{TESCIL_X}px;top:{LINE_Y}px;opacity:{tes_op}"></div>')
    out.append(f'<div id="{p}-tescil-l" class="{p}-mkl {p}-red" style="left:{TESCIL_X - 22}px;top:{LINE_Y + 46}px;opacity:{tes_op}">TESCİL</div>')
    if ay1:
        out.append(f'<div id="{p}-mk-ay1" class="{p}-mk" style="left:{AY1_X}px;top:{LINE_Y}px"></div>')
        out.append(f'<div id="{p}-ay1-top" class="{p}-tag" style="left:{AY1_X - 38}px;top:{LINE_Y - 76}px">1. AY</div>')
        out.append(ay1_label or
                   f'<div id="{p}-ay1-l" class="{p}-mks" style="left:{AY1_X - 22}px;top:{LINE_Y + 46}px">unsur <b>tahakkuk</b> eder</div>')
    ring_html, circ = ("", 0)
    if strip:
        cells = "".join(f'<div class="{p}-sd"><span id="{p}-sd-{d}" style="opacity:{0 if (ring and d == 26) else 1}">{d}</span></div>'
                        for d in range(STRIP_D0, STRIP_D0 + STRIP_N))
        out.append(f'<div id="{p}-ay2-top" class="{p}-tag" style="left:{STRIP_X0}px;top:{STRIP_TOP - 44}px">2. AY</div>')
        out.append(f'<div id="{p}-strip" class="{p}-strip">{cells}</div>')
        if ring:
            ring_html, circ = ring26(p)
            out.append(ring_html)
            out.append(f'<div id="{p}-aksam" class="{p}-tag {p}-redbg" style="left:{day_x(26) - 46}px;top:{STRIP_TOP + STRIP_H + 14}px">AKŞAMINA KADAR</div>')
    if flag:
        fx = day_x(26) + STRIP_W / 2 + 1
        out.append(f'<div id="{p}-flagpole" class="{p}-flagpole" style="left:{fx:.1f}px;top:300px;height:{STRIP_TOP - 300}px"></div>')
        out.append(f'<div id="{p}-flag" class="{p}-chip {p}-redb" style="left:{fx - 182:.1f}px;top:236px">TAMAMLAYICI BEYAN + ÖDEME</div>')
    return "\n".join(out), circ


# ------------------------------------------------------------------ frames (final static state)
def frame_specs():
    F = {}

    # 01 — hook
    p = "f01"
    paper_css = f"""
#{p}-paper {{ position:absolute; left:980px; top:140px; width:780px; height:640px; border:3px solid {DARK}; background:{BG}; }}
.{p}-row {{ position:absolute; left:0; right:0; border-top:1.5px solid {DARK}; }}
.{p}-rk {{ position:absolute; left:24px; top:22px; font-family:'Space Grotesk'; font-weight:600; font-size:20px; letter-spacing:2.5px; }}
.{p}-rv {{ position:absolute; left:260px; top:30px; height:14px; background:{LIGHT}; }}
#{p}-qcell {{ position:absolute; left:236px; top:438px; width:516px; height:176px; border:6px solid {RED}; }}
#{p}-q {{ position:absolute; left:1408px; top:572px; font-family:'Shrikhand'; font-size:240px; line-height:.7; color:{RED};
  transform-origin:center center; }}
"""
    rows = [("EŞYA", 380), ("MİKTAR", 220), ("TESCİL", 300), ("KIYMET", None)]
    paper = [f'<div id="{p}-paper"><div class="{p}-rk" style="top:24px;letter-spacing:4px">BEYANNAME</div>']
    for i, (k, w) in enumerate(rows):
        top = 90 + i * 136
        bar = f'<div class="{p}-rv" style="width:{w}px"></div>' if w else ""
        paper.append(f'<div class="{p}-row" style="top:{top}px;height:136px"><div class="{p}-rk">{k}</div>{bar}</div>')
    paper.append(f'<div id="{p}-qcell"></div></div>')
    F[1] = dict(slug="kiymet-belli-degil", css=paper_css, html="\n".join([
        eyebrow(p, "GÜMRÜK KOÇU · İSTİSNAİ KIYMET"),
        f'<div id="{p}-h1" class="{p}-hero" style="left:69px;top:190px" data-layout-allow-overlap>Kıymet</div>',
        f'<div id="{p}-h2" class="{p}-hero {p}-red" style="left:69px;top:362px;transform:rotate(-4deg)" data-layout-allow-overlap>belli değil.</div>',
        f'<div id="{p}-body" class="{p}-body" style="left:69px;top:640px;width:800px">Tescil günü: <b>kıymet alanı boş.</b></div>',
        "\n".join(paper),
        f'<div id="{p}-q">?</div>',
        cite(p, "GY md. 53"),
    ]))

    # 02 — concept
    p = "f02"
    F[2] = dict(slug="istisnai-kiymet", css="", html="\n".join([
        eyebrow(p, "CEVAP"),
        f'<div id="{p}-h1" class="{p}-hero" style="left:69px;top:160px" data-layout-allow-overlap>İstisnai</div>',
        f'<div id="{p}-h2" class="{p}-hero {p}-red" style="left:69px;top:342px;font-size:132px;transform:rotate(-4deg)" data-layout-allow-overlap>kıymetle beyan</div>',
        f'<div id="{p}-c1" class="{p}-chip" style="left:69px;top:620px">BEYAN SAHİBİNİN <b>TALEBİ</b></div>',
        f'<div id="{p}-ar" class="{p}-abs" style="left:520px;top:632px">{svg_arrow(90, 40, 7, DARK)}</div>',
        f'<div id="{p}-c2" class="{p}-chip {p}-redb" style="left:640px;top:620px">GÜMRÜK İDARESİ · BASİTLEŞTİRİLMİŞ USUL</div>',
        f'<div id="{p}-yon" class="{p}-tag" style="left:1388px;top:92px">SATIŞ BEDELİ YÖNTEMİ · GK MD. 24</div>',
        cite(p, "GY md. 53/1"),
    ]))

    # 03 — five goods
    p = "f03"
    F[3] = dict(slug="bes-esya", css="", html="\n".join([
        eyebrow(p, "KAPSAM"),
        f'<div id="{p}-sh" class="{p}-sh" style="left:69px;top:150px">Beş eşya</div>',
        cards_html(p),
        cite(p, "GY md. 53/1 · GK md. 31/2"),
    ]))

    # 04 — conditions + contracts
    p = "f04"
    F[4] = dict(slug="kosullar", css="", html="\n".join([
        eyebrow(p, "GY MD. 53/2"),
        f'<div id="{p}-k1" class="{p}-chip" style="left:69px;top:150px">GY 22–24 GENEL VE ÖZEL KOŞULLAR <b>ARANMAZ</b></div>',
        f'<div id="{p}-k2" class="{p}-chip" style="left:69px;top:222px">BASİTLEŞTİRİLMİŞ USULÜN DİĞER HAKLARI <b>VERİLMEZ</b></div>',
        cards_html(p, dim=("a", "d"), stamps=("b", "c", "cc")),
        cite(p, "GY md. 53/2"),
    ]))

    # 05 — tescil
    p = "f05"
    tl, circ = timeline_html(p, ay1=False, strip=False, ring=False, flag=False)
    F[5] = dict(slug="tescil", css=timeline_css(p), circ=circ, html="\n".join([
        eyebrow(p, "ZAMAN ÇİZGİSİ"),
        f'<div id="{p}-sh" class="{p}-sh" style="left:69px;top:150px">Tescil günü</div>',
        tl,
        f'<div id="{p}-tes-s" class="{p}-mks" style="left:{TESCIL_X - 22}px;top:{LINE_Y + 112}px">vergi = <b>mevcut belgelerdeki kıymet</b></div>',
        cite(p, "GY md. 53/3"),
    ]))

    # 06 — 26th
    p = "f06"
    tl, circ = timeline_html(p)
    F[6] = dict(slug="yirmi-alti", css=timeline_css(p), circ=circ, html="\n".join([
        eyebrow(p, "ZAMAN ÇİZGİSİ"),
        f'<div id="{p}-sh" class="{p}-sh" style="left:69px;top:150px">Takip eden ayın 26\'sı</div>',
        tl,
        f'<div id="{p}-ay1-s" class="{p}-mks" style="left:{AY1_X - 22}px;top:{LINE_Y + 88}px;font-size:23px">mahiyet ve tutar olarak</div>',
        cite(p, "GY md. 150/3"),
    ]))

    # 07 — higher / lower
    p = "f07"
    tl, circ = timeline_html(p)
    up_x = day_x(26) + STRIP_W / 2
    F[7] = dict(slug="yuksek-dusuk", css=timeline_css(p), circ=circ, html="\n".join([
        eyebrow(p, "TAMAMLAYICI BEYANA GÖRE"),
        f'<div id="{p}-sh" class="{p}-sh" style="left:69px;top:150px">Yüksek mi, düşük mü?</div>',
        tl,
        f'<div id="{p}-up" class="{p}-chip {p}-redb" style="left:1452px;top:120px">YÜKSEK {svg_arrow(46, 26, 5, RED)} EK VERGİ TAHAKKUKU</div>',
        f'<div id="{p}-dn-l" class="{p}-chip" style="left:980px;top:610px">DÜŞÜK {svg_arrow(46, 26, 5, DARK)}</div>',
        f'<div id="{p}-d1" class="{p}-chip" style="left:980px;top:690px;font-size:17px">FARKIN İADESİ BELGELENİR</div>',
        f'<div id="{p}-d2" class="{p}-chip" style="left:1330px;top:690px;font-size:17px">TAHLİL RAPORU GİBİ BELGE · ONAYLI ÖRNEK</div>',
        f'<div id="{p}-d3" class="{p}-chip" style="left:980px;top:766px;font-size:17px">GÜMRÜK İNCELER</div>',
        f'<div id="{p}-d4" class="{p}-stamp" style="left:1250px;top:760px;font-size:22px">GK MD. 211</div>',
        cite(p, "GY md. 53/3"),
    ]))

    # 08 — zamanaşımı
    p = "f08"
    tl, circ = timeline_html(p, tescil_dim=True)
    za_css = f"""#{p}-za {{ position:absolute; left:{day_x(26) + 40}px; top:{STRIP_TOP + STRIP_H + 64}px; height:8px;
  width:{1880 - day_x(26) - 40}px; background:{RED}; transform-origin:left center; }}
#{p}-zah {{ position:absolute; left:1846px; top:{STRIP_TOP + STRIP_H + 48}px; width:0; height:0; border-left:40px solid {RED};
  border-top:20px solid transparent; border-bottom:20px solid transparent; }}"""
    F[8] = dict(slug="zamanasimi", css=timeline_css(p) + za_css, circ=circ, html="\n".join([
        eyebrow(p, "DİKKAT"),
        f'<div id="{p}-sh" class="{p}-sh" style="left:69px;top:150px">Zamanaşımı</div>',
        tl,
        f'<div id="{p}-za"></div><div id="{p}-zah"></div>',
        f'<div id="{p}-zal" class="{p}-tag {p}-redbg" style="left:{day_x(26) + 40}px;top:{STRIP_TOP + STRIP_H + 92}px;font-size:20px">ZAMANAŞIMI BURADAN BAŞLAR</div>',
        f'<div id="{p}-zas" class="{p}-mks" style="left:{day_x(26) + 40}px;top:{STRIP_TOP + STRIP_H + 140}px">tamamlayıcı beyanın <b>verildiği tarih</b></div>',
        cite(p, "GY md. 53/4"),
    ]))

    # 09 — muhasebe kaydı
    p = "f09"
    ay1_label = (f'<div id="{p}-ay1-l" class="{p}-mks" style="left:{AY1_X - 22}px;top:{LINE_Y + 46}px;font-size:24px">'
                 f'<span style="font-family:Space Grotesk;font-weight:600;letter-spacing:2px">TAHAKKUK</span> · 150/3</div>'
                 f'<div id="{p}-ay1-l2" class="{p}-mks {p}-red" style="left:{AY1_X - 22}px;top:{LINE_Y + 86}px;font-size:24px">'
                 f'<span style="font-family:Space Grotesk;font-weight:600;letter-spacing:2px">MUHASEBE KAYDI</span> · 53/5-6</div>')
    tl, circ = timeline_html(p, flag=False, ay1_label=ay1_label, tescil_dim=True)
    F[9] = dict(slug="muhasebe-kaydi", css=timeline_css(p), circ=circ, html="\n".join([
        eyebrow(p, "GY MD. 53/5 · 53/6"),
        f'<div id="{p}-sh" class="{p}-sh" style="left:69px;top:150px">26 kuralı: iki durum daha</div>',
        tl,
        f'<div id="{p}-k5" class="{p}-card" style="left:69px;top:640px;width:560px;height:170px;padding:18px 22px">'
        f'<div style="font-family:Shrikhand;font-size:40px;color:{RED};line-height:1">(5)</div>'
        f'<div style="font-size:24px;line-height:1.4;margin-top:8px">Tescilde varlığı bilinemeyen kıymet / KDV matrah unsurları</div></div>',
        f'<div id="{p}-k6" class="{p}-card" style="left:660px;top:640px;width:560px;height:170px;padding:18px 22px">'
        f'<div style="font-family:Shrikhand;font-size:40px;color:{RED};line-height:1">(6)</div>'
        f'<div style="font-size:24px;line-height:1.4;margin-top:8px">Depolama · tahmil-tahliye · liman giderleri gibi KDV matrah unsurları</div></div>',
        f'<div id="{p}-odeme" class="{p}-chip {p}-redb" style="left:1300px;top:690px">BEYAN + ÖDEME</div>',
        cite(p, "GY md. 53/5 · 53/6"),
    ]))

    # 10 — gecikme
    p = "f10"
    tl, circ = timeline_html(p)
    back_css = f"""#{p}-back {{ position:absolute; left:{TESCIL_X + 30}px; top:362px; height:8px; width:{day_x(26) + 10 - TESCIL_X - 30}px;
  background:{RED}; transform-origin:right center; }}
#{p}-backh {{ position:absolute; left:{TESCIL_X - 4}px; top:346px; width:0; height:0; border-right:40px solid {RED};
  border-top:20px solid transparent; border-bottom:20px solid transparent; }}"""
    F[10] = dict(slug="gecikme", css=timeline_css(p) + back_css, circ=circ, html="\n".join([
        eyebrow(p, "SÜRE KAÇARSA"),
        f'<div id="{p}-sh" class="{p}-sh" style="left:69px;top:150px">Gecikme faizi</div>',
        tl,
        f'<div id="{p}-late" class="{p}-tag" style="left:{day_x(28) + 4}px;top:{STRIP_TOP + STRIP_H + 14}px">SÜRE GEÇTİ</div>',
        f'<div id="{p}-back"></div><div id="{p}-backh"></div>',
        f'<div id="{p}-backl" class="{p}-tag {p}-redbg" style="left:420px;top:306px;font-size:20px">TESCİL TARİHİNDEN İTİBAREN</div>',
        f'<div id="{p}-oran" class="{p}-mks" style="left:980px;top:620px">gecikme zammı oranında · <i>6183 s. Kanun</i></div>',
        f'<div id="{p}-241" class="{p}-stamp" style="left:1300px;top:700px;font-size:24px">GK MD. 241/1</div>',
        cite(p, "GY md. 53/7"),
    ]))

    # 11 — kısacası (red panel)
    p = "f11"
    sum_css = f""".{p}-big {{ position:absolute; font-family:'Shrikhand'; font-size:120px; line-height:1; color:#fff; text-shadow:{SHADOW};
  white-space:nowrap; transform-origin:left top; }}
.{p}-sub {{ position:absolute; font-size:40px; line-height:1.3; color:#fff; }}
#{p}-link {{ position:absolute; left:250px; top:300px; width:1420px; height:6px; background:#fff; transform-origin:left center; }}
.{p}-dot {{ position:absolute; width:40px; height:40px; margin:-20px 0 0 -20px; border-radius:50%; background:#fff; }}
.{p}-rule {{ position:absolute; font-family:'Space Grotesk'; font-weight:600; font-size:26px; letter-spacing:3px; color:#fff; white-space:nowrap; }}"""
    F[11] = dict(slug="kisacasi", ground=RED, prog=DARK, css=sum_css, html="\n".join([
        eyebrow(p, "KISACASI · GY MD. 53 · 150/3", extra=f" {p}-white"),
        '<div id="f11-link"></div>',
        f'<div id="{p}-dot1" class="{p}-dot" style="left:250px;top:303px"></div>',
        f'<div id="{p}-dot2" class="{p}-dot" style="left:1670px;top:303px"></div>',
        f'<div id="{p}-b1" class="{p}-big" style="left:120px;top:380px;transform:rotate(-4deg)">Tescil</div>',
        f'<div id="{p}-s1" class="{p}-sub" style="left:130px;top:540px">belgedeki kıymet</div>',
        f'<div id="{p}-b2" class="{p}-big" style="left:980px;top:380px;transform:rotate(-4deg)">26\'sı akşamı</div>',
        f'<div id="{p}-s2" class="{p}-sub" style="left:990px;top:540px">tamamlayıcı beyan</div>',
        f'<div id="{p}-r1" class="{p}-rule" style="left:130px;top:720px">ZAMANAŞIMI {svg_arrow(50, 26, 5, "#fff")} BEYANDAN</div>',
        f'<div id="{p}-r2" class="{p}-rule" style="left:990px;top:720px">GECİKME FAİZİ {svg_arrow(50, 26, 5, "#fff")} TESCİLDEN</div>',
    ]))

    # 12 — logo
    p = "f12"
    F[12] = dict(slug="kapanis", css="", html="\n".join([
        f'<img id="{p}-logo" class="{p}-abs" src="public/logo-ufuk-cetintas.png" alt="Ufuk Çetintaş — Gümrük Eğitim Koçu" '
        f'style="left:576px;top:150px;width:768px;height:auto">',
        f'<div id="{p}-handle" class="{p}-eyebrow {p}-dark" style="left:0;top:650px;width:{W}px;text-align:center;font-size:31px;letter-spacing:5px">@GUMRUKKOCUNUZ</div>',
    ]))
    return F
