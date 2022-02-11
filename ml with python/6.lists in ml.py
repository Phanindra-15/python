Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
[1,2,3,4,5,6]
[1, 2, 3, 4, 5, 6]
# a lisr can hold numbers  , integerrs ,floating point numbers , list inside list can be inserted  and strings
my_list=[1,3,5,6,4,8]
li=['one',2,4.5]
li
['one', 2, 4.5]
len(li)
3
li(2)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    li(2)
TypeError: 'list' object is not callable
li[2]
4.5
#both indexing and slicing takes place in lists

l=[1,2,3,4,5,6,7,8,9,0]
l[3:8]
[4, 5, 6, 7, 8]

l[4:9]
[5, 6, 7, 8, 9]
l[:5]
[1, 2, 3, 4, 5]
l[3:]
[4, 5, 6, 7, 8, 9, 0]
l[:-1]
[1, 2, 3, 4, 5, 6, 7, 8, 9]
l[::2]
[1, 3, 5, 7, 9]
l[:::3]
SyntaxError: invalid syntax
l[::3]
[1, 4, 7, 0]


#list also follows string concatenation as strng follows

l+li
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'one', 2, 4.5]
l+2
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    l+2
TypeError: can only concatenate list (not "int") to list
l+['2']
[1, 2, 3, 4, 5, 6, 7, 8, 9, 0, '2']
