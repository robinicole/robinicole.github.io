---
title: "Visualiser des résumés de livres avec des graphes de connaissances grâce à ChatGPT"
date: 2024-04-25
draft: false
summary: "Créer des graphes de connaissances de livres visuellement attrayants et informatifs grâce à la puissance des grands modèles de langage"
tags: ["llm", "knowledge-graphs", "visualization"]
toc: true
thumbnailImage: "book_graph.png"
coverImage: "book_graph_darker.png"
---

{{< alert "circle-info" >}}
**Traduction automatique** — Cet article a ete traduit automatiquement depuis l'anglais. Vous pouvez consulter la version originale en anglais via le selecteur de langue en haut de la page.
{{< /alert >}}

# Les graphes créés dans le cadre de ce projet
- [A Tale of Two Cities](/a_tale_of_two_cities.html)
- [Dream of the Red Chamber](/dream_of_the_red_chamber.html)
- [The Alchemyst](/the_alchemyst.html)
- [The Little Prince](/the_little_prince.html)

Une image du graphe de connaissances créé pour Le Petit Prince

![Une image d'un graphe](/little_prince.png)

# Introduction
Les grands modèles de langage comme ChatGPT ont la capacité remarquable d'extraire des informations de documents et de les présenter dans un format concis et facile à comprendre. Cependant, la sortie standard de ChatGPT se limite au texte et aux images. Dans cet article, nous allons explorer comment exploiter les capacités de ChatGPT et contraindre sa sortie pour créer des graphes de connaissances visuellement attrayants qui résument des livres, à l'image de [ce graphe qui résume le célèbre « A Tale of Two Cities »](/a_tale_of_two_cities.html).

La raison pour laquelle j'ai voulu explorer les visualisations par graphes de connaissances est qu'elles peuvent constituer un outil pédagogique complémentaire à la lecture d'un livre. Il est important de noter que ces graphes ne sont pas destinés à remplacer l'acte de lire en lui-même, car ils ne peuvent pas capturer pleinement la profondeur et les nuances du texte. En fait, **le graphe peut ne pas être très utile sans le contexte et les connaissances acquis en lisant réellement le livre**.
Cependant, les graphes de connaissances peuvent **servir d'aide précieuse, surtout lorsque les lecteurs se sentent perdus ou submergés au milieu d'un livre complexe**. En offrant une vue d'ensemble des concepts principaux et de leurs relations, ces visualisations peuvent aider les lecteurs à voir le livre dans sa globalité et faciliter la compréhension de la façon dont les différentes parties du livre s'articulent et contribuent au message ou au thème général.

## Exemples de graphes de connaissances
Voici quelques exemples de graphes de connaissances pour des livres bien connus. Cliquer sur un lien affichera le graphe de connaissances correspondant. Lorsque vous survolez un noeud ou un lien dans le graphe, vous verrez une description de cet élément particulier, fournissant plus de contexte et d'informations sur sa signification au sein de la narration ou de la structure du livre.
- [A Tale of Two Cities](/a_tale_of_two_cities.html)
- [Dream of the Red Chamber](/dream_of_the_red_chamber.html)
- [The Alchemyst](/the_alchemyst.html)
- [The Little Prince](/the_little_prince.html)

Dans la suite de cet article, je décrirai la méthode pour générer les graphes ci-dessus :

# Implémentation
Le code pour générer des graphes de connaissances à partir de résumés de livres avec ChatGPT est disponible dans [ce dépôt GitHub](https://github.com/robinicole/llm-graph). Le processus est simple et comprend les étapes suivantes :

1. Définir un modèle Pydantic pour spécifier la structure du graphe de connaissances. Le graphe est composé de noeuds et de liens, où chaque noeud représente un concept principal et chaque lien représente une connexion entre deux concepts. Le modèle Pydantic est défini comme suit :

```python
from pydantic import BaseModel
from typing import List

class Node(BaseModel):
    node_id: int
    name: str
    description: str

class Link(BaseModel):
    link_id: int
    link_name: str
    node_id_from: int
    node_id_to: int
    link_description: str

class KnowledgeGraph(BaseModel):
    concepts: List[Node]
    links: List[Link]
    name: str
```

2. Demander à ChatGPT de générer un objet JSON conforme au modèle Pydantic spécifié. Le prompt demande à ChatGPT de résumer un livre donné sous forme de graphe de connaissances avec 10 noeuds et 20 liens, en s'assurant que le graphe résultant soit visuellement attrayant et fournisse un bon aperçu du livre. La bibliothèque `instructor` est utilisée pour contraindre la sortie de ChatGPT à correspondre au modèle Pydantic.

```python
from functools import lru_cache
from openai import OpenAI
from typing import List
import instructor

@lru_cache(maxsize=None)
def get_knowledge_graph_object(
    book_title: str,
    model: str = 'gpt-4-turbo',
    client = instructor.from_openai(OpenAI())
) -> KnowledgeGraph:
    return client.chat.completions.create(
        model=model,
        response_model=KnowledgeGraph,
        messages=[
            {"role": "system", "content": "You are an avid reader and you summarize books in knowledge graphs and make it entertaining"},
            {"role": "user", "content": f"""Summarize the book {book_title} in the graph given as type. Each of the nodes in the graph represents one main concept of the book. Each of the links represents a connection between two main concepts. The graph should have 10 nodes and 20 links. The resulting graph should be visually appealing and give a good global understanding of the book it summarizes. Take some time and reason step by step before creating the graph object to make a graph that will be easy to display. A node should not have self-loops and there should not be loops between two nodes. The graph should give the reader a good summary of the book."""}
        ],
    )
```

3. Parser le modèle Pydantic généré et le visualiser sous forme de graphe de connaissances avec la bibliothèque `pyvis`.

```python
from pyvis.network import Network

def draw_kg_with_pyvis(knowledge_graph: KnowledgeGraph):
    net = Network(notebook=True, directed=True, width="800px", height="600px")

    # Add nodes to the network
    for node in knowledge_graph.concepts:
        net.add_node(node.node_id, label=node.name, title=node.description.replace('.', '.\n'), shape="box")

    # Add edges to the network
    for link in knowledge_graph.links:
        net.add_edge(link.node_id_from, link.node_id_to, label=link.link_name, title=link.link_description.replace('.', '.\n'))

    # Set layout options
    net.barnes_hut(gravity=-1000, overlap=100)

    # Display the network
    return net.show(f"{knowledge_graph.name}.html")
```

En suivant ces étapes, vous pouvez exploiter la puissance de ChatGPT pour générer des graphes de connaissances informatifs et visuellement attrayants qui résument des livres. La bibliothèque `instructor` garantit que la sortie générée respecte le modèle Pydantic spécifié, tandis que la bibliothèque `pyvis` permet la visualisation du graphe de connaissances dans un format interactif et convivial.

# Conclusion
Dans cet article, j'ai partagé avec vous des choses intéressantes que l'on peut faire en combinant la puissance de la génération structurée et des bibliothèques de visualisation Python pour créer de jolies visualisations alimentées par ChatGPT. N'hésitez pas à consulter les visualisations que j'ai déjà créées ici :
- [A Tale of Two Cities](/a_tale_of_two_cities.html)
- [Dream of the Red Chamber](/dream_of_the_red_chamber.html)
- [The Alchemyst](/the_alchemyst.html)
- [The Little Prince](/the_little_prince.html)
