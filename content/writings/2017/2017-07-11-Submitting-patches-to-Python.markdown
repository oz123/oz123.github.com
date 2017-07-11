---
title: Submitting patches to Python
author: Oz Nahum Tiram
published: 2017-07-11
tags: Python, news
public: yes
chronological: yes
kind: writing
summary: >
	This is not my typical blog post style. So no "how to" or opinnions. Just
	some reflections on how I submitted a patch to Python's standard library.
---

I managed to submit a code to Python's standard library!
If you asked me a year earlier I would not believe it. So how did it all happen?
First, technically speaking, it's become way more easy since now Python in on Github!
And I have submitted numeros (some significant and less significant) patches and
PRs and issue to small projects, famous examples are Bottle.py, lektor) and
larger ones (such as Django, Kubernetes and SaltSatck, Gentoo and Alpine Linux).
Technically speaking, it just the same process.

For some reasone, Python seemed like a harder task. Working on a pull request
seemed like beyond what I can and should spend my time on. So I thought.
A Bug report, or a maybe ["Feature Request" for having a better Python HTML Calendar][1]
I submitted, got some positive feedback. So I thought, why not submit a PR?

Python has always been a great community, this case was no different.
I got a really [patient mentor][2] and after reviewing two slightly different
branches implemeting my ideas we chose a strategy to implement the feature.
Than he walked me through many tiny issues, such as making the documentation fit the
style (I worked with Sphinx many times in the past, but the
[Python docs have their own directives and style][3], silly spelling
mistakes, consistant naming and so on. Finally  I added official Changlog entry
and then my name to the contributors list. Walter did everything with
lots of patience, since I could not always respond immidietly. After about 1 month
from my PR submittion and a few revision cycles, the PR was ready! And it was merged.

I think that the bug report before making the PR was a good idea.
Because it was like making a pitch for the idea. Doing this and one might
even find other people intrested in the idea and can help you improve it in ways
never thought of before.

I also have to credit Waltr Dör for not dismissing my PR just because I have done
some things in the wrong way (for example my identation of rst files) just because
I didn't read everything in the Developer manual beforehand. Reading the manual
is usualy a very boring exprience, and honestly speaking I think most people
who just want to contribute a single patch won't spend complete working days 
going through every little aspect of the manual.
Now, that I know what is important I will definitely go back and refer to the
developer manual in my next PR. I promise.

If you want to make your PR accepted more quickly, you should too.
However, there other online communities which will not be as caring an forgiving
as my mentor, and they might completely dismiss a PR just because of such issues
and not because the content of the PR. This will usually turn people off, unless
they are really determined.

I think that being patient with new contributores is a great thing, and I really
think this way better attitude then dismissing people with RTFM.
Therefore, I hope other mentors will embrace this attitude and encourage people
to make a contribution, even if they need some extra effort of polishing it.
I think it is worth it for the community, and I think people who encouter such a
friendly mentor will definitely contribute again. I know I will!

This feels really good to give back to the great Python community! And I no longer
think of it as an impossible thing to do. I hope this tiny report will also encourage
other new comers to contribute ideas via bug reports, improving documentation and
submitting new features.

I'd also like to thank Ewa Jodlowska from the PSF, whom I met in EuroPython 2017,
and which encouraged me to write this short reflection post.


[1]: http://bugs.python.org/issue30095
[2]: https://github.com/doerwalter
[3]: https://docs.python.org/devguide/documenting.html#restructuredtext-primer
