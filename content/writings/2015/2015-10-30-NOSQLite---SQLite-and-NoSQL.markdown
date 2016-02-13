---
title: NoSQLite - SQLite, support for JSON field
author: Oz Nahum Tiram
published: 2015-10-30
tags: NoSQL
public: yes
kind: writing
chronological: yes
summary: Released just recently (14-10-2015) the new SQLite (3.9.*) now has optional support for NoSQL like work flows with the new JSON field type. This is a very brief introduction to the JSON1 extension which enables this support. 
---

Released just recently (14-10-2015) the new SQLite (3.9.x) now has optional
support for NoSQL like work flows with the new JSON field type.
This means that for certain use cases you don't have to choose SQL or NoSQ 
database for storing unstructured data. This is similar now to Postgresql, 
which also has support for BSON and JSON fields. 

Let's see how this works. First, you need to download the latest sources
of SQLite and compile them with JSON support.

```shell

 $ wget https://www.sqlite.org/2015/sqlite-autoconf-3090100.tar.gz
 $ tar xvzf sqlite-autoconf-3090100.tar.gz
 $ cd sqlite-autoconf-3090100.tar.gz
 $ ./configure --enable-json1 --enable-readline 
 $ make
 $ sudo make install
```

Now, the new SQLite binary will be installed to `/usr/local/bin`. 
Let's see how it works:

$ /usr/local/bin/sqlite3 
SQLite version 3.9.1 2015-10-16 17:31:12
Enter ".help" for usage hints.
Connected to a transient in-memory database.
Use ".open FILENAME" to reopen on a persistent database.
sqlite> CREATE TABLE test_table (id	INTEGER,test_field JSON ); 

This will create a table with 2 columns, named `id` and `test_field`. Having
the types of `INTEGER` and `JSON`.

Now, let's put some data in the table:

```sql
sqlite> insert into test_table (id, test_field) values \
        (1, ' { "this" : "is", "a": [ "test" ] } ');
sqlite> select * from test_table;
1| { "this" : "is", "a": [ "test" ] } 
sqlite> 
```

This works. But there is one caveat, there is not constraint for what's in the 
json. I could also put junk there. Here is how:

```sql
sqlite> insert into test_table (id, test_field) values \
        (2, 'junk text');
sqlite> select * from test_table;
1| { "this" : "is", "a": [ "test" ] } 
2|junk text
```

OK, you are not impressed. Neither am I. JSON field is basically a text based field.
To really use a json field we need to wrap our json with a function call that
validates the json. If you are using SQLite within Python, for example, that's 
a very easy thing to do. In addition, SQLite offers it's own function:

```sql
sqlite> insert into test_table (id, test_field) values (1, json('junk text'));
Error: malformed JSON
sqlite> insert into test_table (id, test_field) values (1, json('{"not": "junk"}'));
sqlite> select * from test_table;
1| { "this" : "is", "a": [ "test" ] } 
2|junk text
3|{"not":"junk"}
```

Does this work the other way too ? Can you put JSON in a text field?
Yes you can. But that is expected. The real fun begins when you start extarcting
data from json fields. For that, the extension, still widely unknown for the public,
provides some functions like:

```
json_extract(json,path,...) Extract values or subcomponents from a JSON string.
json_insert(json,path,value,...) Insert values into a JSON string without overwriting existing values.
json_object(label1,value1,...) Construct and return a new JSON object based on the arguments.
json_remove(json,path,...) Remove the specified values from a JSON string.
json_replace(json,path,value,...)  Update existing values within a JSON string.
json_set(json,path,value,...)  Insert or replace values in a JSON string. 
                               Overwrite existing elements or create new entries 
                               in the JSON string for elements that do not previously exist.
```

I am still in the process of learning all those and I'm trying to figure out 
examples for all those.

[Further reading about SQLite's JSON extension][1].

[1]: https://www.sqlite.org/json1.html
