# 🎬 Video lessons — Kyle

Video editing — cuts, overlays, transitions, audio render, burned subtitles.
Generalized mistakes and the rule that prevents each. **Read this file and
`video-jl.md` before any render**, whoever is driving (video-use step 0).

**Who writes here:** Kyle's sessions only. JL's sessions add to `video-jl.md`.
IDs here (`L01…`) come from Kyle's global `reflect` sequence, which skips
numbers used in his other ledgers — gaps are expected. Next free ID: see
"Next free ID" in Kyle's `reflect/lessons.md`. Some entries cite `L09`/`L28`,
which live in Kyle's private ledger; the rule each entry states is self-contained.

Moved here from Kyle's `reflect/lessons/video.md` on 2026-09-27 so JL's Claude
can read it; **this is now the only copy.** Entry format is in `README.md`
("Lessons").

---

### L01 — loudnorm bleeds/pumps audio into silent gaps
- Context:    any render with silent stretches (card gaps, B-roll, montage holds)
- Symptom:    faint audio swell or a half-second "repeat"/"cut sound" inside gaps
- Root cause: `loudnorm` normalizes across the whole track, lifting the noise floor
              (and tail of the previous segment) up into what should be silence
- Rule:       render previews with `--no-loudnorm`; the platform re-normalizes on
              upload (YouTube does). If loudness matters, use a fixed, non-bleeding
              gain step, never a single-pass loudnorm over the concatenated master.
- Scope:      video, audio-render
- Seen:       JL heritage R7 (2026-07-10) — MOV region -91 dB no-loudnorm vs -18.5 dB with

### L02 — framed overlay touching a card causes a 1-frame flash
- Context:    a framed (non-full-bleed) photo/Ken-Burns overlay adjacent to a card
- Symptom:    a millisecond flash of speaker footage between the pic and the card
- Root cause: the overlay's baked fade lands over the ~1-frame footage the concat
              exposes at the card boundary (24fps rounding drift, ~0.15s)
- Rule:       a **framed** overlay must have ≥1s footage BEFORE and AFTER it — never
              touching a card on entry or exit. Short/mostly-pic moments should be a
              COVER (full-bleed blur-bg), not framed.
- Scope:      video, overlay-transitions
- Seen:       JL heritage R8 (2026-07-10)

### L03 — cover→card handoff reverts to footage (drift flash)
- Context:    a full-bleed cover (blur-bg) photo handing directly into a card
- Symptom:    the cover fades out and reveals footage for ~1 frame before the card
- Root cause: accumulated 24fps frame-rounding drift (~0.14s) between the overlay's
              nominal start and the concatenated base timeline
- Rule:       end a cover ≥~1s PAST the card's start (extend its opaque tail into the
              card) so its fade-out happens well inside the card, drift-proof. Cover
              may go card→cover directly; framed may not (L02).
- Scope:      video, overlay-transitions
- Seen:       JL heritage R9 (2026-07-10)

### L04 — `・` (katakana middle dot) renders as a box in many CJK fonts
- Context:    titles / subtitle text using `・` as a separator (e.g. Songti TC)
- Symptom:    a tofu box glyph on the card
- Rule:       never use `・` in on-screen text. Use `與`, `／`, `今日的…`, or a plain
              space. Verify any separator glyph actually exists in the chosen font.
- Scope:      video, zh-subtitle, zh-output
- Seen:       JL heritage — recurred across sessions until banned
- Seen:       JL heritage playlist thumbnail (2026-08-14) — recurred AGAIN, in a
              generated JPEG rather than a subtitle, because the ban lived in my head
              as "don't use it in subtitles". It is a FONT-COVERAGE rule, not a
              subtitle rule: it applies to every glyph drawn with PIL/ImageFont in any
              artefact. Cheap guard now used: render each character and assert
              `font.getmask(ch).size[0] != 0` before shipping the image.

### L05 — homophone/OCR class subtitle errors (e.g. 平→坪)
- Context:    ASR + s2twp conversion of domain terms (area 坪, proper nouns, places)
- Symptom:    wrong-but-valid character: 兩千平 for 兩千坪; mis-heard names
- Root cause: ASR hears a homophone; conversion is faithful to the wrong char
- Rule:       keep a per-project SUB_FIXES map of authoritative spellings (measure
              words like 坪, and proper nouns from the source-of-truth doc) and apply
              it after OpenCC. Re-check domain terms on every subtitle pass.
- Scope:      video, zh-subtitle
- Seen:       JL heritage R6 (V1 @1:49, 平→坪)

### L08 — gaze-driven cover: cover the frame when the speaker looks away / is intruded on
- Context:    interview footage where framing degrades (speaker looks off-camera, or
              a second person enters frame)
- Symptom:    weak/awkward framing on screen during otherwise-good audio
- Rule:       looking at camera → keep footage; looking away or interviewer-in-frame
              → cover that stretch with a full-bleed blur-bg photo rather than a
              global crop.
- Scope:      video, overlay-transitions
- Seen:       JL heritage — gaze pass (Session 9)

### L34 — a timeline-wide filter also hits SYNTHETIC sources, and temporal ones smear anything animated
- Context:    an EDL/project-level `grade` (or any global `-vf`) applied per segment,
              where some segments are generated cards, slates, or title graphics
              rather than camera footage.
- Symptom:    generated cards look subtly wrong in a way that is invisible while they
              are static. Here: `tmix=frames=3/5` (anti-flicker for fluorescent
              banding) temporally averaged the animated end-card, ghosting its
              shrink-to-left morph into illegibility — proportional to `frames=N`, so
              the video with `frames=5` was worst and the one with `grade=""` was clean.
- Root cause: the filter is specified once for the *timeline* but is a property of the
              *source*. Anti-flicker, denoise, deband, tmix all exist to fix camera
              artefacts that synthetic sources cannot have. It hid for months because
              averaging N identical frames of a STATIC card is a no-op — the bug only
              appears once a card animates.
- Rule:       synthetic sources opt OUT of source-repair filters. Give the renderer a
              per-range override (`"grade": ""`) and set it on every card range.
              Colour/look grades can stay global; temporal and spatial *repair*
              filters must not be. When adding motion to a previously static generated
              element, re-check every global filter it now passes through.
- Scope:      video, code
- Seen:       JL heritage (2026-08-14). Kyle asked whether the morph was "the same
              style" in all three videos. Geometry WAS identical to the pixel; the
              rendered look was not. Caught only by sampling all three at the same
              offset relative to their closer start and comparing — a single-video
              check would have shown nothing wrong.

### L35 — `afade=out` then `afade=in` on one chain silences everything after the first fade
- Context:    building a gate/duck in ffmpeg by chaining fade filters to bring audio
              down for a middle section and back up afterwards.
- Symptom:    the section you wanted to keep is silent too. Measured -91 dB where the
              audio was supposed to return.
- Root cause: `afade=t=out` holds gain at 0 for the whole remainder of the stream, and
              the following `afade=t=in` multiplies that 0 by its ramp. Fades are
              multiplicative envelopes over the whole timeline, not local events.
- Rule:       for anything shaped more complex than a single in/out, compute ONE gain
              envelope — a single `volume=eval=frame` expression, or (better for many
              regions) build the envelope in numpy with raised-cosine ramps and apply
              it to the samples. `volume=enable=` is not a substitute: it switches
              hard and clicks. Always MEASURE the level in each region afterwards; an
              option that silently does nothing looks identical to one that works.
- Scope:      video, audio
- Seen:       JL heritage music demos (2026-08-14). The "bookend" option — music only
              over the opening and closer — shipped as a demo with no music anywhere.
              Only caught by rendering music-only stems and measuring per section.

### L36 — when compositing into a sub-region, centre on the SUB-REGION and assert the fit
- Context:    programmatic layout (PIL/canvas/SVG) that places text or images into a
              panel, column, cell or margin of a larger frame.
- Symptom:    silently truncated text — `光陰的故事` printed as `光陰`. Or, once content
              grows, elements overlapping: a credits block printed on top of a caption.
- Root cause: two habits. (a) reusing a `centre_on_frame()` helper and then cropping
              the sub-region out of it, so anything wider than the panel is cut with no
              error. (b) mixing a top half that FLOWS from a running `y` with a bottom
              half pinned to `height - margin` — fine until something in the middle
              grows, then they meet.
- Rule:       centre relative to the container you are actually drawing into, not the
              page. Let the whole layout flow from one cursor rather than anchoring
              some parts to the far edge. End every generated page with an assertion
              that content ended before the bottom margin, so overflow fails the build
              instead of shipping. Size type to the container and verify, rather than
              assuming it fits.
              **Assert on the INK, not on the cursor.** `if y + MARGIN > H: fail` tests
              where the layout code THINKS it stopped. Glyphs descend below the
              baseline, a pasted image can exceed its nominal box, and a row height
              computed before the content is measured is a guess. Find the last
              non-background row in the rendered bitmap and assert THAT clears the
              margin.
- Scope:      video, code, print
- Seen:       JL heritage (2026-08-14) — hit TWICE in one session: thumbnail panel text
              cropped to two characters, then A4 poster credits colliding with the QR
              caption after a still and blurb were added between them.
- Seen:       JL heritage poster 4 (2026-08-18, parallel session) — the cursor-based
              overflow assert PASSED while credit ink sat 17px (~1.4mm) off the frame,
              too tight to print; caught only by measuring ink rows directly. Same day,
              both of my sheet generators shipped with that same weak assert, and one
              then failed for real (`content overflows the canvas 4329 > 4311`) because
              the row height I precomputed disagreed with what the rows actually
              consumed. The guess was wrong, not the drawing.
- Seen:       JL Interview 0905 產業篇 (2026-09-28), self-eval — framed photo covers ran
              down behind the burned subtitle box. The container was "the frame", but the
              real one is "the frame above the subtitle band"; now asserted in code.

### L40 — a text fix that runs downstream of a transform can be silently dead
- Context:    any find/replace map applied AFTER a normalizing step — OpenCC
              conversion, case folding, unicode NFC/NFKC, whitespace collapsing,
              a formatter, an autocorrect pass.
- Symptom:    the fix appears to be in place, is listed in the code, is never
              questioned — and does nothing. `"近水游" → "逆水游"` sat in V1's
              SUB_FIXES for months and shipped a wrong subtitle the whole time,
              because OpenCC `s2twp` rewrote 游→遊 *before* the replace ran, so the
              key could never match the text.
- Root cause: the map was written against the string as heard/read (the ASR output),
              but runs against the string as transformed. A `str.replace` that
              matches nothing returns the input unchanged and raises nothing — the
              failure is indistinguishable from success. Same shape as L09: a probe
              that can never fire looks exactly like good news.
- Rule:       **count the hits.** Any replacement map gets a per-key fire counter and
              prints the keys that never matched. Warn, never assert — an entry can
              legitimately be zero once an earlier entry has already fixed the text
              (order matters in an ordered dict), so a hard assert would break honest
              builds. Write the map against a sample of the string *as it arrives at
              the replace*, not as it left the upstream tool. And when adding a fix
              for a character the transform is known to touch, put it first so the
              downstream entries see the corrected form.
- Also:       s2twp does not only fail to fix errors (L05) — it **introduces** them.
              It converted every swimming 游 to the travel-sense 遊 across a whole
              interview. Conversion output is not authoritative for domain words;
              spot-check the converted text against the raw ASR, not just the ASR
              against the audio.
- Scope:      video, zh-subtitle, code
- Seen:       JL heritage (2026-08-18). Kyle asked for 遊→游; applying it revived the
              dormant 近水游 entry, which is how the dead fix was found at all. Guard
              now in all three build scripts — its first run flagged 4 more no-op
              entries across the three maps (all benign, superseded by earlier keys).

### L41 — bitrate is not a quality measurement; CRF output is supposed to be small
- Context:    judging whether a delivered encode is "too compressed", usually by
              comparing its bitrate to the camera source's.
- Symptom:    told Kyle his 1080p exports at 2.4-3.3 Mbps were "roughly 1/10th the
              source bitrate" and proposed a ~2-hour re-render of three videos at a
              lower CRF. Measured afterwards: CRF20-fast→CRF20-medium scored
              **SSIM 0.98463** against a lossless reference of the same filter chain;
              CRF14-slow→CRF16-slow scored **0.98594**. +0.0013 for 2.6x the file
              size — invisible, and the two-generation loss I blamed was never there.
- Root cause: comparing a **quality-targeted** encode (CRF) against a **fixed-rate**
              capture codec. A camera writes 30-60 Mbps regardless of content; x264 at
              CRF 20 writes whatever that content costs. A static talking head on flat
              walls — doubly so with `tmix` smoothing it — is genuinely cheap. Low
              bitrate was evidence the content was easy, not that quality was lost.
- Rule:       never infer encode quality from bitrate, and never from a ratio to the
              source. **Measure**: encode the same filter chain losslessly as a
              reference, run the candidate chains against it with `ssim`/`psnr`, and
              compare the deltas. It costs one short segment and a few minutes. Do it
              BEFORE proposing a re-render, because "re-export everything" is an
              expensive recommendation to be wrong about. If the delta is invisible,
              say so and drop the idea — see L28.
- Also:       when the real target is a platform's own re-encode (YouTube's 1080p tier
              vs its 1440p+ tier), the lever is the upload resolution, not our CRF.
              That one cannot be measured locally — present it as a claim, not a
              finding, and say which is which.
- Scope:      video, encoding, diagnostics
- Seen:       JL heritage (2026-08-18). Caught only because I'd offered Kyle a
              before/after A/B and then actually ran it instead of shipping the
              recommendation.

### L45 — libass's subtitle box pads from font metrics, not ink — CJK fonts come out lopsided
- Context:    burned subtitles on a solid/translucent box (`BorderStyle=3`), especially
              with CJK fonts such as Noto Sans TC.
- Symptom:    every cue has visibly more padding below the text than above it
              (Dailies: "subtitles top/down margin different", all frames).
- Root cause: libass sizes the box from the font's ascent/descent, and CJK fonts
              reserve far more descent than their glyphs use. Separately, libass
              `Fontsize` is the LINE height (ascent+descent), not the em size PIL/CSS
              use — the same number renders ~1.45× smaller in libass.
- Rule:       don't use `BorderStyle=3` for boxed subs. Write an `.ass` with two
              events per cue: an exact rectangle (`{\pos(x,y)\p1}m 0 0 l w 0 w h 0 h`)
              and the text `\an5`-centred on it, offset so the INK band (measured
              with PIL, e.g. over 國說嗎關) is centred rather than the metric line
              box. Set ASS `Fontsize = ascent+descent` from PIL's `getmetrics()` at
              the intended px size. Then MEASURE padding on the rendered output for
              every cue (inside the box, text is the only bright ink).
- Scope:      video, zh-subtitle
- Seen:       JL Interview 0905 戰俘營篇, Dailies r01 (2026-09-27), Kyle

### L46 — a timed overlay clip can pass every check on its own and still mistime in the composite
- Context:    replacing a subtitle burn with a transparent overlay video (or
              per-cue stills) fed through a generic overlay/compositing pass.
- Symptom:    the overlay file matches the SRT frame-by-frame and by `-ss` time,
              yet the composited video shows a cue from seconds later, drifting
              further through the video — or, with single-frame PNG stills, shows
              no subtitles at all. The concat demuxer also added one frame per
              image entry (+88 frames over 42 cues).
- Root cause: not fully isolated — sync between a long alpha clip (qtrle / PNG-in-
              MOV) or one-frame inputs and the main stream inside the overlay chain.
              Checking the overlay in isolation proved nothing about the composite.
- Rule:       for burned subtitles, use libass (its timing was exact) and solve
              styling inside the `.ass` (L45) rather than switching delivery
              mechanism. Whatever the mechanism, verify ON THE FINAL RENDER, by
              time, at several cues spread across the whole video (start, middle,
              end) against the SRT — never only on an intermediate file.
- Scope:      video, zh-subtitle, diagnostics
- Seen:       JL Interview 0905 戰俘營篇 r01→r02 (2026-09-27), Kyle — three
              render rounds lost before reverting to libass

### L47 — stream-copy concat mixes colour ranges: generated cards after full-range footage render darker
- Context:    camera footage that is full range (`yuvj420p`, `color_range=pc` — common on
              Canon and phones) joined by `-c copy` concat with generated cards/slates
              encoded from PNG (limited range, untagged).
- Symptom:    every card AFTER the first footage segment is dimmer than an identical card
              before it — paper 236 → 219, a clean `0.86·x + 16` (a second full→limited
              squeeze). Easy to miss: each card looks fine on its own.
- Root cause: an untagged segment inherits the previous segment's "pc" flag in the
              joined stream, so the final encode converts data that is already limited.
- Rule:       normalize every segment to ONE range and tag it explicitly at extraction
              (`scale=out_range=tv` at the end of the chain + `-color_range tv`). Check:
              the same card PNG must measure identical at every position in the output.
              Sample the decoded Y plane directly for this check; converting a pixel
              to grayscale RGB changes a limited-range value such as Y=216 to 233.
- Scope:      video, audio-render, cards
- Seen:       JL Interview 0905 (2026-09-28), found while checking Kyle's r01 frame of the
              closing card — already present in the accepted 戰俘營篇 r02.
- Seen:       JL Interview 0905 four-film export (2026-10-03), self-eval — corrected
              a grayscale-RGB measurement before accepting the final card check.

### L48 — per-segment AAC + stream-copy concat: the voice drifts behind the picture
- Context:    render pipelines that encode each cut to its own MP4 with AAC audio and then
              join them with the concat demuxer and `-c copy`.
- Symptom:    lip sync worsens toward the end — ~17 ms per segment; 0.35 s after 22 cuts.
              ffprobe's stream durations look fine, so a duration check passes.
- Root cause: each AAC encode starts with ~1024 priming samples that only the container's
              edit list hides; stream copy keeps them all, so the decoded audio is longer
              than its timestamps say.
- Rule:       copy the video but re-encode the audio once at the join
              (`-af aresample=async=1:first_pts=0 -c:a aac`). Verify sync on the FINAL file
              with a known marker in both streams — e.g. where a card's digital silence
              starts vs where its first frame appears — never from stream durations.
- Scope:      video, audio-render, diagnostics
- Seen:       JL Interview 0905 (2026-09-28), found in self-eval — also in 戰俘營篇 r02
              (~0.13 s over 8 cuts).

### L49 — an ASR word boundary is not a safe cut point; check the waveform
- Context:    choosing in/out points from Scribe word timestamps, especially at a
              speaker handoff or inside a fast phrase (「對對對。所以你說」).
- Symptom:    a crackle/distortion at the head of a segment, or a sliver of the next
              word at its tail — Kyle caught both in one review (r01 #1, #4).
- Root cause: the timestamps drifted ~200 ms — past the 30–200 ms padding window.
              「對對對」 was stamped as ending at 1166.10 but still sounded at 1166.30.
- Rule:       after picking an edge from the transcript, read the 10 ms RMS envelope
              around it and put the cut in a real dip (≤ −30 dB). If there is none within
              the padding window, move the cut to the nearest one and adjust the phrase —
              don't trust the stamp. When a splice lands inside continuous speech, flag it
              for listening in Dailies.
- Scope:      video, cut, audio-render
- Seen:       JL Interview 0905 產業篇 r01 (2026-09-28), Kyle

### L50 — compute the timeline from real segment lengths, never nominal EDL lengths or shared intermediates
- Context:    placing subtitles and overlays on the output timeline of a multi-segment
              render (render.py re-times each segment to whole frames).
- Symptom:    subtitles/covers drift early by the end (0.32 s over 21 segments). A first
              "fix" that measured last render's clips silently fell back to nominal after
              another video's render overwrote the same `clips_preview/seg_NN` files.
- Root cause: footage segments round UP to whole frames (video outlasts audio); card
              video rounds down but its audio keeps the exact length; concat advances by
              the longer stream. Intermediates in `edit/` are shared by every video.
- Rule:       derive each segment's length deterministically (footage
              `ceil(d·fps)/fps`, cards `d`) and build every offset from that. Never read
              base/clip intermediates to verify or time one video — another render may
              have replaced them; verify on that video's final output only.
- Scope:      video, zh-subtitle, overlay-transitions, code
- Seen:       JL Interview 0905 產業篇 (2026-09-28), self-eval

### L51 — Ken Burns stepping: whole-pixel resize + paste per frame
- Context:    a slow push/pan on a still (PIL, per-frame), especially long and gentle ones.
- Symptom:    the motion looks laggy, with visible steps (Kyle, r01 #3, all covers).
- Root cause: resizing to `round(w·k)` and pasting at integer x/y changes the picture
              one whole pixel at a time; at 5 % over 10 s most frames don't move.
- Rule:       pre-scale once (Lanczos) to the largest size the move reaches, then place
              each frame with a sub-pixel affine transform (`Image.transform(AFFINE,
              BICUBIC)`), so the photo only ever downsamples slightly. Keep eased ends.
- Scope:      video, overlay-transitions, animation
- Seen:       JL Interview 0905 產業篇 r01 (2026-09-28), Kyle
