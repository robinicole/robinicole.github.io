---
title: Automatically reload your modules in a Python notebook
layout: single
header: 
  image: /assets/images/header.jpg
---

One thing which can be really anoying in a Jupyter notebook is that *the changes you made in a module are not effective until you restart your notebook*. 

## Example 

For example 

If you have a notebook wtih this code

```python
from a_random_module import print_greeting
print_greeting()
>>> Hello
```

but then you modify the function `print_greeting` inside `a_random_module` to return `Goodbye`, you will still get 

```python
from a_random_module import print_greeting
print_greeting()
>>> Hello 
```

and you will have to restart the notebook to see the changes you made to `a_random_module` effective. 

## Automatically reload modules with the `autoreload` magic command

To automatically reload your modules once they have been modified, you just need to add two magic commands on the top of your notebook: 

```python
%load_ext autoreload
%autoreload 2
from a_random_module import print_greeting
print_greeting()
```



`%load_ext autoreload ` loads the autoreload module and `%autoreload 2` activate autoreload as it is explained in the documentation of IPython [here](https://ipython.readthedocs.io/en/stable/config/extensions/autoreload.html).  With those two magic commands *any changes you will make to the `print_greeting` command will be "seen" by your jupyter notebook*. 

## Sources 

[1] [A blog article](https://support.enthought.com/hc/en-us/articles/204469240-Jupyter-IPython-After-editing-a-module-changes-are-not-effective-without-kernel-restart)

[2] [The ipython documentation](https://ipython.readthedocs.io/en/stable/config/extensions/autoreload.html) 
