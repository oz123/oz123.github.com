---
title: Data analysis with Programming
author: Oz Nahum
published: 2008-06-23
tags: Python, Programming
public: yes
chronological: yes
kind: writing 
summary: Last time I wrote about the disadventages of using a spreadsheet program to analyze large amounts of data, espcially when it comes to important data.
---

Last time I wrote about the disadventages of using a spreadsheet program to analyze large amounts of data, espcially when it comes to important data. Well, as I already said I decided to learn some programming language to do the task. So last week I was working on my homework in the course of Oceanography. Our teacher gave us an excel file containing oceanographic data from the Red Sea, Golf of Eilat (or Aqaba if you prefer). Our task was to present graphs of salinty and potential temperatue, and potential vs. pressure and do some oher calculations regarding our course. So I found my self dragging my mouse endlessly and fighting with excel to plot those graphs. I personally prefer working with [Gnumeric](http://www.gnome.org/projects/gnumeric/), but this file contained some macros to calculate the potential density of the water. So after I submitted the excercise I decided it is time to learn a programing language to do the mission. Since I aleady know python, I thought that [matplotlib][http://matplotlib.sourceforge.net/] will be a good choice.

What can I tell you, learning it and ploting my first graphs was quicker then opening excel any spreadsheet. The website has a really good tutorial and for advanced cases you can always get help from the freindly people on the project's mailing list.

Here is a short tutorial describing how I did my first oceanographic plot with matplotlib.

So, the first thing would be to import the data from the file into python. Since I already know python's interface to reading csv files it was very easy to implement. So before starting to actually program I converted each worksheet in the file into a csv file - here is an [example](http://www.tabula0rasa.org/wp-content/uploads/2008/06/data2.csv).

So now the first line of code will be:

    
    import csv
    from pylab import *
    def readData():
    ### Sets an empty arrow to hold the CSV file###
            #WordList = []
        ### call for csv module to read the CSV file
        reader = csv.reader(open("data2.csv", "rb"))
        ### store the file contents in the the array
        #global WORDLIST
        oceandata = []
        for row in reader:
               oceandata.append(row)
        return oceandata


now we have an array called oceandata and we can access it lines to preform the plotting using matplotlib. Just to make the code more human readable I like writing each task I preform under a function, and then calling it throgh the main() function, so we need a function create and array to hold all the 'x' values and the same for 'y' values:

    
    def XData(wholedata):
        x = []
        for i in wholedata:
         x.append(i[0])
        return x
    def YData(wholedata):
        y = []
        for i in wholedata:
         y.append(i[2])
        return y


Now lets look at the main() function were we really use mathplotlib:

    
    def main():
        """This is the main function of the program, it calles all the
        other functions and defines the variables"""
        setp(gca(), 'xticklabels', [])
        wholdata = readData()
        x = XData(wholdata)
        y = YData(wholdata)
        ax=twiny()
        plot(y, x, 'r')
        ax.xaxis.tick_top()
        ylabel('Depth')
        xlabel('Temperature')
        ylim(3000, 0)
    Show()


That's it! it all very clean and simple, and shorter then clicking endlessly with your mouse everywhere. Now you can just copy it to plot any oceanographic data you use. But let me explain what is done here:

The function

setp(gca(), 'xticklabels', [])
ax=twiny() is another function of mathplotlib,

plot(y, x, 'r') is the actual call to plot function and

ax.xaxis.tick_top() -tells the program to put the x axis on top as usual with oceanography data displaying.

ylabel('Depth'), xlabel('Temperature')    I guess the syntax of those two functions really talks for itself...

ylim(3000, 0) - sets the limits of the y axis. And here is the nice trick: the first number (in this case '3000') sets the beginning of the axis, and the second one sets the end, so if you want to plot 'y' in reverse order you have to plot the larger number first and the smaller number second, and if you want to have a 'normal y axis' you just type ylim(0,3000).

And here is the result:

[tempvsdepth-300x225.png)][tempvsdepth.png]

now Adding a second series, exaple the density for the graph, was really a piece of cake:

as before I added a function to store the density values:

    
    def Y1Data(wholedata):
             y1 = []
             for i in wholedata:
             y1.append(i[6])
             return y1


and changed a little main to look like this:

    
    def main():
        """This is the main function of the program, it calles all the
        other functions and defines the variables"""
        setp(gca(), 'xticklabels', [])
        wholdata = readData()
        x = XData(wholdata)
        x1 = X1Data(wholdata)
        y = YData(wholdata)
        ax=twiny()
        plot(x1,y,'b-', x,y,'r-') #notice the change: added series, 'b' for blue :-)
        ax.xaxis.tick_top()
        ylabel('Depth')
        xlabel('Temperature')
        ylim(3000, 0)
        show()


