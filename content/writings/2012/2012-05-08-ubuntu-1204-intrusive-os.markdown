---
title: Ubuntu 12.04 Intrusive OS
author: Oz Nahum
published: 2012-05-08
tags: Opinion, Ubuntu, Hardware
public: yes
chronological : yes
kind: writing 
summary: I installed Ubuntu 12.04 on two laptops by now. and I must rant. Ubuntu developers are assuming two many things about me.
---

I installed Ubuntu 12.04 on two laptops by now. and I must rant. Ubuntu
developers are assuming two many things about me. First, there is this
bug, which the['migration-assitant' mounts existing partitions in
READ-WRITE
mode](https://bugs.launchpad.net/ubuntu/+source/ubiquity/+bug/994510). I
find it dangerous and not necessary for migration.\
Then, today I installed Ubuntu 12.04 on IBM x121e and found out that my
Bluetooth chip is disabled. After about 20 min of looking I discovered,
it is because of a [bug in the installer which messes around with the
BIOS.](https://bugs.launchpad.net/ubuntu/+source/linux/+bug/812866) So
if you have IBM x120e with Intel Chipset, you need to reboot, restore
the BIOS defaults and then Bluetooth works.  \
That's all the ranting for now ...
