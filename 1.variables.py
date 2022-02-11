Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> c=34
>>> a=b=c=c+3
>>> a
37
>>> b
37
>>> c
37
>>> x,y,z=10,1.5,'hello'
>>> x
10
>>> y
1.5
>>> z
'hello'
>>> del b
>>> b
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    b
NameError: name 'b' is not defined
>>> del x,y
>>> x
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> y
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    y
NameError: name 'y' is not defined
>>> 