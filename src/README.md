# Source Code

Reusable Python modules that our notebooks and scripts import from. Anything that gets used in more than one place belongs here so we're not copy-pasting between notebooks.

## Structure

| Subfolder | What goes here | Primary owner |
|---|---|---|
| `pulls/` | Scripts that pull data from the NBA Stats API and Kaggle, cached in `data/raw/` | Germain |
| `clean/` | Cleaning, ID standardization, and schema work; produces `data/interim/` tables | Germain |
| `features/` | Feature engineering — shot context, player context, team context | Germain |
| `models/` | Reusable code for training, evaluating, and running the model | Marc |

## Conventions

- Plain `.py` files only — no notebooks in here.
- Each module should be importable on its own (no code that runs at import time).
- Put a docstring at the top of every file saying what it does.
- If you add a new module, add it to the table above so the rest of us know where to find it.
