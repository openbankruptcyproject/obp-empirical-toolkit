#!/usr/bin/env python3
"""Heuristic classifier for bankruptcy AP outcomes from docket metadata.

Inputs are CourtListener-format docket dicts. Outputs an outcome label.

Usage:
    from classifiers.ap_outcome_classifier import classify_outcome
    label = classify_outcome(docket_dict)
"""

from datetime import datetime, timedelta


STALE_THRESHOLD_DAYS = 18 * 30  # 18 months


def parse_date(s):
    """Parse YYYY-MM-DD date string to datetime; None if invalid."""
    if not s:
        return None
    try:
        return datetime.strptime(s[:10], "%Y-%m-%d")
    except (ValueError, TypeError):
        return None


def classify_outcome(docket, today=None):
    """Classify a docket's outcome.

    Args:
        docket: dict with keys dateFiled, dateTerminated, dateLastFiling,
                docket_entries (list, optional, for entry count)
        today: optional datetime for testing; defaults to now.

    Returns:
        One of: pending, stale_abandoned, quick_dismiss, settled_or_dismissed,
        litigated
    """
    today = today or datetime.now()

    filed = parse_date(docket.get("dateFiled"))
    terminated = parse_date(docket.get("dateTerminated"))
    last_filing = parse_date(docket.get("dateLastFiling"))

    entry_count = docket.get("entry_count") or len(docket.get("docket_entries") or [])

    # Pending: no termination date
    if not terminated:
        if last_filing:
            days_since_last = (today - last_filing).days
            if days_since_last > STALE_THRESHOLD_DAYS:
                return "stale_abandoned"
            return "pending"
        return "pending"

    # Terminated: classify by duration + entry count
    if not filed:
        return "settled_or_dismissed"  # default if we can't calc duration

    duration_days = (terminated - filed).days

    if duration_days <= 60:
        return "quick_dismiss"
    if duration_days <= 365 and entry_count <= 10:
        return "settled_or_dismissed"
    if duration_days >= 365 or entry_count >= 20:
        return "litigated"
    return "settled_or_dismissed"


# Self-test
if __name__ == "__main__":
    test_cases = [
        ({"dateFiled": "2024-01-01", "dateTerminated": "2024-01-15"}, "quick_dismiss"),
        ({"dateFiled": "2024-01-01", "dateTerminated": "2024-06-01", "entry_count": 5}, "settled_or_dismissed"),
        ({"dateFiled": "2022-01-01", "dateTerminated": "2024-01-01", "entry_count": 30}, "litigated"),
        ({"dateFiled": "2024-01-01", "dateLastFiling": "2024-06-01"}, "pending"),
        ({"dateFiled": "2022-01-01", "dateLastFiling": "2022-03-01"}, "stale_abandoned"),
    ]
    for inp, expected in test_cases:
        got = classify_outcome(inp, today=datetime(2026, 4, 27))
        print(f"  {inp} -> {got} (expected {expected}) {'OK' if got == expected else 'FAIL'}")
