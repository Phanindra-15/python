Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s='madam'
>>> if s==s[::-1]:
	print(s,'is a palindrome')

	
madam is a palindrome
>>> s='ieep'
>>> if s==s[::-1]:
	print(s,'is a palindrome')

	
>>> s='radar'
>>> if s==s[::-1]:
	print(s,'is a palindrome')

	
radar is a palindrome
>>> 
>>> s='minnim'
>>> if s==s[::-1]:
	print(s,'is a palindrome')if s==s[::-1]:
		print(s,'is a palindrome')
		
SyntaxError: invalid syntax
>>> s='minnim'
>>>  if s==s[::-1]:
	print(s,'is a palindrome')
	
SyntaxError: unexpected indent
>>> if s==s[::-1]:
	print(s,'is a palindrome')

	
minnim is a palindrome
>>> 