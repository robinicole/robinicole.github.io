---
keywords:
 - LLM
 - prompt engineering 
metaAlignment: center
showTags: true
showPagination: true
showSocial: true
showDate: true
summary: "An overview of prompt engineering to learn how to customize ChatGPT and other AI language models to suit your specific needs. This post covers essential techniques like few-shot prompting, the CO-STAR framework, and Chain of Thought reasoning, along with practical tips for creating reusable prompt templates."
title: "Efficient LLM prompting"
lastmod: 2024-04-09
toc: true
---
{{< alert success >}}
By the end of this post, you'll have the skills to create effective, tailored prompts for ChatGPT and other AI language models. 
{{< /alert >}}
{{< alert success >}}
Please have a look at [this prompt generator](https://prompt-engineering.streamlit.app/), which generate prompts according to the principles outlined in the article.

Courtesy of Robin, the author of this article ;)
{{< /alert >}}
{{< toc >}}
# Introduction

When talking to new ChatGPT users, a common complaint is that the AI's responses don't quite match the desired tone or style for their specific use case.
The reason for this, in my opinion, is that ChatGPT and other LLMs are highly versatile, generic models, which makes it easy to adapt them to various use cases without fine-tuning.
However, this versatility can also be a drawback, as chatGPT tends to provide broad, generalized responses. To make it act the way you want, you need to guide it effectively. In the rest of this article, I will guide you through the wonderful world of prompt engineering or how to make ChatGPT work the best for you with simple tricks such as: 
- Few-shot prompting: Provide examples of the desired output to demonstrate the style, format, and content you're looking for.
- CO-STAR framework: Give detailed context about the audience and purpose of the task to ensure the LLM generates appropriate responses.
- Chain of Thought: Suggest a step-by-step reasoning path for the chatbot to follow, which can lead to more accurate and coherent outputs.

I will then discuss how you can use templates not to have to rewrite the same large prompt again and again. Now let's start and dive head first to discover few prompting methods:


{{< alert info >}}
Throughout this post, the term "LLM" (large language model) will be used to refer to AI chat models like ChatGPT and Claude.
{{< /alert >}}
# Prompting best practices

In this paragraph I describe 3 prompting method to make your prompt top-notch. Note that while those methods are described in isolation, you get the best out of them by combining them together. For example Use the CO-STAR method to describe the context of your prompt, provide few example of outputs you desire and ask the LLM to "think step by step" and you will have a solid prompt.

## Giving examples (Few Shot prompting)
**There is not better way to describe a task than giving few examples!** it is true for us humans as well as LLMs.  
Knowing that, it is natural to want to add example of typical answers to your question from the chatbot in order to have something that fits your needs. This is suggested in the best practice for prompting of [Anthropic, the creators of Claude3 which outperform chatGPT](https://docs.anthropic.com/claude/docs/use-examples) and the infamous [OpenAI](https://platform.openai.com/docs/guides/prompt-engineering/tactic-provide-examples) the creators of the famous ChatGPT. 

This approach is particularly useful for those looking to automate tasks they previously performed manually. 
*By using their past work as examples, they can train the LLM to produce output that matches their preferred style and format.*

For instance, if you're a content writer aiming to create a prompt that automatically generates articles in your writing style, you can provide the LLM with a few articles you've written before. Then, ask the AI to generate new content that mimics the tone, structure, and style of your example pieces. This technique, known as few-shot prompting, helps the LLM understand and replicate your writing voice.

{{< alert info >}}
Few shot prompting works especially well because LLMs are really generic models meaning that they are going to perform ok at a wide range of tasks. By doing few shot prompting you are providing the model some extra training to perform well at the specific task you want it to perform for you.
{{< /alert >}}

If we want to make a prompt that will be useful to a content writer we could write something like: 
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
Where we would replace the two `{}` by some actual content. This would give some examples/ guidelines to follow for the llm to write an article about the great theaters in London following our style. 

## CO-STAR Method
To further improve your prompts you can also use the CO-star method which will allow you to set up better the context in which the chatbot is behaving.

The example and explanation of the CO-STAR method is shamelessly copy/pasted from [This resource](https://github.com/dmatrix/genai-cookbook/blob/main/llm-prompts/1_how_to_use_basic_prompt.ipynb) which I strongly recommend if you know a fair bit of python.

The COStar method is a framework for structuring prompts to help LLMs better understand the context and requirements of a task. COStar stands for: 
- **C**ontext - provide the background
- **O**bjective (or Task) - define the task to be performed
- **S**tyle and **T**one - instruct a writing style. Kind of sentences; formal, informal, magazine sytle, colloqiual, or allude to a know style.
- **A**udience - who's it for?
- **R**esponse - format, Text, JSON, decorate with emojies,

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

## Chain of thought prompting
The Chain of Thought prompting method is based on the idea that encouraging an LLM to reason step by step can lead to more accurate and well-thought-out responses. By explicitly asking the model to break down its reasoning process, you're essentially guiding it to take more time to consider the problem at hand, reducing the likelihood of errors or inconsistencies.

It's intriguing to draw parallels between how humans approach problem-solving and how we can prompt LLMs to do the same. Just as we often benefit from taking a step-by-step approach to complex issues, LLMs can generate higher-quality outputs when guided to reason in a more structured manner.

Surprisingly one simple way to have make LLMs reason in this manner is to simply add `Let's think step by step.` at the end of your prompt. You could also be more specific about the way you want the LLM to tackle the problem by explicitly telling the LLM which steps you want it to perform to arrive at your answer, for example:
```
Analyze the following quote step by step: "Be the change you wish to see in the world." - Mahatma Gandhi

1. Identify the main idea of the quote.
2. Explain what "be the change" means in this context.
3. Discuss how this quote relates to personal responsibility and taking action.
4. Provide an example of how someone could apply this quote to their own life.

Analysis:
```

# Templating for your prompts
Templating is a powerful technique for making your LLM prompts more reusable, modular, and maintainable. When working with AI language models like ChatGPT, you'll often find yourself using similar prompts repeatedly, with only minor variations. This is where templating comes in handy.
By creating prompt templates, you can define a standard structure for your prompts, with placeholders for the parts that change each time. This allows you to quickly generate new prompts by simply filling in the variable components, rather than rewriting the entire prompt from scratch.

For the most straightforward templating approach, you can create a Google Doc or any other document containing your complete prompt, using placeholders to represent the variable data that will change each time the prompt is used.
For the most technical of you I would recommend to use Python either in a Jupyter notebook or using Google Colab in order to create prompt templates. I cannot recommend enough [this free course by DeepLearning.ai](https://www.deeplearning.ai/short-courses/chatgpt-prompt-engineering-for-developers/) which should give you all the basis you need to start prompt templates with python.

In the case of the few shot prompting discussed before your prompt your python code would look like 
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
and it would print on the screen a prompt to copy/paste in your favorite LLM. The great thing about this python approach is that it opens the door to web-apps if you combine it with simple Graphical interfaces such as [Streamlit](https://streamlit.io) which is an easy way to turn python code into beautiful web-apps. See [those examples](https://streamlit.io/gallery?category=llms)

# Conclusion 
In this article, I discussed basic prompting technics to customize chatGPT to your needs and then discussed how you can make your prompt reusable by using templates. One thing to bear in mind is that finding the right prompt for your use case is a trial and error process and it is likely that you will have to refine your prompts quite a few time before you have something that works for you. What I find fascinating about prompt engineering is how it is easy to get good at it if you use simple tricks without a knowledge of Mathematics or computer science except maybe some basic Python.

# About the author (Robin Nicole) 
I finished my PhD in 2017 and am now an Applied Scientist  working on digital marketing for the tourism sector. 
I am both interested and impressed by LLMs and their potential to affect intellectual labour the same way lever affected manual labour.
I love to share my passion about this topic, so if you have any question or just want to have a chat please reach out to me on my [Linkedin](https://www.linkedin.com/in/robin-nicole-phd-54929349/) or by mail robin.nicole.m@gmail.com.
# Bibliography 

## Beginner friendly
- [The prompting best practices from Claude](https://docs.anthropic.com/claude/docs/prompt-engineering)
- [The prompting best practices from OpenAI](https://platform.openai.com/docs/guides/prompt-engineering)
- [A good reference for advanced prompting](https://www.promptingguide.ai/)

## Advanced
- [A complete survey on prompt engineering (technical)](https://arxiv.org/pdf/2402.07927.pdf) 
- [Some IPython notebook for prompt engineering](https://github.com/dmatrix/genai-cookbook/tree/main/llm-prompts)
- [A maths-heavy article about prompting](https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/)