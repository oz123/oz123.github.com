---
title: coverage reporting and logging without a webservice
author: Oz Nahum Tiram
published: 2017-02-28
tags: python, testing, git
public: yes
chronological: yes
kind: writing
summary: Type your summary here.
---

For quite a while now I wanted to have a cheap replacement for collecting
and tracking coverage of codes I work on. Unfortunately, there is no quick
solution I know of which does more or less what coveralls.io do.
There is probably a Jenkins plugin to do it, or some heavy weight solution
which needs a webservice, a database and maintenance.

Alas, we always lack time, and git offers teams a place to keep the history,
so why not use it to track the coverage reporting?

Enter `git commit --amend` and some `Makefile` trickery. You can use git own
powers to amend the last commit and add to the bottom of it the coverage report.

I do it with `make coverage-record`. This runs the tests, and saves the report
in the body of the latest commit message.

You can add the following target to your project make file. If you feel more
courageous, you can add this to your `pre-push` hook. This will have a nice
bonus, which will by default, prevent people pushing broken builds (e.g. failing
tests):

```
coverage-record: TMPFILE := $(shell mktemp)
coverage-record: coverage
	git show -s --format=%B HEAD > $(TMPFILE)
	coverage report >> $(TMPFILE)
	git commit --amend -F $(TMPFILE)
	rm $(TMPFILE)
```

Note that this target depends on `coverage`, which is your how you invoke your
test suite, for example:

```
coverage-run:
	py.test -vv --cov=blogit tests
```

To use this target in the `pre-push` hook, you will slightly have to change
the Makefile syntax to shell syntax.

I would be happy to know of other solutions how you track the test coverage
of your software projects!
