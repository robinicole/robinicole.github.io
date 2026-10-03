# Reading list

The `/reading/` page (`/fr/reading/` in French) lists every Raindrop.io bookmark
tagged `blog`, newest first. Each entry shows the title, the source website, the
date it was saved and the Raindrop note when there is one.

Why it works this way: [ADR 0002](adr/0002-reading-list-from-raindrop.md).

## How it works

1. `scripts/fetch_reading_list.py` calls the Raindrop API and writes
   `data/reading.json`. That file is git-ignored and never committed.
2. `layouts/_default/reading.html` renders the page from that file, styled by
   `assets/css/extended/reading.css`.
3. The deploy workflow runs the script before `hugo`, on every push to `main`,
   once a day (05:17 UTC) and on manual runs from the Actions tab.

To publish a bookmark: tag it `blog` in Raindrop. It shows up after the next
daily build, or straight away if you run the workflow by hand
(Actions → "Deploy Hugo site to Pages" → Run workflow).

## Test it locally

You need a Raindrop test token: Raindrop → Settings → Integrations →
Create new app → open it → Create test token.

```bash
# 1. Fetch your bookmarks (writes data/reading.json)
RAINDROP_TOKEN=your-token python3 scripts/fetch_reading_list.py

# 2. Run the site and open http://localhost:1313/reading/
hugo server --disableFastRender
```

The script prints how many bookmarks it wrote. Re-run step 1 after tagging
something new; `hugo server` picks up the new file on its own.

To try another tag without touching your `blog` bookmarks:

```bash
RAINDROP_TOKEN=your-token RAINDROP_TAG=some-tag python3 scripts/fetch_reading_list.py
```

To see the page as it looks when Raindrop is unreachable, delete the data file:
`rm data/reading.json`. The page then says the list is temporarily unavailable.

The script needs only the Python standard library, no `pip install`.

## Production setup (once)

Add the token as a repository secret: GitHub repo → Settings → Secrets and
variables → Actions → New repository secret, named `RAINDROP_TOKEN`.

## When something goes wrong

The build never fails because of the reading list. If the fetch fails, the
Actions run shows a yellow warning on the "Fetch reading list from Raindrop"
step, and the page shows the unavailable notice until the next good build.

| Warning | Fix |
|---|---|
| `RAINDROP_TOKEN is not set` | Add the secret (see above) |
| `HTTP Error 401` | Token revoked or wrong: create a new one and update the secret |
| Network or 5xx error | Raindrop is down; the next daily run fixes it |

GitHub turns off scheduled runs after 60 days with no activity in the repo. If
the list stops updating after a quiet spell, re-enable the workflow in the
Actions tab or push anything.
