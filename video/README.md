# Intro video — source, assets, and how to edit it

This folder holds everything needed to rebuild or edit the landing-page
intro video («شاهد كيف يعمل»). The published video itself is **not** here:
the site plays `exam-builder-intro-v2.mp4` from the **repo root**, with
`poster-v2.png` (also repo root) as its poster.

## Files

| Path | What it is |
|---|---|
| `build_video2.py` | The whole build: Pillow slides + phone-screenshot pan + narration, assembled with ffmpeg. |
| `shotsite-driver.js` | Browser driver used to capture the phone screenshots from the app. |
| `fonts/` | Bundled Noto Arabic fonts (binary, pushed via git) — the script needs no system fonts. |
| `logos/` | Chatbot logos for the "any chat model" scene (SVG sources + PNG renders). |
| `shots/` | Phone screenshots of the app, 390×844 PNGs, one per scene. `preview.png` is the print scene (a real baccalaureate biology exam in «معاينة الورقة»). |
| `work2/voice-*.mp3` | The narration audio, one file per scene, in scene order. |

## Rebuild

Needs Python 3 + Pillow, ffmpeg, and a narration backend (below):

```
cd video
python3 build_video2.py
```

**Narration is independent of Muse.** Existing `work2/voice-*.mp3`
files are reused as-is; delete them (or run `python3 build_video2.py
--regen`) to re-record. The backend is chosen with the `VIDEO_TTS`
environment variable:

- `edge` (default) — Microsoft Edge neural TTS, voice
  **ar-SY-AmiraNeural** (a real Syrian female voice). Needs internet
  and `pip install edge-tts`.
- `coqui` — fully local Coqui TTS (`pip install TTS`), Arabic Mai
  model `tts_models/ar/mai/glow-tts`; offline after a one-time model
  download. Example: `VIDEO_TTS=coqui python3 build_video2.py --regen`

The narration text in the script's `SCENES` array carries the agreed
harakat spellings, and both backends read them.

Output: `exam-builder-intro-v2.mp4` (and `poster-v2.png`) next to the script.
Copy both to the **repo root** and push — the landing player appears
automatically once the MP4 exists at the root (it is hidden until then).

> **All assets in this folder are version controlled in git**
> (screenshots, fonts, logos, narration MP3s). They reached GitHub via
> a normal `git push` from a server — Muse's in-app GitHub
> integration pushes text files only, so binary assets always travel
> this way. After cloning, this folder is complete and buildable.

## Building on your own PC

The build is **fully offline (0 bytes of internet)** as long as the
narration files in `work2/` are present — the script reuses them as-is.
You only need:

- Python 3 + Pillow (`pip install Pillow`)
- ffmpeg/ffprobe on your PATH (Windows: `winget install Gyan.FFmpeg`;
  Linux: `sudo apt install ffmpeg`)

```
git clone https://github.com/mohammedxmoussa/quiz-builder-syria.git
cd quiz-builder-syria/video
python3 build_video2.py
```

Expected output: `exam-builder-intro-v2.mp4`, **82 seconds, ~1.7 MB**,
identical to the published one — every input is the same file. Check
scene 2 (~0:04): it says «مُنْشِئُ الاختبارات» with a sakinah noon.
Caution: do not delete anything in `work2/` — re-recording narration
is the one step that needs Muse's TTS.

## Troubleshooting

- **The build tries to run a `tts` command and fails:** that means a
  narration file is missing from `work2/`. The script only calls TTS
  for missing files. Restore `work2/voice-*.mp3` (from the repo itself
  once the binary assets are pushed, or from `video-assets.zip`) and
  rebuild — with all 9 files present, TTS is never invoked.
- **`edge-tts` or `tts` command not found / TTS errors:** install the
  backend you selected (`pip install edge-tts`, or `pip install TTS`
  for Coqui). Note Coqui's `tts` and Edge's `edge-tts` are different
  programs; the script calls the right one for the chosen backend.

## Editing the video

- **Scenes, titles, narration:** the `SCENES` array at the top of
  `build_video2.py`. Each entry is
  `(kind, shot, pan_start, chip, title, subtitle, narration)`.
  Kinds: `phone` (screenshot in the bezel), `logos`, `books`.
- **On-screen text carries NO tashkeel** (cleaner slides). **Narration text
  SHOULD carry tashkeel** on ambiguous words — the TTS reads exactly what
  is written. Vocalizations agreed with the project owner:
  مُنْشِئُ — noon sakinah, and keep the final damma: without it the voice reads مُنَشِّء, تْكون, تَستخدمه, مُؤَتْمَتَة.
  And the phrasing «ورقة واحدة، على الوجهين» (not «وجه وقفا»).
- **Voice:** set by the narration backend (see Rebuild). Default is
  Edge's ar-SY-AmiraNeural. (History: the first local builds used a
  Muse catalog voice; the owner required full independence from
  Muse on 2026-11-26, so narration moved to Edge/Coqui. The harakat
  spellings above remain in force for any backend.)
- **Duration changes:** if a rebuild changes the total length, update the
  landing caption in `index.html` («شاهد كيف يعمل — دقيقة و21 ثانية»)
  to match.
- **New screenshots:** serve a copy of the app locally, inject
  `shotsite-driver.js` before `</body>`, and capture with Chrome headless
  at `--window-size=390,844 --device-scale-factor=1`, e.g.
  `?shot=preview` (shots: landing, json, editor, images, print, preview).
  Save over the files in `shots/` keeping the same names and size.
