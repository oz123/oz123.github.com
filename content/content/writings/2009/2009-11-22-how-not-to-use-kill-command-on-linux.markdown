---
title: How not to use the kill Command on Linux
author: Oz Nahum
published: 2009-11-22
tags: Linux, CLI
public: yes
chronological : yes
kind: writing 
summary: A few months ago I installed Debian GNU/Linux on an old Sony Vaio Laptop of a friend of mine. The laptop is really nice with slim case and a 15" screen. She was really happy she could write her thesis on this nice machine again because Windows XP could not function properly on this machine. Installation was a breeze and  the non technical friend of mine was working on it happily for 4 months now.
---

A few months ago I installed Debian GNU/Linux on an old Sony Vaio Laptop of a friend of mine. The laptop is really nice with slim case and a 15" screen. She was really happy she could write her thesis on this nice machine again because Windows XP could not function properly on this machine. Installation was a breeze and  the non technical friend of mine was working on it happily for 4 months now.

Three weeks ago she called me and asked how she can watch DVDs. I figured out I forgot to install libdvdcss2 on her Debian. So I dropped by her place to fix it. I opened Synaptic and searched for it. But somehow it got stuck. So I had a terminal open and I typed

    
    ps aux | grep synaptic.


At this point she mad a remark on "oh, what is this magic and all those words..."

I murmured something about "this is the Linux terminal..." while reading the pid of synaptic, and then I typed:

    
    kill -9 5322


At this moment she stopped breathing and then yelled "Oh, what's going on... don't kill my computer...".

Trying to explain what is the meaning of the command kill was not useful. She was really astound by this.

So my conclusion is for next timpe - to save panic from your non technical friends, avoid using the command kill in front of them. It sounds scary, I guess. If you really have to kill a process, do it from gnome-system-monitor or ask them to bring you a glass of water before you type "kill" on their computer !
