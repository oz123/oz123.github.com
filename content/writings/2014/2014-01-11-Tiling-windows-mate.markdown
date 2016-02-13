---
title: Quick Tip - Tiling Windows manager in Mate-Desktop 
author: Oz Nahum
published: 2014-01-11
tags: Linux, Mate-Desktop
public: yes
chronological : yes
kind: writing 
summary: |
summary: Environment such as Mate-Desktop using x-tile
---

X-Tile is a Desktop Environment agnostic program written in Python which reorganises your open
Windows in different aragenments like DWM or other [Tiling Windows Manager][wiki]. It's advantage is
that you can enjoy all the benefits of using your familiar Desktop, plus you get keyboard 
shortcuts to quickly rearage your windows around. [X-Tile][xtile] is found in the Debian repositoris so 
you can quickly install it with:

```bash
 $ aptitude install x-tile
```
Now, you can quickly add keyboard shortcuts running the following script:
    
```bash
#!/bin/bash
# x-tile_mate_keybindings 
# quickly setup bindings for x-tile in mate, tiling window
# management with a nice DE!

# Thanks for mate developers  Issue #45 in mate-control-center
# is now closed and this is possible again

# this script assumes you have dconf-cli installed
cat << EOF > keys
[custom6]
action='x-tile q'
binding='<Primary><Alt>q'
name='tile quad'

[custom2]
action='x-tile v'
binding='<Alt><Mod4>k'
name='tile vertical'

[custom5]
action='x-tile l'
binding='<Alt><Mod4>l'
name='tile right'

[custom1]
 action='x-tile z'
binding='<Primary><Alt>z'
name='undo tile'

[custom4]
action='x-tile l'
binding='<Alt><Mod4>h'
name='tile left'

[custom0]
action='x-tile u'
binding='<Primary><Alt>u'
name='tile up'

[custom3]
action='x-tile d'
binding='<Alt><Mod4>j'
name='tile down'

[custom7]
action='x-tile l'
binding='<Alt><Mod4>3'
name='tile right 3'
EOF

dconf load /org/mate/desktop/keybindings/ < keys
rm keys
```
That's all. You can download this script [here][script].

[xtile]: http://www.giuspen.com/x-tile/
[wiki]: http://en.wikipedia.org/wiki/Tiling_window_manager
[script]: https://raw.github.com/oz123/dude/master/config_files/x-tile_mate_keybindings
