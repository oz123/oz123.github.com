---
title: Remove all Development packages from Debian 
author: Oz Nahum
published: 2012-04-02
tags: Debian,CLI, Linux
public: yes
chronological: yes
kind: writing 
summary: Another cool one liner to remove all development packages to clean your Debian.
---

Another cool one liner to remove all development packages to clean your
Debian.


    # aptitude remove `dpkg -l | grep -e \-dev | sed 's/ii//g' \| sed 's/rc//g' | sed 's/^ *//;s/ *$//' \| sed 's/ \+ /\t/g' | cut -f 1`

