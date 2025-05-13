---
showDate: true
summary: "Discovering 50 shades of note-taking"
title: "About note-taking"
date: 2024-05-25
toc: true
draft: false
comments: true
---
In this article I want to discuss my approach to note taking and the recent trend of Seconds brain and digital garden. Because the second brain is somehow fashionable at the moment, there has been a lot of hype about it on youtube and this article tries to separate the base from the hype. 
## Digital gardens
Recently, I have been interested in the concept of a "digital garden"[^1] [^2] which is essentially a personal knowledge collection similar to a Wikipedia, but with key differences. A digital garden is a personal online space where individuals collect and connect their thoughts, ideas, and knowledge. Unlike Wikipedia, which aims to present information objectively for a general audience, a digital garden intentionally reflects the way its creator thinks and learns. The main advantage of a digital garden over traditional encyclopedias is that both the content and the connections between topics represent the author's personal thought patterns and learning journey. There's no attempt to standardize the presentation or organization to suit a general audience.

For readers exploring someone's digital garden, the experience goes beyond learning about specific topics. You gain insight into how the author's mind works—their thought processes, connections they make, and how they organize information. After exploring a digital garden, many readers feel they understand the creator's personality better than they understand the actual content. Digital gardens naturally showcase the multifaceted nature of their creators. You might discover someone is not only a talented software engineer but also see how they connect programming concepts to cooking techniques, environmental concerns, or other seemingly unrelated interests. This shows that people are complex, and understanding how different aspects of a person connect gives us a more complete picture of who they are. 

If you want to see by yourself I strongly recommend the two following resources: [^1] and [^2] which are some examples of digital garden.

## Building your own digital garden
After browsing few of the digital gardens listed in [^1] I started to wonder how I could build my own. This is where I discovered the "second brain"[^4]community which discusses how to build second brain which build on a hype around this domain. While I appreciate the amount of information it created, it bothers me that it lead personal knowledge to be presented as a way to achieve high productivity rather than a way to beautifully represent your knowledge. I also find it somehow disappointing that you have 50 different variation of methods to build your knowledge management system which each youtuber claims is the best. There is a similar where fitness youtuber selling you different variation of their workout to achieve the perfect physique while we all know that a simple workout (5x5 for example [^6]) can fit the need of most beginners. 
### The theory: back to basics
I decided to go back to the basics and read the original book about the Zettelkasten method which is one way of building a digital garden which was developped by Niklas Luhmann, a German sociologist who used this system to produce an enormous body of work. Luhmann’s approach wasn’t about productivity hacks or optimizing knowledge for output; it was a system for *thinking* and developing ideas over a lifetime. It stems from the fact that as opposed to the standard notes or articles where the structure of thought is linear (you write an article from the top to the bottom) even though our thought structure is highly non-linear and the system we use to ingest our idea should reflect this property. This is achieved by linking related notes together which enables the structure of the notes to emerge by itself as opposed to being imposed by a predefined hierarchy. This does marvels for creativity and research as it allows to find connections between ideas we would have thought disconnected otherwise.

To learn more about the method, I found the book of Sönke Ahrens, “How to Take Smart Notes" to be really useful for several reasons: 
1. It is gives you the building block of how to implement your own note-taking system but is not too prescriptive about it, following quote 'feed a ’man a fish and you feed him for a day; teach a man to fish and you feed him for a lifetime’. 
2. You can see it was written using knowledge stored into a zettelkasten-like knowledge graph note taking system when the author makes an analogy between one concept he explains and a semingly unrelated topic
The way I recommend reading this book is start by watching one of video in this youtube playlist [^3] to get you started and then dive into the book itself to build your own system tailored to your needs.  

Linear chain of thought 
{{< mermaid >}}
graph LR
    A["202505050: Starting Point - Zettelkasten Method"] --> B["202505051: Atomic Notes Principle"]
    B --> C["202505052: Creating Effective Note Titles"]
    C --> D["202505053: Writing Permanent Notes"]
    D --> E["202505054: Explicit Connections Between Notes"]
    E --> F["202505055: Developing Arguments Through Links"]
    F --> G["202505056: Emergent Structures in Notes"]
    G --> H["202505057: Knowledge Synthesis"]
    H --> I["202505058: Publishing From Your Zettelkasten"]
{{< /mermaid >}}

Non linear chain of thought (better)

{{< mermaid >}}
graph TD
    A["202505060: Core Concepts"] --- B["202505061: Atomic Notes"]
    A --- C["202505062: Linking Strategy"]
    A --- D["202505063: Note Organization"]
    
    B --- E["202505064: Information Chunking"]
    B --- F["202505065: Single-Idea Focus"]
    
    C --- G["202505066: Direct References"]
    C --- H["202505067: Concept Bridges"]
    C --- I["202505068: Surprising Connections"]
    
    D --- J["202505069: Folgezettel Numbering"]
    D --- K["2025050610: Tags vs. Links"]
    
    E --- L["2025050611: Cognitive Load"]
    F --- L
    
    G --- M["2025050612: Citation Practice"]
    H --- N["2025050613: Metaphorical Thinking"]
    I --- N
    I --- O["2025050614: Serendipity"]
    
    J --- P["2025050615: Sequential Thought"]
    K --- Q["2025050616: Emergent Structure"]
    
    L --- R["2025050617: Memory Enhancement"]
    M --- S["2025050618: Building on Others' Ideas"]
    N --- S
    N --- O
    O --- Q
    P --- T["2025050619: Linear Learning"]
    Q --- U["2025050620: Non-linear Creativity"]
    
    R --- V["2025050621: Knowledge Retention"]
    S --- W["2025050622: Intellectual Development"]
    T --- W
    U --- W
    V --- W
{{< /mermaid >}}
### Digital Zettelkasten
At the beginning Niklas Luhmann implemented the zettelkasten using slip note which he cross-referenced. Today however, digital offer a more convenient to store, access and browse your notes. The two software I tried to do that are Notion and Obsidian. For note taking in particular I chose Obsidian over notion for the following reason all your notes are stored in markdown i.e. in plain text, if you decide to store your notes on the obsidian server they are end-to-end encoded which means nobody except you can access them (not event he obsidien team), the linking process between notes is easier than with Notion.
To start building your your digital knowledge graph, I suggest yo watch the some youtube video [^3] to get you started and complement this with the taking smart notes book mentioned in the section [[#The theory back to basics]]. 

## Conclusion
I hope you enjoyed as much as me how the perspective of being able to build a bag of notes which are organised in a way that make sense to you which is the beauty of Zettelkasten and co. method and make them a too of choice for research and creativity. This way of storing and evaluating knowledge seems important especially in the era of LLM which are expert in interpolating idea together where I see the body of knowledge increasing faster than ever.  

## References 
[^1]: A collection of digital garden https://github.com/lyz-code/best-of-digital-gardens
[^2]: An example of a digital garden https://lyz-code.github.io/blue-book/digital_garden/  
[^3]: The result of a youtube research on Obsidian and Zettelkasten https://www.youtube.com/results?search_query=zettelkasten+and+obsidian

[^4]: Second brain on youtube https://www.youtube.com/results?search_query=second+brain 

[^6]: https://www.healthline.com/health/fitness/5x5-workout#weekly-program
