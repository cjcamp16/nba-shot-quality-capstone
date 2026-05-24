# Team

Where we keep track of who's doing what. Update this as we figure things out.

## Members

| Name | Role | Primary folders | Rubric components owned | Currently working on |
|---|---|---|---|---|
| Cole Campbell | TBD | TBD | TBD | — |
| Calder Wyllie | TBD | TBD | TBD | — |
| Germain Meza | TBD | TBD | TBD | — |
| Marc Rajesh | TBD | TBD | TBD | — |

## Possible role split (just an idea, not locked in)

We don't have to use these, but they line up with the natural pieces of the project:

- **Data Engineer** — owns `src/pulls/`, `src/clean/`, and the final enriched shot table. The rest of us can't really start until this is in place.
- **Modeling Lead** — owns `src/models/`, `notebooks/02_modeling/`, and the RQ1 writeup in `docs/`.
- **EDA / Viz Lead** — owns `notebooks/01_eda/`, court charts, and the RQ2 visualizations.
- **Lit Review / Ethics Lead** — owns `docs/02_literature_review.md`, `docs/05_ethics.md`, the RQ4 writeup, and `refs/`.

Whoever takes the Data Engineer role should start first since everything else depends on the shot table being there.

## How we work (let's confirm these as a team)

- All work happens on branches — nothing pushed straight to `main`.
- Someone else reviews each PR before it gets merged.
- If you `pip install` something, also update `requirements.txt` and commit it so the rest of us pick it up.
- Update the "Currently working on" column when you start something new so we all know where things stand.
