---
title: Simple IPTABLES script
author: Oz Nahum
published: 2010-04-11
tags: Linux
public: yes
chronological : yes
kind: writing 
summary: In the following a simple IPTABLES script. It has the following features:
---

In the following a simple IPTABLES script. It has the following features:

Block all incoming communication, excepts on certaion ports, allow outgoing trafic, service start\stop\restart like init script.

Copy to your /etc/init.d/localfw and

    
    chmod +x /etc/init.d/localfw.


You can soft link it to start at boot time with:

    
    ln -s /etc/init.d/localfw /etc/rcS.d/S39localfw


You can stop the firewall or restart it with (need I to say you have to be root or sudo ???):

    
    /etc/init.d/localfw start|stop|restart


Here's is the code:

    
    #!/bin/sh
    
     #added init LSB tags 13/May/2010
     ### BEGIN INIT INFO
     # Provides:          localfw
     # Required-Start:
     # Required-Stop:
     #Default-Start:     2 3 4 5
     # Default-Stop:      0 1 6
     # Short-Description: Start firewall at boot time
     # Description:
     ### END INIT INFO
    
    PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
    
    NAME=localfw
    
    DESC="local firewall  services"
    
    case "$1" in
    
    start)
    
    IPT="/sbin/iptables"
    
    # iptables script generated 2010-03-30
    
    # Flush old rules, old custom tables
    
    $IPT --flush
    
    $IPT --delete-chain
    
    # Set default policies for all three default chains
    
    $IPT -P INPUT DROP
    
    $IPT -P FORWARD DROP
    
    $IPT -P OUTPUT ACCEPT
    
    # Enable free use of loopback interfaces
    
    $IPT -A INPUT -i lo -j ACCEPT
    
    $IPT -A OUTPUT -o lo -j ACCEPT
    
    # All TCP sessions should begin with SYN
    
    $IPT -A INPUT -p tcp ! --syn -m state --state NEW -s 0.0.0.0/0 -j DROP
    
    # Accept inbound TCP packets
    
    $IPT -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
    
    $IPT -A INPUT -p tcp --dport 22 -m state --state NEW -s 0.0.0.0/0 -j ACCEPT
    
    #webserver http
    
    $IPT -A INPUT -p tcp --dport 80 -m state --state NEW -s 0.0.0.0/0 -j ACCEPT
    
    #webserver http + ssl
    
    $IPT -A INPUT -p tcp --dport 443 -m state --state NEW -s 0.0.0.0/0 -j ACCEPT
    
    #accept gpg keys
    
    $IPT -A INPUT -p tcp --dport 11371 -m state --state NEW -s 0.0.0.0/0 -j ACCEPT
    
    # Accept outbound packets
    
    $IPT -I OUTPUT 1 -m state --state RELATED,ESTABLISHED -j ACCEPT
    
    $IPT -A OUTPUT -p udp --dport 53 -m state --state NEW -j ACCEPT
    
    # Accept out going conecntion to TIVOLI storage manager
    
    $IPT -A OUTPUT -p tcp --dport 1500 -m state --state NEW -j ACCEPT
    
    echo 1 > /proc/sys/net/ipv4/conf/all/forwarding
    
    echo "Local Firewall started ..."
    
    ;;
    
    stop)
    
    echo 0 > /proc/sys/net/ipv4/conf/all/forwarding
    
    iptables -t nat -F
    
    iptables -flush
    
    echo "Local Firewall stopped !!!"
    
    ;;
    
    restart)
    
    echo "Restarting the Firewall ..."
    
    /etc/init.d/localfw "stop"
    
    /etc/init.d/localfw "start"
    
    ;;
    
    *)
    
    N=/etc/init.d/$NAME
    
    echo "Usage: $N {start|restart|stop}"
    
    exit 1
    
    ;;
    
    esac
    exit 0


There is probably much more to learn about IPTABLES, but for now I keep it short and clear. Enjoy ...
