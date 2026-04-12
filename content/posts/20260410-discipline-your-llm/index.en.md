---
title: "How to discipline your LLM 101"
date: 2026-04-10
draft: false
summary: "Why LLM need healthy boundaries. The principle of constraints and harnesses for reliable AI systems."
tags:
  - llm
  - ai-engineering
  - agents
  - zettelkasten
  - knowledge-graphs
featured: featured.png
---

{{< alert "circle-info" >}}
**Also on Substack** — This article was originally published on [Artificially intelligent (Substack)](https://robinnicole.substack.com/p/the-harness-and-why-constraints-matter). Read it there for discussions and additional context.
{{< /alert >}}

In this article, I dig into the best way to get an LLM to actually do what you want. My take is pretty simple: LLMs are a lot like us, nobody does their best work drowning in rules, but zero guardrails and things go off the rails fast. The sweet spot is just enough structure to keep them honest, with room to do their thing. I'll start with agentic coding, where this problem is kind of already solved, developers have had compilers, linters, and test suites keeping code in check for years. Then I'll look at how we can bring that same idea to broader tasks using knowledge graphs.

## Code harnesses: constraints compound

Start with what actually works. OpenAI built an internal product[^1] where agents wrote every line of code. A team starting with three engineers, later growing to seven, opened roughly 1,500 pull requests and generated on the order of a million lines of code, with zero manually-written implementations. The engineers stopped writing code and started writing rules: tests, metrics, architecture constraints, feedback loops. The repository became the source of truth because agents cannot reason about what is not in-context. All decisions went into versioned files. Rules were enforced by linters and CI checks, not documentation.

Why does this work ? Richard Sutton[^2], the reinforcement learning pioneer, identified the pattern decades ago: general methods that scale with computation beat hand-crafted knowledge. Chess engines defeated hand-tuned evaluation functions through brute-force search rather than learning; vision systems learned to outperform hand-designed features (edges, SIFT). The principle holds across both: scale beats manual engineering. But scaling does not fix error compounding. At 5% error per step, a 20-step task fails 64% of the time. The harness breaks this chain.

Each constraint, test, type check, linter rule, catches failures before they propagate. Linting is cheap and fast, compared to running another LLM to validate. This is why software suits agents: the constraint harness is partially built in. Type systems, compilers, test suites already constrain mechanically. An agent cannot merge code that does not compile. That instantaneous feedback loop is what makes agent work trustworthy. It mirrors financial market circuit breakers: automatic, mechanical, resistant to gaming.

What persists is not the model. Models improve and get replaced. It is the structure around the model that compounds in value. A rigorous harness survives model generations. The code that passed tests last year will constrain the next generation of agents just as effectively.

## Verification: the leverage point

But constraints are easy to get wrong. Too rigid and the system cannot adapt. Too loose and it drifts. The art is calibration, especially in verification.

DeepMind's AlphaEvolve[^3], an evolutionary coding agent, exposes this perfectly. On over 50 open problems (67 across math, geometry, combinatorics, and number theory): 75% rediscovered state-of-the-art solutions, 20% improved on known results, including advancing the kissing number in 11 dimensions from 592 to 593.

But here is the revealing failure: when verification is weak, the agent exploits it. Early on, AlphaEvolve placed points at virtually identical coordinates in geometry problems, exploiting floating-point precision issues in the linear programming solver. It was not confused. It was well-adapted to a poorly-specified problem. Terence Tao, a collaborator on the AlphaEvolve research, observed that the system found "degenerate solutions or overly forgiving scoring of approximate solutions", passing loose checks that missed the spirit of the actual problem. The fix: engineers tightened the verifier to use exact arithmetic instead of floating-point approximation.

The lesson is sharp: the generator is only as good as the verifier. When you reward something, you get more of it, including fraud. The human effort moves from "find solutions" to "design non-exploitable verification." Exact arithmetic instead of floating-point. Interval arithmetic instead of point estimates. Type-checked steps. The stronger your verifier, the smarter your agent can be. This principle scales from code to proofs to knowledge.

## The personal graph: structure as reasoning

Tests constrain code. Verifiers constrain proofs. These work by rejecting invalid states. An agent cannot submit code that does not compile. But knowledge does not work that way. You cannot compile a bad idea. There is no syntax check for truth. Yet the principle remains: structure enables reasoning.

If you keep notes with wikilinks, you have built a knowledge graph. Every note is a node. Every [[link]] is an edge. Run community detection. Clusters emerge from topology alone, without manual categorization.

This reveals something crucial: your links encode your mental model. You did not categorize notes top-down. You threaded connections bottom-up. The categories are emergent, compressed representations of your associative thinking. More important: you built a unique knowledge graph. Not curated from the internet. Built from your work.

LLMs trained on public text are interpolation machines. They blend known patterns into plausible combinations. They cannot generate what was not implicitly present in their training data. Your personal graph is orthogonal to this. The links you built, econometrics to time-series, causal inference to portfolio theory, Zettelkasten method to neural networks, are non-obvious associations the public internet does not contain. Those are yours.

An LLM with access to your graph does not synthesize from generic patterns. It traverses your specific reasoning chains. It cannot generate those connections alone. The graph supplies what the model lacks: your intellectual history, not training-set average.

## Three approaches to knowledge structure

**Vector RAG**: Embed documents, search by similarity. Fast, but retrieves local context. Cannot reason across the corpus. You get relevant passages, not synthesis.

**GraphRAG**: Extract entities from text via LLM, build a graph, cluster it, summarize clusters. Better connectivity than vector search, but extraction is expensive and hallucinations are common. You pay for that pipeline cost. Signal-to-noise degrades because the LLM makes connection errors.

**Annotated Zettelkasten**: The graph exists because you built it deliberately, one link at a time, over months. Each link is a markdown line. Wrong links get deleted. Zero extraction pipeline. Zero hallucinations. Signal-to-noise is high because you vetted every edge.

The deeper advantage: your links are annotated. Not "A → B," but "A → B because X." Each link carries why it exists. This turns the graph into an argumentative structure, not just a topology. When an LLM walks the graph, it reasons from your causal logic, not statistical correlation. The reasoning chain is transparent, traced in your own language. Exact arithmetic for knowledge.

Parse wikilinks. Run Louvain clustering. Summarize each cluster with a local LLM. Embed each note. Done.

The cost is attention: you must maintain the graph, delete bad links, keep edges annotated. The system does not pay your attention for you. It structures what you already give it. Compare the effort to standard GraphRAG: expensive entity extraction, hallucinated relationships, constant API calls. A manually-maintained graph trades automation for signal-to-noise.

## Six ways to reason over a personal graph

Index the vault. An LLM with MCP[^4] access can now:

**Reasoning chains**: Connect two arbitrary notes via shortest annotated path. "How does Zettelkasten relate to Graph Neural Networks?" The system walks:
- Zettelkasten method
- → Knowledge graph: "naturally forms one"
- → Graph Neural Networks: "GNNs operate on them"

Each step has the why. In your own words.

**Cross-domain bridges**: Community detection finds clusters spanning boundaries. The graph reveals bridges between distant intellectual areas, implicit in your linking, invisible at first glance. You did not name these. The links you built crystallized them into coherent objects. The graph made structure legible.

**Gap detection**: Domain pairs with zero connections reveal structural absences. Physics calls this percolation: a fire spreads only if tree density exceeds a threshold. Knowledge is identical. Ideas percolate across domains only if link density is sufficient. Missing links are firebreaks explaining why insights stay siloed. Filling them is not housekeeping, it is the difference between a folder and a system.

**Global synthesis**: Ask about a domain. The system identifies the relevant community and synthesizes from edge annotations and summaries. That synthesis cannot come from any single note. It requires understanding topology, how ideas relate, not what they are.

**Semantic search and neighborhoods**: Cosine similarity over embeddings, 2-3 hop walks. Simple operations that work because the graph is already curated.

**Proof generation**: Traverse the annotated path, collect each link's reasoning, compose a derivation. "Walk me from X to Y and show your work." Unlike vector search followed by summary, this produces a traced argument.

## How to build this: practical steps

**Start with what you have**: If you already maintain notes with wikilinks (Obsidian, Roam, etc.), you already have a graph. You do not need to wait until it is "complete."

**Parse and cluster**: Read the vault, extract nodes and annotated edges (lines matching `- [[Note]], annotation`). Run Louvain clustering to detect communities. This takes 30 minutes for a 1000-note vault.

**Embed and summarize**: Use a small embedding model (nomic-embed-text via Ollama, or any open model) to embed each note. Summarize each community with a local LLM or a cached API call. Cache results, summaries change slowly.

**Expose the graph**: Build an MCP tool that accepts queries like `reasoning_chain("A", "B")` or `gap_detection()`. Let an LLM traverse it during conversation.

**Annotate incrementally**: Your graph does not need perfect annotations to be useful. As you link notes, add a brief "because" line. This is not overhead, it is the difference between a folder and a system.

## Structure emerges from relationships

The Zettelkasten method[^5] is built on this observation. Neuroscience confirms it. Fleeting notes behave like short-term memory: fragile, ephemeral. Permanent notes behave like long-term memory: structured, linked, integrated. Consolidating a fleeting note means rephrasing, linking to existing knowledge.

This mirrors memory consolidation in the brain[^6]. Research shows that new memories must be interleaved within existing knowledge networks. Learning is not adding isolated information but connecting new material to existing understanding. The more elaboration and connection, the more stable the memory. A Zettelkasten is not metaphorically like a brain. It is a disciplined external process that triggers the same consolidation principles.

This structure becomes machine-queryable. An LLM with MCP[^4] access walks your graph step by step, following your annotations, rather than relying on a single retrieval pass. When it finds gaps, orphans, disconnected domains, it surfaces weaknesses invisible from inside.

Karpathy[^7] described the pattern: build a persistent wiki, knowledge compiled once and kept current, rather than re-derived on every query. A manually-maintained graph extends that with semantic annotations: each link carries why it exists. The wiki is persistent and annotated. Graph structure makes compounding legible.

Here is what an LLM cannot do: spontaneously connect your specific problem to your domain taxonomy, annotated months ago, embedded in links. That requires a graph encoding your intellectual history. The model can interpolate between known ideas from its training set. It cannot generate your non-obvious associations.

## The scaling tradeoff

This approach assumes a small-to-medium knowledge base, curated by hand. At scale, ten thousand notes or more, navigation becomes a challenge. Reasoning chains deepen. An LLM traversing long paths runs out of context. The semantic annotations that make small graphs powerful can become noise at scale.

The solution is layered retrieval: vector RAG to narrow the search space (which 100 communities are relevant?), then graph traversal within those communities. First filter by relevance, then reason over structure. This combines the scalability of embeddings with the precision of annotated edges.

Pure graph navigation without retrieval may be optimal only for boutique personal knowledge bases (100–1000 notes). Larger systems need the hybrid: semantic retrieval at the top level, annotated graph reasoning at the local level. The open question is not whether small graphs work, they do. It is whether this hybrid scales to organizational knowledge bases (100K+ notes) where different users maintain different domains.

---

## Footnotes

[^1]: OpenAI's engineering blog post on Harness Engineering - https://openai.com/index/harness-engineering/ — Documents their experiment where AI agents generated 1M+ lines of code in production. Shows the practical application of constraints to agent systems.

[^2]: Richard Sutton's essay "The Bitter Lesson" - http://www.incompleteideas.net/IncIdeas/BitterLesson.html — An influential blog post explaining why general methods that scale with computation (brute force + learning) outperform hand-crafted domain-specific knowledge over time.

[^3]: DeepMind's research on AlphaEvolve - https://deepmind.google/blog/alphaevolve-a-gemini-powered-coding-agent-for-designing-advanced-algorithms/ — An evolutionary coding agent that solved 67 open problems in mathematics, geometry, and combinatorics, including improving the kissing number in 11 dimensions.

[^4]: The Model Context Protocol (MCP) - https://modelcontextprotocol.io/ — An emerging standard for connecting AI systems to external tools and data sources, enabling structured queries over knowledge bases.

[^5]: Soenke Ahrens' "How to Take Smart Notes" - https://www.soenkeahrens.de/en/takesmartnotes — A practical guide to the Zettelkasten method, showing how to build personal knowledge systems through networked, interconnected notes.

[^6]: Research paper on memory consolidation in the brain - https://pmc.ncbi.nlm.nih.gov/articles/PMC3792618/ — Demonstrates that new memories must be integrated into existing knowledge networks for stability and retrieval.

[^7]: Andrej Karpathy's gist - https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f — Describes the principle of building persistent, compiled knowledge that persists across queries rather than being re-derived on each request.
