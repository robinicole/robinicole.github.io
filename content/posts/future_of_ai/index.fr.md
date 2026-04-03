---
title: "Vrac de pensees : Impact de l'IA (trouver un meilleur titre plus tard)"
date: 2025-12-31
draft: true
summary: Ou nous mene la frenesie de l'IA
tags:
  - ai
  - llm
  - draft
---

{{< alert "circle-info" >}}
**Traduction automatique** — Cet article a ete traduit automatiquement depuis l'anglais. Vous pouvez consulter la version originale en anglais via le selecteur de langue en haut de la page.
{{< /alert >}}

## Vrac de pensees
Ceci est un vrac de pensees a organiser en article pour decrire ou je pense que l'IA nous emmene.

- L'effet de l'automatisation de la generation de connaissances partagera des similitudes avec l'automatisation precedente du travail manuel, et nous observerons deux classes distinctes de connaissances/contenus : 1. Des connaissances basiques a faible valeur ajoutee, generees avec une intervention humaine minimale (l'equivalent IKEA de la connaissance) 2. Des connaissances premium, soigneusement generees par des humains (l'equivalent des meubles artisanaux)

- Les connaissances seront generees a une vitesse croissante dans une boucle auto-entretenue ou la R&D pour creer de nouveaux LLMs plus puissants sera stimulee par les nouvelles capacites des LLMs

{{< mermaid >}}
%%{init: {'theme':'base', 'themeVariables': { 'fontSize':'32px'}}}%%
flowchart TD
    A[Knowledge Generation Automation] --> B[Two Classes of Content]
    
    B --> C[Low Added Value]
    C --> C1[Minimal human intervention]
    C1 --> C2[IKEA furniture equivalent]
    
    B --> D[Premium Knowledge]
    D --> D1[Carefully crafted by humans]
    D1 --> D2[Handcrafted furniture equivalent]
    
    A --> E[Self-Sustaining Loop]
    E --> F[Faster knowledge generation]
    F --> G[Stimulates R&D for more powerful LLMs]
    G --> H[New LLM capabilities]
    H --> F
{{< /mermaid >}}



## Ressources
- https://chrisloy.dev/post/2025/12/30/the-rise-of-industrial-software article tres interessant qui trace un parallele entre l'automatisation actuelle des connaissances par l'IA et la precedente automatisation dans le textile, qui a conduit a avoir deux categories de biens : faible effort / faible valeur (crees avec une forte automatisation) vs. effort eleve / haute valeur (fabriques manuellement et avec soin). Ils soutiennent que dans le cas particulier du logiciel, la R&D rendra la niche artisanale tres precieuse.

{{< mermaid >}}
%%{init: {'theme':'base', 'themeVariables': { 'fontSize':'32px'}}}%%
flowchart TD
    A[Traditional Software] --> B[Craft-based, Expensive, Skilled Labor]
    B --> C[AI Coding Tools]
    C --> D[Industrialization]
    
    D --> E[First Order Effects]
    E --> E1[Lower barriers]
    E --> E2[More competition]
    E --> E3[Faster change]
    
    D --> F[Second Order Effects]
    F --> F1[Disposable Software]
    F1 --> F2[Low cost, low value]
    
    F2 --> G[Jevons Paradox]
    G --> G1[Efficiency leads to more consumption]
    
    G1 --> H[Historical Warning: Food Industry]
    H --> H1[Promised abundance]
    H1 --> H2[Delivered obesity crisis]
    
    D --> I[Future Paths]
    I --> I1[Mass Production]
    I --> I2[Artisan Niche]
    I --> I3[Innovation]
    
    I3 --> J[Cycle of Progress]
    J --> J1[Innovation]
    J1 --> J2[Industrialization]
    J2 --> J3[New Foundation]
    J3 --> J1
    
    J --> K[Open Question]
    K --> K1[Who maintains software no one owns?]
{{< /mermaid >}}
