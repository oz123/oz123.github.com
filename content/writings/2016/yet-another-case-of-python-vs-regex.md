---
title: Yet another case of Python vs. Regular Expressions
author: Oz Nahum Tiram
published: 2016-03-26
tags: Python
public: yes
kind: writing
chronological: yes
summary: Regular Expressions are really awesome, and If you read the last post you might got the wrong impression I am totally against their use. I love using regular expressions, but sometimes, knowing Python is more than enough.
---

Regular Expressions are really awesome, and If you read the last post you might
got the wrong impression I am totally against their use. I love using regular
expressions, but sometimes, knowing Python is more than enough.

Here are two more examples where the use of regular expressions was asked in
stackoverflow, and where while regular expressions worked, there was also a very
elegant solution with just using Python.

The first case is matching e-mails. The problem at hand is matching emails only
in a file containing emails with the "display name", e.g. `Joe Example <joe@example.com>`.
The first name and last name are not interesting for us, matching the list of
emails can be done with a regex in the following way:

```python

In [11]: emails_with_names = ["Joe example <joe@example.com>",
                              "max mustermann <max.mustermann@web.de>",
															"Anni User <anni@user.com>"]

In [12]: l=','.join(emails_with_names)

In [42]: rgx = re.compile("\w+@\w+\.\w+")

In [49]: [f.group() for f in map(rgx.search, emails_with_names)]
Out[49]: ['joe@example.com', 'mustermann@web.de', 'anni@user.com']

# better:
In [52]: re.findall(rgx, l)
Out[52]: ['joe@example.com', 'mustermann@web.de', 'anni@user.com']
```

This works like a charm, and as a side note, watch out for `re.match`. This function
is available too, and way to often it will trip you! Because the name is misleading.
Match, as you would expect does the matching, so you will try that before using
`re.search` and wonder why your regular expression is not working or only partially
working. Here is why:


> *re.match(pattern, string, flags=0)*
>
> If zero or more characters at the beginning of string match the regular
> expression pattern, return a corresponding MatchObject instance.
> Return None if the string does not match the pattern; note that this is
> different from a zero-length match.
> Note that even in MULTILINE mode, re.match() will only match at the beginning
> of the string and not at the beginning of each line.
> If you want to locate a match anywhere in string, use search() instead
> (see also search() vs. match()).

So you most likely want to use `re.search` and if you want the match the head
of a string just stick a `^` to your regex beginning or really use `re.match`.

So how can the exercise above be done without regular expressions? The answer is
`string.index` and slicing of strings:

We can find the index of `<` and `>` enclosing the email, and use this indecies
to extract the emails:

```python
In [55]: def extract_mail(str):
             try:
  	             return str[str.index('<'):str.index('>')+1]
	           except ValueError: #  substring not found
		             return ''

In [60]: emails_with_names = ["Joe example <joe@example.com>", "max mustermann <max.mustermann@web.de>", "Anni User <anni@user.com>"]
In [61]: map(extract_mail, emails_with_names)
Out[61]: ['<joe@example.com>', '<max.mustermann@web.de>', '<anni@user.com>']
```

So this works also with pure Python, and demonstrates again that Python has really
good built-in text processing capabilities. And now for another example.
The task at hand is matching capitalized words in a string.
Using regular expressions we could check for `[A-Z]\w+`:

```
In [69]: re.findall('[A-Z]\w+', "Elephant in the Zoo")
Out[69]: ['Elephant', 'Zoo']
```

But this fails miserably for non ASCII stuff (in the current built in re module of
python (2.7 to 3.5):

```
In [70]: re.findall('[A-Z]\w+', "Älephant in the Üöö")
Out[70]: []
```

There [future plans to fix Python's handling of unicode inside re][1] and you
could somehow fix the situation in the following way:

```
In [72]: re.findall('[A-ZÜÖÄ]\w+', "Älephant in the Üöö", re.UNICODE)
Out[72]: ['\x84lephant', '\x9c\xc3']
```

But note that I added here only 3 German umlauts and you'll probably want to account
for many more other Unicode capital letters. So here is a fix without regular expressions:

```python
>>> [word for word in "Älephant in the Üöö".split() if word[0].isupper()]
['Älephant', 'Üöö']
```

Note however, that if your are using Python 2 (hopefully, you are not...) it
will fail:

```
$ python
Python 2.7.11 (default, Feb 10 2016, 07:38:46)
[GCC 4.9.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> [word for word in "Älephant in the Üöö".split() if word[0].isupper()]
[]
>>>
```

In Python 2 you can have use `frozenset` to solve the problem without regular
expressions:

```
>>> s = "Älephant in the Üöö"
>>> l = s.split()
>>> frozenset(l).intersection(s.capitalize() for s in l)
frozenset(['\xc3\x84lephant', '\xc3\x9c\xc3\xb6\xc3\xb6'])
```

Another alternative is to mark your string as unicode literals or use
a future import:

```
$ python
Python 2.7.11 (default, Feb 10 2016, 07:38:46)
[GCC 4.9.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from __future__ import unicode_literals
>>> 'Üdo'[0].isupper()
True

$ python
Python 2.7.11 (default, Feb 10 2016, 07:38:46)
[GCC 4.9.3] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> 'Üdo'[0].isupper()
False
>>> u'Üdo'[0].isupper()
True
```

So with that, you see there is need to rush and always use regular expressions
when programming with Python. Sometimes, there unavoidable, but in many years
I program with Python, I have rarely seen such cases. Let me finish with a
very smart and funny quote:

> Some people, when confronted with a problem, think ‘I know, I’ll use regular expressions.’
> Now they have two problems.
>
> *Jamie Zawinski*


Credits for this post:

[Python regex for unicode capitalized words][2]

[1]: https://pypi.python.org/pypi/regex
[2]: http://stackoverflow.com/questions/36187349/python-regex-for-unicode-capitalized-words
