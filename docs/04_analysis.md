# Analysis

**Rubric component:** Analysis (100 points)
**Owner:** Cole (writing); Marc + Calder (content)
**Status:** Drafting

> Per the rubric: *Analysis and results of each step, what decisions you made to proceed to the next step and why.*

---

## Analysis

This section walks through the results for each research question, the decisions we made at each step, and the reasoning behind them. The work rests on a single shot-success model: For every field goal attempt, the model estimates the probability the shot goes in based on its context, and the gap between what a player or team actually made and what the model expected is what drives the rest of the analysis. We built that model first, confirmed it was learning correctly, and then used it to answer each question in turn.

### Building and validating the shot-success model

Our first step was to train a model that predicts whether a single shot is made, using the 2014-15 Kaggle shot logs, since that is the only season for which per-shot tracking features (defender distance, shot clock, touch time, and dribbles) are publicly available. We started with logistic regression as a baseline because it's interpretable and gives us a floor that any more complex model has to clearly beat to be worth the added complexity. The baseline returned an accuracy of about 0.613 and a ROC-AUC of about 0.635 on a held-out test set. More importantly, the coefficients made basketball sense: Shot distance had the strongest negative effect on make probability, and defender distance had the strongest positive effect. Farther shots are harder, and more space helps; exactly what we would expect, which gave us confidence the model was learning correctly rather than noisey.

We then moved to a gradient-boosted tree model (XGBoost), because shot success is not a simple linear function of its inputs: The value of an extra foot of space depends on the distance, which depends on the shot clock, and so on. The boosted model captures those interactions without us specifying them in advance. It improved on the baseline on both measures, reaching about 0.619 accuracy and a 0.644 ROC-AUC. Both models comfortably clear the no-information baseline of 54.8 percent (the accuracy of always guessing the more common outcome, a miss), confirming that shot context carries predictive power. Because the boosted model was the stronger of the two, we used it to generate the expected-make probabilities that feed every result below.

One decision worth noting: The shot-clock field had missing values in the Kaggle data. Rather than drop those rows, which would have pushed the sample below the project's 100,000-observation floor, we imputed the missing values. This kept the full sample of roughly 128,000 shots intact.

Several of our modeling decisions were really choices about what *not* to do, and they are worth making explicit. We deliberately used the 2014-15 Kaggle shot logs rather than the much larger enriched multi-season table, because the enriched table lacks the shot-difficulty features the model needs; a bigger but less informative dataset would have produced a weaker model. We chose to impute the missing shot-clock values rather than discard those rows, because the loss in sample size was not worth the marginally cleaner data. And we kept the feature set deliberately simple — a handful of interpretable derived features such as shot-distance and touch-time buckets and a late-shot-clock flag — rather than pushing into heavier feature engineering. A model whose inputs we can explain is more useful for a question that is ultimately about understanding player value than a marginally more accurate but opaque model would be.

### RQ1 — Which players and teams consistently outperform their expected shot value, and what distinguishes them?

With the model trained, we scored every shot and computed residuals — actual makes minus model-expected makes — aggregated to the player and team level. A consistently positive residual means a player made more shots than the model expected, given the difficulty of the shots they took: The cleanest way we have to separate shot-making skill from shot selection.

It's worth being explicit about why this individual player analysis uses only the 2014-15 season. Measuring shot quality requires knowing how hard each individual shot was, which depends on the per-shot tracking features: Defender distance, shot clock, touch time, and dribbles. Those features are only publicly available for 2014-15; for every other season, the NBA releases shot location and outcome, but not the per-shot tracking detail. Without that detail, the model cannot estimate how makeable a given shot was, so it cannot tell whether a player beat expectations. We therefore evaluate individual players on 2014-15, the one season where the data lets us answer the question properly, and we treat the player and team figures below as specific to that season rather than as timeless judgments. (RQ2, which is about shot location over time rather than individual evaluation, uses all thirteen seasons because location and outcome are available for every year.)

The top individual overperformers in 2014-15 were a mix of elite shooters and skilled scorers:

| Player | Makes above expected | Per-shot edge |
|---|---|---|
| Chris Paul | +51.0 | +5.8% |
| Kyle Korver | +45.6 | +9.5% |
| Nikola Vučević | +39.7 | +4.4% |
| Stephen Curry | +38.5 | +4.0% |
| Dirk Nowitzki | +34.1 | +4.2% |

Kyle Korver stands out: on nearly 500 shots he converted at a rate about 9.5 percentage points higher than the model expected, which is an enormous edge over that volume. At the team level, the Los Angeles Clippers led at roughly 78 makes above expectation, well ahead of Toronto (+57) and Minnesota (+49), consistent with a roster built around efficient shot creation and finishing.

Identifying *who* overperforms is only half the question. To answer *what distinguishes them*, we clustered the 129 overperforming players using K-means on their shot-selection features: Average shot distance, defender distance, touch time, dribbles, and three-point rate. The clustering produced four clean and interpretable archetypes:

| Archetype | Players | Example players |
|---|---|---|
| On-Ball Creators | 37 | Chris Paul, Stephen Curry, Kyrie Irving |
| Catch-and-Shoot Specialists | 36 | Kyle Korver, Klay Thompson, Wesley Matthews |
| Interior Finishers | 29 | Anthony Davis, DeAndre Jordan, Nikola Vučević |
| Mid-Range Scorers | 27 | Dirk Nowitzki, Chris Bosh, Carmelo Anthony |

We chose clustering on shot-selection features rather than relying on listed positions because the question is about *how* a player creates their value, not their nominal position, and the features capture that directly: High dribbles and touch time mark on-ball creators, low touch time and a high three-point rate mark catch-and-shoot specialists, and short average distance marks interior finishers. The archetypes line up with what anyone who follows the league would expect, which is a good sign the grouping is meaningful. The takeaway for RQ1 is that overperformance is not concentrated in one type of player; it shows up across distinct roles, and the model rewards each for doing their specific job well.

### RQ2 — How has shot success by court location changed across the 2013-present tracking era?

RQ2 is a descriptive question about change over time, so here we used the full thirteen seasons of location data from the NBA Stats API rather than the single-season modeling sample. We made that decision deliberately: The tracking features that power the model only exist for 2014-15, but shot location and outcome are available for every season, and the question is fundamentally about the geography of shooting across the era.

The headline result is a meaningful shift in *where* teams shoot. Comparing the first and last seasons of the era by zone:

| Zone | Attempt share 2013-14 | Attempt share 2025-26 | Change |
|---|---|---|---|
| Mid-Range | 26.8% | 10.1% | **−16.7** |
| Above the Break 3 | 19.2% | 30.7% | **+11.5** |
| In the Paint (non-RA) | 14.9% | 20.0% | +5.1 |
| Restricted Area | 32.3% | 28.4% | −3.9 |
| Corner 3 (combined) | 6.7% | 10.7% | +4.0 |

The mid-range collapsed by nearly 17 percentage points of total shot share, by far the largest move, while above-the-break threes rose by about 11 points. This is the well-documented "three-point revolution," and our data shows it cleanly.

What is more interesting is that field goal percentage by zone changed far less than attempt share did. The relative ranking of zones by efficiency stayed about stable across the entire window; the restricted area was always the most efficient zone, the corners always reliable, above-the-break threes always the lowest-percentage shot. One subtle pattern is worth drawing out here: Even as three-point attempts surged, three-point shooting percentage ticked down slightly in every three-point zone, by roughly half a percentage point. That decline is best explained not by players getting worse at shooting, but by the rise in volume itself. As more of the offense moved behind the arc, threes were taken by a wider range of players and from more difficult situations, which pulled the league-wide average down even though the shot itself did not become harder to make. The one zone that improved is the restricted area, where shooting rose by about 6 percentage points (from roughly 61 percent to 67 percent), meaning players are finishing at the rim more effectively than they did a decade ago. The conclusion for RQ2 is that the era's transformation was about shot *selection*, not a league-wide improvement in shooting: Teams moved their attempts toward the most efficient zones rather than getting better everywhere at once.

### RQ3 — Does shot-quality-adjusted player ranking differ noticeably from traditional efficiency metrics?

For RQ3 we built a shot-quality-adjusted metric from the model — each player's actual field goal percentage minus their model-expected field goal percentage — and compared the ranking it produces against rankings by traditional field goal percentage and effective field goal percentage. To measure how different the rankings are, we used Spearman rank correlation, which is the standard way to quantify whether two orderings of the same set agree.

The correlations were moderate, not high:

| Comparison | Spearman's ρ |
|---|---|
| Shot-quality-adjusted vs FG% | 0.387 |
| Shot-quality-adjusted vs eFG% | 0.592 |

A correlation of 0.387 against raw field goal percentage is well below 1.0, which tells us directly that the adjusted ranking tells a meaningfully different story than the metric most casual fans would reach for. The correlation against eFG% is higher (0.592) because eFG% already credits three-pointers, partially capturing shot difficulty, but it still leaves a large gap.

The most revealing view is which players move the most between the two rankings. The pattern sorts cleanly by player type. The biggest risers are perimeter shooters whose raw percentages look ordinary but who consistently make contested shots the model did not expect to fall: Pablo Prigioni climbs about 195 spots, with Mo Williams (+177), Jose Calderon (+176), and Channing Frye (+174) close behind. The biggest fallers are interior players whose high raw percentages come from easy shots near the rim: Omer Asik drops about 233 spots, with Andre Drummond (−210) and Tony Allen (−199) nearby. This is the metric working exactly as designed: it rewards making hard shots and gives little credit for making easy ones. The answer to RQ3 is yes, the adjusted ranking differs substantially from traditional efficiency, and the difference is systematic rather than random; it consistently re-values players according to the difficulty of the shots they take.

### Summary of findings

Taken together, the analysis shows that shot context is meaningfully predictive of shot success, that the players and teams who beat the model span distinct and identifiable playing-style archetypes, that the league's decade-long transformation was driven by shot selection rather than league-wide shooting improvement, and that a shot-quality-adjusted view of efficiency reorders players in a meaningful, type-driven way that traditional metrics miss.
