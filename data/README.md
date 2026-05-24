# Data

**Nothing in this folder is committed to git** (except this README and the subfolder placeholders). Data files are pulled locally from the NBA Stats API — see `src/pulls/` once the pull script is added.

## Layout

```
data/
├── raw/         # untouched API pulls + Kaggle files as downloaded
├── interim/     # cleaned, ID-standardized intermediate tables
└── processed/   # final enriched shot-level table used for modeling
```

## How to populate

1. Make sure your environment is set up (see project root `README.md`).
2. Run the pull script (once it exists):
   ```
   python -m src.pulls.fetch_shots
   ```
3. Files land in `data/raw/` and downstream cleaning scripts produce `data/interim/` and `data/processed/`.

## Why it's gitignored

The full enriched shot table is multi-million rows / hundreds of MB — far past GitHub's per-file and per-repo limits. Everyone pulls locally; the pull script lives in git so the data is reproducible.
