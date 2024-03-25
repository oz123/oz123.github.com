---
title: Decrypting bcachefs volumes at boot
author: Oz Tiram
published: 2024-03-25
tags: Linux, Gentoo, bcachefs
public: yes
chronological: yes
kind: writing
summary: This blog post describes how to mount an encrypted array of bcachefs disks at boot time.
---

I have been playing with bcachefs on virtual machines for more than 3 years now.
With the merge of bcachefs into the mainline Linux kernel, I decided I want to
try bcachefs on real hardware.
The problem was that `/etc/fstab` does not support bcachefs arrays nor there was
a way to decrypt volumes at boot.
Hence, it was time for me to roll my sleeves up and come with my own solution.

First, I had to teach `bcachefs-utils` to accept a new command line flag to
read a decryption key from a file. My [PR for adding an option to read a password
from a file][1] got accepted without much re-work.
In this way, one can boot a main root partition
encrypted with LUKS, which is then mounted decrypted using familiar tools.
This partition will then have a key file which is passed to bcachefs-tools.

The process is then:
```
 grub2->dracut (initram-fs)->LUKS->bcachefs-utils decrypts secret->init mounts an array
```

I am not going to describe how to boot from a LUKS encrypted partition since this process
is well documented for almost every Linux distro out there.

First, I created a bcachefs array using the following command:

```
# bcachefs format --compression=lz4 --encrypted --replicas=2 --label=nvme0 /dev/nvme0n1 \
     --label=nvme1 /dev/nvme1n1 --label=nvme2 /dev/nvme2n1 --label=nvme3 /dev/nvme3n1 
```

This prompts for a password, type it and keep it somewhere safe.
Now, if you attempt to mount any of the drives in the array, or the complete array, you
will get an error:

```
# mount -t bcachefs /dev/nvme0n1:/dev/nvme1n1:/dev/nvme2n1:/dev/nvme3n1 /srv
mount: /srv: mount(2) system call failed: Required key not available.
       dmesg(1) may have more information after failed mount system call.
```

Now, you can test that the password works.

```
# mkdir -v /etc/bcachefs-mount/
# echo "YourSecretPassword" > /etc/etc/bcachefs-mount/secret
# bcachefs unlock -f /etc/bcachefs-mount/secret /dev/nvme3n1
```

Since, all disks in the array are encrypted with the same key, it is enough to unlock just
one disk. Now, the mount command should work:

```
# mount -t bcachefs /dev/nvme0n1:/dev/nvme1n1:/dev/nvme2n1:/dev/nvme3n1 /srv
# df -h /srv/
Filesystem                                           Size  Used Avail Use% Mounted on
/dev/nvme0n1:/dev/nvme1n1:/dev/nvme2n1:/dev/nvme3n1  3.4T   13M  3.3T   1% /srv
```

Now, this still isn't happening at boot time. The unlock and mount steps can be automated
as a systemd unit or an openrc service which can be invoked at boot.
I am not using systemd at home, so I am going to share my openrc service, but it should be
easy to port.

First, I created my own copy of `fstab` with a similar structure:

```
$ cat /etc/bcachefs-mount/fstab

# group      mount  point
/dev/nvme0n1:/dev/nvme1n1:/dev/nvme2n1:/dev/nvme3n1 /srv
```

This file is parsed by my init script to determine which array is mounted where.

Also, the init script reads a secrets file, which finds a decryption secret for a device:

```
# disk secret
/dev/nvme0n1 /etc/bcachefs-mount/srv
```

The file `/etc/bcachefs-mount/srv` contains the password.

The init script runs a function at start which decrypts each disk and then mounts each array:

```
SECRET=/etc/bcachefs-mount/secret
FILE_SYSTEMS=/etc/bcachefs-mount/fstab

start() {

    # check if the file exists
    if [ ! -r "${FILE_SYSTEMS}" ]; then
        ebegin "configuration file not found."
    	eend 1
    fi
    
    if [ -r "${SECRET}" ]; then
        while ifs= read -r line; do
            # skip lines starting with '#'
            case "$line" in
                \#*) continue ;;
            esac

            # set the ifs to a space
            ifs=' '

            # read the line into positional parameters
            set -- $line

            # assign the first part to group and the second part to mount
            dev="$1"
            secret_path="$2"

            ebegin "Unlocking device: ${dev} with secret from ${secret_path}"
	    ebegin bcachefs unlock -f "${secret_path}" "${dev}"
	    bcachefs unlock -f "${secret_path}" "${dev}"
            unset ifs

            if [ $? -ne 0 ]; then
               eend $?
            fi

        done < "${SECRET}"
        eend 0

    fi
    # read each line from the file
    while ifs= read -r line; do
        # skip lines starting with '#'
        case "$line" in
            \#*) continue ;;
        esac

        # set the ifs to a space
        ifs=' '

        # read the line into positional parameters
        set -- $line

        # assign the first part to group and the second part to mount
        group="$1"
        mp="$2"

        ebegin "Mounting group: ${group} at ${mp}"
        # optionally, restore the original ifs value
        unset ifs

    	start-stop-daemon --start --exec /bin/mount -- -t bcachefs "${group}" "${mp}"
        if [ $? -ne 0 ]; then
           eend $?
        fi

    done < "${FILE_SYSTEMS}"
    eend 0
}
```

You can find [the complete openrc service in my repository][2]

[1]: https://github.com/koverstreet/bcachefs-tools/pull/241
[2]: https://raw.githubusercontent.com/oz123/dude/master/gentoo/etc/init.d/mount-bcachefs
