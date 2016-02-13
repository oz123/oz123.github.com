---
title: Calcurse, a compact Linux organizer, now with encryption
author: Oz Nahum
published: 2011-04-17
tags: Debian,CLI, Linux
public: yes
chronological: yes
kind: writing 
summary: I bumped into calcurse a while ago, but I didn't take the use of it seriously. When I started using it, I was also using Gnome's Evolution.   
---


I bumped into calcurse a while ago, but I didn't take the use of it
seriously. When I started using it, I was also using Gnome's Evolution.
But than, times changed, and I didn't need a calender anymore, so I
gradually quit using Evolution. When two weeks ago I decide to organize
my life on the computer again, I decided I would like to have a portable
application I could carry on a USB stick. There was calcurse, which
produces a very compact executable which I can carry around. Since it
uses plain text files which are easily editable, I can also edit them on
other operating systems without any problem.\
So there you have it. [A small great lightweight calendar
application](http://calcurse.org/): Calcurse !\
\
As a bonus to myself I decided to play with the idea, that I would like
to encrypt the data I have on my disk on key, since it is possible that
I loose my USB with lots of customers private data. So I wrote the
following script, which launches the binary from the USB, decrypts the
data folder, and then upon closing Calcurse would archive the data
directory, encrypt it, and move it back to the USB.\
\
Notice the following things:\
1. I use OpenSSL, this is probably lame, and I should use GPG key.\
2. You have to do a few steps manually before you can use the script,
you will find them in\
the body of the script below as comments.\
    
    #!/bin/bash
    
    # ENCRYPTCALCURSE.SH
    
    # Written by Oz Nahum <nahumoz__at_you_know_where_no_spam_is_gmail.com>
    # This script is distributed under the terms of the GNU Public License 
    # Version 3 or later.
    # You can obtaion copies of this license at:
    # http://www.gnu.org/licenses/gpl.html
    
    # A script to decrypt the calcurse_date dir, open it in 
    # /home/<user>/calcurse_data
    # then launch calcurse pointing to it, 
    # and upon closing calcurse, encrypt the data, move it to usb stick, 
    # and delete all data from /home/<user>/calcurse_data
    
    ### Begin of Script
    
    INPUT_FILE="calcurse_d.tar.enc"
    OUTPUT_FILE="calcurse_d.tar.enc"
    
    #name of directory to encrypt (e.g. ~.calcurse)
    CALCURSE_DATA_DIR="~/.calcurse/"
    
    # usage:
    # $ bash encryptCalcurse.sh 
    # $ bash encryptCalcurse.sh [ecnrypted_data_in.enc] [encrypted_data_out.enc]
    
    #TODO: test that modified script !
    ### Begin of Script
    #make files readable only by owner
    umask 077
    
    function Config {
        USB=`pwd`
        tar -cf calcurse_data.tar $CALCURSE_DATA_DIR
        openssl aes-256-cbc -salt -in calcurse_data.tar -out calcurse_d.tar.enc
        clc=`which calcurse`
        cp -v $clc $USB
        
    }
    
    function cleanUp {
        find /dev/shm/calcurse_data -type f | xargs shred -fuz;
        if [ -f /dev/shm/cdt.tar ]; then
            shred -fuz /dev/shm/cdt.tar
        fi
        if [ -f /dev/shm/calcurse_data_tmp.tar ]; then
            shred -fuz /dev/shm/calcurse_data_tmp.tar
        fi
        rmdir /dev/shm/calcurse_data/notes
        rmdir /dev/shm/calcurse_data
    }
    
    function readData {
    #first decrypt the data
    openssl enc -d -aes-256-cbc -salt -in $INPUT_FILE -out /dev/shm/calcurse_data_tmp.tar
    echo "extracting data"
    #silently extract data, no need for verbose output (v flag)
    tar -C /dev/shm -xf /dev/shm/calcurse_data_tmp.tar
    #note unpacking removes the original tar
    }
    
    function encryptData {
    openssl aes-256-cbc -salt -in /dev/shm/cdt.tar -out calcurse_d.tar.enc
    }
    
    
    case "$1" in
        "")
        echo "expecting parameter input... see header of script for usage"
        ;;
        "--config")
            CALCURSE_DATA_DIR=$2    
            Config
        ;;
    
        "--read")
            trap "cleanUp" SIGHUP SIGINT SIGQUIT SIGKILL SIGABRT SIGTERM EXIT
            # when calcurse is done tar the direcotry
            readData
            calcurse -D /dev/shm/calcurse_data
            tar -cf /dev/shm/cdt.tar -C /dev/shm/ calcurse_data/
                
            # then encrypt
            # if encryption failed $? == 1 so repeat it again ...
            encryptData
            es=$?
            while [ "$es" = "1" ]; do 
                echo "encrypting data"
                encryptData
                es=$?    
            done
        ;;
        "--decrypt")
            readData
        ;;
        "--encrypt")
            tar -cvf /dev/shm/cdt.tar -C /dev/shm/ calcurse_data/
            encryptData
        ;;
    
            #if encryption succeeded clean up by calling the function
            #cleanUp
        
    esac
    #note about the salt option note found in openssl man page[1],[2]
    #note about lack of compresion with ssl [3]
    
    #sources:
    #[1]http://ubuntuforums.org/showpost.php?p=8287351&postcount=9
    #[2]http://linux.die.net/man/1/enc
    #[3]http://serverfault.com/questions/17855/can-i-compr:ess-an-encrypted-file
    
