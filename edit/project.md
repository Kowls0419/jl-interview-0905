# Project memory — JL Interview 0905

Companion to `JL Interview 0613` (新店礦業文化路徑 heritage series; its three
videos — the **"0613 set"** — were DELIVERED 2026-08-14; that project's log is on
Kyle's Drive only). Same client, same association, new shoot.

**Who's who** (陳總 = 陳國超 = "prof", Hoho, JL, speaker IDs) is in the root
`README.md` — read it before this file. **Video names:** 焦炭窯篇 · 戰俘營篇 ·
產業篇. Older entries say "V1–V3" for the *0613 set*; Session 4's
"V1 焦炭窯 · V2 戰俘營 · V3 產業…" is this project's working split under the old
labels. Notes tagged *(Kyle's machine)* refer to paths/hosts only he has.

**Status (as of 2026-09-26):** candidate-passage shortlist done (Session 7); no
EDL or cut yet. Waiting on prof's answers (video count, length, photo
originals, how to cover the kiln itself). See the latest session.

## Session 1 — 2026-09-18 (`/video-use init` — inventory, no cutting)

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
- `speaker_1` — **尤月里老師**, the main voice. Born and raised there. 5635 16.2
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
classroom one. 尤月里老師 is teaching the volunteer guides the history of the
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
  hauled coal. Then the debris flow — she ran down after school to find every
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
- `尤月里` / `月婷老師` — she is the *teacher*, so not in the 學員 list.
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

## Session 2 — 2026-09-20 (collaboration setup — no cutting)

**Strategy:** Kyle wants a peer (GitHub: `CYLI310`) to be able to collaborate
on the edit from his own PC. No editorial work happened this session — this
was infrastructure: setting up the git/GitHub + Google Drive split so both
people's Claude sessions can pick up full context.

**Decisions:**
- Project root (`JL Interview 0905/`, the parent of this `edit/` dir) is now a
  git repo, pushed to **https://github.com/Kowls0419/jl-interview-0905**
  (private). Kyle and CYLI310 both have access.
- **Split:** git tracks only small text — `edit/project.md` (this file),
  `edit/takes_packed.md`, `edit/transcripts/*.json`, `docs/questions_for_professor.md`,
  and (once they exist) `edl.json`/`master.srt`/`review/*.json`. Everything
  binary (`raw footage/`, `BTS pics/`, renders, `clips_graded/`) stays out of
  git via `.gitignore` and continues to live in Google Drive exactly as
  before — Drive's own sync is untouched by any of this.
- The Drive folder was link-shared with the peer for the raw footage/renders:
  https://drive.google.com/drive/folders/1wwfvlHXUNO4crt0ZVVjCH3QRvXbb3hyh
- `README.md` at the project root documents the full setup: repo-vs-Drive
  split and why, the peer's first-time setup steps, Kyle's own per-session
  workflow (`git pull` → edit → `git add edit && git commit && git push`),
  and a Cautions list (don't both hand-edit `edl.json` at once; Drive must be
  a real desktop sync on the peer's machine, not browser-only access; check
  `git status` before committing in case a binary ever slips past
  `.gitignore`; GitHub needs a PAT/SSH key, not an account password).
- `.gitignore` also excludes `*.pdf` by default — defensive, since
  `questions_for_professor.md` references course review documents that could
  land in this folder later and shouldn't be committed without a deliberate look first.

**Reasoning log:**
- Git-in-a-Drive-synced-folder risk (Drive touching `.git/` internals
  mid-write) was flagged but accepted as low-probability for this project's
  usage pattern (infrequent commits, effectively one person committing at a
  time) rather than solved with a sync exclusion.
- Chose repo-root = project folder (not just `edit/`) so the layout is
  self-documenting for a new clone and matches the sibling `JL Interview 0613`
  repo's structure.

**Outstanding:**
- Peer (CYLI310) hasn't completed first clone/setup yet as of this session.
- Everything from Session 1's Outstanding list is still open — no editorial
  work has started.

## Session 3 — 2026-09-20 (陳總's brief, relayed by Hoho + 焦炭窯 proposal)

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

## Session 4 — 2026-09-20 (decisions + framing analysis)

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

- **5635**: two-shot most of the way. 尤月里 sits camera-right, 陳國超 camera-left
  and frequently **clipped by the left edge** (04m, 07m, 25m, 37m). At **34–37m**
  the camera pans right to bring in the third speaker (pink shirt, grey hair) —
  matches `speaker_4`'s 朱再叔/周再思 block at 31:41–37:40.
- **5636**: noticeably more single-on-尤月里, and the best framing in the whole
  shoot sits at **25–37m** — which is the 戰俘營 block. The POW video therefore
  has the strongest available pictures, which is lucky rather than planned.
- The TV behind them shows the photo slideshow early in 5635 (01–07m, purple)
  and is off/black thereafter.

### ⚠ Punch-in does NOT fix the two-shot (tested — `edit/verify/crop_compare.jpg`)

I tested 1.33× (1440 crop) and 1.5× (1280 crop) punch-ins on a clean two-shot.
**Both make it worse.** The obstruction is the flower basket sitting *between*
the two speakers, not clutter at the edges — so cropping inward enlarges the
basket and 尤月里 stays pinned to the right edge regardless. To get a clean single
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

## Session 5 — 2026-09-20 (repo layout: `edit/` is the skill's namespace)

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

## Session 6 — 2026-09-26 (repo/infra housekeeping; still no cutting)

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

## Session 7 — 2026-09-26 (segment shortlist; question doc scoped to it; video-use fork)

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
  尤月里's full name for the title card (5635 00:13) · 「三十七磅」 (5636 30:25,
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
- **README rewritten** for JL: who's-who, video names, the fork and how to keep
  it in sync (Kyle pushes skill changes; JL pulls before rendering), updated
  install/startup prompts, and a caution to fetch before editing tracked files.
- **This file:** reflect-ledger codes (L05, L28, …) replaced by their rules in
  plain words, since JL doesn't have that ledger; the "V1–V3" collision
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
1. Kyle sends the rewritten `docs/questions_for_professor.md` to prof.
2. ~~Prof's answers~~ mostly in (see Update 2026-09-27). Still open with prof:
   photo originals only (焦炭窯篇 waits on these).
3. Kyle's own list (see "Moved to Kyle" above): names/spellings and the 10 台語 gaps.
4. JL's first-time setup against the new README (fork, not upstream).
5. Once answers land: confirm strategy (Hard Rule 11), then EDLs — 產業篇 long
   version first. Decide target fps before building any overlay.
6. Later, deliberately: merge upstream's 4 commits into the fork's `kyle` branch.
