---
title: "Getting Started with LLM Skills"
date: 2026-06-27
draft: false
summary: "What an agent skill is, explained for someone new to AI assistants."
tags:
  - llm
  - ai
  - agent-skills
---

Here is a useful way to picture an AI assistant. It is a very large pile of statistics about language, trained to continue text in a plausible way. That sounds reductive, and it is, but it buys you the right intuition: the model has read an enormous amount about almost everything, and knows essentially nothing about how *you* want a given job done. The general knowledge is baked in. **The specifics are not.** Every time you open the box and type, you are **paying that gap again**, re-explaining how you like an email worded, what shape a summary should take, the five steps you always run for some task.

A skill is how you **write those specifics down once** instead of repeating them. It is a small text file, a handful of rules, kept in a folder the assistant can reach. The assistant reads it only when the task calls for it, and then it follows what is written there. You are not building software and you are not retraining the model. You are leaving a note on the desk that gets picked up exactly when it is relevant. Cheap to write, and the cost of writing it amortizes over every future conversation.

The clearest example is the one that assisted me in drafting this article. I wrote it with a skill called `grill-with-docs`. Left alone, a model will happily take a vague request and generate something plausible. But plausible is not what you meant, and this skill refuses to play along. It interviews you first. Who is this for, what is the actual point, how long. One question at a time, each with a suggested answer, until the plan is genuinely pinned down. The skill itself is a few lines that amount to "ask me until it is clear, then write." A tiny constraint, and it changes the whole dynamic of the conversation.

A second one I leave switched on is `ponytail`. It tells the model to write the way a blunt, experienced colleague writes, plainly, without padding, deleting the sentence that adds nothing. Notice it adds no new capability whatsoever. It only sets a **temperament**: a bias you impose on a system that, left to its own devices, drifts toward the bland average of its training data.

Skills can also carry a real tool. If a job can be done by running a small program, the skill can bundle that program and tell the model when to reach for it. You do not need this part to get value from skills. It is just worth knowing the same mechanism scales from "write in this tone" up to "run this and read the result."

Using one is almost anticlimactic: you type its name with a slash, like `/grill-with-docs`, and the model finds the file and follows it. Many skills also turn themselves on when what you are doing matches what they are for.

So start with one. Pick a task you keep explaining the same way, write the explanation down once, and let the assistant pick it up when it applies. The interesting thing is not any single skill. It is the **shift in posture**: you stop treating the model as an oracle you interrogate, and start treating it as a system you configure.

## References

- [Anthropic, *Agent Skills* documentation](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview): the place to look for how a skill file is structured and how the assistant decides to load it.
- [Matt Pocock's skills](https://github.com/mattpocock/skills): where `grill-with-docs` and `grill-me` come from.
- [ponytail](https://github.com/DietrichGebert/ponytail): the skill that makes the model write like a blunt senior developer.
