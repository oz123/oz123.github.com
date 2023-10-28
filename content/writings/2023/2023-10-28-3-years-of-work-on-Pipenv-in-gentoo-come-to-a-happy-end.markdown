---
title: 3 years of work on Pipenv in Gentoo come to a happy end
author: Oz Tiram
published: 2023-10-28
tags: Python,Gentoo,FOSS
public: yes
chronological: yes
kind: writing
summary: >
  3 years and 3 months ago, I signed up for maintaining Pipenv in Gentoo. This work made me co-maintainer
  of pipenv. I finally closed a long standing bug in Gentoo's pipenv. Due to this work, pipenv now ships
  less vendored packages, and is about 20% smaller in size.
---

3 years and 3 months ago, I signed up for maintaining [Gentoo's pipenv ebuild][1].
I thought it would be a fun way to learn about Python in Gentoo. I already knew that
pipenv has issues. Also, I knew that the project was a bit dormant, due to the departure
of Keneth Reitz, who was the original developer. And despite that I took on the commitment
to work on that ebuild.

Gentoo's maintainers didn't like the fact that Pipenv bundles tons of Python packages in
its vendor directory. Arguably, a security issue. Hence, bug [717666 - dev-python/pipenv:
bundles humongous number of packages][2] was opened.
I also think that even though disk space is cheap it's a waste of resources. It seems like
a nice project to work on. And what started as fixes for the ebuild, to "unvendor" those
packages, turned into skepticism. 

Are those packages even used? It seemed that many of those python packages where old and
unused. Specifically, [vistir][3] seemed like a grab-bag of hacks to support multiple
platforms and Python versions. But many of those had already better fixes in upstream
packages or the standard library.

Eager to fix those issues, I started looking for good opportunity to fix issues directly
in Pipenv. And then in June 2023, I saw that Frost Ming, the maintainer of Pipenv, [is looking
for help][4]. 

And so, together with [Matt Davis][5] I took over the project. My first goal, was to find
a way to unvendor all those packages. This required a lot of refactoring and patches
to requirementslib and vistir and few other packages that pipenv consumes.
Eventually, we fixed many issues in vistir but ended up dropping it because it was no longer
needed. Matt has done a tremendous job fixing requirementslib, until it was no longer possible,
and he ended up internalizing many parts, and rewritting huge amounts of code.
I continued to incrementally find stuff in the vendor library that was not needed due to fixes
in the standard library. An obvious example, pipenv was still shipping six even though it only
supported Python3 versions. Another example, we shipped `orderedmultidict`. Python has had ordered
dictionaries for quite a while, so it was a bit of a red flag.
We found out that we can safely remove this library in favour of using regular dictionaries,
thus removing hundreds line of code immediately.
Many other vendored libraries where dropped, and in some cases we turned to use vendored libraries
that are found inside pip's own vendor directory, thus reducing duplication. 

In parallel, I kept bumping versions of pipenv in Gentoo, incrementally removing more packages,
from the vendor in favor of adding dependencies to other ebuilds. A few times, I tried removing
all the packages all at once, but failed. Finally, I did the unpreventable and started creating
ebuilds to packages that didn't have any ebuilds in Gentoo. I did not yet upstream them, just
to keep experimenting with Python ebuilds.

This September, I finally decided to give this issue a final blow, and it's now closed.
The Gentoo version no longer bundles packages in vendor!
My work on this issue, has also a positive impact on pipenv for all other users.
This is because recent version of pipenv no longer ship many packages in vendor.
Pipenv release 2023.10.20 has only [16][7] vendored libraries, compared to 59 in [2020.8.13][6].

Finally, despite almost 20% reduction in size, pipenv is still a huge program.
The wheel size of version 2020.8.13 is [3.9MB][8], while the wheel size of version
2023.10.20 is only [3.2MB][9]. I was hopping for more, but the work is still not done.
Future versions of pipenv will continue receiving bug fixes, along with speed improvements
and size reduction.

If you use pipenv, please consider sponsoring our work via Github sponsors.

[1]: https://github.com/gentoo/gentoo/commit/47eb7e89e86d9bfc3575c865a8254e91ad1a4132
[2]: https://bugs.gentoo.org/717666
[3]: https://github.com/sarugaku/vistir
[4]: https://github.com/pypa/pipenv/issues/4894#issuecomment-1008289265
[5]: https://github.com/matteius
[6]: https://github.com/pypa/pipenv/blob/9299ae1f7353bdd523a1829f3c7cad0ee67c2e3b/pipenv/vendor/vendor.txt
[7]: https://github.com/pypa/pipenv/blob/fd4147bd7e69620ef257ea57c0b67eaa80d01ab7/pipenv/vendor/vendor.txt
[8]: https://pypi.org/project/pipenv/2020.8.13/#files
[9]: https://pypi.org/project/pipenv/2023.10.24/#files
