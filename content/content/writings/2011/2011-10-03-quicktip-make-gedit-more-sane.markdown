---
title: Quicktip - make gedit more sane
author: Oz Nahum
published: 2011-10-03
tags: CLI, Debian, GNOME
public: yes
chronological: yes
kind: writing 
summary: Continuing the agile setup of GNOME desktop using gconftool-2. Here's a snippet to make tab width 4 spaces, insert spaces instead of tabs and enable automatic indentation:
---


Continuing the agile setup of GNOME desktop using gconftool-2. Here's a
snippet to make tab width 4 spaces, insert spaces instead of tabs and
enable automatic indentation:
    
    gconftool-2  --set /apps/gedit-2/preferences/editor/tabs/insert_spaces --type bool 1
    gconftool-2  --set /apps/gedit-2/preferences/editor/tabs/tabs_size --type int 4
    gconftool-2  --set /apps/gedit-2/preferences/editor/auto_indent/auto_indent --type bool 1


Well, GNOME 2 isn't that evil. Let's hope the Mate Desktop Environment really catches.
