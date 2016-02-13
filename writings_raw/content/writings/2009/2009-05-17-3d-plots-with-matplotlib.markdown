---
title: 3D plots with matplotlib
author: Oz Nahum
published: 2009-05-17
tags: Programming, Python
public: yes
chronological : yes
kind: writing 
summary: Today I built matplotlib from svn. The answer why I did it is in the post's title. 3D plots are back to this wonderful tool !
---

Today I built matplotlib from svn. The answer why I did it is in the post's title. 3D plots are back to this wonderful tool !

So, if you build matplotlib version 0.98.6svn or later, you can enjoy this. It's sometimes a little bit cranky. With plots of multiple points I got one big black surface, but for simple stuff it works great.

Here is an example of 3D plot of hydraulic head on a coordinate system:

    
    import pylab as pl
    from numpy import *
    import mpl_toolkits.mplot3d.axes3d as axes3d
    
           #  x      y     head
    head = ((25, 225 , 240.1178), #h1
            (75,  225,  242.3238),#h2
            (125,   225, 244.8013),#h3
            (175,   225,    247.2736),
            (225,   225,    248.8057),#h5
            (25, 175 ,  241.7646), #h6
            (75,  175,  242.0468),#h7
            (175,   175, 248.2085),  #h8
            (225,   175,    249.1382),#h9
            (25,   125,    243.1239), #h10
            (225, 125 , 249.5332), #h11
            (25,  75,  244.4780),#h12
            (75,   75, 245.1523),  #h13
            (175,   75,    248.9717),#h14
            (225,   75,    249.4562),#h15
            (25, 25 ,  245.1523), #h16
            (75,  25,  245.8214),#h17
            (125,   25, 247.1543),  #h18
            (175,   25,    248.4819),#h19
            (225,   25,    249.3144)) #h20
    
    x, y, z = zip(*head)
    xi, yi = pl.arange(0, 250, 5), pl.arange(0, 250, 5) #create grid
    head = pl.griddata(x, y, z, xi, yi) #interpolate the scattered data !
    print shape(head)
    print shape(xi)
    print shape(yi)
    f = pl.figure(1)
    pl.scatter(x, y)
    pl.contour(xi, yi, head)
    pl.colorbar() # draw colorbar
    #pl.show()
    
    f = pl.figure(2)
    ax = axes3d.Axes3D(f)
    #X,Y,Z = axes3d.get_test_data(0.05)
    cset = ax.contourf3D(xi,yi,head)
    ax.clabel(cset, fontsize=9, inline=1)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Hydraulic Head')
    
    f = pl.figure(3)
    ax = axes3d.Axes3D(f)
    #X,Y,Z = axes3d.get_test_data(0.05)
    cset = ax.contour3D(xi,yi,head)
    ax.clabel(cset, fontsize=9, inline=1)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Hydraulic Head')
    
    pl.show()




and the output is:
[![head 3D](http://www.tabula0rasa.org/wp-content/uploads/2009/05/head2.png)](http://www.tabula0rasa.org/wp-content/uploads/2009/05/head2.png)




[caption id="attachment_231" align="aligncenter" width="300" caption="Old Style ..."][


[![](http://tabula0rasa.org/wp-content/uploads/2009/05/head-300x219.png)](http://tabula0rasa.org/wp-content/uploads/2009/05/head.png)[/caption]

](http://www.tabula0rasa.org/wp-content/uploads/2009/05/head3d.png)
    Another 3D plot



[caption id="attachment_232" align="aligncenter" width="480" caption="Another 3D plot"][![old fashioned...](http://www.tabula0rasa.org/wp-content/uploads/2009/05/head3.png)](http://www.tabula0rasa.org/wp-content/uploads/2009/05/head3.png)[/caption]

As usual, have fun with python !
