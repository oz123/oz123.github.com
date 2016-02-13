---
title: Localizing applications with gettext 
author: Oz Nahum
published: 2013-08-04
tags: Python, Programming
public: yes
chronological : yes
kind: writing 
summary: I was always interested in how I can add translations to pwman3 or to my little PyGTK tutorial, these are summerizing of my gettext experiences 
---

Gettext is the ubiquitous way to localize FOSS applications. There is a built-in [Python module for gettext][1], so 
it should not be so hard to tranlate Python applications. Unfortunately, the documentation is not covering all 
the steps needed to be done in order to have an application talking more that one language. Hence, this collection
of notes to help getting started. 

Here is a simple applications which prints a simple "hello world" to the terminal. It is already using
gettext:

    ozdeb@yenitiny:~/Desktop/gettext_tutor $ cat hello_gettext.py    
    # -*- coding: utf-8 -*-

    import gettext
    import os

    APPNAME = "hello_gettext"
    TRANSLATION_ROOT = os.path.join(os.getcwd(), "po/locales")

    try:
        l = os.environ['LC_MESSAGES']
        t = gettext.translation(APPNAME, TRANSLATION_ROOT,
                                [l])
    except KeyError:
        t = gettext.translation(APPNAME,
                                TRANSLATION_ROOT)

    _ = t.ugettext

    print _("Hello World")

The first thing to notice is that the `print` statement does not directly print "hello world", 
rather the string is marked for translation with an underscore and it is bracketed. 

Gettext reads strings from a compiled catalog of translation which is found in the `TRANSLATION_ROOT`.
Inside the translations root there is a directory for each locale and a subdirectory called `LC_MESSAGES`.
The initial structure is easily created with:

     ozdeb@yenitiny:~/Desktop/gettext_tutor $ mkdir -pv po/locales/{de_DE,en_US}/LC_MESSAGES/
     mkdir: created directory `po'
     mkdir: created directory `po/locales'
     mkdir: created directory `po/locales/de_DE'
     mkdir: created directory `po/locales/de_DE/LC_MESSAGES/'
     mkdir: created directory `po/locales/en_US'
     mkdir: created directory `po/locales/en_US/LC_MESSAGES/'

The `LC_MESSAGES` will be populated with the `mo` translations. However there are still some steps to be done
first. First a translations template is needed, this translations template is an extraction of 
all the marked strings in the applications. The template is created with the command `xgettext`:

     $ xgettext -k_ -kN_ -o po/locales/hello_gettext.pot hello_gettext.py 
    
The template created still needs to be filled with some missing information. The missing information is shown
with CAPITALIZED text:

    $ cat po/locales/hello_gettext.pot 
    # SOME DESCRIPTIVE TITLE.
    # Copyright (C) YEAR THE PACKAGE'S COPYRIGHT HOLDER
    # This file is distributed under the same license as the PACKAGE package.
    # FIRST AUTHOR <EMAIL@ADDRESS>, YEAR.
    #
    #, fuzzy
    msgid ""
    msgstr ""
    "Project-Id-Version: PACKAGE VERSION\n"
    "Report-Msgid-Bugs-To: \n"
    "POT-Creation-Date: 2013-08-04 05:55+0200\n"
    "PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\n"
    "Last-Translator: FULL NAME <EMAIL@ADDRESS>\n"
    "Language-Team: LANGUAGE <LL@li.org>\n"
    "Language: \n"
    "MIME-Version: 1.0\n"
    "Content-Type: text/plain; charset=CHARSET\n"
    "Content-Transfer-Encoding: 8bit\n"

    #: hello_gettext.py:19
    msgid "Hello World"
    msgstr ""


So just fill in the missing information with `sed` commands or with your favorite text editor 
(Tip: vim supports syntax highlighting for `po` files). After filling the missing information
the content is:

    $ cat po/locales/hello_gettext.pot 
    # Translation catalog for hello_gettext.
    # Copyright (C) 2013 Oz Nahum Tiram
    # This file is distributed under the terms
    # of the GPL v3 or later
    # Oz Nahum Tiram <nahumoz@gmail.com> 2013.
    #
    #, fuzzy
    msgid ""
    msgstr ""
    "Project-Id-Version: hello_gettext 0.1\n"
    "Report-Msgid-Bugs-To: \n"
    "POT-Creation-Date: 2013-08-04 05:55+0200\n"
    "PO-Revision-Date: 2013-08-04 06:05+0200\n"
    "Last-Translator: Oz Nahum <nahumoz@gmail.com>\n"
    "Language-Team: LANGUAGE <LL@li.org>\n"
    "Language: \n"
    "MIME-Version: 1.0\n"
    "Content-Type: text/plain; charset=CHARSET\n"
    "Content-Transfer-Encoding: 8bit\n"

    #: hello_gettext.py:19
    msgid "Hello World"
    msgstr ""

Note that the Language field was left untouched, since this template should be
used for all languages. Localized translations are made from the template using the 
command:

     $ msginit --input=po/locales/hello_gettext.pot --locale=de_DE --output=po/locales/de_DE/LC_MESSAGES/hello_gettext.po
     $ msginit --input=po/locales/hello_gettext.pot --locale=en_US --output=po/locales/en_US/LC_MESSAGES/hello_gettext.po

Then, you can edit the localization file with your editor or a dedicated program for translating like [poedit][2].
When editing the file with a simple text editor you simply write the translation for each string in 
the quotes, e.g:

    #: hello_gettext.py:19
    msgid "Hello World"
    msgstr "Hello Welt"

When all the strings are translated, it is time to compile the translations file:

    $ msgfmt po/locales/de_DE/LC_MESSAGES/hello_gettext.po -o po/locales/de_DE/LC_MESSAGES/hello_gettext.mo

If the command is successful, the following files are found under `LC_MESSAGES`:

    $ ls po/locales/de_DE/LC_MESSAGES/
    hello_gettext.mo  hello_gettext.po

Now the translation should work:

    $ LANGUAGE=de_DE python hello_gettext.py 
    Hallo Welt

Running it without having formatted catalog for `en_US` will result with an error:

    ozdeb@yenitiny:~/Desktop/gettext_tutor $ python hello_gettext.py 
    Traceback (most recent call last):
    File "hello_gettext.py", line 15, in <module>
        TRANSLATION_ROOT)
    File "/usr/lib/python2.7/gettext.py", line 469, in translation
        raise IOError(ENOENT, 'No translation file found for domain', domain)
    IOError: [Errno 2] No translation file found for domain: 'hello_gettext'

A note about setting the language environment: I used the variable `LANGUAGE`, 
however the gettext module looks for the following variables in that order:

    ('LANGUAGE', 'LC_ALL', 'LC_MESSAGES', 'LANG')


Translating with gettext is quite easy, unfortunately, the documentation is not that
straight forward, and I hope this little tutorial will help people who want to get straight
on the job of localizing their python applications.


[1]: http://docs.python.org/2.7/library/gettext.html?highlight=gettext#gettext
[2]: http://poedit.sourceforge.net/
