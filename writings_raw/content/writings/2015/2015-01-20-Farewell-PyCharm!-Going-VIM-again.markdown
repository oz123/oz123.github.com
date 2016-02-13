---
title: Farewell PyCharm! Going VIM again
author: Oz Nahum Tiram
published: 2015-01-20
tags: python, VIM, git
public: yes
chronological: yes
kind: writing
summary: A few months ago we migrated from PyDev to PyCharm. After a 3 months time where I lead the migration from PyDev to PyCharm and SVN to GIT, I am back again to work with VIM. Here are my thoughts about PyCharm.
---

A few months ago, we started working with git. It turned out that ECLIPSE with
PyDev is a real mess to learn with GIT. I talked about it with a friend, and 
he suggested that we try PyCharm. I had my doubts, that we could migrate from
SVN to GIT and simultaneously to PyCharm from PyDev.  

Never the less, I gave PyCharm a spin, and I found it surprisingly straight 
forward. There are no complicated workspaces and views to learn when working 
with GIT. Everything else, like introspection, and project management is really 
a breeze when comparing to PyDev. Even the debugger is really nice to work with. 

What was really weired for me, but really easy for my team, was that PyCharm 
tries to make working with git similar to working with Subversion. It really 
does work for people who com with long SVN history.

However, as my colleagues started to become more convenient with GIT, it turned 
out that PyCharm's intensive caching is really not playing well with git, if you
start working with git directly through a terminal. 

Here is where I am partly fault. While I tried to learn the PyCharm interface, 
I always found that I am faster to cherry-pick or merge or do any git action 
on the shell. So, even when I was sitting with colleagues to do some peer working
on our Software I was showing them the underlying git command. 

Slowly, they started also to get annoyed with the fact that PyCharm's interface
to git is a bit cumbersome, and that git's awesome command completing and 
ability to share git alias and `.config` files is simply faster and easier. 

So now, that everyone is feeling comfortable working with git on the shell, I no
longer feel obligated to work with PyCharm and learn it, so I could help my 
colleagues. Hence, I am back to VIM, and the best interface to git after git 
commands on the shell is `vim-fugitive` if you don't know vim fugitive, watch 
these bunch of screencasts linked in [vim-fugitive's home-page][1].

To sum it up, I really found PyCharm better then PyDev, because it easier to 
understand and to work with. It's Version Control interface, is a bless for SVN 
new comers for git, but at the same time it is very limiting for people who 
really know git. It really helped us migrating to git, but when things became 
more complicated we ended up working with git in the shell, until we really didn't
need or want to use PyCharm's Version Control interface. May be Jetbrains should 
consider enabling git power users turning off this SVN compatibility. For me, 
it's already too late. I am back to VIM. 

And finally, I am a big fan of [the solarized color theme][2]. 
I really missed it in PyCharm -But I also found PyCharm's darcula color theme 
really pleasant. Changing from PyCharm to VIM a couple of times a day 
looking at text with different themes was an eye irritating experience. 
Hence, I changed my default color theme in VIM to [darcula-vim][3], 
and I don't really miss solarized ...

[1]: https://github.com/tpope/vim-fugitive
[2]: https://github.com/oz123/solarized-mate-terminal   
[3]: https://github.com/alem0lars/vim-colorscheme-darcula
