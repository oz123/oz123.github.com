---
title: Making Octave plot nicer
author: Oz Nahum
published: 2009-05-21
tags: Programming, Octave
public: yes
chronological : yes
kind: writing 
summary: Personally, I prefer Python over Octave/Matlab. But since I'm being forced to write Matlab code for one of my courses, I started playing around with Octave.
---

Personally, I prefer Python over Octave/Matlab. But since I'm being forced to write Matlab code for one of my courses, I started playing around with Octave.
By default octave makes ugly ugly plots because it uses the X11 terminal. But there's a solution, you can switch to wxt terminal. In order to do that, add in the bottom of your .bashrc the following line:
`export GNUTERM=wxt`

And a magic will happen:
Before:
[caption id="attachment_245" align="aligncenter" width="300" caption="UGLY !!!"][![UGLY !!!](http://www.tabula0rasa.org/wp-content/uploads/2009/05/octave-300x230.png)](http://www.tabula0rasa.org/wp-content/uploads/2009/05/octave.png)[/caption]

After:
[caption id="attachment_246" align="aligncenter" width="300" caption="NICE !!!"][![NICE !!!](http://www.tabula0rasa.org/wp-content/uploads/2009/05/gnuplot-300x237.png)](http://www.tabula0rasa.org/wp-content/uploads/2009/05/gnuplot.png)[/caption]

That's all folks.
