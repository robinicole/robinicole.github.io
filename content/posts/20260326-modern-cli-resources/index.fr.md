---
title: Ressources CLI modernes
date: 2026-03-26
draft: false
summary: Une liste d'outils et de ressources qui ont changé ma façon d'utiliser le terminal
tags:
  - cli
  - tools
  - resources
toc: true
---

{{< alert "circle-info" >}}
**Traduction automatique** — Cet article a ete traduit automatiquement depuis l'anglais. Vous pouvez consulter la version originale en anglais via le selecteur de langue en haut de la page.
{{< /alert >}}

**Cet article a été ébauché avec l'aide d'une IA et édité par un humain (moi), mais chaque outil listé ici est un outil que j'utilise vraiment au quotidien — ils viennent tous de mon `history` shell.**

Les outils CLI sont vieux — et c'est justement pour ça qu'ils sont bons. Tout comme un bon bricoleur a toujours besoin d'un simple tournevis, peu importe la sophistication de ses outils électriques, tout développeur a besoin de solides fondamentaux en ligne de commande. Les abstractions de base (pipes, fichiers, flux de texte) ont survécu des décennies parce qu'elles sont composables et universelles.

Voici une liste de **quelques** outils simples qui améliorent vraiment mon workflow au quotidien. Comme nous sommes à l'ère de l'IA, j'ai aussi ajouté Claude Code à la fin. Je suis convaincu que l'IA et le CLI sont faits l'un pour l'autre — l'essentiel de ce qui rend les LLMs puissants aujourd'hui, c'est leur capacité à utiliser des outils, et le terminal est la plus ancienne interface d'utilisation d'outils que nous ayons (voir [cette conférence](https://www.youtube.com/watch?v=AFUww-Df0C4) pour approfondir cette idée).

## Émulateurs de terminal

- [iTerm2](https://iterm2.com/) — J'ai quitté Terminal.app il y a des années et je n'ai jamais regardé en arrière. Panneaux divisés, recherche, autocomplétion — il fait tout ce dont on a besoin sans en faire des tonnes.

## Shell et prompt

- [Zsh](https://www.zsh.org/) — C'est le shell par défaut sur macOS depuis Catalina, donc vous l'utilisez peut-être déjà. Je l'associe à [Oh My Zsh](https://ohmyz.sh/) pour les plugins, même si le plus léger [zinit](https://github.com/zdharber/zinit) mérite d'être considéré si vous trouvez Oh My Zsh trop lourd.
- [Starship](https://starship.rs/) — Mon prompt. Il affiche le statut git, les versions des langages et le contexte cloud directement dans la ligne de prompt. Fonctionne avec tous les shells et ne demande quasiment aucune configuration.
- [Zoxide](https://github.com/ajeetdsouza/zoxide) — Probablement l'outil avec le meilleur ratio effort/récompense de cette liste. Il apprend vos répertoires les plus utilisés pour que vous puissiez taper `z blog` au lieu de `cd ~/Documents/projects/my-blog`. Une fois qu'on commence à l'utiliser, le simple `cd` semble cassé.

## Remplaçants modernes des outils classiques

Il y a toute une vague de réécritures en Rust et Go des outils Unix classiques, avec de meilleurs paramètres par défaut et de la couleur. En toute honnêteté : je tape encore `ls`, `cat` et `grep` par habitude. J'utilise [The Silver Searcher (`ag`)](https://github.com/ggreer/the_silver_searcher) pour la recherche dans le code, ce qui est déjà un gros progrès par rapport à `grep`. Le reste est sur ma liste à essayer — l'analogie du tournevis s'applique ici aussi, les originaux fonctionnent très bien mais ceux-ci sont juste plus agréables à manier.

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

Si vous voulez essayer ces outils sans changer vos habitudes, créez simplement des alias pour que votre mémoire musculaire continue de fonctionner :

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

## Navigation dans les fichiers

- [fzf](https://github.com/junegunn/fzf) — Celui-ci est difficile à expliquer tant qu'on ne l'a pas essayé. C'est un chercheur flou (fuzzy finder) — vous lui envoyez n'importe quoi via un pipe et vous obtenez un sélecteur interactif. La vraie puissance vient de sa composition avec d'autres outils : `rg "pattern" | fzf` pour chercher dans le code de manière interactive, ou `git log --oneline | fzf` pour choisir un commit. Une fois installé, il vous donne aussi `ctrl+t` pour la recherche de fichiers et `ctrl+r` pour un historique de commandes bien meilleur.

## Multiplexage

- [tmux](https://github.com/tmux/tmux) — Le multiplexeur de terminal classique, et un autre outil qui a résisté à l'épreuve du temps. Je l'utilise surtout pour garder des serveurs de dev en arrière-plan pendant que je travaille dans un autre panneau. Les sessions persistantes permettent de se déconnecter et de revenir plus tard sans rien perdre. À associer avec [tpm](https://github.com/tmux-plugins/tpm) pour les plugins.

## Utilitaires pour développeurs

- [jq](https://jqlang.github.io/jq/) — Si vous travaillez avec du JSON (et c'est probablement le cas), c'est indispensable. La syntaxe de requête demande un peu d'apprentissage, mais ça paie vite. Pour une approche plus douce, essayez [jnv](https://github.com/ynqa/jnv) qui vous donne un aperçu en direct pendant que vous construisez votre requête.
- [lazygit](https://github.com/jesseduffield/lazygit) — J'ai un alias `lg` pour cet outil et je l'ouvre avant presque chaque commit. Il rend le rebase, le staging de hunks individuels et la résolution de conflits tellement moins pénibles que les commandes git brutes. Si le CLI de git vous intimide, commencez par là.
- [Fork](https://git-fork.com/) — Je l'utilise en complément de lazygit. `fork .` ouvre le dépôt courant dans une interface graphique native et propre, ce qui est utile quand on a besoin de visualiser l'historique des branches ou de comprendre la vue d'ensemble.
- [lazydocker](https://github.com/jesseduffield/lazydocker) — Même concept que lazygit mais pour Docker. Voir les logs, redémarrer des conteneurs, gérer les volumes — le tout depuis une seule interface TUI.
- [tectonic](https://tectonic-typesetting.github.io/) — Si vous utilisez LaTeX, cet outil vous épargnera bien des douleurs. Il télécharge les paquets à la demande, pas de configuration `tlmgr` manuelle. `tectonic document.tex` et ça marche, tout simplement.

## Configuration SSH

Ce n'est pas un outil mais une astuce qui me fait gagner du temps tous les jours. Au lieu de taper `ssh -i ~/.ssh/key user@long-hostname.example.com -p 2222`, vous pouvez définir des alias courts dans `~/.ssh/config` :

```
Host dev
    HostName my-server.example.com
    User deploy
    Port 2222
    IdentityFile ~/.ssh/my_key
```

Ensuite, un simple `ssh dev`. Six caractères au lieu de soixante. Ça fonctionne aussi avec `scp`, `rsync` et VS Code remote.

## L'IA dans le terminal

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) — C'est l'outil qui m'a donné envie d'écrire cet article. Il tourne dans votre terminal, lit votre codebase, édite des fichiers, exécute des commandes et fait des commits. Je commence désormais la plupart de mes projets en tapant `claude` plutôt qu'en ouvrant un éditeur. Le terminal s'avère être une bien meilleure interface pour l'IA qu'une fenêtre de chat — il donne au modèle un accès direct à votre système de fichiers, votre historique git et vos outils de build. Ce qui, pour revenir à l'analogie du tournevis, fait du terminal le manche et du LLM l'embout interchangeable.

## Ressources d'apprentissage

- [The Art of Command Line](https://github.com/jlevy/the-art-of-command-line) — Un guide complet que je revisite de temps en temps. Couvre tout, de la navigation de base aux astuces auxquelles je n'aurais jamais pensé.
- [Modern Unix](https://github.com/ibraheemdev/modern-unix) — C'est là que j'ai découvert la plupart des outils du tableau ci-dessus.
- [Les zines de Julia Evans](https://wizardzines.com/) — La meilleure façon que je connaisse de développer une intuition sur le fonctionnement réel du réseau, de bash, de git et du DNS. Courts, illustrés et étonnamment profonds.
- [Command Line Interface Guidelines](https://clig.dev/) — Si vous *construisez* vos propres outils CLI, c'est le guide de style à suivre.

## Tout installer sur macOS

La plupart de ces outils sont disponibles via [Homebrew](https://brew.sh/). Voici un script unique pour tout installer :

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

Enregistrez ce script sous `install-cli-tools.sh`, lancez `chmod +x install-cli-tools.sh` et exécutez-le. Si certains outils sont déjà installés, Homebrew les ignorera.

---

Cette liste est subjective et reflète ce que j'utilise vraiment. Je la mettrai à jour au fur et à mesure que je découvre de nouveaux outils dignes d'être ajoutés à la boîte à outils.
