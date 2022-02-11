Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l=['1',2,3,4]

l[1]
2
l[0]
'1'
l[4]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    l[4]
IndexError: list index out of range
try:
    l[4]
except:
    print('got eror')

    
got eror

#2nd example

try:
    print(1/5)
except:
    print('the denominator is zero')

    
0.2
0.2
0.2
l=[1,2,3,4,6,7,8,8,9,0,7,5,3]

x=100
for num in l:
    print(x/num)

    
100.0
50.0
33.333333333333336
25.0
16.666666666666668
14.285714285714286
12.5
12.5
11.11111111111111
Traceback (most recent call last):
  File "<pyshell#24>", line 2, in <module>
    print(x/num)
ZeroDivisionError: division by zero
