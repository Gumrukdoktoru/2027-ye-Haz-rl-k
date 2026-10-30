#!/usr/bin/env python3
"""Özet beyanda aykırılıklar (GK 237) — sahne yerleşimleri (taslak ve video ortak kaynağı).

Her sahne, son (yerleşmiş) halini 1920×1080 piksel koordinatlarla tanımlar. Aynı tanım hem taslak
sayfasında (storyboard.html, hareketsiz) hem de sahne dosyalarında (compositions/frames/*.html,
hareketli) kullanılır. Zemin bu videoya özel: lacivert liman gecesi; belgeler kırık beyaz kâğıt.
"""

import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W, H = 1920, 1080
NAVY, SEA = "#0E2640", "#0A1D33"
INK, MUTED = "#F5F2EF", "#A9BBCD"  # yazı (lacivert üstünde)
PAPER, DARK = "#F5F2EF", "#1C1410"  # belge kâğıdı ve mürekkep
RED, RED_T = "#D8000F", "#FF5A4E"  # eksik: dolgu / lacivert üstünde yazı-çizgi
AMBER = "#FFB21E"  # fazla
BG = "#FFFFFF"  # kapanış
SHADOW = "2px 2px 0 rgba(28,20,16,.25), 4px 4px 0 rgba(28,20,16,.2), 6px 6px 0 rgba(28,20,16,.15)"
GROUND = f"linear-gradient(to bottom, {NAVY} 0, {NAVY} 900px, {SEA} 900px, {SEA} 100%)"
N_FRAMES = 12

FONT_FACES = (
    open(os.path.join(ROOT, "assets/fonts.css"))
    .read()
    .replace("url('fonts/", "url('assets/fonts/")
)


# ------------------------------------------------------------------ glyphs (fontta yok → SVG)
def svg_arrow(w, h, stroke, color, pid=None, cls="glyph"):
    idattr = f' id="{pid}"' if pid else ""
    return (
        f'<svg{idattr} class="{cls}" width="{w}" height="{h}" viewBox="0 0 {w} {h}" aria-hidden="true">'
        f'<path d="M{stroke} {h / 2} H{w - stroke * 1.5} M{w - h * 0.42} {h * 0.14} L{w - stroke} {h / 2} L{w - h * 0.42} {h * 0.86}" '
        f'fill="none" stroke="{color}" stroke-width="{stroke}" stroke-linecap="square"/></svg>'
    )


def svg_check(s, color, stroke=7):
    return (
        f'<svg class="glyph" width="{s}" height="{s}" viewBox="0 0 {s} {s}" aria-hidden="true">'
        f'<path d="M{s * .14} {s * .52} L{s * .4} {s * .78} L{s * .88} {s * .2}" fill="none" stroke="{color}" '
        f'stroke-width="{stroke}" stroke-linecap="square"/></svg>'
    )


def kap_svg(w, h, stroke, fill="none", dash=False, sw=5, ribs=True):
    """Konteyner kabı: dikdörtgen + oluklu kaburgalar; dash=True boş yuva."""
    d = ' stroke-dasharray="14 10"' if dash else ""
    body = f'<rect x="{sw / 2}" y="{sw / 2}" width="{w - sw}" height="{h - sw}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'
    if ribs and not dash:
        n = max(4, int(w / 34))
        for i in range(1, n):
            x = round(w * i / n, 1)
            body += f'<path d="M{x} {h * .18} V{h * .82}" stroke="{stroke}" stroke-width="{max(2, sw * .5)}"/>'
    return f'<svg width="{w}" height="{h}" viewBox="0 0 {w} {h}" aria-hidden="true">{body}</svg>'


def ship_svg():
    """Sade gemi silüeti; güverte üstünde kaplar (540×250)."""
    s = f'stroke="{INK}" stroke-width="5" fill="none" stroke-linejoin="round"'
    boxes = ""
    for i, (x, y, c) in enumerate(
        [
            (70, 96, INK),
            (160, 96, INK),
            (250, 96, INK),
            (340, 96, INK),
            (115, 46, INK),
            (205, 46, RED_T),
            (295, 46, INK),
        ]
    ):
        boxes += f'<rect x="{x}" y="{y}" width="84" height="46" fill="{NAVY}" stroke="{c}" stroke-width="5"/>'
    return (
        f'<svg width="540" height="250" viewBox="0 0 540 250" aria-hidden="true">'
        f'<path d="M10 150 H530 L486 240 H58 Z" {s}/>'
        f'<path d="M430 150 V70 H500 V150" {s}/><path d="M446 92 H484" {s}/>{boxes}</svg>'
    )


# ------------------------------------------------------------------ shared CSS
def css_common(p, ground):
    return f"""
{FONT_FACES}
#root {{ position:absolute; inset:0; width:{W}px; height:{H}px; overflow:hidden; color:{INK};
  font-family:'Libre Baskerville', serif; }}
#{p}-bg {{ position:absolute; inset:0; background:{ground}; }}
#root .{p}-abs {{ position:absolute; }}
.glyph {{ display:inline-block; vertical-align:middle; }}
.{p}-eyebrow {{ position:absolute; font-family:'Space Grotesk'; font-weight:600; font-size:19px; letter-spacing:3.5px;
  text-transform:uppercase; color:{RED_T}; white-space:nowrap; }}
.{p}-white {{ color:#fff; }}
.{p}-dark {{ color:{DARK}; }}
.{p}-hero {{ position:absolute; font-family:'Shrikhand'; font-size:150px; line-height:.92; color:{INK};
  transform-origin:left top; white-space:nowrap; }}
.{p}-red {{ color:{RED_T}; }}
.{p}-amber {{ color:{AMBER}; }}
.{p}-sh {{ position:absolute; font-family:'Shrikhand'; font-size:63px; line-height:1.1; color:{INK}; white-space:nowrap; }}
.{p}-body {{ position:absolute; font-size:30px; line-height:1.5; color:{INK}; }}
.{p}-muted {{ color:{MUTED}; }}
.{p}-chip {{ position:absolute; font-family:'Space Grotesk'; font-weight:600; font-size:21px; letter-spacing:2px;
  text-transform:uppercase; border:3px solid {DARK}; padding:12px 18px; background:{PAPER}; color:{DARK}; white-space:nowrap; }}
.{p}-tag {{ position:absolute; font-family:'Space Grotesk'; font-weight:600; font-size:20px; letter-spacing:2.5px;
  text-transform:uppercase; background:{RED}; color:#fff; padding:7px 13px; white-space:nowrap; }}
.{p}-tag.{p}-amberbg {{ background:{AMBER}; color:{DARK}; }}
.{p}-tag.{p}-paperbg {{ background:{PAPER}; color:{DARK}; }}
.{p}-stamp {{ position:absolute; font-family:'Space Grotesk'; font-weight:600; font-size:24px; letter-spacing:3px;
  color:{RED_T}; border:5px solid {RED_T}; padding:9px 16px; white-space:nowrap; background:rgba(10,29,51,.88); }}
.{p}-stamp.{p}-onpaper {{ color:{RED}; border-color:{RED}; background:rgba(245,242,239,.94); }}
.{p}-stamp.{p}-amberst {{ color:{DARK}; border-color:{DARK}; background:{AMBER}; }}
.{p}-cite {{ position:absolute; left:69px; top:836px; font-family:'Space Grotesk'; font-weight:600; font-size:18px;
  letter-spacing:2px; text-transform:uppercase; border:2px solid {INK}; padding:6px 12px; color:{INK}; white-space:nowrap; }}
.{p}-prog {{ position:absolute; left:0; bottom:0; width:{W}px; height:10px; background:{RED}; transform-origin:left center; }}
.{p}-paper {{ position:absolute; background:{PAPER}; color:{DARK}; border:3px solid {DARK}; }}
.{p}-num {{ position:absolute; font-family:'Shrikhand'; font-size:64px; line-height:1; color:{RED}; }}
.{p}-lab {{ position:absolute; font-family:'Space Grotesk'; font-weight:600; font-size:20px; letter-spacing:2.5px;
  text-transform:uppercase; color:{DARK}; white-space:nowrap; }}
.{p}-txt {{ position:absolute; font-size:28px; line-height:1.4; color:{DARK}; }}
"""


def eyebrow(p, text, x=69, y=86, extra=""):
    return f'<div id="{p}-eyebrow" class="{p}-eyebrow{extra}" style="left:{x}px;top:{y}px">{text}</div>'


def cite(p, text):
    return f'<div id="{p}-cite" class="{p}-cite">{text}</div>'


def sh(p, text, top=140, left=69):
    return f'<div id="{p}-sh" class="{p}-sh" style="left:{left}px;top:{top}px">{text}</div>'


# ------------------------------------------------------------------ iki liste (sahne 1–2)
LIST_Y, LIST_W, LIST_H = 180, 390, 560
LIST_X = (1000, 1450)
ROW_Y0, ROW_H = 96, 72
OZET = ["01", "02", "03", "04", "05", None]  # None = satır yok (yuva)
BOSALTMA = ["01", "02", None, "04", "05", "06"]


def lists_css(p):
    return f"""
.{p}-lh {{ position:absolute; left:26px; top:26px; font-family:'Space Grotesk'; font-weight:600; font-size:22px;
  letter-spacing:3px; text-transform:uppercase; color:{DARK}; white-space:nowrap; }}
.{p}-row {{ position:absolute; left:20px; right:20px; height:{ROW_H - 8}px; display:flex; align-items:center; gap:18px;
  padding:0 8px; border-top:1.5px solid rgba(28,20,16,.35); font-family:'Space Grotesk'; font-weight:600;
  font-size:24px; letter-spacing:2px; color:{DARK}; }}
.{p}-row.{p}-hl-r {{ background:rgba(216,0,15,.13); }}
.{p}-row.{p}-hl-a {{ background:rgba(255,178,30,.42); }}
.{p}-row .{p}-x {{ color:rgba(28,20,16,.45); }}
"""


def lists_html(p, marked=False):
    out = []
    for li, (title, rows) in enumerate(
        (("ÖZET BEYAN", OZET), ("BOŞALTMA LİSTESİ", BOSALTMA))
    ):
        key = ("oz", "bo")[li]
        out.append(
            f'<div id="{p}-list-{key}" class="{p}-paper" style="left:{LIST_X[li]}px;top:{LIST_Y}px;width:{LIST_W}px;height:{LIST_H}px">'
        )
        out.append(f'<div class="{p}-lh">{title}</div>')
        for ri, code in enumerate(rows):
            y = ROW_Y0 + ri * ROW_H
            hl = ""
            if marked and ((key == "oz" and ri == 2) or (key == "bo" and ri == 2)):
                hl = f" {p}-hl-r"
            if marked and ((key == "oz" and ri == 5) or (key == "bo" and ri == 5)):
                hl = f" {p}-hl-a"
            rid = f"{p}-row-{key}-{ri + 1}"
            if code is None:
                col = (
                    RED
                    if (marked and ri == 2)
                    else (
                        ("#9A5B00" if marked else "rgba(28,20,16,.45)")
                        if ri == 5
                        else "rgba(28,20,16,.45)"
                    )
                )
                out.append(
                    f'<div id="{rid}" class="{p}-row{hl}" style="top:{y}px">{kap_svg(76, 42, col, dash=True, sw=3)}'
                    f'<span class="{p}-x">— yok —</span></div>'
                )
            else:
                fill = "none"
                stroke = DARK
                if marked and key == "oz" and ri == 2:
                    stroke, fill = RED, "rgba(216,0,15,.18)"
                if marked and key == "bo" and ri == 5:
                    fill = AMBER
                out.append(
                    f'<div id="{rid}" class="{p}-row{hl}" style="top:{y}px">{kap_svg(76, 42, stroke, fill, sw=3)}'
                    f"<span>KAP {code}</span></div>"
                )
        out.append("</div>")
    return "\n".join(out)


# ------------------------------------------------------------------ sol kap yuvası (sahne 3–5, 9)
SLOT_X, SLOT_Y, SLOT_W, SLOT_H = 69, 290, 500, 270


def slot_html(p, kind):
    """kind: 'noksan' (kırmızı kesik yuva) | 'fazla' (kehribar kap) | 'yok' (kehribar kap, listesiz)."""
    if kind == "noksan":
        art = kap_svg(SLOT_W, SLOT_H, RED_T, dash=True, sw=6)
        label, num, col = "NOKSAN KAP", "03", RED_T
    else:
        art = kap_svg(SLOT_W, SLOT_H, DARK, AMBER, sw=6)
        label, num, col = (
            ("FAZLA KAP", "06", AMBER)
            if kind == "fazla"
            else ("ÖZET BEYAN YOK", "?", AMBER)
        )
    numcol = col if kind == "noksan" else DARK
    return (
        f'<div id="{p}-slot" class="{p}-abs" style="left:{SLOT_X}px;top:{SLOT_Y}px;width:{SLOT_W}px;height:{SLOT_H}px">{art}'
        f'<div id="{p}-slotn" class="{p}-abs" style="left:0;top:0;width:{SLOT_W}px;height:{SLOT_H}px;display:flex;'
        f'align-items:center;justify-content:center;font-family:Shrikhand;font-size:120px;color:{numcol}">{num}</div></div>'
        f'<div id="{p}-slotl" class="{p}-tag{"" if kind == "noksan" else f" {p}-amberbg"}" style="left:{SLOT_X}px;top:{SLOT_Y - 52}px">{label}</div>'
    )


# ------------------------------------------------------------------ sonuç şeridi (sahne 5 ve 9)
CHAIN_X, CHAIN_Y0, CHAIN_W, CHAIN_H, CHAIN_STEP = 680, 250, 1160, 104, 128
CHAIN = [
    ("c1", "EL KONUR", ""),
    ("c2", "MÜLKİYETİ KAMUYA GEÇER", ""),
    ("c3", "TASFİYE", "md. 177–180"),
    ("c4", "+ CIF KIYMETİ KADAR PARA CEZASI", ""),
]


def chain_css(p):
    return f"""
.{p}-ch {{ position:absolute; left:{CHAIN_X}px; width:{CHAIN_W}px; height:{CHAIN_H}px; display:flex; align-items:center;
  gap:26px; padding:0 30px; background:{PAPER}; border:3px solid {DARK}; color:{DARK}; font-family:'Space Grotesk';
  font-weight:600; font-size:30px; letter-spacing:2.5px; white-space:nowrap; box-sizing:border-box; }}
.{p}-ch .{p}-chn {{ font-family:'Shrikhand'; font-size:52px; letter-spacing:0; color:{RED}; width:44px; }}
.{p}-ch .{p}-chs {{ font-family:'Libre Baskerville'; font-size:24px; letter-spacing:0; color:rgba(28,20,16,.7); }}
.{p}-ch.{p}-chred {{ background:{RED}; border-color:{RED}; color:#fff; }}
.{p}-ch.{p}-chred .{p}-chn {{ color:#fff; }}
"""


def chain_html(p):
    out = []
    for i, (k, t, s) in enumerate(CHAIN):
        red = f" {p}-chred" if k == "c4" else ""
        sub = f'<span class="{p}-chs">{s}</span>' if s else ""
        out.append(
            f'<div id="{p}-{k}" class="{p}-ch{red}" style="top:{CHAIN_Y0 + i * CHAIN_STEP}px">'
            f'<span class="{p}-chn">{i + 1}</span><span>{t}</span>{sub}</div>'
        )
    return "\n".join(out)


# ------------------------------------------------------------------ frames
def frame_specs():
    F = {}

    # 1 — iki liste
    p = "f01"
    F[1] = dict(
        slug="iki-liste",
        css=lists_css(p) + f"""
#{p}-ship {{ position:absolute; left:400px; top:650px; }}
""",
        html="\n".join(
            [
                eyebrow(p, "GÜMRÜK KOÇU · ÖZET BEYAN"),
                f'<div id="{p}-h1" class="{p}-hero" style="left:69px;top:170px">İki liste</div>',
                f'<div id="{p}-h2" class="{p}-hero {p}-red" style="left:80px;top:330px;transform:rotate(-4deg)" data-layout-allow-overlap>tutmazsa…</div>',
                f'<div id="{p}-body" class="{p}-body" style="left:72px;top:540px">Gümrük Kanunu <b>md. 237</b> devreye girer.</div>',
                f'<div id="{p}-ship">{ship_svg()}</div>',
                lists_html(p, marked=False),
                cite(p, "GK md. 237 · GY md. 75"),
            ]
        ),
    )

    # 2 — eksik mi, fazla mı
    p = "f02"
    F[2] = dict(
        slug="eksik-fazla",
        css=lists_css(p) + f"""
.{p}-def {{ position:absolute; left:69px; width:820px; font-size:32px; line-height:1.45; color:{INK}; }}
.{p}-stamp.{p}-rowst {{ font-size:18px; letter-spacing:2px; padding:5px 10px; border-width:4px; transform:rotate(-4deg); }}
""",
        html="\n".join(
            [
                eyebrow(p, "TANIM · GY MD. 75/3"),
                sh(p, "Eksik mi, fazla mı?"),
                f'<div id="{p}-t1" class="{p}-tag" style="left:69px;top:300px">EKSİK</div>',
                f'<div id="{p}-d1" class="{p}-def" style="top:356px">özet beyanda <b>var</b>, boşaltma listesinde <b>yok</b></div>',
                f'<div id="{p}-t2" class="{p}-tag {p}-amberbg" style="left:69px;top:520px">FAZLA</div>',
                f'<div id="{p}-d2" class="{p}-def" style="top:576px">boşaltma listesinde <b>var</b>, özet beyanda <b>yok</b></div>',
                lists_html(p, marked=True),
                f'<div id="{p}-st1" class="{p}-stamp {p}-onpaper {p}-rowst" style="left:1700px;top:{LIST_Y + ROW_Y0 + 2 * ROW_H + 11}px" data-layout-allow-overlap>EKSİK</div>',
                f'<div id="{p}-st2" class="{p}-stamp {p}-amberst {p}-rowst" style="left:1700px;top:{LIST_Y + ROW_Y0 + 5 * ROW_H + 11}px" data-layout-allow-overlap>FAZLA</div>',
                cite(p, "GY md. 75/3"),
            ]
        ),
    )

    # 3 — noksan kap: kanıt
    p = "f03"
    reasons = [
        ("r1", "1", "Mahrecinden <b>yüklenmedi</b>"),
        ("r2", "2", "Yanlışlıkla <b>başka yere</b> çıkarıldı"),
        ("r3", "3", "Kaza ve <b>avarya</b> ile yok oldu"),
        ("r4", "4", "<b>Çalındı</b>"),
    ]
    pos = [(680, 250), (1270, 250), (680, 420), (1270, 420)]
    cards = []
    for (k, n, t), (x, y) in zip(reasons, pos):
        cards.append(
            f'<div id="{p}-{k}" class="{p}-paper" style="left:{x}px;top:{y}px;width:570px;height:150px">'
            f'<div class="{p}-num" style="left:24px;top:38px">{n}</div>'
            f'<div class="{p}-txt" style="left:96px;right:20px;top:36px">{t}</div></div>'
        )
    hourglass = (
        f'<svg class="glyph" width="44" height="60" viewBox="0 0 44 60" aria-hidden="true">'
        f'<path d="M6 4 H38 M6 56 H38 M10 4 C10 22 34 26 34 30 C34 34 10 38 10 56 M34 4 C34 22 10 26 10 30 C10 34 34 38 34 56" '
        f'fill="none" stroke="{INK}" stroke-width="4"/></svg>'
    )
    F[3] = dict(
        slug="kanit",
        css=f"""
.{p}-sure {{ position:absolute; display:flex; align-items:center; gap:20px; font-size:32px; color:{INK}; white-space:nowrap; }}
.{p}-tir {{ position:absolute; border:2px dashed {MUTED}; padding:14px 18px; font-family:'Space Grotesk'; font-weight:600;
  font-size:19px; letter-spacing:1.5px; line-height:1.55; color:{MUTED}; text-transform:uppercase; }}
.{p}-tir b {{ color:{INK}; font-weight:600; }}
""",
        html="\n".join(
            [
                eyebrow(p, "NOKSAN KAP · GK MD. 237/1"),
                sh(p, "Ne kanıtlanmalı?"),
                slot_html(p, "noksan"),
                *cards,
                f'<div id="{p}-sure" class="{p}-sure" style="left:680px;top:620px">{hourglass}'
                f"<span><b>gümrük idaresince belirlenecek süre</b> içinde</span></div>",
                f'<div id="{p}-tir" class="{p}-tir" style="left:680px;top:716px;width:1160px">'
                f"TIR karnesinde: <b>3 ay</b> · talep üzerine <b>+3 ay</b> · haklı sebeple <b>+1 ay</b> &nbsp;(TIR Seri No: 6)</div>",
                cite(p, "GK md. 237/1"),
            ]
        ),
    )

    # 4 — ceza merdiveni
    p = "f04"
    steps = [
        (
            "s1",
            "1",
            "TARİFE POZİSYONU",
            "gümrük vergileri kadar para cezası",
            680,
            250,
            1160,
        ),
        (
            "s2",
            "2",
            "POZİSYON TESPİT EDİLEMİYORSA",
            "faslın en yüksek vergili pozisyonu esas",
            760,
            430,
            1080,
        ),
        (
            "s3",
            "3",
            "BU DA MÜMKÜN DEĞİLSE",
            "noksan her kap için 241/1'deki miktar",
            840,
            610,
            1000,
        ),
    ]
    st = []
    for k, n, lab, txt, x, y, w in steps:
        st.append(
            f'<div id="{p}-{k}" class="{p}-paper" style="left:{x}px;top:{y}px;width:{w}px;height:150px">'
            f'<div class="{p}-num" style="left:26px;top:38px">{n}</div>'
            f'<div class="{p}-lab" style="left:100px;top:30px">{lab}</div>'
            f'<div class="{p}-txt" style="left:100px;top:72px;white-space:nowrap">'
            f"{svg_arrow(40, 22, 4, DARK)}&nbsp; {txt}</div></div>"
        )
    F[4] = dict(
        slug="ceza-merdiveni",
        css="",
        html="\n".join(
            [
                eyebrow(p, "NOKSAN KAP · CEZA"),
                sh(p, "Kanıtlanamazsa"),
                slot_html(p, "noksan"),
                *st,
                cite(p, "GK md. 237/1–2"),
            ]
        ),
    )

    # 5 — fazla kap
    p = "f05"
    F[5] = dict(
        slug="fazla-kap",
        css=chain_css(p) + f"""
.{p}-q {{ position:absolute; width:500px; font-size:30px; line-height:1.45; color:{INK}; }}
""",
        html="\n".join(
            [
                eyebrow(p, "FAZLA KAP · GK MD. 237/3"),
                sh(p, "Fazla kap"),
                slot_html(p, "fazla"),
                f'<div id="{p}-q" class="{p}-q" style="left:69px;top:600px">Yanlışlıkla mahrecinden <b>fazla yüklendiği</b> kanıtlanamazsa:</div>',
                chain_html(p),
                cite(p, "GK md. 237/3"),
            ]
        ),
    )

    # 6 — dökme eşya
    p = "f06"
    G_X, G_W = 760, 1080
    per = G_W / 8.0
    pile = (
        f'<svg width="560" height="360" viewBox="0 0 560 360" aria-hidden="true">'
        f'<path d="M20 340 C120 300 170 90 280 60 C390 90 440 300 540 340 Z" fill="none" stroke="{INK}" stroke-width="6" stroke-linejoin="round"/>'
        + "".join(
            f'<circle cx="{cx}" cy="{cy}" r="5" fill="{INK}"/>'
            for cx, cy in [
                (250, 120),
                (300, 140),
                (220, 190),
                (280, 200),
                (340, 210),
                (180, 260),
                (240, 270),
                (310, 280),
                (370, 270),
                (420, 300),
                (130, 310),
                (200, 320),
                (270, 325),
                (350, 320),
            ]
        )
        + f'<path d="M0 346 H560" stroke="{INK}" stroke-width="6"/></svg>'
    )

    def gauge(gid, y, lim, label, sub):
        return (
            f'<div id="{p}-{gid}l" class="{p}-glab" style="left:{G_X}px;top:{y - 74}px">{label} <span class="{p}-gsub">{sub}</span></div>'
            f'<div id="{p}-{gid}" class="{p}-abs" style="left:{G_X}px;top:{y}px;width:{G_W}px;height:64px">'
            f'<div id="{p}-{gid}ok" class="{p}-abs {p}-gok" style="left:0;top:0;width:{per * lim:.0f}px;height:64px">TAKİBAT YOK</div>'
            f'<div class="{p}-abs {p}-gover" style="left:{per * lim:.0f}px;top:0;width:{G_W - per * lim:.0f}px;height:64px"></div>'
            f'<div id="{p}-{gid}m" class="{p}-abs {p}-gmark" style="left:{per * lim - 3:.0f}px;top:-14px;height:92px"></div>'
            f'<div class="{p}-abs {p}-gnum" style="left:{per * lim - 40:.0f}px;top:80px">%{lim}</div>'
            f'<div class="{p}-abs {p}-gnum {p}-gz" style="left:0;top:80px">%0</div></div>'
        )

    F[6] = dict(
        slug="dokme",
        css=f"""
.{p}-glab {{ position:absolute; font-family:'Space Grotesk'; font-weight:600; font-size:22px; letter-spacing:2.5px;
  text-transform:uppercase; color:{INK}; white-space:nowrap; }}
.{p}-gsub {{ font-family:'Libre Baskerville'; text-transform:none; letter-spacing:0; font-weight:400; font-size:22px; color:{MUTED}; }}
.{p}-gok {{ background:{PAPER}; color:{DARK}; font-family:'Space Grotesk'; font-weight:600; font-size:20px; letter-spacing:2.5px;
  display:flex; align-items:center; justify-content:center; transform-origin:left center; }}
.{p}-gover {{ background:repeating-linear-gradient(135deg, {RED} 0 14px, rgba(216,0,15,.45) 14px 28px); }}
.{p}-gmark {{ width:6px; background:{INK}; }}
.{p}-gnum {{ font-family:'Shrikhand'; font-size:40px; color:{INK}; white-space:nowrap; }}
.{p}-gz {{ font-size:28px; color:{MUTED}; }}
.{p}-note {{ position:absolute; font-family:'Space Grotesk'; font-weight:600; font-size:20px; letter-spacing:2px;
  text-transform:uppercase; color:{MUTED}; white-space:nowrap; }}
.{p}-note b {{ color:{INK}; font-weight:600; }}
""",
        html="\n".join(
            [
                eyebrow(p, "DÖKME EŞYA · GK MD. 237/4"),
                sh(p, "Dökme eşya"),
                f'<div id="{p}-pile" class="{p}-abs" style="left:69px;top:330px">{pile}</div>',
                gauge(
                    "g1",
                    330,
                    3,
                    "Dökme eşya",
                    "· oranı eşya cinsine göre Cumhurbaşkanı kararı, en çok",
                ),
                gauge(
                    "g2",
                    590,
                    6,
                    "Doğalgaz ürünleri",
                    "· boru hattıyla ithal edilenler hariç, en çok",
                ),
                f'<div id="{p}-note" class="{p}-note" style="left:{G_X}px;top:780px">Takibat yalnızca <b>aşan kısım</b> için · GY md. 75/7</div>',
                cite(p, "GK md. 237/4 · GY md. 75/7"),
            ]
        ),
    )

    # 7 — kap tamam, ölçü farklı
    p = "f07"
    kaps = []
    for i in range(5):
        x = 180 + i * 320
        kaps.append(
            f'<div id="{p}-k{i + 1}" class="{p}-abs" style="left:{x}px;top:300px">{kap_svg(280, 150, INK, NAVY, sw=6)}</div>'
            f'<div id="{p}-ok{i + 1}" class="{p}-abs" style="left:{x + 112}px;top:236px">{svg_check(56, INK)}</div>'
        )
    F[7] = dict(
        slug="kap-tamam",
        css=f"""
.{p}-cnt {{ position:absolute; font-family:'Shrikhand'; font-size:96px; color:{INK}; white-space:nowrap; }}
.{p}-diff {{ position:absolute; font-family:'Space Grotesk'; font-weight:600; font-size:26px; letter-spacing:3px;
  text-transform:uppercase; color:{INK}; white-space:nowrap; }}
.{p}-diff b {{ color:{AMBER}; font-weight:600; }}
""",
        html="\n".join(
            [
                eyebrow(p, "İSTİSNA · GY MD. 583/2"),
                sh(p, "Kap tamam, ölçü farklı"),
                *kaps,
                f'<div id="{p}-cnt" class="{p}-cnt" style="left:180px;top:500px">5 = 5</div>',
                f'<div id="{p}-diff" class="{p}-diff" style="left:184px;top:660px">sayı · baş · ağırlık: <b>farklı</b></div>',
                f'<div id="{p}-st" class="{p}-stamp" style="left:1180px;top:540px;font-size:44px;padding:16px 30px">TAKİBAT YOK</div>',
                cite(p, "GY md. 583/2"),
            ]
        ),
    )

    # 8 — belgedeki miktar
    p = "f08"
    F[8] = dict(
        slug="belgedeki-miktar",
        css=f"""
.{p}-line {{ position:absolute; left:28px; right:28px; height:2px; background:rgba(28,20,16,.3); }}
.{p}-box {{ position:absolute; border:4px solid {RED_T}; padding:22px 28px; font-family:'Space Grotesk'; font-weight:600;
  font-size:30px; letter-spacing:2.5px; color:{INK}; white-space:nowrap; }}
.{p}-md {{ position:absolute; font-family:'Shrikhand'; font-size:64px; line-height:1; color:{INK}; white-space:nowrap; padding:10px 22px; }}
.{p}-md.{p}-keep {{ border:5px solid {RED_T}; color:{RED_T}; }}
.{p}-strike {{ position:absolute; height:8px; background:{RED_T}; transform-origin:left center; }}
.{p}-only {{ position:absolute; font-family:'Space Grotesk'; font-weight:600; font-size:20px; letter-spacing:2.5px;
  text-transform:uppercase; color:{INK}; white-space:nowrap; }}
""",
        html="\n".join(
            [
                eyebrow(p, "GK MD. 237/5"),
                sh(p, "Belgedeki miktar"),
                f'<div id="{p}-doc" class="{p}-paper" style="left:69px;top:260px;width:660px;height:440px">'
                f'<div class="{p}-lab" style="left:28px;top:28px">REJİM BEYANI</div>'
                f'<div class="{p}-line" style="top:80px"></div>'
                f'<div class="{p}-txt" style="left:28px;top:110px">Eşya: <span style="opacity:.55">— — — —</span></div>'
                f'<div class="{p}-txt" style="left:28px;top:180px">Miktar: <b>belgelerde kayıtlı miktar</b></div>'
                f'<div class="{p}-line" style="top:260px"></div></div>',
                f'<div id="{p}-nt" class="{p}-tag" style="left:97px;top:600px">GÜMRÜK TESPİTİ YOK</div>',
                f'<div id="{p}-ar" class="{p}-abs" style="left:770px;top:330px">{svg_arrow(110, 44, 7, INK)}</div>',
                f'<div id="{p}-box" class="{p}-box" style="left:910px;top:300px">FARK = ÖZET BEYAN EKSİĞİ / FAZLASI</div>',
                f'<div id="{p}-m234" class="{p}-md" style="left:910px;top:520px">md. 234</div>',
                f'<div id="{p}-strike" class="{p}-strike" style="left:906px;top:566px;width:300px" data-layout-allow-overlap></div>',
                f'<div id="{p}-m237" class="{p}-md {p}-keep" style="left:1300px;top:510px">md. 237</div>',
                f'<div id="{p}-only" class="{p}-only" style="left:1306px;top:640px">ceza gerekirse yalnızca bu madde</div>',
                cite(p, "GK md. 237/5"),
            ]
        ),
    )

    # 9 — özet beyansız eşya
    p = "f09"
    F[9] = dict(
        slug="ozet-beyansiz",
        css=chain_css(p) + f"""
.{p}-trg {{ position:absolute; left:69px; width:520px; font-size:26px; line-height:1.4; color:{INK};
  border-left:5px solid {AMBER}; padding-left:18px; }}
""",
        html="\n".join(
            [
                eyebrow(p, "GK MD. 237/6"),
                sh(p, "Özet beyansız eşya"),
                slot_html(p, "yok"),
                f'<div id="{p}-tr1" class="{p}-trg" style="top:600px">gümrük idaresince <b>belirlendi</b></div>',
                f'<div id="{p}-tr2" class="{p}-trg" style="top:668px">boşaltma izninden sonra bildirildi, <b>hiçbir özet beyanla ilişkisi yok</b></div>',
                chain_html(p),
                cite(p, "GK md. 237/6"),
            ]
        ),
    )

    # 10 — ceza kimden
    p = "f10"
    F[10] = dict(
        slug="kimden",
        css=f"""
.{p}-who {{ position:absolute; font-family:'Shrikhand'; font-size:54px; line-height:1.12; color:{DARK}; }}
.{p}-dash {{ position:absolute; width:0; border-left:4px dashed {INK}; transform-origin:center top; }}
.{p}-alt {{ position:absolute; display:flex; align-items:center; gap:22px; border:3px solid {INK}; padding:20px 26px;
  font-family:'Space Grotesk'; font-weight:600; font-size:26px; letter-spacing:2.5px; color:{INK}; white-space:nowrap; }}
.{p}-alt b {{ color:{AMBER}; font-weight:600; }}
""",
        html="\n".join(
            [
                eyebrow(p, "GK MD. 237/7"),
                sh(p, "Ceza kimden alınır?"),
                f'<div id="{p}-a" class="{p}-paper" style="left:69px;top:270px;width:800px;height:330px">'
                f'<div class="{p}-lab" style="left:34px;top:32px;color:{RED}">1., 2. VE 3. FIKRA</div>'
                f'<div class="{p}-who" style="left:34px;top:90px">Özet beyanı<br>veren</div></div>',
                f'<div id="{p}-b" class="{p}-paper" style="left:960px;top:270px;width:880px;height:330px">'
                f'<div class="{p}-lab" style="left:34px;top:32px;color:{RED}">6. FIKRA</div>'
                f'<div class="{p}-who" style="left:34px;top:90px">Özet beyanı vermekle<br>yükümlü kişi</div></div>',
                f'<div id="{p}-dash" class="{p}-dash" style="left:1398px;top:604px;height:70px"></div>',
                f'<div id="{p}-alt" class="{p}-alt" style="left:1100px;top:680px">tespit edilemezse {svg_arrow(46, 26, 5, INK)} <b>EŞYAYI GETİREN</b></div>',
                cite(p, "GK md. 237/7"),
            ]
        ),
    )

    # 11 — kısacası (kırmızı panel)
    p = "f11"
    rows = [
        ("r1", "Noksan", "vergi kadar ceza"),
        ("r2", "Fazla", "el koyma + CIF"),
        ("r3", "Dökme", "%3'e kadar takibat yok"),
    ]
    rr = []
    for i, (k, a, b) in enumerate(rows):
        y = 230 + i * 190
        rr.append(
            f'<div id="{p}-{k}" class="{p}-abs {p}-rowk" style="left:120px;top:{y}px">'
            f'<span class="{p}-big">{a}</span>{svg_arrow(90, 50, 8, "#fff")}<span class="{p}-sm">{b}</span></div>'
        )
    F[11] = dict(
        slug="kisacasi",
        ground=RED,
        prog=DARK,
        css=f"""
.{p}-rowk {{ display:flex; align-items:center; gap:36px; white-space:nowrap; }}
.{p}-big {{ font-family:'Shrikhand'; font-size:104px; line-height:1; color:#fff; text-shadow:{SHADOW}; width:520px; }}
.{p}-sm {{ font-size:50px; color:#fff; }}
""",
        html="\n".join(
            [
                eyebrow(p, "KISACASI · GK MD. 237", extra=f" {p}-white"),
                *rr,
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
