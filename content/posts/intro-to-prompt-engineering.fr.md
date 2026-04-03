---
title: "Introduction au prompt engineering (Debutant)"
date: 2024-04-13
draft: true
summary: "Une introduction rapide et simple au prompt engineering, ou comment tirer le meilleur parti des chatbots comme ChatGPT"
tags: ["llm", "prompt-engineering"]
series: ["Prompt Engineering"]
series_order: 1
toc: true
---

A la fin de cet article, vous saurez comment creer des prompts efficaces pour ChatGPT et d'autres modeles de langage IA, meme si vous debutez dans le domaine !
N'hesitez pas a jeter un oeil a [ce generateur de prompts](https://robin-nicole.streamlit.app/), qui genere des prompts selon les principes decrits dans cet article.

Avec les compliments de Robin, l'auteur de cet article ;)
Vous pouvez trouver une version plus detaillee de cet article destinee a un public plus experimente en IA [ici]({{< ref "llm_prompting.md" >}})
# Qu'est-ce que le Prompt Engineering ?
Le prompt engineering est le processus de conception des bons prompts (instructions) pour obtenir le resultat souhaite a partir de modeles de langage IA comme ChatGPT.

C'est un peu comme donner des indications a un ami pour trouver votre maison. Si vous lui donnez des instructions claires et precises, il trouvera facilement. Mais si vos indications sont vagues ou confuses, il risque de se perdre. C'est la meme chose avec les modeles d'IA : meilleurs sont vos prompts, meilleurs sont les resultats !

# Pourquoi le Prompt Engineering est-il important ?
ChatGPT et les autres modeles de langage sont incroyablement polyvalents, ce qui est formidable car cela signifie qu'ils peuvent etre utilises pour toutes sortes de taches. Cependant, cela signifie aussi que leurs reponses peuvent etre assez generiques si vous ne les guidez pas correctement.

Imaginez demander a un ami de vous preparer un gateau sans lui donner de recette. Il fera peut-etre quelque chose de bon, mais ce ne sera pas forcement la saveur ou le style dont vous aviez envie. Le prompt engineering, c'est comme donner a l'IA une recette detaillee a suivre.

# Techniques de base du Prompt Engineering
Voici trois techniques simples que vous pouvez utiliser pour creer des prompts efficaces :

- **Few-Shot Prompting :** Donnez des exemples de ce que vous voulez !
Tout comme montrer a un ami des photos du gateau que vous voulez, donnez a l'IA quelques exemples du resultat souhaite.
Cela aide le modele a comprendre le style, le format et le contenu que vous recherchez.
- **Le framework CO-STAR :** Plantez le decor pour l'IA.
Fournissez le contexte (C) sur le cadre de votre tache.
Definissez clairement l'objectif (O) ou la tache a accomplir.
Specifiez le style et le ton (ST) souhaites : formel, decontracte, ou adapte a un public specifique.
Decrivez le public cible (A pour Audience) du resultat.
Precisez le format de reponse (R) que vous attendez de l'IA.

- **Chain of Thought Prompting :** Encouragez la reflexion etape par etape.
Tout comme nous resolvons des problemes complexes en les decomposant en etapes, vous pouvez demander a l'IA de faire de meme.
Des prompts comme "Reflechissons a cela etape par etape" ou la description d'etapes specifiques a suivre pour l'IA peuvent mener a des reponses plus precises et mieux raisonnees.

# Les templates de prompts : votre arme secrete
Une fois que vous avez elabore le prompt parfait pour une tache, vous voudrez peut-etre le reutiliser a l'avenir avec de legers ajustements. C'est la que les templates de prompts entrent en jeu !

Les templates vous permettent de creer une structure standard pour vos prompts, avec des emplacements reserves pour les informations qui changent a chaque utilisation. Cela vous evite de reecrire l'integralite du prompt a chaque fois que vous en avez besoin.

Vous pouvez creer des templates dans un simple document ou aller plus loin en utilisant du code Python pour remplir automatiquement les emplacements reserves. Mais ne vous inquietez pas si la programmation n'est pas votre truc : meme un simple document template peut vous faire gagner enormement de temps !

# Tout assembler
Un prompt engineering efficace est la cle pour tirer le meilleur parti des modeles de langage IA comme ChatGPT. En combinant des techniques comme le few-shot prompting, le framework CO-STAR et le Chain of Thought prompting, vous pouvez guider l'IA pour generer des resultats adaptes a vos besoins specifiques.

Et n'oubliez pas les templates ! Ils rendront vos prompts reutilisables et vous feront gagner du temps sur le long terme.

# Conclusion
Le prompt engineering peut sembler intimidant au debut, mais avec ces techniques simples, vous maitriserez l'art du prompt en un rien de temps. Le meilleur dans tout ca ? Vous n'avez pas besoin de formation en mathematiques ou en informatique pour commencer.

Alors lancez-vous et experimentez ces methodes pour que ChatGPT et les autres modeles de langage travaillent pour vous. Bon prompting !
