# etl-cleanup-plan

Planning repository for the **ETL cleanup rollout** — the cleanup of our flaky nightly ingestion pipeline.

## Work packages

| # | Work package | Estimate |
| --- | --- | --- |
| 1 | Audit ingestion scripts | 3 person-days |
| 2 | Rewrite validation layer | 5 person-days |
| 3 | Add integration tests | 8 person-days |
| 4 | Write the runbook | 2 person-days |

## Effort summary

| Figure | Person-days |
| --- | --- |
| Base total | 18.0 |
| Contingency (15%) | 2.7 |
| **Grand total** | **20.7** |

These figures are produced by `effort_calc.py` (pandas-based, rerunnable), which computes the base total of the four estimates, a 15% contingency, and the grand total, each rounded to one decimal place.

All four work packages are tracked as sub-issues of the parent issue [**ETL cleanup rollout**](../../issues/1).
