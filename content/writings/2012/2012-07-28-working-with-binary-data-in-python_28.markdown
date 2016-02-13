---
title: Working With Binary Data in Python
author: Oz Nahum
published: 2012-07-28
tags: Programming, Python
public: yes
chronological: yes
kind: writing 
summary: Working with binary data puzzled me for quite a time, so here is a post explaining some of my findings
---

Working with binary data puzzled me for quite a time, so here is a post explaining some of
my findings. 
First we define a bytes array:


    s = bytearray(b"Hello World") 
    for i in s:
          print i 
    ... 72 101 108 108 111 32 87 111 114 108 100


now, let's write this data to a file:
   
    f = open('helloword.bin','wb')
    for i in s:
       f.write(struct.pack("I",i)) f.close()

Let's inspect the file created:
  
    $ du -h points.bin 
    4.0K    points.bin 
    $file points.bin 
    points.bin: data 
    $ less points.bin 
    "points.bin" may be a binary file.  See it anyway?


Binary file sizes
-----------------

let's us write "hello world" into a text file in a text form:

    f = open('helloword.txt") 
    f.write("hello world") 
    f.close()


Once again we can inspect the file:

    $ du -h   helloworld.txt 
    4.0K    helloworld.txt

Now, what happens if we make a longer binary array?\

    s.split() 
    s.append(33) 
    bytearray(b'Hello World!') 
    for i in range(10000): 
    s.append(33) 
    f = open('longhelloword.bin', 'wb') 
    import struct
    
    for i in s: 
    f.write(struct.pack("I",i)) 
    f.close() 
    f = open('longhelloword.txt', 'w') 
    hello = "Hello World!" 
    for i in range(10000): 
        hello = hello+"!"


In a shell, examaining the file sizes:
  
    $ du -h longhelloword.bin 
    40K     longhelloword.bin 
    $ du -h longhelloword.txt 
    12K     longhelloword.txt

Wait a minute ! Why is the binary file almost 4 times bigger?

The answer is: it depends on the format specifier in `struct.pack`. 
Namely, we used an `unsigned int`, for each character we then reserved 4
bytes!. 
When we saved the text, every character was assigned to the file exactly
as a `char` which takes one byte only. 

If we repeat the above with `struct.pack("b",i)` the sizes of the file
won't differ: 


    f = open('longhellowordwithchar.bin', 'w') 
    for i in s: 
    f.write(struct.pack('b',i)) 
    f.close()

and in the shell:

    $ du  longhellowordwithchar.bin 
    12      longhellowordwithchar.bin 
    $ du  longhelloword.txt        
    12      longhelloword.txt


Credits: 
http://dabeaz.blogspot.de/2010/01/few-useful-bytearray-tricks.html 
http://docs.python.org/library/struct.html\#module-struct

