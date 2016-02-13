---
title: The weired Indexing in Perl
author: Oz Nahum
published: 2012-03-16
tags: Programming, Perl
public: yes
chronological: yes
kind: writing 
summary: I am learning Perl. I am doing it with a lot of a resentment, but I am  slowly learning it.
---

I am learning Perl. I am doing it with a lot of a resentment, but I am
slowly learning it. 
Normal people count from 1. Computer Scientist count from 0. Perl
developers count from -1?

WTF?

    oz@server ~ $ test.pl test
    num of args 0 
    oz@server ~ $ test.pl test test
    num of args 1 
    0
    test
    1
    test
    oz@server ~ $ test.pl          
    num of args -1 
    No arguments!
    oz@server ~ $ 

My Code, just in case I am totally wrong about this here, :

    $ cat test.pl 
    #!/usr/local/bin/perl -w
    
    
    print "num of args $#ARGV \n";
    if ( $#ARGV > 0   ){
    
       for ( my $i = 0 ; $i <= $#ARGV  ; ++$i  ) {
    
       print "$i\n";
       print "$ARGV[$i]\n";
       }
    }
    if ( @ARGV > 0 )
    {
      print "Number of arguments: " . scalar @ARGV . "\n";
    }
    else
    {
    print "No arguments!\n";
    }

Comments
--------

linuxpixie

Hi Amir, \
Is there is significant difference between print and say ?

Amir

Well no, counting from 0 is a common standard to which Perl adheres. It
doesn't count from -1.\
\
my @array = (0, 1, 2, 3);\
print scalar @array; \# 4\
print \$\#array; \# 3\
print \$array[0]; \# 0\
\
\
Now get this:\
print \$array[-1]; \# 3\
print \$array[-2]; \# 2\
\
BTW, if you use at least Perl 5.10, put\
use 5.010;\
in the beginning, and use "say" instead of "print".

linuxpixie

Thanks Amir, I know it's a silly rant :-)\
But it's already weired for a lot of people to start counting from Zero
(Fortran and Matlab start from 1). Now, I need to get used to counting
from -1.

Amir

\$\#ARGV is not the number of args. It's the last index of array @ARGV.
I agree that the \$\# thing is weird, but you hardly ever need to use
it.\
\
scalar @ARGV is indeed the number of args.\
\
You also hardly ever have to use the C-style "for( initialization;
condition; increment)" loop. It's nicer to do:\
\
my \$idx = 0;\
foreach my \$arg (@ARGV) {\
 print \$idx++ . ": \$arg\\n";\
}\
\
Read these pages some time:\
\* http://perldoc.perl.org/perlsyn.html\
\* http://perldoc.perl.org/perldata.html
