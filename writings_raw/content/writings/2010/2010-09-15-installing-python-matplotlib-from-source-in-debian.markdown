---
title: Installing python-matplotlib from source in Debian
author: Oz Nahum
published: 2010-09-15
tags: Python, Debian, Programming
public: yes
chronological : yes
kind: writing 
summary: Hoora Debian ! I love how every past experience of developers brings something useful ! If you need to build python matplotlib from sources you need to install quite a lot dependencies. Luckily for me in Debian it's quite easy.
---

Hoora Debian ! I love how every past experience of developers 
brings something useful ! If you need to build python matplotlib 
from sources you need to install quite a lot dependencies. 
Luckily for me in Debian it's quite easy.
Here is how to build this wonderfull tool in Debian.

First, remove the old python-matplotlib supplied by debian.
`apt-get remove python-matplotlib`

Then, install the dependencies:

`apt-get build-dep python-matplotlib`

Finally, continue with the instructions as the following:

`cd matplotlib
python setup.py build
python setup.py install
`

Then to verify installation succeeded:
`$ python
Python 2.6.6 (r266:84292, Aug 29 2010, 19:11:12)
[GCC 4.4.5 20100824 (prerelease)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import matplotlib
>>> print matplotlib.__version__
1.0.0`

