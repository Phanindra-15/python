Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[1,2,-3,4,-5,6,-7,-8,9]
>>> 
>>> l1=[n*2 for n in l]
>>> l1
[2, 4, -6, 8, -10, 12, -14, -16, 18]
>>> l1=[n*2 for n in l if n>0]
>>> l1
[2, 4, 8, 12, 18]
>>> l1=[n*2 for n in l if n!>0]
SyntaxError: invalid syntax
>>> l1=[n*2 for n in l if n<0]
>>> l1
[-6, -10, -14, -16]
>>> 
>>> evens=[n for n in l if n%2==0]
>>> odds=[n for n in l if n%2!==0]
SyntaxError: invalid syntax
>>> odds=[n for n in l if n%2!=0]
>>> 
>>> evens
[2, 4, 6, -8]
>>> odds
[1, -3, -5, -7, 9]
>>> 
>>> m=['apple','bat','cat','dog','eagle','noon']
>>> 
>>> pal=[for word in l if word==word[::-1] ]
SyntaxError: invalid syntax
>>> pal=[word for word in l if word==word[::-1] ]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    pal=[word for word in l if word==word[::-1] ]
  File "<pyshell#20>", line 1, in <listcomp>
    pal=[word for word in l if word==word[::-1] ]
TypeError: 'int' object is not subscriptable
>>> pal=[word for word in m if word==word[::-1] ]
>>> pal
['noon']
>>> 