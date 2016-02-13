---
title: Evalution of a Tracer Test with Python scipy.optimize
author: Oz Nahum
published: 2009-10-10
tags: Programming, Python
public: yes
chronological : yes
kind: writing 
summary: Sometimes, installation of Debian packages is too easy, but then configuration can be quite confusing.
---

This post is not intended only to hydrogeologists, but also to any one who needs a working example of the use of a function minimum search.

It is very common for many scientific problems to search for a minimum condition. In optimization of problems it's very common to use a minimum of least squares function between measured results and some model function.

In the following code you can see the results of a tracer test procedure preformed at a test site called Lauswiesen, at the skirts of ??Tubingen in southren Germany. This tracer test was performed as part of a course called Field Methods in Hydrogeology given in the Master's program of Applied Environmental Geosciences.



In the test we injected fluorescence into a well located 8.81 meter from a pumping well in order to estimate a parameter of the aquifer called dispersivity. The measurment well done by a fluorescence detector at the pumping well at the level of PPB's.

The code for evaluating the results is given in the following:

###

    
    # This program anaylises a tracer test results to find the longitudinal
    # dispersivity of an aquifer. It applies the 1D flow field model as
    # described by Jean-Pierre Sauty, 1980 in "An analysis of Hydrodispersive Transfer in Aquifers"
    ###
    
    #       This program is free software; you can redistribute it and/or modify
    #       it under the terms of the GNU General Public License as published by
    #       the Free Software Foundation; either version 3 of the License, or
    #       (at your option) any later version.
    #       
    #       This program is distributed in the hope that it will be useful,
    #       but WITHOUT ANY WARRANTY; without even the implied warranty of
    #       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    #       GNU General Public License for more details.
    #       
    #       You should have received a copy of the GNU General Public License
    #       along with this program; if not, write to the Free Software
    #       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
    #       MA 02110-1301, USA.
    
    from pylab import *
    from numpy import *
    from scipy.optimize import leastsq, fmin
    from time import time
    
    ###
    
    a=time()
    #injected mass in Kg
    M = 0.01;
    #distance between  the wells
    r = 8.81; #[m]
    ## pumping rate
    Q = 0.0061; #[m^3/sec]
    ##thickness of aquifer saturated with water
    b=4.61; #[m];
    ##uncertainty of the measurments  (concentration measurments)
    sigma_s = 0.01; # [m]
    
    ####
    ## define the measurments
    ####
    
    t = array([1.0,300.0,600.0,    900.,    1200.,    1260.,    1320.,    1380, \
     1440,    1500,    1560,    1620,    1680,    1740,    1800,    1860,
     1920,    1980,    2040,    2100,    2160,    2220,    2280,    2340,\
     2400,    2460,    2520,    2580,    2640,    2700,    2760,    2820,\
     2880,    2940,    3000,    3060,    3120,    3180,    3240,    3300,
     3360,    3420,    3480,    3540,    3600,    3660,    3720,    3780,\
     3840,    3900,    4200,    4500,    4800,    5100,    5400,    5700,\
     6000,    6300,    6600,    6900,    7200,    7500,    7800,    8100,\
     8400,    8700,    9000,    9300,    9600,    9900,   10200,    10500,\
     10800,    11100,    11400,    12000])
    #print t.shape
    t = t.transpose()
    #print t.shape
    
    c = (array([0.07,    0.1,    0.11,    0.13,    1.17,    2.15,    3.65,    5.64,\
     8.12,    11,    14.3,    17.3,    20.6,    23.5,    26.5,    29.1,\
     31.5,    33.5,    35.3,    36.8,    37.9,    38.8,    39.5,    39.8,\
     40.1,    40.2,    40.1,    39.9,    39.5,    39,    38.5,    37.9,    \
     37.3, 36.5,    35.9,    35.1,    34.4,    33.5,    32.9,    32,    \
     31.2,    30.5,    29.9,    29,    28.2,    27.5,    26.8,    26.1,    \
     25.4,    24.7,    21.7,    19,    16.8,    14.8,    13.3,    12.1,    \
     11,    10.1,    9.4,    8.81,    8.15,    7.71,    7.3,    6.98,    \
     6.67,    6.36,    6.12,    5.92,    5.78,    5.58,    5.41,    5.15,    \
     4.77,    4.54,    4.37,    4.19])-0.07)*1e-9*1350
    
    c=c.transpose()
    
    #invCss=diag(ones(size(c)))*1/sigma_s**2
    
    #print invCss
    ## cmax , tmax definitions for 1D model
    ## cmax = 5.427e-5; #already in Kg/m^3
    ## kann auch mit max(c) finden\
    #
    ## die index mit find(c==max(c)) kann man auch finden
    
    cmax = max(c)
    tmax = t[find(c==cmax)]# 2460 ; #sec
    cr=c/cmax # dimensionless concentration [-]
    crmax = max(cr)
    tr=t/int(tmax) # dimensionless time [-]
    trmax = tr[find(cr==crmax)]
    
    #icmax= c.argmax()
    #cmax = c[icmax]
    #tmax = t[icmax]
    #cr=c/cmax
    #crmax=cr[icmax]
    #tr=t/int(tmax)
    #trmax=tr[icmax]
    
    def residuals(alpha, tr, cr):
     #defintion for 1D flow Field
     P = r/alpha#Peclet Number [-]
     tmax=sqrt(1+P**(-2))-1/P;
     #see eq. 21 in Sauty, 1980, this creates a tmax(P), and P(alpha)
     K = tmax**0.5*exp((P/4/tmax)*(1-tmax)**2)
     A=-P/(4*tr)*(1-tr)**2#dimensionless
     f=K/tr**0.5*exp(A)#dimensionless
     err=(f-cr)
     err=err**2
     err=sum(err)
     return err
    
    def OneDmodel(alpha, r):
     ###Calculate the model for plotting !!!
     P = r/alpha# #Peclet Number [-]
     tmax=sqrt(1+P**(-2))-1/P# %see eq. 21 in Sauty, 1980, this creates a tmax(P), and P(alpha)
     K = sqrt(tmax)*exp(P/(4*tmax)*(1-tmax)**2)
     A=-P/(4*tr)*(1-tr)**2#; %dimensionless
     f=K/tr**0.5*exp(A) #%dimensionless
     return f
    
    p0 = 3 #initial alpha value
    #x = arange(0,6e-2,6e-2/30)  
    #alpha = leastsq(residuals, p0, args=(cr, tr))
    alpha = fmin(residuals, p0, args=(tr,cr),maxiter=10000, maxfun=10000)
    b=time()-a
    print 'took ',b ,'sec to run'
    #print plsq[0]
    
    print 'optimized dispersivity is ', alpha[0], 'meters.'
    alpha=alpha[0]
    oneDmodel = OneDmodel(alpha,r)
    ### Plot
    plot(tr,cr, 'r+-')
    plot(tr, oneDmodel, 'bo-')
    xlabel('Relative Time [t/tmax]')
    ylabel('Relative Concentration [C/Cmax]')
    legend(['Real', 'Fit'])  
    show()


The output of this code is the following plot, and the calculated dispersivity.

[](http://www.tabula0rasa.org/wp-content/uploads/2009/10/TracerTest1DModelfromPython.png)[![](http://tabula0rasa.org/wp-content/uploads/2009/10/TracerTest1DModelfromPython-300x225.png)](http://tabula0rasa.org/wp-content/uploads/2009/10/TracerTest1DModelfromPython.png)

We conclude this short post with:
[ad#banner]

Many people would use matlab as a first option to do stuff like this, but it's more than possible with python. I even compared the same code run in matlab and found it to be slower, and harder to write in my opinion.

Optimization with python is fun. Now go measure stuff and have fun with python.

I hope this post is found by some hydrogeologist who can actually use this code for something good ! If you used this code and liked it, please send me your opinion!
