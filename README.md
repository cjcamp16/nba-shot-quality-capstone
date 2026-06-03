# NBA Shot Quality Capstone

**DAT 490 Capstone Project**
**Team:** Cole Campbell, Calder Wyllie, Germain Meza, Marc Rajesh

We're modeling whether an NBA shot goes in based on the context around it — where it was taken, how much time was on the clock, how close the defender was, who took it, and how the game was going. Our data covers every field goal attempt from the 2013-14 season to the current season, which gives us roughly 2 million shots to work with.

## Research Questions

1. Which players and teams consistently outperform their expected shot value, and what distinguishes them?
2. How has shot success by court location changed across the 2013-present tracking era?
3. Does shot-quality-adjusted player ranking differ noticeably from traditional efficiency metrics (FG%, eFG%, TS%)?

## Project Structure

```
nba-shot-quality-capstone/
├── data/              # gitignored - pull locally with the API scripts
│   ├── raw/           # untouched API pulls + Kaggle files
│   ├── interim/       # cleaned, ID-mapped tables
│   └── processed/     # final enriched shot-level table
├── docs/              # all written deliverables for the report
├── notebooks/         # EDA, modeling, and analysis notebooks
├── refs/              # PDFs, notes, and other reference materials
├── src/               # reusable scripts (pulls, cleaning, model code)
├── .vscode/           # shared VS Code config
├── requirements.txt   # pinned Python dependencies
├── TEAM.md            # who owns what
└── README.md
```

## Setup (do this once per machine)

**Prerequisites:** Git, Python 3.14, VS Code, GitHub account with access to the repo.

### Step 1 — Clone the repo through VS Code

1. Open VS Code (no folder open).
2. `Ctrl+Shift+P` → type **"Git: Clone"** → Enter.
3. Paste the repo URL: `https://github.com/cjcamp16/nba-shot-quality-capstone.git`
4. Pick a parent folder (e.g., `E:\Projects\`).
5. Click **"Open"** in the popup once it finishes — VS Code reopens with the project loaded.

### Step 2 — Set up the environment in the integrated terminal

Open the terminal with `` Ctrl + ` `` (Ctrl + backtick). You're already in the project folder.

**Windows:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

**Mac / Linux:**

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

> **Heads up:** `python -m venv .venv` will sit silently for 30-60 seconds while it sets up pip. It's not frozen — let it finish.

### Step 3 — Install the recommended extensions

When VS Code pops up the **"This workspace has extension recommendations"** banner, click **Install**. (Or `Ctrl+Shift+X` → search "@recommended" → install Python and Jupyter.)

### Troubleshooting

If `Activate.ps1` fails with "execution of scripts is disabled," run this once in the terminal (Windows only):

```powershell
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned
```

Then re-run the activate command.

Depending on the name of your files and the pathway to them, you may encounter a issue with the length. Local Windows File Explorer has a 260-character limit. This may occur after running the installation command. If you already cloned the repo, you can move it into a shorter pathway.

### Move your existing folder
Close VS Code. Find your current project folder. Cut the whole folder. Paste it into "C:\". Rename it to something shorter, e.g. nba.

Open VS Code. Click File → Open Folder. Select  "C:\nba".

Open a new terminal and reactivate the virtual environment

From here, you need to re-run the code from above.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Daily Workflow

```bash
# Start of every session
git pull
pip install -r requirements.txt   # only matters if requirements.txt changed

# Work on a branch, never directly on main
git checkout -b yourname/short-description

# When you're done
git add <files>
git commit -m "Short summary of what you did"
git push -u origin yourname/short-description

# Then open a Pull Request on GitHub
```

## Adding a New Package

If you `pip install` something, also update `requirements.txt` so the rest of us get it:

```bash
pip install <package>
pip freeze > requirements.txt
git add requirements.txt
git commit -m "Add <package> for <reason>"
git push
```

## Data

The raw shot-level data isn't committed to git — it's way too big. Everyone pulls it locally instead. See `data/README.md` and `src/pulls/` for how to do that. Once you've run the pull script, your `data/raw/` will match everyone else's.

## Sources

- **NBA Stats API** (via `nba_api`) — primary source, shot-level data 2013-present
- **Kaggle: NBA Shot Logs 2014-15** (`dansbecker/nba-shot-logs`) — prototyping
- **Kaggle: NBA Stats 1947-present** (`sumitrodatta/nba-aba-baa-stats`) — long-horizon player history
