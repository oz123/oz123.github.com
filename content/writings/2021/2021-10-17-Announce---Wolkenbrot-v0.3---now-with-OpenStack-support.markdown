---
title: Announce - Wolkenbrot v0.3 - now with OpenStack support
author: Oz Tiram
published: 2021-10-17
tags: Linux, DevOps, Cloud, OpenStack, AWS
public: yes
chronological: yes
kind: writing
summary: >
	I have just released WolkenBrot v0.3 with OpenStack support.
	WolkenBrot is my own little program to bake cloud images.
	The name means "Cloud Bread" in German.
---

I have just released WolkenBrot v0.3 with OpenStack support. WolkenBrot is my own little
program to bake cloud images. Then name means "Cloud Bread" in German.
It's not equal in features to Hashicorp's Packer, but it's MUCH simpler to use and hack
on.

I recently started working with AWS again, after 5 years hiatus, and I still have clients
using OpenStack. Hence, I thought it would be useful to un-dust WolkenBrot and give it 
OpenStack support.

I've not used for 5 years, and it took me a few hours to add OpenStack support to it.
Mostly, because the Python Client for OpenStack is extremely easy to use.
Check out the [examples][1] on how to use it it.
Give it a spin and send some feedback!



[1]: https://github.com/oz123/wolkenbrot/tree/dev/examples
