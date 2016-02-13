---
title: Poor man's Read-The-Docs
author: Oz Nahum Tiram
published: 2015-01-16
tags: python, git, bash
public: yes
chronological: yes
kind: writing
summary: Here is how to build sphinx documentation on multiple branches in your Python project. If you want to have Sphinx documentation for your project without having to install the whole complicated readthedocs.org image.
---

I needed a solution to build Sphinx documentation for multiple git repositories
on multiple branches. One option was to download and install our own instace of 
Read-the-docs.org While the result is impressive, it would have left me with more
technical debt since I have had to maintain another virtual machine. 
Hence, I used an existing nginx installation to serve the staticaly 
built HTML documentation. Using a cron job that runs hourly only during work hours, 
I poll the git server, and build the  documentation if changes are detected.
The outputs from different branches are  served from subdirectories on a single 
root directory served from nginx. 

So after the introduction above here is the simple shell script that does the magic:

```shell
#!/bin/sh

CONFIG_FILE=$1

source $CONFIG_FILE
BRANCHES=($BRANCHES)
PACKAGES=($PACKAGES)
export PATH=/usr/local/bin:$PATH

function ffw(){

   git checkout $1 
   git rebase "origin/$1"

}

function build_docs(){
   cd docs
   make html 
   if [ $? -eq 0 ]; then
      echo "Make html finished with 0"
      echo -n $CURRENT > ../CURRENT_"$b"        
      cp -R build/html/ $DESTINATION/$b
      cp ../CURRENT_$b $DESTINATION/$b
   fi
   cd ..
}

cd $PROJECT_DIR
git fetch --all 

for (( i= 0; i < ${#BRANCHES[@]}; i++)) do
   b=${BRANCHES[$i]}
   ffw $b
   CURRENT=`git log --oneline -1 | cut -d " " -f 1`
   LATEST=`cat CURRENT_"$b"`
   if [ ${CURRENT} == ${LATEST} ]; then
        echo "Skipping build of "$b"..."
   else
        build_docs 
   fi
done
```

The config file is very simple:

```shell
PROJECT_DIR=/home/user/path/to/git/repo
BRANCHES="MASTER DEVELOPMENT" 
DESTINATION=/usr/share/nginx/www/
```

This script can also be modified to build tags and HEAD instead of branches. 

Before you run the script, you need to clone the repository and initialize the 
`CURRENT_$BRANCHES` files. To do this, run inside the git repository the following 
command:

```shell
for b in $BRANCHES ; do
    echo "START" > CURRENT_$b
done
``` 

Now you can add to your crontab the following task:

```
20 8-16 * * * ~/bin/build_if_new_version ~/bin/build_plugins.txt >> ~logs/build.log 2>&1
```

As your homework for practicing git, I leave it to you, to modify the script 
such that it builds also TAGS and LATEST, like in readthedocs.org 

