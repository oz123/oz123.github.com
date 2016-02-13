---
title: yes yes we can - about the Linux command yes
author: Oz Nahum
published: 2011-03-25
tags: CLI, Linux
public: yes
chronological: yes
kind: writing 
summary: Recently I started building my own [LFS](http://www.linuxfromscratch.org/), I was pretty amused by the command `yes`
---

Recently I started building my own
[LFS](http://www.linuxfromscratch.org/), I was pretty amused by the command `yes`.

However, today I found a use for that command, when I had to install a binary 
firmware on multiple servers. The binary is not editable and expects two
times 'yes' to finish the process.  
So, the solution is to run on all the computers the following command
inside a loop:  

    yes | sh binary\_firmware.exe 

Also, this is a simple example a of parallel programming and pipes.

This little trick saved me quite some typing and waiting in front of the
computer !
