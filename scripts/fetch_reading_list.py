#!/usr/bin/env python3
"""Fetch the reading list from Raindrop.io into data/reading.json.

Pulls every bookmark carrying the publish tag (default "blog") across all
collections and keeps only the fields the /reading/ page shows.

Never fails the build: on any error (missing token, network, bad response)
it prints a GitHub Actions warning, leaves no data file, and exits 0. The
reading page then shows its "temporarily unavailable" notice.

Env:
  RAINDROP_TOKEN  Raindrop test token (required)
  RAINDROP_TAG    tag that publishes a bookmark (default: blog)
"""

import json
import os
import sys
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://api.raindrop.io/rest/v1/raindrops/0"  # 0 = all collections
PER_PAGE = 50  # API maximum
OUTPUT = Path(__file__).resolve().parent.parent / "data" / "reading.json"


def fetch_page(token, tag, page):
    query = urllib.parse.urlencode({
        "search": f"#{tag}",
        "sort": "-created",
        "perpage": PER_PAGE,
        "page": page,
    })
    request = urllib.request.Request(
        f"{API}?{query}",
        headers={"Authorization": f"Bearer {token}"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def fetch_all(token, tag):
    bookmarks = []
    page = 0
    while True:
        body = fetch_page(token, tag, page)
        if not body.get("result"):
            raise RuntimeError(f"Raindrop returned an error: {body.get('errorMessage', body)}")
        items = body.get("items", [])
        bookmarks.extend(
            {
                "title": item.get("title") or item.get("link"),
                "link": item.get("link"),
                "domain": item.get("domain", ""),
                "created": item.get("created", ""),
                "note": (item.get("note") or "").strip(),
            }
            for item in items
        )
        if len(items) < PER_PAGE:
            return bookmarks
        page += 1


def main():
    token = os.environ.get("RAINDROP_TOKEN", "").strip()
    tag = os.environ.get("RAINDROP_TAG", "blog").strip()
    if not token:
        print("::warning::RAINDROP_TOKEN is not set, the reading list will be empty")
        return 0
    try:
        bookmarks = fetch_all(token, tag)
    except Exception as error:  # never block publishing articles
        print(f"::warning::Could not fetch the reading list from Raindrop: {error}")
        return 0
    OUTPUT.parent.mkdir(exist_ok=True)
    OUTPUT.write_text(json.dumps(bookmarks, ensure_ascii=False, indent=2) + "\n")
    print(f"Wrote {len(bookmarks)} bookmarks tagged #{tag} to {OUTPUT}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
