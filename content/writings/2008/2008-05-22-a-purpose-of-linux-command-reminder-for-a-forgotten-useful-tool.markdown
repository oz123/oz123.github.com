---
title: A purpose of a linux command
author: Oz Nahum
published: 2008-05-22
tags: Linux, CLI
public: yes
chronological : yes
kind: writing 
summary: Ever happened to you that you needed to do something on your linux box and didn't know how ? Sure it did!
---


Ever happened to you that you needed to do something on your linux box and didn't know how ? Sure did!

In this case you usually call a friend or Google it. However, your linux box is full with documentation. If you don't know what to look for, a good place to start will be the command 'apropose'. This simple command knows which other command does what on your linux box.


Type in your terminal:

    
    'apropose'


and you'll be answered

    
    'apropos what?'


Now try:

    
    'apropos disk usage'


and you'll get  a list of commands dealing with disks and usage:

    
    baobab (1)           - A graphical tool to analyse disk usage



    
    cfdisk (8)           - Curses/slang based disk partition table manipulator fo...



    
    df (1)               - report file system disk space usage



    
    dvd+rw-booktype (1)  - format DVD+-RW/-RAM disk with a logical format



    
    dvd+rw-format (1)    - format DVD+-RW/-RAM disk



    
    dvd+rw-mediainfo (1) - display information about dvd drive and disk



    
    edd_id (8)           - udev callout to identify BIOS disk drives via EDD



    
    fdformat (8)         - Low-level formats a floppy disk



    
    fdisk (8)            - Partition table manipulator for Linux



    
    git-count-objects (1) - Count unpacked number of objects and their disk consu...



    
    hd (4)               - MFM/IDE hard disk devices



    
    hibernate (8)        - save your computer's state to disk, and then switch it...



    
    hibernate-disk (8)   - save your computer's state to disk, and then switch it...



    
    hibernate-ram (8)    - save your computer's state to disk, and then switch it...



    
    initrd (4)           - boot loader initialized RAM disk



    
    mkboot (8)           - makes a bootdisk



    
    netscsid (1)         - write data to optical disk media



    
    partx (8)            - telling the kernel about presence and numbering of on-...



    
    ram (4)              - ram disk device



    
    ramsize (8)          - query/set image root device, RAM disk size, or video mode



    
    rdev (8)             - query/set image root device, RAM disk size, or video mode



    
    resume (8)           - program to suspend to disk (hibernate)



    
    rootflags (8)        - query/set image root device, RAM disk size, or video mode



    
    s2both (8)           - program to suspend to disk (hibernate)



    
    s2disk (8)           - program to suspend to disk (hibernate)



    
    sd (4)               - Driver for SCSI Disk Drives



    
    sfdisk (8)           - Partition table manipulator for Linux



    
    suspend-keygen (8)   - program to generate a RSA key to be used by s2disk



    
    sync (8)             - synchronize data on disk with memory



    
    uswsusp.conf (8)     - Config file for the s2disk program



    
    vidmode (8)          - query/set image root device, RAM disk size, or video mode



    
    wodim (1)            - write data to optical disk media



    
    xspirograph (6x)     - simulates the rotation of a disk inside a circular rim



    
    du (1)               - estimate file space usage



    
    pod2usage (1)        - print usage messages from embedded pod docs in files


Wonder how it works ? Simple as that: apropose reads the man pages for you. But you'll have to read a little bit more to understand how each command works.
