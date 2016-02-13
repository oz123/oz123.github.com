---
title: Alternatives to systemd using debian
author: Oz Nahum Tiram
published: 2014-10-17
tags: debian, systemd
public: no
chronological: yes
kind: writing
summary: Systemd is not to be ignored. You either happy are unhappy about it. I belong to the second group. Hence, I decided to see what alternatives exist if I still want to use Debian.
---

In this post I would like to summerize some of my findings about init systems, 
and how they feel when using Debian with them. First, I'd like to give a quick 
overview of the init systems I intend to check.   
The parameters of interest for me, are whether the code is actively maintained, 
and if many users can be contacted. The second parameter is, how many lines of 
code there are in the program, and in which languages.
It is my believe that a software should be small, but feature 
complete. The more lines of code, the more complex and buggy a software can be 
(this is not a must, however). The programming language is a minor factor, but 
I do prefer software written in C compared to C++. 
And finally, licensing does matter to me. Unfortunately, there are many good 
software developers out there who don't 
believe in copyleft licensing. Personally, I prefer to write and use software 
with GPL License, because it's my believe it is the only license which pormises
my freedom as a user. It also protect me from companies stealing software (e.g
Apple...). So, here is a quick overview of the software I intend to try:

|Name|License|Last Version|LOC|
|----|-------|------------|---|
|[runit][4] |BSD   | 2014-08-10, 2.1.2 | ansic:     5692 (91.45%) sh: 532 (8.55%)|
|[nosh][5] |ISC    | 2014-10-07, 1.9   | cpp:       14997 (98.93%) sh: 162 (1.07%)|  
|[ninit][6] |GPLv2 | 2010-01-16, 0.14  | ansic: 4949 (87.79%), asm: 435 (7.72%)  sh:  253 (4.49%)|
|[minit][7] |BSD   | 2007, 0.10        | ansic:    1651 (96.83) python: 33 (1.94%) sh: 21 (1.23%)|
|[sinit][3] |BSD   | 2014-08-05, 0.9.1 | ansic: 77 (100) |
|[openrc][9] | BSD | 2014-08-22, 0.13.1| ansic: 10157 (88.96%) sh: 1233 (10.80%) perl: 28 (0.25%) 
|[freedt][10] | BSD    | 2014-09-03, 23    | ansic: 1835 (57.11%)  sh: 1378 (42.89%)|
|[finit][8]|BSD |2014-04-21, 1.9| ansic: 3454 (92.53%) sh:   279 (7.47%) |
|[restartd][2]| GPLv2 | 2013-01-23, 0.23 | ansic: 357 (57.67%) sh: 262 (42.33%) |
|[gnu dmd][11] |GPLv3| 2014-07- 07, 0.2| sh: 3996 (67.63%) lisp: 1913 (32.37%) |
|[perp][12] | BSD    | 2013-01-11, 2.07 | ansic:  14353 (97.19%) sh: 415 (2.81%)

Comments:  
Counting lines of code was done using [sloccount][1]



[1]: http://www.dwheeler.com/sloccount/
[2]: https://github.com/ajraymond/restartd
[3]: http://tools.suckless.org/sinit
[4]: http://smarden.org/runit/
[5]: http://homepage.ntlworld.com/jonathan.deboynepollard/Softwares/nosh.html
[6]: http://riemann.fmi.uni-sofia.bg/ninit/
[7]: http://www.fefe.de/minit/
[8]: http://troglobit.com/finit.html
[9]: https://github.com/OpenRC/
[10]: http://offog.org/code/freedt/
[11]: http://alpha.gnu.org/gnu/dmd/
[12]: http://b0llix.net/perp/
