---
title: A few notes about FreeBSD
author: Oz Nahum
published: 2009-03-14
tags: Opinion, FreeBSD
public: yes
chronological : yes
kind: writing 
summary: Well, I wrote earlier that I'm in love with Debian, but I **had** to try FreeBSD (Someone actually paid me to do that...), and now I am even more with love with Debian! But as a courtesy to the developers of FreeBSD I'll write this short report. Maybe they'll find it useful... maybe not... anyway this could be read as a bug report. And if I bother to write it I means that although I rant and criticize, I had in general a nice experience. Other wish, I would just press 'eject' on the CD-ROM's button and throw the CD out the window (metaphorically speaking). Anyway, here is my short report.
---

Well, I wrote earlier that I'm in love with Debian, but I **had** to try FreeBSD (Someone actually paid me to do that...), and now I am even more with love with Debian! But as a courtesy to the developers of FreeBSD I'll write this short report. Maybe they'll find it useful... maybe not... anyway this could be read as a bug report. And if I bother to write it I means that although I rant and criticize, I had in general a nice experience. Other wish, I would just press 'eject' on the CD-ROM's button and throw the CD out the window (metaphorically speaking). Anyway, here is my short report.

pkg_add is really a nice tool. It brings precompiled packages. But I didn't like the fact that there is no progress bar or any indication of how much is done. It feels like waiting in the dark. Apt-get is a more verbose and communicating with the user.

I loved the huge amount of ports availible and the easy install. But I have to admit that as much I love computers I don't want to spend 4 days compiling all my system. Some of the packages can't be added with pkg_add and when you need to upgrade the system it takes ages. Unless I have extremly large amount of free time to do that I would not go back doing that on my laptop.

As a linux user I was surprised to see that there is no possibility to switch from user to  SU when installing. I could by pass that with adding my user to the wheel group. I was thinking about it a little bit and I still haven't reached a conclusion if I like Stallman approach to the issue or not.

After upgrading from version 7.0 to 7.1 I was suprised to see that only the base system was upgraded. The upgrade was really a piece of cake, if you followed the manual. At this point I was dumb enough to do portupgrade -a. This enden up with 4 days of endless compiling and answering curses dialogs. If I read the instructions of how to upgrade Gnome DE I would save my self lot's of troubles.

In general my impression is very good. I wish debian had an extensive hand book as the FreeBSD hand book. This is the most impressive piece of documentation I've ever seen. And it's pretty updated.

The biggest disadvantage in FreeBSD in my opinion is its BSD lisence which would prevent me from contribution to the project. I know there is a hugh debate between the two camps (GPL vs. BSD). I tend to the side of the GPL.

***

As a source distribution I think I would like to try GENTOO one day, but with all the rotten policies they seem to have I'd stick with my comfy Debian... But since I work on so many Debian servers at work, I'm thinking of switching a distro on my laptop at home just to be familiar with another distro. I might try Slackware, but that is already way beyond the scope of the beginning of this post.
