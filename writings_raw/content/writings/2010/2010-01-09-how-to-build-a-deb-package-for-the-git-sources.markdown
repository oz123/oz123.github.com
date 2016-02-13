---
title: How to Build a DEB package for the git sources
author: Oz Nahum
published: 2010-01-09
tags: Debian, Linux, Packaging
public: yes
chronological : yes
kind: writing 
summary: I wanted to build python-moinmoin from the 1.8.x series because python-moinmoin 1.9 didn't work for me.
---

I wanted to build python-moinmoin from the 1.8.x series because python-moinmoin 1.9 didn't work for me.

So I went and grabbed the source tar ball from http://git.debian.org/?p=collab-maint/moin.git;a=summary.

Then I did the following:

   tar xvzf moin.tar.gz
   sudo apt-get build-dep python-moinmoin

dpkg-buildpackage -rfakeroot -uc

and then I got myself a debian package working, a few more edits on the website configuration, and I was good to go with my wiki.

That's here short for reminding me, in case I need this again...
