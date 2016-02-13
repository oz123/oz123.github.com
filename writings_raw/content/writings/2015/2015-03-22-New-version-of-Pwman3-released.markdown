---
title: New version of Pwman3 released
author: Oz Nahum Tiram
published: 2015-03-22
tags: python, pwman3
public: yes
chronological: yes
kind: writing
summary: I finally managed to release a new version of pwman3, the console and network password manager. Read more about it here.
---

The `De-Facto` password manager a lot of people use is KeePass, which is truly
cross-platform, running on all major OSs, there is even an Android client, with 
QT and console clients. KeePass is full of features and is really great for 
personal use. 
However, for working in a team it KeePass simply horrible because the database is 
file based. So the following scenario is really possible.
A user opens the files over the shared directory (there is no locking...).
He makes some changes and saves it again. In parallel, another team member 
has a KeePass open, and he makes changes in the his copy of the file, 
which does not include the changes from the first user. 
He then saves the file, and the entries that were made by the first team member
are lost.
Pwman3, uses a network database such as MySQL or Postgresql (there is also 
support for SQLite for personal use). Hence, it is much more appropriate for 
use by a team of system administrators or power users. 
I picked up the development of of Pwman3 about 4 years ago, fixing little bugs, 
which I found using it. I then released new versions steadily, realizing how bad
was the code written, and with no testing at all. It became quite a challenge, and
then I decided to do a complete rewrite of the software starting from the most 
important feature of a password manager, the cryptographic engine. Soon, I re-worte
the whole text user interface and finally the database drivers. 
After 6 months of development, mostly at nights and weekend, I am happy to release
the new version, accompanied by proper documentation and testing.

Here you can find the  [documentation of Pwamn3][1] and the newly released version 
is on [pypi][2]. Pwamn3 has been tested on Mac OSX, Windows and Linux. 
It is easy to install and to work with. You should give it a try! 

[1]: http://pwman3.readthedocs.org/en/latest/ 
[2]: https://pypi.python.org/pypi/pwman3/



