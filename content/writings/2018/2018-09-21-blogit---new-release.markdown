---
title: blogit - new release
author: Oz Nahum Tiram
published: 2018-09-21
tags: python, news
public: yes
chronological: yes
kind: writing
summary: >
  After a long development hiatus I am releasing a new version of blogit
---

[blogit.py](https://github.com/oz123/blogit) is the engine that powers this humble
blog. It's written in Python, and like all my software development efforts it
strives to be minimal with two aspects. The first, include the smallest number
of features that make the software useful, but not obsolete. The second aspect
of minimalism is as little code as possible.
This version has all the features of the previous versions but it's a bit less
code:

```
~/Software/blogit [±|tag:v0.3 ✓|] $ wc -l *.py blogit/*.py
   35 conf.py
  312 setup.py
  605 blogit/blogit.py
    0 blogit/__init__.py
  952 total
otiram@yoni:~/Software/blogit [±|tag:v0.3 ✓|] $ git checkout v0.4
Previous HEAD position was fb77c31 Bump version
HEAD is now at dd47f46 Tidy up a bit, give a hint after --quick-start
~/Software/blogit [±|tag:v0.4 ✓|] $ wc -l *.py blogit/*.py
   35 conf.py
  291 setup.py
  580 blogit/blogit.py
    0 blogit/__init__.py
  906 total

```

This is thanks to [pbr](https://docs.openstack.org/pbr/latest/) which makes setup.py much lighter and the update
of markdown2 which now includes my PR, thus cleaning a big monkey patch to
`md2.Markdown` which allows [metadata in blocks](https://github.com/trentm/python-markdown2/pull/224).

A hugh thanks goes to [Boudhayan Gupta](https://gitlab.com/BaloneyGeek)
who did the updates to the dependencies and `setup.py`.

Give blogit a spin, I hope you like it!
