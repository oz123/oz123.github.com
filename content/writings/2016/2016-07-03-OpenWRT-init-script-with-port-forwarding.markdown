---
title: OpenWRT SSH init script with port forwarding
author: Oz Nahum Tiram
published: 2016-07-03
tags: OpenWRT, Linux, SSH
public: yes
chronological: yes
kind: writing
summary: If you have a publicly available server you can setup a permanent SSH connection to it from your OpenWRT. Add remote port forwarding to the plan, and you get an easy way to always access your hosts where your OpenWRT router is.
---

OpenWRT uses it's own init system called procd, which does also process supervision, and is a nice alternative to systemd.
Here how to create a permanent connection from your OpenWRT router to your publicly available server.

First, OpenWRT isn't using OpenBSD's SSH, rather a lightweight alternative called dropbear. It's keys aren't ssh keys. You will
need to create a dropbear key and add its public signature to your `authorized_keys` file in your public server:

```
root@OpenWRT # dropbearkey -t rsa -f /root/.ssh/id_dropbear
```

Then, extract the public key with:

```
 $ dropbearkey -y -f .ssh/id_dropbear
 Public key portion is:
  ... you long public key ...

```

Add the public key to the file `youruser@your_public_server:~/youruser/.ssh/authorized_keys`.

Make sure your the SSH daemon in your public server can forward ports by adding the following option to `/etc/ssh/sshd_config`:

```
GatewayPorts yes
```

Make sure you restart the SSH daemon (`service ssh restart` or what ever init system you use).

Next in your OpenWRT create the following script:

```
root@OpenWrt:~# cat bin/ssh-ccd 
#!/bin/sh

USER=youruser
SERVER_IP=xxx.yyy.zzz.aaa
PORT=10000

ssh -i /root/.ssh/id_dropbear -l $USER $SERVER_IP -R $PORT:127.0.0.1:22 -N &
```

Adapt the variables USER, SERVER_IP and PORT to match your setup, and make the script executable with `chmod +x /root/bin/ssh-ccd`.
Note the last flag `-N`. This option makes sure your connection is done without running any command (not even starting a shell).

Now, it's time to add the init script: 


```shell
root@OpenWrt:~# cat /etc/init.d/ssh-ccd 
#!/bin/sh /etc/rc.common

USE_PROCD=1

START=99
STOP=0


start_service() {
  procd_open_instance
  echo "Starting ssh connection"
  procd_set_param env export HOME=/root  
  procd_set_param command /root/bin/ssh-ccd
  procd_set_param stdout 1 # forward stdout of the command to logd
  procd_set_param stderr 1 # same for stderr

  # respawn automatically if something died, be careful if you have an alternative process supervisor
  # if process dies sooner than respawn_threshold, it is considered crashed and after 5 retries the service is stopped
  procd_set_param respawn ${respawn_threshold:-3600} ${respawn_timeout:-5} ${respawn_retry:-5}
  procd_close_instance
}

```

Again, make sure the script is executable `chmod +x /etc/init.d/ssh-ccd`. You need to enable the script and then start it.

```
root@OpenWrt:~# /etc/init.d/ssh-ccd enable
root@OpenWrt:~# /etc/init.d/ssh-ccd start
```

And if everything works, you should see a permanent SSH process in your OpenWRT:

```
root@OpenWrt:~# ps | grep ssh
4783 root      1288 S    ssh -i /root/.ssh/id_dropbear -l USER SERVER -R PORT:127.0.0.1:22 -N
4894 root      1356 S    grep ssh
```

Now on your public server you can access your OpenWRT with:

```
root@publicserver:/home/user# ssh -l root -p PORT localhost


BusyBox v1.23.2 (2015-07-25 15:09:46 CEST) built-in shell (ash)

  _______                     ________        __
 |       |.-----.-----.-----.|  |  |  |.----.|  |_
 |   -   ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
 -----------------------------------------------------
 CHAOS CALMER (15.05, r46767)
 -----------------------------------------------------
  * 1 1/2 oz Gin            Shake with a glassful
  * 1/4 oz Triple Sec       of broken ice and pour
  * 3/4 oz Lime Juice       unstrained into a goblet.
  * 1 1/2 oz Orange Juice
  * 1 tsp. Grenadine Syrup
 -----------------------------------------------------
root@OpenWrt:~# 

```

Now you can successfully access your OpenWRT from your public server anytime.
