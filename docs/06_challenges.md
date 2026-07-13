# Challenges

**Rubric component:** Challenges (25 points)
**Owner:** Cole (writing); team (content)
**Status:** Drafting

> Per the rubric: *Describing any challenges that you faced when collecting the data or performing the statistical analysis. How might they be mitigated in a future analysis?*

---

## Challenges

We ran into challenges in three broad areas over the course of the project: Setting up and running the data pipeline, working with the data at scale, and building the model around the limits of what the data could tell us. None of them stopped the project, but each one shaped how we worked — and are worth describing — along with how we handled it, and how we would avoid it next time.

### Environment and tooling

Several of the early obstacles had nothing to do with basketball and everything to do with getting four people's machines to run the same code. The first was a Windows file-path limitation: The repository originally lived in a long directory path, and Windows' 260-character path limit caused failures when writing parquet files and installing dependencies. We solved it by moving the repository to a short path (`C:\nba`), which let the pipeline run correctly. The lesson for next time is simply to start the project in a short path on Windows rather than discovering the limit partway through.

A second tooling problem was conflicts between Python environments. The terminal would report that a package like 'pandas' was already installed, but importing it would still raise a `ModuleNotFoundError`; the result of a clash between a system-wide Anaconda installation and the project's virtual environment. We resolved it by standardizing on a dedicated `.venv` for everyone and installing dependencies through `python -m pip install -r requirements.txt`, which guarantees the right interpreter and package set. We also hit cross-platform differences: The gradient-boosted model depends on XGBoost, which would not load on a teammate's Mac because of a missing runtime library. Rather than ask everyone to fight their local setup, we saved the model's output tables as small CSV files in the repository and had the visualization code read those directly, so the charts can be regenerated on any machine without running the model at all. Standardizing the environment from day one, and decoupling the heavy modeling step from the lighter visualization step, are both things we would build in from the start next time.

### Working with the data at scale

The full enriched dataset contained roughly 2.9 million shot records spanning 13 NBA seasons. Storing the data as Parquet files kept processing efficient even at that size, so raw volume was never the real problem. The harder part was maintaining consistent schemas across seasons and making sure our joins preserved the correct number of observations. The game data needed particular care, because the NBA API stores games at the team-game level — each game appears twice, once from each team's perspective — so joining on game alone would have duplicated shots. We joined on game, team, and season together to attach each shot to the correct team, and we ran row-count checks before and after each merge to confirm the enrichment did not silently duplicate or drop observations. In a future analysis we would hardcode those row-count assertions directly into the pipeline as automated checks rather than running them by hand.

One thing that went better than expected is worth noting as well: The underlying data was clean and well organized, and we did not encounter major data-quality errors during exploration. The rows missing critical shot-location fields (`SHOT_DISTANCE`, `LOC_X`, `LOC_Y`) were a tiny fraction of the dataset and were removed with minimal impact; dates were also standardized to a datetime format for consistent handling across seasons. Because we did not have to spend the project fighting messy data, we could focus our limited time on the harder analytical questions.

### The single-season tracking constraint

The most consequential challenge was not a bug, but a limit in the data itself. The contextual features that make shot quality measurable — defender distance, touch time, dribbles, and shot clock — are only publicly available in the Kaggle 2014-15 shot logs. The multi-season NBA API data provides shot location and outcome for every season, but not those per-shot tracking details. This meant we could not build a single model that was both rich in shot-difficulty features, and broad across many seasons.

We handled it by combining the two sources deliberately, rather than forcing one to do everything: The detailed 2014-15 shot logs power the shot-quality model behind RQ1 and RQ3, where measuring the difficulty of individual shots is essential. The full 13-season dataset powers RQ2, which is about how shot selection and success changed over time, and only needs location and outcome. This let the project balance depth and breadth: Detailed context where it existed, long-term trends where it mattered. The single-season limitation is the first thing we would address with more time, by pursuing multi-season tracking data so the model is not tied to one year.

### Modeling around the data

A smaller but explicit modeling challenge was missing values in the shot-clock field of the Kaggle data. Dropping those rows would have risked pushing the sample below the project's 100,000-observation requirement, so we imputed the missing values instead, which kept the full sample of roughly 128,000 shots intact. A related, more persistent challenge was striking the right balance between engineered features and the clarity of the model. It would have been easy to keep adding derived features to chase a slightly better score, but every addition makes the model harder to explain, and for a question that is fundamentally about understanding player value, an interpretable model is worth more than a marginally more accurate one. We resolved it by keeping the feature set small and intuitive, and treating interpretability as a requirement rather than an afterthought.

We also investigated whether the model was systematically unfair to interior players, since big men who take easy shots near the rim tend to look worse once shot difficulty is accounted for. We tested a role-adjusted version of the metric that compares players within playing-style groups, and found that the role-level effect was small: The low rankings of those players reflected actual performance relative to their peers, rather than a bias in the metric. That investigation did not change the final results, but it gave us confidence in how to interpret them, and it's the kind of check we would expand into a full validation step in a longer project.
