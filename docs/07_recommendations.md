# Recommendations & Next Steps

**Rubric component:** Recommendations and Next Steps (25 points)
**Owner:** Cole (writing); team (content)
**Status:** Drafting

> Per the rubric: *What were your overall conclusions from this analysis? Were there different steps that you would have taken or different data that you would have used if you were to complete this analysis again?*

---

## Recommendations and Next Steps

Our overall conclusion is that shot context is predictive of whether a shot goes in, and that modeling it gives us a meaningful way to separate shot-making skill from shot selection. The shot-quality lens surfaces good findings that traditional box-score metrics miss: it identifies undervalued perimeter shooters who consistently make difficult shots, it shows that the league's strategic transformation over the past decade was driven by shot selection rather than across-the-board improvement, and it reorders player efficiency in a way that is systematic and interpretable rather than arbitrary. For a team or analyst, the practical recommendation is to treat shot-quality-adjusted scoring as one input in player evaluation alongside defense, rebounding, and playmaking, where it adds the most value by flagging contributors that raw efficiency overlooks.

The more interesting question is what we would do differently if we had six to twelve months to work on this instead of the two months we had. The short timeline shaped almost every major decision we made, and a longer horizon would change the project in a few specific ways.

The first and most important change would be the data. The single biggest constraint we faced is that the per-shot tracking features that make shot quality measurable — defender distance, shot clock, touch time, and dribbles — are only freely available for the 2014-15 season, which forced us to build the shot-quality model on a single year. With more time, the data itself becomes the project's first phase rather than a fixed starting point. We could reconstruct multi-season tracking data from the aggregated splits the NBA does publish, pursue academic or licensed access to the full tracking feed, or build a longer-running collection pipeline against the sources that do exist. Having those features across many seasons is what unlocks everything else: a model that is not tied to a single year, the ability to test whether our findings hold over time, and the chance to answer all three research questions on the same dataset rather than splitting between a single-season model and multi-season location data.

With multi-season tracking data in hand, the second change would be to the modeling. Two months was enough to build a solid gradient-boosted model and validate it, but it was not enough to pursue the richer spatial and sequential approaches from the literature: The expected-possession-value style models that treat a possession as it unfolds rather than scoring shots in isolation. Those methods require considerably more engineering and tuning time, and with a longer runway we would build toward them, along with proper cross-season validation and checks that a two-month project simply cannot fit.

The third change would be to broaden what the metric measures. The clearest limitation of our work, which we discuss in the ethical recommendations, is that a shot-quality model only captures shot-making and says nothing about the defense, rebounding, and playmaking that make up most of a player's value. With six to twelve months we would treat that as an objective rather than a caveat: Building a more complete player value framework that combines shot quality with the other dimensions of the game, and developing the role-aware or position-adjusted version of the metric that would let us compare players fairly against others who take similar shots. We would also validate our playing-style archetypes against an independent set of role labels to confirm they reflect real basketball roles. Each of these is a natural extension of what we have already built; what we lacked was not the idea but the time.
