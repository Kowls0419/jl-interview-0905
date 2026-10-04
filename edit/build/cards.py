"""Shared opening card and credits card for all four films, so they cannot drift.

Same paper look as the rest of the cards: left-aligned block, rust rule at x=160,
text at x=220. Every opening card has the SAME three lines at the SAME sizes and
the SAME fixed baselines:  place (rust, 56) / headline (ink, 86) / one line (ink, 64).
The credits card replaces each film's old closing card (same card name, same
length), so photo covers that hand off into the closer still land on it.

Import lazily inside a build script's build_cards() (industry.py imports this
module's neighbours, so a top-level import would be circular).
"""
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[2]
FONTS = ROOT / "edit" / "fonts"
W, H = 1920, 1080
PAPER, INK, RUST, GREY = (238, 233, 222), (34, 30, 26), (150, 70, 40), (120, 112, 100)
SERIF = str(FONTS / "NotoSerifTC-Medium.otf")
SANS = str(FONTS / "NotoSansTC-Medium.otf")
LABEL_X, TEXT_X, BAR_X = 220, 220, 160


def _font(path, size):
    return ImageFont.truetype(path, size)


def _guard(f, text):
    bad = [c for c in text if not c.isspace() and f.getmask(c).size[0] == 0]
    assert not bad, f"missing glyphs {bad}"
    assert "・" not in text, "no ・ in on-screen text (L04)"


def _check_ink(im, rule_top, rule_bottom):
    px = im.load()
    rows = [r for r in range(H) if any(px[c, r] != PAPER for c in range(0, W, 4))]
    cols = [c for c in range(W) if any(px[c, r] != PAPER for r in range(0, H, 4))]
    assert rows[0] > 60 and rows[-1] < H - 60, "card ink outside margins"
    assert cols[-1] < W - 120, "card ink too close to the right edge"


def open_card(kicker, headline, line, out):
    """Place / headline / one line. Fixed baselines: identical on every film."""
    f_k, f_h, f_l = _font(SERIF, 56), _font(SERIF, 86), _font(SERIF, 64)
    im = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(im)
    y_k, y_h, y_l = 452, 574, 672
    for f, t in ((f_k, kicker), (f_h, headline), (f_l, line)):
        _guard(f, t)
        assert d.textlength(t, font=f) < W - 220 - 160, f"opening line too wide: {t}"
    d.text((TEXT_X, y_k), kicker, font=f_k, fill=RUST, anchor="ls")
    d.text((TEXT_X, y_h), headline, font=f_h, fill=INK, anchor="ls")
    d.text((TEXT_X, y_l), line, font=f_l, fill=INK, anchor="ls")
    d.rectangle([BAR_X, y_k - 58, BAR_X + 8, y_l + 24], fill=RUST)
    _check_ink(im, y_k - 58, y_l + 24)
    im.save(out)


CREDITS_TITLE = "搶救塗潭焦炭窯"
CREDITS = [
    ("口述", "陳國超、游月裡、張游寶彩、高燈立"),
    ("攝影", "李承洋"),
    ("後製剪輯", "楊大謙"),
    ("指導單位", "新北市政府文化局"),
    ("執行單位", "新北市陳昌梯醫師山林保育協會"),
]


def credits_card(out, extra_rows=(), *, title=CREDITS_TITLE, guiding_unit=None):
    """Film title + credits; optional per-film guide and appended source rows."""
    rows = [(label, guiding_unit if label == "指導單位" and guiding_unit is not None else value)
            for label, value in CREDITS] + list(extra_rows)
    f_t, f_label, f_value = _font(SERIF, 56), _font(SANS, 36), _font(SERIF, 52)
    step, value_x = 92, 520
    im = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(im)
    tb = d.textbbox((0, 0), title, font=f_t, anchor="ls")
    block_h = (-tb[1]) + 70 + step * (len(rows) - 1) + 52
    y0 = (H - block_h) // 2
    _guard(f_t, title)
    assert d.textlength(title, font=f_t) < W - LABEL_X - 160, f"credit title too wide: {title}"
    y_t = y0 - tb[1]
    d.text((LABEL_X, y_t), title, font=f_t, fill=RUST, anchor="ls")
    y = y_t + 70 + 52
    for label, value in rows:
        _guard(f_label, label); _guard(f_value, value)
        assert d.textlength(value, font=f_value) < W - value_x - 160, f"credit too wide: {value}"
        d.text((LABEL_X, y), label, font=f_label, fill=GREY, anchor="ls")
        d.text((value_x, y), value, font=f_value, fill=INK, anchor="ls")
        y += step
    d.rectangle([BAR_X, y0 - 10, BAR_X + 8, y0 + block_h + 10], fill=RUST)
    _check_ink(im, y0 - 10, y0 + block_h + 10)
    im.save(out)
