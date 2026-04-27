#!/usr/bin/env python3
"""Example: pull dockets from CourtListener Search API matching a case-name pattern.

This is a sanitized example for educational use. CourtListener's Search API
is public and does not require auth for read access.

Usage:
    python courtlistener_search_pull.py <case_name_keyword>

Example:
    python courtlistener_search_pull.py "Department of Education"
"""

import json
import sys
import time
import urllib.parse
import urllib.request


CL_API = "https://www.courtlistener.com/api/rest/v4/search/"


def search_dockets(query, court_filter=None, max_pages=5):
    """Iterate Search API results matching `query`.

    Args:
        query: case-name keyword to search.
        court_filter: optional list of court IDs to restrict to.
        max_pages: how many result pages to walk.

    Yields docket dicts.
    """
    params = {"q": query, "type": "r"}  # type=r = dockets
    if court_filter:
        params["court"] = ",".join(court_filter)

    page = 1
    while page <= max_pages:
        params["page"] = str(page)
        url = f"{CL_API}?{urllib.parse.urlencode(params)}"
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                data = json.loads(r.read())
        except Exception as e:
            print(f"  page {page} failed: {e}", file=sys.stderr)
            break

        results = data.get("results", [])
        if not results:
            break
        for r in results:
            yield r
        if not data.get("next"):
            break
        page += 1
        time.sleep(1)  # be a good citizen


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    query = sys.argv[1]
    print(f"Searching CourtListener for: {query!r}")

    count = 0
    for docket in search_dockets(query):
        count += 1
        case_name = docket.get("caseName", "?")
        court = docket.get("court", "?")
        date_filed = docket.get("dateFiled", "?")
        cl_url = f"https://www.courtlistener.com{docket.get('absolute_url', '')}"
        print(f"  [{date_filed}] {court} | {case_name[:80]}")
        print(f"    {cl_url}")

    print(f"\nTotal: {count} dockets")


if __name__ == "__main__":
    main()
