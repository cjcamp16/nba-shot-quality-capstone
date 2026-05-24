# Introduction

**Owner:** TBD
**Status:** Draft

## Database Strategy

We're modeling whether an NBA shot goes in based on the context around it — where it was taken, how much time was on the clock, how close the defender was, who took it, and how the game was going. Our data covers every field goal attempt from the 2013-14 season to the current season, which gives us roughly 2 million shots to work with. That's well past the 100,000-observation minimum, and the feature set easily clears the five-variable requirement.

Our primary source is the **NBA Stats API**, accessed through the open-source `nba_api` Python package. It provides shot-level detail for every attempt since 2013-14 — coordinates, shot zone, defender distance, shot clock, touch time, dribbles, and outcome — along with the matching game logs, player bios, and team data.

Two Kaggle datasets fill specific gaps. The **NBA Shot Logs 2014-15** dataset (`dansbecker/nba-shot-logs`) is a single-season, pre-cleaned file we'll use to prototype the pipeline while the full API pull runs in the background. The **NBA Stats 1947-present** dataset (`sumitrodatta/nba-aba-baa-stats`) gives us long-term player history, which we'll use to track individual player trajectories from before the tracking era.

This works because every source maps to NBA.com IDs through a lookup table, so all joins are ID-based rather than name-based, which is far more reliable. All three sources will be merged into one enriched table where each row is a single shot carrying its own context, the game's context, the shooter's context, and the team's context. That table will provide all the data we need for the project.

## Research Questions

1. What contextual factors best predict whether an NBA shot is made?
2. Which players and teams consistently outperform their expected shot value, and what distinguishes them?
3. How has shot success by court location changed across the 2013-present tracking era?
4. Does shot-quality-adjusted player ranking differ noticeably from traditional efficiency metrics (FG%, eFG%, TS%)?
