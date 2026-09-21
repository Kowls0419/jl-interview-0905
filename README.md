# JL Interview 0905

Interview shoot for the 新店礦業文化路徑 (Xindian mining heritage trail) series —
same client/association as `JL Interview 0613` (V1–V3 delivered 2026-08-14).
One continuous ~88.5 min session across 3 source files: opening/mic check,
then two long-form interview segments with 尤月里老師 and others, covering
塗潭里 / 煤礦 / 獅仔頭山 / 戰俘營 history.

**Status:** inventory + transcription done. No cut yet — see `edit/project.md`
for the full session log and `docs/questions_for_professor.md` for open items.

This repo is the **decision layer** for the edit (cut choices, transcripts,
notes). The **raw footage and rendered video live in Google Drive**, not here
— see below for why and how to get them.

## Repo vs. Drive — what lives where

| | Git (this repo) | Google Drive |
|---|---|---|
| Contains | `edit/project.md`, `edit/takes_packed.md`, `edit/transcripts/*.json`, `edl.json` / `master.srt` (once they exist), `docs/*.md` | `raw footage/`, `BTS pics/`, `edit/clips_graded/`, previews, `final.mp4`, animation renders, `docs/*.pdf` |
| Why | Small text, diffable, mergeable — this is the actual editorial history | Large binaries — git can't diff/merge video and GitHub caps file size anyway |

Drive folder (raw footage + renders): **[JL Interview 0905 on Drive](https://drive.google.com/drive/folders/1wwfvlHXUNO4crt0ZVVjCH3QRvXbb3hyh?usp=drive_link)**

## Kyle's workflow (project owner)

Google Drive is already syncing this whole folder to your disk, exactly as
before — nothing changes there. Git rides on top, tracking only the small
text files.

1. **Before a session:** `git pull` — picks up anything your collaborator pushed.
2. **Edit as normal** (`video-use` through Claude Code, or by hand). Drive
   uploads footage/renders in the background automatically — no action needed.
3. **After a session:**
   ```bash
   git add edit
   git commit -m "short description of what changed"
   git push
   ```
   `git status` shows you exactly what's new — only tracked text files ever
   show up, since `.gitignore` silently excludes binaries.

## Collaborator's workflow (first-time setup)

1. **Accept the GitHub invite** Kyle sent you, then clone the repo:
   ```bash
   git clone https://github.com/Kowls0419/jl-interview-0905.git
   ```
   Pushing needs a [personal access token](https://github.com/settings/tokens)
   or an SSH key on your GitHub account — GitHub no longer accepts account
   passwords for git operations.

2. **Get the Drive folder** from the link above (ask Kyle for edit access if
   it's link-view-only) and make sure the **Google Drive Desktop app is
   actually syncing it to your disk** — viewing it in a browser tab is not
   enough, `video-use` reads and writes real local files.

3. **Line up the folder structure** so the repo and the Drive folder merge
   into one local directory:
   ```
   JL Interview 0905/
   ├── .git/                 ← from git clone
   ├── edit/                 ← merged: repo gives text files, Drive gives the rest
   ├── docs/                 ← client/admin docs (.md in git, .pdf from Drive)
   ├── raw footage/          ← from Drive only
   └── BTS pics/             ← from Drive only
   ```

   `edit/` is the **video-use skill's** namespace — only what the skill reads
   and writes belongs in it. Project admin goes in `docs/`.
   Easiest in practice: let Drive sync the folder to a local path first, then
   run `git init` + `git remote add origin <url>` + `git pull` inside it
   (rather than `git clone` into a location that doesn't exist yet).

4. **Install the tooling:** this project is edited with
   [video-use](https://github.com/browser-use/video-use), an open-source
   conversation-driven video editor by [Browser Use](https://github.com/browser-use),
   run as a Claude Code skill — needs `ffmpeg`/`ffprobe` on PATH and its Python
   deps installed if you're driving edits through Claude. Reviewing or cutting
   manually needs only the raw footage from Drive.

5. **Every session after that:** same three steps as Kyle's workflow above —
   `git pull` before, edit, `git add`/`commit`/`push` after.

## Claude-assisted workflow (recommended)

Both of you are driving this through Claude Code with the `video-use` skill,
so the smoothest path is two copy-pasteable prompts rather than typing git
commands by hand.

### One-time: install video-use + Dailies

If your peer doesn't have the skill yet, have them open Claude Code
(anywhere — this doesn't need to be inside the project folder) and paste:

> Install the video-use skill from https://github.com/browser-use/video-use —
> clone it to a stable local path, then follow its own `install.md` exactly
> (ffmpeg on PATH, ElevenLabs API key in `.env`, register the skill so
> `SKILL.md` is discoverable). Then also get
> https://github.com/Kowls0419/dailies — copy `dailies_server.py` and
> `dailies.html` from it into that video-use clone's `helpers/` directory
> (Dailies isn't part of the upstream video-use repo; it's a separate
> standalone tool that the skill's review step expects to find there).
> Verify by running one real command against a real file rather than just
> checking the files exist.

### Every session: startup prompt

Once installed, open Claude Code **inside this project folder** (make sure
Google Drive has finished syncing it locally first) and paste:

> This is a `video-use` project shared via git + Google Drive — read its
> `README.md` at the project root first for how that split works. Run
> `git pull` to sync the latest edit decisions, then read `edit/project.md`
> (full session log — pay attention to the most recent session) and
> `docs/questions_for_professor.md` for open items. Summarize where things
> left off in one or two sentences, then let's continue. At the end of this
> session, `git add`/`commit`/`push` whatever changed under `edit/` and
> `docs/`, and append a new session entry to `edit/project.md` per the skill's
> own memory format before we stop. Don't put anything in `edit/` that the
> video-use skill doesn't itself read or write.

This gets a new Claude session (yours or your peer's) fully oriented —
editorial history, open questions, *and* the collaboration mechanics — without
either of you re-explaining anything by hand each time.

### Dailies across two machines

[Dailies](https://github.com/Kowls0419/dailies) is the interactive review
tool used in step 8 of the `video-use` process: point it at a rendered
preview and it opens a browser page where you scrub the video, type
timestamped comments, and draw pen/arrow/box annotations directly on a
paused frame — much faster than describing "at 1:32 the caption is cropped"
in prose. It runs as a local server and opens a local browser tab — it's
per-machine, not a shared live session. If your peer runs a Dailies review, it
writes `edit/review/<stem>_rNN.json` (small text) and
`edit/review/frames/*.png` (the annotated screenshots) into his local copy of
this folder. The JSON reaches you via `git pull` once he commits/pushes; the
PNG frames reach you via Drive's normal sync (they're gitignored — too big/
numerous for git, but Drive doesn't care). So: reviews are asynchronous —
whoever runs Dailies should commit+push right after, so the round numbering
(`_r01`, `_r02`, …) stays consistent for whoever picks it up next.

## Cautions

- ⚠️ **Never both edit `edl.json` at the same time.** It's a JSON list of cut
  decisions — two concurrent hand-edits will conflict messily and git can't
  merge them cleanly. Say who's driving the cut before you start.
- ⚠️ **Drive must be a real desktop sync, not just browser access.** Viewing
  the folder on drive.google.com doesn't give `video-use` local files to work with.
- ⚠️ **Check `git status` before committing.** `.gitignore` already excludes
  raw footage and rendered video, but if it ever shows a huge binary file
  staged, stop and check the `.gitignore` rather than committing it.
- ⚠️ **GitHub needs a token or SSH key, not your account password**, for both
  push and (if prompted) pull.
