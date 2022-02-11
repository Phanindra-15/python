Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

#list methods

l=[1,2,3,4]
l.append(5)
l
[1, 2, 3, 4, 5]
#1.append is used to add some thing to the existing list
#count methos is used to count the number is represtng how many times

=[1,2,3,1,2,3,1,2,3,4,5]
SyntaxError: invalid syntax
l=[1,2,3,1,2,3,1,2,3,4,5]
l.count(1)
3
l.pop()
5
l
[1, 2, 3, 1, 2, 3, 1, 2, 3, 4]
l
[1, 2, 3, 1, 2, 3, 1, 2, 3, 4]
#remove is used to remove the elements by its value  where pop remains the element by index
l.remove(5)
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    l.remove(5)
ValueError: list.remove(x): x not in list
l.remove(4)
l
[1, 2, 3, 1, 2, 3, 1, 2, 3]
l.remove(1)
l
[2, 3, 1, 2, 3, 1, 2, 3]
l.pop()
3
l
[2, 3, 1, 2, 3, 1, 2]
