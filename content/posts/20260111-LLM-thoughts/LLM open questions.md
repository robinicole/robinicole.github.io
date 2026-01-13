---
title: LLM open questions
date: 2026-01-11
draft: false
summary: Some random thoughts and open questions on LLMs
tags:
  - ai
  - llm
series:
series_order:
toc: true
---
##  Claude code as an AI markdown editor 
 Is the difference between Claude code and the standard chatGPT interface the same difference we have between a simple markdown editor and a WYSISWYG editor such as Word. 

Claude code seems to be more of an AI interface to an LLM which can be used for a lot of tasks beyond coding and for which the knowledge for every tasks is stored inside Markdown files instead of a database.

**Reading list** https://every.to/source-code/how-to-use-claude-code-for-everyday-tasks-no-programming-required 

## Document generation
When generating documents such as presentations or diagrams, I recommend favouring plain text formats that can later be converted to your desired output format.
For presentations, ask your LLM to use Beamer, the LaTeX presentation framework. As a bonus, Claude can run the LaTeX compilation itself and debug any errors that arise. Try using it to generate presentations summarising arXiv papers.
For diagrams, Mermaid and TikZ are excellent choices. For longer text documents, LaTeX remains my preferred option.
