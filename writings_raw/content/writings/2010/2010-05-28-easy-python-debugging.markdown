---
title: Easy Python debugging
author: Oz Nahum
published: 2010-05-28
tags: Programming, Python
public: yes
chronological : yes
kind: writing 
summary: Just a quicky post ... Python has the excellent pdb module to debug your programs. 
---

Just a quicky post ... Python has the excellent pdb module to debug your programs. 
But frankly, for many needs, I feel it's just an over kill, 
and some times it's easier to use the following, old known method:
Printing out variables, and checking their contents ...

If you have the following structure, which has to run about 500 times, your screen will be packed with variables and sometimes it might be a bit harder to understand:


    
    
      while a[:-2] != '':
            if a[:-2] == '<th>Date of sampling</th><th>Value</th>':
                #print "hola"
                #raw_input("\n\nPress the enter key to exit.")
                a=f.next()
            #for lines in f:
                #while a !=
                while a[:-2] != '':
                    a=clean(a)
                    if TableCounter%2 == 0:
                        t=list(a)
                        if t[0] != '\r':
                          Dates.append(a[:-2])
                          TableCounter=TableCounter+1
                          a=f.next()
                    if TableCounter%2 == 1:
                        a=clean(a)
                        t=list(a)
                        if t[0] != '\r':
                          Values.append(a[:-2])
                          TableCounter=TableCounter+1
                          a=f.next()
                    #print a
                    a=f.next()
            a=f.next()
        return Dates, Values
    



So, here is what I do: I put manual pauses after the print statements, here is how It's done:


    
    
      while a[:-2] != '':
            if a[:-2] == '<th>Date of sampling</th><th>Value</th>':
                print "hola"
                raw_input("\n\nPress any key to continue...")
                a=f.next()
                while a[:-2] != '':
                    a=clean(a)
                    if TableCounter%2 == 0:
                        t=list(a)
                        print t
                        raw_input("\n\nPress any key to continue...")
                        if t[0] != '\r':
                          Dates.append(a[:-2])
                          TableCounter=TableCounter+1
                          a=f.next()
                    if TableCounter%2 == 1:
                        a=clean(a)
                        t=list(a)
                        if t[0] != '\r':
                          Values.append(a[:-2])
                          TableCounter=TableCounter+1
                          a=f.next()
                    #print a
                    a=f.next()
            a=f.next()
        return Dates, Values
    



That's all, and if that's not enough, there is the official [Python debugger](http://docs.python.org/library/pdb.html).
