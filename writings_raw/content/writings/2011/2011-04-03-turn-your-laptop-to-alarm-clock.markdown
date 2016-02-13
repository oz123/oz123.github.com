---
title: Turn your laptop to alarm clock
author: Oz Nahum
published: 2012-04-03
tags: Debian,CLI, Linux, Hardware
public: yes
chronological: yes
kind: writing 
summary: I bumped into an article describing `rtcwake` [here](http://www.dedoimedo.com/computers/wake-cron.html), so I thought it will be cool to write a nice wrapper script around it.  
---


I bumped into an article describing `rtcwake`
[here](http://www.dedoimedo.com/computers/wake-cron.html), so I thought
it will be cool to write a nice wrapper script around it. \
It was also an excuse to master some more bash scripting and the use of
"date" command. 

There are many many other implementations for rtcwake script, like
[here](http://blog.bofh.it/debian/id_222) for example, and I've seen
some other cases in the Ubuntu forums, after I finished writing mine. So
with out further a do, here is my solution, which is easy to use:\


    #!/bin/bash
    #       GoodMorning.sh
    #       
    #       Copyright 2011 Oz Nahum <nahumoz_ATTNOSP_gmail.com>
    #       
    #       This program is free software; you can redistribute it 
    #       and/or modify it under the terms of the GNU General 
    #       Public License as published by the Free Software 
    #       Foundation; either version 3 of the License, or
    #       (at your option) any later version.       
    #       This program is distributed in the hope that it will 
    #       be useful, but WITHOUT ANY WARRANTY; without even the
    #       implied warranty of MERCHANTABILITY or FITNESS FOR A
    #       PARTICULAR PURPOSE.  See the GNU General Public 
    #       License for more details.
    #       
    
    if [ $5 ] && [ $5 !=  "test" ]; 
        then    
            PLAYLIST=$5    
            PLAYER=$4else    
            PLAYLIST=$4
    fi
    if [ $PLAYER ] && [ $PLAYER = "mplayer" ] ; 
        then   
            PLAYER="mplayer -play list"
            else   PLAYER=$4
    fi
    echo "player is" $PLAYER
    
    case "$1" in
        "")        
        echo "  usage: GoodMorning.sh --help to see this how to use that script"        
        exit 1        
        ;;        
        "--help")        
        echo "  GoodMorning.sh [--set|--configure]   "
        echo " "        
        echo "  Options:"        
        echo "  --set"        
        echo "  --configure"        
        echo ""        
        echo "  GoodMorning.sh --set   [player|playlist]"        
        echo "  will set the correct time for the script to wake the computer "
        echo "       with a lovely playlist."
        echo " "        
        echo "  GoodMorning.sh --configure "        
        echo "      will add the specified  to the sudoers list, so that rtcwake"
        echo "      can be called without promting for password. This option is not yet"
        echo "      implemented. This option is only available with sudo or as root..."
        ;;      
        "--set")
        IN=$3    arrIn=(${IN//:/ })                
        echo "will set up wake up to ${arrIn[0]}:${arrIn[1]} $2"
        TODAY=`date +%F`        
        TODAY_IN_SEC=`date --date=$TODAY +%s`
        TIME=`date -d "$2 00:00:00" +%s`
        WAKE_UP_TIME=$(($TIME+3600*${arrIn[0]}+60*${arrIn[1]}))
        echo "date to wake up" `date --date "1970-01-01 $WAKE_UP_TIME sec" "+%Y-%m-%d %T"`
        # check if testing mode        
        if [ "$5" = "test" ] || [ "$6" = "test" ]; then
            echo "testing only", $PLAYER, $PLAYLIST
            sudo rtcwake -t $WAKE_UP_TIME -m on -v && $PLAYER $PLAYLIST
        else
            sudo rtcwake -t $WAKE_UP_TIME -m mem -v && $PLAYER $PLAYLIST
        fi        
        ;;
        "--configure")
        if  [[ $EUID -ne 0 ]]; then 
            echo "This script must be run as root" 1>&2            
            exit 1
        fi
        echo "Will add user " $2 "to sudoers file so that,"        
        echo "$2 will be able to call it without password"              
        echo "$2 ALL= NOPASSWD: /usr/sbin/rtcwake" >> /etc/sudoers        
        ;;
        esac



