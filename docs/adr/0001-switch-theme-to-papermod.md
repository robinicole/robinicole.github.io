# ADR 0001 — Switch site theme from Blowfish to PaperMod

Status: Accepted
Date: 2026-06-28

## Context

The site ran on the Blowfish theme (`themes/blowfish/`, git submodule). We switched
the active theme to PaperMod (`themes/PaperMod/`, git submodule) for a cleaner,
lighter layout. Blowfish remains in the repo as a submodule, so the switch is a
config change plus a handful of compatibility shims, not a deletion.

## Decision

`theme = "PaperMod"` in `config/_default/hugo.toml`.

PaperMod does not ship Blowfish's shortcodes or read Blowfish's param/author
structure, so the switch required local overrides under `layouts/` (these are
project-level overrides; the theme submodules are untouched):

- `layouts/shortcodes/alert.html`, `lead.html`, `mermaid.html` — minimal stubs for
  the Blowfish-only shortcodes used in content (`ref` is a Hugo built-in, no stub
  needed). `mermaid.html` loads mermaid from a CDN.
- `layouts/partials/author.html` — overrides PaperMod's author partial to read the
  author *name* out of the Blowfish-style author **map** (`[params.author]` in
  `languages.en.toml` / `languages.fr.toml`). Without this, PaperMod prints the whole
  map (`map[bio:... name:...]`) in the byline and `<meta name="author">`.
- `layouts/partials/templates/schema_json.html` — overrides PaperMod's JSON-LD
  template. The stock version emits invalid JSON for this site (it inlined the author
  map, and its breadcrumb list dropped a comma on shallow paths), which broke
  `hugo --minify`. The override builds the breadcrumb with `slice`+`jsonify` and pulls
  the author name via the `author.html` partial.
- `layouts/partials/header.html` — overrides PaperMod's header so the language
  switcher links to the *current page's* translation (falling back to the language
  home when the page has no translation), instead of always linking to the language
  home.

Other related config (not strictly required by the switch):
- `disableSpecial1stPost = true` in `config/_default/params.toml` — render every
  homepage post in the same card style (PaperMod otherwise gives the first post a
  full-width hero treatment).
- "Work With Me" menu item points to the external site `https://withrobin.space/en`
  (EN) / `https://withrobin.space/fr` (FR) via `url =` in the per-language menu files,
  instead of an internal `work-with-me` page.

`config/_default/params.toml` is still written for Blowfish. PaperMod ignores the
keys it doesn't recognize, so it stays in place harmlessly and is ready if we revert.

## How to revert to Blowfish

1. In `config/_default/hugo.toml`, set `theme = "blowfish"`.
2. Remove the PaperMod compatibility overrides so Blowfish uses its own
   templates/shortcodes:
   - `rm layouts/shortcodes/alert.html layouts/shortcodes/lead.html layouts/shortcodes/mermaid.html`
     (Blowfish provides its own `alert`, `lead`, `mermaid`).
   - `rm layouts/partials/author.html`
   - `rm layouts/partials/templates/schema_json.html`
   - `rm layouts/partials/header.html`
3. Revert the menu items in `config/_default/menus.en.toml` / `menus.fr.toml` back to
   `pageRef = "work-with-me"` if the internal page is wanted again.
4. Optionally remove `disableSpecial1stPost = true` from
   `config/_default/params.toml` (PaperMod-only key; Blowfish ignores it).
5. Leaving the PaperMod submodule in place is fine. To remove it entirely:
   `git submodule deinit -f themes/PaperMod && git rm -f themes/PaperMod`.
6. Verify with the CI build command: `hugo --gc --minify`.

## Consequences

- The repo carries both theme submodules; switching themes is a one-line config
  change plus deleting/restoring the four `layouts/` overrides above.
- The overrides are coupled to PaperMod's internals. A PaperMod upgrade can drift
  from the copied `header.html` / `schema_json.html`; re-diff against the theme's
  versions after `git submodule update --remote themes/PaperMod`.
