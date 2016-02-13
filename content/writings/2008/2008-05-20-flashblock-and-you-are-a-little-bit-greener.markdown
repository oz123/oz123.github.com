---
title: Greener Browsing  
author: Oz Nahum
published: 2008-05-20
tags: Flash, Mozilla, Web
public: yes
chronological : yes
kind: writing 
summary: I use a very old laptop, a Thosiba Portege 3440ct. This tiny little machine has a Pentium III 500 MHz CPU and 128 RAM.
---


I use a very old laptop, a Thosiba Portege 3440ct. This tiny little machine has a Pentium III 500 MHz CPU and 128 RAM. 
It's okay for my daily needs like emailing and browsing the web. 
However, sometimes I get the cramps because certain websites etensively use Flash in their pages. 
This is really annoying while using Firefox and other flash supporting browser. E
specialy, when browsing to websites like Haaretz.co.il (I really like their contents, not their bloated flash comercialls). 
All this flash consumes CPU and really kills my computer. But, alas !

Today I have found a solution. A firefox extension named [Flashblock](http://flashblock.mozdev.org/). 
Horay! This turns the adds into a button, which enables you - the reader - to choose whether you want to see the commercial or not.

And about the post title: well, if you choose not to see flash, you save CPU power, if you save CPU power, 
you save some watts, and if you save some watts, you save some energy. If you save some energy you reduce the pollution you produce. 
Obvious, isn't it ?

I hope this post help's someone. It's here to remind me about this FF extension.

An update: apparently, Flashblock can be installed on Epiphany-browser. 
Here are the [instructions](http://live.gnome.org/Epiphany/FlashBlock). 
Hooray ! Lately, I've been using in a lot more than Firefox, and this is a real pleasure to go back Epiphany with Flashblock.

Another update: I couldn't make it work under epiphany, but with a little bit of 
googling I discovered that you can just put the following lines in 
your user-stylesheet.css located under ~.gnome2/epiphany:

    
    /* from <http://www.floppymoose.com/> */
    object[classid$=":D27CDB6E-AE6D-11cf-96B8-444553540000"],
    object[codebase*="swflash.cab"],
    object[type="application/x-shockwave-flash"],
    embed[type="application/x-shockwave-flash"],
    embed[src$=".swf"] {
    -moz-binding: url("http://www.floppymoose.com/clickToView.xml#ctv");
    }



That should work now.
