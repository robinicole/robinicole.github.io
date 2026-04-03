---
title: "Introduction au prompt engineering (Avancé)"
date: 2024-04-09
draft: true
summary: "Un panorama du prompt engineering pour apprendre à personnaliser ChatGPT et d'autres modèles de langage IA selon vos besoins spécifiques. Cet article couvre des techniques essentielles comme le few-shot prompting, le framework CO-STAR et le raisonnement en chaîne de pensée, ainsi que des conseils pratiques pour créer des templates de prompts réutilisables."
tags: ["llm", "prompt-engineering"]
series: ["Prompt Engineering"]
series_order: 2
toc: true
---

{{< alert "circle-info" >}}
**Traduction automatique** — Cet article a ete traduit automatiquement depuis l'anglais. Vous pouvez consulter la version originale en anglais via le selecteur de langue en haut de la page.
{{< /alert >}}
À la fin de cet article, vous aurez les compétences nécessaires pour créer des prompts efficaces et sur mesure pour ChatGPT et d'autres modèles de langage IA.
N'hésitez pas à jeter un œil à [ce générateur de prompts](https://robin-nicole.streamlit.app/), qui génère des prompts selon les principes décrits dans cet article.

Avec les compliments de Robin, l'auteur de cet article ;)
Vous pouvez trouver une version plus simple de cet article destinée à un public débutant [ici]({{< ref "intro-to-prompt-engineering.md" >}})
# Introduction

En discutant avec de nouveaux utilisateurs de ChatGPT, une plainte récurrente est que les réponses de l'IA ne correspondent pas tout à fait au ton ou au style souhaité pour leur cas d'usage spécifique.
La raison, à mon avis, est que ChatGPT et les autres LLMs sont des modèles très polyvalents et généralistes, ce qui permet de les adapter facilement à différents cas d'usage sans fine-tuning.
Cependant, cette polyvalence peut aussi être un inconvénient, car ChatGPT a tendance à fournir des réponses larges et généralisées. Pour le faire agir comme vous le souhaitez, vous devez le guider efficacement. Dans la suite de cet article, je vais vous guider à travers le monde merveilleux du prompt engineering, ou comment tirer le meilleur parti de ChatGPT avec des astuces simples telles que :
- Few-shot prompting : Fournir des exemples du résultat souhaité pour illustrer le style, le format et le contenu recherchés.
- Framework CO-STAR : Donner un contexte détaillé sur l'audience et l'objectif de la tâche pour s'assurer que le LLM génère des réponses appropriées.
- Chaîne de pensée (Chain of Thought) : Suggérer un cheminement de raisonnement étape par étape que le chatbot doit suivre, ce qui peut mener à des résultats plus précis et cohérents.

Je discuterai ensuite de la façon dont vous pouvez utiliser des templates pour ne pas avoir à réécrire le même long prompt encore et encore. Commençons maintenant et plongeons tête la première pour découvrir quelques méthodes de prompting :


Tout au long de cet article, le terme « LLM » (large language model) sera utilisé pour désigner les modèles de chat IA comme ChatGPT et Claude.
# Bonnes pratiques de prompting

Dans ce paragraphe, je décris 3 méthodes de prompting pour rendre vos prompts au top. Notez que bien que ces méthodes soient décrites séparément, vous en tirez le meilleur en les combinant ensemble. Par exemple, utilisez la méthode CO-STAR pour décrire le contexte de votre prompt, fournissez quelques exemples des résultats souhaités et demandez au LLM de « réfléchir étape par étape » et vous aurez un prompt solide.

## Donner des exemples (Few Shot prompting)
**Il n'y a pas de meilleure façon de décrire une tâche que de donner quelques exemples !** C'est vrai pour nous les humains comme pour les LLMs.
Sachant cela, il est naturel de vouloir ajouter des exemples de réponses typiques à votre question pour obtenir quelque chose qui corresponde à vos besoins. C'est recommandé dans les bonnes pratiques de prompting d'[Anthropic, les créateurs de Claude3 qui surpasse ChatGPT](https://docs.anthropic.com/claude/docs/use-examples) et du fameux [OpenAI](https://platform.openai.com/docs/guides/prompt-engineering/tactic-provide-examples), les créateurs du célèbre ChatGPT.

Cette approche est particulièrement utile pour ceux qui cherchent à automatiser des tâches qu'ils effectuaient auparavant manuellement.
*En utilisant leur travail passé comme exemples, ils peuvent entraîner le LLM à produire des résultats qui correspondent à leur style et format préférés.*

Par exemple, si vous êtes rédacteur de contenu et que vous souhaitez créer un prompt qui génère automatiquement des articles dans votre style d'écriture, vous pouvez fournir au LLM quelques articles que vous avez écrits auparavant. Puis demandez à l'IA de générer du nouveau contenu qui imite le ton, la structure et le style de vos exemples. Cette technique, connue sous le nom de few-shot prompting, aide le LLM à comprendre et reproduire votre voix d'écriture.

Le few-shot prompting fonctionne particulièrement bien car les LLMs sont des modèles vraiment généralistes, ce qui signifie qu'ils vont performer correctement sur un large éventail de tâches. En faisant du few-shot prompting, vous fournissez au modèle un entraînement supplémentaire pour exceller dans la tâche spécifique que vous voulez qu'il accomplisse pour vous.

Si nous voulons créer un prompt utile à un rédacteur de contenu, nous pourrions écrire quelque chose comme :
```xml
<example>
Text: Write an article about Levi's success
Output: {This is an article about Levi's success}
</example>
<example>
Text: Write an article about The best restaurant in London
Output: {This is an article about the best restaurant in London}
</example>
...
Text: Write an article about five great theater places in London
Output:
```
Où nous remplacerions les deux `{}` par du contenu réel. Cela donnerait des exemples/directives à suivre pour que le LLM rédige un article sur les grands théâtres de Londres en suivant notre style.

## Méthode CO-STAR
Pour améliorer encore vos prompts, vous pouvez aussi utiliser la méthode CO-STAR qui vous permettra de mieux définir le contexte dans lequel le chatbot opère.

L'exemple et l'explication de la méthode CO-STAR sont honteusement copiés-collés depuis [cette ressource](https://github.com/dmatrix/genai-cookbook/blob/main/llm-prompts/1_how_to_use_basic_prompt.ipynb) que je recommande vivement si vous connaissez un peu Python.

La méthode COStar est un framework pour structurer les prompts afin d'aider les LLMs à mieux comprendre le contexte et les exigences d'une tâche. COStar signifie :
- **C**ontexte (Context) - fournir le contexte
- **O**bjectif (Objective/Task) - définir la tâche à accomplir
- **S**tyle et **T**on (Style & Tone) - indiquer un style d'écriture. Type de phrases ; formel, informel, style magazine, familier, ou faire allusion à un style connu.
- **A**udience - à qui c'est destiné ?
- **R**éponse (Response) - format, Texte, JSON, décorer avec des emojis,

```
# CONTEXT #
I want to share our company's new product feature for
serving open source large language models at the lowest cost and lowest
latency. The product feature is Anyscale Endpoints, which serves all Llama series
models and the Mistral series too.

# OBJECTIVE #
Create a LinkedIn post for me, which aims at Gen AI application developers
to click the blog link at the end of the post that explains the features,  
a handful of how-to-start guides and tutorials, and how to register to use it, 
at no cost.

# STYLE #

Follow the simple writing style common in communications aimed at developers 
such as one practised and advocated by Stripe.

Be perusaive yet maintain a neutral tone. Avoid sounding too much like sales or marketing
pitch.

# AUDIENCE #
Tailor the post toward developers seeking to look at an alternative 
to closed and expensive LLM models for inference, where transparency, 
security, control, and cost are all imperatives for their use cases.

# RESPONSE #
Be concise and succinct in your response yet impactful. Where appropriate, use
appropriate emojies.
```

## Prompting par chaîne de pensée (Chain of Thought)
La méthode de prompting par chaîne de pensée repose sur l'idée qu'encourager un LLM à raisonner étape par étape peut mener à des réponses plus précises et mieux réfléchies. En demandant explicitement au modèle de décomposer son processus de raisonnement, vous le guidez essentiellement à prendre plus de temps pour considérer le problème en question, réduisant la probabilité d'erreurs ou d'incohérences.

Il est fascinant de faire des parallèles entre la façon dont les humains abordent la résolution de problèmes et la façon dont nous pouvons inciter les LLMs à faire de même. Tout comme nous bénéficions souvent d'une approche étape par étape pour les problèmes complexes, les LLMs peuvent générer des résultats de meilleure qualité lorsqu'ils sont guidés pour raisonner de manière plus structurée.

De façon surprenante, un moyen simple de faire raisonner les LLMs de cette manière est simplement d'ajouter `Let's think step by step.` à la fin de votre prompt. Vous pourriez aussi être plus spécifique sur la façon dont vous voulez que le LLM aborde le problème en lui indiquant explicitement quelles étapes vous voulez qu'il suive pour arriver à votre réponse, par exemple :
```
Analyze the following quote step by step: "Be the change you wish to see in the world." - Mahatma Gandhi

1. Identify the main idea of the quote.
2. Explain what "be the change" means in this context.
3. Discuss how this quote relates to personal responsibility and taking action.
4. Provide an example of how someone could apply this quote to their own life.

Analysis:
```

# Créer des templates pour vos prompts
Le templating est une technique puissante pour rendre vos prompts LLM plus réutilisables, modulaires et maintenables. Lorsque vous travaillez avec des modèles de langage IA comme ChatGPT, vous vous retrouvez souvent à utiliser des prompts similaires de façon répétée, avec seulement des variations mineures. C'est là que le templating entre en jeu.
En créant des templates de prompts, vous pouvez définir une structure standard pour vos prompts, avec des espaces réservés pour les parties qui changent à chaque fois. Cela vous permet de générer rapidement de nouveaux prompts en remplissant simplement les composantes variables, plutôt que de réécrire le prompt entier à chaque fois.

Pour l'approche de templating la plus simple, vous pouvez créer un Google Doc ou tout autre document contenant votre prompt complet, en utilisant des espaces réservés pour représenter les données variables qui changeront à chaque utilisation du prompt.
Pour les plus techniques d'entre vous, je recommande d'utiliser Python, que ce soit dans un Jupyter notebook ou via Google Colab, pour créer des templates de prompts. Je ne peux que recommander [ce cours gratuit de DeepLearning.ai](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/) qui devrait vous donner toutes les bases nécessaires pour commencer à créer des templates de prompts avec Python.

Dans le cas du few-shot prompting discuté précédemment, votre code Python ressemblerait à ceci :
```python
prompt_template = """
<example>
Text: Write an article about Levi's success
Output: <This is an article about Levi's success>
</example>
<example>
Text: Write an article about The best restaurant in London
Output: <This is an article about the best restaurant in London>
</example>
...
Text: Write an article about {article_topic}
Output:
"""
print(prompt_template.format(article_topic="The seven wonders of the world"))
```
et cela afficherait à l'écran un prompt à copier-coller dans votre LLM préféré. L'avantage de cette approche Python est qu'elle ouvre la porte aux applications web si vous la combinez avec des interfaces graphiques simples comme [Streamlit](https://streamlit.io), qui est un moyen facile de transformer du code Python en de belles applications web. Voir [ces exemples](https://streamlit.io/gallery?category=llms)

# Conclusion
Dans cet article, j'ai présenté des techniques de base de prompting pour personnaliser ChatGPT à vos besoins, puis j'ai discuté de la façon dont vous pouvez rendre vos prompts réutilisables en utilisant des templates. Une chose à garder à l'esprit est que trouver le bon prompt pour votre cas d'usage est un processus d'essai-erreur et il est probable que vous devrez affiner vos prompts un certain nombre de fois avant d'avoir quelque chose qui fonctionne pour vous. Ce que je trouve fascinant dans le prompt engineering, c'est à quel point il est facile de devenir bon en utilisant des astuces simples, sans connaissances en mathématiques ou en informatique, à part peut-être un peu de Python de base.

# À propos de l'auteur (Robin Nicole)
J'ai terminé mon doctorat en 2017 et je suis maintenant Applied Scientist, travaillant sur le marketing digital pour le secteur du tourisme.
Je suis à la fois intéressé et impressionné par les LLMs et leur potentiel à transformer le travail intellectuel de la même manière que le levier a transformé le travail manuel.
J'adore partager ma passion pour ce sujet, donc si vous avez des questions ou si vous voulez simplement discuter, n'hésitez pas à me contacter sur mon [Linkedin](https://www.linkedin.com/in/robin-nicole-phd-54929349/) ou par mail robin.nicole.m@gmail.com.
# Bibliographie

## Pour débutants
- [Les bonnes pratiques de prompting de Claude](https://docs.anthropic.com/claude/docs/prompt-engineering)
- [Les bonnes pratiques de prompting d'OpenAI](https://platform.openai.com/docs/guides/prompt-engineering)
- [Une bonne référence pour le prompting avancé](https://www.promptingguide.ai/)

## Avancé
- [Un survey complet sur le prompt engineering (technique)](https://arxiv.org/pdf/2402.07927.pdf)
- [Des notebooks IPython pour le prompt engineering](https://github.com/dmatrix/genai-cookbook/tree/main/llm-prompts)
- [Un article mathématiquement dense sur le prompting](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/)
