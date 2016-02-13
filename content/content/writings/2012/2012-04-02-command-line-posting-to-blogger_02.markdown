---
title: Command Line Posting to Blogger
author: Oz Nahum
published: 2012-04-02
tags: Blogging, CLI, Web
public: yes
chronological: yes
kind: writing 
summary: Oh man, I'm really becoming a geek. I spend so much time staring at VIM that writing a Blog post using the Web interface seems cumbersome to me.   
---

Oh man, I'm really becoming a geek. I spend so much time staring at VIM
that writing a Blog post using the Web interface seems cumbersome to me.
I know about Google command line interface and I even wrote my own
little script to upload images to Picasa directly from Nautilus (good
times are gone, I don't use GNOME anymore). \

### Basic setup

So, in this post I will explore how post to Blogspot from the command
line in an elegant way. First we need to install Google's CLI tool,
let's grab it: \

    wget http://code.google.com/p/googlecl/downloads/detail?name=googlecl_0.9.13-1_all.deb

Now, let's install it: \

    dpkg -i googlecl_0.9.13-1_all.deb

OK, basically, now you are good to go. The documentation is fairly easy
to understand. Except maybe one note. The first time you will run the
command you will need to configure your client. The config files are
found in: \

    ~/.config/googlecl/config

Well done by googleres who put the stuff where I expected it. Do note,
when you run the config you will be asked for the name of your Blog.
This is NOT the subdomain, e.g. in my case: \

    linuxpixies.blogspot.com

Rather to correct answer is the title of the Blog: \

    Linux Pixies and Stuff

Spaces are digested very well. \

###  

### Making things Fancy

Until now you can post simple text files, or manually edit HTML (YUCK!).
Here comes the fun part. Editing simple text files and automagically
converting them to HTML. Enter markdown. \

####  

#### Markdown

Markdown is a sweet little thing I discovered using stackexchange.com.
The more I use it I want more. This thing is addicting, and even worse,
it makes me hate all other Wiki syntax! Especially TkWiki, which we use
in my workplace. Markdown has many many converters. I use
python-markdown2, so let's install it: \

    pip install markdown2

Now, if you are a pedant, you could make a Debian package, which is
actually better than just dumping Python packages. But pip can also
remove Python packages, so it's now that bad, after all.\
Anyway, at this point, you have python-markdown2 installed, and the
command `markdown` is at your finger tips. You can start writing your
post with your favorite editor, be it Nano, EMACS, Ed or VIM, when your
done, save it with an appropriate title and `md` suffix so you know
later it's Markdown. Now comes the fun part. \

###  

### Converting to HTML

    /usr/local/bin/markdown2  YourCoolPost.md > Title\ of\ Your\ Cool\ Post.html

Now, you can view it with: \

    firefox Title\ of\ Your\ Cool\ Post.html

It will be bare naked HTML, without any styling, but you will get a good
feeling how your post will look like. When your satisfied, go the next
step, publishing. \

###  

###  Publishing your Post

Easy as: \

    google blogger post Title\ of\ Your\ Cool\ Post.html

Done. \

###  

### Final Remarks

I am writing these final remarks from Google's own web interface to
Blogger. I wanted to see how my post looks like in real life. I was
amazed to find a plague of break elements. elements in my post.
Apparently, Blogger's engine parses the HTML once again when it's
submitted. Everywhere I had a line break in VIM using enter, I had
inside Blogger a break element. Quite upsetting, but just remember,
don't use to many of them inside VIM, and your post should look good.

Comments
--------

linuxpixie

Hi Shai, \
Thanks, I had no clue that googlecl is the repos already!!! \
That's really good news.

Shai

On Debian, googlecl is in the main repository (0.9.9 in Stable, 0.9.13
in Testing and Unstable). This means you can simply install it with
**aptitude install googlecl**, no need to download manually and use
low-level tools like dpkg. I suppose this also means it is available (or
will soon be available) in Ubuntu Universe, if not main.
