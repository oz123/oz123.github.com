---
title: Dictionaries in bash scripts - it is possible
author: Oz Nahum Tiram
published: 2015-06-11
tags: bash, linux
public: yes
chronological: yes
kind: writing
summary: Apparently, bash offeres assosiative arrays, similar to Python dictionaries
---

Here is something new I learned. Modern unix shells like bash (>4.x) or zsh, 
offer associative arrays, sometimes called maps, or dictionaries (in Python).

In the past, I worked on legacy systems (RHEL4,5) series which offered BASH 3.x, 
where this didn't exist, and since then I do most of my programming in Python. 
Never the less, it was a pleasant surprise to find this after the first quarter 
of the bash man page:

```
   Bash  provides  one-dimensional  indexed and associative array variables. 
   ...
   Associative arrays are created using declare -A name.
```

Here is an example:

```shell
$ declare -A aa
$ aa[hello]=world
$ echo ${aa[hello]} 
world
$ aa[hello world]="from bash"
$ echo ${aa[hello world]} 
from bash
```

You can read more about this in your nearest `man bash`. 
