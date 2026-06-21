# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Personal Hugo blog ("Thought garden") focused on AI, LLMs, data science, and technology. Deployed to GitHub Pages at https://robinicole.github.io/.

## Build Commands

```bash
# Local development server with live reload
hugo server --disableFastRender

# Production build (matches CI)
hugo --gc --minify

# Create new post
hugo new posts/my-post-name/index.md

# Update theme submodule
git submodule update --remote themes/blowfish
```

## Obsidian Sync

Bidirectional sync tool in `scripts/hugo-obsidian-sync/` for editing posts in Obsidian.

```bash
# Install
pip install pyyaml

# Run tests
python3 scripts/hugo-obsidian-sync/test_sync.py

# Sync commands (if hugo-sync alias is configured)
hugo-sync --pull    # Pull Hugo posts to Obsidian
hugo-sync --push    # Push Obsidian changes to Hugo
hugo-sync --dry-run # Preview without writing
```

Converts between formats: mermaid fenced blocks ↔ `{{< mermaid >}}`, wikilinks ↔ `{{< ref >}}`, callouts ↔ `{{< alert >}}`, Obsidian images ↔ standard markdown.

## Architecture

**Hugo Static Site Generator** with Blowfish theme (git submodule at `themes/blowfish/`).

### Configuration Structure
- `config/_default/` - Modular Hugo configuration
  - `hugo.toml` - Main config (theme, taxonomies, related posts)
  - `params.toml` - Theme parameters (appearance, homepage layout, article settings)
  - `menus.en.toml` / `menus.fr.toml` - Navigation menus per language
  - `languages.en.toml` / `languages.fr.toml` - Site metadata and author info per language
  - `markup.toml` - Markdown rendering (unsafe HTML enabled)

### Content Organization
- `content/posts/` - Blog posts (Markdown with YAML front matter)
- Posts use Hugo's filename-based multilingual convention: `index.en.md` / `index.fr.md` (or `post-name.en.md` / `post-name.fr.md` for single-file posts)
- Taxonomies: tags, categories, authors, series

### Multilingual / Translation

The site is bilingual (English + French). English is the default language (weight 1).

**File naming convention:**
- Original English posts: `index.en.md` (or `post-name.en.md`)
- Original French posts: `index.fr.md`
- Translations use the same base name with the target language suffix

**When adding a new post:**
1. Write the post in its original language with the appropriate suffix (`.en.md` or `.fr.md`)
2. Create a translation file with the other language suffix in the same directory
3. Add a translation notice at the top of the translated file (after front matter):
   - For FR translations: `{{< alert "circle-info" >}}\n**Traduction automatique** — Cet article a ete traduit automatiquement depuis l'anglais. Vous pouvez consulter la version originale en anglais via le selecteur de langue en haut de la page.\n{{< /alert >}}`
   - For EN translations: `{{< alert "circle-info" >}}\n**Automatic translation** — This article was automatically translated from French. You can read the original French version by using the language switcher at the top of the page.\n{{< /alert >}}`
4. Do NOT add the notice to the original-language file

**Translation guidelines:**
- Translate title, summary, description in front matter
- Keep tags in English in both versions
- Keep Hugo shortcodes, code blocks, URLs, and Mermaid diagrams unchanged
- Keep the same date, draft status, and other metadata

**Before committing changes to a post, check that both language versions are in sync.** If the original was modified, update the translation to match.

### Key Front Matter Fields
```yaml
title: "Post Title"
date: 2024-01-01
draft: true/false
summary: "Brief description"
tags: ["tag1", "tag2"]
series: ["Series Name"]
series_order: 1
```

## Writing Style

When drafting or editing article prose, write so it reads like a human wrote it — not like an LLM. This applies to article body text, summaries, and descriptions; it does not apply to code, config, or front matter.

**Avoid the common AI tells:**
- No "It's not just X, it's Y" / "isn't merely X — it's Y" constructions.
- No "In today's fast-paced world", "In the ever-evolving landscape of", or other throat-clearing openers. Start with the actual point.
- Drop filler hedges and intensifiers: "delve", "leverage", "robust", "seamless", "crucial", "vital", "comprehensive", "harness the power of", "unlock", "elevate", "game-changer", "testament to", "navigate the complexities".
- No bullet lists where every item is `**Bold lead-in**: sentence.` — vary structure and write in prose when prose fits.
- Don't end every section with a tidy summarizing sentence ("In conclusion", "Ultimately", "At the end of the day").
- Avoid the rule-of-three rhythm on autopilot ("faster, cheaper, and more reliable") unless it's genuinely accurate.
- Don't overuse the em-dash as a default connector; mix punctuation naturally.
- Don't over-qualify with "it's worth noting", "it's important to remember", "that said".

**Write like the existing posts:**
- Match the voice and rhythm of articles already in `content/posts/`. Read a couple before drafting.
- Prefer concrete, specific claims over vague generalities. Use real examples, numbers, and names.
- Vary sentence length. Short sentences are fine. Some can run longer when the idea needs room.
- It's fine to be direct, opinionated, and occasionally informal — this is a personal garden, not corporate copy.
- Cut any sentence that doesn't add information. If a paragraph restates the previous one, delete it.

When in doubt, read it aloud: if it sounds like a press release or a chatbot, rewrite it.

## Deployment

Automated via GitHub Actions (`.github/workflows/hugo.yaml`):
- Triggers on push to `main` branch
- Uses Hugo Extended v0.124.0
- Builds with `--gc --minify`
- Deploys to GitHub Pages

## Agent skills

### Issue tracker

Issues live as local markdown files under `.scratch/<feature>/`. See `docs/agents/issue-tracker.md`.

### Triage labels

Default five-role vocabulary (needs-triage, needs-info, ready-for-agent, ready-for-human, wontfix). See `docs/agents/triage-labels.md`.

### Domain docs

Single-context repo — one `CONTEXT.md` + `docs/adr/` at the root. See `docs/agents/domain.md`.
