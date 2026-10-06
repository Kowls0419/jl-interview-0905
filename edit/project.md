# Project memory — JL Interview 0905

Companion to `JL Interview 0613` (新店礦業文化路徑 heritage series; its three
videos — the **"0613 set"** — were DELIVERED 2026-08-14; that project's log is on
Kyle's Drive only). Same client, same association, new shoot.

**Who's who** (陳總 = 陳國超 = "prof", Hoho, speaker IDs) is in
`docs/production.md` — read it before this file. Kyle is the sole editor. **Video names:** 焦炭窯篇 · 戰俘營篇 ·
產業篇 · 土石流篇. Older entries say "V1–V3" for the *0613 set*; Session 4's
"V1 焦炭窯 · V2 戰俘營 · V3 產業…" is this project's working split under the old
labels. Notes tagged *(Kyle's machine)* refer to paths/hosts only he has.

**Every session is logged for Kyle:** `## Session N — YYYY-MM-DD — Kyle`.
Use the next sequential number and record which agent handled each task.
Kyle is the sole editor and Git author.

**Status (as of 2026-10-05):** All four films are Public on YouTube in the
塗潭社區產業、環境與歷史｜口述影像 playlist. Prof approved 戰俘營篇 and 焦炭窯篇; the revised
credits in 產業篇 and 土石流篇 still await his confirmation. See Sessions 12–13.

## Session 1 — 2026-09-18 — Kyle (`/video-use init` — inventory, no cutting)

**Status:** inventory + transcription only. No EDL, no cuts. Awaiting Kyle's
direction on what this material becomes.

### Sources (`raw footage/`, all 1920×1080 H.264 / AAC 48k stereo, **59.94fps**)

| file | dur | size | on disk | content |
|---|---|---|---|---|
| 002A5634.MP4 | 0:37 | 281 MB | yes | session opening + mic check |
| 002A5635.MP4 | 43:25 | 19.7 GB | yes (see below) | course part 1 — 塗潭里 / 煤礦 / 邵宗興 |
| 002A5636.MP4 | 44:28 | 11.8 GB | yes | course part 2 — 獅仔頭山 / 戰俘營 |

Total ~88.5 min. Note 5635 is 60 Mbps vs 5636's 35 Mbps — different camera mode.

**This is ONE continuous session, in filename order.** 5634 is the opening and
mic check; 5635 runs to a break ("我們先休息一下", 42:47) where the interviewer tees
up 獅仔頭山 and 樟腦窯 — which is exactly where 5636 opens. Treat as one timeline.

**⚠ 5635 was not materialized on arrival** — Google Drive held it as a 302 MB
placeholder for a 19.7 GB file. Pulled at ~88 MB/min, completed in ~3 h via
`scratchpad/materialize.sh` *(Kyle's machine)* (retry loop; log in `scratchpad/materialize.log`).
Tail verified decodable. *(Kyle's machine:)* kyles-imac is on Tailscale but **relayed** (DERP "hkg"),
not LAN-direct, so copying from the iMac was not a faster path.
**Check `stat -f %b` vs `%z` on every Drive source before planning around it.**

### Framing (sampled frames)

Static wide two-shot across a table: interviewer in white shirt (L), interviewee
lavaliered (R). A flower basket sits centre-foreground and blocks the middle of
the frame. Camera re-frames to a tighter single on the interviewee partway
through 5636 (~26:40 sampled). Mixed daylight through textured glass + interior;
flat and slightly dim. BTS stills show a Canon on a monopod/handheld and more
people at the table than the two on camera.

### Transcripts

Scribe `scribe_v1`, verbatim, word-level, diarized, `--language zho` (prob 1.0).
Cached in `transcripts/`. Packed to `takes_packed.md` — **1,332 phrases, 88m 28s,
122 KB**. 5634: 168 words · 5635: 11,486 · 5636: 12,784.

**Speakers** (diarization IDs are per-file, NOT stable across files):
- `speaker_0` — the interviewer / course leader, man in the white shirt. Frames
  every topic and supplies the analytical read (the 三段 self-contained-system
  argument, the 萬華 economic tie). Mentions 「我媽媽」 re: the 租約 chain, so he has
  a personal stake here. 5635 11.1 min · 5636 5.2 min.
- `speaker_1` — **游月裡老師**, the main voice. Born and raised there. 5635 16.2
  min · 5636 30 min.
- `speaker_4` (5635 only, ~3.4 min) — the second 尤老師 introduced at the top.
  Heavy Taiwanese; carries the 朱再叔 / 1928 / 拓寬 thread.
- `speaker_2`, `speaker_3` — incidental (mic chatter).

**⚠ Lots of Taiwanese.** Scribe emits bare `[台語]` markers where it cannot render
Hokkien — dozens of them, and `speaker_4`'s turns are riddled with them. Any
subtitle pass needs a human (or Kyle) to fill those in; they cannot be recovered
from the ASR.

### What this session IS

A **導覽人員訓練課程** (guide-training class), not a sit-down documentary interview.
Opening line: rain forced a change of plan, so the field session became a
classroom one. 游月裡老師 is teaching the volunteer guides the history of the
新潭路三段 stretch, with the course leader steering and a second 尤老師 filling in.
Stated scope at the top of 5634: (1) 社區礦業歷史 + 礦業遺構, (2) 溪流環境 + how to
actually run the tour. A 審查意見 review-comments item is also raised.

### Content map — 002A5635 (part 1)

- **00:00–01:17** Course opening; both 尤老師 introduced.
- **01:18–02:30** 塗潭里 geography: one long ribbon, 一段→三段, 新潭路 ~15 km.
  Settlement began at 一段/二段 (paddy land); 三段 is up by 獅仔頭山, where 泰雅族 were.
- **02:31–04:50** The 三段 coal mines — small, and mostly *unprofitable*. A 陳 owner
  with no mining background who thought it was easy money, an accident with
  injured workers and no 勞保 in the 40s–50s, so he paid their living costs and
  quit. Repeated 礦災 with deaths.
- **04:50–06:30** After coal: **mandarins**. Seedlings carried up on foot, daily,
  to plant below 獅仔頭山; fruit hand-carried down to the 青果合作社 (the 紅瓦屋 below
  the 林場 was built by them) for juice. Eventually abandoned.
- **06:23–08:30** The **焦炭窯** ("gala" in Taiwanese): two loads a day, ~150 台斤
  each, leaving at 2–3 am. Whether coal was stockpiled and then burned; the
  terraces that are actually coal stockpiles, not paddy.
- **09:22–15:30** The leader's thesis: 三段 was a **self-contained system** — its
  own power plant, its own stockpiles, its own small pits, a 木馬道 — unlike 三峽 or
  瑪陵坑 where 焦炭窯 sat next to easy transport. Plus the 新店↔萬華 class/economy tie.
- **16:01–20:45** The **民國58 (1969) 土石流**. Trucks had replaced carrying; 輕便車
  hauled coal. Then the debris flow — she ran down after class to find every
  house gone, huge boulders and mud. The warning sign: a washing worker found the
  water had stopped at ~6 am; 王才慶 (mid-20s, just out of the army) realised the
  reservoir above must be blocked and told everyone to run.
- **20:46–21:50** Leader: this is the valuable part — environmental disaster
  **will** recur, it is cyclical. He has found before/after photos of the 堰塞湖.
- **21:32–29:30** **邵宗興** — the session's biggest character. From 彰化, a
  well-regarded family. Became the local 農林公司 representative (農林公司 → 林務局),
  so he is the *first name on the 租約 chain* — the leader's own mother took over
  from him. Bought up the mandarin harvest by the field. Had the 三段 road cut up
  to the 獅仔頭山 trailhead (by 「怪手林」, the first excavator anyone there had seen).
  The 洗煤廠 carries his name. 鳳英姐's description — tall, striking, "two kinds of
  women on that mountain" — offered by the leader as something he wants verified.
- **29:29–31:20** The last mine on the mountain (owner surnamed 張, by 秀岡橋).
  Two different 王 families — the hydro-power one and the coal-burning one — same
  great-grandfather, different branches.
- **31:41–37:40** speaker_4's thread: **朱再叔**, pre-1928 widening of the river
  route, 龜土坑, 鐵路尾, a wooden chute, 舢舨-type boats out. Very heavy Taiwanese.
- **37:53–42:45** Synthesis: the 紅瓦屋 labour came in from 三峽, so 三段 developed
  *earlier* than the 一段/二段 story suggests — though for general settlement
  一段 came first. Then the 三井株式會社 tea estates taken over by 台灣農林公司, and the
  discharged 老兵 sent there as the lowest-ranked labour — weeding, and pushing tea
  bales to the 殺青 floor.
- **42:47** Break. Leader tees up 獅仔頭山 and the 樟腦窯 → continues in 5636.

### Content map — 002A5636 (part 2, by interviewer's questions)

- **00:00–14:30** 獅仔頭山: the stele, the 隘勇線, getting it listed as a 三級古蹟
  (submitted 民國92 via 文化局, expert on-site inspection), building the ladder and
  the 步道 — sleepers carried up one by one, a petrol generator hauled to 觀獅亭,
  steel cable threaded through and anchored to rock, ~NT$90k. 陳龍喜 (安康 rep)
  credited. Then the critique: ~NT$40m spent, a pretty toilet with no water in
  the dry season, walkway timber rotted in ~3–4 years and had to be hauled out by
  流籠 — "浪費國家的錢", now back to original state.
- **14:37–16:30** What she hopes for 獅仔頭山's future / handing on to younger people.
- **16:31–21:48** Time sequence: 隘勇線 (earliest) → 煤礦 → later era / road-building.
- **21:49–22:40** The camphor (樟腦) remains on the mountain.
- **22:41–43:50** **戰俘營 (POW camp)** — the long block. Prisoners moved from
  金瓜石, US strafing (including during meals), the three work parties, an
  infirmary, cutting bamboo to confine a man who had lost his mind, the surrender,
  the two-week gap before MacArthur landed and documents were destroyed, the
  question of whether POWs would have been executed on invasion, an ox slaughtered
  the day after, then back to work because the army had not surrendered.
  Repeatedly cites **何麥克 / Michael Hurst** (Taiwan POW Camps Memorial Society).
- **43:52–end** Wrap: topics named as 獅仔頭山、戰俘營、焦炭窯、隘勇穴 + a photo pass.

### ⚠ ASR term errors to resolve before any subtitle burn (homophone mis-hearings, and fixes that silently miss)

Scribe returns **Simplified**; prior project converted with OpenCC `s2twp`, and
this project's output must be **Traditional Chinese only**. These need an authoritative spelling from
Kyle or a source doc — do NOT guess into a burn:

**Confident:**
- `土潭里` → **塗潭里** (新店區, real)
- `南荒松` → **南方松** (treated pine)
- `狮仔头山` / `私彩头山` / `四海投山` / `狮头` → **獅仔頭山**
- `爱永现` / `爱勇穴` → **隘勇線** / **隘勇穴**
- `采柴菊子` → **採柑橘**
- `党员事业` → **黨營事業**
- `秀岗桥` → **秀岡橋**; `玛陵坑` / `马宁坑` → **瑪陵坑**

**RESOLVED by the 焦炭窯 proposal** (`搶救塗潭焦炭窯(測繪調查與社區共守)`,
陳國超, 115年文化局社造補助第2梯次 — copy in `docs/`). This is a funded,
submitted document, so it outranks the ASR:

- `朱再叔` → **周再思** — built the 1928 台車吊橋, "全台第三高", demolished 1973,
  replaced by 直潭壩. The single biggest correction; ASR was nowhere close.
- `邵宗興` **confirmed** — the washing plant is 「宗興煤礦洗煤場」, 新潭路3段36號.
  Not 邵忠興.
- `寶彩` → **游寶彩** — 104高年級資深導遊、新店文史館志工. Listed participant.
- `土潭里` → **塗潭里** ✓ · `華城` ✓ (陳禹廷 is a 華城里居民)
- `冲頭燈` → **礦工頭燈水力發電場舊址** — the 王家 hydro site, a listed station.
- `香路坑` / `歸土坑` → almost certainly **磺窟** (磺窟溪, 直潭段磺窟小段).
- **陳國超** = 協會理事長 = "陳總" = `speaker_0`, the course leader.
- Course this footage is from: **「獅山傳奇磺窟煙雲—解說導覽人訓練」**, funded by
  農業部林業及自然保育署, 12 學員.

**The eight stations along 新潭路** (1,553 m, proposal 表1) — these are the
authoritative place names, and they are the spine of the whole trail:
(a) 宗興煤礦洗煤場 → (b) 鹿容園故事牆 → (c) 溪流生態教育展示區 →
(d) 塗潭焦炭窯 → (e) 戰俘營炭窯 → (f) 浙江煤礦風坑 →
(g) 礦工頭燈水力發電場舊址 → (h) 中碳場聚落.
Note `政三煤礦` in the ASR is probably **浙江煤礦**, not 正三.

**Still unresolved — do NOT guess into a burn:**
- `矮梯` / `IT` — the ladder. Sounds like *ai-ti*; maybe **隘梯**, given 隘勇線.
- `黃環碑` / `皇封碑` / `黃番碑` — one stele, three spellings, none in the proposal.
- `兽中心的时代` · `觀思亭` (→ 觀獅亭?) · `怪手林` (nickname; real name?)
- `徐福全`, `陳龍喜`, `穆國康`, `鍾盛吉`, `廖鳳英`, `夏慎理`
- `王才慶` / `王財慶`, plus 王財昆 / 王才進 / 王如卿 across two 王 families.
- `游月裡` / `月婷老師` — she is the *teacher*, so not in the 學員 list.
- `新堂城`, `防哭城`, `北極北之城`, `廟抬頭`, `精誠霸`, `剝甲船`, `三峽中立`
- `何麥克` = **Michael Hurst** (Taiwan POW Camps Memorial Society) — verify the
  Chinese rendering he himself uses before putting it on screen.

A find/replace map that runs *after* OpenCC can silently do nothing, because the
string it sees has already changed. So whatever map we build gets per-key hit
counters, and entries must be written against the string *as it arrives at the
replace* (post-OpenCC). ASR also produces valid-but-wrong homophones (the 0613
set shipped 兩千平 for 兩千坪 until caught), so re-check every domain term on
every subtitle pass.

### Framing / craft notes for whenever cutting starts

- 59.94fps source; the 0613 set was delivered at 24. Decide the target fps
  *before* building any overlay — photo/card overlays that butt against each
  other flashed one frame of footage in the 0613 set (fade overlap and
  frame-rounding drift), and those fixes are stated in frames, so the maths
  changes with fps.
- The flower basket blocks centre frame throughout. In the wide two-shot both
  speakers sit at the far edges with dead space between them — a crop or a cover
  is going to be wanted more often than in the 0613 set.
- ~23 min into 5635 the camera is wide and both subjects are in profile facing
  each other, not camera. Rule from the 0613 set: when the speaker looks away or
  someone intrudes on the frame, cover that stretch with a photo rather than
  cropping globally.
- The TV behind the speakers displays the photo grid they keep referring to
  (「等一下我們有些照片可以再讓大家看一下」). Those photos are the natural card material,
  and the leader says at the end of 5636 he will hand them over.

### Outstanding

1. **Kyle's direction — what does this material become?** Nothing is cut until
   there's a confirmed plan (Hard Rule 11).
2. Authoritative spellings for the terms above; someone who can fill the `[台語]`
   gaps.
3. The photo set the leader promises at the end of 5636 — not in this directory yet.

## Session 2 — 2026-09-20 — Kyle (Git and Drive setup — no cutting)

**Strategy:** set up the GitHub and Google Drive split for the editorial record.
No footage was cut in this session.

**Decisions:** the project root became the Git repository at
https://github.com/Kowls0419/jl-interview-0905. Git tracks the small text files:
project memory, transcripts, takes, EDLs, subtitles, review JSON, and client
questions. Raw footage, photos, generated media, renders, and PDFs remain on
Google Drive and are excluded by `.gitignore`.

**Reasoning log:** use the whole project folder as the root, matching the 0613
layout, while keeping large binaries out of Git. The current production
workflow is in `docs/production.md`; Kyle is the sole editor and maintainer.

**Outstanding:** Session 1's editorial planning and source questions were still
open at this stage.

## Session 3 — 2026-09-20 — Kyle (陳總's brief, relayed by Hoho + 焦炭窯 proposal)

**Still no cutting.** Brief and source doc logged; strategy not yet confirmed.

### The brief (陳總's, relayed by Hoho over LINE, 15:49–15:50)

Four themes in the Saturday recording:
1. 獅仔頭山地區產業變遷（邵宗興）
2. 戰俘營
3. 焦炭窯
4. 社區堰塞湖及土石流

Then: 「隨意弄成約3個90秒的影片」 / 「3個最少90秒影片就可以」 — roughly three
videos, each **at least 90 seconds**. More docs promised.

### ⚠ Three numbers that do not agree — resolve before building

- The brief (via Hoho) says **3 videos**.
- The 焦炭窯 proposal's budget line says **二支各90秒** (`攝錄及影片製作費 1式
  4,000元 — 紀錄片(含剪接)二支各90秒`), i.e. **2 videos**.
- He listed **4 themes**.

The proposal is only for the 焦炭窯 project, so the other themes may sit under a
different budget (the training course is separately funded by 林業及自然保育署).
Do not assume — ask which budget each video is being delivered against, because
the funded deliverable is a contractual number, not a preference.

### What the proposal is (`docs/…(陳總)A.pdf`)

`搶救塗潭焦炭窯(測繪調查與社區共守)` — 陳國超, 新北市文化局 115年社造一般性補助
第2梯次, NT$50,000 total, execution to 2026-10-15 (公告執行截止日).

The story it tells: 解說員班 students on a field walk found 榕樹 roots splitting
the kiln and evidence of **deliberate squatting** (freshly planted 柑橘 and 芭蕉
on state-owned land, 新店直潭段磺窟小段 0110-0086, 國有財產署). They self-started
a rescue. Three-month plan: (1) clear vegetation, (2) AI-assisted survey and
digital reconstruction of the kiln, (3) **影片剪輯與成果展示** — our part.

The kiln's construction is the detail worth putting on screen: a single massive
stone **結構支撐牆** built first on a narrow three-sided-by-river site, with the
arch stacked forward off it — which is why it has survived decades of floods.

**Note the strategic framing, which shapes tone:** the proposal is explicit that
public display is a weapon against the squatters — 「如何用修復方案反擊惡意占用？」,
「建立社會監控壓力」. These videos are not neutral heritage pieces; they are
intended to make the community's claim visible. Worth confirming with 陳總 how
directly that should read on screen.

**© terms:** the signed 授權同意書 grants 文化局 a non-exclusive, royalty-free,
unlimited licence for non-profit promotion, and waives 著作人格權 toward them.
陳國超 retains 著作財產權. Relevant to how Kyle is credited — check before
assuming a 後製剪輯 credit like the 0613 set's carries over.

### Outstanding

1. **3 or 2 videos? Which themes, against which budget?** (see above)
2. Target length — "at least 90s" is a floor; is there a ceiling?
3. Remaining docs 陳總 is sending (via Hoho).
4. The photo set + 堰塞湖 before/after comparison promised on camera.
5. Still needed: the `[台語]` gaps, and the unresolved names above.

## Session 4 — 2026-09-20 — Kyle (decisions + framing analysis)

### Decisions taken (Kyle)

- **3 videos, each ≥90 s** — quoting 陳總's brief (via Hoho) directly.
- **Working assumption on the merge** (mine, NOT yet confirmed by 陳總):
  V1 焦炭窯 · V2 戰俘營 · V3 產業變遷（邵宗興）＋ 堰塞湖/土石流
  (now named 焦炭窯篇 · 戰俘營篇 · 產業篇).
  Four themes into three. **Confirm before building.**
- **Subtitles: Traditional Chinese only.** Settled for this project; no
  bilingual pass. The 台語 gaps still have to be filled by ear.
- **Visual treatment: rethink for the two-shot**, not a reuse of the 0613 set's treatment.
- Deadline: asking 陳總 whether 10/15 is a hard delivery date.

### Framing analysis (contact sheets in `edit/verify/`)

Sampled every 180 s across both long takes. **The camera is not locked** — the
operator reframes repeatedly between a wide two-shot and a tighter single.

- **5635**: two-shot most of the way. 游月裡 sits camera-right, 陳國超 camera-left
  and frequently **clipped by the left edge** (04m, 07m, 25m, 37m). At **34–37m**
  the camera pans right to bring in the third speaker (pink shirt, grey hair) —
  matches `speaker_4`'s 朱再叔/周再思 block at 31:41–37:40.
- **5636**: noticeably more single-on-游月裡, and the best framing in the whole
  shoot sits at **25–37m** — which is the 戰俘營 block. The POW video therefore
  has the strongest available pictures, which is lucky rather than planned.
- The TV behind them shows the photo slideshow early in 5635 (01–07m, purple)
  and is off/black thereafter.

### ⚠ Punch-in does NOT fix the two-shot (tested — `edit/verify/crop_compare.jpg`)

I tested 1.33× (1440 crop) and 1.5× (1280 crop) punch-ins on a clean two-shot.
**Both make it worse.** The obstruction is the flower basket sitting *between*
the two speakers, not clutter at the edges — so cropping inward enlarges the
basket and 游月裡 stays pinned to the right edge regardless. To get a clean single
on her you would have to crop past ~2.5×, which a 1080p source will not survive.

**Consequence for the treatment:** do not plan a reframing/crop pass. The levers
that actually exist are (1) **select** the camera's own tighter framings rather
than synthesising them, and (2) **cover** generously with photo cards, which is
what the 0613 set did anyway. That makes the photo originals a hard dependency, not a
nice-to-have — currently the only copies are 24 PDF-embedded images, mostly
under 1024 px, of which 3 are usable at framed size.

The obvious fix was tested before being proposed, and the test killed it —
check that a remedy changes the thing you blame before recommending it.

### Outstanding

1. 陳總: video count (3 vs the proposal's 2), the merge, 10/15, length ceiling,
   **photo originals**, and how directly to state the occupation issue.
   All added to `docs/questions_for_professor.md` as section 〇.

## Session 5 — 2026-09-20 — Kyle (repo layout: `edit/` is the skill's namespace)

Kyle's rule: **`edit/` holds only what the video-use skill reads and writes.**
Anything else I added there was in the wrong place. Restructured:

```
docs/   client + admin — questions_for_professor.md (tracked),
        the 焦炭窯 proposal PDF (ignored by *.pdf), extracted/ (ignored)
edit/   video-use only: project.md, takes_packed.md, transcripts/,
        animations/, clips_graded/, review/, verify/, downloads/
```

- `questions_for_professor.md` moved with `git mv` so its history follows it.
- Removed a duplicate of the proposal PDF I had created under `edit/docs/` —
  byte-identical (sha1 `337dd113…`) to the one Kyle already had at the root.
  Kept his, consolidated into `docs/`.
- `.gitignore` gained `docs/extracted/`, with a reason.
- README updated: status link, repo-vs-Drive table, folder diagram, and the
  onboarding prompt now say `docs/`, and the prompt tells future sessions not
  to put non-skill files in `edit/`.
- All stale paths in this file rewritten.

## Session 6 — 2026-09-26 — Kyle (repo/infra housekeeping; still no cutting)

No editorial work. Six days since the last session; nothing in the footage,
transcripts or decisions changed.

### ⚠ Git history is now a SINGLE commit — this file IS the history

The repo was squashed to one "Initial Commit" and force-pushed. The
per-session git trail is gone, so `edit/project.md` is the only record of how
the edit got here. **Keep appending to it**, and do not assume `git log` will
tell a future session anything useful.

Also landed on the repo:
- `LICENSE` (MIT, © 2026 Kyle Yang).
- `CLAUDE.md` added to `.gitignore`.
- `private/` — a local-only folder, gitignored, never pushed. Leave it alone.
- `gh` (GitHub CLI) installed and authenticated as `Kowls0419`.

**Near-miss worth remembering:** I edited `project.md`, `README.md` and
`.gitignore` against a stale base while the remote had already moved ahead.
Kyle caught it before the push. Had it gone through, the force-push would have
destroyed `LICENSE` and the `CLAUDE.md` ignore line. Recovery was to rebuild
`.gitignore` from `git show origin/main:.gitignore` rather than the local copy,
reset onto the remote commit, and `git checkout origin/main -- LICENSE`.
**Always `git fetch` and diff against `origin/main` BEFORE editing tracked
files, not after** — this repo gets pushed to from more than one place.

### Cloud vs local

The repo carries text only (9 files); all 31.8 GB of footage is gitignored and
lives in Drive. A cloud session can read the transcripts and plan cuts, but
cannot run `ffprobe`/`ffmpeg`, sample frames, render previews or run Dailies.
**Any real edit pass has to run on a machine with the Drive folder synced.**

### Still open — unchanged since Session 4, and now 6 days old

1. **陳總 has not answered** (as far as this session knows): video count
   (his 3 vs the grant's 二支各90秒), which budget each video sits under, the
   four-themes-into-three merge, whether 10/15 is a hard delivery date, a length
   ceiling above 90 s, and **the photo originals**.
2. The **10/15 execution deadline is 19 days away** and 影片剪輯 is the grant's
   third-month task. If the photos and the answers do not arrive soon, either
   the scope or the date has to give.
3. The `[台語]` gaps (33 passages) and the unresolved names still need a human.

## Session 7 — 2026-09-26 → 09-28 — Kyle (shortlist; prof's answers; fork; shared lessons; 戰俘營篇 test cut)

**Strategy:** Kyle's call — pick the passages each video will use *first*, then
ask prof only about names, facts and 台語 inside those passages. Asking him to
check all ~30 names and 34 台語 gaps across 88 minutes was mostly wasted effort,
since most of that material will never be on screen. Still no EDL — this is a
shortlist of candidate passages, not a cut (Hard Rule 11 still applies).

**Decisions:**
- **3 videos — settled** (Kyle, 2026-09-26; not asked of prof despite the
  grant's 「二支各90秒」). **The 10/15 deadline is not raised with prof** —
  Kyle's call; don't reintroduce it in client docs.
- **Video names** from now on: 焦炭窯篇 · 戰俘營篇 · 產業篇 (see header).
- **產業篇 gets a long version first** (~3 min, both themes), shown to prof
  before deciding whether to cut it to 90 s. Fallback if prof insists on 90 s:
  move the coal/mine passages into 焦炭窯篇 and keep 產業篇 to 土石流 + a short
  邵宗興 thread. 焦炭窯篇 and 戰俘營篇 aim near 90 s.
- **Shortlist** (file mm:ss; candidates, not final in/out points):

  **戰俘營篇** (5636 — best framing in the shoot, tight single 25–37m; ~100 s if all used)
  | time | content |
  |---|---|
  | 23:32–24:27 | 1998 (民國87): a foreigner (何麥克) pulls up at her door asking if elders saw 阿兜仔 |
  | 25:15–25:26 | asks everyone 80–90+; they'd seen POWs, nobody knew where they were held |
  | 26:04–26:37 | **王財慶: 「啊你不會來問我」** — his father was assigned to teach the POWs to grow sweet potatoes. Best moment in the shoot. |
  | 29:58–30:31 | they came from 金瓜石 abused near to death, skin and bone |
  | 29:12–29:29 | four former POWs return from the UK and cry |
  Alternates: 29:43 bamboo cage for a man who went mad · 33:06 strafed at the
  rice-ball meal by 碧潭 · 34:09 arrival at 7 pm, slept on bare ground ·
  42:29 soap, bathing in the river all day after the surrender.

  **焦炭窯篇** (5635 — two-shot throughout; TV slideshow visible 01–07m)
  | time | content |
  |---|---|
  | 06:23–07:26 | her father carried *gala*: two trips a day, ~150 台斤, to 安坑 without resting |
  | 07:31–08:01 | leave at 2–3 am, watch for the kiln smoke, queue |
  | 11:45–12:15 | 陳總: 三段 was a self-contained system (own power, kiln, stockpiles, pits) — unlike 三峽/瑪陵坑 |
  | 30:19–30:51 | not anyone could burn — the mine boss gave the job to 王家 |
  ⚠ **The kiln itself is never discussed on camera** — no support wall, roots,
  clearing, squatting or survey, which is the grant's whole subject. That half
  must come from photos/cards or a site shoot → new question E for prof.

  **產業篇** (long version)
  - Industry order: 5636 19:29–19:45 藍染 → 樟腦 → 煤 · 5636 20:42–21:49 her
    childhood memory of an old couple steaming camphor in a thatch hut ·
    5635 02:26–02:55 + 04:12–04:28 coal found, most mines lost money, deaths ·
    5635 05:20–06:22 mandarins carried up as seedlings, too little sun → juice → abandoned.
  - 邵宗興: 5635 24:08–25:09 buying mandarins by the field; first name on the
    state leases · 26:37–27:38 had 怪手林 cut the road, paid him in land ·
    28:59–29:08 「對山段是很有貢獻的人」.
  - 土石流: 5635 16:43–17:27 民國58, every house gone, boulders and mud ·
    18:54–20:02 at 6 am the washing workers' water stops, 王才慶 says the dam
    above is blocked, run; an hour later everything is swept away ·
    20:46–21:09 陳總: water that should come and doesn't — it *will* recur, it's cyclical.
  - **EXCLUDE 5635 28:00–28:31** (「山上有兩種女人」 about 邵宗興): gossip about a
    real, named person, which 陳總 himself flags as unverified. Do not use.
- **Question doc rewritten** around the shortlist: 台語 gaps 34 → 10 (8 in the
  *gala* passage), names ~30 → 8. Dropped items the proposal already answered
  (邵宗興, 游寶彩, 周再思). Added E (kiln not on camera) and the long-version
  plan under D. Added a "三支影片目前的段落" section so prof can object to a
  passage. Removed an outdated aside from question C.
- **Question doc then cut to 6 one-line questions** (Kyle: the final doc must be
  TL;DR, and several items were ones he can answer himself). Only what prof
  alone can answer stayed. **Moved to Kyle (not in the prof doc):**
  游月裡's full name for the title card (5635 00:13) · 「三十七磅」 (5636 30:25,
  likely wrong — check against Hurst's published account) · 何麥克's own Chinese
  rendering (5636 24:45) · how to write *gala* (5635 06:44) · 「下層里」 place name
  (5635 07:07) · 政三煤礦 → 浙江/正三? (5635 02:38) · the **10 台語 gaps**
  (5635 06:44–08:01 ×8, 5635 12:08, 5636 34:30) · the 審查意見 document.
- **Fixed an unsupported claim** in question B: it said 邵宗興's road and the
  民國58 flood were "同一條線". The transcript doesn't say that. The supported
  link is that the flood swept away the miners'/washing workers' 油毛氈 houses
  around the washing site (5635 18:12–20:02), so it belongs to the mining era.
- **Kyle's video-use fork:** https://github.com/Kowls0419/video-use, default
  branch `kyle` = upstream 92c2b34 + Dailies + optional reflect loop +
  `render.py --crf/--preset` and per-range `"grade"`. Upstream `main` has 4 newer
  commits (incl. **fps now preserved by default**) deliberately NOT merged —
  merging mid-project would change render output on a 59.94 fps source.
  `edl_to_fcpxml.py` is no longer used and was left out.
- **README rewritten:** working names, video names, the fork, install/startup
  prompts, and a caution to fetch before editing tracked files. The current
  viewer-facing README and production guide supersede this setup.
- **This file:** reflect-ledger codes (L05, L28, …) replaced by their rules in
  plain words; the "V1–V3" collision
  resolved; machine-specific notes tagged *(Kyle's machine)*; Session 3 now
  says the brief was 陳總's, relayed by Hoho.

### Update — 2026-09-27: prof's answers + kiln photos

**Prof's answers** (LINE, 2026-09-26 23:25–23:37): the split and the long
產業篇 first are OK · 王才慶/王財慶 are the same person → write **王財慶** ·
he sent kiln structure + clearing photos, 「這照片可用」 · originals: 「原照片我再找
當時可能沒存原檔」 — plan around the LINE copies. Still open (now the whole
`docs/questions_for_professor.md`): occupation framing, 怪手林's real name,
photo originals.

**Kiln photos** — `photo import session 7/` (Drive only; now gitignored along
with all image types). 24 JPGs = **20 unique**: `S__15073360–63` are byte-identical
re-sends of `…34–37`. The three `SCR-*.png` are Kyle's LINE screenshots, not
material. All LINE-compressed: 1280×960 / 1477×1108 (+ portraits) → use
**framed on a blurred background**; full-bleed 1080p would upscale 1.3–1.5×
and look soft.

| role in 焦炭窯篇 | files (`S__150733xx_0.jpg`) |
|---|---|
| overgrown, before | 34 (walking in), 35, 37 |
| structure + roots | **47** (stump growing on the masonry — the roots problem in one frame), 39 (root-covered wall), 59, 56 + **58** (arched kiln mouth) |
| clearing | **52** (chainsaw beside the stone wall), 49, 50, 51, 53, 54, 57, 48 |
| after | **46** (prof with sign before the cleared row of kiln mouths), 45 (group selfie) |
| survey | **38** — hand-drawn plan, several U-shaped chambers; candidate animated card |
| context | 36 (prof pointing, on the road) |

The plants being cleared in 49–54 are largely **芭蕉** — the proposal names
planted 芭蕉/柑橘 as the squatters' — so the clearing photos *are* the
occupation story visually. How explicit to be still waits on prof (open #1).
焦炭窯篇 is no longer blocked on material: interview audio (the *gala* and
self-contained-system passages) + this photo arc.

**Kyle's decisions (2026-09-27):**
- **Occupation framing: factual, no one named.** State what happened to the
  site (crops planted on it, roots breaking into the kiln, the class clearing
  it) and let the 芭蕉-clearing photos carry it. Never name or identify an
  occupant — defamation (誹謗) exposure on a 文化局-funded video. Taken off
  prof's list.
- **怪手林: nickname only, as she says it — no real name, no name card, not
  asked of prof** (Kyle, 2026-09-27). Caution: the passage continues into 「他也擁有很多國有林地…有些有
  租約，有些也沒有」 (5635 27:14–27:22) — that attaches the land question to a
  nameable person; don't use that line without Kyle deciding explicitly.
- **Original photos: wait for them.** 焦炭窯篇 is held until prof finds the
  kiln originals (he said they may not exist — if they don't, ask Kyle before
  building from the LINE copies). 戰俘營篇 and 產業篇 are not held by this.

**Lessons and session logging (2026-09-27, Kyle's request):**
- Kyle's video lessons moved from his private `reflect` ledger into this
  project's `lessons/video.md` (the only copy; reflect holds a pointer).
- Session headers identify Kyle and use sequential numbers. Entries record
  which agent handled each task; startup reads the lessons and ends with
  reflection, session logging, and a push when Kyle requests it.
- Fork `SKILL.md` (commit `38bf34e`): step 0 / Hard Rule 13 read a project's
  root `lessons/` folder with or without the reflect skill.
- **戰俘營篇 research (Hurst's Taiwan POW Camps Memorial Society):** the camp is
  **Kukutsu = 磺窟**, opened 1945-05-16 (groups 5/16, 5/30, 6/16), closed
  08-24; sweet potatoes + peanuts on an old tea plantation; two deaths;
  location found 1997; three ex-POWs at the 1999 memorial. Her account
  differs on arrival (「四月底五月初」), the year she met him (民國87 = 1998)
  and the number who returned (four) — keep her words, but cards use only
  Hurst's figures. 「三十七磅」 is unsupported → cut before it. 何麥克 is the
  Chinese name used by the society and the press. ASR 「黃富」 = 磺窟.

**Output spec + look for all three videos (Kyle, 2026-09-27):**
- **29.97 fps** (exact half of the 59.94 source → clean frame drop, no judder).
  1920×1080. Overlay/card timing rules are stated in frames, so compute them at
  29.97, not the 0613 set's 24.
- **Look C — clean documentary** (chosen over reusing the 0613 set's look).
  Mockup was made on 5636 26:21.
  - Subtitles: **Noto Sans TC Medium**, white, on a soft dark box
    (black ≈ 60 % opacity), bottom-centre. libass boxes (BorderStyle=3) are
    square-cornered; the mockup's rounded box needs PNG subtitle overlays —
    decide at the first preview.
  - Cards: paper `(238,233,222)` background, ink `(34,30,26)` text in **Noto
    Serif TC Medium**, rust accent `(150,70,40)` as a vertical rule / date line,
    grey `(120,112,100)` for the 「新店礦業文化路徑」 kicker. Left-aligned block.
  - Fonts: `edit/fonts/` (Drive only, gitignored; copied from the 0613 project).
  - Rules carried over: no `・` in any on-screen text; assert every glyph has
    ink before shipping a card; centre on the container, and check the rendered
    ink stays inside the margins.

**戰俘營篇 test cut (2026-09-27)** — `edit/pow_preview.mp4`, 112.7 s, 29.97 fps.
Built by `edit/build/pow.py` (cards → `edit/cards_pow/`, `edit/edl_pow.json`,
`edit/master_pow.srt`); rendered with the fork's new `render.py --fps
30000/1001 --sub-style … --fonts-dir edit/fonts --preview --no-loudnorm`
(fork commit `66d6d45`). Order: open card → 23:32 door → 23:59 asked about
foreigners → 25:15 nobody knew → 26:04 王財慶 → 29:10 POWs return and cry →
29:58 from 金瓜石 near death (stops before 三十七磅) → close card (Hurst's
dates, two deaths, source credit). Self-eval: no flashes at any cut; audio at
every cut below the surrounding speech (fades working); cards silent. Watch:
jump cuts at 39.98 and 85.90 (near-identical framing both sides); 29:10–30:20
is a two-shot with prof, not the tight single; source audio peaks near 0 dBFS.
Subtitle fixes hit: 阿託嘎→阿兜仔 ×4, 黃富→磺窟 ×1, 臺→台 ×1.

**Dailies r01 → r02 (Kyle reviewed; 1 note, applies to every cue):** subtitle
box padding uneven top vs bottom. Cause: libass `BorderStyle=3` pads from font
metrics (Noto Sans TC descent ≫ ascent). Fix: subtitles now come from
`edit/master_pow.ass` — per cue an exact vector-drawn box plus text centred on
the ink band; ASS `Fontsize` = ascent+descent (73) so text is 50 px. Measured
on the final render: ≈23 px top / 22 px bottom / 29 px each side on all 42
cues. Detours tried and dropped (all mistimed in render.py's composite): a
full-length qtrle overlay, PNG-in-MOV, per-cue PNG stills — see lessons L45/L46.
Render now: `render.py edit/edl_pow.json -o edit/pow_preview.mp4 --preview
--no-loudnorm --fps 30000/1001 --fonts-dir edit/fonts --sub-style "Encoding=1"`
(the dummy `--sub-style` stops render.py's default force_style overriding the
.ass styles). Corrections this round: 1.

**Dailies r02 (Kyle, 2026-09-28): no changes — 0 corrections** (r01: 1 → r02: 0).
The 戰俘營篇 test cut as it stands (`edit/pow_preview.mp4`, 112.7 s) is accepted.
Not yet decided: whether to trim toward 90 s, and the jump cuts at 0:40 / 1:26.

**Reasoning log:**
- Shortlist before verification because verification effort should follow what
  can reach the screen — 24 of the 34 台語 gaps are in passages we won't use.
- 戰俘營篇 is framed through her discovery story (1998 → 王財慶) rather than a
  POW chronology: it's first-hand, has a turn and a laugh, and sits in the
  best-framed stretch; the POW facts can ride on cards.
- 「三十七磅」 flagged rather than subtitled: 37 lb is not survivable for an
  adult, so either the ASR or the recollection is off.
- Fork on a separate `kyle` branch instead of rebasing onto upstream: keeps the
  tested version both machines will run, and leaves upstream sync as a
  deliberate later step.

**Outstanding:**
1. **產業篇 — next.** Long version first (~3 min), per prof. Candidate passages
   are in the Session 7 shortlist; exclude 5635 28:00–28:31; 怪手林 stays as the
   nickname and the passage must end before 27:14 (land-lease line).
2. **戰俘營篇 — accepted (Dailies r02, 0 notes)** at 112.7 s. Open: trim toward
   90 s or not; jump cuts at 0:40 and 1:26 (cover with a photo/card?).
3. **焦炭窯篇 — on hold** until prof finds the original kiln photos; if he says
   they don't exist, ask Kyle before building from the LINE copies. Occupation:
   factual, no one named.
4. **Kyle's own list:** 游月裡's full name for a title card · *gala* spelling ·
   「下層里」 (5635 07:07) · 政三煤礦 (5635 02:38) · the 10 台語 gaps
   (5635 06:44–08:01 ×8, 12:08; 5636 34:30).
5. Later, deliberately: merge upstream's 4 commits into the fork's `kyle` branch
   (includes an fps-default change — re-check renders after).
6. `temp/` holds the 怪手林 clips from 2026-09-27 — no longer needed; delete if unwanted.

## Session 8 — 2026-09-28 → 09-29 — Kyle (產業篇 long version; prof's posters; renderer + Dailies fixes)

Kyle drove and reviewed every round in
Dailies (產業篇 r01, r02; 戰俘營篇 r03).

**Strategy:** keep the split prof approved on 9/26 — 戰俘營篇 (done) · 焦炭窯篇
(standalone: the kiln grant's video deliverable is about the kiln) · 產業篇 =
產業變遷＋堰塞湖/土石流. Kyle re-pasted prof's four themes and asked to rethink;
the posters strengthened the merge rather than breaking it: prof's 中碳場 poster
says the flood 「沖毀中碳場所有工寮」, the coal settlement, so the flood is the end
of the industry story. The alternative (土石流篇 alone, coal folded into 焦炭窯篇)
was declined: it dilutes the grant video and would hold 產業 behind the kiln photos.

### prof's posters (`posters/`, Drive only — now gitignored)

19 `.docx` "posters" for the trail stations + one unrelated file
(`FTC 2026-27 英文競賽手冊(917).pdf`, a robotics manual — ignore). 43 images,
extracted to `docs/extracted/posters/` (gitignored). **Their captions are
shuffled between files** (formatting damage — Kyle's warning). Use images only;
write our own captions. Known facts and mislabels:
- The big aerial (`戰俘營/image2.png` = `茶廠/image2.png`, 2037×2059) has
  **「13AF 5 SEPT 47」** on the film — a US 13th Air Force photo, 5 Sept 1947.
  Poster captions for it (「文山茶廠1973年」, 「航照圖 1948」) are wrong.
- `場中碳` = **中碳場** (title reversed). `image1.png` (470×468) is the one captioned
  「新潭路2段民國52年 淹塞湖事件前航照」 — confirmed by Kyle's screenshot of the
  poster. `image2.png` (612×471) is the other pre-flood aerial (captioned 民國50).
- `站4 梯田.docx` actually holds the 新潭路二段老宅 poster; the 梯田 aerial is
  also used as the 站7 水力充電 image.
- Poster text worth using: 邵宗興「光復後塗潭聞人及建設重要人物，道路開築及電力引入」;
  磺窟溪「新店溪的支流，全長約4.25公里，發源於獅仔頭山北側」; 焦炭窯「煤炭進窯經過24小時
  高溫燃燒…質地較好的送煉鋼廠，較差的送打鐵舖」; 早期新潭路一、二段為台車道、三段為木馬路.
- For 焦炭窯篇: `站5焦炭窯/image1.png` (kiln interior) and `image3.png` (clearing
  by a kiln mouth) are NEW — not duplicates of the Session 7 LINE photos.
- Conflicts with the interview: the poster says the flood was **民國52** and that
  *her father* saw the creek run dry; on camera she says **民國58** and 王財慶.
  **Kyle: drop it** — subtitles keep her words, cards carry no year. The poster
  spells her **游月里** (not 尤) — confirm with her before any name card. POW poster
  says 5/16–8/15; the 戰俘營篇 closing card keeps Hurst's 5/16–8/24.
- Credits if used later: 塗潭社區 photo「攝影：劉育柔」; 磺窟溪 old photo「游寶彩提供」.

### 產業篇 — long version, accepted (Dailies r01: 8 notes → r02: 0)

Built by `edit/build/industry.py` (two-source fork of pow.py) →
`edit/cards_ind/`, `edit/edl_ind.json`, `edit/master_ind.srt/.ass`; preview
`edit/ind_preview.mp4`, **3:57 (237.4 s)**. Order: open card (新店區塗潭里 /
藍染、樟腦、煤礦、柑橘 / 一座山的產業變遷) → 5636 19:26 藍染 was earliest → her childhood
camphor memory (20:36, 20:56, 21:39) → coal, most bosses lost money, deaths
(5635 02:25, 04:12) → mandarins (04:41, 05:18, 05:49) → 邵宗興 (24:02) · 怪手林 cut
the road (26:29, ends before 27:14) · 「很有貢獻」＋洗煤廠 (28:59) → mid card
(塗潭里 / 堰塞湖與土石流, no year) → 民國58 debris flow (16:43, 17:07) → 6 am, the
water stops, 王財慶, run (18:54, 19:20–20:05) → 陳總「會再發生」(20:47, 21:04) →
close card (磺窟溪 / 發源於獅仔頭山北側 / 全長約 4.25 公里，匯入新店溪).
Covers (framed on blurred bg, captions ours): coal-bed map · 宗興洗煤場石碑 ·
中碳場 aerial image1 「新潭路二段 土石流前的航照」 · 磺窟溪.
Excluded: 28:00–28:31 (gossip), 27:14+ (land lease), 28:36–28:47 (private land
from his debts — same kind of claim), 02:38 政三煤礦 (unresolved name).

r01 fixes (Kyle): start at 「你說」 (the old in-point sat inside 對對對 → distortion);
cut 「那個塔」; end 0.11 s earlier after 「名字啊」; use the poster's image1 aerial,
out on 「白天」 (it now starts at 「我們這邊有一次土石流」 so it isn't a 3-s flash);
remove the 新店礦業文化路徑 kicker from cards; smooth the photo push. Kyle OK'd
「山段」→「三段」 by ear, all four kept jump cuts (0:21, 0:32, 1:08, 3:43), the 1:32
camera zoom (source), and the closing-card text.

### 戰俘營篇 — r03 → r04, accepted

Two covers over the jump cuts: 1947 aerial 「1947 年航照」 at 0:34–0:41 (ends as
「你不會來問我」 starts) and the memorial photo (no caption) at 1:19–1:29 — both OK'd
(r03). r03 note: remove the kicker from the opening card → r04 (the closing
card keeps its source credit). Subtitles now use exact segment timing (up to
~0.1 s closer to the voice at the end). Same renderer fixes as below.

### Renderer fixes (Kyle's fork, `~/.claude/skills/video-use`)
- **Cards after footage rendered darker** (paper 236 → 219): full-range camera
  footage + untagged limited-range cards in a stream-copy concat. `render.py` now
  converts every segment to limited range, tagged (L47). Was in 戰俘營篇 r02 too.
- **Lip sync drifted** up to 0.35 s by the end: per-segment AAC priming kept by
  `-c copy` concat. The join now copies video and re-encodes audio once with
  `aresample=async=1` — within one frame of the picture (L48). Also in 戰俘營篇 r02.
- Build scripts compute each segment's real length (footage rounds up to whole
  frames) instead of nominal EDL lengths — the nominal timeline drifted 0.32 s (L50).

### Dailies features (Kyle's request)
- **Claude's flags:** I write `edit/review/<stem>_flags.json` after self-eval;
  Dailies shows them as violet timeline marks + a checklist (OK / Change, `[`/`]`
  to jump, ▶ play, dashed region box). Answers are stored in the round JSON under
  `flags`; a Change is a normal note with `"flag": id`. Documented in SKILL.md.
- **Edit / delete notes** (✎ / 🗑); note ids never reused; saved-note thumbnails now
  load (`/frames/` was a 404); next free port if 8756 is busy.

**Reasoning log:**
- 產業篇 runs 3:57, not ~3:00 — exact word boundaries came out longer; Kyle
  accepted the length. The 3:05 variant (drop camphor + 藍染 exchange) stays the
  first cut if prof wants it shorter.
- Round numbers: 戰俘營篇's accepted r02 had no JSON (0 notes), so its next review
  was started as `--round 3` to match this log.
- I picked the wrong 中碳場 aerial (image2) because the poster's captions are
  unreliable; the flag caught it and Kyle's screenshot settled it. With damaged
  captions, show the candidates rather than choose silently.

**Outstanding:**
1. **Show prof both previews** (戰俘營篇 r04, 產業篇 long version) — his call on
   trimming 產業篇 toward 90 s (first cut: the 3:05 variant).
2. **焦炭窯篇 — still on hold** for the kiln originals. New material now exists
   (two poster kiln photos + the 24-hour burn text); if prof says the originals
   don't exist, ask Kyle before building from LINE copies.
3. **Kyle's own list:** 游月里 (poster) vs 尤 — confirm with her before any name
   card · *gala* spelling · 「下層里」 (5635 07:07) · 政三煤礦 (5635 02:38) · the
   10 台語 gaps (焦炭窯篇 passages).
4. Later, deliberately: merge upstream's 4 commits into the fork (fps default).
5. `temp/` still holds the 怪手林 clips from 2026-09-27 — delete if unwanted.

## Session 9 — 2026-09-29 — Kyle (焦炭窯篇 photo decision and build handoff)

Kyle drove the decision; Codex drove the planning and handoff. Claude had already
synced the project and the video-use fork, both up to date, and found no new project changes since Session 8. No cut or render was made this session.

**Strategy:** Kyle said to ignore the original kiln photos, clearing the hold
on 焦炭窯篇. Codex inspected the existing LINE and poster images and wrote a
build plan for Claude below. Aim for 90–120 seconds: the brief says each video
must be at least 90 seconds, and 120 seconds is Codex's editorial estimate,
not a client ceiling. Claude will propose the cut to Kyle before editing, as
the video-use skill requires.

**Build plan:** open on 塗潭焦炭窯; move through 游月裡老師's memory of her father
carrying the finished product (5635 06:38–07:26), the early-morning smoke and
queue (5635 07:31–08:01), then 陳總's account of 三段's power plant, kiln, coal
stockpiles and small pits (5635 11:45–12:00). Use a brief card for the poster's
「煤炭進窯經過24小時高溫燃燒」; then show roots in the masonry, clearing, the exposed
kiln mouths and the preservation work. The present-day half needs photos and
short cards because the interview does not discuss the rescue. Use 29.97 fps,
the accepted clean documentary look, paper cards, framed photos on blurred
backgrounds and Traditional Chinese subtitles. No name card until she confirms
whether her surname is 尤 or 游.

**Photo candidates:** LINE `S__15073358_0.jpg` (overgrown kiln mouth),
`S__15073347_0.jpg` (roots in stonework), `S__15073352_0.jpg` (chainsaw during
clearing), `S__15073346_0.jpg` (cleared kiln row), and optionally
`S__15073338_0.jpg` (hand-drawn survey plan). The poster adds
`站5焦炭窯/image1.png` (kiln interior) and `站5焦炭窯/image3.png` (clearing at a
kiln mouth), plus the 24-hour burn text. Write short factual captions for the
selected images from the proposal and the images themselves; the poster's
captions are shuffled, so inspect the images instead of copying those labels.
Never name or imply an occupant. Frame the compressed LINE copies rather than
stretching them full-bleed.

**Decisions:** use the available LINE copies and poster photos; frame the
compressed images on blurred backgrounds in the established 29.97 fps look C.
`docs/questions_for_professor.md` no longer asks for the kiln originals.
The existing factual rule remains: describe the site's condition and clearing,
without identifying an occupant. The two accepted videos were not changed.

**Reasoning log:** the interview covers the kiln's past but not its current
rescue, so the photo arc and short cards must carry the present-day half. The
5635 06:44–08:01 passage contains unresolved 台語 and *gala* spelling; the plan
avoids putting uncertain words on screen until Kyle verifies them. Poster
captions are shuffled, so Claude must inspect images and write new captions.

**Reflect:** no mistake needed correction during this planning-only session;
no new recurring lesson was added.

**Outstanding:**
1. Claude confirms the 焦炭窯篇 story shape with Kyle, then builds and reviews it
   from the existing assets. Kyle shows prof the accepted 戰俘營篇 and 產業篇
   previews; prof decides whether to trim 產業篇 toward 90 s (first cut: 3:05).
2. Kyle's own list: 游月里 (poster) vs 尤 — confirm with her before any name card ·
   *gala* spelling · 「下層里」 (5635 07:07) · 政三煤礦 (5635 02:38) · the 10 台語 gaps
   in the shortlisted passages.
3. Later, deliberately merge upstream's 4 commits into the fork (includes an
   fps-default change, so re-check renders afterwards).
4. `temp/` still holds the 怪手林 clips from 2026-09-27 — delete if unwanted.

## Session 10 — 2026-09-30 → 10-03 — Kyle (four professor review files)

Codex drove the edit and exports while Kyle reviewed the Dailies rounds and
made the cut and audio decisions. Claude checked the first kiln draft and wrote
the starting handoff.

**Strategy:** finish 戰俘營篇 and 焦炭窯篇, then follow prof's 2026-10-03 decision
to split the former long 產業篇 into separate 產業篇 and 土石流篇. Keep the existing
paper-card, framed-photo, burned Traditional Chinese subtitle look. Prepare
four files named with `篇` for Kyle to show prof.

**Decisions:** Kyle kept the tighter 82.7-second 焦炭窯篇 cut despite the original
≥90-second brief. Kyle also approved a fixed −1.5 dB audio gain for all four
review files. The long industry cut remains as its own earlier version; the new
產業篇 uses its industry half and a new closing card, while 土石流篇 begins with
the former middle card. No single-pass loudnorm was used. The final files are:

- `edit/戰俘營篇.mp4` — 112.768 s
- `edit/產業篇.mp4` — 137.971 s
- `edit/土石流篇.mp4` — 104.832 s
- `edit/焦炭窯篇.mp4` — 82.709 s

The four full-quality, unattenuated masters remain as `edit/final_pow.mp4`,
`edit/final_industry.mp4`, `edit/final_flood.mp4`, and `edit/final_kiln.mp4`.
Media stays on Drive and outside git.

**Review and changes:** 焦炭窯篇 r01 received 9 notes; r02 received 4; r03
received 2, with all four r03 flags marked OK. The r03 notes asked to remove
brief stray replies after 「堆煤的」 and 「木馬道」. Codex trimmed those tails,
kept the audible final 「道」 in the subtitle, and built the current 82.709-second
cut. Kyle accepted the last trim in r04: 0 notes and both flags OK. The long
產業篇 r03 received 1 note and both flags OK. Kyle's note changed 「這裡路」 to
「這里路」; the correction
fires once in the new 產業篇. The professor's instruction replaced one spoken
subtitle in 土石流篇 with 「這樣應該是上面山崩土石堵住溪流」; it fires once. The old 24-hour
kiln claim is removed. Kyle also accepted the new split 產業篇 and 土石流篇 in
their first Dailies rounds: 0 notes each; all six flags OK. No annotated frames
or further video changes were needed. 戰俘營篇 had already been accepted in r04.

**Verification:** rebuilt all EDLs, cards, SRT and ASS before full-quality
renders. The four review files are 1920×1080 at 30000/1001 fps, with durations
matching their previews. Rendered card paper measures Y=216. Final-composite
frames show the 「這里路」 and landslide corrections. Audio mean levels are about
1.5 dB below the full-quality masters. The last three Dailies rounds were all
accepted with 0 notes and all eight flags OK. Their review JSONs are in
`edit/review/`.

**Reasoning log:** the professor requested a four-film set, so the split uses
the approved material and cut point rather than reopening the long version's
story. The review files sit directly in `edit/`, where video-use already reads
and writes MP4 output, and are named for the professor's review. They have not
been sent to prof or LINE. The 82.7-second kiln runtime is Kyle's explicit
choice; the brief's ≥90-second minimum remains a known exception.

**Reflect:** one self-check initially measured card brightness after RGB gray
conversion and got 233 instead of the encoded Y=216; the direct-Y check
corrected it. Strengthened the existing colour-range lesson. A system Python
build attempt lacked `opencc`; rerunning under the skill virtual environment
resolved it before any render. No new lesson was needed for that environment
mistake because the skill already names its interpreter.
The final three Dailies rounds required no corrections, so no new lesson
qualified. Kiln's note counts fell 9 → 4 → 2 → 0; both new split films had
0 notes in their first rounds.

**Outstanding:**
1. The four Kyle-accepted review files are ready to show prof; no prof verdict
   has been recorded on this four-film set. Copies in sibling `../exports` were
   verified byte-for-byte and synced to Drive.
2. The original ≥90-second minimum conflicts with Kyle's approved 82.7-second
   kiln cut. If prof requires the minimum, add distinct material after his review.
3. Kyle's open source questions: 游月里 (poster) vs 尤 — confirm with her before
   any name card · *gala* spelling · 「下層里」 (5635 07:07) · 政三煤礦
   (5635 02:38) · the 10 台語 gaps in the shortlisted kiln passages.
4. Later, deliberately merge upstream's four commits into the fork, including
   its fps-default change, and re-check renders afterwards.
5. `temp/` still holds the 怪手林 clips from 2026-09-27; delete if unwanted.

### Session 10 addendum — 2026-10-03 — Kyle (Claude drove this part)
- **Ends:** every old closing card is gone. Each film now ends on one 7 s credits card (`edit/build/cards.py` → `credits_card`): 口述 陳國超、游月裡、張游寶彩、高燈立 · 攝影 李承洋 · 後製剪輯 楊大謙 · 指導單位 新北市政府文化局 · 執行單位 新北市陳昌梯醫師山林保育協會 (names as signed on the video consent form). 戰俘營篇 keeps its source line as a sixth row (資料來源 台灣戰俘營紀念協會). The card takes the closer's place under the same card name, so photo covers that hand off into it (產業篇 stele, 土石流篇 creek) still work.
- **Openings aligned:** all four openers share one layout (`cards.py` → `open_card`): place line (rust, 56) / headline (ink, 86) / one line (ink, 64), same fixed baselines. Wording: 戰俘營篇 新店區磺窟 · 磺窟戰俘營 · 1945 年 5 月，戰俘自金瓜石遷來; 產業篇 新店區塗潭里 · 塗潭里的產業變遷 · 藍染、樟腦、煤礦、柑橘; 土石流篇 新店區塗潭里 · 堰塞湖與土石流 · 民國 58 年的土石流記憶; 焦炭窯篇 新店區塗潭里 · 塗潭焦炭窯 · 一座山的煤礦記憶. 焦炭窯篇's inner 「從礦坑到焦炭窯」 card is unchanged. The facts that were on the old closers (磺窟溪 length, the POW dates and deaths) are no longer on screen.
- Re-rendered the four masters and the −1.5 dB review copies. Lengths: 戰俘營篇 113.7 s, 產業篇 138.0 s, 土石流篇 104.8 s, 焦炭窯篇 82.7 s. Footage and audio before the end are identical to the earlier versions (frames at 10/30/60 s and mean/peak levels); paper Y=216 on opening and credits cards. Review copies are in `exports/` inside the project folder.
- Spelling: the interviewee is **游月裡** (as signed), not 尤月里. Fixed in README and this log.
- YouTube series title for this set: **搶救塗潭焦炭窯**. Prof approved four films.

## Session 11 — 2026-10-05 — Kyle (prof's credits corrections)

Codex drove the two credits revisions. Kyle relayed prof's exact LINE wording
and identified the screenshot order: image 8 is 產業篇, image 9 is 土石流篇.
The third screenshot grouped 戰俘營篇 and 焦炭窯篇 in red; prof said the red
group is OK.

**Strategy and decisions:** keep the accepted edits and update only the last
credits scene in the blue-group films. 產業篇 now says
「塗潭社區社區產業演進」; 土石流篇 says「塗潭社區社區環境災害」.
Both say「指導單位　文化部文資局」. The repeated「社區」 follows prof's message
exactly. 戰俘營篇 and 焦炭窯篇 keep their existing title and 指導單位.

**Build and verification:** `edit/build/cards.py` now accepts a per-film
credits title and guiding unit without changing the default for the red group.
`industry.py` builds the 土石流篇 card, and `split_industry.py` builds the
產業篇 card. Rebuilt both EDLs and card MP4s with the video-use virtual
environment; tracked EDLs and subtitles did not change. Rendered full-quality
masters with no loudnorm, then made fixed −1.5 dB AAC review copies with video
stream copy. Both rendered credits were opened and checked against Kyle's
message. Decoded frames before the credits match the previous exports at
2/30/60/120 s (產業篇) and 2/30/60/90 s (土石流篇). Export format remains
1920×1080 at 30000/1001, durations 137.9708/104.832 s, and paper Y=216.
Speech mean in a matched 30–40 s sample fell exactly 1.5 dB in both exports.
The revised edit and project-local `exports/` copies are byte-identical;
the red-group export hashes did not change. Google Drive's browser shows
exactly four files in this project's `exports/` folder. The two revised
file IDs match DriveFS metadata with the new local byte sizes (131199270 and
89155992 bytes), and its operation and upload queues are empty. An older
土石流篇 metadata row remains cached locally but does not appear in Drive's
folder view; no duplicate was removed.

**Reflect:** prof supplied new wording, rather than finding a preventable
editing error. No new lesson qualified. The exact text was checked on the
rendered composite, not only on the source PNG.

**Outstanding:**
1. Kyle can show the revised `exports/產業篇.mp4` and `exports/土石流篇.mp4`
   to prof. No revised version has been sent by Codex. Prof's confirmation
   of these revisions remains open; the red-group films are OK.
2. Kyle's remaining source questions: *gala* spelling · 「下層里」 (5635 07:07)
   · 政三煤礦 (5635 02:38) · the 10 台語 gaps in the shortlisted kiln passages.
   The interviewee spelling is resolved as 游月裡 from her signed consent form.
3. Later, deliberately merge upstream's four commits into the fork, including
   the fps-default change, and re-check renders afterwards.
4. `temp/` still holds the 怪手林 clips from 2026-09-27; delete if unwanted.
5. The optional other-photo request remains in `docs/questions_for_professor.md`.

## Session 12 — 2026-10-05 — Kyle (YouTube publication)

Codex drove the YouTube metadata, publishing, playlist order, public README,
and factual production timeline. Kyle selected the four local MP4s in the
native upload picker, chose Public visibility, requested AI-use Yes and each
film's featured location, and decided to add custom thumbnails himself later.
Claude made an initial thumbnail set, then discussed a new visual theme and
frame options with Kyle in the other cmux pane.

**Strategy and decisions:** use the four verified `exports/*.mp4` files and
Claude's `private/youtube_0905.md` title/description draft. The two revised
films' YouTube descriptions say「指導單位｜文化部文資局」; the approved red-group
films retain「新北市政府文化局」. All four videos are Public, marked not made for
kids, marked AI use Yes at Kyle's request, and set to Chinese (Traditional).
The 產業篇、土石流篇、焦炭窯篇 location is the YouTube result for 塗潭里;
戰俘營篇 uses 磺窟戰俘營紀念碑. No custom thumbnail was attached. YouTube's
automatic thumbnails remain until Kyle chooses and uploads his own.

**Published videos and playlist:**

1. 產業篇 — 2:18 — https://youtu.be/F7Pn8-HIm2w
2. 土石流篇 — 1:45 — https://youtu.be/odgVTGZ_kWg
3. 焦炭窯篇 — 1:23 — https://youtu.be/eWMPvhX_uqo
4. 戰俘營篇 — 1:54 — https://youtu.be/gi6nBEnOoEw
5. Public playlist, manually ordered as above — https://www.youtube.com/playlist?list=PLNQi8ivhM3Y0

**Verification:** checked every description chapter start against the current
EDL range boundaries; all four sets match to the nearest second. Studio
confirmed `Video published` for each file, and the refreshed playlist showed
Public / four videos in the intended order with the correct IDs. Studio's
checks reported no issues for 焦炭窯篇、土石流篇、戰俘營篇 before publication.
產業篇's copyright check was still running unusually long at publication;
Studio allowed publication and had reported no issue. Recheck that result.
No video file was edited or re-rendered for YouTube.

**Reflect:** Kyle changed the thumbnail direction after seeing Claude's first
set; that was a design preference, so no recurring editing lesson was added.
A YouTube search for the kiln's name returned a location in Keelung; Codex
checked the city and used 塗潭里 instead, before saving a wrong location. No
published metadata required correction after a user's review in this session.

**Outstanding:**
1. Recheck 產業篇's unusually slow YouTube copyright check and any later
   notices. Kyle will choose and upload the custom thumbnails after Claude's
   new-theme frame options.
2. Prof's confirmation of the revised 產業篇 and 土石流篇 credits remains open;
   戰俘營篇 and 焦炭窯篇 were already OK. No video link was sent to prof by Codex.
3. Kyle's source questions: *gala* spelling ·「下層里」(5635 07:07) · 政三煤礦
   (5635 02:38) · the 10 台語 gaps in the shortlisted kiln passages.
4. Later, deliberately merge upstream's four commits into the fork, including
   the fps-default change, and re-check renders afterwards.
5. `temp/` still holds the 怪手林 clips from 2026-09-27; delete if unwanted.
6. The optional other-photo request remains in `docs/questions_for_professor.md`.

## Session 13 — 2026-10-05 — Kyle (publication titles and sole-editor documentation)

Codex drove the 0905 README, production-guide cleanup, live YouTube metadata,
private share text, and reflection lessons. Kyle clarified that he is the sole
editor, requested English as the README's primary language, and chose
「塗潭社區產業、環境與歷史｜口述影像」as the combined playlist name. Claude
compared the 0613 documentation, reviewed the 0905 README, and corrected the
two blue thumbnail labels. His proposed 0613 README edit was reverted after
Kyle clarified that the requested README change was for 0905. The 0613
repository has no changes from this work. Claude handles the coordinated
0905 commit and push under Kyle's identity.

**Strategy:** use the latest professor message for each film's public title,
rather than the superseded upload draft. Make the README useful to viewers:
English introduction, playlist and video links, subjects and lengths, credits,
and a link to the earlier films. Remove the repository-contents section and
retired second-editor setup. Keep 李承洋's cinematography credit.

**Decisions:**
- 產業篇's public title is「產業篇｜塗潭社區社區產業演進」.
- 土石流篇's public title is「土石流篇｜塗潭社區社區環境災害」.
- The repeated「社區」follows the professor's exact message. Both retain
  文化部文資局 as the supervising organization.
- 焦炭窯篇 and 戰俘營篇 retain their approved titles and 搶救塗潭焦炭窯 branding.
- All four descriptions now refer to the combined playlist and list the two
  corrected project names. Playlist description and private share text match.
  Narrative summaries, chapter times, video IDs, Public visibility, and order
  remain as accepted; the existing MP4s did not require another render.
- `docs/production.md` replaces `docs/collaboration.md`; the empty second-editor
  lesson file is removed. Retired setup administration was removed from the
  session log while keeping the editorial record. Local AGENTS.md and the
  shared reflect pointers now read the single active `lessons/video.md`.
- The comparison with 0613 kept clear viewer context, direct watch links, and
  production credits. 0613's existing tracked thumbnail/poster links are valid;
  0905 uses live YouTube links because its images are private, untracked assets.
  No licensing claim was added to 0905.

**Verification:** saved every Studio edit and confirmed Save returned to its
completed state. Reloaded the playlist details: selected title, corrected blue
names, both supervising organizations, and Public visibility persisted. The
public playlist shows four videos in the intended order with the two exact
new titles and unchanged red titles/IDs. Kyle had reported that the manual
thumbnail uploads and industry copyright check were done; Studio shows no
notice for 產業篇. Claude independently checked the README's four video links,
playlist, and earlier-project link against live pages. Checked the Gregorian
year against the original production record and arithmetic: ROC 58 + 1911 =
1969. Scanned documentation for retired collaboration instructions, broken
references to the removed guide/lesson file, and formatting errors.

**Reasoning log:** the professor's title correction applies across the public
publication, not just the rendered credits. One combined playlist should not
impose the kiln project's name on differently titled films. The public README
uses English for explanations and original Chinese for names and project
titles; the internal production guide holds operational instructions.

**Reflect:** two preventable mistakes were corrected: superseded title wording
survived in public metadata and thumbnails; Codex also converted ROC year 58
incorrectly to 1959 in the English README and private timeline. Claude caught
the date, and both now say 1969. Added generalized publication-naming and
calendar-conversion lessons. Each correction task converged from one correction
to zero after verification. The sole-editor workflow and English README were
Kyle's updated requirements. The proposed 0613 README edit was reverted after
scope clarification; no video edit or publication URL changed.

**Outstanding:**
1. Kyle must replace only the two uploaded blue thumbnails with
   `private/youtube_thumbnails/產業篇_thumbnail.jpg` and
   `private/youtube_thumbnails/土石流篇_thumbnail.jpg`. Claude corrected their
   top labels; the other two JPGs are byte-identical to Kyle's uploads. Prior
   blue JPGs are in `private/youtube_thumbnails/previous_uploaded/`.
2. Prof's confirmation of the revised 產業篇 and 土石流篇 credits remains open;
   戰俘營篇 and 焦炭窯篇 were already OK. Codex sent no link to prof.
3. Kyle's source questions: *gala* spelling ·「下層里」(5635 07:07) · 政三煤礦
   (5635 02:38) · the 10 台語 gaps in the shortlisted kiln passages.
4. Later, deliberately merge upstream's four commits into the video-use fork,
   including the fps-default change, and re-check renders afterwards.
5. `temp/` still holds the 怪手林 clips from 2026-09-27; delete if unwanted.
6. The optional other-photo request remains in `docs/questions_for_professor.md`.

## Session 14 — 2026-10-05 — Kyle (final YouTube audit and share preparation)

Codex drove the final settings audit and thumbnail verification. Kyle asked
Claude to make a playlist cover using the earlier playlist layout in the new
0905 theme, then draft the message to prof after Codex verified YouTube.
Claude replied to Codex through the current cmux pane after each completed part.

**Strategy:** check saved Studio settings for every film and the public
playlist, then compare actual live thumbnails with the current approved names.
Prepare the playlist artwork and a message Kyle can send with all five links.

**Decisions and results:**
- All four films remain Public, not made for kids, with no age restriction,
  no paid promotion, AI-use Yes, Traditional Chinese video language, and no
  Studio notice. They belong to the intended combined playlist.
- Locations: 產業篇、土石流篇、焦炭窯篇 use Tutan Village (塗潭里);
  戰俘營篇 uses Kukutsu POW Camp Memorial (磺窟戰俘營紀念碑).
- Standard YouTube License, Nonprofits & Activism category, embedding enabled,
  and comments On with Basic moderation were present consistently. Optional
  recording-date and title/description language fields remain unfilled; no
  request depended on filling them. No setting needed another correction.
- The playlist is Public, named「塗潭社區產業、環境與歷史｜口述影像」and
  manually ordered 產業篇 → 土石流篇 → 焦炭窯篇 → 戰俘營篇. Titles, credits,
  descriptions, and live chapter starts match the current publishing decisions.
- Codex downloaded and opened all four LIVE full-size YouTube thumbnails.
  Kyle has already uploaded both corrected blue title labels. The red thumbnails
  also match the approved style/wording, so no video-thumbnail upload remains.
- Claude made `private/youtube_thumbnails/playlist_thumbnail.jpg` (1280×720):
  four selected frame slices under a paper scrim with centered ink/rust type,
  following the previous playlist format in the current visual theme. It uses
  the combined title, four film names, and no speaker name or umbrella kiln
  branding. Codex opened the image at full size. Builder and images are private.
- Claude drafted `private/message_to_prof_0905.txt`: brief greeting, all four
  film titles and lengths, each video URL on its own indented line, playlist
  URL, and note that the two blue titles/guiding-unit credits were corrected.
  It asks prof to review those revisions; it does not assert his acceptance.
  Kyle sends the message. The neutral share list remains separately available
  in `private/分享訊息.txt`.

**Verification:** the audit reads selected radio-button states, displayed
language/location/playlist fields, enabled embedding, and saved-state controls
from each actual Studio details page. Public playlist read-back confirms its
name, four correct IDs and order. All live chapter starts still match the
previously verified current EDL boundaries. Private audit evidence is in
`private/youtube_final_audit.json`. No film was rendered, replaced, or sent.

**Reasoning log:** a local corrected JPG does not prove its live upload; the
public thumbnail was downloaded and viewed. That check resolved the stale
blue-thumbnail upload item from Session 13. A separate playlist cover uses
neutral collection wording because the films have different approved project
names. Prof's message is prepared for Kyle, with no direct external send.

**Reflect:** no new preventable mistake qualified. The audit found no wrong
saved setting; thumbnail verification confirmed Kyle had already finished the
two replacements. Claude completed the playlist artwork and message draft.

**Outstanding:**
1. Kyle uploads `private/youtube_thumbnails/playlist_thumbnail.jpg` as the
   playlist's custom thumbnail; the public playlist still uses 產業篇's image.
   The public playlist has an Edit Thumbnail control over its cover.
2. Kyle sends `private/message_to_prof_0905.txt` to prof. Prof's confirmation
   of the revised 產業篇 and 土石流篇 remains open; the red films were already OK.
3. Kyle's source questions: *gala* spelling ·「下層里」(5635 07:07) · 政三煤礦
   (5635 02:38) · the 10 台語 gaps in the shortlisted kiln passages.
4. Later, deliberately merge upstream's four commits into the video-use fork,
   including the fps-default change, and re-check renders afterwards.
5. `temp/` still holds the 怪手林 clips from 2026-09-27; delete if unwanted.
6. The optional other-photo request remains in `docs/questions_for_professor.md`.

## Session 15 — 2026-10-06 — Kyle (Drive-only documents)

Codex drove this change at Kyle's request. Claude was notified of Git ownership
and the updated storage rule. No video or YouTube setting changed.

**Strategy:** keep all working documents in Google Drive and exclude the entire
`docs/` folder from GitHub.

**Decisions:** added `/docs/` to `.gitignore` and removed
`docs/production.md` and `docs/questions_for_professor.md` from Git tracking.
Both files remain locally available on Drive. The local production guide,
agent instructions and handoff now say never to stage `docs/`.

**Verification:** no `docs/` path remains in the Git index; both documents are
ignored. SHA-256 checks before and after untracking confirm the local copies
were preserved. Staging excludes media, private material and the existing
untracked `edit/cards_kiln/` folder.

**Reasoning log:** an ignore rule alone cannot stop tracking files already in
Git. Removing them from the index preserves local working copies and removes
them from the current published branch. Previous commits retain their history.

**Reflect:** no new preventable mistake qualified; this was an updated storage
preference.

**Outstanding:**
1. Kyle's upload of `private/youtube_thumbnails/playlist_thumbnail.jpg` as the
   playlist's custom cover has not been confirmed.
2. Kyle has sent the videos to prof. Prof's confirmation of the revised
   產業篇 and 土石流篇 remains open; the red films were already OK.
3. Kyle's source questions: *gala* spelling ·「下層里」(5635 07:07) · 政三煤礦
   (5635 02:38) · the 10 台語 gaps in the shortlisted kiln passages.
4. Later, deliberately merge upstream's four commits into the video-use fork,
   including the fps-default change, and re-check renders afterwards.
5. `temp/` still holds the 怪手林 clips from 2026-09-27; delete if unwanted.
6. The optional other-photo request remains in the Drive-only
   `docs/questions_for_professor.md`.
