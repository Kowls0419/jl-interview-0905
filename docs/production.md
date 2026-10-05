# Production workflow

Kyle Yang is the sole editor and maintainer. 李承洋 is credited for
cinematography; there is no second-editor GitHub setup or handoff to maintain.

## People and working names

| Name in production notes | Role |
|---|---|
| Kyle / Kowls0419 | Project owner, editor, and sole Git contributor |
| 陳國超 / 陳總 / prof (LINE: jason chen 1526) | Client and association chair; also interviewed |
| Hoho | Kyle's mother; helps relay the client's messages |
| 游月裡老師 | Main interview participant |
| 張游寶彩 / 寶彩姐 | Interview participant and senior guide |
| 高燈立 | Interview participant |
| 李承洋 | Cinematography |

Transcript speaker IDs are specific to each source file. Check the file before
assigning an identity. The interview participant's signed name is 游月裡.

## Editorial record and media

- `edit/project.md`: chronological decisions, verification, and outstanding work.
- `edit/`: only files read or written by video-use, including build scripts,
  transcripts, EDLs, subtitles, and Dailies review JSON.
- `docs/questions_for_professor.md`: short questions only the client can answer.
- `lessons/video.md`: generalized rules to check before every render.
- Google Drive: original footage, photos, posters, generated graphics, review
  frames, and rendered media. Final share copies are in project-local `exports/`.
- `private/`: local working material, including YouTube metadata and the share
  message; excluded from Git.

Project media: [Google Drive folder](https://drive.google.com/drive/folders/1wwfvlHXUNO4crt0ZVVjCH3QRvXbb3hyh).
The Drive desktop app must have the media available locally before a build.
Do not add media, PDFs, posters, fonts, or `private/` to Git.

## Editing and review

1. Read `HANDOFF.md`, this guide, the latest project sessions, open client
   questions, and `lessons/video.md`.
2. Fetch and compare Git state before editing. When Kyle runs Claude and Codex
   together, assign each agent explicit files and record ownership in the local
   `HANDOFF.md`. Keep one owner for each EDL and render; shared intermediates
   mean different films should not render concurrently.
3. Use [Kyle's video-use fork](https://github.com/Kowls0419/video-use), branch
   `kyle`. Confirm its version before rendering; it provides Dailies and the
   per-range grading behavior used by these builds. Do not update render
   behavior partway through an accepted cut without checking the effect.
4. Build, render, and inspect the final composite against the editing lessons.
   Run Dailies locally, ingest every note and annotated frame, then iterate
   until Kyle accepts the round. Save review JSON and decision records.
5. Log work as `## Session N — YYYY-MM-DD — Kyle`, with Strategy, Decisions,
   Reasoning log, and the complete Outstanding list. Record agent work inside
   the entry; Kyle remains the editor and Git author.
6. Commit and push only when Kyle asks, using his Git identity. Check the staged
   file list and `git diff --cached --check`; exclude media and attribution
   trailers. Verify Drive sync separately for delivered MP4s.

## Learning from corrections

Before any render, read the lesson file. Only add a lesson when a correction
was preventable and likely to recur. State the general rule, check for an
existing entry first, and strengthen that entry where appropriate. Entry format:

```text
### Lnn — one-line title
- Context:    when the situation arises
- Symptom:    what the user or a check sees
- Root cause: why it happens
- Rule:       what to do to prevent it
- Scope:      relevant video and workflow tags
- Seen:       project / review round / date
```

## Publication naming

The combined collection is `塗潭社區產業、環境與歷史｜口述影像`. Its blue-group
titles are `產業篇｜塗潭社區社區產業演進` and
`土石流篇｜塗潭社區社區環境災害`; the repeated 社區 follows the client's
supplied wording. Their supervising organization is 文化部文資局. 焦炭窯篇 and
戰俘營篇 retain the approved 搶救塗潭焦炭窯 branding and 新北市政府文化局 credit.

When a client changes a name or credit, review every public appearance:
video graphics, YouTube titles and descriptions, playlist text, thumbnails,
README, and the share message. Verify the saved live pages against the client's
message. Do not treat an older upload draft as the source of truth.
