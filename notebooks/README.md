# Notebooks

All our Jupyter work lives here, sorted by phase of the project.

## Structure

| Subfolder | What goes here | Rubric component | Primary owner |
|---|---|---|---|
| `01_eda/` | Exploring every variable we plan to use in the model | #5 EDA | Calder |
| `02_modeling/` | Building, tuning, and evaluating the model | #6 Methodology, #8 Analysis | Marc |
| `03_analysis/` | Final results, RQ-specific deep dives, and the visualizations that go in the report | #7 Data Viz, #8 Analysis | Calder (viz), Marc (analysis) |

## Naming convention

`NN_owner_topic.ipynb` where `NN` is a two-digit ordering number.

Examples:
- `01_germain_distance_distributions.ipynb`
- `02_germain_defender_proximity.ipynb`
- `01_cole_logistic_baseline.ipynb`

That way notebooks sort by creation order and you can tell at a glance who owns each one.

## Conventions

- Keep notebooks reproducible — clear noisy or huge outputs before committing.
- Pull reusable functions out of notebooks and into `src/` so we're not copying and pasting between files.
- One notebook should answer one specific question or build one specific artifact. Don't let them sprawl into "everything I tried this week."