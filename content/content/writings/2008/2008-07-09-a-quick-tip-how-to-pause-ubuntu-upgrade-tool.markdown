---
title: A quick tip - How to pause ubuntu upgrade tool
author: Oz Nahum
published: 2008-07-09
tags: Ubuntu, Linux
public: yes
chronological: yes
kind: writing
summary: I've been upgrading my ubuntu laptop since ubuntu 6.06, even though sometimes I break my installation and need to do a clean install... Never the less I think ubuntu's upgrade tool has no second in the linux world. It is mostly a reliable tool and usually does the job. But there is one thing that always annoyed me about it. Once you get it running you can't stop it, and if you stop it cleans all the packages downloaded. It's really annoying because when it runs it completely over takes the net usage and other net applications.
---

I've been upgrading my ubuntu laptop since ubuntu 6.06, even though sometimes I break my installation and need to do a clean install... Never the less I think ubuntu's upgrade tool has no second in the linux world. It is mostly a reliable tool and usually does the job. But there is one thing that always annoyed me about it. Once you get it running you can't stop it, and if you stop it cleans all the packages downloaded. It's really annoying because when it runs it completely over takes the net usage and other net applications.

On my relatively slow internet connection it is not possible for example to make a VOIP conversion while this tool is running. So here comes the great power of  unix shell to save the day:

First lets open a terminal and run 'top' or 'htop' which can help us find what is running under gksu user:

[![](http://www.tabula0rasa.org/wp-content/uploads/2008/07/htop.png)](http://www.tabula0rasa.org/wp-content/uploads/2008/07/htop.png)

you can see that the name of the process is 'gksu /tmp/tmp0U_pP/hardy'. Using F5 in htop will expand the tree of the processes and we'll find that the process is really a python script, which got a 'pid number' in my case it is 5974.

Now in order to pause the process we can type:

    
    ozubu@karo:~$ sudo kill -STOP 5947


this will halt the process without killing it or causing the loss of data. In order to continue the process,

    
    ozubu@karo:~$ sudo kill -CONT 5947


and this will enable us to recieve a VOIP call during the upgrade process...
