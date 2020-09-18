---
title:  "Cheatsheets"
layout: single
permalink: /cheatsheets/
author_profile: true
toc: true
comments: true
---
> A collection of code snippets
 
# Python

- Running file as a package 
```bash
python -m package
```
- Add a progress bar with `tqdm`
```python
from time import 
from tqdm import tqdm 
for _ in tqdm(range(100)):
     sleep(0.01) 
```

# Spark 

# Bash

- Write command output to a file and write it on `stdout`
```bash
./command_to_run 2>&1 | tes output_file.log
```

# Git
- Checkout last branch: 
```python
git checkout -
```

# Scala
- Define a function 
```scala
def mul(m: Int): Int = m * 1
```
