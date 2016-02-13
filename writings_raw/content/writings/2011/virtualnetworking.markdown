---
title: Create a virtual networking lab with vmware workstation
author: Oz Nahum
published: 2011-02-01
tags: Virtualization, Linux, Hardware
public: yes
chronological: yes
kind: writing 
summary: This is a post to demonstrate how you can build a LAN with DNS servers and DHCP servers running inside VMWARE. 
---

This is a post to demonstrate how you can build a LAN with DNS servers and DHCP servers running inside VMWARE. 
This can be useful when planning networks or just when you want to learn networking stuff, but don't have the real hardware.


First you need to create a few VM Servers. In this examples I have set up 2 CentOS servers, and one Debian server:

![VMware Workstation Machines](/img/content/Bildschirmfoto-CentOS-Server-VMware-Workstation-1024x799.png "VMware Workstation Machines")

Next edit the networking settings of the machine to point to /dev/vmnet9 - which is a virtual switch:

![Virtual Machine Settings](/img/content/Bildschirmfoto-Virtual-Machine-Settings-300x211.png "Virtual Machine Settings")

Then boot in to your server - and configure the IP address of the interface manually. 
In CentOS it is done by choosing the Administration menu from the Panel, and then clicking on the Network configure applet:

![Network config](/img/content/Screenshot-Network-Configuration.png "Network Config")

Click on Edit and insert manually the values you want:

![Ethernet Device](/img/content/Screenshot-Ethernet-Device.png "Ethernet Device")

Finally, edit the file /etc/sysconfig/network and change the host name:

    NETWORKING=yes
    NETWORKING_IPV6=no
    HOSTNAME=ServerCentOS.loc


Repeat the same for all guests giving them different IP addresses ... 
and you are ready to set up services like DHCP and DNS in side the virtual LAN.

