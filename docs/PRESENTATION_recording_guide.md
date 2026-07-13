# NBA Shot Quality Capstone — Recording & Assembly Guide

**Deck:** `NBA Shot Quality Capstone - Presentation.pptx` (26 slides)
**Target:** one 20-minute video, recorded as **5 separate clips** and stitched in order.

Every slide has a **timed speaker script in its Notes** (open in PowerPoint → use **Presenter View**, or **View → Notes Page**, to read it while recording). The script is written to land each person on time at a normal speaking pace.

---

## Who records what

| Order | Clip | Presenter | Slides | Time |
|------|------|-----------|--------|------|
| 1 | **Opening** | **Cole Campbell** | 1 – 6 | ~3:00 |
| 2 | **Data & Engineering** | **Germain Meza** | 7 – 11 | ~5:00 |
| 3 | **EDA & Visualization** | **Calder Wyllie** | 12 – 16 | ~5:00 |
| 4 | **Methodology, Modeling & Results** | **Marc Rajesh** | 17 – 21 | ~5:00 |
| 5 | **Ethics, Recommendations & Conclusion** | **Cole Campbell** | 22 – 26 | ~2:00 |

**Total ≈ 20:00.** Cole records two short clips (opening + closing); everyone else records one.

> Each segment starts on a **dark navy divider slide** that names the presenter and time — that's your cue card for where your part begins and ends.

### Slide-by-slide ownership
- **Cole (open) — slides 1–6:** Title → Agenda → *Segment 1 divider* → Problem & the NBA → Research questions → Literature review.
- **Germain — slides 7–11:** *Segment 2 divider* → Data sources → Pipeline & scale → Data quality & the single-season constraint → Engineering challenges.
- **Calder — slides 12–16:** *Segment 3 divider* → What we explored → The three-point revolution (RQ2) → Efficiency held steady → Court-density takeaway.
- **Marc — slides 17–21:** *Segment 4 divider* → The model → RQ1 overperformers → RQ1 archetypes → RQ3 adjusted vs. traditional.
- **Cole (close) — slides 22–26:** *Segment 5 divider* → Ethics → Recommendations → Conclusion → Thank you.

---

## How to record your part

1. Open the deck in **PowerPoint** and start **Slide Show → Record** (or use Zoom/Teams/OBS — screen-share the slideshow with your webcam in a corner).
2. Read your **slide Notes** as the script. It's written to pace you to the target time — talk at a normal, unhurried pace and you'll land on time.
3. **Record only your slide range.** Start on your divider slide, stop after your last slide.
4. End each clip cleanly: pause ~1 second on your final slide before stopping (makes stitching seamless).
5. Export **1080p (1920×1080), MP4, 30 fps.**
6. Name your file: `NBA_Capstone_<order>_<name>.mp4`
   e.g. `NBA_Capstone_1_Cole_open.mp4`, `NBA_Capstone_2_Germain.mp4`, … `NBA_Capstone_5_Cole_close.mp4`.

### Handoff lines (already in the scripts, for smooth transitions)
- Cole → "…I'll hand off to Germain on the data."
- Germain → "…Calder will take you into what it actually shows."
- Calder → "…that sets up the modeling — Marc, over to you."
- Marc → "…Cole will close us out."

---

## Assembly (Cole + Claude)

1. Collect all five MP4s named as above.
2. Concatenate **in order 1 → 5** (Cole-open, Germain, Calder, Marc, Cole-close). Any editor works — CapCut, Clipchamp (built into Windows), DaVinci Resolve, or `ffmpeg`.
3. Optional polish: a half-second crossfade between clips; normalize audio levels so no one is louder than the rest.
4. Export final at 1080p MP4. Confirm total runtime is ~20:00.

**Quick ffmpeg concat** (same resolution/fps across clips):
```
# files.txt:
# file 'NBA_Capstone_1_Cole_open.mp4'
# file 'NBA_Capstone_2_Germain.mp4'
# file 'NBA_Capstone_3_Calder.mp4'
# file 'NBA_Capstone_4_Marc.mp4'
# file 'NBA_Capstone_5_Cole_close.mp4'
ffmpeg -f concat -safe 0 -i files.txt -c copy NBA_Capstone_Final.mp4
```
(If clips were exported with different settings, drop `-c copy` to re-encode.)

---

## Tips for a consistent feel
- Same intro framing for everyone: say your **name and role** once at the start of your segment (the scripts already do this).
- Quiet room, mic close, decent lighting. Look at the camera, not the slides.
- Keep webcam placement/size consistent across recorders if you're showing faces.
- Do one practice run against the on-screen timer before the real take.
