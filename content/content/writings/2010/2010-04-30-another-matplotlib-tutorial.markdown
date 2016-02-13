---
title: Another matplotlib tutorial
author: Oz Nahum
published: 2010-04-24
tags: Programming, Fortran
public: yes
chronological : yes
kind: writing 
summary: Recently I started working with [MIN3P](http://www.eos.ubc.ca/about/faculty/U.Mayer.html), a reactive transport modeling software, which produces data output which can be easily visualized with a commercial software package. However, I can't afford purchasing this package for my research, and I won't even though they have a Linux client.
---

Recently I started working with [MIN3P](http://www.eos.ubc.ca/about/faculty/U.Mayer.html), a reactive transport modeling software, which produces data output which can be easily visualized with a commercial software package. However, I can't afford purchasing this package for my research, and I won't even though they have a Linux client.
Instead, I decided to dedicate sometimes to improve my matplotlib skills, and write some scripts to visualize the output.
In the following is another short tutorial of visualization of a series of output data files from a demo problem of 1D transient flow and evaporation in a 1D soil column in the length of 3 meters.

First, here is an example structure of the data output files:

    
    title = "dataset evap"
    variables = "x", "y", "z", "h_w", "p_w", "s_w", "theta_w", "s_g", "theta_g", "q_root", "evap"
    zone t = "Flow variables, initial condition" i =  300, j =    1, k =    1,  f=point
      0.0000000E+00  0.0000000E+00  0.0000000E+00 -0.9500000E+00 -0.9500000E+00  0.6920443E+00  0.2512121E+00  0.3079557E+00  0.1117879E+00  0.2339689-267  0.2100667E+00
      0.0000000E+00  0.0000000E+00  0.1003344E-01 -0.1000000E+01 -0.1010033E+01  0.6766303E+00  0.2456168E+00  0.3233697E+00  0.1173832E+00  0.2339689-267  0.2100667E+00
      0.0000000E+00  0.0000000E+00  0.2006689E-01 -0.1000000E+01 -0.1020067E+01  0.6741777E+00  0.2447265E+00  0.3258223E+00  0.1182735E+00  0.2339689-267  0.2100667E+00
    


There are 5 output times at 0, 10,20,30,50 days of flow. And each file has 300 rows, representing 300 hundreds nodes. Obviously, producing graphs from these data files with a spread sheet software would be a tedious task.
[ad#ad-2]
So, here python and matplotlib come to help again. First, we need a mechanism to read the files into a plot-able array format. For this I re-use a function from [scipy cookbook](http://www.scipy.org/Cookbook), with slight changes to fit the output format.

    
    def read_array2(filename, dtypes,lineskip=3, separator='  '):
        """ Read a file with an arbitrary number of columns.
            The type of data in each column is arbitrary
            It will be cast to the given dtype at runtime
            This is an improved function that also cleanes the data
        """
        startFromLine = lineskip
        linesCounter = 1
        cast = N.cast
        # a nice syntax to initialize a list with determine size
        data = [[] for dummy in xrange(len(dtypes))]
        for line in open(filename, 'r'):
            #print type(line)
            if linesCounter>startFromLine:
                fields = line.strip().split(separator)
                #clean double numbers because of minus signs
                for i, number in enumerate(fields):
                    temp=number.split(" ")
                    if len(temp)>1:
                        #pdb.set_trace()
                        del fields[i]
                        for j, hold in enumerate(temp):
                            #print j, hold
                            #pdb.set_trace()
                            fields.insert(i+j,hold)
                            #print len(fields)
                        del temp
                #remove trailing calvin degrees in fields
                for i, number in enumerate(fields):
                    if number[-4]=='-':
                        hold=number[:-4]
                        del fields[i]
                        fields.insert(i,hold)
                #split fields and append to data
                for i, number in enumerate(fields):
                    data[i].append(number)
                   #data[i].append(number)
            linesCounter=linesCounter+1
        #cast data to a nice array
        #pdb.set_trace()
        for i in xrange(len(dtypes)):
            data[i] = cast[dtypes[i]](data[i])
        return N.rec.array(data, dtype=dtypes)
    


The cool thing about this function is that it returns an array which can be accessed in a similar way done in R. It takes a N.dtype which is the description of the array columns. Here is an example:

    
    gsp_descr = N.dtype([("x",'float32'), ("y", 'float32'),("z",'float32'), ("h_w",'float32'),\
     ("p_w",'float32'), ("s_w",'float32'), ("theta_w",'float32'), ("s_g",'float32'),\
     ("theta_g",'float32'), ("q_root", 'float32'),("evap",'float32')])
    


This is just the header of the file copied with the definition type of each column.
Next, we need to read the files, which can be downloaded [here](http://www.tabula0rasa.org/wp-content/uploads/2010/04/evap.zip).

    
    day1 = read_array2('../evap_0.gsp', gsp_descr)
    day10 = read_array2('../evap_1.gsp', gsp_descr)
    day20 = read_array2('../evap_2.gsp', gsp_descr)
    day30 = read_array2('../evap_3.gsp', gsp_descr)
    day50 = read_array2('../evap_4.gsp', gsp_descr)
    


I now have all the data loaded into the python shell. Next, I would like to plot the data. Since this is a depth oriented data I would to plot it that the Y axis is reversed and the X axis is on the top. Another requirement, is that I would like to plot all the data on the same plot, using subplots. This means I want to have 5 line graphs, in the same figure. So let's begin:

I start by creating a figure instance, and creating a subplot with 1 row and 5 columns:

    
    fig = plt.figure() #plt is matplotlib.pyplot
    ax1 = fig.add_subplot(151)
    


Next, I add some graph into the designated subplot area:

    
    a=ax1.plot(day1['h_w'],day1['z'],'-')
    #ax1.plot(day1['p_w'],day1['z'],'-')
    b=ax1.plot(day1['s_w'],day1['z'],'-')
    c=ax1.plot(day1['theta_w'],day1['z'],'-')
    #ax1.plot(day1['p_w'],day1['z'],'-')
    d=ax1.plot(day1['theta_g'],day1['z'],'-')
    e=ax1.plot(day1['evap'],day1['z'],'-')
    


Notice, that I assigned each line element into a letter variable. This seems odd, but I can tell you now that later, I will use the variables to create a fancy legend to the plot with them.
typing

    
    show()


in the python console will create the following graph:
[](http://www.tabula0rasa.org/wp-content/uploads/2010/04/graph1.png)[![graph1](http://tabula0rasa.org/wp-content/uploads/2010/04/graph1-300x200.png)](http://tabula0rasa.org/wp-content/uploads/2010/04/graph1.png)
You can type CTRL+C to break from the figure and work interactively with the figure. Now, I will modify the location of the X axis, to be on top, notice that draw() function is redrawing the graph:

    
    ax1.xaxis.tick_top()
    draw()
    


Which results in:
[[![graph2](http://tabula0rasa.org/wp-content/uploads/2010/04/graph2-300x200.png)](http://tabula0rasa.org/wp-content/uploads/2010/04/graph2.png)](http://www.tabula0rasa.org/wp-content/uploads/2010/04/graph2.png)

The labels on the top X axis are a bit to crowded, so I will rotate them, and change the odd default limits that are chosen. In addition I will revert the Y axis:

    
    setp(plt.gca().get_xmajorticklabels(),
             size=10,rotation=30)
    ax1.set_xlim(-1, max(day1['s_w']))
    bottom, top = ax1.get_ylim()
    ax1.set_ylim(top, bottom)
    draw()
    


Which results in:
[[![graph3](http://tabula0rasa.org/wp-content/uploads/2010/04/graph3-300x200.png)](http://tabula0rasa.org/wp-content/uploads/2010/04/graph3.png)](http://www.tabula0rasa.org/wp-content/uploads/2010/04/graph3.png)
Now we need to add figure titles:

    
    ax1.set_ylabel('Depth')
    t=ax1.set_title('day 00')
    t.set_position((0.5,1.05))
    ax1.grid()
    


Notice, I changed the default location of the top title which collides with the tick labels, since by default there is no labels on the top. This is done with the last two lines above. In addition I added a grid in the plot. So, far pretty straight forward.

Next we need to add the other subplots:

    
    ax1 = fig.add_subplot(152)
    ax1.plot(day10['h_w'],day1['z'],'-')
    ax1.plot(day10['s_w'],day1['z'],'-')
    ax1.plot(day10['theta_w'],day1['z'],'-')
    ax1.plot(day10['theta_g'],day1['z'],'-')
    ax1.plot(day10['evap'],day1['z'],'-')
    ax1.xaxis.tick_top()
    bottom, top = ax1.get_ylim()
    ax1.set_ylim(top, bottom)
    ax1.set_xlim(0, max(day1['s_w']))
    ax1.grid()
    ax1.set_yticklabels([])
    setp(plt.gca().get_xmajorticklabels(),
             size=10,rotation=30)
    t=ax1.set_title('day 10')
    t.set_position((0.5,1.05))
    


This results in:
[[![graph4](http://tabula0rasa.org/wp-content/uploads/2010/04/graph4-300x200.png)](http://tabula0rasa.org/wp-content/uploads/2010/04/graph4.png)](http://www.tabula0rasa.org/wp-content/uploads/2010/04/graph4.png)
Here I used `ax1.set_yticklabels([]) ` to hide the y axis labels, since it's going to be overcrowded showing them 5 times ! The rest is pretty similar, repeating what we so far.

Finaly, I create a legend with 5 columns, thus forcing a wide legend shape, which can fit in the bottom of the figure:

    
    figlegend( (a,b,c,d,e),
              ('h_w', 's_w', 'theta_w','theta_g','evap'),
             'lower center',ncol=5)
    


Here is the final result:
[[![graph5](http://tabula0rasa.org/wp-content/uploads/2010/04/graph5-300x200.png)](http://tabula0rasa.org/wp-content/uploads/2010/04/graph5.png)](http://www.tabula0rasa.org/wp-content/uploads/2010/04/graph5.png)
The full code can be found [ad#banner]

[view_gsp.py](http://tabula0rasa.org/wp-content/uploads/2010/04/view_gsp.py_.zip) and the [data files](http://tabula0rasa.org/wp-content/uploads/2010/04/evap.zip).
