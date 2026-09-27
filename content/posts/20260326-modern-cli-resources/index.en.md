---
title: Modern CLI resources
date: 2026-03-26
draft: false
summary: A curated list of tools and resources that have changed how I use the terminal
tags:
  - cli
  - tools
  - resources
toc: true
---

**This article was drafted with AI and edited by a human (me), but every tool listed here is one I actually use daily — they all come from my shell `history`.**

CLI tools are old — and that is exactly why they are good. Just like every handyman needs a simple screwdriver no matter how advanced power tools get, every developer needs solid command-line fundamentals. The basic abstractions (pipes, files, text streams) have survived decades because they are composable and universal.

Here is a list of a **few** simple tools that genuinely make my workflow smoother. Because we are in the age of AI, I also added Claude Code at the end. I firmly believe that AI and the CLI are a natural fit — most of what makes LLMs powerful today is their ability to use tools, and the terminal is the oldest tool-use interface we have (see [this talk](https://www.youtube.com/watch?v=AFUww-Df0C4) for a deeper dive on this idea).

## Terminal emulators

- [iTerm2](https://iterm2.com/) — I switched from the default Terminal.app years ago and never looked back. Split panes, search, autocomplete — it does everything you need without being fancy about it.

## Shell and prompt

- [Zsh](https://www.zsh.org/) — It has been the default on macOS since Catalina, so you might already be using it. I pair it with [Oh My Zsh](https://ohmyz.sh/) for plugins, though the lighter [zinit](https://github.com/zdharber/zinit) is worth considering if you find Oh My Zsh too heavy.
- [Starship](https://starship.rs/) — My prompt. It shows git status, language versions, and cloud context right in the prompt line. Works across shells and you barely need to configure it.
- [Zoxide](https://github.com/ajeetdsouza/zoxide) — Probably the tool with the best effort-to-reward ratio on this list. It learns your most-used directories so you can type `z blog` instead of `cd ~/Documents/projects/my-blog`. Once you start using it, plain `cd` feels broken.

## Modern replacements for classic tools

There is a whole wave of Rust and Go rewrites of classic Unix tools with better defaults and colour output. Full disclosure: I still type plain `ls`, `cat`, and `grep` out of muscle memory. I do use [The Silver Searcher (`ag`)](https://github.com/ggreer/the_silver_searcher) for code search, which is already a big step up from `grep`. The rest are on my list to try — the screwdriver analogy applies here too, the originals work fine but these are just nicer to hold.

| Classic | Modern replacement | Why |
|---------|-------------------|-----|
| `ls` | [eza](https://github.com/eza-community/eza) | Colour, icons, git status, tree view |
| `cat` | [bat](https://github.com/sharkdp/bat) | Syntax highlighting, git integration, paging |
| `find` | [fd](https://github.com/sharkdp/fd) | Simpler syntax, respects `.gitignore`, faster |
| `grep` | [ripgrep (rg)](https://github.com/BurntSushi/ripgrep) | Much faster, smart defaults, `.gitignore` aware |
| `du` | [dust](https://github.com/bootandy/dust) | Visual directory size breakdown |
| `top` | [btop](https://github.com/aristocratos/btop) | Beautiful resource monitor with mouse support |
| `sed` | [sd](https://github.com/chmln/sd) | Simpler regex syntax, string literal mode |
| `diff` | [delta](https://github.com/dandavella/delta) | Syntax highlighting, side-by-side view, git integration |
| `curl` | [xh](https://github.com/ducaale/xh) | Coloured output, simpler syntax for JSON APIs |
| `man` | [tldr](https://tldr.sh/) | Community-maintained cheat sheets with practical examples |

If you want to try these without changing your habits, just alias them so your muscle memory keeps working:

```bash
alias ls="eza --icons --group-directories-first"
alias cat="bat --style=auto"
alias find="fd"
alias grep="rg --smart-case"
alias du="dust -r"
alias top="btop"
alias sed="sd"
alias diff="delta --side-by-side"
alias curl="xh"
alias man="tldr"
```

## File navigation

- [fzf](https://github.com/junegunn/fzf) — This one is hard to explain until you try it. It is a fuzzy finder — you pipe anything into it and get an interactive selector. The real power is composing it with other tools: `rg "pattern" | fzf` to search code interactively, or `git log --oneline | fzf` to pick a commit. Once installed it also gives you `ctrl+t` for file search and `ctrl+r` for a much better history search.

## Multiplexing

- [tmux](https://github.com/tmux/tmux) — The classic terminal multiplexer, and another tool that has survived the test of time. I use it mostly to keep dev servers running in the background while working in another pane. Persistent sessions mean you can disconnect and come back later without losing anything. Pair it with [tpm](https://github.com/tmux-plugins/tpm) for plugins.

## Developer utilities

- [jq](https://jqlang.github.io/jq/) — If you work with JSON (and you probably do), this is essential. The query syntax takes a bit of learning, but it pays off fast. For a gentler start, try [jnv](https://github.com/ynqa/jnv) which gives you a live preview as you build your query.
- [lazygit](https://github.com/jesseduffield/lazygit) — I have this aliased to `lg` and I open it before almost every commit. It makes rebasing, staging individual hunks, and resolving conflicts so much less painful than raw git commands. If git's CLI intimidates you, start here.
- [Fork](https://git-fork.com/) — I use this alongside lazygit. `fork .` opens the current repo in a clean native GUI, which is useful when you need to visualise branch history or understand the big picture across branches.
- [lazydocker](https://github.com/jesseduffield/lazydocker) — Same idea as lazygit but for Docker. View logs, restart containers, manage volumes — all from one TUI.
- [tectonic](https://tectonic-typesetting.github.io/) — If you use LaTeX, this saves a lot of pain. It downloads packages on demand, no manual `tlmgr` setup. `tectonic document.tex` just works.

## SSH config

This is not a tool but a trick that saves me time every day. Instead of typing `ssh -i ~/.ssh/key user@long-hostname.example.com -p 2222`, you can define short aliases in `~/.ssh/config`:

```
Host dev
    HostName my-server.example.com
    User deploy
    Port 2222
    IdentityFile ~/.ssh/my_key
```

Then just `ssh dev`. Six characters instead of sixty. It also works with `scp`, `rsync`, and VS Code remote.

## AI in the terminal

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) — This is the tool that prompted me to write this article. It runs in your terminal, reads your codebase, edits files, runs commands, and commits code. I now start most projects by typing `claude` rather than opening an editor. The terminal turns out to be a much better interface for AI than a chatbox — it gives the model direct access to your filesystem, git history, and build tools. Which, going back to the screwdriver analogy, makes the terminal the handle and the LLM the interchangeable bit.

## Learning resources

- [The Art of Command Line](https://github.com/jlevy/the-art-of-command-line) — A comprehensive guide that I revisit from time to time. Covers everything from basic navigation to tricks I had never thought of.
- [Modern Unix](https://github.com/ibraheemdev/modern-unix) — Where I discovered most of the tools in the table above.
- [Julia Evans' zines](https://wizardzines.com/) — The best way I know to build intuition about how networking, bash, git, and DNS actually work. Short, illustrated, and surprisingly deep.
- [Command Line Interface Guidelines](https://clig.dev/) — If you are *building* CLI tools yourself, this is the style guide to follow.

## Install everything on macOS

Most of these are available via [Homebrew](https://brew.sh/). Here is a single script to install them all:

```bash
#!/bin/bash
set -e

# Check for Homebrew
if ! command -v brew &> /dev/null; then
    echo "Installing Homebrew..."
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi

# Terminal emulator
brew install --cask iterm2

# Shell and prompt
brew install starship zoxide atuin

# Modern replacements
brew install eza bat fd ripgrep dust btop sd git-delta xh tldr the_silver_searcher

# File navigation
brew install fzf yazi
$(brew --prefix)/opt/fzf/install --key-bindings --completion --no-update-rc

# Multiplexing
brew install tmux

# Developer utilities
brew install jq lazygit lazydocker tectonic
brew install --cask fork

# AI
brew install claude-code

echo ""
echo "Done! Add the following to your ~/.zshrc:"
echo ""
echo '# Starship prompt'
echo 'eval "$(starship init zsh)"'
echo ""
echo '# Zoxide'
echo 'eval "$(zoxide init zsh)"'
echo ""
echo '# Atuin'
echo 'eval "$(atuin init zsh)"'
echo ""
echo '# Modern tool aliases'
echo 'alias ls="eza --icons --group-directories-first"'
echo 'alias cat="bat --style=auto"'
echo 'alias find="fd"'
echo 'alias grep="rg --smart-case"'
echo 'alias du="dust -r"'
echo 'alias top="btop"'
echo 'alias sed="sd"'
echo 'alias diff="delta --side-by-side"'
echo 'alias curl="xh"'
echo 'alias man="tldr"'
echo 'alias lg="lazygit"'
```

Save this as `install-cli-tools.sh`, run `chmod +x install-cli-tools.sh`, and execute it. If you already have some of these installed, Homebrew will skip them.

---

This list is opinionated and reflects what I actually use. I will update it as I discover new tools worth adding to the toolbox.
