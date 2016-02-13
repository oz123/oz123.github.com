---
title: PyGTK CD Ripper Tutorial - Part 7
author: Oz Nahum
published: 2013-06-02
tags: Python, Programming, PyGTK
public: yes
chronological : yes
kind: writing 
summary: Part 6 of this tutorial completed the Preferences dialog and introduced gtk.Frames and gtk.Expanders. This part of the tutorial will add some more polish to th UI, introducing icons and completing the About Dialog
---


Part 1 of this [pygtk tutorial][tutor1] stopped with a working toolbar and two place 
holders. [Part 2][tutor2] of this tutorial  extended this minimal UI with a list of
songs which was created using GTK ListView. [Part 3][tutor3] showed how to gain better control 
on `ListView`. [Part 4][tutor4] added some final polish to the UI and added an empty Preferences 
Dialog. [Part 5][tutor5] of this tutorial added a `gtk.Notebook` to the Preferences dialog, and 
showed how to populate the first to Notebook pages (tabs) with the appropriate widget.  [Part 6][tutor6]
of the tutorial showed how to the gtk.Notebook, by populating the "Encode" and "Advanced"
pages, thus completing the Preferences dialog. This part of the tutorial will add more polish to the 
UI. Here is how the UI looked when running the code after completing Part 6:

![The UI of Part 6][uipart6]

Here is what is missing from the UI:

![The UI of asunder][asunder_highlighted]

The elements missing both contain an image, the rip button and the application logo, which is not 
visible in all GTK themes (the one in the photo is TradionalOK on Mate Desktop and Debian Wheezy).  

The method responsible for loading the PNG image is `window.set_icon_from_file(filename)`. Hence, 
our window instance has already this method included, and it will be just add to the `__init__`
method of the main UI. 
Before new code is introduced, I will take a short side deviation. In the previous parts of this 
tutorial the code consisted of just one class, the `PunderUI` class. However, keeping  this 
structure creates a very big class, which is getting harder and harder to maintain and follow. 
Hence, I am going to separte some functionality from the main Window Class and put it in other classes.
This is not new, if you following the previous part of the tutorial, you have seen this done before
with the `PrefDialog` class. Hence the structure the code will now be the following:

    import gtk
    
    class PrefDialog(object):
        ....
    class AboutUI(object):
        ....
    class PunderUI(object):
        ....


Back to adding the main Window icon, I add only one line:

    def __init__(self):
        """
        create the gui using GTK Window, and Toolbar.
        """
        self.window = gtk.Window()
        self.window.set_default_size(500, -1)

        # Set VBox to heterogeneous so different widgets can have 
        # different sizes 
        # All widgets attached will be the same size
        # Setting homogeneous to false makes the UI look sane
        # only in a few cases we create VBOX with the homogenous option
        vbox = gtk.VBox(False)
        self.window.add(vbox)
        
        ...
        ...

        # adding this line will add a window icon which will be propagated
        # to all dialogs of the main program, 
        # try running the program and you will see this icon also added 
        # to the window of the Preferences dialog. 
        self.window.set_icon_from_file("asunder.png")
        
        # add the elements needed to show the Rip Button:
        self.make_rip_button(vbox)

        self.window.show_all()

The next item, is the Rip button, to create this button I added a self baked
method to the init just below the calling of the built-in method `set_icon_from_file`.
This method has all the usual elements that were show before and one extra new method.
The is the `gtk.image_new_from_stock` method. [GTK includes many more icons you can use
when needed][gtkimages]:


        def make_rip_button(self, vbox):
            """
            add rip button, and icon to that button. 
            """
            # gtk.image_new_from_stock(stock_icon_name, size_in_pixels)
            cdrom = gtk.image_new_from_stock(gtk.STOCK_CDROM, gtk.ICON_SIZE_BUTTON)
            rip = gtk.Button()
            label = gtk.Label("Rip")
            fillerBox = gtk.HBox(False)
            button_hbox = gtk.HBox(False)
            button_hbox.pack_end(label, False, False)
            button_hbox.pack_end(cdrom, False, False, 5)
            rip.add(button_hbox)
            fillerBox.pack_end(rip, False, False, 0)
            vbox.pack_start(fillerBox, False, False, 0)
        

The method above is using all the usual tricks shown before. 3 GTK widgets are created (`cdrom`,
`rip` and `label`). To these widgets 2 Boxes were added (`filler_Box` and `button_hbox`). The 
boxes define the visual relationships between the widgets using packing as done many times before. 
Finally, these elements are added to the main UI by packing them into `vbox` which belongs to the 
main window. The main window and the Preferences dialog are now completed. However the about dialog 
is still not complete. The code for this dialog was included in the main UI class as a method and
gave some sparse information about the program:

    def help_dialog(self, widget):
        """
        create a GTK help dialog upon button click and destroy it when pressing the
        close button
        """
        self.about = gtk.AboutDialog()
        sometext=gtk.Label('This is just the beggining.\nWill Get back to it  later.')
        self.about.vbox.pack_start(sometext)
        self.about.show_all()
        result = self.about.run()
        # adding this will cause the about dialog to close when we
        # press the button 'Close'.
        self.about.hide()


However, a help dialog can contain much more info, and GTK includes many built in methods to supply 
the user with this info. Here is how to present this info, packed into a class:

        class AboutUI(object):
        """
        Show the about dialog
        """
        def __init__(self, widget):
            """
            create a GTK help dialog upon button click and destroy it when pressing the
            close button
            """
            self.about = gtk.AboutDialog()
            sometext=gtk.Label('This is just the beggining.\nWill Get back to it  later.')
            #self.about.vbox.pack_start(sometext)
            self.about.set_program_name("Punder")
            self.about.set_comments("An application to save tracks from an Audio CD \n"+\
            "as WAV, MP3, OGG, FLAC, Wavpack, Musepack, Monkey's Audio, and/or "+\
            "AAC files.")
            self.about.set_license("This program is distributed under the terms of GPLv3+.")
            self.about.set_copyright("Copyright 2013 Oz Nahum")
            self.about.set_website("https://github.com/oz123/punder")
            authors = ["Oz Nahum"]
            self.about.set_authors(authors)
            self.about.set_translator_credits("German - Franz Schubert\nFrench - Leon Blum")
            self.about.set_artists(["The CD icon of Punder is originally from Asunder.\nhttp://littlesvr.ca/asunder/"])
            self.about.show_all()
            self.about.set_icon_from_file("asunder.png")
            self.about.run()
            # adding this will cause the about dialog to close when we
            # press the button 'Close'.
            self.about.hide()

This class contains much more info, comparing to the previous method. The main PunderUI needs to know
how to use this class. Previously, the `About` button was connected to a method:

            button_about.connect("clicked", self.help_dialog)

However, the `help_dialop` does not exist anymore, and instead the button is connected to calling an
instance of the AboutUI class in the following way:
            
            button_about.connect("clicked", AboutUI)
        

With this last addition, the UI is complete (as usual, [the full code is here][UI_Complete]):

![Punder Complete][uicomplete]           

Further work on this application will be to get it working. Hence this will be infrastructure code, 
no Screenshots to share. If you like this tutorial, you can keep following the changes by staring 
it on github, or visiting this blog again. 


[tutor1]: http://oz123.github.com/writings/2013-01-03-A%20Complete%20PyGTK%20CD%20Ripper%20Tutorial/
[tutor2]: http://oz123.github.com/writings/2013-01-04-PyGTK%20CD%20Ripper%20Tutorial%20Continued/
[tutor3]: http://oz123.github.com/writings/2013-01-09-PyGTK%20CD%20Ripper%20Tutorial%20Part%203/
[tutor4]: http://oz123.github.com/writings/2013-01-21-PyGTK%20CD%20Ripper%20Tutorial%20Part%204/
[tutor5]: http://oz123.github.com/writings/2013-02-11-PyGTK%20CD%20Ripper%20Tutorial%20Part%205/
[tutor6]: http://oz123.github.io/writings/2013-02-27-PyGTK%20CD%20Ripper%20Tutorial%20Part%206/
[uipart6]: https://lh3.googleusercontent.com/-NBzN56B7o5c/UamNiz1yDXI/AAAAAAAACP0/7Jjt3Uy4IpE/s508/EndOfPart6.png
[asunder_highlighted]: https://lh3.googleusercontent.com/-J2rSBaebmqQ/UamMIHeJMkI/AAAAAAAACP0/1-y10KU5VFY/s606/Screenshot-Asunder-Highlighted.png
[gtkimages]: http://www.learngtk.org/pygtk-tutorial/stockimages.html
[uicomplete]: https://lh6.googleusercontent.com/-0cb-ircw1SQ/UasDBoEYpfI/AAAAAAAACQQ/LvO7A77Io90/s736/UI-Complete.png
[UI_Complete]: https://github.com/oz123/punder/tree/UI_Complete
