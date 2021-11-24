---
title: Using IPython Notebook on Linux Machines in the Enterprise Corp.
author: Oz Tiram
published: 2021-11-24
tags: Linux, SSH, Python
public: yes
chronological: yes
kind: writing
summary: >
	A short guide for using IPython and Jupyter Notebook on remote Linux machine
	in the Enterprise Corp, where you don't have root rights.
---

## Installing Python packages as normal user

The first problem is that you need to solve is that you don't have
the rights to install packages using `apt` or `yum`.
This is actually, easy to solve.
You don't need to be Admin (or `root` in the Unix terminology)
to install Python software.

You can use Python's own package manager to create isolated environments
with your own Python collection of packages.

To do so, you first need to create a `virtual environment`.
For that we invoke python as the following:

```
$ python3 -m venv <name-of-your-virtualenv>
```

For example:

```
$ python3 -m venv my-data-science-project
```

To use it you need to activate it:

```
$ source ./my-data-science-project/bin/activate
```
Doing so tells the shell where is `pip3` installed,
and it also tells `pip3` where to install packages.
Once done, you will see that your shell has a new prefix, and `pip3` is
no longer the one in `/usr/bin/`

```
(my-data-science-project)$ which pip3
/home/oz123/my-data-science-project/bin/pip3
```

Now, you can install packages into this environment. You need to tell `pip3`
to avoid compiling packages and prefer binary packages:

```
(my-data-science-project)$ pip3 install --prefer-binary jupyter
```

This will install IPython and the Jupyter Notebook in your virtual environment.
You can use IPython directly, or you can use the Web Notebook.
To use IPython simply type:

```
(my-data-science-project)$ ipython
Python 3.8.10 (default, Sep 28 2021, 16:10:42)
Type 'copyright', 'credits' or 'license' for more information
IPython 7.29.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]:
```

Using the Jupyter notebook requires a little work ...

## Using Jupyter Notebook:

If you run Jupyter notebook you will see something similar to this:

```
(my-data-science-project)$ jupyter-notebook
[I 15:00:36.756 NotebookApp] Serving notebooks from local directory: /home/oz123
[I 15:00:36.756 NotebookApp] Jupyter Notebook 6.4.6 is running at:
[I 15:00:36.756 NotebookApp] http://localhost:8888/?token=4fb831758d182a0f1c727193e41d01b54d4bf3a434e87ee1
[I 15:00:36.756 NotebookApp]  or http://127.0.0.1:8888/?token=4fb831758d182a0f1c727193e41d01b54d4bf3a434e87ee1
[I 15:00:36.756 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[W 15:00:36.759 NotebookApp] No web browser found: could not locate runnable browser.
[C 15:00:36.759 NotebookApp]

    To access the notebook, open this file in a browser:
        file:///home/oz123/.local/share/jupyter/runtime/nbserver-778704-open.html
    Or copy and paste one of these URLs:
        http://localhost:8888/?token=4fb831758d182a0f1c727193e41d01b54d4bf3a434e87ee1
     or http://127.0.0.1:8888/?token=4fb831758d182a0f1c727193e41d01b54d4bf3a434e87ee1
```

You will not be able to connect to the notebook, since per default the notebook server listens
only on the private network connection. One can force the application to listen on the public
IP addresses with:

```
(my-data-science-project)$ jupyter-notebook --ip 10.100.6.66
[I 15:03:05.068 NotebookApp] Serving notebooks from local directory: /home/oz123
[I 15:03:05.068 NotebookApp] Jupyter Notebook 6.4.6 is running at:
[I 15:03:05.068 NotebookApp] http://10.100.6.666:8888/?token=98ca17cd95dd209b7d2f2d9f0e946fee6c6d82563fdc03dd
[I 15:03:05.068 NotebookApp]  or http://127.0.0.1:8888/?token=98ca17cd95dd209b7d2f2d9f0e946fee6c6d82563fdc03dd
[I 15:03:05.068 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[W 15:03:05.070 NotebookApp] No web browser found: could not locate runnable browser.
[C 15:03:05.071 NotebookApp]

    To access the notebook, open this file in a browser:
        file:///home/oz123/.local/share/jupyter/runtime/nbserver-779914-open.html
    Or copy and paste one of these URLs:
        http://10.100.6.666:8888/?token=98ca17cd95dd209b7d2f2d9f0e946fee6c6d82563fdc03dd
     or http://127.0.0.1:8888/?token=98ca17cd95dd209b7d2f2d9f0e946fee6c6d82563fdc03dd
```

**Important**: You will have another token! Don't just copy the lines I show here.

Now, in theory, you could open the browser on your laptop and access the following address:

```
http://10.100.6.66:8888/?token=98ca17cd95dd209b7d2f2d9f0e946fee6c6d82563fdc03dd
```

You will notice, however, that nothing is loaded. That is because our servers our behind a firewall.
To access the notebook you will need to employ SSH sorcery. Namely, port forwarding.
From another Putty or Terminal access the machine where Jupyter is running in the following way:

```
ssh ds.machine.ecorp.net -L 8889:127.0.0.1:8888
```

This tells SSH to tunnel the port 8888 on the `localhost` to your local machine on port 8889.
Now if you copy line from the output of Jupyter and paste it in your browser, modifying 8888 to 8889
you should be able to access the notebook.

```
http://127.0.0.1:8889/?token=98ca17cd95dd209b7d2f2d9f0e946fee6c6d82563fdc03dd
```

OK, that was not so ergonomic. There is a lot of typing and copying and modifying. You can
configure you SSH client to do the port forwarding for you.
Add the following to the file `~/.ssh/config` on your Laptop (this will work if you are using
WSL or MobaXterm on Windows, for Putty you will have to google around):

```
Host ECorpServer
   User oz123
   Hostname ds.machine.ecorp.net
   # You can replace the line above with the internal IP of ds.machine.ecorp.net
   # Hostname 10.100.6.66
   LocalForward 8888 127.0.0.1:8888
```

This will allow you to simply do the following:

```
# on WSL
$ ssh ECorpServer
# You will now be on the remote server
oz123@ds.machine.ecorp.net:~$ source my-data-science-project/bin/activate
(my-data-science-project) oz123@ds.machine.ecorp.net:~$ jupyter-notebook
[I 15:00:36.756 NotebookApp] Serving notebooks from local directory: /home/oz123
[I 15:00:36.756 NotebookApp] Jupyter Notebook 6.4.6 is running at:
[I 15:00:36.756 NotebookApp] http://localhost:8888/?token=4fb831758d182a0f1c727193e41d01b54d4bf3a434e87ee1
[I 15:00:36.756 NotebookApp]  or http://127.0.0.1:8888/?token=4fb831758d182a0f1c727193e41d01b54d4bf3a434e87ee1
[I 15:00:36.756 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[W 15:00:36.759 NotebookApp] No web browser found: could not locate runnable browser.
[C 15:00:36.759 NotebookApp]

    To access the notebook, open this file in a browser:
        file:///home/oz123/.local/share/jupyter/runtime/nbserver-778704-open.html
    Or copy and paste one of these URLs:
        http://localhost:8888/?token=4fb831758d182a0f1c727193e41d01b54d4bf3a434e87ee1
     or http://127.0.0.1:8888/?token=4fb831758d182a0f1c727193e41d01b54d4bf3a434e87ee1
```
Back on your laptop, copy one of the URIs starting with `http://` and paste it in the location bar
of the browser on your Windows machine, and you will see the Jupyter notebook.

