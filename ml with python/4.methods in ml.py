Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#methods in string

s='hello world'
s.capitalize()
'Hello world'
s.upper
<built-in method upper of str object at 0x000001D4EB9C8330>
s=s.upper()
s
'HELLO WORLD'
s.upper()
'HELLO WORLD'
s.lower()
'hello world'
#we cant change values in the string but we can replace values in rhe string
s.split()
['HELLO', 'WORLD']
s1='this is my fab movie whcih i seen in my entore life upto now '
s1.split()
['this', 'is', 'my', 'fab', 'movie', 'whcih', 'i', 'seen', 'in', 'my', 'entore', 'life', 'upto', 'now']
s1.split("e")
['this is my fab movi', ' whcih i s', '', 'n in my ', 'ntor', ' lif', ' upto now ']
