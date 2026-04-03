---
title: Astuces LLM
date: 2026-01-11
draft: false
summary: Quelques réflexions et questions ouvertes sur les LLMs
tags:
  - ai
  - llm
series:
series_order:
toc: true
---

{{< alert "circle-info" >}}
**Traduction automatique** — Cet article a ete traduit automatiquement depuis l'anglais. Vous pouvez consulter la version originale en anglais via le selecteur de langue en haut de la page.
{{< /alert >}}
## Claude Code comme éditeur Markdown dopé à l'IA
La différence entre Claude Code et l'interface chatGPT classique est-elle la même que celle entre un simple éditeur Markdown et un éditeur WYSIWYG comme Word ?

Claude Code semble être davantage une interface IA vers un LLM utilisable pour de nombreuses tâches au-delà du code, et pour laquelle les connaissances de chaque tâche sont stockées dans des fichiers Markdown plutôt que dans une base de données.

**Liste de lecture** https://every.to/source-code/how-to-use-claude-code-for-everyday-tasks-no-programming-required 

## Génération de documents
Lorsque vous générez des documents tels que des présentations ou des diagrammes, je recommande de privilégier les formats en texte brut qui peuvent ensuite être convertis vers le format de sortie souhaité.
Pour les présentations, demandez à votre LLM d'utiliser Beamer, le framework de présentation LaTeX. En bonus, Claude peut lui-même lancer la compilation LaTeX et déboguer les erreurs éventuelles ([voir cette conversation par exemple](https://claude.ai/share/ba43da87-e11e-410c-8909-3997184dfc32)). Essayez de l'utiliser pour générer des présentations résumant des articles d'arXiv.
Pour les diagrammes, Mermaid et TikZ sont d'excellents choix. Pour les documents textuels plus longs, LaTeX reste mon option préférée.
