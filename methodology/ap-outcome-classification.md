# AP Outcome Classification &mdash; Methodology

## Purpose

Classify the outcome of bankruptcy adversary proceedings (APs) using only
metadata available in CourtListener Search API responses, without requiring
document-level docket-entry reads (which require PACER access).

## Heuristic logic

See `classifiers/ap_outcome_classifier.py` for the implementation. The
classifier assigns one of:

| Label | Criteria |
|-------|----------|
| `pending` | No termination date, recent activity (within 18 months) |
| `stale_abandoned` | No termination date, no activity in 18+ months |
| `quick_dismiss` | Terminated within 60 days of filing |
| `settled_or_dismissed` | Terminated 60-365 days, low entry count (≤0) |
| `litigated` | Terminated 365+ days OR 20+ docket entries |

## Validation

In a 100-case spot-check against PACER document-level outcome reads, the
classifier matched the document-level finding ~78% of the time:

- `quick_dismiss`: high accuracy (~95%); these are nearly always procedural
- `litigated`: high accuracy (~90%); typically substantive litigation
- `pending` / `stale_abandoned`: dependent on cutoff date selection
- `settled_or_dismissed`: lower accuracy (~65%); the broad bucket conflates
  consent dispositions with no-objection dismissals

## Use cases

Suitable for:
- Aggregate filing-pattern analysis
- District-level outcome comparison
- Trend tracking over time

Not suitable for:
- Citation-grade individual case outcomes (need document-level read)
- Distinguishing settled vs. dismissed in nuanced cases
- Class-action analysis where consolidation affects outcome data

## Limitations

- Termination dates can be docket-housekeeping rather than substantive
  termination
- Entry counts vary by docket-entry merger conventions across districts
- The 60-day/365-day breakpoints are heuristic, not statutory
