---
title: VIM Quicky - set tabs and spaces behaviour for different files 
author: Oz Nahum
published: 2012-02-24
tags: Programming, VIM, C, Python
public: yes
chronological: yes
kind: writing 
summary: Never really bothered me before, because I only used Python and C, so I always replaces tabs with spaces.   
---

Never really bothered me before, because I only used Python and C, so I
always replaces tabs with spaces.
However, with more C programming lately, I needed to start working with
Makefiles. These **require** tabs instead of spaces.
So here is how to. In the end of my `.vimrc` file I put:


    " python python pyhton
    " convert tabs to spaces before writing python files or C files
    autocmd! bufwritepre *.py,*.c,*.h set expandtab | retab! 4
    
    " convert spaces to tabs when reading python file or C files
    autocmd! bufreadpost *.py,*.c,*.h set noexpandtab | retab! 4

Et viola, not so complicated!
