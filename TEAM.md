# Team

Single source of truth for who owns what. Update as roles get assigned.

## Members

| Name | Role | Primary folders | Rubric components owned | Currently working on |
|---|---|---|---|---|
| Cole Campbell | TBD | TBD | TBD | — |
| Calder Wyllie | TBD | TBD | TBD | — |
| Germain Meza | TBD | TBD | TBD | — |
| Marc Rajesh | TBD | TBD | TBD | — |

## Suggested role split (for discussion)

We don't have to use these, but they map cleanly to the project's natural divisions:

- **Data Engineer** — owns `src/pulls/`, `src/clean/`, the canonical enriched shot table. Unblocks everyone else.
- **Modeling Lead** — owns `src/models/`, `notebooks/02_modeling/`, RQ1 writeup in `docs/`.
- **EDA / Viz Lead** — owns `notebooks/01_eda/`, court charts, RQ2 visualizations.
- **Lit Review / Ethics Lead** — owns `docs/02_literature_review.md`, `docs/05_ethics.md`, RQ4 writeup, `refs/`.

Whoever takes the Data Engineer role should start first — everyone else's work depends on the shot table existing.

## Working norms (to confirm as a team)

- All work happens on branches; nothing pushed directly to `main`.
- One teammate reviews each PR before merge.
- If you `pip install` something, update `requirements.txt` and commit it.
- Update the "Currently working on" column above when you start something new.
