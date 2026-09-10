# NBA Shot Quality Capstone

Modeling the probability that any NBA shot goes in, based on the context around it, and using that model to separate two things traditional stats conflate: **shot selection** and **shot-making skill**.

Built as the DAT 490 Data Science Capstone at Arizona State University by a four-person team: **Cole Campbell** (team lead), Calder Wyllie, Germain Meza, and Marc Rajesh.

## Headline findings

- **Shot-quality-adjusted player rankings differ substantially from traditional efficiency metrics.** The adjusted ranking correlates with raw FG% at just Spearman's ρ ≈ 0.39, and the reordering is systematic, not noise: it elevates perimeter shooters who consistently make hard shots (Pablo Prigioni climbs ~195 spots; Mo Williams +177) and lowers interior players whose high percentages come from easy shots at the rim (Omer Asik drops ~233; Andre Drummond −210).
- **The league's transformation was driven by shot selection, not better shooting.** Across the tracking era, mid-range attempts collapsed by about 17% of total shot share while three-point attempts rose, even though efficiency *within* each zone stayed largely stable.
- **Overperformance spans playstyles.** The players and teams that consistently beat their expected shot value are not one archetype; they split across on-ball creators, catch-and-shoot specialists, interior finishers, and mid-range scorers.

## The data

**2.9 million shot attempts** (2,912,157 rows): every NBA field goal attempt, regular season and playoffs, from the 2013-14 season through 2024-25, pulled from the NBA Stats API and enriched into a single shot-level table. Per-shot tracking features that make shot difficulty measurable (defender distance, shot clock, touch time, dribbles) come from the 2014-15 shot logs, the one season those features are freely available, and that season anchors the shot-quality model itself.

## How it works

A gradient-boosted tree model predicts the make probability of each shot from its context: court location, clock, defender pressure, shooter identity, and game state. The model reaches ~62% accuracy and ~0.64 ROC-AUC, comfortably above the no-information baseline, which is the point: shot outcomes are mostly variance, and the signal that *does* exist is what lets us price every shot's difficulty. A player's shots are then compared against what the model expected, and the gap between actual and expected makes is the shot-making skill estimate.

We call this metric **SMOKE**, Shots Made Over Known Expectation.

## Read the full work

- [Final Report (PDF)](docs/NBA%20Shot%20Quality%20Capstone%20-%20Final%20Report.pdf), the complete write-up: methodology, EDA, analysis, ethics, and recommendations
- [Presentation deck](docs/NBA%20Shot%20Quality%20Capstone%20-%20Presentation.pptx)
- `docs/` holds every section as markdown if you'd rather read it that way

## Repository layout

```
├── data/              # gitignored; rebuilt locally via the pull scripts in src/
├── docs/              # final report, presentation, and every written section
├── notebooks/         # EDA, modeling, and analysis notebooks
├── src/               # data pulls, cleaning, and model code
└── requirements.txt   # pinned dependencies
```

## Reproducing

The shot-level data is too large to commit, so it's rebuilt locally:

```bash
git clone https://github.com/cjcamp16/nba-shot-quality-capstone.git
cd nba-shot-quality-capstone
python -m venv .venv && source .venv/bin/activate   # .venv\Scripts\Activate.ps1 on Windows
pip install -r requirements.txt
```

Then see `data/README.md` and `src/` for the pull scripts. Once they've run, `data/` matches the state the analysis was built on.

## Status

The capstone is complete (Summer 2026). The work is continuing beyond the course: extending the model past a single tracking season and hardening the validation, with the goal of publication at a sports analytics conference.

## Erratum (September 2026)

A full audit of this pipeline during the follow-on research found two defects in the graded version, recorded here so the academic record is honest. The code and report at tag `v1.0-capstone` are left as submitted.

1. **Shooting team was misassigned on every home shot.** The Kaggle `MATCHUP` string always names the shooter's team first, but `extract_shooting_team` read it as "away @ home" and used the home/away flag to pick a side. Every home shot (half the data) was credited to the opponent, so the team-level table in the Analysis section (Los Angeles Clippers +78, Toronto +57, Minnesota +49) mixes each team's away shots with its opponents' home shots and should not be cited. Player-level results are unaffected by this bug.
2. **Two game-outcome columns were model features.** `FINAL_MARGIN` and `W` (the game's final margin and result) are not knowable when a shot is released and were removed in the follow-on work. Their presence raised the model's expectation for players on winning teams and slightly suppressed the shot-making credit of the best players on the best teams; the headline rank correlation between the adjusted ranking and raw FG% moves from 0.39 to 0.44 once they are removed.

The corrected pipeline, with cross-fitted expectations, the corrected team table, and a re-run validation battery, is the SMOKE research repository that continues this work.

## Sources

- **NBA Stats API** (via `nba_api`): shot-level data, 2013 to present
- **Kaggle: NBA Shot Logs 2014-15** (`dansbecker/nba-shot-logs`): per-shot tracking features
- **Kaggle: NBA Stats 1947-present** (`sumitrodatta/nba-aba-baa-stats`): long-horizon player history
