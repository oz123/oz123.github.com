---
title: Playing with wordpress - Hacking the header to display random pictures  
author: Oz Nahum
published: 2008-09-03
tags: Programming, Wordpress, Web
public: yes
chronological : yes
kind: writing 
summary: After I started seriously playing with wordpress and discovered how cool it is, I decided that I can seriously hack to it my own needs.
---


After I started seriously playing with wordpress and discovered how cool it is, I decided that I can seriously hack to it my own needs. I looked and many many themes and found this theme called amazing grace. It has lots of cool features, but I find its overall look a bit overwhelming and childish. My heart goes into simple themes like andreas. But I decided to borrow the random header image from amazing grace. This random image effect can be achieved with plugins like nextgen gallery, but in order to keep it simple I borrowed one line of code from amazing grace. So in this short tutorial I'll show how to do it with wp-andreas theme.

Andreas theme comes with 15 different header images. In order to change between them randomly we first have to rename them all in the following scheme fornt0.jpg, front1.jpg front2.jpg and so on.

Next we open the file header.php with a text editor, or the theme editor from within wordpress, and we change the following line:
`<img id="frontphoto" src="<?php bloginfo('template_directory'); ?>/img/front.jpg" width="760" height="175" alt="" />`
to:
`<img id="frontphoto" src="<?php bloginfo('template_directory'); ?>/img/front<?php echo (rand()%14); ?>.jpg" width="760" height="175" alt="" />`
next we save the file, and that's it. We're done!

Now hit the refresh button on your main page of your blog and see how the header image changes with every refresh we do.
