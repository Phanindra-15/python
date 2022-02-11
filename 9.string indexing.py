Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s1=hi phanindra
SyntaxError: invalid syntax
>>> s1=
SyntaxError: invalid syntax
>>> s1="hi phanindra"
>>> s2="hello sumanth"
>>> s1
'hi phanindra'
>>> s2
'hello sumanth'
>>> len(s1)
12
>>> len(s2)
13
>>> s1[3]
'p'
>>> s2[1]
'e'
>>> s2[-1]
'h'
>>> s2[len(s)-1]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s2[len(s)-1]
NameError: name 's' is not defined
>>> s2[len(s2)-1]
'h'
>>> 