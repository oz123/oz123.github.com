---
title: WordPress rant...
author: Oz Nahum
published: 2008-08-11
tags: Web
public: yes
chronological : yes
kind: writing 
summary: WordPress is a great tool for quickly building a personal blog, website or even a store or a large community website. However, there comes a time with every wordpress installation, or maybe even every pre built content management system such as Drupal or Joomla!, that you encounter the glass ceiling where you have to start heavily digging in code you didn't write 
---


WordPress is a great tool for quickly building a personal blog, website or even a store or a large community website. However, there comes a time with every wordpress installation, or maybe even every pre built content management system such as Drupal or Joomla!, that you encounter the glass ceiling where you have to start heavily digging in code you didn't write.
I started with Drupal 4.7 almost two years ago. I built www.cyclejerusalem.org in a couple of days. But when I started reaching a higher degree of complexity I stoped using Drupal and moved to Wordpress because it was easier to handle. This week I finished building the new website of www.cyclejerusalem.org using wordpress.

This is a list of stuff I am not happy with, which can be read as a bug report if you wish.



TinyMCE in wordpress is a great feature, but for some reason Wordpress developers decided to remove or hide the directionality button from the editor. I wasted 7 hours digging into this and couldn't find an easy solution. Eventually I discovered that in gecko based browsers control+shift+x do the switch. Apparently this also works for gmail. But for christ's sake, are we supposed to guess it ? At least include it in the documentation, why the hack I need to waste 7 hours for this ???

Users register - Here again Wordpress developers decided to make usernames only in ascii letters. This a really bad feature in my opinion. Drupal enables you the have users in any language you'd like.

And finally - Plugins Clutter - Wordpress has many many great plugins. But it's plugin directery is an absolute mess. When you browse plugins they are ordered by tags or keyword but not by version. Thus you find many abandoned or non-relevant plugins in the directory. This makes it really hard to find the right plugin for you. That said, I must say I see the positive side of it... It makes you see what others have dove and enables you to continue their work if you want.

To sum up: I do like Wordpress, and I'll keep using it for the while. But there is no doubt that if I had more time I'd build my own CMS, and I am currently looking at Django and CakePHP for that.

