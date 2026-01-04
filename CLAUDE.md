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
  - `menus.en.toml` - Navigation menus
  - `languages.en.toml` - Site metadata and author info
  - `markup.toml` - Markdown rendering (unsafe HTML enabled)

### Content Organization
- `content/posts/` - Blog posts (Markdown with YAML front matter)
- Posts can be single `.md` files or directories with `index.md` + assets
- Taxonomies: tags, categories, authors, series

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
