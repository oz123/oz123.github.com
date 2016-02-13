---
title: Floats wider than text in Latex
author: Oz Nahum
published: 2010-09-16
tags: LaTeX, Debian, Programming
public: yes
chronological : yes
kind: writing 
summary: Latex floats  by default have the text width or smaller. Took me some time to figure out how to make a float wider than the text width itself.
---

Latex floats  by default have the text width or smaller. Took me some time to figure out how to make a float wider than the text width itself.
Here is an example how it is possible to do it, with pretty simple setup and no custom packages. Just note the custom command defined:


    
    
    \documentclass{article}
    \usepackage{changepage}
    \usepackage{graphicx}
    \usepackage{float}
    \usepackage{lipsum}% just to automatically generate some text
    \newenvironment{changemargin}[2]{\begin{list}{}{
    \setlength{\topsep}{0pt}\setlength{\leftmargin}{0pt}
     \setlength{\rightmargin}{0pt}
     \setlength{\listparindent}{\parindent}
     \setlength{\itemindent}{\parindent}
     \setlength{\parsep}{0pt plus 1pt}
     \addtolength{\leftmargin}{#1}\addtolength{\rightmargin}{#2}
     }\item }{\end{list}}
    
    \begin{document}
    
    \lipsum[1-2]
    
    \begin{figure}[t]
    \begin{changemargin}{-3cm}{2cm}
     \lipsum[1]
     \includegraphics[scale=0.3]{./pics/co3-2gim-reaction.png}
    \end{changemargin}
    \caption{asdfasdf}
    \end{figure}
    
    \lipsum[1-5]
    
    \end{document}
    
