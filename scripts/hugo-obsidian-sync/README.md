# Hugo-Obsidian Sync

Bidirectional sync between Hugo blog posts and an Obsidian vault with automatic shortcode conversion.

## Features

- **Bidirectional sync** - Edit in Hugo or Obsidian, changes propagate both ways
- **Shortcode conversion** - Automatically converts between Hugo and Obsidian formats
- **Conflict detection** - Prompts when both sides have changes
- **Format preservation** - Directory-style and single-file posts maintain their structure

## Shortcode Conversions

| Hugo | Obsidian |
|------|----------|
| `{{< mermaid >}}...{{< /mermaid >}}` | ` ```mermaid...``` ` |
| `{{< ref "post.md" >}}` | `[[post]]` |
| `{{< alert >}}...{{< /alert >}}` | `> [!info]...` |
| `![](image.png)` | `![[image.png]]` |

## Installation

### 1. Install dependencies

```bash
pip install pyyaml
```

### 2. Create configuration

```bash
cd /path/to/hugo-blog/scripts/hugo-obsidian-sync
cp config.yaml.example config.yaml
```

Edit `config.yaml` with your paths:

```yaml
obsidian_vault: /path/to/obsidian-vault/blog-posts
hugo_content: /path/to/hugo-blog/content/posts
state_file: ~/.config/hugo-obsidian-sync/state.json
```

### 3. Add as a global command

To run `hugo-sync` from any folder, copy and paste this into your terminal:

```bash
# Create the command (replace /path/to/hugo-blog with your actual path)
sudo tee /usr/local/bin/hugo-sync > /dev/null << 'EOF'
#!/bin/bash
python3 /path/to/hugo-blog/scripts/hugo-obsidian-sync/sync.py "$@"
EOF

# Make it executable
sudo chmod +x /usr/local/bin/hugo-sync
```

That's it! Now you can run `hugo-sync` from anywhere.

#### Alternative: Shell alias

If you don't have sudo access, add this line to your `~/.zshrc` (or `~/.bashrc`):

```bash
alias hugo-sync='python3 /path/to/hugo-blog/scripts/hugo-obsidian-sync/sync.py'
```

Then reload your shell:

```bash
source ~/.zshrc
```

## Usage

```bash
# First sync - pull all Hugo posts to Obsidian
hugo-sync --pull

# Bidirectional sync (prompts on conflicts)
hugo-sync

# Push Obsidian changes to Hugo
hugo-sync --push

# Pull Hugo changes to Obsidian
hugo-sync --pull

# Preview changes without writing
hugo-sync --dry-run

# Force one side to win all conflicts
hugo-sync --force obsidian
hugo-sync --force hugo
```

## Workflow

1. **Initial setup**: Run `hugo-sync --pull` to copy all Hugo posts to Obsidian
2. **Daily editing**: Edit posts in either Hugo or Obsidian
3. **Before committing**: Run `hugo-sync` to sync changes
4. **On conflicts**: Choose which version to keep when prompted

## Creating a New Post in Obsidian

### Simple post (no images)

Create a new markdown file in your Obsidian vault's blog folder:

```
<obsidian-vault>/blog-posts/my-new-post.md
```

Add Hugo front matter at the top:

```yaml
---
title: "My New Post"
date: 2025-01-04
draft: true
summary: "A brief description of the post"
tags: ["tag1", "tag2"]
---

Your content here...
```

### Post with images

Create a folder for your post with images inside:

```
<obsidian-vault>/blog-posts/my-gallery-post/
├── my-gallery-post.md
├── photo1.png
└── photo2.jpg
```

In your markdown, embed images using Obsidian syntax:

```markdown
---
title: "My Gallery Post"
date: 2025-01-04
draft: false
summary: "A post with images"
tags: ["photography"]
---

Here's a photo:

![[photo1.png]]

And another:

![[photo2.jpg]]
```

When synced to Hugo, this becomes `my-gallery-post/index.md` with images alongside.

### Using Obsidian features

These Obsidian features automatically convert to Hugo shortcodes:

**Mermaid diagrams** - Use fenced code blocks:

````markdown
```mermaid
graph LR
    A[Start] --> B[End]
```
````

**Callouts** - Use Obsidian callout syntax:

```markdown
> [!info]
> This is an info callout
```

**Internal links** - Use wikilinks to reference other posts:

```markdown
See also [[other-post-name]]
or with custom text [[other-post-name|click here]]
```

### Front matter reference

| Field | Required | Description |
|-------|----------|-------------|
| `title` | Yes | Post title |
| `date` | Yes | Publish date (YYYY-MM-DD) |
| `draft` | No | Set to `true` to hide from production |
| `summary` | No | Brief description for post listings |
| `tags` | No | List of tags |
| `series` | No | Series name for multi-part posts |
| `series_order` | No | Position in series (1, 2, 3...) |

### Publish workflow

1. Create post in Obsidian with `draft: true`
2. Write and edit your content
3. Run `hugo-sync --push` to sync to Hugo
4. Preview with `hugo server` in the blog repo
5. When ready, set `draft: false` and sync again
6. Commit and push to publish

## File Structure

```
hugo-obsidian-sync/
├── sync.py              # Main CLI
├── converters.py        # Shortcode conversion
├── state.py             # Change tracking
├── config.yaml          # Your configuration
├── config.yaml.example  # Template
├── requirements.txt     # Dependencies
├── test_sync.py         # Tests
└── README.md
```

## Troubleshooting

### Reset sync state

If posts get out of sync, delete the state file and re-pull:

```bash
rm ~/.config/hugo-obsidian-sync/state.json
hugo-sync --pull
```

### Run tests

```bash
cd /path/to/hugo-blog/scripts/hugo-obsidian-sync
python3 test_sync.py
```
