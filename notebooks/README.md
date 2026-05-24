# Notebooks

All Jupyter analysis lives here, organized by project phase.

## Structure

| Subfolder | Purpose | Rubric component | Primary owner |
|---|---|---|---|
| `01_eda/` | Exploratory analysis of every variable used in modeling | #5 EDA | TBD |
| `02_modeling/` | Model development, tuning, evaluation | #6 Methodology, #8 Analysis | TBD |
| `03_analysis/` | Results, RQ-specific deep dives, final visualizations | #7 Data Viz, #8 Analysis | TBD |

## Naming convention

`NN_owner_topic.ipynb` where `NN` is a two-digit ordering number.

Examples:
- `01_germain_distance_distributions.ipynb`
- `02_germain_defender_proximity.ipynb`
- `01_cole_logistic_baseline.ipynb`

This keeps notebooks sorted by creation order and makes the owner obvious from the filename.

## Conventions

- Keep notebooks reproducible: clear outputs before committing if outputs are noisy or large.
- Import reusable functions from `src/` rather than copy-pasting between notebooks.
- A notebook should answer a specific question or build a specific artifact — don't let them sprawl into "everything I tried this week."
