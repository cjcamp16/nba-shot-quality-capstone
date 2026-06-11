# Docs

All the written pieces of our capstone report live here. Each file lines up with one of the components in the official assignment spec (`dat490_assignment_spec.pdf`).

**Course:** DAT 490 — Summer 2026 Session A. 600 points total.
**Rough Draft due:** Sunday, June 21, 2026 at 11:59 PM
**Final Report due:** Friday, June 26, 2026 at 11:59 PM

## Rubric mapping

Cole writes every doc. The "Content from" column shows where the substance comes from when it isn't all on Cole.

### Separately submitted components (325 pts)

| File | Component | Points | Writer | Content from | Status |
|---|---|---|---|---|---|
| `00_introduction.md` + `00_introduction.pdf` | Introduction / Research Questions (covers both) | 25 | Cole | team | Submitted |
| `01_project_plan.md` + `01_project_plan.pdf` | Project Plan | 50 | Cole | team | Submitted |
| `02_literature_review.md` + `02_literature_review.pdf` | Literature Review | 50 | Cole | Cole | Submitted |
| `03_EDA.md` + `03_EDA.pdf` | Exploratory Data Analysis | 50 | Cole | Calder | Submitted |
| `04_methodology.md` + `04_methodology.pdf` | Methodology | 50 | Cole | Marc | Submitted |
| `03_methodology.md` | Methodology | 50 | Cole | Marc | Not Started |
| `04_analysis.md` | Analysis | 100 (Rough Draft) | Cole | Marc + Calder | Not Started |
| `05_ethics.md` + `05_ethics.pdf` | Ethical Recommendations & Implications | 50 | Cole | Cole | Submitted |
| `06_data_visualizations.md` + `06_data_visualizations.pdf` | Data Visualizations | 50 | Cole | Calder + Marc | Submitted |
| `06_challenges.md` | Challenges | 25 (Rough Draft) | Cole | team | Not Started |
| `07_recommendations.md` | Recommendations & Next Steps | 25 (Rough Draft) | Cole | team | Not Started |
| `08_abstract.md` | Abstract / Executive Summary | 25 (Rough Draft) | Cole | Cole | Not Started |
| `09_references.md` | References (APA) | 25 (Rough Draft) | Cole | team | Not Started |

### Need to add

| Component | Points |
|---|---|
| Exploratory Data Analysis (notebooks + writeup) | 50 |
| Data Visualizations (notebooks + writeup) | 50 |
| Final Report (incorporates all Rough Draft changes) | 75 |

### Note on the Research Questions assignment

The Introduction (`00_introduction.pdf`) is what we submitted for the Research Questions assignment. It covers both the database strategy and the three research questions, which together fulfill the 25-point requirement.

## Components handled elsewhere

| Component | Where it lives |
|---|---|
| Large dataset (100k+ obs) | `data/` (gitignored) + `src/pulls/` |
| Source Code (Appendix) | `src/` and `notebooks/` — goes in the Appendix of the final report PDF |
| EDA notebooks | `notebooks/01_eda/` |
| Data Visualizations | `notebooks/03_analysis/` |

## Research Questions

1. Which players and teams consistently outperform their expected shot value, and what distinguishes them?
2. How has shot success by court location changed across the 2013-present tracking era?
3. Does shot-quality-adjusted player ranking differ noticeably from traditional efficiency metrics (FG%, eFG%, TS%)?

## Conventions

- Markdown for everything in this folder by default.
- When a deliverable is finalized as a separate Word / PDF document (like `01_project_plan.pdf`), keep the matching `.md` file as a short pointer that links to it and tracks status.
- Keep filenames in their numbered order so they sort by rubric position.
- Write in full sentences — what's in here is going to end up in the final report.
- The authoritative source on requirements is `dat490_assignment_spec.pdf`. Check there before assuming.
