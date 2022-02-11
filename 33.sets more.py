Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> s1={'a','b','c','x','y','z'}
>>> s2={'x','y','z','a','b','c','d'}
>>> s3={'x','y','z','a','b','c'}
>>> 
>>> s1==s3
True
>>> s1 is s2
False
>>> s3 is s1
False
>>> s1.issubset(s2)
True
>>> s1.issubset(s3)
True
>>> s1<s3
False
>>> s1,=s3
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    s1,=s3
ValueError: too many values to unpack (expected 1)
>>> s1<=s3
True
>>> s3>s1
False
>>> s3>=s1
True
>>> s3.isiuperset(s1)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    s3.isiuperset(s1)
AttributeError: 'set' object has no attribute 'isiuperset'
>>> s3.issuperset(s1)
True
>>> s4={1,2,3,4}
>>> s1.isdisjoint(s2)
False
>>> s4.isdisjoint(s2)
True
>>> pp={'a','b','c','d','e'}
>>> jp={'f','g','h','i','j'}
>>> cp={'k','l','m','n','o'}
>>> 
>>> pp.intersection(jp)
set()
>>> pp={'a','b','c','d','e'}
>>>  jp={'f','b','h','d','j'}
 
SyntaxError: unexpected indent
>>> pp={'a','b','c','d','e'}
>>> jp={'f','b','h','d','j'}
>>> cp={'k','f','h','d','o'}
>>> pp.intersection(jp)
{'b', 'd'}
>>> pp.intersection(cp)
{'d'}
>>> pp&jp&cp
{'d'}
>>> cp.union(pp)
{'e', 'b', 'f', 'o', 'c', 'k', 'a', 'd', 'h'}
>>> cp |pp
{'e', 'b', 'f', 'o', 'c', 'k', 'a', 'd', 'h'}
>>> pp-jp
{'c', 'e', 'a'}
>>> pp-cp
{'c', 'e', 'b', 'a'}
>>> jp-cp
{'b', 'j'}
>>> pp.difference(jp)
{'c', 'e', 'a'}
>>> pp.symmetric_difference(jp)
{'c', 'e', 'j', 'a', 'f', 'h'}
>>> 