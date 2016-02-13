---
title: salt quick tip - changing passwords on multiple clusters
author: Oz Nahum Tiram
published: 2014-10-24
tags: [salt, linux, sudo]
public: yes
chronological: yes
kind: writing
summary: Using salt stack to manage your own private cloud on clusters can ease your life. Here is how you can allow users to update their passwords on multipl Linux hosts.
---

Salt is a configuration management system and a remote execution framework written
in Python. It runs on Linux, BSD, and even Windows. It provide various execution
modules which help you automate tasks on heterrougenous clusters. 
Usually, you would like to provide a single password to all Linux hosts for a user. 
On such method would be to install and configure an authetication server like LDAP
or a similar. 
However, LDAP and similar services are usually very complex to install and configure
and even learn. If your cluster is small or you have a little amount of users, you 
might have been thinking of different sollution. One such solution would be to 
synchronize `/etc/shadow` files between machines. This requires some kind of script
or manual involvement. 
Using salt and sudo you can automate the process. Here is how you can do it. 
First, add the following line to your `/etc/sudoers` on the salt master:
    
```bash
# users in the group cops can run this script without a password
%cluster-users ALL=(ALL:ALL) PASSWD: /usr/local/bin/cluster-changepass
```  

This will allow users in the `cluster-users` group to run the command 
`/usr/local/bin/cluster-changepass` as root after giving their password. 
Now let's creat the script that actually does the job:
    
```bash 
#!/bin/sh
echo "Changing password for:" $SUDO_USER
read -s -p "New Password: " PASSWORD1
echo
read -s -p "repeat Password: " PASSWORD2
if [ $PASSWORD1 != $PASSWORD2 ]; then
    echo "The passwords don't match!"
    exit 1
fi
echo $PASSWORD
HASH=`mkpasswd -m sha-512 -s $PASSWORD1`
salt '*' shadow.set_password $SUDO_USER $HASH
``` 

Save the above content to `/usr/local/bin/cluster-changepass` and change the 
permissions and ownership of the script:

```bash
$ chmod 0755 /usr/local/bin/cluster-changepass
$ chwon root:root /usr/local/bin/cluster-changepass 
```

Now, your users can modify their password after typing their current password.
For the script above to work, the command `mkpasswd` has to be installed, on 
debian based systems it is found in the package `whois`.

