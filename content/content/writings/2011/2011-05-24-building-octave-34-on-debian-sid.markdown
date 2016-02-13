---
title: Building Octave-3.4 on Debian Sid
author: Oz Nahum
published: 2012-05-02
tags: Foss, Matlab, Octave, Programming
public: yes
chronological: yes
kind: writing 
summary: I wanted to build the latest Octave (3.4) on my Debian Sid. Well, it wasn't as easy as before, since I upgrade it quite often.    
---


I wanted to build the latest Octave (3.4) on my Debian Sid. Well, it
wasn't as easy as before, since I upgrade it quite often. So now, the
GCC-4.6 is used in Octave. However, due to some bugs in GCC-4.6 or
Octave(?), it won't build. So, the trick that did it for me:


    sudo aptitude build-dep octave3.2sudo apt-get install libgl1-mesa-dev libglu1-mesa-devsudo aptitude install gcc-4.5 gfortran-4.5 g++-4.5


than, we need to do something ugly, but it does work ... ;-)


    sudo mv /usr/bin/gfortran /usr/bin/gfortran.ORG
    sudo ln -s /usr/bin/gfortran-4.5 /usr/bin/gfortran

now we tell Octave to build using GCC-4.5:

export CC=/usr/bin/gcc-4.5export CXX=/usr/bin/g++-4.5

the rest is easy:


   ./configure 
   make 
   make test
   sudo make install
   sudo checkinstall

Et viola! A post which is more positive and not ranting! Octave 3.4 is
faster, and provides better Matlab compatability. Give it a try and you
won't look back!

