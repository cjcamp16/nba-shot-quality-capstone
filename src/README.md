# Source Code

Reusable Python modules that notebooks and scripts import from. Code that gets used in more than one place belongs here, not duplicated across notebooks.

## Structure

| Subfolder | Purpose | Primary owner |
|---|---|---|
| `pulls/` | API pull scripts (NBA Stats API via `nba_api`); cache raw data to `data/raw/` | TBD |
| `clean/` | Cleaning, ID standardization, schema enforcement; produces `data/interim/` tables | TBD |
| `features/` | Feature engineering (shot context, player context, team context) | TBD |
| `models/` | Reusable model training, evaluation, and prediction code | TBD |

## Conventions

- Pure-Python `.py` files — no notebooks here.
- Each module should be importable in isolation (no top-level side effects).
- Add a docstring at the top of each file explaining what it does.
- If you add a new module, add it to the table above.
