---
layout: single
title: Supporting Latex in a Jekyll Blog
---
Just after I set up this Blog with Jekyll, I wanted to use $$\LaTeX$$ to write maths but this is not shipped with the minimal-mistakes theme I use for Jekyll. A nice trick I found on the website of Ian Goodfellow  [here](http://www.iangoodfellow.com/blog/jekyll/markdown/tex/2016/11/07/latex-in-markdown.html) activates MathJax and then you can turn 

```latex
\int_0^\infty \exp(-x) {\rm d} x = 1 
```

into 

$$ \int_0^\infty \exp(-x) {\rm d} x = 1 $$ 
