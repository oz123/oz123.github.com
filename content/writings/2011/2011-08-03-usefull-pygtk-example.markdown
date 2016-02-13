---
title: A Usefull PyGTK Example
author: Oz Nahum
published: 2011-08-03
tags: Python, GTK, Programming
public: yes
chronological: yes
kind: writing 
summary: I have been looking for a good pygtk tutorial for a very long time. I have found a few tutorials which where an overkill, so I don't link to them.
---

I have been looking for a good pygtk tutorial for a very long time. I
have found a few tutorials which where an overkill, so I don't link to
them. By over kill I mean that they where full with details which
prevented me from actually having an application working.
I found this [nice pygtk tutorial](http://zetcode.com/tutorials/pygtktutorial/), which is
actually more a capabilities demonstration. After reading for a few
hours, I got intrigued. But I was very frustrated since the tutorial
does not produce any real life example. For example, I would have expand
the calculator example to working one. I did a Google search and bumped
into this [pygtk calculator](http://code.google.com/p/calculator-using-pygtk/) working
example. After a couple of more hours, I have managed to produce the
following "Hello World!" pygtk application which demonstrates some basic
pygtk principles:

    #!/usr/bin/python
    
    # A Usefull and Active PyGTK Example
    #
    # This example demonstrates a few Widgets which actually do 
    # some stuff, and interact with each other.
    #
    # oz nahum
    # linuxpixies.blogspot.com 
    # August 2011
    
    import gtk
    
    class PyApp(gtk.Window):
    
        def __init__(self):
            super(PyApp, self).__init__()
            
            self.set_title("Entry")
            self.set_size_request(250, 200)
            self.set_position(gtk.WIN_POS_CENTER)
    
            self.fixed = gtk.Fixed()
    
            self.label = gtk.Label("Please Enter Your Name below")
            self.fixed.put(self.label, 60, 40)
            
            self.entry = gtk.Entry()
            self.entry.add_events(gtk.gdk.KEY_RELEASE_MASK)
            self.fixed.put(self.entry, 60, 100)
            
            self.entry.set_text("bla")
            self.UserName=self.entry.get_text()  
    
            self.outlabel=gtk.Label('name')
            self.fixed.put(self.outlabel, 60,180)
            
            self.button = gtk.Button("Greeting:")
            self.fixed.put(self.button, 60,140)
            self.button.connect("clicked",self.greeting)
            
            self.clearbutton = gtk.Button("Clear")
            self.fixed.put(self.clearbutton, 140,140)
            self.clearbutton.connect("clicked",self.cleartxt)
           
            self.button = gtk.Button("Close")
            self.button.connect("clicked",gtk.main_quit)
            self.fixed.put(self.button, 200,140)
    
            self.connect("destroy", gtk.main_quit)
            self.add(self.fixed)
            self.show_all()
            
        def greeting(self, event):
            self.outlabel.set_text("Hello "+self.UserName)
            self.entry.set_text('Hello '+self.UserName)
            
        def cleartxt(self, event):
            self.entry.set_text("")
    
    PyApp()
    gtk.main()


