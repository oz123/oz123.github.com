---
title: Tiny Python script to convert Fortran comments to "!"
author: Oz Nahum
published: 2010-05-29
tags: Programming, Python, Fortran
public: yes
chronological : yes
kind: writing 
summary: I work on a very old Fortran code, which is Fixed form Fortran 77 mixed with some Fortran 95. Geany IDE, had problem displaying lines starting with "c" as comments.
---

I work on a very old Fortran code, which is Fixed form Fortran 77 mixed with some Fortran 95. Geany IDE, had problem displaying lines starting with "c" as comments.
Eclipse didn't. But ECLIPSE is over overwhelm with features I don't need, so I prefer workin with Geany. Since I couldn't wait until Geany will have that feature I wan't, I just converted all the comments from "c" to "!".
Since it's a fixed form Fortran, it can't be that a variable name will start with "c", and words like "call" are never in the first column.

Here is the little script to do the conversion:

    
    #!/usr/bin/python
    # Script to convert old fortran comments with "c" to "!"
    # Friday, May 28 2010, Oz Nahum,
    # disributed under the terms of the GPLv3 or later
    #
    # Usage: run the script in the directory of the files
    # All files will be output to a directory called ''output'
    # Be sure to create it.
    
    import os
    FilesList=os.listdir(".")
    
    for fileName in FilesList:
        if fileName[-1] == 'f':
            f=open(fileName,'r')
            newf=open("output/"+fileName,"w")
            #print help(newf)
            print fileName
            lines=f.readlines()
            for line in lines:
                print line
                newf=open("output/"+fileName,"a")
                #l=f.next()
                l=list(line)
                #print l
                if l[0]=="c":
                    l[0]="!"
                l="".join(l)
                print l
                newf.write(l)
                newf.close()
