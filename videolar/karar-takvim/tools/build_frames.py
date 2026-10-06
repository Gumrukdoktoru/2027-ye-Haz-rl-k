#!/usr/bin/env python3
"""Karar · Takvim — sahne (frame) kompozisyonlarını üretir.

Onaylanan taslak (storyboard.html v1) yerleşimini ve audio_meta.json kelime
zamanlarını kullanarak compositions/frames/NN-*.html dosyalarını yazar.
Takvim ızgarası tüm sahnelerde aynı ölçüyle üretildiği için geçişlerde kıpırdamaz.

Kullanım:  python3 tools/build_frames.py   (proje kökünden)
"""
import json
import math
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
W, H = 1920, 1080
RED, DARK, BG, LIGHT = "#D8000F", "#1C1410", "#FFFFFF", "#F5F2EF"
SHADOW = "2px 2px 0 rgba(28,20,16,.25), 4px 4px 0 rgba(28,20,16,.2), 6px 6px 0 rgba(28,20,16,.15)"
N_FRAMES = 10

FONT_FACES = open(os.path.join(ROOT, "assets/fonts.css")).read().replace("url('fonts/", "url('assets/fonts/")
META = json.load(open(os.path.join(ROOT, "audio_meta.json")))
DUR = {v["frame"]: v["duration_s"] for v in META["voices"]}
WORDS = {v["frame"]: v["words"] for v in META["voices"]}


def cue(frame, word, nth=1, offset=0.0):
    """Start time (s, frame-relative) of the nth occurrence of `word` in this frame's narration."""
    k = 0
    for w in WORDS[frame]:
        if w["text"] == word:
            k += 1
            if k == nth:
                return round(w["start"] + offset, 3)
    raise KeyError(f"frame {frame}: word {word!r} #{nth} not found")


# ---------------------------------------------------------------- SVG glyphs
# →, ≠ and ⇄ are missing from the bundled fonts, so they are drawn as SVG.
def svg_arrow(w, h, stroke, color):
    return (f'<svg class="glyph" width="{w}" height="{h}" viewBox="0 0 {w} {h}" aria-hidden="true">'
            f'<path d="M{stroke} {h/2} H{w-stroke*1.5} M{w-h*0.42} {h*0.14} L{w-stroke} {h/2} L{w-h*0.42} {h*0.86}" '
            f'fill="none" stroke="{color}" stroke-width="{stroke}" stroke-linecap="square"/></svg>')


def svg_neq(size, color):
    s = size
    return (f'<svg class="glyph" width="{s}" height="{s}" viewBox="0 0 100 100" aria-hidden="true">'
            f'<path d="M14 38 H86 M14 64 H86 M66 12 L34 90" fill="none" stroke="{color}" stroke-width="13" '
            f'stroke-linecap="square"/></svg>')


def svg_swap(w, h, color, pid):
    return (f'<svg id="{pid}" width="{w}" height="{h}" viewBox="0 0 270 170" aria-hidden="true">'
            f'<path d="M20 55 H235 M190 15 L240 55 L190 95" fill="none" stroke="{color}" stroke-width="18" stroke-linecap="square"/>'
            f'<path d="M250 120 H35 M80 80 L30 120 L80 160" fill="none" stroke="{color}" stroke-width="18" stroke-linecap="square"/>'
            f'</svg>')


# ---------------------------------------------------------------- calendar
class Cal:
    """A fin-grid calendar. Geometry is fixed per stage so frames line up exactly."""

    def __init__(self, p, left, top, width, rows, row_h, days=35, numbered=None, cols=7, label="TAKVİM · GÜN"):
        self.p, self.left, self.top, self.width = p, left, top, width
        self.rows, self.row_h, self.days, self.cols = rows, row_h, days, cols
        self.numbered = days if numbered is None else numbered
        self.label = label
        self.grid_top = top + 38
        self.cell_w = width / cols

    def center(self, d):
        r, c = divmod(d, self.cols)
        return (self.left + (c + 0.5) * self.cell_w, self.grid_top + (r + 0.5) * self.row_h)

    def html(self, rings=(), dim_rings=(), fills=(), hatch=(), tags=None, up=(), numbers=True,
             frame_cell=None, label_id=None, later=()):
        """later: ringed days whose ring is drawn mid-frame — their small numeral shows until then."""
        p = self.p
        tags = tags or {}
        out = [f'<div id="{p}-cal" class="{p}-calwrap" style="left:{self.left}px;top:{self.top}px;width:{self.width}px">',
               f'<div id="{label_id or p + "-callabel"}" class="{p}-eyebrow {p}-dark {p}-static">{self.label}</div>',
               f'<div class="{p}-cal" style="grid-template-columns:repeat({self.cols},1fr);grid-template-rows:repeat({self.rows},{self.row_h}px)">']
        for d in range(self.days):
            if d >= self.numbered:
                out.append(f'<div class="{p}-d {p}-blank"></div>')
                continue
            inner = f'<div id="{p}-fill-{d}" class="{p}-fill" style="opacity:{1 if d in fills else 0}"></div>'
            if d in hatch:
                inner += f'<div id="{p}-hatch-{d}" class="{p}-hatch"></div>'
            if frame_cell == d:
                inner += f'<div id="{p}-cellframe-{d}" class="{p}-cellframe"></div>'
            show_small = numbers and (d not in rings or d in later) and d not in dim_rings
            inner += f'<span id="{p}-n-{d}" class="{p}-n" style="opacity:{1 if show_small else 0}">{d}</span>'
            out.append(f'<div class="{p}-d">{inner}</div>')
        out.append('</div></div>')
        # rings + tags live in an overlay so they can overhang cells
        r = min(self.cell_w, self.row_h) * 0.40
        circ = 2 * math.pi * r
        for d in list(rings) + list(dim_rings):
            cx, cy = self.center(d)
            dim = d in dim_rings
            out.append(
                f'<div id="{p}-ring-{d}" class="{p}-ring{" " + p + "-dimring" if dim else ""}" '
                f'style="left:{cx - r - 8:.1f}px;top:{cy - r - 8:.1f}px;width:{2 * r + 16:.1f}px;height:{2 * r + 16:.1f}px">'
                f'<svg width="{2 * r + 16:.1f}" height="{2 * r + 16:.1f}">'
                f'<circle id="{p}-ringc-{d}" cx="{r + 8:.1f}" cy="{r + 8:.1f}" r="{r:.1f}" '
                f'transform="rotate(-90 {r + 8:.1f} {r + 8:.1f})" style="stroke-dasharray:{circ:.1f};stroke-dashoffset:0"/></svg>'
                f'<span id="{p}-ringn-{d}" class="{p}-rn">{d}</span></div>')
        for d, text in tags.items():
            cx, cy = self.center(d)
            last_row = d // self.cols == self.rows - 1
            if d in up:
                y = cy - self.row_h / 2 - 34
            elif last_row:
                y = cy + self.row_h / 2 + 8
            else:  # sit in the middle of the next row, below its day numerals
                y = cy + self.row_h / 2 + 44
            out.append(f'<div id="{p}-tag-{d}" class="{p}-tag" style="left:{cx:.1f}px;top:{y:.1f}px">'
                       f'<span>{text}</span></div>')
        return "\n".join(out), circ


# ---------------------------------------------------------------- frame shell
def css_common(p, ground):
    return f"""
{FONT_FACES}
#root {{ position:absolute; inset:0; width:{W}px; height:{H}px; overflow:hidden; color:{DARK};
  font-family:'Libre Baskerville', serif; }}
#{p}-bg {{ position:absolute; inset:0; background:{ground}; }}
#root .{p}-abs {{ position:absolute; }}
.{p}-eyebrow {{ position:absolute; font-family:'Space Grotesk'; font-weight:600; font-size:19px; letter-spacing:3.5px;
  text-transform:uppercase; color:{RED}; white-space:nowrap; }}
.{p}-dark {{ color:{DARK}; }}
.{p}-white {{ color:#fff; }}
.{p}-static {{ position:static; margin-bottom:12px; }}
.{p}-stat {{ position:absolute; font-family:'Shrikhand'; font-size:422px; line-height:.82; color:{RED};
  transform-origin:left top; white-space:nowrap; }}
.{p}-hero {{ position:absolute; font-family:'Shrikhand'; font-size:173px; line-height:.88; color:{DARK};
  transform-origin:left top; white-space:nowrap; }}
.{p}-red {{ color:{RED}; }}
.{p}-heros {{ font-size:88px; }}
.{p}-sh {{ position:absolute; font-family:'Shrikhand'; font-size:63px; line-height:1.08; color:{DARK}; }}
.{p}-body {{ position:absolute; font-size:31px; line-height:1.6; white-space:nowrap; }}
.{p}-w {{ display:inline-block; }}
.{p}-card {{ position:absolute; padding-left:24px; }}
.{p}-bar {{ position:absolute; left:0; top:0; bottom:0; width:7px; background:{RED}; transform-origin:top; }}
.{p}-ct {{ font-family:'Shrikhand'; font-size:38px; line-height:1.1; margin-bottom:18px; }}
.{p}-li {{ position:relative; font-size:33px; line-height:1.5; padding-left:56px; margin-bottom:14px; }}
.{p}-li.{p}-big {{ font-size:36px; margin-bottom:26px; }}
.{p}-li > .{p}-mk {{ position:absolute; left:0; top:0; color:{RED}; font-family:'Space Grotesk'; font-weight:600; }}
.{p}-li b {{ font-weight:700; }}
.{p}-strk {{ position:relative; display:inline-block; }}
.{p}-strk > i.{p}-line {{ position:absolute; left:-4px; right:-4px; top:52%; height:6px; background:{RED};
  transform-origin:left center; }}
.{p}-uline {{ position:absolute; left:0; right:0; bottom:-4px; height:5px; background:{RED}; transform-origin:left center; }}
.glyph {{ display:inline-block; vertical-align:middle; }}
.{p}-cite {{ position:absolute; left:69px; top:836px; font-family:'Space Grotesk'; font-weight:600; font-size:18px;
  letter-spacing:2px; text-transform:uppercase; border:2px solid {DARK}; padding:6px 12px; background:{BG}; white-space:nowrap; }}
.{p}-prog {{ position:absolute; left:0; bottom:0; width:{W}px; height:10px; background:{RED}; transform-origin:left center; }}
.{p}-calwrap {{ position:absolute; }}
.{p}-cal {{ display:grid; gap:1.5px; background:{DARK}; border:3px solid {DARK}; }}
.{p}-d {{ position:relative; background:{BG}; overflow:hidden; }}
.{p}-blank {{ background:{LIGHT}; }}
.{p}-fill {{ position:absolute; inset:0; background:{LIGHT}; }}
.{p}-hatch {{ position:absolute; inset:0; background:repeating-linear-gradient(-45deg, {BG} 0 10px, {DARK} 10px 12.5px);
  transform-origin:left center; }}
.{p}-cellframe {{ position:absolute; inset:3px; border:5px solid {RED}; }}
.{p}-n {{ position:absolute; left:9px; top:6px; font-family:'Space Grotesk'; font-weight:600; font-size:18px; color:{DARK}; }}
.{p}-ring {{ position:absolute; display:flex; align-items:center; justify-content:center; }}
.{p}-ring svg {{ position:absolute; left:0; top:0; overflow:visible; }}
.{p}-ring circle {{ fill:{BG}; stroke:{RED}; stroke-width:6; }}
.{p}-dimring circle {{ stroke:{DARK}; stroke-width:3; }}
.{p}-rn {{ position:relative; font-family:'Shrikhand'; font-size:44px; color:{RED}; line-height:1; }}
.{p}-dimring .{p}-rn {{ color:{DARK}; }}
.{p}-tag {{ position:absolute; width:640px; margin-left:-320px; height:0; text-align:center; }}
.{p}-tag > span {{ display:inline-block; white-space:nowrap; font-family:'Space Grotesk';
  font-weight:600; font-size:16px; letter-spacing:2px; text-transform:uppercase; background:{DARK}; color:#fff; padding:5px 10px; }}
"""


def words_html(p, wid, words):
    return " ".join(f'<span id="{p}-{wid}-{i}" class="{p}-w">{w}</span>' for i, w in enumerate(words))


def write_frame(n, slug, body, css_extra, js, ground=BG, prog_color=RED):
    fid = f"{n:02d}-{slug}"
    p = f"f{n:02d}"
    dur = DUR[n]
    prog_from, prog_to = (n - 1) / N_FRAMES, n / N_FRAMES
    html = f"""<template>
<style>
{css_common(p, ground)}
.{p}-prog {{ background:{prog_color}; }}
{css_extra}
</style>
<div id="root" data-composition-id="{fid}" data-start="0" data-duration="{dur}" data-width="{W}" data-height="{H}">
<div id="{p}-bg" class="clip" data-start="0" data-duration="{dur}" data-track-index="0"></div>
{body}
<div id="{p}-prog" class="{p}-prog"></div>
</div>
<script>
(function () {{
  const tl = gsap.timeline({{ paused: true }});
  const E = "power3.out";
  const q = (s) => "#{p}-" + s;
  tl.fromTo(q("prog"), {{ scaleX: {prog_from} }}, {{ scaleX: {prog_to}, duration: {dur}, ease: "none" }}, 0);
{js}
  window.__timelines["{fid}"] = tl;
}})();
</script>
</template>
"""
    path = os.path.join(ROOT, "compositions/frames", fid + ".html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w").write(html)
    return fid


# JS helpers (strings)
def j_in(sel, t, y=24, d=0.5, x=0):
    return (f'  tl.fromTo(q("{sel}"), {{ opacity: 0, y: {y}, x: {x} }}, '
            f'{{ opacity: 1, y: 0, x: 0, duration: {d}, ease: E }}, {t});')


def j_fade(sel, t, d=0.5):
    return f'  tl.fromTo(q("{sel}"), {{ opacity: 0 }}, {{ opacity: 1, duration: {d}, ease: E }}, {t});'


def j_stamp(sel, t, rot, scale=1.35, d=0.5, rot_from=None):
    rf = rot - 8 if rot_from is None else rot_from
    return (f'  tl.fromTo(q("{sel}"), {{ opacity: 0, scale: {scale}, rotation: {rf} }}, '
            f'{{ opacity: 1, scale: 1, rotation: {rot}, duration: {d}, ease: E }}, {t});')


def j_strike(sel, t, d=0.4):
    return f'  tl.fromTo(q("{sel}"), {{ scaleX: 0 }}, {{ scaleX: 1, duration: {d}, ease: "power2.inOut" }}, {t});'


def j_ring(p, d, t, circ, dur=0.6):
    return "\n".join([
        f'  tl.fromTo(q("n-{d}"), {{ opacity: 1 }}, {{ opacity: 0, duration: 0.2, ease: E }}, {t});',
        f'  tl.fromTo(q("ringc-{d}"), {{ strokeDashoffset: {circ:.1f} }}, {{ strokeDashoffset: 0, duration: {dur}, ease: "power2.inOut" }}, {t});',
        f'  tl.fromTo(q("ringn-{d}"), {{ opacity: 0, scale: 0.6 }}, {{ opacity: 1, scale: 1, duration: 0.45, ease: E }}, {t + 0.15});',
    ])


def j_words(p, wid, times, y=24, d=0.4):
    return "\n".join(j_in(f"{wid}-{i}", t, y=y, d=d) for i, t in enumerate(times))


# Calendar stages (fixed geometry)
def cal_A(p, **kw):  # frames 1–5
    return Cal(p, left=900, top=148, width=940, rows=5, row_h=128, **kw)


def cal_B(p, **kw):  # frame 6 — itiraz
    return Cal(p, left=998, top=228, width=845, rows=5, row_h=116, numbered=31, label="İTİRAZ · 30 GÜN", **kw)


def cal_C(p, **kw):  # frames 7–8 — lehe karar şeridi
    return Cal(p, left=1210, top=208, width=634, rows=2, row_h=182, days=14, label="LEHE KARAR · YÜRÜRLÜK", **kw)


frames = []

# ------------------------------------------------------------------ 01
n, p = 1, "f01"
cal = cal_A(p, label="TAKVİM")
cal_html, _ = cal.html(numbers=False)
q_words = ["Peki", "bu", "otuz", "gün…", "ne", "zaman", "başlar?"]
body = f"""
<div id="{p}-eyebrow" class="{p}-eyebrow" style="left:69px;top:86px">GÜMRÜK KOÇU · KARAR</div>
<div id="{p}-stat" class="{p}-stat" style="left:77px;top:150px" data-layout-allow-overlap>30</div>
<div id="{p}-gun" class="{p}-hero" style="left:520px;top:392px;font-size:140px" data-layout-allow-overlap>GÜN</div>
<div id="{p}-q" class="{p}-sh" style="left:69px;top:628px;width:800px;line-height:1.45">{words_html(p, "qw", q_words)}</div>
{cal_html}
<div id="{p}-cite" class="{p}-cite">GK md. 6/2</div>
"""
js = "\n".join([
    j_fade("eyebrow", 0.0, 0.6),
    j_in("cal", 0.0, y=16, d=0.8),
    j_stamp("stat", cue(n, "otuz") - 0.1, -6, scale=1.5, rot_from=-16, d=0.55),
    j_in("gun", cue(n, "günü"), y=0, x=-40, d=0.45),
    j_fade("cite", cue(n, "var.")),
    j_words(p, "qw", [cue(n, w, 2 if w == "otuz" else 1) for w in q_words]),
])
frames.append(write_frame(n, "otuz-gun", body, "", js))

# ------------------------------------------------------------------ 02
n, p = 2, "f02"
cal = cal_A(p)
cal_html, circ = cal.html(rings=(0,), tags={0: "BAŞVURU İDAREYE ULAŞIR"}, later=(0,))
body = f"""
<div id="{p}-eyebrow" class="{p}-eyebrow" style="left:69px;top:86px">SÜRE NE ZAMAN BAŞLAR?</div>
<div id="{p}-gonder" class="{p}-abs" style="left:69px;top:196px;font-style:italic;font-size:61px">
  <span class="{p}-strk">gönderdiğin gün<i id="{p}-gline" class="{p}-line"></i></span></div>
<div id="{p}-hero" class="{p}-hero {p}-red" style="left:69px;top:360px">ulaştığı<br>gün.</div>
<div id="{p}-body" class="{p}-body" style="left:69px;top:760px">İdareye ulaştığı tarih = <b>0. gün</b></div>
{cal_html}
<div id="{p}-cite" class="{p}-cite">GK md. 6/2</div>
"""
num_js = "\n".join(
    f'  tl.fromTo(q("n-{d}"), {{ opacity: 0 }}, {{ opacity: 1, duration: 0.25, ease: E }}, {0.1 + d * 0.03:.2f});'
    for d in range(1, 35))
js = "\n".join([
    j_fade("eyebrow", 0.0),
    num_js,
    f'  tl.set(q("ring-0"), {{ opacity: 1 }}, 0);',
    f'  tl.fromTo(q("ringc-0"), {{ strokeDashoffset: {circ:.1f} }}, {{ strokeDashoffset: {circ:.1f}, duration: 0.01 }}, 0);',
    f'  tl.fromTo(q("ringn-0"), {{ opacity: 0 }}, {{ opacity: 0, duration: 0.01 }}, 0);',
    j_in("gonder", cue(n, "gönderdiğin"), d=0.45),
    j_strike("gline", cue(n, "değil")),
    j_stamp("hero", cue(n, "ULAŞTIĞI") - 0.05, -4, scale=1.25, rot_from=-12),
    j_ring(p, 0, cue(n, "gün.") - 0.1, circ),
    j_in("tag-0 > span", cue(n, "gün.") + 0.35, y=10, d=0.4),
    j_fade("cite", cue(n, "gün.") + 0.35),
    j_in("body", cue(n, "tuzakları"), d=0.5),
])
frames.append(write_frame(n, "ulastigi-gun", body, "", js))

# ------------------------------------------------------------------ 03
n, p = 3, "f03"
cal = cal_A(p)
cal_html, circ = cal.html(rings=(0,), frame_cell=0)
h_words = ["Talep", "yazılı", "yapılır."]
body = f"""
<div id="{p}-eyebrow" class="{p}-eyebrow" style="left:69px;top:86px">0. GÜN</div>
<div id="{p}-sh" class="{p}-sh" style="left:69px;top:150px;width:780px">{words_html(p, "hw", h_words)}</div>
<div id="{p}-card" class="{p}-card" style="left:69px;top:330px;width:760px">
  <i id="{p}-bar" class="{p}-bar"></i>
  <div id="{p}-ct" class="{p}-ct">Başvurunun şekli</div>
  <div id="{p}-li1" class="{p}-li"><span class="{p}-mk">—</span><b>YAZILI</b> talep
    <span class="{p}-strk">sözlü<i id="{p}-sline" class="{p}-line"></i></span> <i>(öngörülmemiş)</i></div>
  <div id="{p}-li2" class="{p}-li"><span class="{p}-mk">—</span>Gerekli bütün bilgi ve belgeler {svg_arrow(44, 26, 4, DARK)}
    <span style="position:relative;display:inline-block"><b>talep eden ibraz eder</b><i id="{p}-uline" class="{p}-uline"></i></span></div>
</div>
{cal_html}
<div id="{p}-cite" class="{p}-cite">GK md. 6/1 · 6/2</div>
"""
js = "\n".join([
    j_fade("eyebrow", 0.0, 0.4),
    j_fade("cellframe-0", 0.2, 0.5),
    j_fade("cite", 0.5),
    j_words(p, "hw", [cue(n, "talep"), cue(n, "yazılı"), cue(n, "yapılır;")]),
    f'  tl.fromTo(q("bar"), {{ scaleY: 0 }}, {{ scaleY: 1, duration: 0.5, ease: E }}, {cue(n, "sözlü") - 0.2});',
    j_in("ct", cue(n, "sözlü") - 0.1, d=0.45),
    j_in("li1", cue(n, "sözlü"), d=0.45),
    j_strike("sline", cue(n, "öngörülmemiş.")),
    j_in("li2", cue(n, "Gerekli"), d=0.45),
    j_strike("uline", cue(n, "talep", 3), d=0.5),
])
frames.append(write_frame(n, "yazili-talep", body, "", js))

# ------------------------------------------------------------------ 04
n, p = 4, "f04"
cal = cal_A(p)
cal_html, circ = cal.html(rings=(0, 30), fills=(), tags={30: "KARAR + YAZILI TEBLİĞ"}, later=(30,))
body = f"""
<div id="{p}-eyebrow" class="{p}-eyebrow" style="left:69px;top:86px" data-layout-allow-overlap>SAYAÇ</div>
<div id="{p}-stat" class="{p}-stat" style="left:69px;top:170px" data-layout-allow-overlap><span id="{p}-count">0</span></div>
<div id="{p}-sh" class="{p}-sh" style="left:69px;top:652px">gün içinde karar</div>
<div id="{p}-body" class="{p}-body" style="left:69px;top:748px">takvim günü · <span class="{p}-strk">iş günü<i id="{p}-iline" class="{p}-line"></i></span></div>
{cal_html}
<div id="{p}-cite" class="{p}-cite">GK md. 6/2</div>
"""
t0, t1 = cue(n, "otuz"), cue(n, "karar") + 0.45
step = (t1 - t0) / 30
fill_js = "\n".join(
    f'  tl.fromTo(q("fill-{d}"), {{ opacity: 0 }}, {{ opacity: 1, duration: 0.18, ease: "none" }}, {t0 + (d - 1) * step:.3f});'
    for d in range(1, 31))
js = "\n".join([
    j_fade("eyebrow", 0.0, 0.4),
    f'  tl.fromTo(q("stat"), {{ opacity: 0, rotation: -6 }}, {{ opacity: 1, rotation: -6, duration: 0.4, ease: E }}, 0.05);',
    f'  const c = {{ v: 0 }}; const el = document.querySelector(q("count"));',
    f'  tl.fromTo(c, {{ v: 0 }}, {{ v: 30, duration: {t1 - t0:.3f}, ease: "none", onUpdate: () => {{ el.textContent = String(Math.round(c.v)); }} }}, {t0});',
    fill_js,
    f'  tl.fromTo(q("ringc-30"), {{ strokeDashoffset: {circ:.1f} }}, {{ strokeDashoffset: {circ:.1f}, duration: 0.01 }}, 0);',
    f'  tl.fromTo(q("ringn-30"), {{ opacity: 0 }}, {{ opacity: 0, duration: 0.01 }}, 0);',
    j_in("sh", cue(n, "karar"), d=0.45),
    j_ring(p, 30, t1, circ),
    j_in("tag-30 > span", cue(n, "tebliğ"), y=10, d=0.4),
    j_fade("cite", cue(n, "tebliğ") + 0.2),
    j_in("body", cue(n, "Dikkat:"), d=0.45),
    j_strike("iline", cue(n, "iş")),
])
frames.append(write_frame(n, "otuzuncu-gun", body, "", js))

# ------------------------------------------------------------------ 05
n, p = 5, "f05"
cal = cal_A(p)
flag = f'<i style="display:inline-block;width:12px;height:12px;background:{RED};margin-right:8px;vertical-align:1px"></i>'
cal_html, circ = cal.html(rings=(0, 30), fills=range(1, 31), hatch=range(31, 35),
                          tags={26: flag + "SÜRE DOLMADAN BİLDİRİM", 32: "EK SÜRE"}, up=(26,))
body = f"""
<div id="{p}-eyebrow" class="{p}-eyebrow" style="left:69px;top:86px">30 GÜNE UYULAMAZSA</div>
<div id="{p}-sh" class="{p}-sh" style="left:69px;top:150px">Süre aşılabilir.</div>
<div id="{p}-card" class="{p}-card" style="left:69px;top:318px;width:760px">
  <i id="{p}-bar" class="{p}-bar"></i>
  <div id="{p}-ct" class="{p}-ct">Süre dolmadan bildirilir</div>
  <div id="{p}-li1" class="{p}-li"><span class="{p}-mk">—</span>Süre aşımını haklı kılan <b>gerekçeler</b></div>
  <div id="{p}-li2" class="{p}-li"><span class="{p}-mk">—</span>Karar için gerekli <b>ek süre</b></div>
</div>
<div id="{p}-hero" class="{p}-hero {p}-red {p}-heros" style="left:69px;top:690px">aşım {svg_neq(78, RED)} ret</div>
{cal_html}
<div id="{p}-cite" class="{p}-cite">GK md. 6/2</div>
"""
js = "\n".join([
    j_fade("eyebrow", 0.0, 0.4),
    j_fade("cite", 0.4),
    j_in("sh", cue(n, "süre"), d=0.45),
    "\n".join(f'  tl.fromTo(q("hatch-{d}"), {{ scaleX: 0 }}, {{ scaleX: 1, duration: 0.3, ease: "power2.out" }}, {cue(n, "aşılabilir.") + (d - 31) * 0.12:.3f});'
              for d in range(31, 35)),
    j_in("tag-32 > span", cue(n, "aşılabilir.") + 0.55, y=10, d=0.4),
    f'  tl.fromTo(q("bar"), {{ scaleY: 0 }}, {{ scaleY: 1, duration: 0.5, ease: E }}, {cue(n, "Ama") - 0.1});',
    j_in("ct", cue(n, "Ama"), d=0.45),
    j_in("tag-26 > span", cue(n, "dolmadan,"), y=-24, d=0.45),
    j_in("li1", cue(n, "gerekçeyi"), d=0.45),
    j_in("li2", cue(n, "ek"), d=0.45),
    j_stamp("hero", cue(n, "ret") - 0.05, -4, scale=1.3, rot_from=-12),
])
frames.append(write_frame(n, "sure-asimi", body, "", js))

# ------------------------------------------------------------------ 06
n, p = 6, "f06"
cal = cal_B(p)
cal_html, circ = cal.html(rings=(0, 30), tags={30: "KARARA BAĞLANIR"}, up=(30,), later=(0, 30))
stamp_css = f""".{p}-stamp {{ position:absolute; font-family:'Space Grotesk'; font-weight:600; font-size:24px; letter-spacing:3px;
  color:{RED}; border:5px solid {RED}; padding:10px 18px; white-space:nowrap; }}"""
body = f"""
<div id="{p}-eyebrow" class="{p}-eyebrow" style="left:69px;top:86px">KARARDAN SONRA</div>
<div id="{p}-st1" class="{p}-stamp" style="left:1000px;top:80px">GEREKÇELİ</div>
<div id="{p}-st2" class="{p}-stamp" style="left:1330px;top:92px">DERHAL UYGULANIR</div>
<div id="{p}-card" class="{p}-card" style="left:69px;top:200px;width:830px">
  <i id="{p}-bar" class="{p}-bar"></i>
  <div id="{p}-li1" class="{p}-li {p}-big"><span class="{p}-mk">—</span>Ret / aleyhe karar: <b>gerekçeli</b>;<br>itiraz yolu kararda belirtilir</div>
  <div id="{p}-li2" class="{p}-li {p}-big"><span class="{p}-mk">—</span>Kararlar <b>derhal uygulanır</b></div>
  <div id="{p}-li3" class="{p}-li {p}-big"><span class="{p}-mk">—</span>İtiraz: <b>30 gün</b> içinde karara bağlanır</div>
</div>
{cal_html}
<div id="{p}-cite" class="{p}-cite">GK md. 6/3 · 6/4 · GY md. 586/1</div>
"""
t0 = cue(n, "otuz")
t1 = cue(n, "bağlanır.")
step = (t1 - t0) / 30
fill_js = "\n".join(
    f'  tl.fromTo(q("fill-{d}"), {{ opacity: 0 }}, {{ opacity: 1, duration: 0.15, ease: "none" }}, {t0 + (d - 1) * step:.3f});'
    for d in range(1, 31))
js = "\n".join([
    j_fade("eyebrow", 0.0, 0.4),
    j_fade("cite", 0.3),
    f'  tl.fromTo(q("bar"), {{ scaleY: 0 }}, {{ scaleY: 1, duration: 0.5, ease: E }}, 0.05);',
    j_in("li1", cue(n, "Ret"), d=0.45),
    j_stamp("st1", cue(n, "gerekçeli"), -4, scale=1.5, rot_from=-14, d=0.4),
    j_in("li2", cue(n, "Kararlar"), d=0.45),
    j_stamp("st2", cue(n, "derhal"), -3, scale=1.5, rot_from=-12, d=0.4),
    j_in("li3", cue(n, "İtiraz"), d=0.45),
    f'  tl.fromTo(q("ringc-0"), {{ strokeDashoffset: {circ:.1f} }}, {{ strokeDashoffset: {circ:.1f}, duration: 0.01 }}, 0);',
    f'  tl.fromTo(q("ringn-0"), {{ opacity: 0 }}, {{ opacity: 0, duration: 0.01 }}, 0);',
    f'  tl.fromTo(q("ringc-30"), {{ strokeDashoffset: {circ:.1f} }}, {{ strokeDashoffset: {circ:.1f}, duration: 0.01 }}, 0);',
    f'  tl.fromTo(q("ringn-30"), {{ opacity: 0 }}, {{ opacity: 0, duration: 0.01 }}, 0);',
    j_ring(p, 0, cue(n, "İtiraz") + 0.2, circ, dur=0.5),
    fill_js,
    j_ring(p, 30, t1 - 0.1, circ, dur=0.5),
    j_in("tag-30 > span", t1 + 0.2, y=-10, d=0.35),
])
frames.append(write_frame(n, "itiraz", body, stamp_css, js))

# ------------------------------------------------------------------ 07
n, p = 7, "f07"
cal = cal_C(p)
cal_html, circ = cal.html(rings=(5,), tags={5: "İPTAL KARARININ VERİLDİĞİ GÜN"}, up=(5,), later=(5,))
br_css = f""".{p}-brk {{ position:absolute; width:40px; border:6px solid {RED}; border-left:none; transform-origin:top; }}
.{p}-brl {{ position:absolute; font-family:'Space Grotesk'; font-weight:600; font-size:19px; letter-spacing:3px; color:{RED};
  line-height:1.35; width:150px; }}"""
body = f"""
<div id="{p}-eyebrow" class="{p}-eyebrow" style="left:69px;top:86px">GK MD. 7/1</div>
<div id="{p}-sh" class="{p}-sh" style="left:69px;top:140px;width:1080px"><span id="{p}-sh1" class="{p}-w">Üçü bir aradaysa</span>
  <span id="{p}-sh2" class="{p}-w">{svg_arrow(70, 40, 7, DARK)} iptal edilir</span></div>
<div id="{p}-card" class="{p}-card" style="left:69px;top:330px;width:860px">
  <i id="{p}-bar" class="{p}-bar"></i>
  <div id="{p}-li1" class="{p}-li {p}-big"><span class="{p}-mk">a)</span>Yanlış veya eksik bilgiye dayanılmış</div>
  <div id="{p}-li2" class="{p}-li {p}-big"><span class="{p}-mk">b)</span>Başvuran bunu biliyor / bilmesi gerekir</div>
  <div id="{p}-li3" class="{p}-li {p}-big" style="margin-bottom:0"><span class="{p}-mk">c)</span>Doğru bilgiyle karar verilemez</div>
</div>
<div id="{p}-brk" class="{p}-brk" style="left:960px;top:336px;height:236px"></div>
<div id="{p}-brl" class="{p}-brl" style="left:1022px;top:415px">ÜÇÜ BİR<br>ARADA</div>
{cal_html}
<div id="{p}-hero" class="{p}-hero {p}-red {p}-heros" style="left:1190px;top:720px">verildiği gün</div>
<div id="{p}-cite" class="{p}-cite">GK md. 7/1 · 7/4</div>
"""
js = "\n".join([
    j_in("cal", cue(n, "lehe"), y=16, d=0.6),
    f'  tl.fromTo(q("ringc-5"), {{ strokeDashoffset: {circ:.1f} }}, {{ strokeDashoffset: {circ:.1f}, duration: 0.01 }}, 0);',
    f'  tl.fromTo(q("ringn-5"), {{ opacity: 0 }}, {{ opacity: 0, duration: 0.01 }}, 0);',
    j_fade("eyebrow", cue(n, "Gümrük"), 0.4),
    j_fade("cite", cue(n, "fıkra:")),
    f'  tl.fromTo(q("bar"), {{ scaleY: 0 }}, {{ scaleY: 1, duration: 0.5, ease: E }}, {cue(n, "yanlış") - 0.2});',
    j_in("li1", cue(n, "yanlış"), d=0.45),
    j_in("li2", cue(n, "başvuranın"), d=0.45),
    j_in("li3", cue(n, "doğru"), d=0.45),
    f'  tl.fromTo(q("brk"), {{ scaleY: 0 }}, {{ scaleY: 1, duration: 0.5, ease: E }}, {cue(n, "Üçü")});',
    j_in("brl", cue(n, "ARADAYSA"), x=-16, y=0, d=0.4),
    j_in("sh1", cue(n, "Üçü"), d=0.45),
    j_in("sh2", cue(n, "iptal"), d=0.45),
    j_ring(p, 5, cue(n, "VERİLDİĞİ") - 0.1, circ),
    j_in("tag-5 > span", cue(n, "VERİLDİĞİ") + 0.3, y=-10, d=0.4),
    j_stamp("hero", cue(n, "gün") , -4, scale=1.3, rot_from=-12),
])
frames.append(write_frame(n, "yedi-bir", body, br_css, js))

# ------------------------------------------------------------------ 08
n, p = 8, "f08"
cal = cal_C(p)
cal_html, circ = cal.html(rings=(5, 10), tags={5: "İPTAL KARARININ VERİLDİĞİ GÜN", 10: "TEBLİĞ GÜNÜ"}, up=(5,), later=(10,))
dim_css = ""
c4x, c4y = cal.center(5)
body = f"""
<div id="{p}-eyebrow" class="{p}-eyebrow" style="left:69px;top:86px">GK MD. 7/2</div>
<div id="{p}-sh" class="{p}-sh" style="left:69px;top:140px;width:1080px"><span id="{p}-sh1" class="{p}-w">Değiştirilir</span>
  <span id="{p}-sh2" class="{p}-w">veya iptal edilebilir</span></div>
<div id="{p}-card" class="{p}-card" style="left:69px;top:330px;width:900px">
  <i id="{p}-bar" class="{p}-bar"></i>
  <div id="{p}-li1" class="{p}-li {p}-big"><span class="{p}-mk">—</span>Karara esas koşul gerçekleşmemiş /<br>gerçekleşemez</div>
  <div id="{p}-li2" class="{p}-li {p}-big" style="margin-bottom:0"><span class="{p}-mk">—</span>Öngörülen yükümlülüğe uyulmamış</div>
</div>
{cal_html}
<div id="{p}-tag-5-alt" class="{p}-tag" style="left:{c4x:.1f}px;top:{c4y - cal.row_h / 2 - 34:.1f}px"><span>7/1 · VERİLDİĞİ GÜN</span></div>
<div id="{p}-hero" class="{p}-hero {p}-red {p}-heros" style="left:1190px;top:720px">tebliğ günü</div>
<div id="{p}-cite" class="{p}-cite">GK md. 7/2 · 7/4</div>
"""
t_dim = cue(n, "farklı:")
js = "\n".join([
    # 7/1 ring/tag start red (continuity from frame 7), then turn into a thin ink ring
    j_fade("eyebrow", 0.0, 0.4),
    j_fade("cite", 0.3),
    f'  tl.fromTo(q("ringc-5"), {{ stroke: "{RED}", strokeWidth: 6 }}, {{ stroke: "{DARK}", strokeWidth: 3, duration: 0.5, ease: E }}, {t_dim});',
    f'  tl.fromTo(q("ringn-5"), {{ color: "{RED}" }}, {{ color: "{DARK}", duration: 0.5, ease: E }}, {t_dim});',
    f'  tl.fromTo(q("tag-5 > span"), {{ opacity: 1 }}, {{ opacity: 0, duration: 0.3, ease: E }}, {t_dim});',
    f'  tl.fromTo(q("tag-5-alt > span"), {{ opacity: 0 }}, {{ opacity: 1, duration: 0.4, ease: E }}, {t_dim + 0.25});',
    f'  tl.fromTo(q("ringc-10"), {{ strokeDashoffset: {circ:.1f} }}, {{ strokeDashoffset: {circ:.1f}, duration: 0.01 }}, 0);',
    f'  tl.fromTo(q("ringn-10"), {{ opacity: 0 }}, {{ opacity: 0, duration: 0.01 }}, 0);',
    f'  tl.fromTo(q("tag-10 > span"), {{ opacity: 0 }}, {{ opacity: 0, duration: 0.01 }}, 0);',
    f'  tl.fromTo(q("bar"), {{ scaleY: 0 }}, {{ scaleY: 1, duration: 0.5, ease: E }}, {cue(n, "karara") - 0.2});',
    j_in("li1", cue(n, "karara"), d=0.45),
    j_in("li2", cue(n, "yükümlülüğe"), d=0.45),
    j_in("sh1", cue(n, "değiştirilir"), d=0.45),
    j_in("sh2", cue(n, "veya"), d=0.45),
    j_ring(p, 10, cue(n, "Yürürlük"), circ),
    f'  tl.fromTo(q("tag-10 > span"), {{ opacity: 0, y: 10 }}, {{ opacity: 1, y: 0, duration: 0.4, ease: E }}, {cue(n, "TEBLİĞ")});',
    j_stamp("hero", cue(n, "TEBLİĞ") + 0.05, -4, scale=1.3, rot_from=-12),
])
frames.append(write_frame(n, "yedi-iki", body, dim_css, js))

# ------------------------------------------------------------------ 09
n, p = 9, "f09"
R9 = 190
circ9 = 2 * math.pi * R9
ring9 = lambda side, x: (
    f'<div id="{p}-big{side}" class="{p}-abs" style="left:{x}px;top:200px;width:{2 * R9 + 40}px;height:{2 * R9 + 40}px">'
    f'<svg width="{2 * R9 + 40}" height="{2 * R9 + 40}" style="position:absolute;left:0;top:0">'
    f'<circle id="{p}-bigc{side}" cx="{R9 + 20}" cy="{R9 + 20}" r="{R9}" fill="none" stroke="#fff" stroke-width="19" '
    f'transform="rotate(-90 {R9 + 20} {R9 + 20})" style="stroke-dasharray:{circ9:.1f};stroke-dashoffset:0"/></svg>'
    f'<div id="{p}-bigt{side}" class="{p}-bigt">7/{1 if side == "L" else 2}</div></div>')
css9 = f""".{p}-bigt {{ position:absolute; left:0; right:0; top:0; bottom:0; display:flex; align-items:center; justify-content:center;
  font-family:'Shrikhand'; font-size:140px; color:#fff; text-shadow:{SHADOW}; }}
.{p}-quote {{ position:absolute; font-family:'Shrikhand'; font-size:90px; line-height:1.1; color:#fff; text-shadow:{SHADOW};
  white-space:nowrap; text-align:center; width:700px; }}"""
body = f"""
<div id="{p}-eyebrow" class="{p}-eyebrow {p}-white" style="left:69px;top:86px">AKILDA KALSIN · GK MD. 7/4</div>
{ring9("L", 230)}
{ring9("R", 1270)}
<div id="{p}-swapw" class="{p}-abs" style="left:825px;top:300px">{svg_swap(270, 170, "#fff", p + "-swap")}</div>
<div id="{p}-swl" class="{p}-eyebrow {p}-white" style="left:660px;top:520px;width:600px;text-align:center">SINAVDA YER DEĞİŞTİRİR</div>
<div id="{p}-q1" class="{p}-quote" style="left:70px;top:680px">verildiği gün</div>
<div id="{p}-q2" class="{p}-quote" style="left:1110px;top:680px">tebliğ günü</div>
"""
js = "\n".join([
    j_fade("eyebrow", 0.0, 0.4),
    f'  tl.fromTo(q("bigcL"), {{ strokeDashoffset: {circ9:.1f} }}, {{ strokeDashoffset: 0, duration: 0.7, ease: "power2.inOut" }}, {cue(n, "iki")});',
    f'  tl.fromTo(q("bigcR"), {{ strokeDashoffset: {circ9:.1f} }}, {{ strokeDashoffset: 0, duration: 0.7, ease: "power2.inOut" }}, {cue(n, "halka:")});',
    j_stamp("bigtL", cue(n, "birinci"), -6, scale=1.3, rot_from=-14, d=0.45),
    j_stamp("q1", cue(n, "verildiği"), -4, scale=1.2, rot_from=-10, d=0.45),
    j_stamp("bigtR", cue(n, "ikinci"), -6, scale=1.3, rot_from=-14, d=0.45),
    j_stamp("q2", cue(n, "tebliğ"), -4, scale=1.2, rot_from=-10, d=0.45),
    f'  tl.fromTo(q("swapw"), {{ opacity: 0, scale: 0.7 }}, {{ opacity: 1, scale: 1, duration: 0.5, ease: E }}, {cue(n, "Sınavda")});',
    j_in("swl", cue(n, "yerlerini"), y=12, d=0.4),
])
frames.append(write_frame(n, "iki-halka", body, css9, js, ground=RED, prog_color=DARK))

# ------------------------------------------------------------------ 10
n, p = 10, "f10"
body = f"""
<img id="{p}-logo" class="{p}-abs" src="public/logo-ufuk-cetintas.png" alt="Ufuk Çetintaş — Gümrük Eğitim Koçu"
  style="left:576px;top:150px;width:768px;height:auto">
<div id="{p}-handle" class="{p}-eyebrow {p}-dark" style="left:0;top:650px;width:{W}px;text-align:center;font-size:31px;letter-spacing:5px">@GUMRUKKOCUNUZ</div>
"""
js = "\n".join([
    j_in("logo", 0.1, y=36, d=0.9),
    j_in("handle", cue(n, "Ufuk"), y=14, d=0.5),
])
frames.append(write_frame(n, "kapanis", body, "", js))

print("\n".join(frames))
