Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> t1=(1,2,3,4)
>>> t2=6,7,8
>>> t1
(1, 2, 3, 4)
>>> t2
(6, 7, 8)
>>> t1+t2
(1, 2, 3, 4, 6, 7, 8)
>>> t2*5
(6, 7, 8, 6, 7, 8, 6, 7, 8, 6, 7, 8, 6, 7, 8)
>>> t3=(9,)
>>> t4(9)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    t4(9)
NameError: name 't4' is not defined
>>> type(t3)
<class 'tuple'>
>>> type(t4)
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    type(t4)
NameError: name 't4' is not defined
>>> t4=(9)
>>> type(t4)
<class 'int'>
>>> l=[1,2,3,4,5,6,7,8,9]
>>> t=tuple(l)
>>> t
(1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> t[2]
3
>>> t[-1]
9
>>> t[::-1]
(9, 8, 7, 6, 5, 4, 3, 2, 1)
>>> 