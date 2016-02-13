---
title: Quicktip - Setting keyboard layout in GNOME via CLI
author: Oz Nahum
published: 2011-09-27
tags: GNOME,CLI, Linux
public: yes
chronological: yes
kind: writing 
summary: Of course backups could do the job, but I find a clean install much cleaner and safer for my purposes.  
---

Since I tend to break my installation quite often while testing new
stuff, I am always looking for more agile way of re-setting my system
quicky. Of course backups could do the job, but I find a clean install
much cleaner and safer for my purposes.
So, here is a tip how to set keyboard layouts from the command line
using GNOME. This is very useful if you speak more than one language:
    
    gconftool-2  -R /desktop/gnome/peripherals/keyboard/kbdgconftool-2 --recursive-unset
      /desktop/gnome/peripherals/keyboard/kbdgconftool-2 -s 
      /desktop/gnome/peripherals/keyboard/kbd/layouts -t list --list-type=string [us,de]
    gconftool-2 -s /desktop/gnome/peripherals/keyboard/kbd/options 
       -t list --list-type=string ["grp   grp:alt_shift_toggle,terminate  terminate:ctrl_alt_bksp"]

Do notice: there are TABS in the empty spaces up there. GNOME's xml was
intolerant for my attempts to replace them with spaces, and really only
worked with the braces.
