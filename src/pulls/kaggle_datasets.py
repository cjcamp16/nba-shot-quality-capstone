"""Download the three supporting Kaggle datasets.

Prerequisites:
1. `pip install kaggle` (already in requirements.txt)
2. A Kaggle API token at ~/.kaggle/kaggle.json (Windows: %USERPROFILE%\\.kaggle\\kaggle.json)
   Get yours: kaggle.com -> account settings -> "Create New API Token"

Each dataset lands in its own subfolder under data/raw/kaggle/.
Idempotent: skips datasets that already have files extracted.

If a dataset slug below is wrong (Kaggle URLs occasionally change),
update the SLUG in the constant for that dataset and re-run.
"""
from __future__ import annotations
from pathlib import Path

from src.pulls._paths import KAGGLE_DIR, ensure_dirs

# Dataset slugs (the "owner/dataset" part of the Kaggle URL).
# If any of these fail with 404, look up the current slug at kaggle.com.
SHOT_LOGS_SLUG = "dansbecker/nba-shot-logs"
GAMES_DB_SLUG = "nathanlauga/nba-games"
HISTORICAL_STATS_SLUG = "drgilermo/nba-players-stats"

DATASETS = {
    "shot_logs_2014_15": SHOT_LOGS_SLUG,
    "games_database": GAMES_DB_SLUG,
    "historical_stats": HISTORICAL_STATS_SLUG,
}


def _has_extracted_files(dest: Path) -> bool:
    """True if the directory exists and contains at least one non-hidden file."""
    if not dest.exists():
        return False
    return any(p.is_file() and not p.name.startswith(".") for p in dest.iterdir())


def download_dataset(slug: str, dest: Path) -> None:
    """Download and unzip one Kaggle dataset into `dest`."""
    # Import here so the module can be imported without kaggle creds present
    # (e.g. for help/inspection); credentials are only required at download time.
    from kaggle import api as kaggle_api  # type: ignore

    dest.mkdir(parents=True, exist_ok=True)
    print(f"  Downloading {slug} -> {dest}")
    kaggle_api.dataset_download_files(slug, path=str(dest), unzip=True, quiet=False)


def main() -> None:
    ensure_dirs()
    for name, slug in DATASETS.items():
        dest = KAGGLE_DIR / name
        if _has_extracted_files(dest):
            print(f"Skip {name} (already extracted at {dest})")
            continue
        try:
            download_dataset(slug, dest)
            print(f"  Done: {name}")
        except Exception as exc:
            print(f"  FAILED: {name} ({slug}) -> {exc}")
            print(f"    If this is a 404, verify the slug at kaggle.com and update kaggle_datasets.py")


if __name__ == "__main__":
    main()
