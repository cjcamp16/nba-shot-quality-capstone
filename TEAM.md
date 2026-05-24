# Team

Where we keep track of who's doing what.

## Members

| Name | Role | Primary folders | Rubric components owned | Currently working on |
|---|---|---|---|---|
| Cole Campbell | Lit Review, Ethics, & Doc Lead | `docs/`, `refs/` | #4 Lit Review, #9 Ethics, plus the writing for every doc | — |
| Calder Wyllie | EDA / Viz Lead | `notebooks/01_eda/`, `notebooks/03_analysis/` | #5 EDA, #7 Data Visualizations | — |
| Germain Meza | Data Engineer | `src/pulls/`, `src/clean/`, `src/features/` | #1 Large dataset (the data pipeline) | — |
| Marc Rajesh | Modeling Lead | `src/models/`, `notebooks/02_modeling/` | #6 Methodology, #8 Analysis (content) | — |

## How the writing works

Cole writes up every doc in `docs/`, but the content comes from whoever owns that area:

- **Methodology and Analysis** content comes from Marc, written up by Cole
- **EDA results and visualizations** come from Calder, written up by Cole
- **Data pipeline details** (sources, joins, schema) come from Germain, written up by Cole
- **Lit Review and Ethics** are Cole's own areas — he handles content and writing

That keeps the report consistent in voice without making one person also do everyone else's analysis.

## How we work

- All work happens on branches — nothing pushed straight to `main`.
- Someone else reviews each PR before it gets merged.
- If you `pip install` something, also update `requirements.txt` and commit it so the rest of us pick it up.
- Update the "Currently working on" column when you start something new so we all know where things stand.

## Where to start

Germain's data pulls unblock everyone else, so that's the natural first step. Once `data/raw/` is populated, Calder can start EDA, Marc can prototype the model, and Cole can get the project plan and lit review going in parallel.
