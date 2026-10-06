#!/usr/bin/env python3
"""Logo filigranı — index.html'e ortada, %10 opaklıkta, bütün süre boyunca.

Sıra: build_frames.py → assemble-index.mjs → transitions.mjs inject → bu betik.
Tekrar çalıştırmak güvenlidir (önceki filigran bloklarını silip yeniden ekler).
Kapanış sahnesinde (logo zaten ortada) filigran geçişle birlikte söner.
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX = os.path.join(ROOT, "index.html")
LOGO = "public/logo-ufuk-cetintas.png"
OPACITY = 0.10
WIDTH = 720  # px; logo oranı 1823×999
FADE = 0.6
W, H = 1920, 1080
COMP = "compositions/filigran.html"

CSS_START, CSS_END = "/* filigran:start */", "/* filigran:end */"
EL_START, EL_END = "<!-- filigran:start -->", "<!-- filigran:end -->"
JS_START, JS_END = "// filigran:start", "// filigran:end"


def strip(s, a, b):
    return re.sub(r"[ \t]*" + re.escape(a) + r".*?" + re.escape(b) + r"\n?", "", s, flags=re.S)


def main():
    html = open(INDEX).read()
    for a, b in ((CSS_START, CSS_END), (EL_START, EL_END), (JS_START, JS_END)):
        html = strip(html, a, b)

    total = float(re.search(r'data-composition-id="main"[^>]*?data-duration="([0-9.]+)"', html, re.S).group(1))
    closing = float(re.findall(r'class="scene"[^>]*?data-start="([0-9.]+)"', html, re.S)[-1])

    h = round(WIDTH * 999 / 1823)
    comp = f"""<template>
<style>
#root {{ position:absolute; inset:0; width:{W}px; height:{H}px; overflow:hidden; pointer-events:none; }}
#filigran-logo {{ position:absolute; left:{(W - WIDTH) // 2}px; top:{(H - h) // 2}px; width:{WIDTH}px; height:{h}px; opacity:{OPACITY}; }}
</style>
<div id="root" data-composition-id="filigran" data-start="0" data-duration="{total:g}" data-width="{W}" data-height="{H}">
<img id="filigran-logo" src="{LOGO}" alt="">
</div>
<script>
(function () {{
  window.__timelines = window.__timelines || {{}};
  window.__timelines["filigran"] = gsap.timeline({{ paused: true }});
}})();
</script>
</template>
"""
    open(os.path.join(ROOT, COMP), "w").write(comp)

    css = (f"      {CSS_START}\n"
           f"      #el-filigran {{ z-index: 100; pointer-events: none; }}\n"
           f"      {CSS_END}\n")
    html = html.replace("    </style>\n  </head>", css + "    </style>\n  </head>", 1)

    el = (f"      {EL_START}\n"
          f'      <div id="el-filigran" class="scene" data-composition-id="filigran" data-composition-src="{COMP}"\n'
          f'        data-start="0" data-duration="{total:g}" data-track-index="20"></div>\n'
          f"      {EL_END}\n")
    html = re.sub(r"(\n    </div>\n\n    <script>)", "\n" + el.rstrip("\n") + r"\1", html, count=1)

    js = (f"        {JS_START}\n"
          f'        tl.to("#el-filigran", {{ opacity: 0, duration: {FADE}, ease: "power2.inOut" }}, {closing:g});\n'
          f"        {JS_END}\n")
    anchor = "        tl.to({}, { duration:"
    assert anchor in html, "full-span anchor not found"
    html = html.replace(anchor, js + anchor, 1)

    open(INDEX, "w").write(html)
    print(f"filigran: {LOGO} · %{OPACITY * 100:.0f} · {WIDTH}px · 0–{total:g}s (kapanışta {closing:g}s'de söner)")


if __name__ == "__main__":
    main()
