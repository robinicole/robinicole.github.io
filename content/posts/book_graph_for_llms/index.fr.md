---
title: "Visualiser des résumés de livres avec des graphes de connaissances"
date: 2024-04-25
draft: false
summary: "Transformer la sortie texte des LLM en graphes de connaissances de livres en la contraignant à un schéma"
tags: ["llm", "knowledge-graphs", "visualization"]
toc: true
thumbnailImage: "book_graph.png"
coverImage: "book_graph_darker.png"
---

{{< alert "circle-info" >}}
**Traduction automatique** — Cet article a ete traduit automatiquement depuis l'anglais. Vous pouvez consulter la version originale en anglais via le selecteur de langue en haut de la page.
{{< /alert >}}

![Le graphe de connaissances du Petit Prince](/little_prince.png)

# Introduction
ChatGPT sait lire un document et vous en rendre l'essentiel. Mais ce qu'il vous rend, c'est un mur de texte. Or le texte est une lecture à une dimension de quelque chose qui ne l'est pas : un livre est une toile de personnages, de lieux et d'idées qui se renvoient les uns aux autres. J'ai donc voulu forcer la sortie à prendre cette forme, cesser de demander de la prose au modèle pour lui demander à la place une structure de données, un ensemble de noeuds et d'arêtes que l'on peut ensuite dessiner. Le résultat ressemble au graphe ci-dessus.

Une réserve avant la démonstration. Un graphe comme celui-ci ne remplace pas la lecture du livre ; donnez-le à quelqu'un qui n'a jamais ouvert le roman et ce sera presque du bruit. Il devient utile au milieu d'un livre long et touffu, quand on a perdu le fil de qui est lié à qui et de la raison pour laquelle une scène lue 200 pages plus tôt compte maintenant. Voyez-le comme une carte que l'on consulte quand on est perdu, pas comme un substitut au voyage.

## Les graphes
Cliquez sur un lien pour en ouvrir un. Survolez un noeud ou une arête pour obtenir une description de ce qu'il représente.
- [A Tale of Two Cities](/a_tale_of_two_cities.html)
- [Dream of the Red Chamber](/dream_of_the_red_chamber.html)
- [The Alchemyst](/the_alchemyst.html)
- [The Little Prince](/the_little_prince.html)

# Implémentation
Tout le code se trouve dans [ce dépôt GitHub](https://github.com/robinicole/llm-graph). Il n'y a que trois pièces mobiles.

D'abord, décrire la forme voulue avec un modèle Pydantic : un ensemble de noeuds, chacun un concept, et un ensemble de liens entre eux. C'est le contrat que le modèle devra remplir.

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

Ensuite, demander au modèle de le remplir. Le prompt dit : résume ce livre sous forme de graphe avec 10 noeuds et 20 liens, sans boucle sur soi-même ni arête en double. C'est la bibliothèque `instructor` qui fait le vrai travail ici : elle contraint la sortie pour que vous récupériez un véritable objet `KnowledgeGraph` et non une chaîne de caractères qu'il faut parser en croisant les doigts. Les nombres 10 et 20 sont arbitraires ; c'est juste ce qui restait lisible à l'écran. Augmentez-les et le graphe vire au plat de spaghettis.

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

Enfin, le dessiner. L'objet n'est qu'un ensemble de noeuds et d'arêtes, donc n'importe quelle bibliothèque de graphes ferait l'affaire ; j'ai pris `pyvis` parce qu'elle produit un fichier HTML interactif que l'on peut déplacer et survoler.

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

Voilà toute la chaîne : un schéma, un appel contraint, une bibliothèque de tracé.

# Conclusion
La leçon dépasse les résumés de livres. Dès lors qu'on peut épingler la sortie du modèle à un schéma, le LLM cesse d'être quelque chose qu'on lit pour devenir un composant qu'on branche dans un programme. Ici le schéma était un graphe et le programme un tracé ; remplacez l'un ou l'autre et la recette tient toujours.
