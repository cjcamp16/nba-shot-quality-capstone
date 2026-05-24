# NBA Shot Quality Capstone

**DAT 490 Capstone Project**
**Team:** Cole Campbell, Calder Wyllie, Germain Meza, Marc Rajesh

Modeling the probability that an NBA shot is made based on pre-shot context (location, defender distance, shot clock, shooter, game state) using shot-level data from 2013-14 to the present.

## Research Questions

1. What contextual factors best predict whether an NBA shot is made?
2. Which players and teams consistently outperform their expected shot value, and what distinguishes them?
3. How has shot success by court location changed across the 2013-present tracking era?
4. Does shot-quality-adjusted player ranking differ noticeably from traditional efficiency metrics (FG%, eFG%, TS%)?

## Project Structure

```
nba-shot-quality-capstone/
├── data/              # gitignored - pull locally via the API script
│   ├── raw/           # untouched API pulls + Kaggle files
│   ├── interim/       # cleaned, ID-mapped tables
│   └── processed/     # final enriched shot-level table
├── notebooks/         # EDA, modeling, and analysis notebooks
├── src/               # reusable scripts (pulls, cleaning, model code)
├── .vscode/           # shared VS Code config
├── requirements.txt   # pinned Python dependencies
└── README.md
```

## Setup (do this once)

**Prerequisites:** Git, Python 3.14, VS Code, GitHub account with repo access.

### Windows

```powershell
# One-time per machine - allow PowerShell to run the venv activate script
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned

# Clone and set up
git clone https://github.com/cjcamp16/nba-shot-quality-capstone.git
cd nba-shot-quality-capstone
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Mac / Linux

```bash
git clone https://github.com/cjcamp16/nba-shot-quality-capstone.git
cd nba-shot-quality-capstone
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

Then open the folder in VS Code. When prompted, install the recommended extensions (Python, Jupyter).

> **Note:** `python -m venv .venv` will pause for 30-60 seconds on `ensurepip`. Don't Ctrl+C — let it finish.

## Daily Workflow

```bash
# At the start of every session
git pull
pip install -r requirements.txt   # only matters if requirements.txt changed

# Work on a branch, never directly on main
git checkout -b yourname/short-description

# When done
git add <files>
git commit -m "Short summary of what you did"
git push -u origin yourname/short-description

# Then open a Pull Request on GitHub
```

## Adding a New Package

If you `pip install` something, also update `requirements.txt` so teammates get it:

```bash
pip install <package>
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Add <package> for <reason>"
git push
```

## Data

The raw shot-level data is **not** committed to git (too large). Each teammate runs the API pull script locally — see `src/pulls/` once the script is added. Output lands in `data/raw/` and is gitignored.

## Sources

- **NBA Stats API** (via `nba_api`) — primary source, shot-level data 2013-present
- **Kaggle: NBA Shot Logs 2014-15** — prototyping
- **Kaggle: NBA Games Database (Nathan Lauga)** — backup for game-level context
- **Kaggle: NBA Stats 1950-present** — long-horizon player history
