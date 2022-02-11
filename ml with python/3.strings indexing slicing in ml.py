Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
'hello'
'hello'
'phani'
'phani'
len('hello')
5
len('phani')
5
#strings in python

# we should use single quotes and doble quotes based on the condtion of   the nams we are giving
" i don't know"
" i don't know"
'i dont"know'
'i dont"know'
s1=asd
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    s1=asd
NameError: name 'asd' is not defined
s1='add'
s2='sub'
s1+s2
'addsub'
#indexing and slicing
#indexing

#getting individual element is called indexing

#indexing  in python is always start with zero
s='hello
SyntaxError: unterminated string literal (detected at line 1)
s='hello'
s[0]
'h'
s[1]
'e'
s[2]
'l'
#negative indexing
s[-1]
'o'
s[-2]
'l'
s='he llo'
len(s)
6
s[3]
'l'
s[2]
' '
#slicing

#getting a piece of something is called slicing
s='i like this movie very much'
s[2:5]
'lik'
s[6:14]
' this mo'
s[-5:-2]
' mu'
s[6:]
' this movie very much'
s[1:5:2]
' i'
s[2:10:3]
'leh'
s1='abcdefghijk'
s1[2:10:3]
'cfi'
s1[2:10:2]
'cegi'
