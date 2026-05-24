"""Shared path constants for pull scripts.

Centralizes where raw data lands so individual modules don't reinvent it.
"""
from __future__ import annotations
from pathlib import Path

# Repo root (this file is at src/pulls/_paths.py, so go up 3 levels)
REPO_ROOT = Path(__file__).resolve().parents[2]

DATA_ROOT = REPO_ROOT / "data"
RAW = DATA_ROOT / "raw"

SHOTS_DIR = RAW / "shots"
GAMES_DIR = RAW / "games"
PLAYERS_FILE = RAW / "players.parquet"
TEAMS_FILE = RAW / "teams.parquet"
KAGGLE_DIR = RAW / "kaggle"


def ensure_dirs() -> None:
    """Create all raw data subdirectories if they don't exist."""
    for d in (SHOTS_DIR, GAMES_DIR, KAGGLE_DIR):
        d.mkdir(parents=True, exist_ok=True)


# Default season range: 2013-14 (start of tracking-data era) through current.
# Update DEFAULT_END_SEASON each year as new seasons complete.
DEFAULT_START_SEASON = 2013
DEFAULT_END_SEASON = 2025  # represents the 2025-26 season


def season_str(start_year: int) -> str:
    """Format a season as 'YYYY-YY' (NBA convention).

    >>> season_str(2023)
    '2023-24'
    """
    return f"{start_year}-{str(start_year + 1)[-2:]}"


def all_seasons(start: int = DEFAULT_START_SEASON, end: int = DEFAULT_END_SEASON) -> list[str]:
    """Return list of season strings from start to end inclusive."""
    return [season_str(y) for y in range(start, end + 1)]
