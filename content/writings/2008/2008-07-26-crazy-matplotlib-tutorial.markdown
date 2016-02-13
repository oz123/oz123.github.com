---
title: Crazy Matplotlib tutorial
author: Oz Nahum
published: 2008-07-26
tags: Python, Programming
public: yes
chronological : yes
kind: writing 
summary: I started using python's matplotlib to plot graphs in my Oceanography courses. Matplotlib is pretty easy to understand if you already know some python. However it's documentation is somewhat frustrating, even though it comes with a plethora of examples.
---

Note: A better and more realistic tutorial can be found [here](http://www.tabula0rasa.org/2009/01/a-matplotlib-tutorial/) and a new version[ here ](http://www.tabula0rasa.org/2010/04/another-matplotlib-tutorial/).
I started using python's matplotlib to plot graphs in my Oceanography courses. Matplotlib is pretty easy to understand if you already know some python. However it's documentation is somewhat frustrating, even though it comes with a plethora of examples.

So I turned to seek help on the user's list, and that was a great experience. I got responses almost immediately, and many times the respondent was the author of the program himself. That was very nice, but people kept telling me I should read the tutorial and user guide and I kept answering that I prefer to learn by doing. Which is true. I use another program which has a steep learning curve called latex-beamer. It comes with a wonderful 300+ pages user guide. I read bits and parts of it. But mostly, I just saw other people code and copied it and changed it to fit my own presentation needs. Unfortunately, I couldn't do the same with Matplotlib, maybe because graph codes is not something people show around like beamer presentation.

So I ended up quite frustrated and I wrote the following to the mailing list:

I am a lost case about reading tutorial at the moment.
I am in a middle of a very intense course, and they expect us to do crazy stuff with matlab. so it's either that or solving with python. I'll do read it when I have time...

    
    I am mostly frustrated with documentation writers who write very nice tutorials describing
    how to plot completely unuseful graphs of spheres inside loops and a <span class="nfakPe">dolphin</span> swimming
    in the middle. Come on, this is not what users need. I am talking about what many students
    feel. We need real tutorials, this why I wrote my own little tutorial here
    <a href="../?p=21" target="_blank">http://www.tabula0rasa.org/?p=21</a>.


So I vented a lit bit my frustration. The reply didn't wait long before arriving in a very funny way:



    
    Oz Nahum wrote:
    
    >I am mostly frustrated with documentation writers who write very nice tutorials describing how
    >to plot completely unuseful graphs of spheres inside loops and a dolphin swimming in the middle.
    
    I'm sorry.  I just couldn't resist writing a tutorial example for this.  Please take it in the spirit of fun it was intended.
    
    Mike



    
    import matplotlib.pyplot as plt
    from matplotlib.patches import Circle, PathPatch
    from matplotlib.path import Path
    from matplotlib.transforms import Affine2D
    import numpy as np
    
    r = np.random.rand(50)
    t = np.random.rand(50) * np.pi * 2.0
    x = r * np.cos(t)
    y = r * np.sin(t)
    
    fig = plt.figure(figsize=(6,6))
    ax = plt.subplot(111)
    circle = Circle((0, 0), 1, facecolor=(0,0,0.8),
    edgecolor=(0,0.8,0.8), linewidth=3, alpha=0.5)
    ax.add_patch(circle)
    
    plt.plot(x, y, 'o', color=(0.9, 0.9, 1.0), alpha=0.8)
    
    # Dolphin from OpenClipart library by Andy Fitzsimon
    #
    #
    #
    #
    #
    
    dolphin = """
    M -0.59739425,160.18173 C -0.62740401,160.18885 -0.57867129,160.11183
    -0.57867129,160.11183 C -0.57867129,160.11183 -0.5438361,159.89315
    -0.39514638,159.81496 C -0.24645668,159.73678 -0.18316813,159.71981
    -0.18316813,159.71981 C -0.18316813,159.71981 -0.10322971,159.58124
    -0.057804323,159.58725 C -0.029723983,159.58913 -0.061841603,159.60356
    -0.071265813,159.62815 C -0.080250183,159.65325 -0.082918513,159.70554
    -0.061841203,159.71248 C -0.040763903,159.7194 -0.0066711426,159.71091
    0.077336307,159.73612 C 0.16879567,159.76377 0.28380306,159.86448
    0.31516668,159.91533 C 0.3465303,159.96618 0.5011127,160.1771
    0.5011127,160.1771 C 0.63668998,160.19238 0.67763022,160.31259
    0.66556395,160.32668 C 0.65339985,160.34212 0.66350443,160.33642
    0.64907098,160.33088 C 0.63463742,160.32533 0.61309688,160.297
    0.5789627,160.29339 C 0.54348657,160.28968 0.52329693,160.27674
    0.50728856,160.27737 C 0.49060916,160.27795 0.48965803,160.31565
    0.46114204,160.33673 C 0.43329696,160.35786 0.4570711,160.39871
    0.43309565,160.40685 C 0.4105108,160.41442 0.39416631,160.33027
    0.3954995,160.2935 C 0.39683269,160.25672 0.43807996,160.21522
    0.44567915,160.19734 C 0.45327833,160.17946 0.27946869,159.9424
    -0.061852613,159.99845 C -0.083965233,160.0427 -0.26176109,160.06683
    -0.26176109,160.06683 C -0.30127962,160.07028 -0.21167141,160.09731
    -0.24649368,160.1011 C -0.32642366,160.11569 -0.34521187,160.06895
    -0.40622293,160.0819 C -0.467234,160.09485 -0.56738444,160.17461
    -0.59739425,160.18173
    """
    
    vertices = []
    codes = []
    parts = dolphin.split()
    i = 0
    code_map = {
    'M': (Path.MOVETO, 1),
    'C': (Path.CURVE4, 3),
    'L': (Path.LINETO, 1)
    }
    
    while i < len(parts):
    code = parts[i]
    path_code, npoints = code_map[code]
    codes.extend([path_code] * npoints)
    vertices.extend([[float(x) for x in y.split(',')] for y in parts[i+1:i+npoints+1]])
    i += npoints + 1
    vertices = np.array(vertices, np.float)
    vertices[:,1] -= 160
    
    dolphin_path = Path(vertices, codes)
    dolphin_patch = PathPatch(dolphin_path, facecolor=(0.6, 0.6, 0.6),
    edgecolor=(0.0, 0.0, 0.0))
    ax.add_patch(dolphin_patch)
    
    vertices = Affine2D().rotate_deg(60).transform(vertices)
    dolphin_path2 = Path(vertices, codes)
    dolphin_patch2 = PathPatch(dolphin_path2, facecolor=(0.5, 0.5, 0.5),
    edgecolor=(0.0, 0.0, 0.0))
    ax.add_patch(dolphin_patch2)
    
    plt.show()


and of course, here is a picture of this plot:

[![](http://www.tabula0rasa.org/wp-content/uploads/2008/07/dolphin-300x300.png)](http://www.tabula0rasa.org/wp-content/uploads/2008/07/dolphin.png)
