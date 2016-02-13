---
title: A matplotlib tutorial
author: Oz Nahum
published: 2009-01-05
tags: Python, Programming
public: yes
chronological : yes
kind: writing 
summary: Most people that find my blog in the end of the internet arrive here while looking for python matplotlib tutorial. That's thanks to the crazy matplotlib tutorial I already have in my blog. However, this tutorial is not very useful. And since I'm using matplotlib to do some of my homeworks, I been wanting to post some real life tutorial. After all why not give the audience what it wants?
---

Most people that find my blog in the end of the internet arrive here while looking for python matplotlib tutorial. That's thanks to the crazy matplotlib tutorial I already have in my blog. However, this tutorial is not very useful. And since I'm using matplotlib to do some of my homeworks, I been wanting to post some real life tutorial. After all why not give the audience what it wants?

So here it is - a real life, hydrological problem solved with python matplotlib. First, some background.
Notice, I wrote another [matplotlib tutorial](http://www.tabula0rasa.org/2010/04/another-matplotlib-tutorial/).

In hydro-geology, the science describing water flow in rocks, one would like to know how good is the hydraulic conductivity of a certain rock bearing water, in order to know how easy it would be the extract these water. In order to find the hydraulic conductivity hydrologists conduct pumping tests, in which they extract large amount of water via one pumping well and observe the draw down of water in near by wells. More can be found [here](http://en.wikipedia.org/wiki/Aquifer_test).
In real life the field data the hydrologist gets is a water heights in wells and the distances of these observations wells from the pumping well.

    r [m]    h [m]
    
    15       6.40
    14.95    6.53 
    30.7     6.80
    30.6     6.89
    57.7     7.16
    57.9     7.23

The water level in all wells with out pumping is 8.2 m, and it is easy to see that this data is slightly noisy. This can be in reality due to errors of measurements in the field. In order to get rid of the noise, one can do a linear regression. So in this tutorial we'll do some linear regression and plot the draw down in the wells as a function of the logarithmic distance to the pumping well.  Using the corrected draw down after Jacob, 1963, and the regression of the logarithmic distance vs. corrected draw down  we will find the hydraulic conductivity of the aquifer. Let's just write down the mathematical equations in mathematical language before really coding it in python:
The draw down is:

      s(r)=h_0-h(r)
      h_0,h(r)
      
are the original water level, without pumping and the observed level after pumping, respectively.
The corrected draw down is:

      s'(r)=s_i-\frac{s_i^2}{2h_0}
and the linear regression that is preformed is according to the following formula:

    s'(r)=\frac{Q_w}{2\pi T}\cdot \ln r-\frac{Q_w}{2\pi T}\cdot \ln R


I'm not going to fully explain how this formula is developed because that's not the scope of this post. But it easy to see that this formula is in the form of a linear line which follows the scheme of y=ax+b. So the first term will be given by the slope of the regressions, and the first term will be given by the intercept. Also in the formula are [math]Q_w, T, r, R[/math] which are respectively the pumping rate, transmissivity (related to hydraulic conductivity), distance of observation well, and maximum distance of influence due to pumping.
OK, enough background let's start coding. As with every python mathplotlib program, we start by extending our python capabilities with importing various  modules and functions:

    
    from pylab import plot, title, show , legend, figure, ylim, ylabel, xlabel
    from scipy import *


Now we define the constants and data given for out problems as variables:

    
    Qw = -6.31e-2 #rate of pumping in cubic meter per second, minus sign for extraction well.
    h0=8.2 #Initial height in meters, without pumping
    r=array((15  , 14.95, 30.7,  30.6,  57.7,  57.9))#distance from well in meters
    h=array((6.40, 6.53,  6.80,  6.89,  7.16,  7.23))     #head height in meters


Note that I've defined the table of distances and heights as two numpy arrays. This is because I want the code to run efficiently. When doing algebra or any operation on a vectory (a numpy array) the result is also a vector, which makes things easier, and negates the need to write loops in our code to go over lists, for example.  Let's do some basic calculations of draw down and corrected draw down:

    
    print "draw down is:"
    print r
    s=h0-h #drawdown
    print s
    sc = s-s*s/2/h0 #corrected drawdown
    print sc
    lnr = log(r) #this is  scipy log, which takes a vector and returns a vector
    print lnr
    


The print declarations can be omitted, they are just to see that the result of operation on a vector, is a vector.
Now we do a linear regression on our data:

    
    (ar,br)=polyfit(lnr,sc,1) #ar, slope. br, intercept
    xr=polyval([ar, br], lnr)
    


The function polyfit gets the x-series, y-series, and the order of the polynomial  regression. In this case 1st order means that our polynomial regression is in the form of y=ax+b, like we wanted, and the function returns then two values: ar, br, which are the slope and the intercept.
The function polyval takes a vector of x values and processes them through the equation of the polynomial regression. In return it gives a new vector of y values according to the polynomial regression. These values can be plotted as the trend line later.
Now we use the values of the slope and the intercept of the linear regression to calculate the transmissivity, T, of the aquifer and the Hydraulic conductivity, K, and the maximum distance of well influence.

    
    T = Qw/2/pi/ar #[m^2/sec]
    K = T/h0 #Hydraulic conductivity in m/sec.
    Rmax = exp((br/abs(ar))) #Max distance of well influence
    


Just before we go to the final stage of plotting the data, we add some output lines, which will print the results of our calculations:

    
    print('Linear regression using polyfit')
    print "slope", abs(ar), "intercept", br
    print "Aquifer Transmissivity is: ", round(T, 4) , "m^2/sec"
    print "Aquifer Hydraulic Conductiviy is: ", round(K, 4) , "m^2/sec"
    print "Max distance of well influence is: ", Rmax, "m."


And finally we present our data of corrected draw down vs. distance and  corrected draw down vs. logarithmic distance in graphs:

    
    figure(1)
    title('Well Data Ploted vs. Distance from Well')
    plot(r,h,'b+--')
    ylim(5.5, 7.5)
    ylabel('Water level in well [m]')
    xlabel('Distance to well [m]')
    figure(2)
    title('Corrected drawdown vs. Logarithmic Distance from Well')
    plot(lnr,sc,'b+')
    plot(lnr, xr,'k-')
    ylim(0, 1.7)
    ylabel('Corrected Drawdown [m]')
    xlabel('Log distance to well [m]')
    figure(3)
    title('Corrected drawdown vs. Distance from Well')
    plot(r,sc,'go')
    ylim(0.6, 1.7)
    ylabel('Corrected Drawdown [m]')
    xlabel('Distance to well [m]')
    show()
    


And that's it, run the program and here is the text out put we get and the graphs:

    
    draw down is:
    [ 15.    14.95  30.7   30.6   57.7   57.9 ]
    print draw down
    [ 1.8   1.67  1.4   1.31  1.04  0.97]
    print corrected draw down
    [ 1.60243902  1.49994512  1.2804878   1.20535976  0.97404878  0.91262805]
    log distance:
    [ 2.7080502   2.7047113   3.42426265  3.42100001  4.05525717  4.05871738]
    xr:
    [ 1.55477368  1.55627462  1.23281334  1.23428     0.94916119  0.94760571]
    
    Extraction rate  -0.0631 cubic meter per sec
    Linear regression using polyfit
    slope 0.449531885929 intercept 2.77212859042
    Aquifer Transmissivity is:  0.0223 m^2/sec
    Aquifer Hydraulic Conductiviy is:  0.0027 m^2/sec
    Max distance of well influence is:  476.611020898 m.
    


[![](http://tabula0rasa.org/wp-content/uploads/2009/01/1-300x226.png)](http://tabula0rasa.org/wp-content/uploads/2009/01/1.png)
[![](http://tabula0rasa.org/wp-content/uploads/2009/01/2-300x226.png)](http://tabula0rasa.org/wp-content/uploads/2009/01/2.png)
[![](http://tabula0rasa.org/wp-content/uploads/2009/01/3-300x226.png)](http://tabula0rasa.org/wp-content/uploads/2009/01/3.png)

And that all. The full source can be fetched [here](http://tabula0rasa.org/wp-content/uploads/2009/01/problem16correctedb.py_.zip).

P.S Due to some weird problem with the new wordpress I had to upload the file zipped. Why it doesn't let me upload python sources I don't know...



