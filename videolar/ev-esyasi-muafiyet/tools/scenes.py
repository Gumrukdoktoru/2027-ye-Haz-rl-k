#!/usr/bin/env python3
"""Kullanılmış ev eşyası muafiyeti — sahne yerleşimleri (taslak ve video ortak kaynağı).

Her sahne, son (yerleşmiş) halini 1920×1080 piksel koordinatlarla tanımlar; aynı tanım hem taslakta
(storyboard.html) hem de hareketli sahnelerde (compositions/frames/*.html) kullanılır.
Zemin bu videoya özel: kraft karton, üst ve alt kenarda koli bandı.
"""

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W, H = 1920, 1080
KRAFT, TAPE, BOX = "#E6D5B8", "#CDB48C", "#C9A97A"
DARK, MUTED, PAPER = "#1C1410", "#5E4E3A", "#FFFFFF"
RED, RED_T = "#D8000F", "#A8000B"
BG = "#FFFFFF"
SHADOW = "2px 2px 0 rgba(28,20,16,.25), 4px 4px 0 rgba(28,20,16,.2), 6px 6px 0 rgba(28,20,16,.15)"
GROUND = (
    f"linear-gradient(to bottom, {TAPE} 0, {TAPE} 34px, {KRAFT} 34px, {KRAFT} 1000px, "
    f"{TAPE} 1000px, {TAPE} 1040px, {KRAFT} 1040px)"
)
N_FRAMES = 12

FONT_FACES = (
    open(os.path.join(ROOT, "assets/fonts.css"))
    .read()
    .replace("url('fonts/", "url('assets/fonts/")
)


# ------------------------------------------------------------------ glyphs (fontta yok → SVG)
def svg_arrow(w, h, stroke, color, cls="glyph"):
    return (
        f'<svg class="{cls}" width="{w}" height="{h}" viewBox="0 0 {w} {h}" aria-hidden="true">'
        f'<path d="M{stroke} {h / 2} H{w - stroke * 1.5} M{w - h * 0.42} {h * 0.14} L{w - stroke} {h / 2} L{w - h * 0.42} {h * 0.86}" '
        f'fill="none" stroke="{color}" stroke-width="{stroke}" stroke-linecap="square"/></svg>'
    )


def svg_check(s, color, stroke=6):
    return (
        f'<svg class="glyph" width="{s}" height="{s}" viewBox="0 0 {s} {s}" aria-hidden="true">'
        f'<path d="M{s * .14} {s * .52} L{s * .4} {s * .78} L{s * .88} {s * .2}" fill="none" stroke="{color}" '
        f'stroke-width="{stroke}" stroke-linecap="square"/></svg>'
    )


def box_svg(w, h, label=True):
    """Bantlı taşınma kolisi."""
    s = f'stroke="{DARK}" stroke-width="5"'
    lab = ""
    if label:
        lw, lh = w * 0.62, h * 0.2
        lab = (
            f'<rect x="{(w - lw) / 2}" y="{h * .5}" width="{lw}" height="{lh}" fill="{PAPER}" {s}/>'
            f'<text x="{w / 2}" y="{h * .5 + lh * .64}" text-anchor="middle" font-family="Space Grotesk" font-weight="600" '
            f'font-size="{lh * .36:.0f}" letter-spacing="2" fill="{DARK}">EV EŞYASI</text>'
        )
    return (
        f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" aria-hidden="true">'
        f'<rect x="2.5" y="2.5" width="{w - 5}" height="{h - 5}" fill="{BOX}" {s}/>'
        f'<rect x="{w * .43}" y="2.5" width="{w * .14}" height="{h * .32}" fill="{TAPE}" {s}/>'
        f'<path d="M2.5 {h * .32} H{w - 2.5}" {s}/>{lab}</svg>'
    )


def icon(key):
    s = f'stroke="{DARK}" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"'
    r = f'stroke="{RED}" stroke-width="6" fill="none" stroke-linecap="round" stroke-linejoin="round"'
    if key == "a":  # takvim + uçak
        body = (
            f'<rect x="20" y="30" width="110" height="96" {s}/><path d="M20 58 H130 M48 18 V40 M102 18 V40" {s}/>'
            f'<text x="75" y="108" text-anchor="middle" font-family="Shrikhand" font-size="40" fill="{RED}">24</text>'
            f'<path d="M150 98 L200 60 M172 70 L188 102 M160 80 L150 62" {r}/>'
        )
    elif key == "b":  # evrak çantası
        body = (
            f'<rect x="30" y="50" width="150" height="90" {s}/><path d="M80 50 V30 H130 V50 M30 86 H180" {s}/>'
            f'<path d="M98 80 H112 V96 H98 Z" {r}/>'
        )
    elif key == "c":  # kimlik kartı
        body = (
            f'<rect x="20" y="34" width="170" height="104" {s}/><circle cx="66" cy="76" r="18" {s}/>'
            f'<path d="M42 118 C46 100 86 100 90 118" {s}/><path d="M110 68 H170 M110 90 H170" {r}/>'
        )
    else:  # vasiyet / belge + mühür
        body = (
            f'<path d="M40 20 H140 L170 50 V140 H40 Z" {s}/><path d="M140 20 V50 H170" {s}/>'
            f'<path d="M62 70 H146 M62 94 H120" {s}/><circle cx="150" cy="118" r="22" {r}/>'
        )
    return f'<svg width="210" height="150" viewBox="0 0 210 150" aria-hidden="true">{body}</svg>'


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
  text-transform:uppercase; color:{RED_T}; white-space:nowrap; }}
.{p}-white {{ color:#fff; }}
.{p}-hero {{ position:absolute; font-family:'Shrikhand'; font-size:150px; line-height:.92; color:{DARK};
  transform-origin:left top; white-space:nowrap; }}
.{p}-red {{ color:{RED_T}; }}
.{p}-sh {{ position:absolute; font-family:'Shrikhand'; font-size:63px; line-height:1.1; color:{DARK}; white-space:nowrap; }}
.{p}-body {{ position:absolute; font-size:32px; line-height:1.5; color:{DARK}; }}
.{p}-muted {{ color:{MUTED}; }}
.{p}-chip {{ position:absolute; font-family:'Space Grotesk'; font-weight:600; font-size:21px; letter-spacing:2px;
  text-transform:uppercase; border:3px solid {DARK}; padding:12px 18px; background:{PAPER}; color:{DARK}; white-space:nowrap; }}
.{p}-chip b {{ color:{RED_T}; font-weight:600; }}
.{p}-tag {{ position:absolute; font-family:'Space Grotesk'; font-weight:600; font-size:20px; letter-spacing:2.5px;
  text-transform:uppercase; background:{RED}; color:#fff; padding:7px 13px; white-space:nowrap; }}
.{p}-tag.{p}-darkbg {{ background:{DARK}; }}
.{p}-stamp {{ position:absolute; font-family:'Space Grotesk'; font-weight:600; font-size:30px; letter-spacing:3px;
  color:{RED}; border:6px solid {RED}; padding:10px 20px; white-space:nowrap; background:rgba(255,255,255,.9); }}
.{p}-stamp.{p}-ok {{ color:{DARK}; border-color:{DARK}; }}
.{p}-cite {{ position:absolute; top:836px; font-family:'Space Grotesk'; font-weight:600; font-size:18px;
  letter-spacing:2px; text-transform:uppercase; border:2px solid {DARK}; padding:6px 12px; color:{DARK}; white-space:nowrap; }}
.{p}-prog {{ position:absolute; left:0; bottom:0; width:{W}px; height:10px; background:{RED}; transform-origin:left center; }}
.{p}-card {{ position:absolute; background:{PAPER}; color:{DARK}; border:3px solid {DARK}; }}
.{p}-lab {{ position:absolute; font-family:'Space Grotesk'; font-weight:600; font-size:21px; letter-spacing:2.5px;
  text-transform:uppercase; color:{DARK}; white-space:nowrap; }}
.{p}-txt {{ position:absolute; font-size:27px; line-height:1.42; color:{DARK}; }}
.{p}-txt b {{ color:{RED_T}; }}
.{p}-node {{ position:absolute; background:{PAPER}; border:4px solid {DARK}; padding:24px 28px; box-sizing:border-box;
  font-size:30px; line-height:1.35; color:{DARK}; }}
.{p}-node b {{ color:{RED_T}; }}
.{p}-node small {{ display:block; font-family:'Space Grotesk'; font-weight:600; font-size:18px; letter-spacing:2px;
  text-transform:uppercase; color:{MUTED}; margin-top:8px; }}
"""


def eyebrow(p, text, x=69, y=86, extra=""):
    return f'<div id="{p}-eyebrow" class="{p}-eyebrow{extra}" style="left:{x}px;top:{y}px">{text}</div>'


def cite(p, text, x=69):
    return f'<div id="{p}-cite" class="{p}-cite" style="left:{x}px">{text}</div>'


def sh(p, text, top=140, left=69):
    return f'<div id="{p}-sh" class="{p}-sh" style="left:{left}px;top:{top}px">{text}</div>'


# ------------------------------------------------------------------ dört etiket (sahne 2–3)
LAB_X = [69, 517, 965, 1413]
LAB_Y, LAB_W, LAB_H = 290, 420, 440
LABELS = [
    (
        "a",
        "a)",
        "YURT DIŞI ≥ 24 AY",
        "en az 24 ay ikamet, yerleşim yerini <b>kesin olarak</b> Türkiye'ye nakleden",
    ),
    ("b", "b)", "KAMU GÖREVLİSİ", "yurt dışındaki <b>sürekli görevinden</b> dönen"),
    (
        "c",
        "c)",
        "VATANDAŞLIĞA GEÇEN",
        "Türk vatandaşlığına geçip yerleşim yerini <b>kesin olarak</b> nakleden",
    ),
    (
        "cc",
        "ç)",
        "MİRASÇI",
        "yurt dışında yerleşik kişinin ölümüyle, <b>Türkiye'de yerleşik</b> mirasçı",
    ),
]


def labels_css(p):
    return f"""
.{p}-lh {{ position:absolute; left:0; right:0; top:0; height:64px; background:{RED}; color:#fff; display:flex; align-items:center;
  gap:16px; padding:0 22px; font-family:'Space Grotesk'; font-weight:600; font-size:21px; letter-spacing:2.5px; white-space:nowrap; }}
.{p}-lh span {{ font-family:'Shrikhand'; font-size:40px; letter-spacing:0; }}
.{p}-li {{ position:absolute; left:0; right:0; top:84px; display:flex; justify-content:center; }}
"""


def labels_html(p, dim=()):
    out = []
    for i, (k, letter, title, text) in enumerate(LABELS):
        op = 0.35 if k in dim else 1
        out.append(
            f'<div id="{p}-lab-{k}" class="{p}-card" style="left:{LAB_X[i]}px;top:{LAB_Y}px;width:{LAB_W}px;height:{LAB_H}px;opacity:{op}">'
            f'<div class="{p}-lh"><span>{letter}</span>{title}</div>'
            f'<div class="{p}-li">{icon(k)}</div>'
            f'<div class="{p}-txt" style="left:24px;right:22px;top:250px">{text}</div></div>'
        )
    return "\n".join(out)


# ------------------------------------------------------------------ karar ağacı (sahne 4–6)
CAL_X, CAL_Y, CAL_CW, CAL_H = 640, 510, 100, 80
MONTHS = ["O", "Ş", "M", "N", "M", "H", "T", "A", "E", "E", "K", "A"]


def tree_css(p):
    return f"""
.{p}-cal {{ position:absolute; top:{CAL_Y}px; width:{CAL_CW}px; height:{CAL_H}px; box-sizing:border-box; border:3px solid {DARK};
  background:{PAPER}; font-family:'Space Grotesk'; font-weight:600; font-size:24px; color:{DARK};
  display:flex; align-items:flex-end; justify-content:center; padding-bottom:10px; }}
.{p}-cal.{p}-in {{ background:{DARK}; color:#fff; }}
.{p}-six {{ position:absolute; left:{CAL_X + 6 * CAL_CW - 4}px; top:{CAL_Y - 22}px; width:8px; height:{CAL_H + 44}px; background:{RED}; }}
.{p}-ln {{ position:absolute; background:{DARK}; }}
"""


def tree_html(p, stage):
    """stage 4: kök + takvim; 5: + 10/5 istisnası; 6: + döngü."""
    out = [
        f'<div id="{p}-root" class="{p}-node" style="left:69px;top:300px;width:440px;height:170px">'
        f"Yurt dışında <b>≥ 24 ay</b> ikamet<small>(a) kişisi · (ç)'de ölen kişi</small></div>",
        f'<div id="{p}-a1" class="{p}-abs" style="left:520px;top:362px">{svg_arrow(108, 46, 7, DARK)}</div>',
        f'<div id="{p}-n2" class="{p}-node" style="left:640px;top:300px;width:1200px;height:170px">'
        f"Bir takvim yılında Türkiye'de <b>en çok 6 ay</b><small>altı aydan fazla kalmamış olmalı</small></div>",
    ]
    for i, m in enumerate(MONTHS):
        cls = f" {p}-in" if i < 6 else ""
        out.append(
            f'<div id="{p}-m{i + 1}" class="{p}-cal{cls}" style="left:{CAL_X + i * CAL_CW}px">{m}</div>'
        )
    out.append(f'<div id="{p}-six" class="{p}-six" data-layout-allow-overlap></div>')
    out.append(
        f'<div id="{p}-sixl" class="{p}-tag" style="left:{CAL_X + 6 * CAL_CW - 40}px;top:{CAL_Y + CAL_H + 30}px">6 AY</div>'
    )
    out.append(
        f'<div id="{p}-d45" class="{p}-chip" style="left:{CAL_X}px;top:{CAL_Y + CAL_H + 30}px">≤ 45 gün / yıl <b>= yurt dışı</b> sayılır</div>'
    )
    if stage >= 5:
        out += [
            f'<div id="{p}-n3" class="{p}-node" style="left:69px;top:700px;width:440px;height:130px">'
            f"Son <b>10 yılda ≥ 5 yıl</b> yurt dışı</div>",
            f'<div id="{p}-a3" class="{p}-abs" style="left:520px;top:742px">{svg_arrow(150, 46, 7, RED)}</div>',
            f'<div id="{p}-free" class="{p}-stamp" style="left:690px;top:728px">SÜRE ŞARTI ARANMAZ</div>',
            f'<div id="{p}-ele" class="{p}-chip" style="left:1330px;top:{CAL_Y + CAL_H + 30}px">giriş-çıkış: <b>elektronik sistem</b></div>',
        ]
    if stage >= 6:
        loop = (
            f'<svg width="380" height="80" viewBox="0 0 380 80" aria-hidden="true">'
            f'<path d="M340 76 C340 10 40 10 40 70" fill="none" stroke="{RED}" stroke-width="7"/>'
            f'<path d="M22 50 L40 76 L60 52" fill="none" stroke="{RED}" stroke-width="7" stroke-linecap="square"/></svg>'
        )
        out += [
            f'<div id="{p}-loop" class="{p}-abs" style="left:100px;top:222px" data-layout-allow-overlap>{loop}</div>',
            f'<div id="{p}-again" class="{p}-tag" style="left:500px;top:236px">tekrar için: yeniden ≥ 24 ay</div>',
        ]
    return "\n".join(out)


# ------------------------------------------------------------------ frames
def frame_specs():
    F = {}

    # 1 — kesin dönüş
    p = "f01"
    F[1] = dict(
        slug="kesin-donus",
        css="",
        html="\n".join(
            [
                eyebrow(p, "GÜMRÜK KOÇU · MUAFİYET TEBLİĞİ (SERİ NO: 2)"),
                f'<div id="{p}-b1" class="{p}-abs" style="left:120px;top:560px">{box_svg(340, 240)}</div>',
                f'<div id="{p}-b2" class="{p}-abs" style="left:470px;top:600px">{box_svg(280, 200, label=False)}</div>',
                f'<div id="{p}-b3" class="{p}-abs" style="left:190px;top:330px">{box_svg(300, 230, label=False)}</div>',
                f'<div id="{p}-h1" class="{p}-hero" style="left:860px;top:250px">Kesin dönüş</div>',
                f'<div id="{p}-h2" class="{p}-hero {p}-red" style="left:880px;top:420px;transform:rotate(-4deg)" data-layout-allow-overlap>muaf mı?</div>',
                f'<div id="{p}-body" class="{p}-body" style="left:884px;top:640px">Kullanılmış ev eşyası · <b>gümrük vergileri</b></div>',
                cite(p, "Muafiyet Tebliği (Seri No: 2) · md. 10–16"),
            ]
        ),
    )

    # 2 — dört kişi
    p = "f02"
    F[2] = dict(
        slug="dort-kisi",
        css=labels_css(p),
        html="\n".join(
            [
                eyebrow(p, "KİŞİLER · MD. 10"),
                sh(p, "Kimler yararlanır?"),
                labels_html(p),
                cite(p, "md. 10"),
            ]
        ),
    )

    # 3 — aile ünitesi
    p = "f03"
    F[3] = dict(
        slug="aile-unitesi",
        css=labels_css(p) + f"""
.{p}-band {{ position:absolute; left:69px; top:244px; width:1316px; height:32px; background:{DARK}; color:#fff;
  font-family:'Space Grotesk'; font-weight:600; font-size:19px; letter-spacing:3px; display:flex; align-items:center;
  justify-content:center; transform-origin:left center; }}
""",
        html="\n".join(
            [
                eyebrow(p, "MD. 11/1-A"),
                sh(p, "Aile ünitesi"),
                f'<div id="{p}-band" class="{p}-band">AİLE ÜNİTESİ ESAS ALINIR · a · b · c</div>',
                labels_html(p, dim=("cc",)),
                f'<div id="{p}-doc" class="{p}-chip" style="left:69px;top:760px">tespit: <b>vukuatlı nüfus kayıt örneği</b></div>',
                cite(p, "md. 11/1-a", x=1660),
            ]
        ),
    )

    # 4–6 — karar ağacı
    for n, stage, ey, title, ct in (
        (4, 4, "ŞARTLAR · MD. 11/1-B", "Takvim yılı kuralı", "md. 11/1-b"),
        (5, 5, "İSTİSNA · MD. 11/1-B, C", "On yılda beş yıl", "md. 11/1-b, c"),
        (6, 6, "TEKRAR · MD. 11/2", "İkinci kez", "md. 11/2"),
    ):
        p = f"f{n:02d}"
        F[n] = dict(
            slug=("takvim-yili", "on-yilda-bes", "ikinci-kez")[n - 4],
            css=tree_css(p),
            html="\n".join(
                [
                    eyebrow(p, ey),
                    sh(p, title),
                    tree_html(p, stage),
                    cite(p, ct, x=1580),
                ]
            ),
        )

    # 7 — kimler yararlanamaz
    p = "f07"
    ex = [
        (
            "e1",
            "GEÇİCİ GÖREVLİ",
            "<b>≤ 24 ay</b> geçici görevlendirilen kamu görevlisi",
            False,
        ),
        (
            "e2",
            "VATANDAŞLIKTAN ÇIKAN",
            "<b>çıkma izniyle</b> Türk vatandaşlığından çıkıp yabancı vatandaşlık kazanan",
            False,
        ),
        ("e3", "ÇİFT UYRUKLU", "çift uyruklu kişiler", True),
    ]
    cards = []
    for i, (k, t, b, ok) in enumerate(ex):
        x = 69 + i * 610
        hdr = DARK if ok else RED
        cards.append(
            f'<div id="{p}-{k}" class="{p}-card" style="left:{x}px;top:300px;width:560px;height:330px">'
            f'<div class="{p}-lh2" style="background:{hdr}">{t}</div>'
            f'<div class="{p}-txt" style="left:28px;right:24px;top:110px;font-size:30px">{b}</div></div>'
        )
        if ok:
            cards.append(
                f'<div id="{p}-s{i + 1}" class="{p}-stamp {p}-ok" style="left:{x + 120}px;top:560px">'
                f"{svg_check(40, DARK)} YARARLANIR</div>"
            )
        else:
            cards.append(
                f'<div id="{p}-s{i + 1}" class="{p}-stamp" style="left:{x + 90}px;top:560px">YARARLANAMAZ</div>'
            )
    F[7] = dict(
        slug="istisnalar",
        css=f"""
.{p}-lh2 {{ position:absolute; left:0; right:0; top:0; height:64px; color:#fff; display:flex; align-items:center; padding:0 24px;
  font-family:'Space Grotesk'; font-weight:600; font-size:23px; letter-spacing:2.5px; white-space:nowrap; }}
""",
        html="\n".join(
            [
                eyebrow(p, "İSTİSNA · MD. 12"),
                sh(p, "Kimler yararlanamaz?"),
                *cards,
                cite(p, "md. 12"),
            ]
        ),
    )

    # 8 — getirme süresi
    p = "f08"
    F[8] = dict(
        slug="getirme-suresi",
        css=f"""
.{p}-line {{ position:absolute; height:6px; background:{DARK}; transform-origin:left center; }}
.{p}-dot {{ position:absolute; width:34px; height:34px; margin:-14px 0 0 -17px; border-radius:50%; background:{DARK}; }}
.{p}-br {{ position:absolute; height:22px; border:5px solid {RED}; border-top:none; box-sizing:border-box; transform-origin:left center; }}
.{p}-brl {{ position:absolute; font-family:'Shrikhand'; font-size:44px; color:{RED_T}; white-space:nowrap; }}
.{p}-pl {{ position:absolute; font-family:'Space Grotesk'; font-weight:600; font-size:20px; letter-spacing:2.5px;
  text-transform:uppercase; color:{MUTED}; white-space:nowrap; }}
.{p}-note {{ position:absolute; font-size:28px; font-style:italic; color:{MUTED}; white-space:nowrap; }}
""",
        html="\n".join(
            [
                eyebrow(p, "SÜRE · MD. 13"),
                sh(p, "Ne zaman getirilir?"),
                f'<div id="{p}-t1" class="{p}-tag {p}-darkbg" style="left:69px;top:300px">a · b · c</div>',
                f'<div id="{p}-l1" class="{p}-line" style="left:300px;top:320px;width:1520px"></div>',
                f'<div id="{p}-d1" class="{p}-dot" style="left:880px;top:323px"></div>',
                f'<div id="{p}-g1" class="{p}-tag" style="left:828px;top:244px">GELİŞ</div>',
                f'<div id="{p}-p1" class="{p}-pl" style="left:470px;top:360px">ÖNCE</div>',
                f'<div id="{p}-p2" class="{p}-pl" style="left:800px;top:360px">BERABER</div>',
                f'<div id="{p}-br1" class="{p}-br" style="left:900px;top:350px;width:640px"></div>',
                f'<div id="{p}-bl1" class="{p}-brl" style="left:1100px;top:390px">sonra 6 ay</div>',
                f'<div id="{p}-t2" class="{p}-tag {p}-darkbg" style="left:69px;top:560px">ç · mirasçı</div>',
                f'<div id="{p}-l2" class="{p}-line" style="left:300px;top:580px;width:1520px"></div>',
                f'<div id="{p}-d2" class="{p}-dot" style="left:520px;top:583px"></div>',
                f'<div id="{p}-g2" class="{p}-tag" style="left:420px;top:504px">VERASET İLAMI</div>',
                f'<div id="{p}-br2" class="{p}-br" style="left:540px;top:610px;width:1200px"></div>',
                f'<div id="{p}-bl2" class="{p}-brl" style="left:1060px;top:650px">24 ay</div>',
                f'<div id="{p}-note" class="{p}-note" style="left:300px;top:760px">mücbir sebep ve beklenmeyen haller saklı</div>',
                cite(p, "md. 13"),
            ]
        ),
    )

    # 9 — ülkeden ülkeye atanan (md. 15)
    p = "f09"
    chk = svg_check(30, RED_T, 5)
    F[9] = dict(
        slug="ulkeden-ulkeye",
        css=f"""
.{p}-box {{ position:absolute; height:120px; background:{PAPER}; border:4px solid {DARK}; display:flex; align-items:center;
  justify-content:center; font-family:'Shrikhand'; font-size:44px; color:{DARK}; box-sizing:border-box; }}
.{p}-al {{ position:absolute; font-family:'Space Grotesk'; font-weight:600; font-size:20px; letter-spacing:2px;
  text-transform:uppercase; color:{DARK}; white-space:nowrap; text-align:center; }}
.{p}-al b {{ color:{RED_T}; font-weight:600; }}
.{p}-ret {{ position:absolute; border:5px solid {DARK}; border-top:none; box-sizing:border-box; }}
.{p}-info {{ position:absolute; width:0; border-left:4px dashed {MUTED}; }}
""",
        html="\n".join(
            [
                eyebrow(p, "MD. 15"),
                sh(p, "Ülkeden ülkeye atanan"),
                f'<div id="{p}-sub" class="{p}-body" style="left:72px;top:222px;font-size:28px">yeni ülkeye <b>götüremediği</b> ev eşyası için de</div>',
                f'<div id="{p}-k1" class="{p}-box" style="left:69px;top:330px;width:300px">KİŞİ</div>',
                f'<div id="{p}-a1" class="{p}-abs" style="left:384px;top:368px">{svg_arrow(360, 44, 6, DARK)}</div>',
                f'<div id="{p}-al1" class="{p}-al" style="left:384px;top:300px;width:360px">dilekçe + <b>4 nüsha</b> liste</div>',
                f'<div id="{p}-k2" class="{p}-box" style="left:760px;top:330px;width:320px">KURUM</div>',
                f'<div id="{p}-a2" class="{p}-abs" style="left:1096px;top:368px">{svg_arrow(360, 44, 6, DARK)}</div>',
                f'<div id="{p}-al2" class="{p}-al" style="left:1096px;top:300px;width:360px">uygun görürse · <b>3 nüsha</b></div>',
                f'<div id="{p}-k3" class="{p}-box" style="left:1470px;top:330px;width:370px;background:{DARK};color:#fff">GÜMRÜK</div>',
                f'<div id="{p}-ins" class="{p}-card" style="left:1180px;top:500px;width:660px;height:150px">'
                f'<div class="{p}-txt" style="left:24px;top:20px;font-size:26px">{chk} kullanılmış ev eşyası mı?<br>{chk} getirilmesi zorunlu mu?</div></div>',
                f'<div id="{p}-info" class="{p}-info" style="left:920px;top:454px;height:110px"></div>',
                f'<div id="{p}-infol" class="{p}-al" style="left:780px;top:574px;width:280px;color:{MUTED}">kuruma bilgi</div>',
                f'<div id="{p}-ret" class="{p}-ret" style="left:218px;top:454px;width:1440px;height:290px" data-layout-allow-overlap></div>',
                f'<div id="{p}-retl" class="{p}-tag" style="left:560px;top:722px">ONAYLI LİSTE ÖRNEĞİ → KİŞİYE</div>',
                cite(p, "md. 15", x=1700),
            ]
        ),
    )

    # 10 — mükerrer kullanım (md. 16)
    p = "f10"
    parts = "".join(
        f'<div id="{p}-p{i + 1}" class="{p}-abs" style="left:{960 + i * 280}px;top:430px">{box_svg(220, 150, label=False)}'
        f'<div class="{p}-pn">{i + 1}. parti</div></div>'
        for i in range(3)
    )
    F[10] = dict(
        slug="mukerrer",
        css=f"""
.{p}-scr {{ position:absolute; background:{DARK}; color:#fff; border:4px solid {DARK}; }}
.{p}-st {{ position:absolute; font-family:'Space Grotesk'; font-weight:600; font-size:26px; letter-spacing:2.5px; color:#fff;
  white-space:nowrap; display:flex; align-items:center; gap:14px; }}
.{p}-band {{ position:absolute; border:4px dashed {DARK}; box-sizing:border-box; }}
.{p}-bandl {{ position:absolute; font-family:'Space Grotesk'; font-weight:600; font-size:20px; letter-spacing:2.5px;
  text-transform:uppercase; color:{DARK}; white-space:nowrap; }}
.{p}-pn {{ font-family:'Space Grotesk'; font-weight:600; font-size:20px; letter-spacing:2px; text-transform:uppercase;
  color:{DARK}; text-align:center; margin-top:8px; }}
""",
        html="\n".join(
            [
                eyebrow(p, "KONTROL · MD. 16"),
                sh(p, "Mükerrer mi?"),
                f'<div id="{p}-scr" class="{p}-scr" style="left:69px;top:300px;width:720px;height:420px">'
                f'<div class="{p}-abs" style="left:34px;top:26px;font-family:Shrikhand;font-size:72px">BİLGE</div>'
                f'<div class="{p}-st" style="left:36px;top:150px">{svg_check(34, "#fff", 5)} KİŞİNİN KENDİSİ</div>'
                f'<div class="{p}-st" style="left:36px;top:210px">{svg_check(34, "#fff", 5)} AİLE ÜNİTESİ</div>'
                f'<div class="{p}-st" style="left:36px;top:300px;font-size:30px">HAK MÜKERRER Mİ?</div></div>',
                f'<div id="{p}-band" class="{p}-band" style="left:930px;top:400px;width:900px;height:250px"></div>',
                f'<div id="{p}-bandl" class="{p}-bandl" style="left:930px;top:356px">md. 13 süresi içinde</div>',
                parts,
                f'<div id="{p}-not" class="{p}-stamp {p}-ok" style="left:1130px;top:680px">MÜKERRER DEĞİL</div>',
                cite(p, "md. 16"),
            ]
        ),
    )

    # 11 — üç sayı (kırmızı panel)
    p = "f11"
    nums = [
        ("n1", "24", "ay dışarıda"),
        ("n2", "6", "ay · yılda en çok içeride"),
        ("n3", "6", "ay içinde beyan · gelişten sonra"),
    ]
    nn = []
    for i, (k, num, cap) in enumerate(nums):
        x = 120 + i * 590
        nn.append(
            f'<div id="{p}-{k}" class="{p}-abs" style="left:{x}px;top:260px;width:540px">'
            f'<div class="{p}-big">{num}</div><div class="{p}-cap">{cap}</div></div>'
        )
    F[11] = dict(
        slug="uc-sayi",
        ground=RED,
        prog=DARK,
        css=f"""
.{p}-big {{ font-family:'Shrikhand'; font-size:240px; line-height:1; color:#fff; text-shadow:{SHADOW}; }}
.{p}-cap {{ font-size:36px; line-height:1.35; color:#fff; margin-top:20px; }}
""",
        html="\n".join(
            [
                eyebrow(p, "KISACASI · ÜÇ SAYI", extra=f" {p}-white"),
                *nn,
            ]
        ),
    )

    # 12 — logo
    p = "f12"
    F[12] = dict(
        slug="kapanis",
        ground=BG,
        css=f"""
.{p}-handle {{ position:absolute; font-family:'Space Grotesk'; font-weight:600; font-size:31px; letter-spacing:5px; color:{DARK}; text-align:center; }}
""",
        html="\n".join(
            [
                f'<img id="{p}-logo" class="{p}-abs" src="public/logo-ufuk-cetintas.png" alt="Ufuk Çetintaş — Gümrük Eğitim Koçu" '
                f'style="left:576px;top:150px;width:768px;height:auto">',
                f'<div id="{p}-handle" class="{p}-handle" style="left:0;top:650px;width:{W}px">@GUMRUKKOCUNUZ</div>',
            ]
        ),
    )
    for n in F:
        F[n].setdefault("ground", GROUND)
    return F
