# JL Interview 0905

Interview shoot for the 新店礦業文化路徑 (Xindian mining heritage trail) series —
same client/association as `JL Interview 0613` (the **"0613 set"**: three
videos delivered 2026-08-14). One continuous ~88.5 min session across 3 source
files: opening/mic check, then two long-form segments with 尤月里老師 and others,
covering 塗潭里 / 煤礦 / 焦炭窯 / 土石流 / 獅仔頭山 / 戰俘營 history.

**Status (2026-10-03):** Four professor review files are prepared:
戰俘營篇 · 產業篇 · 土石流篇 · 焦炭窯篇. The long 產業篇 was split at the
professor's request. The new split and latest kiln trim await Kyle's review.
Details are in the latest session of `edit/project.md`;
open questions for the client are in `docs/questions_for_professor.md`.

This repo is the **decision layer** for the edit (cut choices, transcripts,
notes). The **raw footage and rendered video live in Google Drive**, not here
— see below for why and how to get them.

## Who's who (read this first)

The session log uses these names without re-introducing them.

| Name in the log | Who |
|---|---|
| **Kyle** (GitHub `Kowls0419`) | Project owner and editor. Owns this repo and the video-use fork. |
| **JL** (GitHub `CYLI310`) | Kyle's collaborator; co-shot the footage. The folder name `JL Interview` is his initials. |
| **陳國超** = **陳總** = **"prof"** (LINE: `jason chen 1526`) | The client. 協會理事長, course leader on camera (`speaker_0` in the transcripts), and author of the 焦炭窯 grant proposal in `docs/`. `questions_for_professor.md` is addressed to him (「老師」). |
| **Hoho** | Kyle's mom — sometimes relays prof's messages (e.g. the original brief over LINE). Not the client. |
| **尤月里老師** | Main interviewee, born and raised in 塗潭里 (`speaker_1`). |
| **游寶彩** (寶彩姐/老師) | Senior guide, mentioned often on camera; listed participant in the proposal. |

⚠ Transcript speaker IDs (`speaker_0`, `speaker_1`, …) are **per file**, not
stable across the three sources — check the file before trusting an ID.

**Video names.** This project's three videos are called by topic —
**焦炭窯篇**, **戰俘營篇**, **產業篇** (industry + 土石流). "V1–V3" in older log
entries means the *0613 set*, not these.

## Repo vs. Drive — what lives where

| | Git (this repo) | Google Drive |
|---|---|---|
| Contains | `edit/project.md`, `lessons/*.md`, `edit/takes_packed.md`, `edit/transcripts/*.json`, `edl.json` / `master.srt` / `review/*.json` (once they exist), `docs/*.md` | `raw footage/`, `BTS pics/`, `photo import */` + `posters/` (client photos and prof's station posters — the posters' captions are shuffled, see Session 8), `edit/clips_graded/`, `edit/verify/`, previews, `final.mp4`, animation renders, `review/frames/*.png`, `docs/*.pdf` |
| Why | Small text, diffable, mergeable — this is the actual editorial history | Large binaries — git can't diff/merge video and GitHub caps file size anyway |

Drive folder (raw footage + renders): **[JL Interview 0905 on Drive](https://drive.google.com/drive/folders/1wwfvlHXUNO4crt0ZVVjCH3QRvXbb3hyh?usp=drive_link)**

`edit/` is the **video-use skill's** namespace — only what the skill reads and
writes belongs in it. Project admin (client questions, the proposal) goes in `docs/`.
Editing lessons go in `lessons/` (see below).

⚠ Git history was squashed to one commit on 2026-09-26, so **`edit/project.md`
is the editorial history** — `git log` won't tell you how the edit got here.

## Tooling: both machines run the same video-use

This project is edited with **[Kyle's fork of video-use](https://github.com/Kowls0419/video-use)**
(default branch `kyle`), a Claude Code skill based on the open-source
[browser-use/video-use](https://github.com/browser-use/video-use). **Use the
fork, not upstream.** The fork adds:

- **Dailies** — the browser review app (see below). Upstream doesn't have it.
- A `render.py` that understands per-range `"grade"` in `edl.json` and
  `--crf`/`--preset`. Upstream silently ignores those, so the same EDL would
  render **differently** on the two machines.
- An optional `reflect` learning loop that is Kyle's own. JL doesn't need the
  `reflect` skill — the shared editing lessons live in this repo's `lessons/`
  folder instead (below), and project-specific rules (e.g.
  Traditional-Chinese-only subtitles) are written into `edit/project.md`.

**Keeping the two in sync.** Kyle's copy lives in his Google Drive, but Drive
only syncs to *his* machines — changes reach JL through GitHub only:

- **Kyle**, after changing `SKILL.md` or anything in `helpers/`:
  ```bash
  cd ~/.claude/skills/video-use && git add -A && git commit -m "what changed" && git push
  ```
- **JL**, before any session that renders:
  ```bash
  git -C ~/.claude/skills/video-use pull
  ```
- Before rendering an EDL the other person wrote, check you're on the same
  version: `git -C ~/.claude/skills/video-use log -1 --oneline` on both machines.

## Lessons (shared, one part each)

Generalized editing mistakes and the rule that prevents each, so the same fix
isn't re-requested next session. Both Claudes **read both files before any
render**; each person **writes only their own**:

| file | written by | IDs |
|---|---|---|
| `lessons/video.md` | Kyle's sessions | `L…` (Kyle's global sequence — gaps are normal) |
| `lessons/video-jl.md` | JL's sessions | `J01`, `J02`, … (next free ID is at the top of the file) |

A lesson is worth adding when a mistake was **preventable and likely to
recur** — typically something the other person had to correct in a Dailies
round. Write the **rule, not the instance** ("never use `・` in on-screen text —
it renders as a box", not "fixed the dot at 1:32"). Before adding, re-read both
files and strengthen an existing entry with a `Seen:` line rather than adding a
near-duplicate. Format:

```
### J01 — one-line title
- Context:    when this situation arises
- Symptom:    what the user or a check sees
- Root cause: why it happens
- Rule:       the thing to DO to prevent it
- Scope:      video + sub-tags (zh-subtitle, overlay-transitions, audio-render, …)
- Seen:       project / Dailies round / date / who
```

## Who did what — the session log

Every entry in `edit/project.md` is headed `## Session N — YYYY-MM-DD — Kyle`
or `— JL`, numbered in one shared sequence. Commits carry each person's own git
identity. So "what did JL do last time?" is answered by the latest `— JL`
entry plus `git log --author`.

## Kyle's workflow (project owner)

Google Drive syncs this whole folder to disk as before. Git rides on top,
tracking only the small text files.

1. **Before a session:** `git pull` — picks up anything JL pushed.
2. **Edit as normal** (video-use through Claude Code, or by hand). Drive
   uploads footage/renders in the background automatically.
3. **After a session:**
   ```bash
   git add edit docs lessons
   git commit -m "short description of what changed"
   git push
   ```
   `git status` shows exactly what's new — `.gitignore` silently excludes binaries.

## JL's workflow (first-time setup)

1. **Accept the GitHub invite**, then get the repo (see step 3 for where).
   Pushing needs a [personal access token](https://github.com/settings/tokens)
   or an SSH key — GitHub no longer accepts account passwords for git.

2. **Get the Drive folder** from the link above (ask Kyle for edit access if
   it's view-only) and make sure the **Google Drive desktop app is actually
   syncing it to your disk** — a browser tab is not enough; video-use reads and
   writes real local files.

3. **Line up the folder** so the repo and the Drive folder merge into one
   local directory:
   ```
   JL Interview 0905/
   ├── .git/                 ← from git
   ├── edit/                 ← merged: repo gives text files, Drive gives the rest
   ├── docs/                 ← .md from git, .pdf from Drive
   ├── raw footage/          ← Drive only
   └── BTS pics/             ← Drive only
   ```
   Easiest: let Drive sync the folder locally first, then inside it run
   ```bash
   git init && git remote add origin https://github.com/Kowls0419/jl-interview-0905.git && git fetch && git checkout -f main
   ```
   rather than `git clone` into a location that doesn't exist yet.

4. **Install the tooling** with the one-time prompt below (Kyle's video-use
   fork, Dailies included). Needs `ffmpeg`/`ffprobe` on PATH. An **ElevenLabs
   API key is only needed to transcribe *new* footage** — this project's
   transcripts are already in `edit/transcripts/` and must not be re-done.

5. **Every session after that:** use the startup prompt below — it pulls both
   repos, reads the lessons, and at the end logs the session as yours, adds any
   new lesson to `lessons/video-jl.md`, and pushes.

## Claude-assisted workflow (recommended)

Both of you drive this through Claude Code with the video-use skill, so the
smoothest path is two copy-pasteable prompts.

### One-time: install video-use

Open Claude Code (anywhere — not necessarily inside the project) and paste:

> Install the video-use skill from https://github.com/Kowls0419/video-use (it's
> a fork — use it, not upstream browser-use/video-use; its default branch
> `kyle` already includes the Dailies review app). Clone it to a stable local
> path and follow its own `install.md` exactly: ffmpeg on PATH, Python deps,
> register the skill so `SKILL.md` is discoverable. Skip the ElevenLabs key
> unless I say I have new footage to transcribe. I don't use the `reflect`
> skill — that's expected. Verify by running one real command (e.g.
> `helpers/render.py --help` and `helpers/dailies_server.py --help`) rather
> than just checking the files exist.

### Every session: startup prompt

Open Claude Code **inside this project folder** (after Drive has finished
syncing it) and paste — the same prompt works for both of you:

> This is a `video-use` project shared via git + Google Drive — read its
> `README.md` at the project root first for how that split works and who
> everyone is. Work out who is driving this session from
> `gh api user --jq .login` (`Kowls0419` = Kyle, `CYLI310` = JL); if that's
> unclear, ask me. Run `git pull` to sync the latest edit decisions, and
> `git -C ~/.claude/skills/video-use pull` to make sure video-use is current.
> Then read `edit/project.md` (full session log — pay attention to the most
> recent session, and to what the *other* person did since my last session),
> `docs/questions_for_professor.md` for open items, and both files in
> `lessons/` — treat those lessons as rules to self-check against before any
> render. Summarize where things left off in one or two sentences, then let's
> continue.
>
> Before we stop:
> 1. **Reflect:** list any mistakes that had to be corrected this session. For
>    each one that was preventable and likely to recur, add a generalized
>    lesson to *my* lessons file (`lessons/video.md` if I'm Kyle,
>    `lessons/video-jl.md` if I'm JL) in the README's format, or strengthen an
>    existing entry. If nothing qualifies, say so.
> 2. **Log:** append a new session entry to `edit/project.md` per the skill's
>    memory format, headed `## Session N — <date> — <Kyle|JL>` with the next
>    shared session number, saying who did what.
> 3. **Push:** `git add`/`commit`/`push` whatever changed under `edit/`,
>    `docs/` and `lessons/`.
>
> Don't put anything in `edit/` that the video-use skill doesn't itself read or write.

### Dailies across two machines

Dailies is the review step (step 8 of the video-use process): point it at a
rendered preview and it opens a browser page where you scrub the video, type
timestamped comments, and draw pen/arrow/box annotations on a paused frame —
much faster than describing "at 1:32 the caption is cropped" in prose.

It runs as a local server — per-machine, not a shared live session. A review
writes `edit/review/<stem>_rNN.json` (small text — reaches the other person via
`git pull` once committed) and `edit/review/frames/*.png` (gitignored — reaches
them via Drive sync). So reviews are asynchronous: **whoever runs Dailies
commits and pushes right after**, so the round numbering (`_r01`, `_r02`, …)
stays consistent for whoever picks it up next.

## Cautions

- ⚠️ **Write only your own lessons file** — Kyle `lessons/video.md`, JL
  `lessons/video-jl.md` — so the two never conflict.
- ⚠️ **Never both edit `edl.json` at the same time.** Two concurrent edits
  conflict messily and git can't merge them cleanly. Say who's driving the cut
  before you start.
- ⚠️ **Same video-use version on both machines** before rendering each
  other's EDLs (see "Keeping the two in sync").
- ⚠️ **`git fetch` and compare with `origin/main` before editing tracked
  files**, not after — this repo is pushed to from two places.
- ⚠️ **Drive must be a real desktop sync, not just browser access.**
- ⚠️ **Check `git status` before committing.** If a huge binary ever shows as
  staged, stop and fix `.gitignore` rather than committing it.
- ⚠️ **GitHub needs a token or SSH key, not your account password.**
