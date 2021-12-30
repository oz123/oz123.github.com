---
title: Announce - CoreDNS Netbox Plugin v0.2, now with IPv6
author: Oz Tiram
published: 2021-12-30
tags: CoreDNS, Golang, Netbox
public: yes
chronological: yes
kind: writing
summary: >
    I just released the 2nd version of my CoreDNS plugin for getting DNS records from Netbox. This release adds IPv6.
---

I started this CoreDNS plugin while working in a startup which used Netbox to manage their infrastructure.
We needed a DNS, and I suggested to use CoreDNS, since it's already in every Kubernetes plugin.
As a bonus, it's easy to extend I argued. To make a PoC, I spent a night on a weekend to query records from netbox.
The CoreDNS maintainers were kind to offer their help, and even linked the plugin in the list of plugins, even
though it was very early in developement.
Eventually, the company chose not to use CoreDNS and I forgot about this plugin for a while. However, recently
I installed Netbox for a client of mine (for whom, I build bare metal Kubernetes clusters), and I thought it would
be nice to pick it up again. To my surprise, the plugin has got more than 20 Github stars from people I don't know.
A possible sign, that people actually use it out there.
This new version includes a small refactoring of the query code to handle hosts with multiple IPs and IPv6.
To implement this support, I also added a docker-compose setup and a set of make file to automate building and
testing against a real netbox (an integration test suite if you want to call it). The code for this suite is
still in the closed source repository. However, there is good unit test coverage and examples which allow you to
quickly get comfortable using the plugin.
You can find the latest release in the [project's Github page][1].

[1]: https://github.com/oz123/coredns-netbox-plugin/
