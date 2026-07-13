# Abstract / Executive Summary

**Rubric component:** Abstract / Executive Summary (25 points)
**Owner:** Cole
**Status:** Drafting

> Per the rubric: *High level summary of the purpose, data, and summary of your findings. This should include some information about the company that you have chosen as your dependent variable.*

---

## Abstract

This project models the quality of NBA shots — the probability that any given field goal attempt goes in based on the context around it — and uses that model to separate two things traditional statistics conflate: Shot selection and shot-making skill. The organization at the center of the work is the National Basketball Association, the premier professional basketball league in North America and the stakeholder our analysis is built for. The league office, its thirty franchises, and its broadcast partners all rely on player evaluation to make decisions about contracts, rosters, and how the game is presented, and a sharper understanding of shot quality speaks directly to that work.

Our data comes from the NBA's official statistics API, which provides shot-level detail for every field goal attempt from the 2013-14 season through the present — roughly two million shots — supplemented by a Kaggle dataset of 2014-15 shot logs that adds the per-shot tracking features (defender distance, shot clock, touch time, and dribbles) needed to model shot difficulty. We trained a gradient-boosted tree model on those features, reaching an accuracy of about 62 percent and a ROC-AUC of about 0.64, comfortably above the no-information baseline, which confirms that shot context is a relevant factor in predicting shot success.

We applied the model to three research questions. First, we found that the players and teams who consistently make more shots than expected span four distinct playstyles — on-ball creators, catch-and-shoot specialists, interior finishers, and mid-range scorers — rather than concentrating in any single type. Second, we found that the league's transformation over the tracking era was driven by shot selection rather than league-wide shooting improvement: Mid-range attempts collapsed by about 17% of total shot share while three-point attempts rose, even though efficiency within each zone stayed largely stable. Third, we found that a shot-quality-adjusted ranking of players differs substantially from traditional field goal percentage (Spearman's ρ of about 0.39), systematically elevating perimeter shooters who make difficult shots and lowering interior players who take easy ones. The overarching conclusion is that shot quality is a measurable and informative lens on player value — one that surfaces contributors that traditional metrics overlook — provided it is used as one input among many rather than one, complete verdict on a player.
