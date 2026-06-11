# Sources

Everything we're using for the lit review, methodology, and ethics sections. Every entry below is downloaded and sitting in this folder, ready to read.

## Foundational NBA analytics context

| File | Citation | Why it matters |
|---|---|---|
| `four_factors_revisited_2023.pdf` | Poropudas, J., & Halme, T. (2023). *Dean Oliver's Four Factors Revisited.* arXiv:2305.13032. | Revisits the seminal Oliver (2004) framework that anchors modern NBA analytics. Good field-overview piece that bridges classical metrics with modern statistical analysis. |

## Shot selection theory

| File | Citation | Why it matters |
|---|---|---|
| `skinner_2011_shot_selection.pdf` | Skinner, B. (2011). *The Problem of Shot Selection in Basketball.* arXiv:1107.5793. | Earlier theoretical framing of shot selection as an optimization problem. Good for the history paragraph of the lit review. |

## Expected possession value and shot quality modeling

| File | Citation | Why it matters |
|---|---|---|
| `cervone_2014_pointwise.pdf` | Cervone, D., D'Amour, A., Bornn, L., & Goldsberry, K. (2014). *POINTWISE: Predicting Points and Valuing Decisions in Real Time with NBA Optical Tracking Data.* MIT Sloan Sports Analytics Conference. | The seminal expected-possession-value paper. Anchors our methodology and lit review. |
| `cervone_2014_multiresolution.pdf` | Cervone, D., D'Amour, A., Bornn, L., & Goldsberry, K. (2014). *A Multiresolution Stochastic Process Model for Predicting Basketball Possession Outcomes.* arXiv:1408.0777. | Technical companion to POINTWISE. Goes deep on the modeling framework — useful when writing the methodology section. |

## Modern player evaluation through shot-quality lenses

| File | Citation | Why it matters |
|---|---|---|
| `expected_points_above_average_2024.pdf` | *Expected Points Above Average: A Novel NBA Player Metric Based on Bayesian Hierarchical Modeling* (2024). arXiv:2405.10453. | Modern follow-on work — directly relevant to RQ1 (residual analysis comparing actual vs. expected shot value by player). |
| `kono_fujii_2024_off_ball_scoring.pdf` | Kono, R., & Fujii, K. (2024). *Mathematical models for off-ball scoring prediction in basketball.* arXiv:2406.08749. | Predicts off-ball scoring opportunities using player tracking data on 630 NBA games from 2015–16. Adds depth on how player tracking can quantify possession-level value. |
| `rethinking_player_evaluation_2025.pdf` | *Rethinking Player Evaluation in Sports: Goals Above Expectation and Beyond* (2025). arXiv:2509.20083. | Statistical framework for residualized player evaluation metrics — directly parallels our RQ1 approach. Argues for valid frequentist inference around expected-above metrics. |

## Ethics framework

| File | Citation | Why it matters |
|---|---|---|
| `barocas_hardt_narayanan_fairmlbook.pdf` | Barocas, S., Hardt, M., & Narayanan, A. (2023). *Fairness and Machine Learning: Limitations and Opportunities.* MIT Press. | The standard reference for ML fairness. Supporting reference for the ethics section. Free under CC BY-NC-ND 4.0. |
| `thomas_uminsky_2020_problem_with_metrics.pdf` | Thomas, R. L., & Uminsky, D. (2020). *Reliance on Metrics is a Fundamental Challenge for AI.* arXiv:2002.08512. | Argues that overemphasizing a single metric in ML systems is fundamentally problematic and that a slate of metrics should be used instead. Core support for the ethics argument. |
| (book — not a committed file) | Muller, J. Z. (2018). *The Tyranny of Metrics.* Princeton University Press. | The canonical case that single quantitative measures replace judgment and get treated as the whole picture. Anchors the ethics argument. Not freely downloadable; cited from the published book. |

## Conventions

- Save PDFs here with the same naming style: `lastname_year_keyword.pdf` (or `topic_year.pdf` if multiple authors)
- When you cite something in `docs/`, also add the citation to `docs/09_references.md`
- Don't commit PDFs larger than ~20 MB — link to them here instead
- For domain books that aren't freely downloadable (e.g., *SprawlBall*, *Basketball on Paper*), buy or check out through ASU's library if anyone wants extra depth — they're not required for the lit review
