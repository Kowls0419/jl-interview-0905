"""戰俘營篇 — build cards, EDL and master SRT for a video-use render.

Run from the project root:  python edit/build/pow.py
Then render (see the print at the end).

Look C (project.md, Session 7): paper cards in Noto Serif TC, Noto Sans TC
subtitles on a dark box, 29.97 fps.
"""
import json
import re
import subprocess
from collections import OrderedDict
from pathlib import Path

import opencc
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
EDIT = ROOT / "edit"
FONTS = EDIT / "fonts"
CARDS = EDIT / "cards_pow"
SRC = ROOT / "raw footage" / "002A5636.MP4"
W, H = 1920, 1080
FPS = "30000/1001"

PAPER, INK, RUST, GREY = (238, 233, 222), (34, 30, 26), (150, 70, 40), (120, 112, 100)
SERIF = str(FONTS / "NotoSerifTC-Medium.otf")
SANS = str(FONTS / "NotoSansTC-Medium.otf")

# (start, end, beat) on 002A5636 — word-boundary cuts, padded into the pauses
RANGES = [
    (1412.27, 1426.60, "a foreigner pulls up at her door"),
    (1438.99, 1447.93, "asks whether elders ever saw foreigners here"),
    (1514.94, 1526.65, "nobody knew where the POWs were held"),
    (1563.90, 1594.45, "王財慶: 你不會來問我 — his father taught them to grow sweet potatoes"),
    (1750.18, 1765.55, "former POWs come back from the UK and cry"),
    (1797.86, 1818.60, "they had come from 金瓜石 nearly starved (stops before 三十七磅)"),
]
OPEN_S, CLOSE_S = 5.0, 6.0
PUNCT = set("，。？！、-")

# Authoritative spellings, applied AFTER OpenCC. Keys are written against the
# converted (Traditional) text; every key's hits are counted and reported.
SUB_FIXES = OrderedDict([
    ("阿託嘎", "阿兜仔"),
    ("阿托嘎", "阿兜仔"),
    ("黃富", "磺窟"),
    ("王才慶", "王財慶"),
    ("臺", "台"),          # s2twp writes 臺; project docs use 台
])


def font(path, size):
    return ImageFont.truetype(path, size)


def guard(f, text):
    bad = [c for c in text if not c.isspace() and f.getmask(c).size[0] == 0]
    assert not bad, f"missing glyphs {bad}"


def draw_block(lines, out):
    """lines: [(text, font, fill, gap_before)] — one left-aligned block, flowing
    from a single cursor, with a rust rule beside it."""
    im = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(im)
    heights = []
    for text, f, _, gap in lines:
        guard(f, text)
        b = d.textbbox((0, 0), text, font=f)
        heights.append((b[3] - b[1], gap))
    total = sum(h + g for h, g in heights)
    y0 = y = (H - total) // 2
    x = 220
    for (text, f, fill, gap), (h, _) in zip(lines, heights):
        y += gap
        b = d.textbbox((0, 0), text, font=f)
        d.text((x, y - b[1]), text, font=f, fill=fill)
        y += h
    d.rectangle([160, y0 - 10, 168, y + 10], fill=RUST)
    # assert on the ink, not the cursor
    px = im.load()
    rows = [r for r in range(H) if any(px[c, r] != PAPER for c in range(0, W, 4))]
    assert rows[0] > 60 and rows[-1] < H - 60, "card ink outside margins"
    im.save(out)


def card_mp4(png, seconds, out):
    subprocess.run([
        "ffmpeg", "-v", "error", "-y", "-loop", "1", "-framerate", FPS, "-i", str(png),
        "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
        "-t", f"{seconds}", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "14",
        "-c:a", "aac", "-shortest", str(out)], check=True)


def build_cards():
    CARDS.mkdir(parents=True, exist_ok=True)
    draw_block([
        ("1945 年 5 月", font(SERIF, 56), RUST, 0),
        ("日軍將金瓜石戰俘", font(SERIF, 78), INK, 60),
        ("移往新店山區磺窟", font(SERIF, 78), INK, 36),
        ("新店礦業文化路徑", font(SANS, 34), GREY, 70),
    ], CARDS / "open.png")
    draw_block([
        ("磺窟戰俘營", font(SERIF, 56), RUST, 0),
        ("1945.5.16 — 8.24", font(SERIF, 78), INK, 60),
        ("兩名戰俘死於營中", font(SERIF, 78), INK, 36),
        ("資料來源：台灣戰俘營紀念協會", font(SANS, 30), GREY, 70),
    ], CARDS / "close.png")
    card_mp4(CARDS / "open.png", OPEN_S, CARDS / "open.mp4")
    card_mp4(CARDS / "close.png", CLOSE_S, CARDS / "close.mp4")


def srt_time(t):
    ms = int(round(t * 1000))
    return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"


def build_srt():
    words = [w for w in json.load(open(EDIT / "transcripts" / "002A5636.json"))["words"]
             if w.get("type") == "word"]
    cc = opencc.OpenCC("s2twp")
    hits = {k: 0 for k in SUB_FIXES}
    cues, offset = [], OPEN_S
    for ri, (a, b, _) in enumerate(RANGES):
        seg = [w for w in words if w["start"] >= a - 0.01 and w["end"] <= b + 0.01]
        chunk, chunks = [], []
        for w in seg:
            t = w["text"]
            if chunk and (w["start"] - chunk[-1]["end"] > 0.5):
                chunks.append(chunk); chunk = []
            chunk.append(w)
            n = sum(len(x["text"]) for x in chunk if x["text"] not in PUNCT)
            # sentence end: break once there's something to read; comma: only
            # once the line is reasonably full; hard cap only at a punctuation-free
            # run so no line splits inside a phrase
            if (t in "。？！" and n >= 3) or (t in "，、" and n >= 8) or n >= 40:
                chunks.append(chunk); chunk = []
        if chunk:
            chunks.append(chunk)
        for ch in chunks:
            raw = "".join(x["text"] for x in ch)
            raw = re.sub(r"(\S)-(?=\1)", "", raw)   # stutter 種-種 → 種
            txt = cc.convert(raw)
            for k, v in SUB_FIXES.items():
                n = txt.count(k)
                if n:
                    hits[k] += n; txt = txt.replace(k, v)
            txt = txt.replace("-", "").strip("，。？！、 ").replace("，", " ")
            if not txt:
                continue
            s = ch[0]["start"] - a + offset
            e = min(ch[-1]["end"] + 0.15, b) - a + offset
            cues.append((s, e, txt, ri))
        offset += b - a
    # merge tiny cues (≤3 chars, e.g. a lone 欸) into the previous one if it fits
    merged = []
    for c in cues:
        if merged and len(c[2]) <= 3 and len(merged[-1][2]) + len(c[2]) <= 20 \
                and c[0] - merged[-1][1] < 0.5 and c[3] == merged[-1][3]:   # never across a cut
            s0, _, t0, r0 = merged[-1]; merged[-1] = (s0, c[1], t0 + " " + c[2], r0)
        else:
            merged.append(c)
    cues = merged
    # split over-long cues at the space nearest the middle, timing by characters
    MAXLEN, out = 18, []
    for c in cues:
        s0, e0, t0, r0 = c
        if len(t0) > MAXLEN and " " in t0:
            mid = len(t0) / 2
            k = min((i for i, ch in enumerate(t0) if ch == " "), key=lambda i: abs(i - mid))
            a_, b_ = t0[:k], t0[k + 1:]
            cut = s0 + (e0 - s0) * len(a_) / (len(a_) + len(b_))
            out += [(s0, cut, a_, r0), (cut + 0.04, e0, b_, r0)]
        else:
            out.append(c)
    cues = out
    long_ = [t for _, _, t, _ in cues if len(t) > 22]
    if long_:
        print("  WARN over-long cues:", long_)
    # no overlaps: end each cue before the next starts
    for i in range(len(cues) - 1):
        s, e, t, r = cues[i]
        cues[i] = (s, min(e, cues[i + 1][0] - 0.04), t, r)
    with open(EDIT / "master_pow.srt", "w") as f:
        for i, (s, e, t, _) in enumerate(cues, 1):
            f.write(f"{i}\n{srt_time(s)} --> {srt_time(e)}\n{t}\n\n")
    for k, n in hits.items():
        print(f"  SUB_FIX {k}→{SUB_FIXES[k]}: {n} hit(s)" + ("  ← never matched" if n == 0 else ""))
    return len(cues), offset + CLOSE_S


def build_edl(total):
    ranges = [{"source": "OPEN", "start": 0.0, "end": OPEN_S, "beat": "OPEN CARD", "grade": ""}]
    ranges += [{"source": "5636", "start": a, "end": b, "beat": beat} for a, b, beat in RANGES]
    ranges += [{"source": "CLOSE", "start": 0.0, "end": CLOSE_S, "beat": "CLOSE CARD", "grade": ""}]
    edl = {
        "version": 1,
        "sources": {"5636": str(SRC), "OPEN": str(CARDS / "open.mp4"), "CLOSE": str(CARDS / "close.mp4")},
        "ranges": ranges,
        "grade": "eq=brightness=0.02:contrast=1.06:saturation=1.05",
        "overlays": [],
        "subtitles": "master_pow.srt",
        "total_duration_s": round(total, 2),
    }
    (EDIT / "edl_pow.json").write_text(json.dumps(edl, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    build_cards()
    n, total = build_srt()
    build_edl(total)
    print(f"cards + {n} subtitle cues + EDL written; expected duration {total:.2f}s")
