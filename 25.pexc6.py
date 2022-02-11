Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n = [12,32,55,67,3,55,68,22,55,89,55,1,19,32]
>>> n.count(55)
4
>>> n.index(55)
2
>>> n.index(55,4,10)
5
>>> n.index(min(n))
11
>>> n[n.index(max(n))=1000
  
SyntaxError: invalid syntax
>>> n[n.index(max(n))]=1000
>>> n
[12, 32, 55, 67, 3, 55, 68, 22, 55, 1000, 55, 1, 19, 32]
>>> l=sorted(n)[-3:]
>>> l
[67, 68, 1000]
>>> sum(sorted(n))[:5]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    sum(sorted(n))[:5]
TypeError: 'int' object is not subscriptable
>>> sum(sorted(n)[:5])
57
>>> l=[none]*20
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    l=[none]*20
NameError: name 'none' is not defined
>>> l=[None]*20
>>> l
[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
>>> l(range(1000,0,-100)
  l
  
SyntaxError: invalid syntax
>>> 
>>> l(range(1000,0,-100)
  l(range(1000,0,-100)
    l
    
SyntaxError: invalid syntax
>>> l(range(1000,0,-100))
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    l(range(1000,0,-100))
TypeError: 'list' object is not callable
>>> 