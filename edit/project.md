# Project memory — JL Interview 0905

Companion to `../2026/JL Interview 0613/edit/project.md` (新店礦業文化路徑 heritage
series, V1–V3 DELIVERED 2026-08-14). Same client, same association, new shoot.

**Status (as of 2026-09-20):** preparatory work only — inventory,
transcription, and collaboration setup. Actual editing (first cut, EDL,
grading, subtitling) has not started.

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
`scratchpad/materialize.sh` (retry loop; log in `scratchpad/materialize.log`).
Tail verified decodable. kyles-imac is on Tailscale but **relayed** (DERP "hkg"),
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

### ⚠ ASR term errors to resolve before any subtitle burn (L05 / L40 class)

Scribe returns **Simplified**; prior project converted with OpenCC `s2twp` and
`L06` requires Traditional-only output. These need an authoritative spelling from
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

Per **L40**, whatever map we build gets per-key hit counters, and entries must be
written against the string *as it arrives at the replace* (post-OpenCC).
Per **L05**, re-check every domain term on every subtitle pass.

### Framing / craft notes for whenever cutting starts

- 59.94fps source. V1–V3 delivered at 24. Decide the target fps *before* building
  any overlay — L02/L03's flash rules are stated in frames and the drift maths
  changes.
- The flower basket blocks centre frame throughout. In the wide two-shot both
  speakers sit at the far edges with dead space between them — a crop or a cover
  is going to be wanted more often than in V1–V3.
- ~23 min into 5635 the camera is wide and both subjects are in profile facing
  each other, not camera. **L08** says cover those stretches rather than
  globally cropping.
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

## Session 3 — 2026-09-20 (brief received from Hoho + 焦炭窯 proposal)

**Still no cutting.** Brief and source doc logged; strategy not yet confirmed.

### The brief (Hoho, LINE, 15:49–15:50)

Four themes in the Saturday recording:
1. 獅仔頭山地區產業變遷（邵宗興）
2. 戰俘營
3. 焦炭窯
4. 社區堰塞湖及土石流

Then: 「隨意弄成約3個90秒的影片」 / 「3個最少90秒影片就可以」 — roughly three
videos, each **at least 90 seconds**. More docs promised.

### ⚠ Three numbers that do not agree — resolve before building

- Hoho's message says **3 videos**.
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
intended to make the community's claim visible. Worth confirming with Hoho how
directly that should read on screen.

**© terms:** the signed 授權同意書 grants 文化局 a non-exclusive, royalty-free,
unlimited licence for non-profit promotion, and waives 著作人格權 toward them.
陳國超 retains 著作財產權. Relevant to how Kyle is credited — check before
assuming a 後製剪輯 credit like V1–V3 carries over.

### Outstanding

1. **3 or 2 videos? Which themes, against which budget?** (see above)
2. Target length — "at least 90s" is a floor; is there a ceiling?
3. Remaining docs Hoho is sending.
4. The photo set + 堰塞湖 before/after comparison promised on camera.
5. Still needed: the `[台語]` gaps, and the unresolved names above.

## Session 4 — 2026-09-20 (decisions + framing analysis)

### Decisions taken (Kyle)

- **3 videos, each ≥90 s** — quoting Hoho's brief directly.
- **Working assumption on the merge** (mine, NOT yet confirmed by 陳總):
  V1 焦炭窯 · V2 戰俘營 · V3 產業變遷（邵宗興）＋ 堰塞湖/土石流.
  Four themes into three. **Confirm before building.**
- **Subtitles: Traditional Chinese only.** Settles L06 for this project; no
  bilingual pass. The 台語 gaps still have to be filled by ear.
- **Visual treatment: rethink for the two-shot**, not a V1–V3 reuse.
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
what V1–V3 did anyway. That makes the photo originals a hard dependency, not a
nice-to-have — currently the only copies are 24 PDF-embedded images, mostly
under 1024 px, of which 3 are usable at framed size.

This is a case of L28/L41's shape: the obvious fix was tested before being
proposed, and the test killed it.

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
