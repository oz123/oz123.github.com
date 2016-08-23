---
title: On learning Ruby coming from Python ...
author: Oz Nahum Tiram
published: 2016-08-23
tags: python, ruby
public: yes
chronological: yes
kind: writing
summary: I am learning Ruby, and coming from Python it's not a very easy thing. Ruby is confusing, it has a weird syntax, and things are not really simple as in Python. There are still many things which are like dark magic. There's `nil`, there are `gems` and `bundler`. And there is _Rails, isn't Ruby_. Ruby was good for so many people out there, and I am sure you can do amazing stuff in it. I already know it's never going to be my weapon of choice, but it's not bad knowing my way around it. I'd like to know how to set up a simple project, read and debug code, install gems and package ruby projects. I have been ignoring Ruby for too long.
---

I am learning Ruby, and coming from Python it's not a very easy thing. Ruby is confusing, it 
has a weird syntax, and things are not really simple as in Python. There are still many things which are like dark magic. There's nil, there are gems and bundler. And there is Ruby on Rails, isn't Ruby. Ruby was good for so many people out there, and I am sure you can do amazing stuff in it. I already know it's never going to be my weapon of choice, but it's not bad knowing my way around it. I'd like to know how to set up a simple project, read and debug code, install gems and package ruby projects. I have been ignoring Ruby for too long.

Well, that is a lie. I never ignored it. There many applications that I use, which are using Ruby, and the language always intrigued me. I met some really cool people working with this language, which made me curious about it. But I was afraid of entering a new realm, being incapable again in a programming language is something I am not really fond of, if the benefits are not that big for me.

Python offered more for me, coming from science and High Performance computing, so I picked it first, when I had to choose a scripting language to automate computational stuff. I didn't reject Ruby, but it didn't offer tools like Matplotlib, SciPy or Pandas. It had Rails, and that is all I knew about Ruby more or less. And unfortunately, that was enough to discourage me from learning it for the last 8 years. Alas, the time for me to learn Ruby has come.

A great catalyst for this is watching the video casts in destroyallsoftware.com, which often use Ruby. And here something Gary Bernhardt, who makes these casts, put very nicely in his cast about packaging in Python and Ruby:

> Python tends to have very good fundamentals, but not such good interface on top of them. Whereas Ruby tends to have not as quite thought out fundamental solutions, but the interface on it tends to be nicer.

This is a citation from 2011, when pip was so new, and there was no virtualenv-wrapper. Eventually, I think if your foundations are good, people will build good interfaces.

Installing ruby packages was for me always a magic, which I didn't understand. After watching this screen-cast, I understand better what is going on when I do gem install .... But I also think that Python does have a simpler and better interface for package installation. It's very UNIX, and it's simpler. There is no bundler, bundler exec, no multiple versions installed of a package installed inside a virtualenv (Ruby allows multiple versions installed side by side).

This is also a very large trend between the two languages, which I see early on. Python tends to be simpler where it can. It might not be as fun and magical an in Ruby. But it makes the code simpler and the maintenance easier. It is the Zen of Python, where “There should be one-- and preferably only one --obvious way to do it.” and readability and simplicity count.

Ruby has some cool tricks, and I think it's OK to use it. However, it will not be my weapon of choice, if can choose Python. Nevertheless, learning Ruby helps me understand things Python. This is either through reflection over stuff that has already become transparent or through rethinking aspects of Object Orientation and Design as are those expressed in Ruby when I compare them to Python. So despite my frustrations with Ruby, it's a fun ride, and I recommend investing sometime in looking into Ruby.
