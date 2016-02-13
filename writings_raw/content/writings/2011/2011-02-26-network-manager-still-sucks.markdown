---
title: Network-manager still sucks !
author: Oz Nahum
published: 2011-02-26
tags: WICD, GNOME, Linux
public: yes
chronological: yes
kind: writing 
summary: I have been long complaining about the buggy network-manager included in GNOME. Today, I have (re)discovered I am still unable to use Network-Manager to connect to a WPA secured wirless
---


I have been long complaining about the buggy network-manager included in
GNOME. Today, I have (re)discovered I am still unable to use
Network-Manager to connect to a WPA secured wirless...
Being too lazy to look up why on a clean install of Debian Mint Linux
Edition, Network-Manager is still retarded, I opted to the following
solution:

    apt-get --purge remove network-manager && apt-get install wicd
    wicd-gtk

So long, Network-Manager!

