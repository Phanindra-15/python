Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>>  def result(*args):
	total=sum(args)
	per=total/len(args)
	print(args)
	print(f'total marka={total},percentage={per}%')
	print('pass' if per>40 else 'fail')


SyntaxError: unexpected indent
>>> def result(*args):
	total=sum(args)
	per=total/len(args)
	print(args)
	print(f'total marka={total},percentage={per}%')
	print('pass' if per>40 else 'fail')

	
>>> result(45,56,6,77,88,76)
(45, 56, 6, 77, 88, 76)
total marka=348,percentage=58.0%
pass
>>>  result(45,56,6,77)
 
SyntaxError: unexpected indent
>>> result(45,77,88,76)
(45, 77, 88, 76)
total marka=286,percentage=71.5%
pass
>>> result(45,56,6,77,88,76,4,22,44)
(45, 56, 6, 77, 88, 76, 4, 22, 44)
total marka=418,percentage=46.44444444444444%
pass
>>> resilt(34)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    resilt(34)
NameError: name 'resilt' is not defined
>>> result(56)
(56,)
total marka=56,percentage=56.0%
pass
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> def average(*args):
	return sum(args)/len(args)

>>> average(9,2,1)
4.0
>>> average(9,5,3,6,3,36,7,31,6)
11.777777777777779
>>> l=[1,4,3,6,7,48,8]
>>> average(*l)
11.0
>>> l=[1,4,3,6,7,48,8,11,22,33,44,5,5,65,6]
>>> average(*l)
17.866666666666667
>>> 
>>> d=['john':23,'phani':21,'hemanth':19)
SyntaxError: invalid syntax
>>> d=('john':23,'phani':21,'hemanth':19)
SyntaxError: invalid syntax
>>> d={'john':23,'phani':21,'hemanth':19}
>>> 
>>> 
>>> average(*d.values())
21.0
>>> 