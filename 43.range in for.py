Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> for i in range(5):
	print(i*i,end=' ')

	
0 1 4 9 16 
>>> for i in range(10):
	print(i*i,end=' ')

	
0 1 4 9 16 25 36 49 64 81 
>>> for i in range(3,10):
	print(i*i,end=' ')

	
9 16 25 36 49 64 81 
>>> for i in range(3,10,2)
SyntaxError: invalid syntax
>>> for i in range(3,10,2):
	print(i*i,end=' ')

	
9 25 49 81 
>>> total=0
>>> for i in range(5,21):
	total=total+i

	
>>> total
200
>>> for i in range(1,5)
SyntaxError: invalid syntax
>>> for i in range(1,5):
	print('*' *i)

	
*
**
***
****
>>> for i in range(5,10):
	print('*' *i)

	
*****
******
*******
********
*********
>>> n=int(input('enter a number:'))
enter a number: