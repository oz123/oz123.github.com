---
title: Git tip - Count commits between tags 
author: Oz Nahum
published: 2013-09-10
tags: git, Programming, pwman3
public: yes
chronological : yes
kind: writing 
summary: Once every N commits I would like to release a new version of pwman3, so here is how to keep a track of this number between releases ...
---

Not much in this post, just a reminder how to track changes:

```bash
[25] oz123@debian:~/pwman3  [master]  $ git rev-list HEAD --count
227
...
[38] oz123@debian:~/pwman3  [master]  $ echo `git rev-list HEAD --count` - \
                                                      `git rev-list v0.3.9d \
                                                      --count` | bc 
31
```

That was a quick post.
