---
title: Ubuntu Gusty is Bloatware
author: Oz Nahum
published: 2007-11-06
tags: Linux, Ubuntu
public: yes
chronological: yes
kind: writing 
summary: Ubuntu Gutsy is Bloatware. The latest ubuntu distro is terrible, comparing with the previous one, Feisty Fawn. Cases like this make me think about the 6 months release cycle, and really appreciate my Debian stable, which is old, but working. So why am I saying Ubuntu Gutsy is terrible ?
---

Ubuntu Gutsy is Bloatware. The latest ubuntu distro is terrible,
comparing with the previous one, Feisty Fawn.
Cases like this make me think about the 6 months release cycle, and
really appreciate my Debian stable, which is old, but working. So why am
I saying Ubuntu Gutsy is terrible ?
First, upgrading breaks USB mounting. During Beta testing phase many
people reported that upgrading will break mounting of external disks.
Well, the guys in Canonical think this is not important, and released
without supplying an adequate solution. 
This is wrong, because it hearts product loyalty. Many users, like me
are loyal until something just happens. I've used Ubuntu from version
6.04 to 7.10 as main laptop working station. Prior to this, I've use
SuSE, until their terrible package management drove me away ! Now with
Ubuntu 7.10 being so bad, I looking for alternatives.
Second, Gutsy has many great features, but do we need them all ?
Canonical, has done a great job winning the linux desktop, and now is
aiming for the server and corporate market. But I suspect that some
decisions are just to biased. For example, the inclusion of AppArmor and
SELinux. Security is important feature of any OS and linux is already
doing a great job. Do desktop users need such enhanced security as
AppArmor or SElinux, which is implemented in the NSA ?
Well, the reason I rant about that is that, both services slow down boot
times significantly, and remind me the days I've been working with
OpenSuSE 10.1, which was slugish. I used ubuntu 7.04 on a small old
laptop, which has a 500 MHz processor and 128 MB of RAM. Boot time from
GRUB to GDM took 1:47 minutes. With the new kernel and boot process it
takes over 5 minutes!
Now, advanced users can of course disable AppArmor on boot time, but try
removing the package libselinux - everything is dependent on it ! So it
won't be removed.
So, old laptops will just work terribly slow with gutsy ! So does
Tracker slows things down, and behaves in awkward ways. Tracker,
SElinux, and AppArmor, are all great features, but are terribly heavy,
and should not be installed on old computers. Hardware detection should
do better and at least ask the user if they should be activated by
default.
Eventually, I've ended up, burning another feisty CD, and reinstalling
it. I'll wait and see what will be with ubuntu 8.04. If it won't work to
my liking I'll completely switch to Debian. My server runs on it and I'm
happy with it.
