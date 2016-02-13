---
title: Extending Python's Popen 
author: Oz Nahum
published: 2012-12-03
tags: Python, Programming
public: yes
chronological : yes
kind: writing 
summary: I use Python's Popen quite often, and sometimes, I need to debug scripts using it. Here is how I extended Popen, to include a verbose debug mode ...
---

As a System's Engineer I use Python's subprocess module quite extensively. 
Quite often I call to Popen using complex and long command with switches 
which are determined based on different conditions where the scripts is 
supposed to run. Hence, my Python codes will often have a similar lines to:

    import subprocess as sp
    ...
    ...
    lookupcmd = 'lookup -C class -v variable -h %s' % host
    lookup = sp.Popen(lookupcmd, shell=True, stdin=sp.PIPE, stdout=sp.PIPE)
    ans = lookup.communicate()

This was often debugged using calls to:

    print lookupcmd

or even using `import pdb; pdb.set_trace()` just before `subrocess.Popen(...)`.
After doing this a few times for a few different tasks, I decided that enough is enough
and I am going to extend Popen to include a new keyword. 

# Using Inheritence 
My first approach was  to use that fact the `Popen` is a Class which could be 
inherited and extented:

    import subprocess as sp

    class nPopen(sp.Popen):
        """
        override the default Popen in subprocess, to allow
        test modus.
        usage:
        p = nPopen("ls -l", shell=True, stdout=sp.PIPE,testmode=True)
        will print "ls -l" and will not execute anything.
        This will behave as subprocess.Popen
        p = nPopen("ls -l", shell=True, stdout=sp.PIPE,testmode=False)
        print p.communicate()
        """
        def __init__(self, args, bufsize=0, executable=None,
                     stdin=None, stdout=None, stderr=None,
                     preexec_fn=None, close_fds=False, shell=False,
                     cwd=None, env=None, universal_newlines=False,
                     startupinfo=None, creationflags=0,testmode=False):

            if testmode: 
                print args
                return None

         p = sp.Popen.__init__(self,args, bufsize, executable,
                     stdin, stdout, stderr,
                     preexec_fn, close_fds, shell,
                     cwd, env, universal_newlines,
                     startupinfo, creationflags)

            return p


Using this `nPopen` is done exactly like subprocess`s own Popen:

    lsp=nPopen('ls -l', shell=True, stdout=sp.PIPE, testmode=True)

Because of `testmode=True` this assignment will just print `ls -l`
to the standard output, and when testmode is set to `True` a normal
Popen object will be created and we can use it as if we called 

   subprocess.Popen('ls -l', shell=True, stdout=sp.PIPE)

# Using a wrapper function
A second approach was suggested by kind Stackoverflow member in response
to my [feedback reuest](http://stackoverflow.com/q/13383322/492620).

    def nPopen(*args, **kw):
        """
        override the default Popen in subprocess, to allow
        test modus.
        usage:
        p = Popen("ls -l", shell=True, stdout=sp.PIPE,testmode=True)
        will print "ls -l" and will not execute anything.
        This will behave as subprocess.Popen
        p = Popen("ls -l", shell=True, stdout=sp.PIPE,testmode=False)
        p.communicate()
        """
        dummy = False
        if 'testmode' in kw.keys():
            dummy = kw['testmode']
            del kw['testmode']
        if dummy:
            print ''.join([repr(arg) for arg in args])
            return None
        else:
            proc = sp.Popen(*args, **kw)
            return proc

The first approach is more sofisticated and uses the Object Oriented nature
of Python. It also requires a bit more typing, and _might_ be harder to understand
if someone is not familiar with concepts like inheritence. The second approach
is quite simple, and provides the same interface using a bit more simple approach. 
Both approaches can be reused using `from my_module import nPopen`. 

 
I installed Ubuntu 12.04 on two laptops by now. and I must rant. Ubuntu
developers are assuming two many things about me. First, there is this
bug, which the['migration-assitant' mounts existing partitions in
READ-WRITE
mode](https://bugs.launchpad.net/ubuntu/+source/ubiquity/+bug/994510). I
find it dangerous and not necessary for migration.\
