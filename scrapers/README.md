# Scrapers

Sanitized example scrapers for public bankruptcy-data sources. None of these
contain credentials; you must provide your own (PACER login, etc.) to use them.

## Files

- `courtlistener_search_pull.py` &mdash; example pull from CourtListener's
  public Search API by case-name pattern. No authentication required for
  Search API.
- `pacer_docket_pull.py` &mdash; structural example of a PACER docket pull.
  Requires PACER credentials (which we don't ship here). The docket-text
  parsing logic is the reusable part.

## Rate limiting

The CourtListener Search API allows reasonable use without authentication
but rate-limits aggressive scrapers. Be a good citizen: cache, sleep
between requests, prefer batch endpoints where available.

For PACER: query consciously. Fees are real and add up. Use RECAP/CourtListener
first when possible.
