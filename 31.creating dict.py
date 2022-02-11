Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[['x',4],['y',5],['z',6]]
>>> d=dict(l)
>>> d
{'x': 4, 'y': 5, 'z': 6}
>>> country=['france','austria','japan','india']
>>> capitals=['paris','vienna','tokyo','delhi']
>>> d=dict(zip(country,cpitals))
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    d=dict(zip(country,cpitals))
NameError: name 'cpitals' is not defined
>>>  d=dict(zip(country,capitals))
 
SyntaxError: unexpected indent
>>> 
>>> d=dict(zip(country,capitals))
>>> d
{'france': 'paris', 'austria': 'vienna', 'japan': 'tokyo', 'india': 'delhi'}
>>> ll=[['apple',100],['mango',200]]
>>> 
>>> tl=(['apple',100],['mango',200])
>>> 
>>> tt=(('apple',100),('mango',200))
>>> 
>>> ls=[('apple',100),('mango',200)]
>>> 
>>> dict(ll)
{'apple': 100, 'mango': 200}
>>> dict(lt)
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    dict(lt)
NameError: name 'lt' is not defined
>>> dict(tl)
{'apple': 100, 'mango': 200}
>>> dict(tt)
{'apple': 100, 'mango': 200}
>>> dict(ls)
{'apple': 100, 'mango': 200}
>>> items=['a','b','c','d','e','f']
>>> dict.frpmkeys(items,0)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    dict.frpmkeys(items,0)
AttributeError: type object 'dict' has no attribute 'frpmkeys'
>>> dict.fromkeys(items,0)
{'a': 0, 'b': 0, 'c': 0, 'd': 0, 'e': 0, 'f': 0}
>>> dict.fromkeys(items,5)
{'a': 5, 'b': 5, 'c': 5, 'd': 5, 'e': 5, 'f': 5}
>>> dict.fromkeys(items)
{'a': None, 'b': None, 'c': None, 'd': None, 'e': None, 'f': None}
>>> dict.fromkeys(range(7))
{0: None, 1: None, 2: None, 3: None, 4: None, 5: None, 6: None}
>>> 
>>> price1=['a':100,'m':200]
SyntaxError: invalid syntax
>>> price1=('a':100,'m':200)
SyntaxError: invalid syntax
>>> price1={'a':100,'m':200}
>>> price2={'g',300,'b',400}
>>> price1.update(price2)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    price1.update(price2)
TypeError: cannot convert dictionary update sequence element #0 to a sequence
>>> 