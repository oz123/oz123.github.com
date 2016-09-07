---
title: Dockerfile quicky - templating with M4
author: Oz Nahum Tiram
published: 2016-09-07
tags: docker, linux
public: yes
chronological: yes
kind: writing
summary: >
	Creating abstracted Dockerfile is something I really wish existed. Every time, 
	I write a `Dockerfile` for a specific base image I must specify the correct
	package manager command. You either use `apt-get` or `apk` or `yum` or any other
	call for the package manager. This is unfortunately, not very reusable. But,
	here is a simple schema how to use M4 macros to achieve this abstraction.
---

Creating abstracted Dockerfile is something I really wish existed. Every time, 
I write a `Dockerfile` for a specific base image I must specify the correct
package manager command. I must call `apt-get` or `apk` or `yum` or any other
call for the package manager. This is unfortunately, not very reusable. 

I am comparing this to many years of experience with `salt-stack` which includes
a great wrapper around many common Linux package managers. This spares the
details of distinguishing between `apt`, `apk` or `yum` and `dnf`, you just
write `pkg.install` and you get your packages installed.

Here is a simple `M4` schema how to achieve this abstraction. A better
solution will probably involve Jinja2 templates ...
This can spare you the need to remember which package manager you need to use
in which Docker image. Here is a very quick intro, how to this.

First create an `m4` template:

```
$ cat Dockerfile.in 
FROM ifdef(`ALPINE', alpine, ubuntu)
MAINTAINER Oz N Tiram <oz.tiram@gmail.com>

RUN ifdef(`ALPINE', apk add --update --no-cache, 
          apt-get update && apt-get install -y) curl tar xz bash

```

Now, create a simple `Makefile`:

```
$ cat Makefile 
ALPINE ?=

ifdef ALPINE
	USE_ALPINE := -DALPINE
endif

dockerfile:
	@m4 $(USE_ALPINE) Dockerfile.in
```

Now you can create `Dockerfile` for your image from Ubuntu with:

```
$  make > Dockerfile
```

Or you can create a `Dockerfile` based on Alpine Linux:

```
$ make ALPINE=1 > Dockerfile
```
