Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> currency={}
>>> currency['India']='Rupee'
>>> currency['UK']='Pound'
>>> currency['Japan']='Yen'
>>> currency['Austria']='Euro'
>>> currency['Bangladesh']='Taka'
>>> 
>>> 
>>> del currency['UK']
>>> c=currency.pop('japan')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    c=currency.pop('japan')
KeyError: 'japan'
>>> c=currency.pop('Japan')
>>> c
'Yen'
>>> currency.pop()
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    currency.pop()
TypeError: pop expected at least 1 argument, got 0
>>> currency.popitem()
('Bangladesh', 'Taka')
>>> currency.popitem()
('Austria', 'Euro')
>>> currency['Switzerland']='swiss franc'
>>> currency
{'India': 'Rupee', 'Switzerland': 'swiss franc'}
>>> currency['India']='Indian rupee'
>>> currency
{'India': 'Indian rupee', 'Switzerland': 'swiss franc'}
>>> currency.keys()
dict_keys(['India', 'Switzerland'])
>>> currency.values()
dict_values(['Indian rupee', 'swiss franc'])
>>> currency.items()
dict_items([('India', 'Indian rupee'), ('Switzerland', 'swiss franc')])
>>> x = fruits_prices.setdefault('apple',0)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    x = fruits_prices.setdefault('apple',0)
NameError: name 'fruits_prices' is not defined
>>> fruits_prices =  { 'apple': 100, 'banana':75, 'mango':80 }
>>>  x = fruits_prices.setdefault('apple',0)
 
SyntaxError: unexpected indent
>>> x = fruits_prices.setdefault('apple',0)
>>> x
100
>>> y = fruits_prices.setdefault('grapes',0)
>>> y
0
>>> names = ['John', 'Sam', 'Marie', 'Anne']
>>> login=dict.fromkeys(names,none)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    login=dict.fromkeys(names,none)
NameError: name 'none' is not defined
>>> login=dict.fromkeys(names,None)
>>> login
{'John': None, 'Sam': None, 'Marie': None, 'Anne': None}
>>> designation = ['programmer', 'manager', 'accountant']
>>> salary = [4000, 5000, 3000]
>>> d=dict(zip(destination,salary))
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    d=dict(zip(destination,salary))
NameError: name 'destination' is not defined
>>> d=dict(zip(designation,salary))
>>> d
{'programmer': 4000, 'manager': 5000, 'accountant': 3000}
>>> python_books = [ 'Learn Python', 'Programming in Python', 'Python in depth']
>>> cplusplus_books = ['C++ in depth', 'C++ Programming']
>>> java_books = ['Java Programming', 'Learn Java']
>>>  books = { 'python':python_books, 'c++':cplusplus_books, 'java':java_books }
 
SyntaxError: unexpected indent
>>> books = { 'python':python_books, 'c++':cplusplus_books, 'java':java_books }
>>> books
{'python': ['Learn Python', 'Programming in Python', 'Python in depth'], 'c++': ['C++ in depth', 'C++ Programming'], 'java': ['Java Programming', 'Learn Java']}
>>> books['python']
['Learn Python', 'Programming in Python', 'Python in depth']
>>> books['c++']
['C++ in depth', 'C++ Programming']
>>> books['java']
['Java Programming', 'Learn Java']
>>> book_prices = {'Learn ABC':150, 'Learn 123': 200, 'Rhymes':300, 'Cursive Writing':250}
>>> new_stock = {'Stories':350, 'Poems':290, 'Spellings':200}
>>> book_prices.update(new_stock)
>>> book_prices
{'Learn ABC': 150, 'Learn 123': 200, 'Rhymes': 300, 'Cursive Writing': 250, 'Stories': 350, 'Poems': 290, 'Spellings': 200}
>>> new_stock
{'Stories': 350, 'Poems': 290, 'Spellings': 200}
>>> dict.fromkeys( range(1000, 10000, 1000) , None )
{1000: None, 2000: None, 3000: None, 4000: None, 5000: None, 6000: None, 7000: None, 8000: None, 9000: None}
>>> dict.fromkeys( range(100, 1000, 100) , None )
{100: None, 200: None, 300: None, 400: None, 500: None, 600: None, 700: None, 800: None, 900: None}
>>> dict.fromkeys( range(1000, 10000, 1000) , Phani )
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    dict.fromkeys( range(1000, 10000, 1000) , Phani )
NameError: name 'Phani' is not defined
>>> student = { 'name': {  'first': 'John',
                       'last': 'Mark'
                      },
             'marks':98,
             'age':20
           }
>>> student['name']['last']
'Mark'
>>> d = { 2:300, 8:900, 7:800, 1:100}
>>> sorted(d.keys())
[1, 2, 7, 8]
>>>  d = { 2:300, 8:900, 7:800, 1:100,4:122,5:433,7:54}
 
SyntaxError: unexpected indent
>>> d = { 2:300, 8:900, 7:800, 1:100,4:122,5:433,7:54}
>>> sorted(d.keys())
[1, 2, 4, 5, 7, 8]
>>> 