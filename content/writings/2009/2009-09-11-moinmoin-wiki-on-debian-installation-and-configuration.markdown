---
title: MoinMoin wiki on Debian, Installation and configuration
author: Oz Nahum
published: 2009-08-27
tags: Linux, Python, Wiki
public: yes
chronological : yes
kind: writing 
summary: Sometimes, installation of Debian packages is too easy, but then configuration can be quite confusing.
---


=======================================================
posted: 2009-09-11 23:04:23
slug: moinmoin-wiki-on-debian-installation-and-configuration

Sometimes, installation of Debian packages is too easy, but then configuration can be quite confusing.

This is the case, in my opinion, with the README.Debian file which describes an example of moin-moin wiki installation under a subdomain wiki.example.org.

Here are my notes of how to install moinmoin package from Debian Squeeze on Debian Lenny.

First, you need to install python-support from debian-backports.org.

Second, download manually or with apt-get the package of debian lenny for python-moinmoin.

Install both packages, if you downloaded them manually with the command:

    
    dpkg -i python-support_1.0.3~bpo50+1_all.deb python-moinmoin_1.8.4-1_all.deb


After that you need to issue the following command, which are also described in the README.Debian:

1) Create and populate /var/www/mywiki

    
    mkdir /var/www/mywiki



    
    cp -r /usr/share/moin/server/moin.cgi /var/www/mywiki
    mkdir /var/lib/mywiki
    cp -r /usr/share/moin/data /usr/share/moin/underlay /var/lib/mywiki


2) Pass on the wiki to Apache:

    
     chown -R www-data: /var/www/mywiki /var/lib/mywiki


3) Configure Apache2:
Add the following as /etc/apache2/sites-available/mywiki:

    
    <VirtualHost *:80>
     #comment the line below if you intend to use only http://localhost/mywiki
     ServerName wiki.example.org
     DocumentRoot /var/www/mywiki/
     Alias /moin_static184/applets/FCKeditor/ "/usr/share/fckeditor/"
     Alias /moin_static184/ "/usr/share/moin/htdocs/"
     ScriptAlias /MyWiki "/var/www/mywiki/moin.cgi"
    </VirtualHost>
    <Directory /var/www/mywiki/>
     Options Indexes FollowSymLinks MultiViews
     AllowOverride None
     Order allow,deny
     allow from all
     Options +ExecCGI
    </Directory>


4) Configure MoinMoin:

Edit /etc/moin/farmconfig.py to commentout data_dir and
data_underlay_dir (we need those defined separately for each wiki)

Edit /etc/moin/mywiki.py to include these lines:

    
     sitename = u'MyWiki' # [Unicode]



    
     data_dir = '/var/lib/mywiki/data'
     data_underlay_dir = '/var/lib/mywiki/underlay'


Edit /etc/moin/wikilist to include this line:

    
     www-data wiki.example.org/


5) Activate wiki:

    
    a2ensite mywiki
    invoke-rc.d apache2 reload


6) Enjoy your new wiki at http://your.site/MyWiki/


### A Note about themes, debian, moin-moin


Debian is intended for the server... Thus it's quite biased for a wiki-farm rather than a personal use wiki. Default moinmoin shares lot's of files between different possible moinmoin installations.

The appropriate directory for installation of themes, under Debian won't be the data directory (in the above example, /var/lib/mywiki/data)  rather a shared directory under /usr/share/moin/htdocs.

So the css/, img/, js/ directories of a plugin go there, and the python module of the theme goes to /var/lib/mywiki/data/plugin/theme.

Here is an example of how I installed fixedleft theme:

    
    ls -p /usr/share/moin/
    config/  data/    htdocs/  server/  underlay/
    
    ls -p /usr/share/moin/htdocs/
    applets/  common/      fixedleft/  modern/    rightsidebar/
    classic/  favicon.ico  index.html  modernized/    robots.txt
    
    ls -p /usr/share/moin/htdocs/fixedleft/
    css/  img/  js/
    
    ls -p /var/lib/mywiki/data/plugin/theme/
    fixedleft.py  fixedleft.pyc  __init__.py  __init__.pyc


To activate the theme, you need to /etc/moin/mywiki.py, add the following line:

    
    theme_default = 'fixedleft'


to activate fixed left as the default theme.

If you have two lines like this:

    
    theme_default = 'rightsidebar'
    theme_default = 'fixedleft'


The last one will be the effective one.
