Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> n = [1,2,3,4,5,6,7,8]
>>> n.append(100)
>>> n
[1, 2, 3, 4, 5, 6, 7, 8, 100]
>>> n.insert(0,200)
>>> n
[200, 1, 2, 3, 4, 5, 6, 7, 8, 100]
>>> n.insert(3,150)
>>> n
[200, 1, 2, 150, 3, 4, 5, 6, 7, 8, 100]
>>> n.insert(23,23)
>>> n
[200, 1, 2, 150, 3, 4, 5, 6, 7, 8, 100, 23]
>>> n.extend([12,13,14,15])
>>> n
[200, 1, 2, 150, 3, 4, 5, 6, 7, 8, 100, 23, 12, 13, 14, 15]
>>> n.remove(5)
>>> n
[200, 1, 2, 150, 3, 4, 6, 7, 8, 100, 23, 12, 13, 14, 15]
>>> n.pop()
15
>>> n.pop()
14
>>> n.pop()
13
>>> n.pop()
12
>>> n.clear()
>>> n
[]
>>> del listA[5]
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    del listA[5]
NameError: name 'listA' is not defined
>>> 