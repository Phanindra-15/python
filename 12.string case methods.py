Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s="hello life is a journey... not a race"
>>> s.upper()
'HELLO LIFE IS A JOURNEY... NOT A RACE'
>>> s
'hello life is a journey... not a race'
>>> s=s.upper()
>>> s
'HELLO LIFE IS A JOURNEY... NOT A RACE'
>>> s.capitalize()
'Hello life is a journey... not a race'
>>> s
'HELLO LIFE IS A JOURNEY... NOT A RACE'
>>> s.isupper()
True
>>> s.isnumeric()
False
>>> s.ljust(40)
'HELLO LIFE IS A JOURNEY... NOT A RACE   '
>>> s.rjust(40)
'   HELLO LIFE IS A JOURNEY... NOT A RACE'
>>> s.centerjust(100)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s.centerjust(100)
AttributeError: 'str' object has no attribute 'centerjust'
>>> s.center(100)
'                               HELLO LIFE IS A JOURNEY... NOT A RACE                                '
>>> s.lstrip()
'HELLO LIFE IS A JOURNEY... NOT A RACE'
>>> 