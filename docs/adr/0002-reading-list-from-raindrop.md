# ADR 0002: Reading list fetched from Raindrop at build time

Status: Accepted
Date: 2026-10-03

## Context

The author saves articles in Raindrop.io and wants the ones worth recommending
on the site, styled like the rest of PaperMod, in both languages.

Raindrop's embed widget was ruled out: it is an iframe from raindrop.io, so the
site CSS cannot reach it, it does not follow PaperMod's theme toggle, and search
engines do not see the links.

## Decision

- A bookmark is published by tagging it `blog` in Raindrop, in any collection.
  Private collections stay private apart from what carries that tag.
- `scripts/fetch_reading_list.py` queries the Raindrop REST API for that tag
  across all collections (collection id `0`) and writes `data/reading.json`
  with the fields the page shows: title, link, domain, created date and note.
- The fetch runs inside the existing deploy workflow, just before `hugo`. The
  workflow also runs daily on a cron and on manual dispatch.
- `data/reading.json` is git-ignored. We do not commit fetched data: pushes
  made with the workflow's `GITHUB_TOKEN` do not trigger other workflows, so a
  fetch-and-commit job would not redeploy the site, and it would fill the
  history with bot commits.
- A failed fetch never fails the build. The script prints a GitHub Actions
  warning and exits 0; the page shows a "temporarily unavailable" notice.
  Publishing articles must not depend on a third-party API.
- Authentication uses a Raindrop test token stored as the `RAINDROP_TOKEN`
  repository secret. Raindrop has no read-only token; OAuth would add setup
  without narrowing access.

## Consequences

- The reading list is at most a day stale, unless the workflow is run by hand.
- The token grants full access to the Raindrop account. Revoke it by deleting
  the app in Raindrop's integration settings.
- GitHub disables scheduled workflows after 60 days without repository
  activity; the list then stops refreshing until the workflow is re-enabled or
  something is pushed.
- A Raindrop outage on a deploy day leaves the page showing the notice until
  the next successful build.
- Local builds without a token work; the page shows the notice. See
  `docs/reading-list.md` to test with real data.
