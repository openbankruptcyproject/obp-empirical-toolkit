#!/usr/bin/env python3
"""Demo: classify synthetic AP dockets using the outcome classifier."""

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))

from classifiers.ap_outcome_classifier import classify_outcome

DEMO_DOCKETS = [
    {"name": "Quick procedural dismiss", "docket": {"dateFiled": "2024-01-01", "dateTerminated": "2024-01-30"}},
    {"name": "Settled at 6 months", "docket": {"dateFiled": "2024-01-01", "dateTerminated": "2024-07-01", "entry_count": 8}},
    {"name": "Litigated to judgment", "docket": {"dateFiled": "2022-01-01", "dateTerminated": "2024-03-01", "entry_count": 35}},
    {"name": "Active pending", "docket": {"dateFiled": "2025-06-01", "dateLastFiling": "2026-02-15"}},
    {"name": "Stale abandoned", "docket": {"dateFiled": "2022-03-01", "dateLastFiling": "2022-08-01"}},
]


if __name__ == "__main__":
    for case in DEMO_DOCKETS:
        outcome = classify_outcome(case["docket"])
        print(f"  {case['name']:35} -> {outcome}")
