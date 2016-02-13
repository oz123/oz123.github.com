---
title: Remove all GNOME from debian - a one line
author: Oz Nahum
published: 2012-04-02
tags: Debian,CLI, GNOME
public: yes
chronological: yes
kind: writing 
summary: This one is not so easy to follow, but it works for me    ...
---

This one is not so easy to follow, but it works for me :-).

Do try only the stuff inside \`\` (back tick operator in the bash
language), to see what it does:


    $ aptitude remove `dpkg -l | grep gnome | sed 's/ii//g' \| sed 's/rc//g' | sed 's/^ *//;s/ *$//' \| sed 's/ \+ /\t/g' | cut -f 1`

