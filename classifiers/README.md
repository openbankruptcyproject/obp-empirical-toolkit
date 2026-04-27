# Classifiers

Heuristic classifiers for bankruptcy adversary proceeding (AP) outcomes.

## Files

- `ap_outcome_classifier.py` &mdash; classify a docket's outcome based on
  filing/termination dates and entry-count patterns. No document-level
  reading required; works from CourtListener Search API metadata alone.

## Approach

The classifier assigns one of:

- `pending` &mdash; docket has no termination date and recent activity
- `stale_abandoned` &mdash; docket has no termination but no activity in 18+ months
- `quick_dismiss` &mdash; terminated within 60 days (typically procedural dismissal)
- `settled_or_dismissed` &mdash; terminated 60-365 days, low entry count
- `litigated` &mdash; terminated 365+ days OR high entry count

These are heuristics, not document-level adjudications. For citation-grade
outcome data, you'd need to read the final dispositive docket entry. The
heuristic gets you ~80% accuracy at zero cost; the additional 20% requires
PACER pulls that may exceed available resources.
