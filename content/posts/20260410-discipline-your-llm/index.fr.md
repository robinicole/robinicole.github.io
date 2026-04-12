---
title: "Comment discipliner son LLM pour les nuls"
date: 2026-04-10
draft: false
summary: "Comment discipliner ses agents. Le principe des contraintes et des harnais pour les systèmes d'IA fiables."
tags:
  - llm
  - ia-engineering
  - agents
  - zettelkasten
  - graphes-de-connaissances
featured: featured.png
---

{{< alert "circle-info" >}}
**Aussi sur Substack** — Cet article a été publié à l'origine sur [Intelligent artificiellement (Substack)](https://robinnicolem.substack.com/p/larchitecture-des-agents-dignes-de). Lisez-le là-bas pour les discussions et le contexte supplémentaire.
{{< /alert >}}

{{< alert "circle-info" >}}
**Traduction automatique** — Cet article a été traduit automatiquement depuis l'anglais. Vous pouvez consulter la version originale en anglais via le sélecteur de langue en haut de la page.
{{< /alert >}}

Dans cet article, je creuse la meilleure façon d'amener un LLM à faire réellement ce qu'on lui demande. Mon point de vue est assez simple : les LLM sont un peu comme nous, personne ne fait son meilleur travail noyé sous les règles, mais sans aucun garde-fou, tout dérape vite. Le point d'équilibre, c'est juste assez de structure pour les garder honnêtes, avec de la marge pour qu'ils fassent leur travail. Je commencerai par le code agentique, où le problème est en quelque sorte déjà résolu : les développeurs disposent depuis des années de compilateurs, de linters et de suites de tests pour garder le code sous contrôle. Puis j'examinerai comment transposer cette même idée à des tâches plus larges en utilisant les graphes de connaissances.

## Les harnais de code : les contraintes se composent

Commençons par ce qui marche vraiment. OpenAI a construit un produit interne[^1] où des agents ont écrit chaque ligne de code. Une équipe partant de trois ingénieurs, puis passée à sept, a ouvert environ 1 500 pull requests et généré de l'ordre d'un million de lignes de code, sans aucune implémentation écrite manuellement. Les ingénieurs ont cessé d'écrire du code et se sont mis à écrire des règles : tests, métriques, contraintes d'architecture, boucles de rétroaction. Le dépôt est devenu la source de vérité, car les agents ne peuvent pas raisonner sur ce qui n'est pas dans leur contexte. Toutes les décisions ont été versionnées dans des fichiers. Les règles étaient appliquées par des linters et des vérifications CI, pas par de la documentation.

Pourquoi est-ce que ça marche ? Richard Sutton[^2], le pionnier de l'apprentissage par renforcement, a identifié le schéma il y a des décennies : les méthodes générales qui passent à l'échelle avec la puissance de calcul battent le savoir artisanal. Les moteurs d'échecs ont battu les fonctions d'évaluation ajustées à la main par la recherche en force brute plutôt que par l'apprentissage ; les systèmes de vision ont appris à surpasser les descripteurs conçus manuellement (contours, SIFT). Le principe vaut dans les deux cas : l'échelle bat l'ingénierie manuelle. Mais passer à l'échelle ne corrige pas la composition des erreurs. Avec 5 % d'erreur par étape, une tâche de 20 étapes échoue 64 % du temps. Le harnais brise cette chaîne.

Chaque contrainte (test, vérification de type, règle de linter) intercepte les défaillances avant qu'elles ne se propagent. Le linting est peu coûteux et rapide, comparé à l'exécution d'un autre LLM pour valider. C'est pourquoi le logiciel convient aux agents : le harnais de contraintes est en partie déjà intégré. Systèmes de types, compilateurs, suites de tests contraignent déjà de façon mécanique. Un agent ne peut pas fusionner du code qui ne compile pas. Cette boucle de rétroaction instantanée est ce qui rend le travail agentique fiable. Cela rappelle les coupe-circuits des marchés financiers : automatiques, mécaniques, résistants à la manipulation.

Ce qui persiste, ce n'est pas le modèle. Les modèles s'améliorent et sont remplacés. C'est la structure autour du modèle qui compose en valeur. Un harnais rigoureux survit aux générations de modèles. Le code qui passait les tests l'an dernier contraindra la prochaine génération d'agents tout aussi efficacement.

## La vérification : le point de levier

Mais les contraintes sont faciles à mal calibrer. Trop rigides et le système ne peut pas s'adapter. Trop lâches et il dérive. L'art réside dans le calibrage, en particulier pour la vérification.

AlphaEvolve[^3] de DeepMind, un agent de code évolutionnaire, illustre cela parfaitement. Sur plus de 50 problèmes ouverts (67 en mathématiques, géométrie, combinatoire et théorie des nombres) : 75 % ont retrouvé les solutions de l'état de l'art, 20 % ont amélioré les résultats connus, y compris en faisant passer le nombre de baisers en dimension 11 de 592 à 593.

Mais voici l'échec révélateur : quand la vérification est faible, l'agent l'exploite. Au début, AlphaEvolve plaçait des points à des coordonnées quasi identiques dans des problèmes de géométrie, exploitant des problèmes de précision en virgule flottante dans le solveur de programmation linéaire. Il n'était pas perdu. Il était bien adapté à un problème mal spécifié. Terence Tao, collaborateur sur la recherche AlphaEvolve, a observé que le système trouvait des « solutions dégénérées ou une évaluation trop indulgente de solutions approchées », passant des vérifications lâches qui manquaient l'esprit du problème réel. La correction : les ingénieurs ont renforcé le vérificateur pour utiliser l'arithmétique exacte au lieu de l'approximation en virgule flottante.

La leçon est nette : le générateur ne vaut que ce que vaut le vérificateur. Quand on récompense quelque chose, on en obtient davantage, y compris de la fraude. L'effort humain passe de « trouver des solutions » à « concevoir une vérification non exploitable ». Arithmétique exacte plutôt que virgule flottante. Arithmétique par intervalles plutôt qu'estimations ponctuelles. Étapes vérifiées par typage. Plus votre vérificateur est solide, plus votre agent peut être intelligent. Ce principe passe à l'échelle du code aux preuves jusqu'à la connaissance.

## Le graphe personnel : la structure comme raisonnement

Les tests contraignent le code. Les vérificateurs contraignent les preuves. Ils fonctionnent en rejetant les états invalides. Un agent ne peut pas soumettre du code qui ne compile pas. Mais la connaissance ne fonctionne pas ainsi. On ne peut pas compiler une mauvaise idée. Il n'existe pas de vérification syntaxique pour la vérité. Pourtant le principe demeure : la structure permet le raisonnement.

Si vous tenez des notes avec des wikilinks, vous avez construit un graphe de connaissances. Chaque note est un nœud. Chaque [[lien]] est une arête. Lancez une détection de communautés. Des clusters émergent de la topologie seule, sans catégorisation manuelle.

Cela révèle quelque chose de crucial : vos liens encodent votre modèle mental. Vous n'avez pas catégorisé vos notes de haut en bas. Vous avez tissé des connexions de bas en haut. Les catégories sont émergentes, des représentations compressées de votre pensée associative. Plus important : vous avez construit un graphe de connaissances unique. Pas curé depuis internet. Construit à partir de votre travail.

Les LLM entraînés sur du texte public sont des machines à interpolation. Ils mélangent des schémas connus en combinaisons plausibles. Ils ne peuvent pas générer ce qui n'était pas implicitement présent dans leurs données d'entraînement. Votre graphe personnel est orthogonal à cela. Les liens que vous avez construits (économétrie vers séries temporelles, inférence causale vers théorie du portefeuille, méthode Zettelkasten vers réseaux de neurones) sont des associations non évidentes que l'internet public ne contient pas. Celles-là sont les vôtres.

Un LLM ayant accès à votre graphe ne synthétise pas à partir de schémas génériques. Il parcourt vos chaînes de raisonnement spécifiques. Il ne peut pas générer ces connexions seul. Le graphe fournit ce qui manque au modèle : votre histoire intellectuelle, pas la moyenne du jeu d'entraînement.

## Trois approches de la structuration des connaissances

**RAG vectoriel** : Embedder des documents, chercher par similarité. Rapide, mais récupère du contexte local. Ne peut pas raisonner à travers le corpus. On obtient des passages pertinents, pas de synthèse.

**GraphRAG** : Extraire des entités du texte via un LLM, construire un graphe, le partitionner, résumer les clusters. Meilleure connectivité que la recherche vectorielle, mais l'extraction est coûteuse et les hallucinations fréquentes. On paie ce coût de pipeline. Le rapport signal/bruit se dégrade parce que le LLM fait des erreurs de connexion.

**Zettelkasten annoté** : Le graphe existe parce que vous l'avez construit délibérément, un lien à la fois, sur des mois. Chaque lien est une ligne markdown. Les liens erronés sont supprimés. Zéro pipeline d'extraction. Zéro hallucination. Le rapport signal/bruit est élevé parce que vous avez validé chaque arête.

L'avantage plus profond : vos liens sont annotés. Pas « A → B », mais « A → B parce que X ». Chaque lien porte le pourquoi de son existence. Cela transforme le graphe en structure argumentative, pas seulement en topologie. Quand un LLM parcourt le graphe, il raisonne à partir de votre logique causale, pas de corrélations statistiques. La chaîne de raisonnement est transparente, tracée dans votre propre langage. L'arithmétique exacte pour la connaissance.

Parsez les wikilinks. Lancez un clustering de Louvain. Résumez chaque cluster avec un LLM local. Embeddez chaque note. C'est fait.

## Six façons de raisonner sur un graphe personnel

Indexez le coffre-fort. Un LLM avec accès MCP[^4] peut désormais :

**Chaînes de raisonnement** : Relier deux notes arbitraires via le chemin annoté le plus court. « Quel est le lien entre Zettelkasten et les réseaux de neurones sur graphes ? » Le système parcourt :
- Méthode Zettelkasten
- → Graphe de connaissances : « en forme naturellement un »
- → Réseaux de neurones sur graphes : « les GNN opèrent dessus »

Chaque étape porte le pourquoi. Dans vos propres mots.

**Ponts inter-domaines** : La détection de communautés trouve des clusters franchissant les frontières. Le graphe révèle des ponts entre des zones intellectuelles distantes, implicites dans vos liens, invisibles au premier regard. Vous ne les avez pas nommés. Les liens que vous avez construits les ont cristallisés en objets cohérents. Le graphe a rendu la structure lisible.

**Détection de lacunes** : Les paires de domaines sans aucune connexion révèlent des absences structurelles. En physique, on appelle cela la percolation : un feu ne se propage que si la densité d'arbres dépasse un seuil. La connaissance est identique. Les idées ne percolent entre domaines que si la densité de liens est suffisante. Les liens manquants sont des coupe-feu expliquant pourquoi les intuitions restent cloisonnées. Les combler n'est pas du rangement, c'est la différence entre un dossier et un système.

**Synthèse globale** : Interrogez sur un domaine. Le système identifie la communauté pertinente et synthétise à partir des annotations d'arêtes et des résumés. Cette synthèse ne peut venir d'aucune note isolée. Elle nécessite de comprendre la topologie : comment les idées sont reliées, pas ce qu'elles sont.

**Recherche sémantique et voisinages** : Similarité cosinus sur les embeddings, parcours à 2-3 sauts. Des opérations simples qui fonctionnent parce que le graphe est déjà curé.

**Génération de preuves** : Parcourir le chemin annoté, collecter le raisonnement de chaque lien, composer une dérivation. « Va de X à Y et montre ton travail. » Contrairement à une recherche vectorielle suivie d'un résumé, cela produit un argument tracé.

## Comment construire cela : étapes pratiques

**Partez de ce que vous avez** : Si vous maintenez déjà des notes avec des wikilinks (Obsidian, Roam, etc.), vous avez déjà un graphe. Pas besoin d'attendre qu'il soit « complet ».

**Parsez et partitionnez** : Lisez le coffre-fort, extrayez nœuds et arêtes annotées (lignes correspondant à `- [[Note]], annotation`). Lancez un clustering de Louvain pour détecter les communautés. Cela prend 30 minutes pour un coffre-fort de 1 000 notes.

**Embeddez et résumez** : Utilisez un petit modèle d'embedding (nomic-embed-text via Ollama, ou tout modèle ouvert) pour embedder chaque note. Résumez chaque communauté avec un LLM local ou un appel API mis en cache. Mettez en cache les résultats : les résumés changent lentement.

**Exposez le graphe** : Construisez un outil MCP qui accepte des requêtes comme `reasoning_chain("A", "B")` ou `gap_detection()`. Laissez un LLM le parcourir pendant la conversation.

**Annotez progressivement** : Votre graphe n'a pas besoin d'annotations parfaites pour être utile. Quand vous liez des notes, ajoutez une brève ligne « parce que ». Ce n'est pas de la surcharge, c'est la différence entre un dossier et un système.

## La structure émerge des relations

La méthode Zettelkasten[^5] repose sur cette observation. Les neurosciences la confirment. Les notes éphémères se comportent comme la mémoire à court terme : fragiles, évanescentes. Les notes permanentes se comportent comme la mémoire à long terme : structurées, liées, intégrées. Consolider une note éphémère signifie reformuler, relier aux connaissances existantes.

Cela reflète la consolidation de la mémoire dans le cerveau[^6]. La recherche montre que les nouveaux souvenirs doivent être entrelacés au sein des réseaux de connaissances existants. Apprendre, ce n'est pas ajouter de l'information isolée mais connecter du nouveau matériel à une compréhension existante. Plus il y a d'élaboration et de connexion, plus le souvenir est stable. Un Zettelkasten n'est pas métaphoriquement comme un cerveau. C'est un processus externe discipliné qui déclenche les mêmes principes de consolidation.

Cette structure devient interrogeable par une machine. Un LLM avec accès MCP[^4] parcourt votre graphe pas à pas, en suivant vos annotations, plutôt que de s'appuyer sur un seul passage de récupération. Quand il trouve des lacunes (orphelins, domaines déconnectés), il fait remonter des faiblesses invisibles de l'intérieur.

Karpathy[^7] a décrit le schéma : construire un wiki persistant, la connaissance compilée une fois et maintenue à jour, plutôt que redérivée à chaque requête. Un graphe maintenu manuellement étend cela avec des annotations sémantiques : chaque lien porte le pourquoi de son existence. Le wiki est persistant et annoté. La structure du graphe rend la composition lisible.

Voici ce qu'un LLM ne peut pas faire : connecter spontanément votre problème spécifique à votre taxonomie de domaine, annotée il y a des mois, encodée dans des liens. Cela nécessite un graphe encodant votre histoire intellectuelle. Le modèle peut interpoler entre des idées connues de son jeu d'entraînement. Il ne peut pas générer vos associations non évidentes.

## Le compromis de passage à l'échelle

Cette approche suppose une base de connaissances de petite à moyenne taille, curée à la main. À l'échelle (dix mille notes ou plus), la navigation devient un défi. Les chaînes de raisonnement s'approfondissent. Un LLM parcourant de longs chemins manque de contexte. Les annotations sémantiques qui rendent les petits graphes puissants peuvent devenir du bruit à grande échelle.

La solution est la récupération par couches : le RAG vectoriel pour réduire l'espace de recherche (quelles 100 communautés sont pertinentes ?), puis le parcours de graphe au sein de ces communautés. D'abord filtrer par pertinence, puis raisonner sur la structure. Cela combine la capacité de passage à l'échelle des embeddings avec la précision des arêtes annotées.

La navigation pure sur graphe sans récupération n'est peut-être optimale que pour des bases de connaissances personnelles de taille modeste (100 à 1 000 notes). Les systèmes plus grands nécessitent l'approche hybride : récupération sémantique au niveau supérieur, raisonnement sur graphe annoté au niveau local. La question ouverte n'est pas de savoir si les petits graphes fonctionnent (c'est le cas). C'est de savoir si cet hybride passe à l'échelle pour des bases de connaissances organisationnelles (100 000+ notes) où différents utilisateurs maintiennent différents domaines.

---

## Notes de bas de page

[^1]: Blog d'ingénierie OpenAI sur « Harness Engineering » - https://openai.com/index/harness-engineering/ — Documente l'expérience où des agents IA ont généré 1M+ lignes de code en production, montrant l'application pratique des contraintes dans les systèmes agents.

[^2]: L'essai de Richard Sutton « The Bitter Lesson » - http://www.incompleteideas.net/IncIdeas/BitterLesson.html — Un article de blog influent expliquant pourquoi les méthodes générales qui passent à l'échelle avec la puissance de calcul dépassent les approches artisanales spécifiques aux domaines.

[^3]: Recherche DeepMind sur AlphaEvolve - https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/ — Un agent de code évolutionnaire qui a résolu 67 problèmes ouverts en mathématiques, géométrie et combinatoire.

[^4]: Model Context Protocol (MCP) - https://modelcontextprotocol.io/ — Un standard émergeant pour connecter les systèmes IA à des outils externes et des sources de données, permettant des requêtes structurées sur les bases de connaissances.

[^5]: « How to Take Smart Notes » de Soenke Ahrens - https://www.soenkeahrens.de/en/takesmartnotes — Un guide pratique de la méthode Zettelkasten, montrant comment construire des systèmes de connaissances personnels par des notes interconnectées.

[^6]: Recherche sur la consolidation de la mémoire dans le cerveau - https://pmc.ncbi.nlm.nih.gov/articles/PMC3792618/ — Démontre que les nouveaux souvenirs doivent être intégrés dans les réseaux de connaissances existants pour la stabilité et la récupération.

[^7]: Gist d'Andrej Karpathy - https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f — Décrit le principe de construire des connaissances persistantes et compilées qui persistent à travers les requêtes plutôt que d'être redérivées à chaque fois.
