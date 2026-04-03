---
title: Claude Code et le contrôle de version pour les connaissances de votre LLM
date: 2026-01-09
draft: true
summary: Comment utiliser Claude Code pour versionner les connaissances de votre LLM
tags:
  - llm
  - programming
  - git
series:
series_order:
toc: true
---

{{< alert "circle-info" >}}
**Traduction automatique** — Cet article a ete traduit automatiquement depuis l'anglais. Vous pouvez consulter la version originale en anglais via le selecteur de langue en haut de la page.
{{< /alert >}}
Lorsqu'on travaille avec des LLMs via l'interface chatbot classique de ChatGPT, Anthropic (Claude) ou un autre fournisseur de chatbot, l'un des aspects frustrants est le manque de transparence sur la façon dont le chatbot retient vos discussions entre les sessions. Dans cet article, j'explore comment utiliser Claude Code pour avoir de la transparence sur ce que le LLM retient (c'est stocké dans des fichiers Markdown standards) et comment utiliser git pour versionner ces connaissances.
