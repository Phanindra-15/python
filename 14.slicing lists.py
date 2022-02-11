Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> numbers=[10,20,30,40,50,60,70,80,90]
>>> type(numbers)
<class 'list'>
>>> numbers[3]
40
>>> numbers[-2]
80
>>> numbers[20]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    numbers[20]
IndexError: list index out of range
>>> numbers[4]=55
>>> numbers
[10, 20, 30, 40, 55, 60, 70, 80, 90]
>>> numbers[2:6]
[30, 40, 55, 60]
>>> numberss[:6]
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    numberss[:6]
NameError: name 'numberss' is not defined
>>> numbers[:6]
[10, 20, 30, 40, 55, 60]
>>> numbers[2:]
[30, 40, 55, 60, 70, 80, 90]
>>> numbeers[:]
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    numbeers[:]
NameError: name 'numbeers' is not defined
>>> numbers[:]
[10, 20, 30, 40, 55, 60, 70, 80, 90]
>>> n=numbers[:]
>>> n
[10, 20, 30, 40, 55, 60, 70, 80, 90]
>>> numbers[::-1]
[90, 80, 70, 60, 55, 40, 30, 20, 10]
>>> 