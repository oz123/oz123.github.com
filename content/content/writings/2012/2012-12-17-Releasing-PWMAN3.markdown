---
title: Releasing PWMAN3 v.0.2.1
author: Oz Nahum
published: 2012-12-17
tags: Python, Programming
public: yes
chronological : yes
kind: writing 
summary: pwman3 is a command line password manager written in Python. Pwman3 was originally started by Ivan Kelly, and published on github. I recenty became the maintainer, and now version 0.2 is released. Read more about it ...
---

pwman3 is a command line password manager written in Python. 
Pwman3 was originally started by [Ivan Kelly](https://github.com/ivankelly), 
and published on github.     
I bumped into this little application when I looked for a command
line alternative to the notorious mono based Keepass. 
Since pwman3 is writtne in Python I tried compiling it on Windows, 
which turned out to be harder than I thought, because of the dependencies
on PyCrypto. Eventually, I got it working, but the output looked quite 
funny because it was meant to be printed to a UNIX console.   
So, I lifted my sleaves and modified the code so it prints  clear unformated 
text on Windows.  
Than, I had the idea I could directly copy the password to the clipboard
and paste it. Again, I did some coding ... and even sent a pull request to Ivan. 
Suprisingly, he incorporated it quite fast, and after a few pull request, 
and correspondence with the [Debian maintainer of PWMAN3, Emmanuel Bouthenot](kolter@debian.org), 
I became the maintainer of PWMAN3. 
I set up a repositoy in github together with Ivan Kelly, and started merging
pull request of other people. Soon, came the idea to add the copy to clip
board of Mac OSX, and some more ideas.  
I started reading more code and did some more changes like using argparse.  
First buds of better documentation also started appearing, and after 37 commits
I decided to release a newer version of PWMAN3.  
Thanks to the clear coding style of Ivan Kelly, I know already how most of 
pwman parts talk to each other and what is going under the hood.   
[A friend who is security minded](https://twitter.com/huland) had encouraged me to
review the encryption mechanism. But this is still in the pipe.  
Working on this project in little bits when time allows is definitley a privielige,
becuase I get to learn so many things, here is a partial list:

   * github and git usage have become way more fluent. 
   * SQLITE, which was always on my list, is now no longer strange land. 
   * getting to use in real project class overloading and inheritance outside
   of text book scope or homework.
   * learning to use Python's distutils.
   * some more VIM tools I learned like vim's [python-mode](https://github.com/klen/python-mode) 
   and [syntastic](git://github.com/scrooloose/syntastic.git) which I started using more heavily. 


So, without further a due, here you can find PWMAN3 [tar balls](https://github.com/pwman3/pwman3/archive/v0.2.1.tar.gz) 
and a [zip file](https://github.com/pwman3/pwman3/archive/v0.2.1.zip) of version 0.2.1.     
I hope you find it useful. 
