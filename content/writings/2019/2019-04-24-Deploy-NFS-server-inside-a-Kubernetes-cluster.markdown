---
title: Deploy NFS server inside a Kubernetes cluster
author: Oz Tiram
published: 2019-04-24
tags: Linux, Kubernetes
public: no
chronological: yes
kind: writing
summary: >
	Using NFS shared volumes in Kubernetes is easy. But what if you want to serve 
	NFS volumes from with Kuberentes? It turns out to be a tricky thing. Here is
	a tutorial on how to enable Kuberentes to share NFS volumes.
	In the end of this tutorial we create a Deployment with a container sharing
	a directory from the host machine, and a few containers using this shared
	directory as a persistent volume.
---

First, let's start by clearing the motivation. Sharing NFS volumes requires
modifications of services and packages on a Linux server. If you want to set up
a server with NFS your first and easies option is to use SSH and set this up
manually on a server (maybe one of the worker nodes in your Kuberenetes cluster).
You can also set up a dedicated machines, or use a service by your cloud provider.
If you run a Kuberentes on premises, chances you have some dedicated NFS server,
or maybe even a more sophisticated service like NetApp). Doing SSH on a running
server an setting up NFS manually, is idea terrible. Having this configuration
save in Ansible Playbook is a bit better. The trouble is that you now have to
keep working in 2 different environments Ansible and Kubernetes. While both
offer declarative style configuration, you still need to switch context while
changing from one to another. Using only Kuberentes to configure you
infrastructure simplifies things a little bit (although, by no means, Kuberentes
is simple).
So, now that the motivation is clear let's jump right in. To run NFS server from
a containers the host has to have a kernel that supports NFS. In my case, my
hosts where using a kernel which didn't support it. So setting up NFS failed.

```
$ sudo apt install nfs-kernel-server
Reading package lists... Done
Building dependency tree
Reading state information... Done
nfs-kernel-server is already the newest version (1:1.2.8-9ubuntu12.1).
0 upgraded, 0 newly installed, 0 to remove and 4 not upgraded.
1 not fully installed or removed.
After this operation, 0 B of additional disk space will be used.
Do you want to continue? [Y/n] y
Setting up nfs-kernel-server (1:1.2.8-9ubuntu12.1) ...
A dependency job for nfs-server.service failed. See 'journalctl -xe' for details.
nfs-server.service couldn't start.
debconf: unable to initialize frontend: Dialog
debconf: (No usable dialog-like program is installed, so the dialog based frontend cannot be used. at /usr/share/perl5/Debconf/FrontEnd/Dialog.pm line 76.)
debconf: falling back to frontend: Readline
debconf: unable to initialize frontend: Dialog
debconf: (No usable dialog-like program is installed, so the dialog based frontend cannot be used. at /usr/share/perl5/Debconf/FrontEnd/Dialog.pm line 76.)
debconf: falling back to frontend: Readline
A dependency job for nfs-server.service failed. See 'journalctl -xe' for details.
invoke-rc.d: initscript nfs-kernel-server, action "start" failed.
● nfs-server.service - NFS server and services
   Loaded: loaded (/lib/systemd/system/nfs-server.service; enabled; vendor preset: enabled)
   Active: inactive (dead)

Apr 26 09:09:18 master-1-test systemd[1]: Dependency failed for NFS server and services.
Apr 26 09:09:18 master-1-test systemd[1]: nfs-server.service: Job nfs-server.service/start failed with result 'dependency'.
Apr 27 06:34:12 master-1-test systemd[1]: Dependency failed for NFS server and services.
Apr 27 06:34:12 master-1-test systemd[1]: nfs-server.service: Job nfs-server.service/start failed with result 'dependency'.
Apr 27 06:34:14 master-1-test systemd[1]: Dependency failed for NFS server and services.
Apr 27 06:34:14 master-1-test systemd[1]: nfs-server.service: Job nfs-server.service/start failed with result 'dependency'.
Apr 27 15:00:28 master-1-test systemd[1]: Dependency failed for NFS server and services.
Apr 27 15:00:28 master-1-test systemd[1]: nfs-server.service: Job nfs-server.service/start failed with result 'dependency'.
Apr 27 15:00:30 master-1-test systemd[1]: Dependency failed for NFS server and services.
Apr 27 15:00:30 master-1-test systemd[1]: nfs-server.service: Job nfs-server.service/start failed with result 'dependency'.
dpkg: error processing package nfs-kernel-server (--configure):
 subprocess installed post-installation script returned error exit status 1
Errors were encountered while processing:
 nfs-kernel-server
E: Sub-process /usr/bin/dpkg returned an error code (1)
ubuntu@node-2-test:~$ uname -r
4.4.0-1044-kvm
```

Switching to the generic kernel of ubuntu fixed the issue.
This is done by doing:

```
$ sudo apt install linux-image-generic
$ grep menuentry /boot/grub/grub.cfg
...
$ sudo grub-reboot '1>6'  # you probably want to change this number
$ sudo reboot
```
After the reboot:

```
ubuntu@node-2-test:~$ uname -r
4.4.0-146-generic
```

Now, that the host OS is ready we can continue to deploy a kuberentes Pod
which serves NFS. This Pod is deployed with the following manfiest:


```
---
# Run the NFS server a Pod

kind: Pod
apiVersion: v1
metadata:
  name: nfs-server-pod
  labels:
    role: nfs
spec:
  nodeSelector:
    kubernetes.io/hostname: node-2-test
  containers:
    - name: nfs-server-container
      image: oz123/nfs-server:0.1
      securityContext:
        privileged: true
      - mountPath: /srv/exports0002
        name: exports0002
      securityContext:
        privileged: true
      env:
       - name: MOUNTS
         value: "/srv/exports0001"
  volumes:
   - name: exports0001
     hostPath:
       path: /srv/exports0001
       type: DirectoryOrCreate
```

Note the following things about the manifest:

1. I specified that the pod should run on `node-2-test` using a `nodeSelector`.
   That is the node where I previously installed a kernel that supports NFS.
   You can use any other selector or none if all your hosts support NFS.
2. The container is running a privileged container. This is required for two
   reasons, the obvious one is that the container will try to create a new
	 directory in `/`, using the directive `DirectoryOrCreate`. The less obvious
	 one, is that NFS needs to run as root too. Other wise the a Pod trying to
	 mount a shared volume will encouter error.

The [container which runs the NFS server][1] deserves some explanation too. If you
try to understand what is going on in it, you might have some difficulty.
First, this container is quite unusual, since it uses an init to start multiple
process and restart them if the crash.
This is done by [installing runit][2]. Runit manages services by watching
directories  in `/etc/sv`. A service is defined as directory with the following
scripts at list:

```
/etc/sv/<service>/run
/etc/sv/<service>/finish
```

https://wiki.debian.org/SecuringNFS
[1]: https://github.com/oz123/docker-nfs-server/blob/master/Dockerfile
[2]: https://github.com/oz123/docker-nfs-server/blob/master/Dockerfile#L3
