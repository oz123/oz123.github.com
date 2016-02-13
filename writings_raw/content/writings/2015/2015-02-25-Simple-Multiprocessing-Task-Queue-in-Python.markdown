---
title: Simple Multiprocessing Task Queue in Python
author: Oz Nahum Tiram
published: 2015-02-25
tags: python, linux
public: yes
chronological: yes
kind: writing
summary: Yet another tutorial about Python's multiprocessing. What make this one different? Well, it's based on a real life example and shows what is going on behind the sceanes on your Linux host. 
---

Python's most popular implementation does `Threading` quite differently from what
most people understand. In order to utilize multiple CPUs on a modern computer, one
has to start multiple processes. One way to do it, is to write python programs
which accept command line parameters and start different instances with different 
parameters (either from the shell or using Python's `subprocess` module. 
Thus, one lets the Operating System utilize the CPUs.  
But one can also start multiple Python processes directly from within a running 
Python program. 

In the following tutorial, a simple multiple tasks are started via a main process, 
which looks for tasks, and when it finds them, it runs them without blocking the 
main process (which has only one task, look for tasks and lunch them when found). 
If you want to see a full blown application that does something similar to that, 
e.g. a Task Queue see [Celeryproject.org](celeryproject.org).

So let's get started. The skeleton of the application called `tasku.py` is rather 
simple:


```python
def run():
    
    """
    The main loop of tasku where everything happens.
    """
    
    while True:
        for task in check_for_tasks():
            start_task(task)
        clean_finished_tasks()


if __name__ == '__main__':
   run()
```

The application is quite straight forward. Jobs are sought, and when found they are launched. 
A second step cleans all the finished tasks. But the above application lack the functions,
`check_for_task`, `start_task` and `clean_finished_tasks`. Let's begin defining a `Task` 
and `check_for_tasks`.

A `Task` is a Python class that does not do much, it starts, reads a message from a file, 
and hangs around for a period of time which is also read from that file. The fact that 
the task does not immediately terminate is useful, so we can see the task in the OS process tree:

```python

class Task(object):
   """
   read a task file with the following content: Hello Parallel Tasks;5
   """
   def __init__(self, taskfile):
      self.name = taskfile
      with open(taskfile) as t:
           msg, delay = t.read().split(";")
      
      self.msg = msg
      self.delay = delay
   
   def run(self):
       print(self.msg)
       time.sleep(self.delay)
```

The `Task` class is also quite straight forward. It has a constructor, and a `run` method. 
The function `check_for_tasks` is as follows:

```python
def check_for_tasks():
    """
    find files with .task ending in current directory.
    This a file based no-priority queue which only find the files
    """
    tasks = filter(lambda x: x.endswith('.task'),
                  filter(path.isfile, os.listdir('.')))
    # this should also check for jobs that are not already running ...
    return tasks
```

The `Task` file can be named `do_something.task` and `say_hello.task` they will be return in 
alphabetical order. Hence, priority setting is by the naming of files. 

Next, the function `start_task` is shown, and finally, multiprocessing is coming 
into the game:

```python

def start_task(task):
    """
    open the file, read it's conent, then start a process with the file
    running is a global directory holding the running jobs
    """
    if task not in running:

        ti = Task(task)

        p = mp.Process(target=ti.run, name=ti.name)
        p.start()
        running[ti.name] = (p, p.pid, p.is_alive()) 
```

Note, here that I did `import multiprocessing as mp`. The last step in the main 
loop is `clean_finished_tasks`:

```python
def clean_finished_tasks():
    """
    Check the running dictionary for items, each task that is done,
    is moved to the correct place (errors, or completed),
    errors and executed are global dictionaries. 
    """
    for k, v in running.items():
        print k, v.is_alive()
        if not v.is_alive():
            if v.exitcode:
                errors[k] = v.exitcode
            else:
                executed[k] = 'success!'
                running.pop(k)
                os.rename(k, k+'.done')
```

Finally, all the building stones are there. The full program is then:

```python 
import multiprocessing as mp
import os
from os import path
import time
import datetime

# non persistant task list
running = {}
executed = {}
errors = {}


class Task(object):
    """
    read a task file with the following content: Hello Parallel Tasks;5
    """

def __init__(self, taskfile):
    self.name = taskfile
    with open(taskfile) as t:
        msg, delay = t.read().split(";")

    self.msg = msg
    self.delay = int(delay)

def run(self):
    print(self.msg)
    time.sleep(self.delay)


def check_for_tasks():
    """
    find files with .task ending in current directory.
    This a file based no-priority queue which only find the files
    """
    tasks = filter(lambda x: x.endswith('.task'),
                    filter(path.isfile, os.listdir('.')))
    # this should also check for jobs that are not already running ...
    return tasks


def start_task(task):
    """
    open the file, read it's conent, then start a process with the file
    running is a global directory holding the running jobs
    """
    if task not in running:

        ti = Task(task)

        p = mp.Process(target=ti.run, name=ti.name)
        p.start()
        running[ti.name] = (p, p.pid, p.is_alive())


def clean_finished_tasks():
    """
    Check the running dictionary for items, each task that is done,
    is moved to the correct place (errors, or completed),
    errors and executed are global dictionaries.
    """
    for k, v in running.items():
        print k, v[0].is_alive()
        if not v[0].is_alive():
            if v[0].exitcode:
                errors[k] = v[0].exitcode
            else:
                executed[k] = 'success!'
                running.pop(k)
                os.rename(k, k+'.done')


def run():
    """
    The main loop of tasku where everything happens.
    """

    while True:
        for task in check_for_tasks():
            start_task(task)

        clean_finished_tasks()
        print "successfully cleaned! "
        # added some information output
        print "executed, ", executed
        print "running, ", running
        print datetime.datetime.now()
        # add some delay so, we could see what is going on in the OS
        time.sleep(5)

if __name__ == '__main__':
    run()
```

To see what happens when this code runs, start it with `python tasku.py`, you 
should see something similar to this:

```
$ python tasku.py                               
executed,  {}                                                                      
running,  {}                                                                       
2015-02-25 21:32:51.766882                                                         
executed,  {}                                                                      
running,  {}                                                                       
2015-02-25 21:32:56.771922  
```

This is kind of Boring, so let's put create a task. On a different shell issue:

	$ echo "I am the first task;7" > 1.task 

After a maximum of 5 seconds you should see you task working:

    executed,  {}
    running,  {}
    2015-02-26 05:03:27.223866
    1.task True
    executed,  {}
    running,  {'1.task': (<Process(1.task, started)>, 6882, True)}
    2015-02-26 05:03:32.232389
    I am the first task
    1.task True
    executed,  {}
    running,  {'1.task': (<Process(1.task, started)>, 6882, True)}
    2015-02-26 05:03:37.237662
    1.task False
    successfully cleaned 1.task ! 
    executed,  {'1.task': 'success!'}
    running,  {}
    2015-02-26 05:03:42.243716


The task has it's own PID, and you can see the process tree with `pstree`:

    $ pstree -a -p 6870
    python,6870 tasku.py
      |
       `-python,6882 tasku.py

The process `6882` is launched by 6870. You can find this by doing:

    echo "I am the first task;7" > 1.task && sleep 3 && pgrep -f tasku

To make thing a bit more interesting in `tasku` lets see what happens when multiple
tasks are placed on the queue for immediate run, but different delay times to 
finish. In order to automate the putting of tasks I wrote a Makefile which 
can be downloaded here. The following assumes this make file was downloaded
(You can find all the sources needed for here: [tasku.py](https://gist.github.com/oz123/b3aab600e629fcd37d54)).

    make create_all_tasks

The `create_all_tasks` target will enqueue 4 jobs with different delay times, wait
a little for `tasku` to find and launch the tasks and then print the process tree.
Here is what should be seen in both terminals:

```
make create_all_tasks
echo

python,26652 tasku.py
  |-python,26653 tasku.py
  |-python,26654 tasku.py
  |-python,26655 tasku.py
  `-python,26656 tasku.py
python,26653 tasku.py
python,26654 tasku.py
python,26655 tasku.py
python,26656 tasku.py
```

The process `tasku.py`

```
$ python tasku.py`
I am the the second task
this task will finish quickly
2.task True
3.task True
1.task True
4.task True
executed,  {}
running,  {'2.task': (<Process(2.task, started)>, 26653, True), '3.task': 
          (<Process(3.task, started)>, 26654, True), 
          '1.task': (<Process(1.task, started)>, 26655, True), 
          '4.task': (<Process(4.task, started)>, 26656, True)}
2015-02-26 10:48:21.235133
this task will hang around
I am the first task
2.task True
3.task True
1.task True
4.task True
executed,  {}
running,  {'2.task': (<Process(2.task, started)>, 26653, True), 
           '3.task': (<Process(3.task, started)>, 26654, True), 
           '1.task': (<Process(1.task, started)>, 26655, True), 
           '4.task': (<Process(4.task, started)>, 26656, True)}
2015-02-26 10:48:26.242138
2.task False
3.task False
1.task False
4.task True
successfully cleaned 2.task ! 
successfully cleaned 3.task ! 
successfully cleaned 1.task ! 
executed,  {'2.task': 'success!', '3.task': 'success!', '1.task': 'success!'}
running,  {'4.task': (<Process(4.task, started)>, 26656, True)}
2015-02-26 10:48:31.248629
4.task False
successfully cleaned 4.task ! 
executed,  {'2.task': 'success!', '3.task': 'success!', 
            '1.task': 'success!', '4.task': 'success!'}
running,  {}
```

As can be seen, the main process (`pid 26652`) now launched other processes, 
which take a certain delay time to finish. Once, these process are finish, they 
will exist, and will no longer be found in the process tree. This way, one can
distribute the work of certain complicated tasks to multiple CPUs using python. 
This rudimentary example only scratches the surface of `multiprocessing`. For 
example it does not show how the processes can share data with each other, or 
how to pass parameters to the process when launching it. I will try to cover 
those in another part.
