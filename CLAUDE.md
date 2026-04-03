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

## Deployment

Automated via GitHub Actions (`.github/workflows/hugo.yaml`):
- Triggers on push to `main` branch
- Uses Hugo Extended v0.124.0
- Builds with `--gc --minify`
- Deploys to GitHub Pages
