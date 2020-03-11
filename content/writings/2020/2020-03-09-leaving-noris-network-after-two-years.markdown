---
title: Thoughts after leaving noris network after two years
author: Oz Tiram
published: 2020-03-09
tags: career, life
public: yes
chronological: yes
kind: writing
summary: >
	After two years at noris network AG, yesterday was my last day with this company.
  It has been a long time since it felt so hard leaving a company. In my two years
	I worked with really great people on some of the most cutting edge technologies.
	All these things were not possible without the help of so many great people with
	whom I worked with. Some of them might read this post, so here is a big thanks.
	I wanted to summerize my two years and gather all the lessons I learned in one place
	for my future self and others too.  
	It's quite hard summerize such an eclectic post. It's been a wild ride in noris network
	with lots of new technologies and ideas. We have had a lot of success. I would like
	to think that a great part was because we opted to work in a an open source matter,
	even thougah not all our projects where open source. This blog post is a summary of the
	good things we did, and the positive leasons we learned.  
	I hope reading through these will inspire you to choose a similar path.

---

After two years at noris network AG, yesterday was my last day with this company.
It has been a long time since it felt so hard leaving a company. In my two years
I worked with really great people on some of the most cutting edge technologies.
Mostly, I served as a Kubernetes and Cloud Native advocate\Architect\Developer.
It's hard to say what exactly what I did, but at times it felt like I was doing a lot.  

All these things were not possible without the help of so many great people with
whom I worked with. Some of them might read this post, so here is a big thanks.

I would like also to reflect on a few good things we - the small team I was part
of, but also the company as a whole - did together in the spirit
of open-source. I believe this really helped us succeed in pushing noris network
to quickly adopt new technologies and habits.

To start with, my team has adopted a git first workflow. We tried as much as
possible to avoid using our company's wiki, because internally we wanted to 
have rigorous review process on all documents we produced. This allowed us to
stay in sync with what the team does. As much as we could we used markdown and RST
formats together with Sphinx. This allowed us to create documents in HTML format
which are pleasant to read, and also have a very shallow learning curve.
Markdown formatting isn't more complicated than the syntax of MediaWiki or
Confluence. However, the most important feature of using Sphinx is inn my opinion
is that the documentation is stored in files which can be put in a version control
system. Having git as version control allowed us to collaborate on the documentation
and have review process. To some extent one can create automation for this
review process (for example spell checking, or style). A second great feature
of Sphinx is that one can have documentation weaved into the code of software
projects. Sphinx is widely used in Python projects, but not only. The Linux kernel
is using it, and some other highly visible Open Source projects. There are 
plugins for [documenting software project in many languages using sphinx][1].

Writing documentation is not enough. If you don't advertise, no one is
going to read your documentation. As the goal of our team was to spread the use
of kubernetes in the company, we used every possible opportunity to shout kubernetes
cloud native, CI\CD. This can be very annoying to some people. But it worked.
We managed to get this thing going. This opportunities might vary in your company,
but the ideas might still apply.

Talk about your ideas repeatadly: in the corridor, in the line to the coffee machine,
in the companies' training events and barbecues and bar-camps (noris network as a great
biannually conference which allows people to share their ideas). Hold a 15 to 30
minutes talk about your ideas. Pitch your idea and see if this solved people's
problems, there is a great chance someone else has the same problem, or he is already
started working on a solution. This allows you to recruit people to support your
idea or allows you to build on their solution and collaborate. Either way, it's a
win-win if there are no ego-fighting and NIHblog, publish 
If your company has an Intranet or internal blog, post there too. And when you
release a software package or a library make sure to create a news article about
it.

In the spirit of open-source, if your company has a chat software, create a channel
dedicated to this idea or software your are trying to promote where people can
share information and help each other with problems. Expect this to be time-consuming
at the beginning, since you are probably the best authority for that.

Find a local meetup that relates to the software\technology\idea.
If there isn't an active meetup, consider creating one. It's a great way to
find even more people that share the  same idea, or have the same problem to
solve, or have interest in learning this cool new technology.
We did, by the way, happen to launch the [Nürnberg CNCF meetup][2].

Help foster an Open Source mentality: Every company with a decent size is pre-destined
to re-invent solutions locally. This means a lot of wasted energy, time and money.
Adopting inner open source culture means that people know what happens currently in
the company. In noris network we adopted a process similar to the one already used
by large open source communities - we called it PIEP, which stands for
Products, Innovations, Enhancement Process. Sounds similar to [PEP][3], [KEP][4] or [JEP][5]?
Right, we didn't invent the wheel. We fostered a process where everyone can suggest
the most crazy idea, or not so crazy solution, pitch it, get budget and time to work
on together with other stake holders.
Sounds crazy? Consider the alternative where two different departments or employees
implement a similar-we-have-a-workstation-under-the-table-with-build-server-style
solution. You know what I mean right? Your last company's chat server was set up
this way, right?
Managing any project like a software project isn't a bad idea. It forces your to
write your assumptions, assess the risks, and gather supporters. Alternatively,
you find out that somebody has already solved your problem, which, allows delivering
more value.

Remove barriers and lead by doing. If you want people to use your software or ideas
it is not enough to talk about it, or create management guidelines. You should make
it darn easy to use. Want people to adopt kubrenetes? [Find and installer that
is easy to use or build one][6].

At times, it felt like moving a 300 person company is impossible. Days like
this where mentally dragging down. As my fellow put it, a company culture is read
only. But at other times, most of the time actually, it felt like small battles
are won. You see fellow engineers using kubernetes, people coming through the 
door to ask you something about CI\CD, Docker, kubernetes or even simple stuff
as coding style guidelines.
Being on the cutting edge, or simply being an innovator, you will always feel
like change is impossible. However, changes happens slowly, and people start seeing your
work as valuable. That feels fantastic, but you need patience.

To summarize, my two years in noris network felt like almost a decade, and I wish
I could see seeds I planted grow into mighty trees. On the other hand I am already
looking forward to start the next challege in my life. Managing a small distributed
team of software engineers. It's going to be fun!

[1]: https://www.sphinx-doc.org/en/1.5.1/domains.html#more-domains
[2]: https://www.meetup.com/Kubernetes-Nurnberg/
[3]: https://www.python.org/dev/peps/
[4]: https://github.com/kubernetes/enhancements/tree/master/keps
[5]: https://openjdk.java.net/jeps/0
[6]: https://github.com/noris-network/koris
