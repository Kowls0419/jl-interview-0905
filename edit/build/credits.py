"""Credits card appended to the end of each finished EDL (all four films).

Run from the project root with the video-use venv, AFTER the film's own build
script has written its EDL:
    ~/.claude/skills/video-use/.venv/bin/python edit/build/credits.py [pow industry flood kiln]
Re-running is safe: an EDL that already ends in CREDITS is left alone. Rebuilding
a film with its own script regenerates the EDL, so run this again afterwards.

The card is the same paper look as the closers. It is added as an ordinary card
range (grade "") so render.py normalises its colour range like every other card
(L47). It carries no subtitles, so nothing earlier on the timeline moves.
"""
import json
import sys

from PIL import Image, ImageDraw

import industry as base

CREDITS_S = 7.0
CARD_DIR = base.EDIT / "cards_credits"
W, H, PAPER, INK, RUST, GREY = base.W, base.H, base.PAPER, base.INK, base.RUST, base.GREY

KICKER = "搶救塗潭焦炭窯"
ROWS = [
    ("口述", "陳國超、游月裡、張游寶彩、高燈立"),
    ("攝影", "李承洋"),
    ("後製剪輯", "楊大謙"),
    ("指導單位", "新北市政府文化局"),
    ("執行單位", "新北市陳昌梯醫師山林保育協會"),
]
LABEL_X, VALUE_X, ROW_STEP = 220, 520, 92


def build_card():
    CARD_DIR.mkdir(parents=True, exist_ok=True)
    f_kick = base.font(base.SERIF, 56)
    f_label = base.font(base.SANS, 36)
    f_value = base.font(base.SERIF, 52)
    im = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(im)
    kb = d.textbbox((0, 0), KICKER, font=f_kick)
    block_h = (kb[3] - kb[1]) + 70 + ROW_STEP * (len(ROWS) - 1) + 52
    y0 = (H - block_h) // 2
    base.guard(f_kick, KICKER)
    d.text((LABEL_X, y0 - kb[1]), KICKER, font=f_kick, fill=RUST)
    y = y0 + (kb[3] - kb[1]) + 70
    for label, value in ROWS:
        base.guard(f_label, label)
        base.guard(f_value, value)
        lb = d.textbbox((0, 0), label, font=f_label)
        vb = d.textbbox((0, 0), value, font=f_value)
        base_y = y + 52                                  # shared baseline per row
        d.text((LABEL_X, base_y), label, font=f_label, fill=GREY, anchor="ls")
        d.text((VALUE_X, base_y), value, font=f_value, fill=INK, anchor="ls")
        y += ROW_STEP
    d.rectangle([160, y0 - 10, 168, y0 + block_h + 10], fill=RUST)
    # assert on the ink, not the cursor
    px = im.load()
    rows = [r for r in range(H) if any(px[c, r] != PAPER for c in range(0, W, 4))]
    cols = [c for c in range(W) if any(px[c, r] != PAPER for r in range(0, H, 4))]
    assert rows[0] > 60 and rows[-1] < H - 60, "credits ink outside margins"
    assert cols[-1] < W - 120, "credits ink too close to the right edge"
    png = CARD_DIR / "credits.png"
    im.save(png)
    base.card_mp4(png, CREDITS_S, CARD_DIR / "credits.mp4")
    return png


def patch_edl(stem):
    path = base.EDIT / f"edl_{stem}.json"
    edl = json.loads(path.read_text())
    if edl["ranges"][-1]["source"] == "CREDITS":
        print(f"  {stem}: already ends in CREDITS, left alone")
        return
    edl["sources"]["CREDITS"] = str(CARD_DIR / "credits.mp4")
    edl["ranges"].append({"source": "CREDITS", "start": 0.0, "end": CREDITS_S,
                          "beat": "CREDITS CARD", "grade": ""})
    edl["total_duration_s"] = round(edl["total_duration_s"] + CREDITS_S, 2)
    path.write_text(json.dumps(edl, ensure_ascii=False, indent=2))
    print(f"  {stem}: +{CREDITS_S:.0f} s credits, total_duration_s {edl['total_duration_s']}")


if __name__ == "__main__":
    print("card:", build_card())
    for stem in (sys.argv[1:] or ["pow", "industry", "flood", "kiln"]):
        patch_edl(stem)
