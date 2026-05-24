# Data

**Nothing in this folder gets committed to git** (other than this README and a couple of placeholder files). All the data files are pulled locally so the repo stays small and every teammate works from the same raw inputs.

## Layout

```
data/
├── raw/                   # untouched API pulls + Kaggle files
│   ├── shots/             # shots_{SEASON}.parquet, one per season
│   ├── games/             # games_{SEASON}.parquet, one per season
│   ├── players.parquet    # all NBA players (historical + current)
│   ├── teams.parquet      # all NBA teams (static)
│   └── kaggle/            # the two supporting Kaggle datasets
│       ├── shot_logs_2014_15/   # dansbecker/nba-shot-logs (for prototyping)
│       └── historical_stats/    # sumitrodatta/nba-aba-baa-stats (1947-present)
├── interim/               # cleaned, ID-standardized tables (populated by src/clean/)
└── processed/             # final enriched shot-level table (populated by src/build/)
```

## How to fill it

### Step 1 — Kaggle credentials (one-time per machine)

The Kaggle pull needs an API token. Everyone sets up their own — these never go in git.

1. Go to https://www.kaggle.com/settings -> scroll to **API** -> click **Create New API Token**. A `kaggle.json` file downloads.
2. Move it to the right folder:
   - **Windows:** `%USERPROFILE%\.kaggle\kaggle.json` (create the `.kaggle` folder if it isn't there yet)
   - **Mac/Linux:** `~/.kaggle/kaggle.json`, then `chmod 600 ~/.kaggle/kaggle.json`

### Step 2 — Run all the pulls

From the project root, with the venv activated:

```bash
python -m src.pulls.fetch_all
```

This runs every pull in order (teams -> players -> games -> shots -> Kaggle). The whole thing takes about **10-15 minutes** on a fresh machine, with the shot pull eating most of that. Output lands in `data/raw/`.

### Or run them one at a time

```bash
python -m src.pulls.nba_teams           # static metadata, instant
python -m src.pulls.nba_players         # 1 API call
python -m src.pulls.nba_games           # ~30 sec per season
python -m src.pulls.nba_shots           # ~30-40 sec per season (slowest one)
python -m src.pulls.kaggle_datasets     # needs Kaggle creds
```

## Why it's gitignored

The full enriched shot table is going to be millions of rows / hundreds of MB — way past GitHub's per-file (100 MB) and per-repo (~1 GB) limits. The pulls are idempotent and cached, so each teammate runs `fetch_all` once and they're done.

## Default season range

Right now the scripts pull **2013-14 through 2025-26** — the full tracking-data era. If we want to change that, edit `DEFAULT_START_SEASON` / `DEFAULT_END_SEASON` in `src/pulls/_paths.py`.

## If a Kaggle download fails with 404

Kaggle dataset slugs change sometimes. If that happens, look up the current slug at kaggle.com and update the constant for that dataset in `src/pulls/kaggle_datasets.py`.
