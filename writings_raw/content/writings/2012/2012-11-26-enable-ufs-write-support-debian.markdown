---
title: Enable UFS Write support under Debian
author: Oz Nahum
published: 2012-11-26
tags: Debian, Kernel, FreeBSD
public: yes
chronological: yes
kind: writing 
summary: A short memo on enabling UFS write support on Debian 
---

I recently installed FreeBD 9.0 on my laptop, side by side with Debian GNU\Linux. 
While I am very excited about FreeBSD, I am still not ready to turn it into my 
main operation system. Hence, from a time to time I would like to be able to 
stuff or exchange data between Debian an FreeBSD. 

So, here is how I recompiled the UFS module under Debian Wheezy, without the need
to recompile the whole kernel. 

    sudo apt-get build-dep --no-install-recommends linux-image-$(uname -r)
    mkdir ufs_rw
    cd ufs_rw
    apt-get source linux-image-$(uname -r)
    cd linux-3.2.32 
    cp -v /usr/src/linux-headers-3.2.0-4-amd64/Module.symvers .
    cp -v /boot/config-3.2.0-4-amd64 .
    make EXTRAVERSION=-4 O=~/ufs_rw menuconfig
    
if you feel like doing stuff with sed instead of the Curses Menu:

    make EXTRAVERSION=-4 O=~/ufs_rw  oldconfig
    sed -i 's/# CONFIG_UFS_FS_WRITE is not set/CONFIG_UFS_FS_WRITE=y/' ~/ufs_rw/.config
    
Then, continue with

    make EXTRAVERSION=-4 O=~/ufs_rw prepare
    make EXTRAVERSION=-4 O=~/ufs_rw outputmakefile
    make EXTRAVERSION=-4 O=~/ufs_rw archprepare
    make EXTRAVERSION=-4 O=~/ufs_rw modules SUBDIRS=scripts
    make EXTRAVERSION=-4 O=~/ufs_rw modules SUBDIRS=fs/ufs

Now, you find the compiled module under ~/ufs_rw/

    sudo modinfo fs/ufs/ufs.ko 
    filename:       /home/ozdeb/ufs_rw/fs/ufs/ufs.ko
    license:        GPL
    depends:        
    vermagic:       3.2.32-4 SMP mod_unload modversions 

you can install the module or just use it every time you need it.

    sudo cp ~/ufs_rw/fs/ufs/ufs.ko /lib/modules/3.2.0-4-amd64/kernel/fs/ufs/
    #to load the module:
    modprope -iv ufs.ko



