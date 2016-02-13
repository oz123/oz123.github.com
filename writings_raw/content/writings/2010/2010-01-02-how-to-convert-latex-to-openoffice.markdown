---
title: Convert LATEX to OPENOFFICE
author: Oz Nahum
published: 2010-01-02
tags: Web, LaTeX
public: yes
chronological : yes
kind: writing 
summary: For a long time I know that I can export lyx files to ODT format, and it does a pretty good job. Today, I start lyx with moving it to the background and I looked what's going in on when I export to ODT. It's using a commant htlatex, which can be found in the Debian package tex4ht .
---

For a long time I know that I can export lyx files to ODT format, and it does a pretty good job. Today, I start lyx with moving it to the background and I looked what's going in on when I export to ODT. It's using a commant htlatex, which can be found in the Debian package tex4ht .

Here's how to use it:

    
    htlatex yourlatexfilename.tex "xhtml,ooffice" "ooffice/! -cmozhtf" "-cooxtpipes -coo"
    
    


This is pretty CPU intesive if your document is pretty complex, so be patient !

A Brief what to expect and few cavities I could not solve:



    
  1. Images are not inserted! So total fail here.

    
  2. Bibliography is done pretty good, design of your style is kept, and all the references are inserted in the correct place. However, the bibliography items, are just text, not like real references! So, here I give it "almost good"

    
  3. Styles are done nicely, so it's very good.

    
  4. Dynamic lists, i.e. Table of Contents, List of Figures etc, are not created ! Clicking Update on the Table of Contents solves the problem, however, I tried doing this on the List Of Figures, and created again the Table on Contents ! So here htlatex gets a "sufficient" grade, but not good!


So, in my opinion this is not a very good to my need, but never the less, I can't find any better alternative. If you find a better one or know how to solve one of the above issues, I'll be happy to know.

    
    
    
