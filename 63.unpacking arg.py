Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> def result(m1,m2,m3,m4):
	total+m1+m2+m3+m4
	per=total/4
	print(f'total marka={total},percentage={per}%')
	print('pass' if per>40 else 'fail')

	
>>> result(23,56,78,98)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    result(23,56,78,98)
  File "<pyshell#6>", line 2, in result
    total+m1+m2+m3+m4
NameError: name 'total' is not defined
>>> def result(m1,m2,m3,m4):
	total=m1+m2+m3+m4
	per=total/4
	print(f'total marks={total},percentage={per}%')
	print('pass' if per>40 else 'fail')

	
>>> result
<function result at 0x000001207945B310>
>>> result(23,45,78,98)
total marks=244,percentage=61.0%
pass
>>> result(12,11,10,21)
total marks=54,percentage=13.5%
fail
>>> 
>>> marks=[95,78,86,76]
>>> 
>>> result(marks[0],marks[1],marks[2],marks[3])
total marks=335,percentage=83.75%
pass
>>> 
>>> marks=[5,8,6,6]
>>> 
>>> result(marks[0],marks[1],marks[2],marks[3])
total marks=25,percentage=6.25%
fail
>>> result(*marks)
total marks=25,percentage=6.25%
fail
>>> mark=[23,56,7,75,78]
>>> 
>>> print(marks)
[5, 8, 6, 6]
>>> print(mark)
[23, 56, 7, 75, 78]
>>> print(*mark)
23 56 7 75 78
>>> print(*marks)
5 8 6 6
>>> 