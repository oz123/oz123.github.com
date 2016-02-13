---
title: Good Bye Latex ? Hello WeasyPrint
author: Oz Nahum
published: 2012-03-20
tags: Latex, Programming, Python
public: yes
chronological : yes
kind: writing 
summary: Latex, is my main way of producing reports and scientific works. Usually these are formed as PDF before being actually printed. Latex is AWESOME.   
---

Latex, is my main way of producing reports and scientific works. Usually
these are formed as PDF before being actually printed. Latex is AWESOME.
I love writing documents with latex. That said, although I am not a
beginner with latex, when I want to deviate from normal good old latex
patterns things become a bit rough.
Despite using the Latex language for almost 5 years, I still don't fully
understand the syntax of writing packages, although mostly a long enough
search will yield some solution which does not require me to hack on my
own. Never the less this is a bit tiresome sometimes.\
Enter [WeasyPrint](https://github.com/Kozea/WeasyPrint). This project
seems really cool because it allows anyone with basic knowledge of HTML
and CSS to produce good looking PDFs. Further more, I can really think
of a simple work flow once a template is made:\
Write your documents  with
[Markdown](http://daringfireball.net/projects/markdown/), use something
like [Jekyll](https://github.com/mojombo/jekyll) to convert your easy to
understand Markdown to HTML with some [Jinja](http://jinja.pocoo.org/)or
CSS and finally convert your pages to good looking PDF's.\
I think this is more or less what [Sphinx](http://sphinx.pocoo.org/)
does (except that Sphinx uses RST instead of Markdown). I never really
mastered CSS or HTML, but this seems like a good opportunity to start
mastering both\
\
Besides, consider this:\
\
MarkDown + Convert to HTML +  WeasyPrint  = Sphinx from Scratch.\
\
Besides being a very cool educational project, a project like this can
allow people with CSS + HTML knowledge to produce some great looking
PDF. It also allowed a lot of flexibility if you are good at both.  \
\
Never the less, Latex has still one big advantage: Latex is well
designed to produce good looking documents even though you are not an
expert on typography and page layout. Additionally it is thousands of
ready made packages and kind community that can help solving many
existing problems. So maybe after all, Latex is not going away so fast!\
\

Comments
--------

Simon Sapin

Hi. WeasyPrint author here. Glad you like it! Although it's still work
in progress. Please ask anything if you need help or have feedback.
