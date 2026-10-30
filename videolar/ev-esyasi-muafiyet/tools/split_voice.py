#!/usr/bin/env python3
"""Seçilen okumayı (assets/voice/cem-full.mp3) sahnelere böler → assets/voice/NN.wav + audio_meta.json.

Kesim noktası: bir satırın son kelimesiyle sonraki satırın ilk kelimesi arasındaki boşluğun ortası.
Satır başları iki kelimelik çapalarla bulunur (tek kelime metinde daha önce de geçebilir).
"""

import json
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "assets/voice/cem-full.mp3")
WORDS = [
    w
    for w in json.load(open(os.path.join(ROOT, "assets/voice/cem-full.words.json")))[
        "words"
    ]
    if w.get("type", "word") == "word"
]
ANCHORS = [("Yurt", "dışından"), ("Dört", "kişi"), ("İlk", "üç"), ("Yirmi", "dört"), ("Ama", "son"),
           ("Bu", "muafiyetten"), ("Kimler", "yararlanamaz?"), ("Beyan", "ne"), ("Bir", "ülkeden"),
           ("Hak", "mükerrer"), ("Kısacası,", "üç"), ("Gümrük", "Koçu…")]
CLOSING_HOLD = 4.6  # son sahne: imza + logo bekleme


def find(a, b, after):
    for i in range(after, len(WORDS) - 1):
        if WORDS[i]["text"] == a and WORDS[i + 1]["text"] == b:
            return i
    raise KeyError((a, b))


def main():
    idx, k = [], 0
    for a, b in ANCHORS:
        k = find(a, b, k)
        idx.append(k)
        k += 1
    cuts = [0.0] + [
        round((WORDS[i - 1]["end"] + WORDS[i]["start"]) / 2, 3) for i in idx[1:]
    ]
    end_audio = float(
        subprocess.check_output(
            [
                "ffprobe",
                "-v",
                "error",
                "-show_entries",
                "format=duration",
                "-of",
                "csv=p=0",
                SRC,
            ]
        )
        .decode()
        .strip()
    )
    voices = []
    for n in range(len(ANCHORS)):
        t0 = cuts[n]
        t1 = cuts[n + 1] if n + 1 < len(cuts) else end_audio
        dur = round(t1 - t0, 2) if n + 1 < len(cuts) else CLOSING_HOLD
        out = os.path.join(ROOT, f"assets/voice/{n + 1:02d}.wav")
        subprocess.run(
            [
                "ffmpeg",
                "-v",
                "error",
                "-y",
                "-i",
                SRC,
                "-ss",
                f"{t0:.3f}",
                "-to",
                f"{t1:.3f}",
                "-ar",
                "48000",
                "-ac",
                "2",
                out,
            ],
            check=True,
        )
        lo, hi = idx[n], (idx[n + 1] if n + 1 < len(idx) else len(WORDS))
        words = [
            {
                "id": f"w{n + 1:02d}-{j}",
                "text": w["text"],
                "start": round(w["start"] - t0, 3),
                "end": round(w["end"] - t0, 3),
            }
            for j, w in enumerate(WORDS[lo:hi])
        ]
        voices.append(
            {
                "frame": n + 1,
                "path": f"assets/voice/{n + 1:02d}.wav",
                "duration_s": dur,
                "words": words,
            }
        )
    meta = {"bgm": None, "bgm_pending": False, "voices": voices, "sfx": []}
    json.dump(
        meta,
        open(os.path.join(ROOT, "audio_meta.json"), "w"),
        ensure_ascii=False,
        indent=1,
    )
    for v in voices:
        print(
            v["frame"],
            v["duration_s"],
            v["words"][0]["text"],
            "…",
            v["words"][-1]["text"],
        )
    print("total", round(sum(v["duration_s"] for v in voices), 2))


if __name__ == "__main__":
    main()
