---
title: A Complete PyGTK CD Ripper Tutorial
author: Oz Nahum
published: 2013-01-03
tags: Python, Programming, PyGTK
public: yes
chronological : yes
kind: writing 
summary: Most tutorials on GTK, create partial UIs, and thus leave the reader to connect the rest by himself. Some others create an almost complete application, but usually, this application is useless. This tutorial, will lead (eventually, I hope...) to a functional application, that rips CD and converts them to MP3 using cdparanoia and lame. In addition to writing this tutorial in blog posts with code, the code will be highly verbose and commented thoroughly ...
---

Most tutorials on GTK, create partial UIs, and thus leave the reader to connect the rest by himself. 
Some others create an almost complete application, but usually, this application is useless. 
This tutorial, will lead (eventually, I hope...) to a functional application, 
that rips CD and converts them to MP3 using cdparanoia and lame. 
In addition to writing this tutorial in blog posts with code, the code will 
be highly verbose and commented thoroughly.

First, a statement of destination: My goal is to produces a functional PyGTK clone of 
[asunder](http://littlesvr.ca/asunder/), a full blown GTK CD Ripper and converter. 
The goal is not to rewrite the software in Python, rather to Develop a full tutorial, 
and document the steps leading to a complete application, with the right and wrong decisions, 
exposed and open for discussion. 

For the beginning, here is what out first GTK Window should look like:

![asunder main window1][main_window]





    #!/usr/bin/env python
    
    """
    punder.py - part one:
    
    creating a very very basic UI. A tool bar with Four buttons.
    2 of the buttones contain icons and text, and two buttons contain
    just icons.
    """
    
    import gtk
    
    class PunderUI():
        """
    Initial class to draw the first toolbar.
    """
        def __init__(self):
            """
    create the gui using GTK Window, and Toolbar.
    """
            window = gtk.Window()
            window.set_default_size(500, -1)
            
            toolbar = gtk.Toolbar()
            # bad naming convention
            button1 = gtk.ToolButton()
            button1 = gtk.ToolButton(gtk.STOCK_REFRESH)
                 
            button1.set_label("CDDB")
            button1.set_is_important(True)
            
            button2 = gtk.ToolButton(gtk.STOCK_PREFERENCES)
            button2.set_is_important(True)
            
            separator1 = gtk.SeparatorToolItem()
            
            # more verbose ... hard to type, but nothing that
            # a decent IDE can not cope with.
            # give your items clear name, which indicate
            # their roles
            button_about = gtk.ToolButton(gtk.STOCK_ABOUT)
            
            # if you set a button to not important, it's text label
            # will not be shown!
            # unlike button2.set_is_important(True)
            button_about.set_is_important(False)
            
            window.connect("destroy", lambda w: gtk.main_quit())
            window.add(toolbar)
            toolbar.insert(button1, 0)
            toolbar.insert(button2, 1)
            toolbar.insert(separator1, 2)
            toolbar.insert(button_about, 3)
            # launch the window.
            window.show_all()
    
    PunderUI()
    gtk.main()

If you run this code with `python punder.py` you will see the following
window:

![asunder tool_bar][tool_bar]

### Making a button do something

Now we have a simple toolbar with 3 buttons that don't do anything. 
In order to make a button do something we need to call the Gobject method 
connect. We call this method with a callback function and a signal.  

It makes sense that when pressing the about button an about dialog will
pop up, so here is the right code:

    button_about.connect("clicked", self.help_dialog)
    
Now, we still have not defined the `help_dialog` method, so pressing that
button will result in an error. Here is the right handler function:

    def help_dialog(self, widget):
        """
        create a GTK help dialog upon button click and destroy it when pressing the 
        close button
        """
        self.about = gtk.AboutDialog()
        sometext=gtk.Label('This is just the beggining.\nWill Get back to later.')
        self.about.vbox.pack_start(sometext)      
        self.about.show_all()
        result = self.about.run() 
        # adding this will cause the about dialog to close when we
        # press the button 'Close'.
        self.about.hide()

All together our `PunderUI` class looks like that:

    class PunderUI():
        """
        Initial class to draw the first toolbar.
        """
        def help_dialog(self, widget):
            """
            create a GTK help dialog upon button click and destroy it when pressing the 
            close button
            """
            self.about = gtk.AboutDialog()
            sometext=gtk.Label('This is just the beggining.\nWill Get back to later.')
            self.about.vbox.pack_start(sometext)      
            self.about.show_all()
            result = self.about.run() 
            # adding this will cause the about dialog to close when we
            # press the button 'Close'.
            self.about.hide()
        
        def __init__(self):
            """
            create the gui using GTK Window, and Toolbar.
            """
            window = gtk.Window()
            window.set_default_size(500, -1)
            
            toolbar = gtk.Toolbar()
            # bad naming convention
            button1 = gtk.ToolButton()
            button1 = gtk.ToolButton(gtk.STOCK_REFRESH)
            
            button1.set_label("CDDB")
            button1.set_is_important(True)
            
            button2 = gtk.ToolButton(gtk.STOCK_PREFERENCES)
            button2.set_is_important(True)
            
            separator1 = gtk.SeparatorToolItem()
            
            # more verbose ... hard to type, but nothing that 
            # a decent IDE can not cope with. 
            # give your items clear name, which indicate
            # their roles
            #button_help = gtk.ToolButton(gtk.STOCK_HELP)
            #button_help.set_is_important(True)
            button_about = gtk.ToolButton(gtk.STOCK_ABOUT)
            
            # if you set a button to not important, it's text label
            # will not be shown!
            # unlike button2.set_is_important(True)
            button_about.set_is_important(False)
            
            # with .connect we make a button do something
            # in this case, the event clicked will trigger
            # the class method rundialog
            # gtk.Button is inherited from the class gobject
            # hence it contains also the method connect, which
            # takes by default 2 arguments:
            # def connect(detailed_signal, handler, ...)
            # see more info the [method documentation][doc1]
            button_about.connect("clicked", self.help_dialog)
            
            window.connect("destroy", lambda w: gtk.main_quit())       
            window.add(toolbar)
            toolbar.insert(button1, 0)
            toolbar.insert(button2, 1)
            toolbar.insert(separator1, 2)
            toolbar.insert(button_about, 3)
            window.show_all()

And pressing the `About` button will show the following dialog:

![punder_about][About_dialog]

### Packing more widgets

Until now the window created is pretty poor. By using packing it is 
possible to add more elements to user interface. Packing is done, 
this by defining a container box:
    
    vbox = gtk.VBox()

And adding it to the Window:

    window.add(vbox)    

Now a child widget can be added to `vbox`, for example, the toolbar
created earlier, can be drawn inside `vbox`, instead directly in the 
window.
    
    #window.add(toolbar)
    vbox.pack_start(toolbar, False)

To test how a user interface looks like, it is possible to define 
simple place holders and also pack them into `vbox`:

    # add some more stuff to vbox
    album_info = gtk.Label('A place holder for Album info')
    vbox.pack_start(album_info)
        
    track_list = gtk.Label('A place holder for track_list')
    vbox.pack_start(track_list)

The full PunderUI class will result in the following window:

![A Window with more the just a toolbar][pack_demo]

The full code, for this part of the tutorial can be found
in the [github repository under the tag end_part_1][github]. The next
part, will demonstrate how to create a `gtk.TreeView()` to populate
the list of songs. Naturally, it will need to demonstrate how to populate
the text in the boxes, retrieved from a process that reads the CD-ROM.
Stay tuned!

[github]: https://github.com/oz123/punder/blob/end_part_1/punder.py
[pack_demo]: https://lh6.googleusercontent.com/-lEICR2zzbLE/UOWYIaWv92I/AAAAAAAACCk/k0PgOYD6aJs/s506/Screenshot-punder.py-packing_demo.png "Advancing toward the full Window"
[doc1]: http://www.pygtk.org/docs/pygobject/class-gobject.html#method-gobject--connect 
[About_dialog]: https://lh6.googleusercontent.com/-4KumGibmvWU/UOV2ILkUjxI/AAAAAAAACCE/l9VRfLRv0rw/s214/Screenshot-About%2520punder.py.png "A Raw About Dialog"
[tool_bar]: https://lh4.googleusercontent.com/-D_XgKwFkY-o/UOVUpPseR9I/AAAAAAAACBo/QEAuSoye_gw/s506/Screenshot-punder.py.png "A hubmle start"
[main_window]: https://lh3.googleusercontent.com/-_4S1FVNGUZ0/UOVMeWTcoUI/AAAAAAAACA0/mebapvcgPlI/s606/Screenshot-Asunder.png "Where we want to be"
