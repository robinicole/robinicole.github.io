---
keywords:
 - LLM
 - prompt engineering 
metaAlignment: center
showTags: true
showPagination: true
showSocial: true
showDate: true
draft: true
summary: "A quick and simple introduction prompt engineering or how to take advantage of chatbots such as ChatGPT"
title: "Introduction to prompt engineering (Beginner)"
lastmod: 2024-04-13
toc: true
# thumbnailImage: "prompting_cover.webp"
# coverImage: "prompting_cover.webp"

---

By the end of this post, you'll know how to create effective prompts for ChatGPT and other AI language models, even if you're new to the topic!
Please have a look at [this prompt generator](https://robin-nicole.streamlit.app/), which generate prompts according to the principles outlined in the article.

Courtesy of Robin, the author of this article ;)
You can find a more detailed version of this article aimed at more ai-experienced audience [here]({{< ref "llm_prompting.md" >}})
# What is Prompt Engineering?
Prompt engineering is the process of designing the right prompts (instructions) to get the desired output from AI language models like ChatGPT.

Think of it like giving a friend directions to your house. If you give them clear, specific instructions, they'll find it easily. But if your directions are vague or confusing, they might get lost. It's the same with AI models - the better your prompts, the better the results!

# Why is Prompt Engineering Important?
ChatGPT and other language models are incredibly versatile, which is great because it means they can be used for all sorts of tasks. However, this also means their responses can be quite generic if you don't guide them properly.

Imagine asking a friend to bake you a cake without giving them a recipe. They might make something tasty, but it might not be the specific flavor or style you were craving. Prompt engineering is like giving the AI a detailed recipe to follow.

# Basic Prompt Engineering Techniques
Here are three simple techniques you can use to craft effective prompts:

- **Few-Shot Prompting:** Give examples of what you want!
Just like showing a friend photos of the cake you want, give the AI a few examples of the desired output.
This helps the model understand the style, format, and content you're looking for.
- **CO-STAR Framework:** Set the stage for the AI.
Provide context (C) about the background of your task.
Clearly define the objective (O) or task to be performed.
Specify the style and tone (ST) you want, like formal, casual, or specific to a certain audience.
Describe the intended audience (A) for the output.
Outline the format you want for the AI's response (R).

- **Chain of Thought Prompting:** Encourage step-by-step thinking.
Just like we solve complex problems by breaking them down into steps, you can ask the AI to do the same.
Prompts like "Let's think about this step by step" or outlining specific steps for the AI to follow can lead to more accurate, well-reasoned responses.

# Prompt Templates: Your Secret Weapon
Once you've crafted the perfect prompt for a task, you might want to use it again in the future with small tweaks. That's where prompt templates come in!

Templates allow you to create a standard structure for your prompts, with placeholder spots for info that changes each time. This saves you from rewriting the whole prompt whenever you need it.

You can create templates in a regular document or get fancy and use Python code to automatically fill in the placeholders. But don't worry if coding isn't your thing - even a simple document template can be a huge time-saver!

# Putting It All Together
Effective prompt engineering is the key to getting the most out of AI language models like ChatGPT. By combining techniques like few-shot prompting, the CO-STAR framework, and Chain of Thought prompting, you can guide the AI to generate outputs tailored to your specific needs.

And don't forget about templates! They'll make your prompts reusable and save you time in the long run.

# Conclusion
Prompt engineering might seem daunting at first, but with these simple techniques, you'll be crafting top-notch prompts in no time. The best part? You don't need a background in math or computer science to get started.

So go ahead and experiment with these methods to make ChatGPT and other language models work for you. Happy prompting!