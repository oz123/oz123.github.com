---
title: Stripping EOL from output in BASH
author: Oz Nahum
published: 2011-04-15
tags: BASH, CLI, Linux
public: yes
chronological: yes
kind: writing 
summary: Sometimes you have to text process the output of many chained commands, e.g. bash command to list all dev package in Debian. The results are usually outputted with "\\n"   
---

Sometimes you have to text process the output of many chained commands,
e.g. bash command to list all dev package in Debian. The results are
usually outputted with "\\n", e.g.


    output1
    output2
    output3
    output4

If the list is long enough your screen will scroll, and it will be hard
to control the output without less. A solution is to strip the EOL marks
with echo, for example compare:

    getent passwd | cut -f 1 -d ":"

to:

    echo $(getent passwd | cut -f 1 -d ":")

