"""產業篇 (long version) — build cards, photo covers, EDL and subtitles.

Run from the project root with the video-use venv:
    ~/.claude/skills/video-use/.venv/bin/python edit/build/industry.py
Then render (see the print at the end).

Same approach and look as pow.py (戰俘營篇): look C cards, .ass subtitles with
ink-balanced boxes, 29.97 fps. Differences: two sources (5635 + 5636), a middle
card, and photo covers taken straight from prof's poster .docx files in
`posters/` — images only; the posters' captions are shuffled between files, so
every caption here is our own and no aerial carries a date it doesn't print.
"""
import json
import math
import re
import subprocess
import zipfile
from collections import OrderedDict
from pathlib import Path

import opencc
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = Path(__file__).resolve().parents[2]
EDIT = ROOT / "edit"
FONTS = EDIT / "fonts"
CARDS = EDIT / "cards_ind"
POSTERS = ROOT / "posters"
SRC = {"5635": ROOT / "raw footage" / "002A5635.MP4",
       "5636": ROOT / "raw footage" / "002A5636.MP4"}
W, H = 1920, 1080
FPS, FPS_F = "30000/1001", 30000 / 1001

PAPER, INK, RUST, GREY = (238, 233, 222), (34, 30, 26), (150, 70, 40), (120, 112, 100)
SERIF = str(FONTS / "NotoSerifTC-Medium.otf")
SANS = str(FONTS / "NotoSansTC-Medium.otf")

CARD_S = {"OPEN": 5.0, "MID": 5.0, "CLOSE": 7.0}

# (source, start, end, beat) — word-boundary cuts, padded into the pauses.
# Cards are ranges too, so the timeline is this one list.
RANGES = [
    ("OPEN", 0, CARD_S["OPEN"], "open card"),
    ("5636", 1166.60, 1181.95, "藍染 was earliest, then 樟腦 (陳總 corrected); starts at 你說 — "
                               "對對對 runs on to 1166.30, cutting into it distorted (Dailies r01)"),
    ("5636", 1236.14, 1247.62, "age 5-6: an old couple moved in next door"),
    ("5636", 1256.16, 1261.30, "they built a thatch hut"),
    ("5636", 1299.25, 1306.95, "shaved the camphor wood … 然後再倒進"),
    ("5636", 1307.62, 1308.95, "那個桶裡面蒸 (「那個塔」 cut out, Dailies r01)"),
    ("5635", 151.00, 154.42, "塗潭里 also had several coal mines; earlier discovery line moved to kiln"),
    ("5635", 252.08, 268.30, "most mine bosses lost money; disasters killed several"),
    ("5635", 281.52, 289.45, "after coal: mandarins"),
    ("5635", 318.63, 331.70, "seedlings carried up on foot, every day"),
    ("5635", 348.98, 357.25, "too little sun, small fruit, only good for juice"),
    ("5635", 1442.65, 1452.75, "邵宗興, from the Japanese era — buying up mandarins"),
    ("5635", 1589.56, 1603.40, "怪手林 cut the 三段 road for 邵宗興 (ends before 27:14)"),
    ("5635", 1739.86, 1751.79, "a man who contributed a lot; the washing plant bears his name "
                               "(ends before the next voice at ~1751.80, Dailies r01)"),
    ("MID", 0, CARD_S["MID"], "mid card"),
    ("5635", 1003.60, 1017.93, "民國58: the first debris flow she ever saw"),
    ("5635", 1027.90, 1041.45, "ran down after class: every house gone, huge boulders"),
    ("5635", 1134.38, 1145.05, "one morning — the washing workers from outside"),
    ("5635", 1160.22, 1205.80, "no water at 6 am; 王財慶: the dam above is blocked, run; 陳總: no one died"),
    ("5635", 1247.40, 1250.95, "陳總: water that should come and doesn't"),
    ("5635", 1264.27, 1269.30, "陳總: it will happen again"),
    ("CLOSE", 0, CARD_S["CLOSE"], "close card"),
]
PUNCT = set("，。？！、-")

# Authoritative spellings, applied AFTER OpenCC. Keys are written against the
# converted (Traditional) text; every key's hits are counted and reported.
SUB_FIXES = OrderedDict([
    ("邵忠興", "邵宗興"),     # 宗興洗煤場 (proposal + 石碑 poster)
    ("王才慶", "王財慶"),     # prof, 2026-09-26
    ("這樣應該是上面水庫的水關起來了", "這樣應該是上面山崩土石堵住溪流"),  # prof, 2026-09-30
    ("這裡路", "這里路"),   # Kyle, Dailies r03: 里 in this place reference
    ("這個山段", "這個三段"),  # inferred from context — confirm by ear in review
    ("趕，快", "趕快"),        # ASR put a comma inside 趕快
    ("衝，沖", "沖，沖"),      # s2twp wrote 冲 two ways in one phrase
    ("臺", "台"),
])

# Photo covers: (name, poster docx, media file, caption, start, end).
# start/end are (source, source time) — resolved to the range that contains it —
# or ("card", card name, seconds in). A cover never begins or ends within 1 s of
# a cut; one that hands into a card runs 1 s into it (lesson L03).
COVERS = [
    ("coal", "煤礦", "image2.png", None, ("5635", 152.10), ("5635", 258.70)),
    ("stele", "宗興洗煤場石碑", "image1.jpeg", "宗興洗煤場石碑", ("5635", 1744.70), ("card", "MID", 1.0)),
    # image1 = the one captioned 「新潭路2段民國52年 淹塞湖事件前航照」 on the poster
    # (Kyle's screenshot, Dailies r01); ends as she says 白天
    ("aerial", "場中碳", "image1.png", "新潭路二段 土石流前的航照", ("5635", 1008.55), ("5635", 1028.92)),
    ("creek", "磺窟溪.03", "image3.png", "磺窟溪", ("5635", 1248.45), ("card", "CLOSE", 1.0)),
]


def font(path, size):
    return ImageFont.truetype(path, size)


def guard(f, text):
    bad = [c for c in text if not c.isspace() and f.getmask(c).size[0] == 0]
    assert not bad, f"missing glyphs {bad}"
    assert "・" not in text, "no ・ in on-screen text (L04)"


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
    cols = [c for c in range(W) if any(px[c, r] != PAPER for r in range(0, H, 4))]
    assert rows[0] > 60 and rows[-1] < H - 60, "card ink outside margins"
    assert cols[-1] < W - 120, "card ink too close to the right edge"
    im.save(out)


def card_mp4(png, seconds, out):
    subprocess.run([
        "ffmpeg", "-v", "error", "-y", "-loop", "1", "-framerate", FPS, "-i", str(png),
        "-f", "lavfi", "-i", "anullsrc=r=48000:cl=stereo",
        "-t", f"{seconds}", "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "14",
        "-c:a", "aac", "-shortest", str(out)], check=True)


def build_cards():
    CARDS.mkdir(parents=True, exist_ok=True)
    from cards import open_card, credits_card
    open_card("新店區塗潭里", "塗潭里的產業變遷", "藍染、樟腦、煤礦、柑橘", CARDS / "open.png")
    open_card("新店區塗潭里", "堰塞湖與土石流", "民國 58 年的土石流記憶", CARDS / "mid.png")   # 土石流篇's opener
    credits_card(CARDS / "close.png", title="塗潭社區社區環境災害",
                 guiding_unit="文化部文資局")    # 土石流篇 credits
    for k in CARD_S:
        card_mp4(CARDS / f"{k.lower()}.png", CARD_S[k], CARDS / f"{k.lower()}.mp4")


# ---------------------------------------------------------------- timeline
def seg_len(src, a, b):
    """What one EDL range really occupies in render.py's concat. Footage is cut
    with -t and re-timed to 29.97, so its video rounds UP to whole frames and
    outlasts the audio; a card's video rounds down but its audio keeps the exact
    length. The concat advances by the longer stream. (Measured on r01 clips:
    exact for all 21 segments. Nominal lengths drifted 0.32 s by the end.)"""
    d = b - a
    if src in CARD_S:
        return d
    return math.ceil(d * FPS_F - 1e-6) / FPS_F


def offsets():
    out, t = [], 0.0
    for src, a, b, _ in RANGES:
        out.append(t); t += seg_len(src, a, b)
    return out, t


def out_time(ref, offs):
    if ref[0] == "card":
        ri = next(i for i, r in enumerate(RANGES) if r[0] == ref[1])
        return offs[ri] + ref[2]
    src, t = ref
    hits = [i for i, (s_, a, b, _) in enumerate(RANGES) if s_ == src and a <= t <= b]
    assert len(hits) == 1, f"cover edge {ref} is in {len(hits)} ranges"
    ri = hits[0]; a, b = RANGES[ri][1], RANGES[ri][2]
    assert a + 1.0 <= t <= b - 1.0, f"cover edge {ref} within 1 s of a cut"
    return offs[ri] + (t - a)


# ---------------------------------------------------------------- covers
def ease_in_out(t):
    return 4 * t ** 3 if t < 0.5 else 1 - (-2 * t + 2) ** 3 / 2


def poster_image(docx, member):
    with zipfile.ZipFile(POSTERS / f"{docx}.docx") as z:
        from io import BytesIO
        return Image.open(BytesIO(z.read(f"word/media/{member}"))).convert("RGB")


def caption_layer(text):
    f = font(SANS, 32)
    guard(f, text)
    ink = f.getbbox(text, anchor="ls")
    pad_x, pad_y = 20, 12
    bw, bh = ink[2] - ink[0] + 2 * pad_x, ink[3] - ink[1] + 2 * pad_y
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay)
    x0, y0 = 80, 64
    d.rectangle([x0, y0, x0 + bw, y0 + bh], fill=(0, 0, 0, 153))
    d.text((x0 + pad_x - ink[0], y0 + pad_y - ink[1]), text, font=f, fill=(255, 255, 255, 255), anchor="ls")
    return lay


def build_cover(name, docx, member, caption, seconds, out_dir=CARDS):
    """Photo framed on a blurred, darkened copy of itself; slow push-in."""
    src = poster_image(docx, member)
    # background: fill the frame, blur, darken
    s = max(W / src.width, H / src.height)
    bg = src.resize((round(src.width * s), round(src.height * s)), Image.LANCZOS)
    bg = bg.crop(((bg.width - W) // 2, (bg.height - H) // 2, (bg.width - W) // 2 + W, (bg.height - H) // 2 + H))
    bg = bg.filter(ImageFilter.GaussianBlur(40)).point(lambda v: int(v * 0.5))
    # foreground: fit a 1500×780 box whose bottom (after the 5 % push) stays
    # above the subtitle box (top ≈ y 933); never more than 1.6× native
    fit = min(1500 / src.width, 780 / src.height, 1.6)
    PUSH, CY = 0.05, 470
    # Pre-scale ONCE (Lanczos) to the largest size the push reaches, then move
    # it per frame with a sub-pixel affine transform. Resizing to a rounded
    # integer size and pasting at an integer position every frame made the push
    # visibly step (Dailies r01, "laggy / clear steps").
    big = src.resize((round(src.width * fit * (1 + PUSH)), round(src.height * fit * (1 + PUSH))),
                     Image.LANCZOS).convert("RGBA")
    assert CY + big.height / 2 < 920, "cover photo runs into the subtitle box"
    cap = caption_layer(caption) if caption else None
    n = round(seconds * FPS_F)
    out = out_dir / f"cover_{name}.mp4"
    p = subprocess.Popen([
        "ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24",
        "-s", f"{W}x{H}", "-r", FPS, "-i", "-", "-frames:v", str(n),
        "-c:v", "libx264", "-pix_fmt", "yuv420p", "-crf", "14", "-r", FPS, str(out)],
        stdin=subprocess.PIPE)
    bg = bg.convert("RGBA")
    for i in range(n):
        k = (1.0 + PUSH * ease_in_out(i / max(n - 1, 1))) / (1 + PUSH)   # ≤ 1: only ever downsample
        # output (x, y) ← big((x - W/2)/k + bw/2, (y - CY)/k + bh/2)
        fg = big.transform((W, H), Image.AFFINE,
                           (1 / k, 0, big.width / 2 - (W / 2) / k, 0, 1 / k, big.height / 2 - CY / k),
                           resample=Image.BICUBIC, fillcolor=(0, 0, 0, 0))
        fr = Image.alpha_composite(bg, fg)
        if cap:
            fr = Image.alpha_composite(fr, cap)
        p.stdin.write(fr.convert("RGB").tobytes())
    p.stdin.close()
    assert p.wait() == 0
    print(f"  cover {name}: {src.width}x{src.height} shown at ≤{fit * 1.05:.2f}×, {seconds:.2f}s")
    return out


# ---------------------------------------------------------------- subtitles
def srt_time(t):
    ms = int(round(t * 1000))
    return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"


def build_srt(offs, stem="ind"):
    words = {k: json.load(open(EDIT / "transcripts" / f"002A{k}.json"))["words"] for k in SRC}
    cc = opencc.OpenCC("s2twp")
    hits = {k: 0 for k in SUB_FIXES}
    cues = []
    for ri, (src, a, b, _) in enumerate(RANGES):
        if src not in SRC:
            continue
        inside = [w for w in words[src] if w["start"] >= a - 0.01 and w["end"] <= b + 0.01]
        events = [w["text"] for w in inside if w["type"] == "audio_event"]
        assert not any("台" in e or "方言" in e for e in events), f"range {ri} has an unfilled dialect gap: {events}"
        seg = [w for w in inside if w["type"] == "word"]
        chunk, chunks = [], []
        for w in seg:
            t = w["text"]
            if chunk and (w["start"] - chunk[-1]["end"] > 0.5):
                chunks.append(chunk); chunk = []
            chunk.append(w)
            n = sum(len(x["text"]) for x in chunk if x["text"] not in PUNCT)
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
            txt = txt.replace("-", "").strip("，。？！、 ").replace("，", " ").replace("。", " ")
            txt = re.sub(r" +", " ", txt)
            if not txt:
                continue
            s = ch[0]["start"] - a + offs[ri]
            e = min(ch[-1]["end"] + 0.15, b) - a + offs[ri]
            cues.append((max(s, offs[ri]), e, txt, ri))
    merged = []
    for c in cues:
        if merged and len(c[2]) <= 3 and len(merged[-1][2]) + len(c[2]) <= 20 \
                and c[0] - merged[-1][1] < 0.5 and c[3] == merged[-1][3]:   # never across a cut
            s0, _, t0, r0 = merged[-1]; merged[-1] = (s0, c[1], t0 + " " + c[2], r0)
        else:
            merged.append(c)
    cues = merged
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
    for i in range(len(cues) - 1):
        s, e, t, r = cues[i]
        cues[i] = (s, min(e, cues[i + 1][0] - 0.04), t, r)
    with open(EDIT / f"master_{stem}.srt", "w") as f:
        for i, (s, e, t, _) in enumerate(cues, 1):
            f.write(f"{i}\n{srt_time(s)} --> {srt_time(e)}\n{t}\n\n")
    for k, n in hits.items():
        print(f"  SUB_FIX {k}→{SUB_FIXES[k]}: {n} hit(s)" + ("  ← never matched" if n == 0 else ""))
    return cues


# Subtitles: same .ass construction as pow.py (lessons L45/L46) — an exact
# vector box per cue plus the text centred on the ink band, burned by libass.
SUB_SIZE, PAD_Y, PAD_X, BOX_BOTTOM = 50, 16, 28, H - 64
INK_NUDGE = 0


def ass_time(t):
    cs = int(round(t * 100))
    return f"{cs // 360000}:{cs // 6000 % 60:02d}:{cs // 100 % 60:02d}.{cs % 100:02d}"


def build_ass(cues, stem="ind"):
    f = font(SANS, SUB_SIZE)
    asc, desc = f.getmetrics()
    ref = f.getbbox("國說嗎關", anchor="ls")
    band_h = ref[3] - ref[1]
    box_h = band_h + 2 * PAD_Y
    y0 = BOX_BOTTOM - box_h; yc = y0 + box_h / 2
    ink_c = (ref[1] + ref[3]) / 2; line_c = (desc - asc) / 2
    ty = yc - (ink_c - line_c) + INK_NUDGE
    ass_size = asc + desc
    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {W}
PlayResY: {H}
WrapStyle: 2
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Box,Noto Sans TC Medium,{ass_size},&H66000000,&H66000000,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,7,0,0,0,1
Style: Text,Noto Sans TC Medium,{ass_size},&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,0,0,0,0,100,100,0,0,1,0,0,5,0,0,0,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    lines = []
    for s0, e0, txt, _ in cues:
        guard(f, txt.replace(" ", ""))
        ink = f.getbbox(txt, anchor="ls"); tw = ink[2] - ink[0]
        bw = tw + 2 * PAD_X; x0 = (W - bw) / 2
        t0, t1 = ass_time(s0), ass_time(e0)
        lines.append(f"Dialogue: 0,{t0},{t1},Box,,0,0,0,,{{\\pos({x0:.0f},{y0:.0f})\\p1}}m 0 0 l {bw:.0f} 0 {bw:.0f} {box_h:.0f} 0 {box_h:.0f}{{\\p0}}")
        lines.append(f"Dialogue: 1,{t0},{t1},Text,,0,0,0,,{{\\pos({W / 2:.0f},{ty:.1f})}}{txt}")
    (EDIT / f"master_{stem}.ass").write_text(head + "\n".join(lines) + "\n")


def build_edl(total, overlays, stem="ind"):
    sources = {k: str(v) for k, v in SRC.items()}
    sources.update({k: str(CARDS / f"{k.lower()}.mp4") for k in CARD_S})
    ranges = []
    for src, a, b, beat in RANGES:
        r = {"source": src, "start": a, "end": b, "beat": beat}
        if src in CARD_S:
            r["grade"] = ""          # synthetic sources opt out of the grade (L34)
        ranges.append(r)
    edl = {
        "version": 1,
        "sources": sources,
        "ranges": ranges,
        "grade": "eq=brightness=0.02:contrast=1.06:saturation=1.05",
        "overlays": overlays,
        "subtitles": f"master_{stem}.ass",
        "total_duration_s": round(total, 2),
    }
    (EDIT / f"edl_{stem}.json").write_text(json.dumps(edl, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    build_cards()
    offs, total = offsets()
    overlays = []
    for name, docx, member, caption, a, b in COVERS:
        t0, t1 = out_time(a, offs), out_time(b, offs)
        build_cover(name, docx, member, caption, t1 - t0)
        overlays.append({"file": f"cards_ind/cover_{name}.mp4", "start_in_output": round(t0, 3),
                         "duration": round(t1 - t0, 3)})
        print(f"    at {t0:.2f}–{t1:.2f}")
    cues = build_srt(offs)
    build_ass(cues)
    build_edl(total, overlays)
    print(f"cards + {len(COVERS)} covers + {len(cues)} subtitle cues + EDL written; expected duration {total:.2f}s")
    print("render: ~/.claude/skills/video-use/.venv/bin/python ~/.claude/skills/video-use/helpers/render.py "
          "edit/edl_ind.json -o edit/ind_preview.mp4 --preview --no-loudnorm --fps 30000/1001 "
          "--fonts-dir edit/fonts --sub-style \"Encoding=1\"")
