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

## La théorie

Voici une façon utile de se représenter un assistant IA. C'est un très grand tas de statistiques sur le langage, entraîné à prolonger un texte de manière plausible. C'est réducteur, et ça l'est vraiment, mais ça donne la bonne intuition: le modèle a lu une quantité énorme de choses sur à peu près tout, et ne sait pratiquement rien de la façon dont *vous* voulez qu'un travail soit fait. La connaissance générale est intégrée. **Les détails, non.** Chaque fois que vous ouvrez la boîte et que vous tapez, vous **repayez cet écart**, en réexpliquant comment vous voulez qu'un courriel soit tourné, la forme que doit prendre un résumé, les cinq étapes que vous suivez toujours pour une tâche donnée.

Un skill, c'est la façon d'**écrire ces détails une seule fois** au lieu de les répéter. C'est un petit fichier texte, quelques règles, rangé dans un dossier que l'assistant peut atteindre. L'assistant le lit seulement quand la tâche le demande, puis il suit ce qui y est écrit. Vous ne construisez pas de logiciel et vous ne réentraînez pas le modèle. Vous laissez une note sur le bureau, ramassée pile au moment où elle est pertinente. Pas cher à écrire, et ce coût d'écriture s'amortit sur toutes les conversations à venir.

L'exemple le plus clair est celui qui m'a aidé à rédiger cet article. Je l'ai écrit avec un skill appelé `grill-with-docs`. Laissé à lui-même, un modèle prend volontiers une demande vague et génère quelque chose de plausible. Mais plausible n'est pas ce que vous vouliez dire, et ce skill refuse de jouer le jeu. Il vous interroge d'abord. Pour qui est-ce, quelle est l'idée réelle, quelle longueur. Une question à la fois, chacune avec une réponse suggérée, jusqu'à ce que le plan soit vraiment fixé. Le skill lui-même tient en quelques lignes qui reviennent à dire "interroge-moi jusqu'à ce que ce soit clair, puis écris." Une toute petite contrainte, et elle change toute la dynamique de la conversation.

Un deuxième que je garde activé est `ponytail`. Il dit au modèle d'écrire comme écrit un collègue direct et expérimenté, simplement, sans remplissage, en supprimant la phrase qui n'apporte rien. Remarquez qu'il n'ajoute aucune capacité nouvelle. Il fixe seulement un **tempérament**: un biais que vous imposez à un système qui, livré à lui-même, dérive vers la moyenne fade de ses données d'entraînement.

Les skills peuvent aussi porter un vrai outil. Si un travail peut se faire en lançant un petit programme, le skill peut embarquer ce programme et dire au modèle quand y recourir. Vous n'avez pas besoin de cette partie pour tirer parti des skills. Il vaut juste la peine de savoir que le même mécanisme passe de "écris sur ce ton" à "lance ceci et lis le résultat."

En utiliser un est presque trop simple: vous tapez son nom précédé d'une barre oblique, comme `/grill-with-docs`, et le modèle trouve le fichier et le suit. Beaucoup de skills s'activent aussi tout seuls quand ce que vous faites correspond à ce pour quoi ils sont faits.

## La pratique

Écrire le vôtre est plus simple qu'il n'y paraît. Un skill est un fichier appelé `SKILL.md` placé dans son propre dossier. Le fichier a deux parties. En haut, entre deux lignes de `---`, un petit bloc de métadonnées: un nom et une description. En dessous, les instructions, écrites en français ordinaire. En voici un complet, qui transforme des notes de réunion en vrac en un résumé propre:

```markdown
---
name: meeting-notes
description: Transforme des notes de réunion brutes en décisions et actions. À utiliser quand je colle des notes de réunion.
---

Quand je te donne des notes de réunion:
1. Liste les décisions prises, une par ligne.
2. Liste les actions à mener, chacune avec la personne qui en est responsable.
3. Fais court. Pas de préambule, pas de résumé du résumé.
```

C'est tout. Enregistrez-le sous `meeting-notes/SKILL.md` dans le dossier que lit votre assistant (pour Claude Code, c'est `.claude/skills/`), et à partir de là vous pouvez taper `/meeting-notes` et coller. **Les skills ne sont pas propres à Claude Code.** Le chatbot Claude les comprend aussi, sur claude.ai et dans l'application de bureau, si bien que le même fichier fonctionne que vous viviez dans un terminal ou dans une fenêtre de chat. La ligne de description fait un travail discret mais important: c'est ce que l'assistant lit pour décider, tout seul, si ce skill est pertinent par rapport à ce que vous venez de demander. Écrivez-la comme une étiquette destinée à votre futur vous.

Les instructions peuvent être tout ce que vous taperiez autrement à la main. Commencez petit, utilisez le skill quelques fois, et resserrez la formulation partout où le résultat n'est pas tout à fait ce que vous vouliez. Un skill n'est jamais fini, il devient juste moins faux.

Alors commencez par un seul. Choisissez une tâche que vous expliquez sans cesse de la même manière, notez l'explication une fois, et laissez l'assistant la ramasser quand elle s'applique. L'intéressant n'est pas tel ou tel skill. C'est le **changement de posture**: vous cessez de traiter le modèle comme un oracle que vous interrogez, et commencez à le traiter comme un système que vous configurez.

## Ressources

- [Anthropic, documentation *Agent Skills*](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview): l'endroit où regarder pour la structure d'un fichier de skill et la façon dont l'assistant décide de le charger.
- [Use skills in Claude](https://support.claude.com/en/articles/12512180-use-skills-in-claude): comment ajouter et activer des skills dans les applications Claude pour ordinateur et web (Customize > Skills).
- [Les skills de Matt Pocock](https://github.com/mattpocock/skills): d'où viennent `grill-with-docs` et `grill-me`.
- [ponytail](https://github.com/DietrichGebert/ponytail): le skill qui fait écrire le modèle comme un développeur senior sans détour.
