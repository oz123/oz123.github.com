---
title: TMUX - copy mode and how to control multiple servers at once
author: Oz Nahum
published: 2012-05-02
tags: Cluster, Linux, tmux
public: yes
chronological: yes
kind: writing 
summary: Two tips which needs to be documented
---

Two tips which needs to be documented:

The first one is how to copy in tmux, which had me struggling a lot.
Most places say that you need to type the following sequence:
**CTRL+a,[** (note my prefix is CTRL+a instead if CTRL+b).
Then something tricky happens:
In some servers I found out that selection of text is initiated with
either SPACE or **CTRL+SPACE**. So, try one of them.
Navigate with the ARROWS to select the text.
Than, copy the selected text with **CTRL+W** (or ALT+W if that does not
work).
Now, navigate to the desired place where you want to paste the text and
type the following sequence:
**CTRL+a,]**. 


The second tip is how to control multiple servers with TMUX:
First, export a variable called HOSTS holding your servers list, e.g.:

    HOSTS="host1 host2 host3 host4 host5"

then run the following script in your BASH:
    
    #!/bin/bash
    # ssh-everywhere.sh
    
    # a script to ssh multiple servers over multiple tmux panes 
    
    usage() {
        echo
        echo
        echo "Application Call: "
        echo
        echo "$BNAME sessionname"
        echo "before calling the script do: export HOSTS='host1 host2 host3'"
        echo "as a list of hosts to work on, or you will be promted to type"
        echo "the list in." 
    }
    
    starttmux() {
        echo 
        echo $HOSTS
        if [ -z "$HOSTS" ]; then
           echo -n "Please provide of list of hosts separated by spaces [ENTER]: "
           read HOSTS
        fi
        
        tmux new-session -d -s $sessionname 
        for i in $HOSTS
        do
        tmux split-window -v -t $sessionname "ssh $i"
        tmux select-layout tiled
        done
        #tmux set-window-option synchronize-panes on
        tmux attach -t $sessionname 
    }
    
    BNAME=`basename $0`
    if  [ $# -lt 1 ]; then
        usage
        exit 0
    fi
    
    sessionname=$1
    start tmux

That is all about TMUX for now.

P.S. \
After a long struggle again, I found out how to copy paste in VI mode
with tmux:\
**SPACE**, stars selection. \
**CTRL+m** copies to buffer.\
**CTRL+a,]** pastes the buffer.\
