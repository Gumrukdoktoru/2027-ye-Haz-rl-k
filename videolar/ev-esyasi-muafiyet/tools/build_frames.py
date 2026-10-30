#!/usr/bin/env python3
"""Kullanılmış ev eşyası muafiyeti — compositions/frames/NN-*.html (onaylı taslak + kelime zamanları).

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



def stagger(prefix, n, t, step, fn=None, **kw):
    fn = fn or j_in
    return [fn(f"{prefix}{i + 1}", round(t + step * i, 3), **kw) for i in range(n)]


def main():
    F = frame_specs()
    built = []

    n = 1; js = [
        j_fade("eyebrow", 0.0, 0.5),
        j_in("b1", 0.1, y=-60, d=0.6), j_in("b2", 0.35, y=-60, d=0.6), j_in("b3", 0.6, y=-80, d=0.7),
        j_in("h1", cue(n, "kesin"), d=0.5),
        j_in("body", cue(n, "Kolilerdeki"), d=0.5),
        j_fade("cite", cue(n, "Kolilerdeki")),
        j_stamp("h2", cue(n, "muaf"), rot=-4, rot_from=-12, scale=1.25),
    ]; built.append(write_frame(n, F[n], "\n".join(js)))

    n = 2; js = [
        j_fade("eyebrow", 0.0, 0.4), j_fade("cite", 0.3),
        j_in("sh", cue(n, "Dört"), d=0.45),
        j_in("lab-a", cue(n, "yurt"), y=50, d=0.55),
        j_in("lab-b", cue(n, "dışındaki"), y=50, d=0.55),
        j_in("lab-c", cue(n, "Türk"), y=50, d=0.55),
        j_in("lab-cc", cue(n, "ve"), y=50, d=0.55),
    ]; built.append(write_frame(n, F[n], "\n".join(js)))

    n = 3; js = [
        j_fade("eyebrow", 0.0, 0.4), j_fade("cite", 0.3),
        j_fade("lab-cc", cue(n, "İlk"), 0.5, 1, 0.35),
        j_in("sh", cue(n, "aile"), d=0.45),
        j_scale("band", cue(n, "aile"), d=0.6),
        j_in("doc", cue(n, "vukuatlı"), d=0.45),
    ]; built.append(write_frame(n, F[n], "\n".join(js)))

    n = 4; tk = cue(n, "takvim")
    js = [j_fade("eyebrow", 0.0, 0.4), j_fade("cite", 0.3), j_in("sh", 0.1, d=0.45),
          j_pop("root", cue(n, "Yirmi")),
          j_in("a1", cue(n, "şart"), x=-30, y=0, d=0.4),
          j_in("n2", cue(n, "bir", 2), d=0.5)]
    js += stagger("m", 12, tk, 0.05, y=20, d=0.35)
    js += [j_scale("six", cue(n, "altı"), prop="scaleY", d=0.4, ease="power3.out"),
           j_in("sixl", cue(n, "aydan"), y=-10, d=0.4),
           j_in("d45", cue(n, "Yılda"), d=0.45)]
    built.append(write_frame(n, F[n], "\n".join(js)))

    n = 5; js = [
        j_fade("eyebrow", 0.0, 0.4), j_fade("cite", 0.3), j_fade("sh", 0.0, 0.4),
        j_in("n3", cue(n, "son"), d=0.5),
        j_in("a3", cue(n, "beşini"), x=-40, y=0, d=0.45),
        j_stamp("free", cue(n, "aranmaz."), rot=-4, rot_from=-14, scale=1.5, d=0.45),
        j_in("ele", cue(n, "Giriş-çıkış"), d=0.45),
    ]; built.append(write_frame(n, F[n], "\n".join(js)))

    n = 6; js = [
        j_fade("eyebrow", 0.0, 0.4), j_fade("cite", 0.3), j_fade("sh", 0.0, 0.4),
        j_fade("loop", cue(n, "tekrar"), 0.5),
        j_in("again", cue(n, "yeniden"), y=-10, d=0.45),
    ]; built.append(write_frame(n, F[n], "\n".join(js)))

    n = 7; js = [
        j_fade("eyebrow", 0.0, 0.4), j_fade("cite", 0.3),
        j_in("sh", cue(n, "Kimler"), d=0.45),
        j_in("e1", cue(n, "Yirmi"), y=40, d=0.5),
        j_stamp("s1", cue(n, "görevlileri."), rot=-4, rot_from=-14, scale=1.5, d=0.45),
        j_in("e2", cue(n, "Ve"), y=40, d=0.5),
        j_stamp("s2", cue(n, "çıkanlar."), rot=-4, rot_from=-14, scale=1.5, d=0.45),
        j_in("e3", cue(n, "Çift"), y=40, d=0.5),
        j_stamp("s3", cue(n, "yararlanır."), rot=-4, rot_from=-14, scale=1.5, d=0.45),
    ]; built.append(write_frame(n, F[n], "\n".join(js)))

    n = 8; js = [
        j_fade("eyebrow", 0.0, 0.4), j_fade("cite", 0.3),
        j_in("sh", cue(n, "Beyan"), d=0.45),
        j_in("t1", cue(n, "İlk"), x=-20, y=0, d=0.4),
        j_scale("l1", cue(n, "İlk"), d=0.7),
        j_pop("d1", cue(n, "gelişlerinden")), j_in("g1", cue(n, "gelişlerinden"), y=-10, d=0.4),
        j_in("p1", cue(n, "önce,"), y=10, d=0.35),
        j_in("p2", cue(n, "beraberlerinde"), y=10, d=0.35),
        j_scale("br1", cue(n, "sonraki"), d=0.6),
        j_in("bl1", cue(n, "altı"), y=10, d=0.4),
        j_in("t2", cue(n, "mirasçılar,"), x=-20, y=0, d=0.4),
        j_scale("l2", cue(n, "mirasçılar,"), d=0.7),
        j_pop("d2", cue(n, "veraset")), j_in("g2", cue(n, "veraset"), y=-10, d=0.4),
        j_scale("br2", cue(n, "itibaren"), d=0.7),
        j_in("bl2", cue(n, "yirmi"), y=10, d=0.4),
        j_in("note", cue(n, "Mücbir"), d=0.45),
    ]; built.append(write_frame(n, F[n], "\n".join(js)))

    n = 9; js = [
        j_fade("eyebrow", 0.0, 0.4), j_fade("cite", 0.3),
        j_in("sh", cue(n, "Bir"), d=0.45),
        j_in("sub", cue(n, "götüremediği"), d=0.45),
        j_in("k1", cue(n, "yararlanır:"), y=30, d=0.45),
        j_in("a1", cue(n, "dört"), x=-40, y=0, d=0.45), j_in("al1", cue(n, "dört"), y=-10, d=0.4),
        j_in("k2", cue(n, "kurumuna,"), y=30, d=0.45),
        j_in("a2", cue(n, "üç"), x=-40, y=0, d=0.45), j_in("al2", cue(n, "üç"), y=-10, d=0.4),
        j_in("k3", cue(n, "gümrüğe"), y=30, d=0.45),
        j_in("ins", cue(n, "inceler"), y=20, d=0.45),
        j_fade("info", cue(n, "inceler", off=0.4), 0.4), j_fade("infol", cue(n, "inceler", off=0.4), 0.4),
        j_fade("ret", cue(n, "onaylı"), 0.5),
        j_in("retl", cue(n, "onaylı", off=0.3), y=10, d=0.4),
    ]; built.append(write_frame(n, F[n], "\n".join(js)))

    n = 10; tp = cue(n, "partiler")
    js = [j_fade("eyebrow", 0.0, 0.4), j_fade("cite", 0.3),
          j_in("sh", cue(n, "Hak"), d=0.45),
          j_in("scr", cue(n, "Kişi"), y=30, d=0.5),
          j_fade("band", cue(n, "süresi"), 0.4), j_in("bandl", cue(n, "süresi"), y=-10, d=0.4)]
    js += stagger("p", 3, tp, 0.25, y=-50, d=0.5)
    js += [j_stamp("not", cue(n, "mükerrer", 2), rot=-4, rot_from=-14, scale=1.5, d=0.45)]
    built.append(write_frame(n, F[n], "\n".join(js)))

    n = 11; js = [
        j_fade("eyebrow", 0.0, 0.4),
        j_in("n1", cue(n, "yirmi"), y=40, d=0.5),
        j_in("n2", cue(n, "yılda"), y=40, d=0.5),
        j_in("n3", cue(n, "gelişten"), y=40, d=0.5),
    ]; built.append(write_frame(n, F[n], "\n".join(js)))

    n = 12; js = [
        j_in("logo", 0.1, y=36, d=0.9),
        j_in("handle", cue(n, "Ufuk"), y=14, d=0.5),
    ]; built.append(write_frame(n, F[n], "\n".join(js)))

    print("\n".join(built))


if __name__ == "__main__":
    main()
