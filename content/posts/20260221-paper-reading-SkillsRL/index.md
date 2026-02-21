---
title: "Review: SkillsRL"
date: 2026-02-21
draft: false
summary:
tags:
  - llm
  - PaperReading
  - ai
---
In this article, I review a paper called [SkillRL](https://arxiv.org/abs/2602.08234) which I recently read.

## What the paper does

The paper's central claim is that they can teach small LLMs to use skills by combining three techniques:

1. **Experience-based skill distillation**: they use OpenAI o3 as a teacher model to distill insights from agent trajectories—both successful and failed—into compact, reusable skills. Failed trajectories are transformed into "failure lessons" rather than being discarded.
    
2. **Hierarchical skill library (SkillBank)**: skills are organised into two categories: General Skills (universal strategies applicable across all tasks) and Task-Specific Skills (category-level heuristics). General skills are always included in context, while task-specific skills are retrieved via semantic similarity using Qwen3-Embedding-0.6B—essentially a RAG mechanism.
    
3. **Recursive skill evolution**: the training pipeline has two phases. First, a cold-start supervised fine-tuning (SFT) phase where the teacher model generates skill-augmented reasoning traces to teach the base model how to use skills. Then, GRPO-based reinforcement learning begins, during which the skill library co-evolves with the policy by analysing validation failures and generating new skills to address gaps.
    

The authors compare their approach with prompt-based methods (ReAct, Reflexion), vanilla RL baselines (RLOO, GRPO), and memory-augmented RL methods (MemRL, EvolveR). SkillRL consistently outperforms all baselines: 89.9% success rate on ALFWorld (+12.3% over vanilla GRPO), 72.7% on WebShop, and 47.1% average on seven search-augmented QA tasks.

The ablation studies are informative: removing the hierarchical structure drops performance by ~13%, replacing skills with raw trajectories causes up to 25% degradation, and removing cold-start SFT causes a ~20% drop. They report 10–20× token compression compared to raw trajectory storage, though this is an expected byproduct of summarisation rather than a novel result. The more meaningful finding from the ablations is that using distilled skills actually outperforms raw trajectories by up to 25%, suggesting the compression preserves (or even enhances) useful information rather than just reducing context length.

They share their full implementation in a [GitHub repo](https://github.com/aiming-lab/SkillRL), which uses the [verl](https://github.com/volcengine/verl) library for RL training and [Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct) as the base model.

## My take

This is more of an engineering paper than a theoretical one. The three techniques are not novel in isolation: step one is learning skills from LLM history via a teacher model, step two is embedding-based retrieval to fetch relevant skills per task, and step three is SFT followed by RL with continuous skill library updates. As a result, I did not find the paper particularly compelling to read. Moreover their language is overly complicated for simple topics, for example their hierarchical skills library is not really hierarchical and just tagged skills, and skills distillation is just using a large model to learn skills from chat history. 

That said, the value here lies in the integration. The most interesting part of this work is not the paper itself but the implementation they share, which provides a working pipeline combining these existing techniques. The reported results are strong—particularly the gains on complex multi-step tasks like "PickTwo" and "Cool" where SkillRL outperforms GRPO by over 20%.

One open question is cost. This pipeline involves cold-start SFT, continuous GRPO training, and repeated calls to o3 for skill distillation and evolution. The paper doesn't provide a detailed cost breakdown. How many inferences does the small LLM need to run before the performance gains offset the training costs?

---

## Sources

- **Paper**: Xia, P., Chen, J., Wang, H., et al. (2026). _SkillRL: Evolving Agents via Recursive Skill-Augmented Reinforcement Learning_. arXiv:2602.08234. [https://arxiv.org/abs/2602.08234](https://arxiv.org/abs/2602.08234)
- **Code**: [https://github.com/aiming-lab/SkillRL](https://github.com/aiming-lab/SkillRL)
- **Base model**: Qwen2.5-7B-Instruct — [https://huggingface.co/Qwen/Qwen2.5-7B-Instruct](https://huggingface.co/Qwen/Qwen2.5-7B-Instruct)
- **RL library**: verl — [https://github.com/volcengine/verl](https://github.com/volcengine/verl)