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

**Cet article a été ébauché avec l'aide d'une IA et édité par un humain (moi), mais chaque outil listé ici est un outil que j'utilise vraiment au quotidien. Ils sortent tous de l'`history` de mon shell.**

Coder avec l'IA, c'est parti pour durer, et j'adore ça. Mais comme l'écrivait John Naughton [dans le Guardian](https://www.theguardian.com/technology/2025/mar/16/ai-software-coding-programmer-expertise-jobs-threat), on n'a peut-être plus besoin de code pour être programmeur, **on a toujours besoin d'expertise**. Une bonne partie de cette expertise n'a rien de glamour : savoir se débrouiller dans un terminal. Comme un bricoleur qui garde un tournevis à côté de ses outils électriques, tout développeur a besoin des fondamentaux de la ligne de commande. Pipes, fichiers et flux de texte ont traversé les décennies parce qu'ils sont composables et universels.

C'est aussi ce sur quoi les LLM s'appuient : le terminal est la plus ancienne interface d'appel d'outils que nous ayons, et la conférence de Rémi Louf [AI needs its Unix moment](https://www.youtube.com/watch?v=AFUww-Df0C4) propose même de traiter les LLM comme des outils en ligne de commande, une piste que je trouve prometteuse. **Une maison a toujours besoin de fondations solides, et ces fondations, c'est la ligne de commande moderne.** Je suppose que c'est pour ça qu'[OpenAI a racheté Astral](https://www.bloomberg.com/news/articles/2026-03-19/openai-to-acquire-python-startup-astral-expanding-push-into-coding), l'entreprise derrière uv et Ruff, pour bâtir l'outillage autour de Codex.

Voici les outils qui rendent mon travail quotidien plus fluide, avec Claude Code à la fin.

## Émulateurs de terminal

- [iTerm2](https://iterm2.com/) : j'ai quitté Terminal.app il y a des années et je ne l'ai jamais regretté. Panneaux divisés, recherche, autocomplétion. Il fait tout ce dont on a besoin sans en faire des tonnes.

## Shell et prompt

- [Zsh](https://www.zsh.org/) : le shell par défaut sur macOS depuis Catalina, donc vous l'utilisez peut-être déjà. Je l'associe à [Oh My Zsh](https://ohmyz.sh/) pour les plugins, même si le plus léger [zinit](https://github.com/zdharma-continuum/zinit) vaut le coup d'œil si vous trouvez Oh My Zsh trop lourd.
- [Starship](https://starship.rs/) : mon prompt. Il affiche le statut git, les versions des langages et le contexte cloud directement dans la ligne de prompt. Fonctionne avec tous les shells et ne demande quasiment aucune configuration.
- [Zoxide](https://github.com/ajeetdsouza/zoxide) : **probablement l'outil de cette liste avec le meilleur rapport effort/bénéfice**. Il apprend vos répertoires les plus utilisés pour que vous puissiez taper `z blog` au lieu de `cd ~/Documents/projects/my-blog`.

## Remplaçants modernes des outils classiques

Il y a toute une vague de réécritures en Rust et Go des outils Unix classiques, avec de meilleurs paramètres par défaut et de la couleur. Je tape encore `ls`, `cat` et `grep` par habitude. J'utilise [The Silver Searcher (`ag`)](https://github.com/ggreer/the_silver_searcher) pour la recherche dans le code, ce qui est déjà un gros progrès par rapport à `grep`. Le reste est sur ma liste de choses à essayer.

| Classique | Remplaçant moderne | Pourquoi |
|-----------|--------------------|----------|
| `ls` | [eza](https://github.com/eza-community/eza) | Couleur, icônes, statut git, vue arborescente |
| `cat` | [bat](https://github.com/sharkdp/bat) | Coloration syntaxique, intégration git, pagination |
| `find` | [fd](https://github.com/sharkdp/fd) | Syntaxe plus simple, respecte le `.gitignore`, plus rapide |
| `grep` | [ripgrep (rg)](https://github.com/BurntSushi/ripgrep) | Bien plus rapide, bons réglages par défaut, respecte le `.gitignore` |
| `du` | [dust](https://github.com/bootandy/dust) | Répartition visuelle de la taille des répertoires |
| `top` | [btop](https://github.com/aristocratos/btop) | Moniteur de ressources soigné, avec support de la souris |
| `sed` | [sd](https://github.com/chmln/sd) | Syntaxe regex plus simple, mode chaîne littérale |
| `diff` | [delta](https://github.com/dandavison/delta) | Coloration syntaxique, vue côte à côte, intégration git |
| `curl` | [xh](https://github.com/ducaale/xh) | Sortie en couleur, syntaxe plus simple pour les API JSON |
| `man` | [tldr](https://tldr.sh/) | Aide-mémoire communautaires avec des exemples concrets |

Si vous voulez essayer ces outils sans changer vos habitudes, **créez des alias pour que votre mémoire musculaire continue de fonctionner** :

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

- [fzf](https://github.com/junegunn/fzf) : difficile à expliquer tant qu'on ne l'a pas essayé. C'est un outil de recherche floue (fuzzy finder) : vous lui envoyez n'importe quoi via un pipe et vous obtenez un sélecteur interactif. **Ça devient intéressant quand on le compose avec d'autres outils**, `rg "pattern" | fzf` pour chercher dans le code de manière interactive, ou `git log --oneline | fzf` pour choisir un commit. Une fois installé, il vous donne aussi `ctrl+t` pour la recherche de fichiers et `ctrl+r` pour une recherche dans l'historique bien plus efficace.

## Multiplexage

- [tmux](https://github.com/tmux/tmux) : le multiplexeur de terminal classique, et un autre outil qui a résisté à l'épreuve du temps. Je l'utilise surtout pour garder des serveurs de dev en arrière-plan pendant que je travaille dans un autre panneau. **Les sessions persistantes permettent de se déconnecter et de revenir plus tard sans rien perdre.** À associer avec [tpm](https://github.com/tmux-plugins/tpm) pour les plugins.

## Utilitaires pour développeurs

- [jq](https://jqlang.github.io/jq/) : si vous travaillez avec du JSON (et c'est probablement le cas), c'est indispensable. La syntaxe de requête demande un peu d'apprentissage, mais ça paie vite. Pour une approche plus douce, essayez [jnv](https://github.com/ynqa/jnv), qui vous donne un aperçu en direct pendant que vous construisez votre requête.
- [lazygit](https://github.com/jesseduffield/lazygit) : j'ai un alias `lg` pour cet outil et **je l'ouvre avant presque chaque commit**. Il rend le rebase, le staging hunk par hunk et la résolution de conflits bien moins pénibles que les commandes git brutes. Si la ligne de commande de git vous intimide, commencez par là.
- [Fork](https://git-fork.com/) : je l'utilise en complément de lazygit. `fork .` ouvre le dépôt courant dans une interface graphique native et propre, ce qui est utile quand on a besoin de visualiser l'historique des branches ou de comprendre la vue d'ensemble.
- [lazydocker](https://github.com/jesseduffield/lazydocker) : même concept que lazygit mais pour Docker. Voir les logs, redémarrer des conteneurs, gérer les volumes, le tout depuis une seule interface en mode texte.
- [tectonic](https://tectonic-typesetting.github.io/) : si vous utilisez LaTeX, cet outil vous épargnera bien des tracas. Il télécharge les paquets à la demande, pas de configuration `tlmgr` manuelle. `tectonic document.tex` et ça marche, tout simplement.

## Configuration SSH

Ici, ce n'est pas un outil mais une astuce de configuration, et elle me fait gagner du temps tous les jours. Au lieu de taper `ssh -i ~/.ssh/key user@long-hostname.example.com -p 2222`, vous pouvez définir des alias courts dans `~/.ssh/config` :

```
Host dev
    HostName my-server.example.com
    User deploy
    Port 2222
    IdentityFile ~/.ssh/my_key
```

**Ensuite, un simple `ssh dev`. Six caractères au lieu de soixante.** Ça fonctionne aussi avec `scp`, `rsync` et VS Code remote.

## L'IA dans le terminal

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) : un outil en ligne de commande pour coder avec Claude. C'est lui qui m'a donné envie d'écrire cet article.

## Ressources d'apprentissage

- [The Art of Command Line](https://github.com/jlevy/the-art-of-command-line) : un long guide que je relis de temps en temps. Couvre tout, de la navigation de base aux astuces auxquelles je n'aurais jamais pensé.
- [Modern Unix](https://github.com/ibraheemdev/modern-unix) : **c'est là que j'ai découvert la plupart des outils du tableau ci-dessus**.
- [Les zines de Julia Evans](https://wizardzines.com/) : la meilleure manière que je connaisse de développer une intuition sur la façon dont le réseau, bash, git et le DNS fonctionnent vraiment. Courts, illustrés, et plus profonds qu'ils n'en ont l'air.
- [Command Line Interface Guidelines](https://clig.dev/) : si vous *développez* vos propres outils en ligne de commande, c'est le guide de style à suivre.

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

Cette liste reflète ce que j'utilise vraiment. Je la mettrai à jour au fur et à mesure que je trouve de nouveaux outils qui méritent d'y figurer.
