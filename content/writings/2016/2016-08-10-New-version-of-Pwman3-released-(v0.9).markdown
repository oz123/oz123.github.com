---
title: New version of Pwman3 released (v0.9)
author: Oz Nahum Tiram
published: 2016-08-10
tags: pwman3, cryptography, CLI
public: yes
chronological: yes
kind: writing
summary: Yesterday night I released a new version of my CLI password manager Pwman3. This is a major mile stone, with huge amount of changes and improvements. Read more to find about what changed, and what I learned writing this version.
---

Yesterday I released a new version of my command line password manager [pwman3 in pypi][1].
This version is 191 commits after the last announcement of pwman3 here (that was v0.6)
and 1 year and 3 months following.
I the mean while, I worked quietly on building a better password manager for the command
line, adding Python3 support for versions 0.7.x and even released version 0.8 and 0.8.1
un-announced.

So what happened in the mean while? People still reported bugs (less than before, which 
is good and bad). It's good because maybe pwman3 does what it advocates? It's bad,
because maybe no one except me uses it? Just released 0.8, a month ago, and I already
got on bug report (sadly from a user who still used version 0.5!). 

I also started writing more and more software in Python3 and realized I don't feel
like supporting Python2. If there are not so many users who use that software, 
I don't feel so obliged to keep support for legacy enterprise OSes which still
don't ship Python 3.3 and later by default. Hence, I decided to drop support for
Python 2 and code Pwman3 using Python3 only. 

This decision turned out to be very helpful when working with cryptographic modules
which process bytes and not strings. Since unicode in Python3 is bytes type, this
reduced a lot of code of handling strings and bytes. This also turned to be tricky
with Postgresql, since earlier versions of Pwman3 stored encrypted text in the database.

Postgres saves bytes and byte type not as `TEXT` type and uses the `pg.Binary` method
to insert bytes from Python (for the technically inclide this is the exact commit
for [inserting bytes to Postgresql][2]).

Another pending issue that was troubling me since a long time was PyCrypto. PyCrypto
had a terrible API, which took me a lot of time to control. It was impossible to 
build on Windows, and I had an ugly hack that downloaded the PyCrypto binary for
Windows. But that meant that Windows users could not install it from PyPi. At least
not without me further improving the default install command, but since my access 
to that other OS is very limited my abilities where limited. 

PyCrypto was not really actively maintained anymore, and the Python community moved
towards Cryptography, a new contender for being the default Cryptography library
for Python developers. My intent was then to replace PyCrypto with some other
library. 

I stumbled upon PyCryptodome, a fork of PyCrypto which offers (as it claims) a 
similar API, and can serve as a drop in replacement. This library is somewhat active
and offers wheels for Windows. So my initial try was to use it. 

This failed miserably. PyCrypto had a default BAD API, and even the maintainers
of PyCryptodome, who understand more than me in cryptography, decided to move away from it.

Along with this miserable failure, I learned that using AES encryption with ECB
mode is considered harmful and not safe, and that one should use AES with CBC mode.
Well, Pwman3 original developer used AES with ECB, and so moving away from it, meant
that the old database won't be readable anymore. 

Despite being an annoyance for the users, I decided that the migration from ECB
to CBC is worth the trouble. And if moving to CBC mode, I should opt to used an
easy API for best practice of encryption. This is what is offered by the `Fernet`
module of Cryptography. Easy out of the box AES encryption with CBC mode and hash
validation. 

So, I parted away from PyCryptodome and re-wrote the cryptography engine with
Cryptographys Fernet. This tured out to be easier than thought (Great API!, and 
way better documentation than PyCrypto and PyCryptodome). 

Using Cryptography, means that now users can install Pwman3 with SQLite without
a need for a compiler, on any platform where pip installed, which makes SQLite 
truly cross platform now!.

And finally, because I found [Fernet][3] so fascinating, I decided to create
a simple [pure Python implementation of Fernet][4] which can be used as a reference
for those wanting to study the code behind it.


[1]: https://pypi.python.org/pypi/pwman3/0.9.0
[2]: https://github.com/pwman3/pwman3/commit/2d45a27d3e64e41ec29cff2649035178377dac8b
[3]: https://cryptography.io/en/latest/fernet/
[4]: https://pypi.python.org/pypi/fernet/0.1
