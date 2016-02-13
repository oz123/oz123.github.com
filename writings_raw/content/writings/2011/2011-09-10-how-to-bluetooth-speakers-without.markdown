---
title: Using BluetoothSpeakers without Pulseaudio
author: Oz Nahum
published: 2011-09-10
tags: Debian,FOSS, Hardware
public: yes
chronological: yes
kind: writing 
summary: |
summary: Creative Labs D200, which provide me with nice tunes compared to the prices. 
---



About 3 months ago I have purchased a Bluetooth Speakers set. I chose
the Creative Labs D200, which provide me with nice tunes compared to the
prices. The speakers worked out of the box with my Bluetooth adapter.
Pulseaudio also makes life easier to switch between the laptop's own
speaker to the Bluetooth speakers. However, I get irritated sometimes
with pulseaudio, and I was looking for an alternative solution.

After researching a few different sources I have come up with my own
flavor of solution, which I document here for future benefit of myself
and others.

The first step included removing all the components of Pulse-Audio, and
installing the bluez-alsa packages:

    apt-get remove pulse-audioapt-get install bluez-alsa

then edit the file .asoundrc:
   
   linuxpixie@laptop:~$ cat .asoundrc 
    pcm.bluetooth {
        type bluetooth
        device 00:02:3C:26:BA:87 # change this MAC address using the command "hcitool scan"
        profile "auto"}
    pcm.!default {
       type hw
       card 0
       device 0
    }
    
Now pair your device to the laptop, using hcipair command or
gnome-blue-tooth-applet or blueman-applet, what ever you use.
Now you need to tell gstreamer to use the bluetooth device as  the audio
sink. This is basically done with the following command:

    
    gconftool-2 -t string -s /system/gstreamer/0.10/default/musicaudiosink "alsasink device=bluetooth"

I modified a small script to make the switching to bluetooth sound and
backward. This script lies in my ~bin/ directory. 

    linuxpixie@laptop:~$ cat bin/audioswitcher.sh 
    #!/bin/bash
    state=`gconftool-2 --get /system/gstreamer/0.10/default/musicaudiosink |  
    cut -d\  -f1`
    if [ $state == "autoaudiosink" ]; then
        gconftool-2 -t string -s /system/gstreamer/0.10/default/musicaudiosink 
        "alsasink device=bluetooth" 
        zenity --info --title="GStreamer" --text="Switched to bluetooth speakers"
    else
        gconftool-2 -t string -s /system/gstreamer/0.10/default/musicaudiosink "autoaudiosink"
        zenity --info --title="GStreamer" --text="Switched to laptop speakers"  
    fi

Don't forget to make the script executable, with: 

    linuxpixie@laptop:~$ chmod +x bin/audioswitcher.sh   

Now you can just call the script use gnome-launcher, a keyboard shortcut
or just using the terminal.
One Last thing. VLC is a very popular player which I use too. However,
this solution does not work for VLC, since it does not use Gstreamer.
So, the solution, is to edit the VLC config file found 

    .config/vlc/vlcrc
    [alsa] 
    # ALSA audio output
    # ALSA Device Name (string)
    #alsa-audio-device=hw:0,0
    #alsa-audio-device=default
    alsa-audio-device=bluetooth

As a nice bonus, if your Bluetooth adapter is ON and available, you
don't need to pair it with laptop when playing with VLC. VLC will hang
for about 4 second, waiting for the Bluetooth speakers to turn ON, and
will pair automatically, and then the music will be played automatically
through the Bluetooth speakers. If the Bluetooth devices is not found,
VLC will play the music through the Laptop speakers.

UPDATE (March 2012):
Upgrading from bluez 4.96 to 4.98 broke this setup and I could not find
a solution until I reported a bug on that issue. The maintainer send me
a solution:

addding following into [General] section of `/etc/bluetooth/audio.conf`


    Disable=MediaEnable=Socket

A more updated version of the script, can be found in [my
github](https://github.com/oz123/dude/blob/master/bin/speakersswitcher.sh).
This Updated version is also working on
[mate-desktop](http://linuxpixies.blogspot.de/2011/12/short-news-about-gnome-2-fork.html).

