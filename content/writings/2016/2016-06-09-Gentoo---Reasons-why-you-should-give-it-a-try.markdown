---
title: Gentoo - Reasons why you should give it a try
author: Oz Nahum Tiram
published: 2016-06-09
tags: gentoo, linux, programming
public: no
chronological: yes
kind: writing
summary: Type your summary here.
---

About a year a go I stopped using Debian completely (I'm still using Ubuntu
partially) and made Gentoo my primary Linux distribution of choice. If you 
are doing some kind of software development or advanced linux usage (I'll coin
that term soon) I believe you should definitely consider trying Gentoo, and 
in the long run move to it.  
But first, let's bust some myths!

### Gentoo is hard! Only for hackers or hard core Linux frikzzzzz

Gentoo is already being indirectly used by millions of people running around
with Chromebooks. Gentoo is deploying with every instance of CoreOS. 
You can argue that since these gentoo variants don't come with a package 
manager, or not meant to be upgraded constantly, they are  not real Gentoo. 
But never the less, they are being produced with Gentoo, 
and so can you achieve Linux Nirvana on your Laptop, Workstation or Server(s). 

### But I have to compile everything ...

First of all you DON'T have to compile everything. Gentoo's portage supports
creating binary packages and installing binary packages. 
It's just that Gentoo's community belief that you should compile everything, 
if not as an learning excercise, than as a means of allowing you to stich your
own best suite of software packages.

Never the less, Gentoo supplies some binary packages to software which it's 
upstream vendors supply those packages pre-built. 
A few examples are: Oracle's Java, node.js, Firefox, and Chromium Browser. 
At the time of writing this post, searching for 'bin' packages yields
in in the gentoo package archive yields
more than 80 packages.

You can also install other binaries, supplied by Debian packages or RPM packages, 
if they don't have to many dependancies. As an example you can take any Ubuntu
kernel, unpack it and use it for your own Gentoo. You will then be responsible 
of upgrading it when security flaws are found.

So, you don't have to compile everything. And even than, Gentoo's build system
is so awesome (see below) that it really eases the task comparing to building
RPM or DEB packages. Now, if you have been using Linux more than a couple of years
or you do software development, chance are that you did compile software on your
own. Which brings me the the next section.

### You sohuld consider Gentoo if ... 

If you ever worked in a corporate environment, there is a really good chance
you have had to compile software or distribute software packages to more than
one machine.

If you are a hobbyist loving a particulare software package, and you can't wait
for your favorite Linux distro to package the latest and shiniest, you have 
been building from source.

If you always felt that for your laptop Debian stable is too old, and you have
been running "Testing" or "Unstable" you have been experience frequent updates, 
not often, but stiil, some stuff would break and you would pin packages.  

If you maintain more than one Linux box ...

For me these are all advanced usages of linux, which justify the consideration 
of Gentoo.

### Gentoo's build system and Package manager - Portage, its good for you!

As said above, chances are that if you are a power user, you have been building
packages. And if so, you have an opinion about it, and your own set of tools. 
I want to quote a long time Debian developer, Lars Wirzenius, 
regarding [build systems](http://blog.liw.fi/posts/debian-developing-it-wrong/):

> Build tools should be intelligent, packaging should be dumb 

And further:

> Making packaging intelligent, rather than the build tool, means packagers need 
> to do more work, and there's more work to do when, say, 
> the Debian policy changes, or when there are other changes that affect a 
> large number of packages. If packaging is intelligent, then every package
> needs changes. If the build tool is intelligent, 
> then you change the build tool and re-build everything.

And he has a point. To see how is point is affecting Debian in real life, I want
to share a piece of data that shocked me when I first noticed it. That is
the number of packages available in Debian vs. the number available in Gentoo.
As of now, Debian's website contains the following statement:

> Debian provides more than a pure OS: it comes with over 43000 packages, 

[Debian is 6 years older and currently has 1033 active developers](https://en.wikipedia.org/wiki/Debian#Organization).

Currently, Gentoo offers a [humble number of 19039 packages](https://packages.gentoo.org/), 
and has about 240 active developers[1]. So, with an about the quarter of Debian's
human resources, Gentoo's developers make almost half the size of Debian's package
collection. If Gentoo had the amount of Debian developers, it had the stunning amount
of more that 80,000 packages to choose from. So, creating Debian package is
hard even for skilled people as Debian developers themselves. RPM based distro
are even more worse. [RHEL has only 9617 source RPMS](https://git.centos.org/project/rpms).
And that is the largest by USD value open source company...

So now that we set some background, I hope the potential of portage is clear
to you.


#### How easy is it to build a Gentoo package? 

A gentoo package is a simple bash script file ending with `.ebuild`. So all 
you have to do is edit a single file (with a relativly familiar language). 
Here is how gentoo is building `figlet`:

```
# Copyright 1999-2014 Gentoo Foundation
# Distributed under the terms of the GNU General Public License v2
# $Id$

EAPI=5
inherit eutils bash-completion-r1 toolchain-funcs

DESCRIPTION="program for making large letters out of ordinary text"
HOMEPAGE="http://www.figlet.org/"
SRC_URI="ftp://ftp.figlet.org/pub/figlet/program/unix/${P}.tar.gz"

LICENSE="BSD"
SLOT="0"
KEYWORDS="~alpha amd64 arm hppa ~ia64 ~mips ppc ppc64 ~sparc x86 ~x86-fbsd \
 ~x86-interix ~amd64-linux ~x86-linux ~ppc-macos ~x64-macos ~x86-macos"
IUSE=""

src_compile() {
	emake clean
	emake \
		CC="$(tc-getCC)" \
		LD="$(tc-getCC)" \
		CFLAGS="${CFLAGS}" \
	    LDFLAGS="${LDFLAGS}" \
		prefix="${EPREFIX}/usr" \
		all
}

src_install() {
	emake \
		DESTDIR="${ED}" \
		BINDIR="${EPREFIX}/usr/bin" \
		MANDIR="${EPREFIX}/usr/share/man" \
		prefix="${EPREFIX}/usr" \
		install

	doman chkfont.6 figlet.6 figlist.6 showfigfonts.6
	dodoc README figfont.txt

	dobashcomp "${FILESDIR}"/figlet.bashcomp
}
```

Of course it's not plain BASH, and you have to know what each function is doing, 
and what each variable is doing. But that is all documented in a very good [manual
for creating ebuilds](https://devmanual.gentoo.org/ebuild-writing/).
Compare this ebuild, composed of a single file to the following stuff needed
to create a package for debian:

```
$ tree debian
.
├── changelog
├── clean
├── compat
├── control
├── copyright
├── dirs
├── docs
├── examples
│   └── moolets
├── figlet.el
├── manpages
├── patches
│   ├── makefile_set_debian_buildflags.patch
│   ├── makefile_set_debian_paths.patch
│   └── series
├── postinst
├── prerm
├── rules
├── source
│   └── format
└── watch

3 directories, 18 files
```

Ignoring the fact the debian includes here patches, you see a much complicated 
build system. 

And that is just a simple example. Creating rule files is generally a task so 
complicated that normal people who don't to upload packages to the debian 
repository opt for using tools like [fpm](https://github.com/jordansissel/fpm).
The same goes for creating RPM, altough, personally I think creating RPMs is
a bit more simple compared to creating Debian packages. 

####  Reusing Built packages

Building packages is only half the story. If you need to distribute packages
to your machines, building Debian repositories and RPM repositories is also 
not the easiest task. Although I used Debian much longer, 
and prefered it for social reasons, I feel that creating and maintaining RPM 
repositories for CentOS and Red Hat is much simpler. But both are complicated 
tasks comparing to creating a [binary package host for gentoo][2].

If you have one machine in the network which builds packages, this machine can 
serve your binary packages to all other machines. 
This is where in my opinion Gentoo's excellent handbook falls short! The user
guide tells and shows an example with the following CFLAGS:

```
CFLAGS="-march=native -O2 -pipe"
```

So you end up installing one machine in which you compile many packages, and then
you realize that when you install another machine chances are you can't use the
compiled packages. My recommendation, if you have machines with Intel CPU, choose
the architecture of the oldest one in your hands, newer models are backward 
compatible. For example I have a few laptops with Intel Core i7 and Core i5 CPUs. 
So on all my machines I have the following CFLAGS:

```
CFLAGS="-march=haswell -O2 -pipe"
```

This is the architecture of the Core i5 CPUs. So I build packages once and 
distribute them to all my laptops. You can also use broader categories and CFLAGS
such that you can build packages for AMD and Intel CPUs.

### The Quick and dirty installation of Gentoo

First of all - Don't do quick and dirty things. Learn the tools you use. If you 
don't have time to read the Gentoo book all at once, install gentoo in the way I 
show you, but promise to read the book in short intervals with your morning coffee
or at lunch break 15 minutes a day! 
It will make solving problems, when they arise, quicker. 

The hand book will lead you to install gentoo with a bare `stage 3`. You can 
immidietly work with a `stage 3` inside a chroot envrionment, almost as you would
work with a plain `debootstrap`ed Debian. So all you need is a partition on 
your hard-drive to play with. 

Another option is to install Gentoo with a Vagrant image (Personaly, I never 
tried them so I don't know how safe they are).

Gentoo's package manager is not like apt, yum or dnf. It's a different beast.
If you know what RPM dependency hell is, you are an avid or long time Linux 
user, Gentoo's version for that is called `blocked` and `masked`. Most chances, 
that you won't experience that, but you will need to read about dealing with
building hardships. Read about them in [when Portage is complaining][3].

Once you are feeling safe with portage, you can try boot Gentoo. Again, here
the handbook will show you how to compile a kernel. Compiling a kernel is a task
that should be automated. There is some work in this direction, but until than, 
optimizing a kernel for many machines, and many periferal is not something you
should waste your time on! 

Do you have all your machines and devices working with the latest Ubuntu? Great!
You can reuse this kernel with Gentoo!

*TODO: Addd instructions for that*

*WARNING* this is the DIRTY part. This will boot your system, but you won't get
any security or patches. 

your shoulder! You can build a kernel your self with Ubunutu kernel Configuration. 
Now you are no longer using a dirty solution. And you can reuse this kernel with 
all your machines too.

From now on you can keep using this huge configuration (which compiles a lot of
modules and things you don't really need), or when you have free time, you can 
look inside and removed modules for controllers you don't have, or input devices 
you'll never buy. It's a good learning excercise.

### Wrapping up ...

Installing Gentoo, and using Gentoo isn't hard as you think, or contrary to common
mind. Gentoo's handbook, is a great learning resource, but you don't necessarily 
need to follow the installation in the A to Z path. I recommend skipping the kernel
chapters in the beginning, and concentrating on Portage usage. After all, the kernel
is a package you rarely care for, upgrade or use, where as, other packages are being
installed and used more often. 
After you trust yourself with portage, try composing your own bootable system, 
with a pre-built kernel. 
Once this system boots, compile your own kernel with a pre-configured configuration
file. And once you are done with that, you can try and create your own minimalistic
kernels.
Usually that last step is not something you need to do, and gives you no real 
benefit, besides a better understaning of all the Linux Kernel components. 
Finally, you are now done with the Gentoo handbook, although you didn't read it
as intended, and you can use gentoo on one or more machines. 
A few recommendations for being a gentoo user.  Gentoo is, like 
any other system, breakable! But no Gentoo system breaks on its own. 
Keep a backup of your `etc` directory and especially
`/etc/portage`. It will save you time if you break things. 
you a lot of time if *you* break things. Don't go and upgrade `@world` without
understanding what your are doing. Doing this is like doing an Ubuntu upgrade 
from an LTS to a non LTS version while drunk. You have been warned. 
Have fun using Gentoo. 


[1]: https://www.gentoo.org/inside-gentoo/developers/
[2]: https://wiki.gentoo.org/wiki/Binary_package_guide
[3]  https://wiki.gentoo.org/wiki/Handbook:AMD64/Working/Portage#When_Portage_is_complaining:
