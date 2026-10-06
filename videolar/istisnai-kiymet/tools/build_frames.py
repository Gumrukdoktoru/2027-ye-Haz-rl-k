#!/usr/bin/env python3
"""İstisnai kıymet — compositions/frames/NN-*.html (onaylı taslak + kelime zamanları).

Yerleşim tools/scenes.py'den gelir (taslakla birebir); burada yalnızca hareket eklenir.
Kullanım: python3 tools/build_frames.py   (proje kökünden)
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from scenes import ROOT, W, H, BG, RED, DARK, N_FRAMES, css_common, frame_specs  # noqa: E402

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
    return (f'  tl.fromTo(q("{s}"), {{ opacity: 0, scale: {scale}, rotation: {rot_from} }}, '
            f'{{ opacity: 1, scale: 1, rotation: {rot}, duration: {d}, ease: E }}, {t});')


def j_scale(s, t, prop="scaleX", d=0.6, ease="power2.inOut"):
    return f'  tl.fromTo(q("{s}"), {{ {prop}: 0 }}, {{ {prop}: 1, duration: {d}, ease: "{ease}" }}, {t});'


def j_pop(s, t, d=0.4):
    return f'  tl.fromTo(q("{s}"), {{ opacity: 0, scale: 0.4 }}, {{ opacity: 1, scale: 1, duration: {d}, ease: E }}, {t});'


def j_ring(p, t, circ, d=0.6):
    return "\n".join([
        f'  tl.fromTo(q("ring26c"), {{ strokeDashoffset: {circ:.1f} }}, {{ strokeDashoffset: 0, duration: {d}, ease: "power2.inOut" }}, {t});',
        f'  tl.fromTo(q("ring26n"), {{ opacity: 0, scale: 0.6 }}, {{ opacity: 1, scale: 1, duration: 0.45, ease: E }}, {t + 0.15});',
    ])


def write_frame(n, spec, js):
    p = f"f{n:02d}"
    fid = f"{n:02d}-{spec['slug']}"
    dur = DUR[n]
    ground = spec.get("ground", BG)
    prog = spec.get("prog", RED)
    html = spec["html"].replace(TILT, "")  # tilt is applied by the timeline (no CSS/GSAP transform clash)
    pf, pt = (n - 1) / N_FRAMES, n / N_FRAMES
    out = f"""<template>
<style>
{css_common(p, ground)}
.{p}-prog {{ background:{prog}; }}
{spec['css']}
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


def main():
    F = frame_specs()
    built = []

    n = 1; js = [
        j_fade("eyebrow", 0.0, 0.5),
        j_in("paper", 0.15, y=30, d=0.7),
        j_in("h1", cue(n, "kıymeti,"), d=0.5),
        j_fade("cite", cue(n, "kıymeti,")),
        j_in("body", cue(n, "tescil"), d=0.5),
        j_stamp("h2", cue(n, "kesinleşmemiştir."), rot=-4, rot_from=-12, scale=1.25),
        j_fade("qcell", cue(n, "kesinleşmemiştir.") + 0.3, 0.4),
        j_stamp("q", cue(n, "Peki"), rot=-6, rot_from=-18, scale=1.6, d=0.55),
    ]; built.append(write_frame(n, F[n], "\n".join(js)))

    n = 2; js = [
        j_fade("eyebrow", 0.0),
        j_in("h1", cue(n, "istisnai"), d=0.5),
        j_stamp("h2", cue(n, "kıymetle"), rot=-4, rot_from=-12, scale=1.25),
        j_fade("cite", cue(n, "beyan.")),
        j_in("yon", cue(n, "Satış"), y=-12, d=0.45),
        j_in("c1", cue(n, "sahibinin"), d=0.45),
        j_in("ar", cue(n, "gümrük"), x=-30, y=0, d=0.4),
        j_in("c2", cue(n, "idaresi"), d=0.45),
    ]; built.append(write_frame(n, F[n], "\n".join(js)))

    n = 3; js = [
        j_fade("eyebrow", 0.0, 0.4),
        j_in("sh", cue(n, "Beş"), d=0.45),
        j_fade("cite", cue(n, "için:")),
        j_in("card-a", cue(n, "konsinye"), y=40, d=0.55),
        j_in("card-b", cue(n, "Kıymet"), y=40, d=0.55),
        j_in("card-c", cue(n, "Fiyatı"), y=40, d=0.55),
        j_in("card-cc", cue(n, "Boru"), y=40, d=0.55),
        j_in("card-d", cue(n, "Ve"), y=40, d=0.55),
    ]; built.append(write_frame(n, F[n], "\n".join(js)))

    n = 4; js = [
        j_fade("eyebrow", 0.0, 0.4),
        j_fade("cite", 0.3),
        j_in("k1", cue(n, "genel"), d=0.45),
        j_in("k2", cue(n, "ama"), d=0.45),
        j_fade("card-a", cue(n, "Be,"), 0.5, 1, 0.32),
        j_fade("card-d", cue(n, "Be,"), 0.5, 1, 0.32),
        j_stamp("stamp-b", cue(n, "Be,"), rot=-4, rot_from=-14, scale=1.5, d=0.4),
        j_stamp("stamp-c", cue(n, "ce"), rot=-4, rot_from=-14, scale=1.5, d=0.4),
        j_stamp("stamp-cc", cue(n, "çe"), rot=-4, rot_from=-14, scale=1.5, d=0.4),
    ]; built.append(write_frame(n, F[n], "\n".join(js)))

    n = 5; js = [
        j_fade("eyebrow", 0.0, 0.4),
        j_scale("line", cue(n, "zaman"), d=1.1),
        j_pop("mk-tescil", cue(n, "TESCİL")),
        j_in("tescil-l", cue(n, "TESCİL"), d=0.45),
        j_in("sh", cue(n, "TESCİL"), d=0.45),
        j_in("tes-s", cue(n, "vergi,"), d=0.45),
        j_fade("cite", cue(n, "vergi,")),
    ]; built.append(write_frame(n, F[n], "\n".join(js)))

    n = 6; c = F[n]["circ"]; js = [
        j_fade("eyebrow", 0.0, 0.4),
        j_pop("mk-ay1", cue(n, "eksik")),
        j_in("ay1-top", cue(n, "eksik"), y=-10, d=0.4),
        j_in("ay1-s", cue(n, "mahiyet"), d=0.45),
        j_in("ay1-l", cue(n, "tahakkuk"), d=0.45),
        j_fade("cite", cue(n, "Tamamlayıcı")),
        j_in("ay2-top", cue(n, "ayı"), y=-10, d=0.4),
        j_in("strip", cue(n, "ayı"), x=40, y=0, d=0.6),
        j_in("sh", cue(n, "takip"), d=0.45),
        j_fade("sd-26", cue(n, "yirmi"), 0.2, 1, 0),
        j_ring("f06", cue(n, "yirmi"), c),
        j_in("aksam", cue(n, "akşamına"), y=10, d=0.4),
        j_scale("flagpole", cue(n, "verilir;"), prop="scaleY", d=0.5, ease="power3.out"),
        j_in("flag", cue(n, "verilir;") + 0.35, y=-14, d=0.45),
    ]; built.append(write_frame(n, F[n], "\n".join(js)))

    n = 7; js = [
        j_fade("eyebrow", 0.0, 0.4),
        j_fade("cite", 0.3),
        j_in("sh", cue(n, "beyana"), d=0.45),
        j_in("up", cue(n, "YÜKSEKSE,"), y=-20, d=0.5),
        j_in("dn-l", cue(n, "DÜŞÜKSE:"), d=0.45),
        j_in("d1", cue(n, "farkın"), d=0.45),
        j_in("d2", cue(n, "tahlil"), d=0.45),
        j_in("d3", cue(n, "gümrük"), d=0.45),
        j_stamp("d4", cue(n, "Kanunun"), rot=-4, rot_from=-14, scale=1.5, d=0.45),
    ]; built.append(write_frame(n, F[n], "\n".join(js)))

    n = 8; js = [
        j_in("eyebrow", cue(n, "Dikkat:"), y=-8, d=0.4),
        j_fade("cite", 0.4),
        j_fade("mk-tescil", cue(n, "zamanaşımı,"), 0.5, 1, 0.35),
        j_fade("tescil-l", cue(n, "zamanaşımı,"), 0.5, 1, 0.35),
        j_in("sh", cue(n, "zamanaşımı,"), d=0.45),
        j_scale("za", cue(n, "tamamlayıcı", 2), d=0.6),
        j_fade("zah", cue(n, "tamamlayıcı", 2) + 0.5, 0.2),
        j_in("zal", cue(n, "VERİLDİĞİ"), y=10, d=0.4),
        j_in("zas", cue(n, "tarihten"), d=0.45),
    ]; built.append(write_frame(n, F[n], "\n".join(js)))

    n = 9; js = [
        j_fade("eyebrow", 0.0, 0.4),
        j_in("sh", cue(n, "Yirmi"), d=0.45),
        j_fade("cite", 0.5),
        j_in("ay1-l", cue(n, "iki"), d=0.45),
        j_in("k5", cue(n, "tescil"), y=30, d=0.5),
        j_in("k6", cue(n, "tutarı"), y=30, d=0.5),
        j_in("ay1-l2", cue(n, "MUHASEBE"), d=0.45),
        f'  tl.fromTo(q("ring26"), {{ scale: 1 }}, {{ scale: 1.22, duration: 0.25, ease: "power2.out" }}, {cue(n, "yirmi")});',
        f'  tl.fromTo(q("ring26"), {{ scale: 1.22 }}, {{ scale: 1, duration: 0.35, ease: "power2.inOut", immediateRender: false }}, {cue(n, "yirmi") + 0.25});',
        j_in("odeme", cue(n, "vergiler"), d=0.45),
    ]; built.append(write_frame(n, F[n], "\n".join(js)))

    n = 10; js = [
        j_fade("eyebrow", 0.0, 0.4),
        j_fade("cite", 0.5),
        j_fade("mk-tescil", 0.0, 0.01, 0.35, 0.35),
        j_fade("tescil-l", 0.0, 0.01, 0.35, 0.35),
        j_scale("flagpole", 0.05, prop="scaleY", d=0.5, ease="power3.out"),
        j_in("flag", 0.35, y=-14, d=0.45),
        j_in("late", cue(n, "verilmezse?"), y=10, d=0.4),
        j_fade("mk-tescil", cue(n, "TESCİL"), 0.4, 0.35, 1),
        j_fade("tescil-l", cue(n, "TESCİL"), 0.4, 0.35, 1),
        j_scale("back", cue(n, "TESCİL") - 0.3, d=0.8),
        j_fade("backh", cue(n, "TESCİL") + 0.45, 0.2),
        j_in("backl", cue(n, "itibaren"), y=-10, d=0.4),
        j_in("sh", cue(n, "gecikme"), d=0.45),
        j_in("oran", cue(n, "oranında"), d=0.45),
        j_stamp("241", cue(n, "Kanunun"), rot=-4, rot_from=-14, scale=1.5, d=0.45),
    ]; built.append(write_frame(n, F[n], "\n".join(js)))

    n = 11; js = [
        j_fade("eyebrow", 0.0, 0.4),
        j_scale("link", 0.05, d=0.7),
        j_pop("dot1", cue(n, "tescilde")),
        j_stamp("b1", cue(n, "tescilde"), rot=-4, rot_from=-12, scale=1.25),
        j_in("s1", cue(n, "belgedeki"), d=0.45),
        j_pop("dot2", cue(n, "takip")),
        j_stamp("b2", cue(n, "takip"), rot=-4, rot_from=-12, scale=1.25),
        j_in("s2", cue(n, "tamamlayıcı"), d=0.45),
        j_in("r1", cue(n, "Zamanaşımı"), d=0.45),
        j_in("r2", cue(n, "gecikme"), d=0.45),
    ]; built.append(write_frame(n, F[n], "\n".join(js)))

    n = 12; js = [
        j_in("logo", 0.1, y=36, d=0.9),
        j_in("handle", cue(n, "Ufuk"), y=14, d=0.5),
    ]; built.append(write_frame(n, F[n], "\n".join(js)))

    print("\n".join(built))


if __name__ == "__main__":
    main()
