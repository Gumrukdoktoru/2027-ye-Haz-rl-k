#!/usr/bin/env python3
"""Özet beyan (GK 237) — compositions/frames/NN-*.html (onaylı taslak + kelime zamanları).

Yerleşim tools/scenes.py'den gelir (taslakla birebir); burada yalnızca hareket eklenir.
Kullanım: python3 tools/build_frames.py   (proje kökünden)
"""

import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scenes import (
    ROOT,
    W,
    H,
    RED,
    GROUND,
    N_FRAMES,
    css_common,
    frame_specs,
)  # noqa: E402

META = json.load(open(os.path.join(ROOT, "audio_meta.json")))
DUR = {v["frame"]: v["duration_s"] for v in META["voices"]}
WORDS = {v["frame"]: v["words"] for v in META["voices"]}
TILT = "transform:rotate(-4deg)"


def cue(n, word, nth=1, off=0.0):
    k = 0
    for w in WORDS[n]:
        if w["text"] == word:
            k += 1
            if k == nth:
                return round(w["start"] + off, 3)
    raise KeyError(f"frame {n}: {word!r} #{nth}")


# ---------------------------------------------------------------- tween helpers (JS lines)
def j_in(s, t, y=24, d=0.5, x=0):
    return f'  tl.fromTo(q("{s}"), {{ opacity: 0, y: {y}, x: {x} }}, {{ opacity: 1, y: 0, x: 0, duration: {d}, ease: E }}, {t});'


def j_fade(s, t, d=0.5, a=0, b=1):
    return f'  tl.fromTo(q("{s}"), {{ opacity: {a} }}, {{ opacity: {b}, duration: {d}, ease: E }}, {t});'


def j_stamp(s, t, rot=-4, rot_from=-12, scale=1.3, d=0.5):
    return (
        f'  tl.fromTo(q("{s}"), {{ opacity: 0, scale: {scale}, rotation: {rot_from} }}, '
        f"{{ opacity: 1, scale: 1, rotation: {rot}, duration: {d}, ease: E }}, {t});"
    )


def j_scale(s, t, prop="scaleX", d=0.6, ease="power2.inOut"):
    return f'  tl.fromTo(q("{s}"), {{ {prop}: 0 }}, {{ {prop}: 1, duration: {d}, ease: "{ease}" }}, {t});'


def j_pop(s, t, d=0.45):
    return f'  tl.fromTo(q("{s}"), {{ opacity: 0, scale: 0.6 }}, {{ opacity: 1, scale: 1, duration: {d}, ease: E }}, {t});'


def j_bg(s, t, rgba_to, d=0.4):
    rgba_from = rgba_to.rsplit(",", 1)[0] + ",0)"
    return (
        f'  tl.fromTo(q("{s}"), {{ backgroundColor: "{rgba_from}" }}, '
        f'{{ backgroundColor: "{rgba_to}", duration: {d}, ease: E }}, {t});'
    )


def write_frame(n, spec, js):
    p = f"f{n:02d}"
    fid = f"{n:02d}-{spec['slug']}"
    dur = DUR[n]
    ground = spec.get("ground", GROUND)
    prog = spec.get("prog", RED)
    # tilt/stamp açıları zaman çizelgesinden gelir (CSS/GSAP transform çakışmasın)
    html = spec["html"].replace(TILT, "")
    css = spec["css"].replace(" transform:rotate(-4deg);", "")
    pf, pt = (n - 1) / N_FRAMES, n / N_FRAMES
    out = f"""<template>
<style>
{css_common(p, ground)}
.{p}-prog {{ background:{prog}; }}
{css}
</style>
<div id="root" data-composition-id="{fid}" data-start="0" data-duration="{dur}" data-width="{W}" data-height="{H}">
<div id="{p}-bg" class="clip" data-start="0" data-duration="{dur}" data-track-index="0"></div>
{html}
<div id="{p}-prog" class="{p}-prog"></div>
</div>
<script>
(function () {{
  const tl = gsap.timeline({{ paused: true }});
  const E = "power3.out";
  const q = (s) => "#{p}-" + s;
  tl.fromTo(q("prog"), {{ scaleX: {pf:.4f} }}, {{ scaleX: {pt:.4f}, duration: {dur}, ease: "none" }}, 0);
{js}
  window.__timelines["{fid}"] = tl;
}})();
</script>
</template>
"""
    path = os.path.join(ROOT, "compositions/frames", fid + ".html")
    os.makedirs(os.path.dirname(path), exist_ok=True)
    open(path, "w").write(out)
    return fid


RED_HL, AMB_HL = "rgba(216,0,15,.13)", "rgba(255,178,30,.42)"


def main():
    F = frame_specs()
    built = []

    n = 1
    js = [
        j_fade("eyebrow", 0.0, 0.5),
        j_in("ship", 0.1, y=0, x=-90, d=1.1),
        j_in("h1", cue(n, "Elimizde"), d=0.5),
        j_in("list-oz", cue(n, "özet"), y=40, d=0.6),
        j_in("list-bo", cue(n, "boşaltma"), y=40, d=0.6),
        j_stamp("h2", cue(n, "tutmazsa,"), rot=-4, rot_from=-12, scale=1.25),
        j_in("body", cue(n, "Gümrük"), d=0.5),
        j_fade("cite", cue(n, "Gümrük")),
    ]
    built.append(write_frame(n, F[n], "\n".join(js)))

    n = 2
    js = [
        j_fade("eyebrow", 0.0, 0.4),
        j_in("sh", 0.1, d=0.45),
        j_fade("cite", 0.3),
        j_in("t1", cue(n, "Özet"), y=-10, d=0.4),
        j_in("d1", cue(n, "Özet", off=0.15), d=0.45),
        j_bg("row-oz-3", cue(n, "kayıtlı"), RED_HL),
        j_bg("row-bo-3", cue(n, "listesinde"), RED_HL),
        j_stamp("st1", cue(n, "EKSİK."), rot=-4, rot_from=-14, scale=1.5, d=0.4),
        j_in("t2", cue(n, "Boşaltma"), y=-10, d=0.4),
        j_in("d2", cue(n, "Boşaltma", off=0.15), d=0.45),
        j_bg("row-bo-6", cue(n, "listesinde", 2), AMB_HL),
        j_bg("row-oz-6", cue(n, "olmayan", 2), AMB_HL),
        j_stamp("st2", cue(n, "FAZLA."), rot=-4, rot_from=-14, scale=1.5, d=0.4),
    ]
    built.append(write_frame(n, F[n], "\n".join(js)))

    n = 3
    js = [
        j_fade("eyebrow", 0.0, 0.4),
        j_fade("cite", 0.3),
        j_pop("slot", cue(n, "Noksan")),
        j_in("slotl", cue(n, "kapta,"), y=-10, d=0.4),
        j_in("sh", cue(n, "kapta,"), d=0.45),
        j_in("r1", cue(n, "mahrecinden"), y=30, d=0.5),
        j_in("r2", cue(n, "yanlışlıkla"), y=30, d=0.5),
        j_in("r3", cue(n, "kaza"), y=30, d=0.5),
        j_in("r4", cue(n, "çalındığı,"), y=30, d=0.5),
        j_in("sure", cue(n, "gümrük"), d=0.5),
        j_fade("tir", cue(n, "belirleyeceği"), 0.6),
    ]
    built.append(write_frame(n, F[n], "\n".join(js)))

    n = 4
    js = [
        j_fade("eyebrow", 0.0, 0.4),
        j_fade("cite", 0.3),
        j_in("sh", cue(n, "Kanıtlanamazsa,"), d=0.45),
        j_in("s1", cue(n, "tarife"), y=30, d=0.55),
        j_in("s2", cue(n, "Pozisyon"), y=30, d=0.55),
        j_in("s3", cue(n, "Bu"), y=30, d=0.55),
    ]
    built.append(write_frame(n, F[n], "\n".join(js)))

    n = 5
    js = [
        j_fade("eyebrow", 0.0, 0.4),
        j_fade("cite", 0.3),
        j_in("sh", cue(n, "Fazla"), d=0.45),
        j_in("slot", cue(n, "Fazla"), y=0, x=60, d=0.6),
        j_in("slotl", cue(n, "kapta"), y=-10, d=0.4),
        j_in("q", cue(n, "yanlışlıkla"), d=0.5),
        j_in("c1", cue(n, "el"), x=40, y=0, d=0.45),
        j_in("c2", cue(n, "mülkiyeti"), x=40, y=0, d=0.45),
        j_in("c3", cue(n, "tasfiye"), x=40, y=0, d=0.45),
        j_stamp("c4", cue(n, "sif"), rot=0, rot_from=-3, scale=1.08, d=0.45),
    ]
    built.append(write_frame(n, F[n], "\n".join(js)))

    n = 6
    js = [
        j_fade("eyebrow", 0.0, 0.4),
        j_fade("cite", 0.3),
        j_in("sh", cue(n, "Dökme"), d=0.45),
        j_in("pile", cue(n, "Dökme", off=0.1), y=40, d=0.6),
        j_in("g1l", cue(n, "yüzde"), y=-10, d=0.4),
        j_in("g1", cue(n, "üçü"), d=0.5),
        j_scale("g1ok", cue(n, "takibat"), d=0.6),
        j_fade("note", cue(n, "yapılmaz."), 0.5),
        j_in("g2l", cue(n, "Doğalgaz"), y=-10, d=0.4),
        j_in("g2", cue(n, "ürünlerinde,"), d=0.5),
        j_scale("g2ok", cue(n, "altıyı"), d=0.6),
    ]
    built.append(write_frame(n, F[n], "\n".join(js)))

    n = 7
    t0 = cue(n, "Kap")
    tt = cue(n, "tamam,")
    js = [j_fade("eyebrow", 0.0, 0.4), j_fade("cite", 0.3), j_in("sh", t0, d=0.45)]
    js += [j_in(f"k{i + 1}", round(t0 + 0.08 * i, 3), y=30, d=0.45) for i in range(5)]
    js += [j_pop(f"ok{i + 1}", round(tt + 0.07 * i, 3), d=0.35) for i in range(5)]
    js += [
        j_in("cnt", tt + 0.2, d=0.45),
        j_in("diff", cue(n, "sayı,"), d=0.45),
        j_stamp("st", cue(n, "takibat"), rot=-4, rot_from=-14, scale=1.5, d=0.45),
    ]
    built.append(write_frame(n, F[n], "\n".join(js)))

    n = 8
    js = [
        j_fade("eyebrow", 0.0, 0.4),
        j_fade("cite", 0.3),
        j_in("sh", cue(n, "Miktarı"), d=0.45),
        j_in("doc", cue(n, "Miktarı", off=0.2), y=30, d=0.55),
        j_stamp("nt", cue(n, "tespit"), rot=0, rot_from=-6, scale=1.2, d=0.4),
        j_in("ar", cue(n, "fark"), x=-30, y=0, d=0.45),
        j_in("box", cue(n, "özet"), d=0.5),
        j_in("m234", cue(n, "iki"), d=0.45),
        j_scale("strike", cue(n, "değil,"), d=0.4),
        j_stamp("m237", cue(n, "yalnızca"), rot=-4, rot_from=-12, scale=1.3, d=0.45),
        j_in("only", cue(n, "uygulanır."), y=10, d=0.4),
    ]
    built.append(write_frame(n, F[n], "\n".join(js)))

    n = 9
    js = [
        j_fade("eyebrow", 0.0, 0.4),
        j_fade("cite", 0.3),
        j_in("sh", cue(n, "Taşıtta,"), d=0.45),
        j_pop("slot", cue(n, "Taşıtta,", off=0.1)),
        j_in("slotl", cue(n, "özet"), y=-10, d=0.4),
        j_in("tr1", cue(n, "verilmeden"), d=0.45),
        j_in("tr2", cue(n, "getirilmiş"), d=0.45),
        j_in("c1", cue(n, "el"), x=40, y=0, d=0.45),
        j_in("c2", cue(n, "koyma,"), x=40, y=0, d=0.45),
        j_in("c3", cue(n, "tasfiye"), x=40, y=0, d=0.45),
        j_stamp("c4", cue(n, "sif"), rot=0, rot_from=-3, scale=1.08, d=0.45),
    ]
    built.append(write_frame(n, F[n], "\n".join(js)))

    n = 10
    js = [
        j_fade("eyebrow", 0.0, 0.4),
        j_fade("cite", 0.3),
        j_in("sh", cue(n, "Peki"), d=0.45),
        j_in("a", cue(n, "Birinci,"), y=30, d=0.55),
        j_in("b", cue(n, "Altıncı"), y=30, d=0.55),
        j_scale("dash", cue(n, "o"), prop="scaleY", d=0.4, ease="power3.out"),
        j_in("alt", cue(n, "tespit"), y=-10, d=0.45),
    ]
    built.append(write_frame(n, F[n], "\n".join(js)))

    n = 11
    js = [
        j_fade("eyebrow", 0.0, 0.4),
        j_in("r1", cue(n, "noksan"), x=-40, y=0, d=0.5),
        j_in("r2", cue(n, "fazla"), x=-40, y=0, d=0.5),
        j_in("r3", cue(n, "dökme"), x=-40, y=0, d=0.5),
    ]
    built.append(write_frame(n, F[n], "\n".join(js)))

    n = 12
    js = [
        j_in("logo", 0.1, y=36, d=0.9),
        j_in("handle", cue(n, "Ufuk"), y=14, d=0.5),
    ]
    built.append(write_frame(n, F[n], "\n".join(js)))

    print("\n".join(built))


if __name__ == "__main__":
    main()
