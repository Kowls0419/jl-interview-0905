"""Build separate 產業篇 and 土石流篇 from the accepted combined cut.

Run from the project root with the video-use venv:
    ~/.claude/skills/video-use/.venv/bin/python edit/build/split_industry.py

The former middle card becomes the flood opener. The industry film gets its
own closing card. The interview ranges and photo choices come from industry.py.
"""
import industry as base


def build_part(stem, ranges, covers):
    base.RANGES = ranges
    offs, total = base.offsets()
    overlays = []
    for name, docx, member, caption, a, b in covers:
        t0, t1 = base.out_time(a, offs), base.out_time(b, offs)
        base.build_cover(name, docx, member, caption, t1 - t0)
        overlays.append({"file": f"cards_ind/cover_{name}.mp4",
                         "start_in_output": round(t0, 3),
                         "duration": round(t1 - t0, 3)})
        print(f"  {stem} cover {name}: {t0:.2f}–{t1:.2f}")
    cues = base.build_srt(offs, stem)
    base.build_ass(cues, stem)
    base.build_edl(total, overlays, stem)
    print(f"{stem}: {len(ranges)} ranges, {len(cues)} cues, expected {total:.2f}s")
    print(f"render: ~/.claude/skills/video-use/.venv/bin/python "
          f"~/.claude/skills/video-use/helpers/render.py edit/edl_{stem}.json "
          f"-o edit/{stem}_preview.mp4 --preview --no-loudnorm --fps 30000/1001 "
          f"--fonts-dir edit/fonts --sub-style 'Encoding=1'")


if __name__ == "__main__":
    all_ranges = base.RANGES[:]
    all_covers = base.COVERS[:]
    split_at = next(i for i, r in enumerate(all_ranges) if r[0] == "MID")

    base.build_cards()
    base.CARD_S["IND_CLOSE"] = 7.0
    from cards import credits_card
    credits_card(base.CARDS / "ind_close.png", title="塗潭社區社區產業演進",
                 guiding_unit="文化部文資局")      # 產業篇 credits
    base.card_mp4(base.CARDS / "ind_close.png", base.CARD_S["IND_CLOSE"],
                  base.CARDS / "ind_close.mp4")

    industry_covers = []
    for name, docx, member, caption, a, b in all_covers[:2]:
        if name == "stele":
            b = ("card", "IND_CLOSE", 1.0)
        industry_covers.append((name, docx, member, caption, a, b))
    build_part("industry", all_ranges[:split_at] +
               [("IND_CLOSE", 0, base.CARD_S["IND_CLOSE"], "industry closer")],
               industry_covers)
    build_part("flood", all_ranges[split_at:], all_covers[2:])
