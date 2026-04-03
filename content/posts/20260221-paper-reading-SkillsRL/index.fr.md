---
title: "Revue : SkillsRL"
date: 2026-02-21
draft: false
summary:
tags:
  - llm
  - PaperReading
  - ai
---
Dans cet article, je passe en revue un article intitule [SkillRL](https://arxiv.org/abs/2602.08234) que j'ai lu recemment.

## Ce que l'article propose

L'affirmation centrale de l'article est qu'il est possible d'enseigner a de petits LLMs l'utilisation de competences (skills) en combinant trois techniques :

1. **Distillation de competences par l'experience** : ils utilisent OpenAI o3 comme modele enseignant pour distiller des enseignements a partir des trajectoires d'agents, tant reussies qu'echouees, sous forme de competences compactes et reutilisables. Les trajectoires echouees sont transformees en "lecons d'echec" plutot que d'etre ecartees.
    
2. **Bibliotheque hierarchique de competences (SkillBank)** : les competences sont organisees en deux categories : les competences generales (strategies universelles applicables a toutes les taches) et les competences specifiques a une tache (heuristiques au niveau des categories). Les competences generales sont toujours incluses dans le contexte, tandis que les competences specifiques sont recuperees par similarite semantique a l'aide de Qwen3-Embedding-0.6B, essentiellement un mecanisme de RAG.
    
3. **Evolution recursive des competences** : le pipeline d'entrainement comporte deux phases. D'abord, une phase de fine-tuning supervise a froid (SFT) ou le modele enseignant genere des traces de raisonnement augmentees par les competences pour apprendre au modele de base comment utiliser les competences. Ensuite, l'apprentissage par renforcement base sur GRPO demarre, au cours duquel la bibliotheque de competences co-evolue avec la politique en analysant les echecs de validation et en generant de nouvelles competences pour combler les lacunes.
    

Les auteurs comparent leur approche avec des methodes basees sur les prompts (ReAct, Reflexion), des baselines RL classiques (RLOO, GRPO) et des methodes RL augmentees par la memoire (MemRL, EvolveR). SkillRL surpasse systematiquement toutes les baselines : 89,9 % de taux de reussite sur ALFWorld (+12,3 % par rapport au GRPO classique), 72,7 % sur WebShop et 47,1 % en moyenne sur sept taches de QA avec recherche augmentee.

Les etudes d'ablation sont instructives : supprimer la structure hierarchique fait chuter la performance d'environ 13 %, remplacer les competences par des trajectoires brutes entraine une degradation allant jusqu'a 25 %, et supprimer le SFT a froid provoque une baisse d'environ 20 %. Ils rapportent une compression de 10 a 20 fois des tokens par rapport au stockage de trajectoires brutes, bien que ce soit un sous-produit attendu de la synthese plutot qu'un resultat nouveau. La conclusion plus significative des ablations est que l'utilisation de competences distillees surpasse en fait les trajectoires brutes de jusqu'a 25 %, ce qui suggere que la compression preserve (voire ameliore) l'information utile plutot que de simplement reduire la longueur du contexte.

Ils partagent leur implementation complete dans un [depot GitHub](https://github.com/aiming-lab/SkillRL), qui utilise la bibliotheque [verl](https://github.com/volcengine/verl) pour l'entrainement RL et [Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct) comme modele de base.

## Mon avis

C'est davantage un article d'ingenierie qu'un article theorique. Les trois techniques ne sont pas nouvelles individuellement : la premiere etape consiste a apprendre des competences a partir de l'historique d'un LLM via un modele enseignant, la deuxieme est une recuperation basee sur les embeddings pour trouver les competences pertinentes par tache, et la troisieme est un SFT suivi de RL avec des mises a jour continues de la bibliotheque de competences. En consequence, je n'ai pas trouve l'article particulierement captivant a lire. De plus, leur langage est excessivement complexe pour des sujets simples : par exemple, leur "bibliotheque hierarchique de competences" n'est pas vraiment hierarchique mais simplement constituee de competences etiquetees, et la "distillation de competences" n'est en fait que l'utilisation d'un grand modele pour apprendre des competences a partir de l'historique de conversation.

Cela dit, la valeur reside dans l'integration. La partie la plus interessante de ce travail n'est pas l'article lui-meme mais l'implementation qu'ils partagent, qui fournit un pipeline fonctionnel combinant ces techniques existantes. Les resultats rapportes sont solides, en particulier les gains sur les taches complexes a plusieurs etapes comme "PickTwo" et "Cool" ou SkillRL surpasse GRPO de plus de 20 %.

Une question ouverte concerne le cout. Ce pipeline implique un SFT a froid, un entrainement GRPO continu et des appels repetes a o3 pour la distillation et l'evolution des competences. L'article ne fournit pas de ventilation detaillee des couts. Combien d'inferences le petit LLM doit-il executer avant que les gains de performance ne compensent les couts d'entrainement ?

---

## Sources

- **Article** : Xia, P., Chen, J., Wang, H., et al. (2026). _SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning_. arXiv:2602.08234. [https://arxiv.org/abs/2602.08234](https://arxiv.org/abs/2602.08234)
- **Code** : [https://github.com/aiming-lab/SkillRL](https://github.com/aiming-lab/SkillRL)
- **Modele de base** : Qwen2.5-7B-Instruct — [https://huggingface.co/Qwen/Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct)
- **Bibliotheque RL** : verl — [https://github.com/volcengine/verl](https://github.com/volcengine/verl)
