---
title: Running more than one linux distribution without rebooting
author: Oz Nahum
published: 2012-03-31
tags: Debian, Linux
public: yes
chronological: yes
kind: writing 
summary: My laptop has reached Nirvana with Debian Squeeze, everything works out of the box, and I very happy with the stability of the system.
---

My laptop has reached Nirvana with Debian Squeeze, everything works out
of the box, and I very happy with the stability of the system. I don't
feel the software is outdated, because I anyway install some
applications I need or like directly from source.
However, I still want to be able to run Debian testing, and see how my
system evolves. Enter "chroot". 

With chroot I can run more that one Linux Distro and more than one
X-Server with out the need to stop my work and reboot my laptop. This is
just great. 

Here is how to do it, assuming you already have a partition with a
Debian installed on in do the following (if you don't have a partition
with Debian installed, I suggest you take a look at "debootstrap"):

1. First make a location where you will work as the root of the new
debian, in my case:

    $ su -# mkdir /debian-sec


2. now mount that partition, in my case /dev/sda5:
    
    mount /dev/sda5 /debian-sec

3. enable important devices so the new Debian will work as expected:
    
    mount -o bind /proc /debina-sec/procmount -o bind /dev/ /debian-sec/dev/
    mount /dev/pts /debian-sec/dev/pts -t devpts 
    mount -t sysfs /sysfs/ /debian-sec/sys 

4. finally change the root with chroot:

    chroot /debian-sec/ /bin/bash

If you want to run a secondary X-Server, do the following inside the
chroot:

    chroot # vi /etc/gdm/gdm.conf # 
    do s/vt7/vt9/ in [servers] sectionchroot 
    # /etc/init.d/gdm start

this will start another X-Server on vt9, to which you can switch with to
`Alt+Ctrl+F9`. 

Cheerios, Linux and Debian !

UPDATE: The last section about GDM in chroot seems not to work with gdm3...

    chroot # vim /usr/share/gdm/gdm.schemas

change the following keys:
    
    <shema>
        <key>daemon/FirstVT</key>
        <signature>i</signature>
        <default>9</default>
    </schema>

What does work ?

Switch to tty1, login as root, and chroot into the chrooted debian. 
Then chanage to with "su - "

now start the X server as the following:

    startx /usr/bin/fluxbox -- :1&

or 

    startx /usr/bin/gnome-session -- :1&


or

    startx  -- :1&
