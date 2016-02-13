---
title: More GCONF Fun - Setting display backlight
author: Oz Nahum
published: 2011-10-23
tags: Debian,FOSS, Linux
public: yes
chronological: yes
kind: writing 
summary: In my Clevo notebook all the Fn keys work, except the Brightness keys. So after search quite long, I have found that the only solution that really works for me is `xbacklight`
---

In my Clevo notebook all the Fn keys work, except the Brightness keys.
So,\
after search quite long, I have found that the only solution that really
works for me\
is "xbacklight".\
So, here is how to map the "Special Key " and alt together with F8 and
F9 to reduce or\
increase screen brightness.\
First, install xbacklight: \


    aptitude install xbacklight


Decide where you want the custom script to reside (see bellow) and
export the following bash variable: \

    export PATHWHEREYOUWANTYOURSCRIPT=/usr/local/bin/increasebacklight.sh

Then create custom keybindings: 

    #setting to decrease
    gconftool-2 -s /desktop/gnome/keybindings/custom1/action -t string "xbacklight -dec 14"
    gconftool-2 -s /desktop/gnome/keybindings/custom1/binding -t string "F8"
    gconftool-2 -s /desktop/gnome/keybindings/custom1/name -t string "Reduce Backlight"
    #setting to increase backlightg
    conftool-2 -s /desktop/gnome/keybindings/custom2/action -t string "$PATHWHEREYOUWANTYOURSCRIPT"
    gconftool-2 -s /desktop/gnome/keybindings/custom2/binding -t string "F9"
    gconftool-2 -s /desktop/gnome/keybindings/custom2/name -t string "Increase Backlight"


And finally, setup the the script which increases the screen
brightness:

    #note: if you chose like me /usr/local/bin/increasebacklight.sh
    #run the following as root.
    #you can also have it in ~/bin/increasebacklight.sh, just make
    #sure ~/bin/ is in your PATH
    
    cat >> $PATHWHEREYOUWANTYOURSCRIPT <<EOF
    #!/bin/bash
    
    # a simple script to avoid the fact 
    # that it is impossile to increase 0 precent
    # by add more precent ...
    
    LEVEL=`xbacklight -get`
    
    if [ $LEVEL == "0.000000" ]; then
        xbacklight -set 15
    else
        xbacklight -inc 15
    fi
    EOF
    
    chmod +x $PATHWHEREYOUWANTYOURSCRIPT

That is all.\
\
P.S.\
Yariv,\
If you are reading this, thanks for introducing me to xbacklight.
