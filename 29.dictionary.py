
Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> price={'pencil':10,
       'pen':20,
       'scale':24,
       'eraser':5
       }
>>> s={'name':'phani',
        'age':21,
       'gender':'M'
       'marks':[34,45,56]
   
SyntaxError: invalid syntax
>>> s={'name':'phani',
        'age':21,
       'gender':'M'
       'marks':[34,45,56]}
SyntaxError: invalid syntax
>>> s={'name':'phani',
        'age':21,
       'gender':'M',
       'marks':[34,45,56]}
>>> s
{'name': 'phani', 'age': 21, 'gender': 'M', 'marks': [34, 45, 56]}
>>> price
{'pencil': 10, 'pen': 20, 'scale': 24, 'eraser': 5}
>>> s('name')
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    s('name')
TypeError: 'dict' object is not callable
>>> s['name']
'phani'
>>> s['marks'][0]
34
>>> price['pen']
20
>>> price['pen']=45
>>> price
{'pencil': 10, 'pen': 45, 'scale': 24, 'eraser': 5}
>>> len(price)
4
>>> 'age' in s
True
>>> 'age' in price
False
>>> 'grade' not in s
True
>>> 
