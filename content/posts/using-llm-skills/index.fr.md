---
title: "Premiers pas avec les skills LLM"
date: 2026-06-27
draft: false
summary: "Ce qu'est un skill d'agent, expliqué à quelqu'un qui découvre les assistants IA."
tags:
  - llm
  - ai
  - agent-skills
---

{{< alert "circle-info" >}}
**Traduction automatique** — Cet article a ete traduit automatiquement depuis l'anglais. Vous pouvez consulter la version originale en anglais via le selecteur de langue en haut de la page.
{{< /alert >}}

Voici une façon utile de se représenter un assistant IA. C'est un très grand tas de statistiques sur le langage, entraîné à prolonger un texte de manière plausible. C'est réducteur, et ça l'est vraiment, mais ça donne la bonne intuition: le modèle a lu une quantité énorme de choses sur à peu près tout, et ne sait pratiquement rien de la façon dont *vous* voulez qu'un travail soit fait. La connaissance générale est intégrée. **Les détails, non.** Chaque fois que vous ouvrez la boîte et que vous tapez, vous **repayez cet écart**, en réexpliquant comment vous voulez qu'un courriel soit tourné, la forme que doit prendre un résumé, les cinq étapes que vous suivez toujours pour une tâche donnée.

Un skill, c'est la façon d'**écrire ces détails une seule fois** au lieu de les répéter. C'est un petit fichier texte, quelques règles, rangé dans un dossier que l'assistant peut atteindre. L'assistant le lit seulement quand la tâche le demande, puis il suit ce qui y est écrit. Vous ne construisez pas de logiciel et vous ne réentraînez pas le modèle. Vous laissez une note sur le bureau, ramassée pile au moment où elle est pertinente. Pas cher à écrire, et ce coût d'écriture s'amortit sur toutes les conversations à venir.

L'exemple le plus clair est celui qui m'a aidé à rédiger cet article. Je l'ai écrit avec un skill appelé `grill-with-docs`. Laissé à lui-même, un modèle prend volontiers une demande vague et génère quelque chose de plausible. Mais plausible n'est pas ce que vous vouliez dire, et ce skill refuse de jouer le jeu. Il vous interroge d'abord. Pour qui est-ce, quelle est l'idée réelle, quelle longueur. Une question à la fois, chacune avec une réponse suggérée, jusqu'à ce que le plan soit vraiment fixé. Le skill lui-même tient en quelques lignes qui reviennent à dire "interroge-moi jusqu'à ce que ce soit clair, puis écris." Une toute petite contrainte, et elle change toute la dynamique de la conversation.

Un deuxième que je garde activé est `ponytail`. Il dit au modèle d'écrire comme écrit un collègue direct et expérimenté, simplement, sans remplissage, en supprimant la phrase qui n'apporte rien. Remarquez qu'il n'ajoute aucune capacité nouvelle. Il fixe seulement un **tempérament**: un biais que vous imposez à un système qui, livré à lui-même, dérive vers la moyenne fade de ses données d'entraînement.

Les skills peuvent aussi porter un vrai outil. Si un travail peut se faire en lançant un petit programme, le skill peut embarquer ce programme et dire au modèle quand y recourir. Vous n'avez pas besoin de cette partie pour tirer parti des skills. Il vaut juste la peine de savoir que le même mécanisme passe de "écris sur ce ton" à "lance ceci et lis le résultat."

En utiliser un est d'une simplicité presque décevante: vous tapez son nom précédé d'une barre oblique, comme `/grill-with-docs`, et le modèle trouve le fichier et le suit. Beaucoup de skills s'activent aussi tout seuls quand ce que vous faites correspond à ce pour quoi ils sont faits.

Alors commencez par un seul. Choisissez une tâche que vous expliquez sans cesse de la même manière, notez l'explication une fois, et laissez l'assistant la ramasser quand elle s'applique. L'intéressant n'est pas tel ou tel skill. C'est le **changement de posture**: vous cessez de traiter le modèle comme un oracle que vous interrogez, et commencez à le traiter comme un système que vous configurez.

## Références

- [Anthropic, documentation *Agent Skills*](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview): l'endroit où regarder pour la structure d'un fichier de skill et la façon dont l'assistant décide de le charger.
- [Les skills de Matt Pocock](https://github.com/mattpocock/skills): d'où viennent `grill-with-docs` et `grill-me`.
- [ponytail](https://github.com/DietrichGebert/ponytail): le skill qui fait écrire le modèle comme un développeur senior sans détour.
