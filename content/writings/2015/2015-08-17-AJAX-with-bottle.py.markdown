---
title: AJAX with bottle.py
author: Oz Nahum Tiram
published: 2015-08-17
tags: python, web, JQuery
public: yes
chronological: yes
kind: writing
summary: A working example of AJAX with JQuery and Bottle 
---

Without much further ado, here is how to create a webpage with AJAX, JQuery and
Bottle.py. 

Here is the web application:

```python
from bottle import route, run, debug, template, request
import json


@route('/_add_numbers')
def add_numbers():
    """Add two numbers server side, ridiculous but well..."""
    a = request.params.get('a', 0, type=int)
    b = request.params.get('b', 0, type=int)
    return json.dumps({'result': a+b})


@route('/')
def index():
    return template('index.tpl', request=request)


debug(True)
run(port=9030)
```

And this is the template:

```html
<!doctype html>
<title>jQuery Example</title>
<script type="text/javascript"
  src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.2/jquery.min.js"></script>
<script type="text/javascript">
  var $SCRIPT_ROOT = "{{ request.script_name }}";
</script>

<script type="text/javascript">
  $(function() {
    var submit_form = function(e) {
      $.getJSON($SCRIPT_ROOT + '_add_numbers', {
        a: $('input[name="a"]').val(),
        b: $('input[name="b"]').val()
      }, function(data) {
        $('#result').text(data.result);
        $('input[name=a]').focus().select();
      });
      return false;
    };

    $('a#calculate').bind('click', submit_form);

    $('input[type=text]').bind('keydown', function(e) {
      if (e.keyCode == 13) {
        submit_form(e);
      }
    });

    $('input[name=a]').focus();
  });
</script>
<h1>jQuery Example</h1>
<p>
  <input type="text" size="5" name="a"> +
  <input type="text" size="5" name="b"> =
  <span id="result">?</span>
<p><a href=# id="calculate">calculate server side</a>
</body>
</html>
```

The code is based on the original example given inside Flask sources by Armin Ronacher.
You can download both files directy from here: [ajax_bottle.py][1], [index.tpl][2].

[1]: http://oz123.github.io/media/uploads/ajax_bottle_files/ajax_bottle.py
[2]: http://oz123.github.io/media/uploads/ajax_bottle_files/index.tpl
