---
title: Git tip - git describe  
author: Oz Nahum
published: 2013-12-08
tags: git, Programming, pwman3
public: yes
chronological : yes
kind: writing 
summary: Earlier I posted a tip how to count commits between tags, this post suggests a better way to do it
---

Apparently git comes with batteries included. If you want to track the 'distance' from a certain tag 
all you have to do it use the command `git describe`:

```bash
[3] oz123@debian:~/software/pwman3  [master]  $ git describe 
v0.4.3-7-g75ae633
```
The output is easy to understand: 

```
    <tag>-<N-Commits>-<hash of the latest commit>
```
To see this output you first have to annotate or sign you tags, so check the man page 
of `git-tag`.


