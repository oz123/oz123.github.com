---
title: backup and restore with duplicity
author: Oz Nahum Tiram
published: 2018-10-07
tags: linux, shell
public: yes
chronological: yes
kind: writing
summary: >
  Duplicity backup utility is the old workhorse in all recent Ubuntu versions.
  I use the GUI called Deja-Dup for quite a while now. But until now I never bothered
  to check how to restore my files. I did decide to check how to restore file,
  because backup is only half the job! It turns out, that the GUI does a disservice
  for duplicity users. Restoring an encrypted backup turned out to not work.
  I didn't bother to research why, and turned to the CLI. This is a reminder on
  how to restore the files.
---

Duplicity backup utility is the old workhorse in all recent Ubuntu versions.
I use the GUI called Deja-Dup for quite a while now. But until now I never bothered
to check how to restore my files. I did decide to check how to restore file,
because backup is only half the job! It turns out, that the GUI does a disservice
for duplicity users. Restoring an encrypted backup turned out to not work.
I didn't bother to research why, and turned to the CLI. This is a reminder on
how to restore the files.
duplicity accepts the decryption passphrase using only an environment variables.
For new comers to Linux and CLI it might look strange. However, [current linux versions
do not leak environment variables via PS][1].
So without much further words, here is how to restore a backup from an external drive:

```bash

$ export PASSPHRASE=YourVeryS3kr3tBackupK3y
$ duplicity restore  file:///path/to/volume/containing/backups /path/to/restore/location/

```

Duplicity, is quite easy to use, and I like the fact that my desktop reminds me regularly
to backup. When I plug a certain USB hard-drive backup simply starts and goes on without
me having to think about it too much.
I wish restoring was that easy, but that's not the case. 
One more extremely bothering issue, is that duplicity is practically about to die with Python2.
I hope it's not the case, but it seems duplicity has reached it's end, and no one is really
working on it.



[1]: https://unix.stackexchange.com/a/369568

