Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> toppers  =  { 'id11', 'id23', 'id34', 'id45', 'id77', 'id12', 'id89', 'id56', 'id55', 'id70' }
>>> champions  = { 'id19', 'id23', 'id78', 'id99', 'id79', 'id13', 'id56', 'id45', 'id80' }
>>> toppers.remove('id12')
>>> toppers.add('id45')
>>> toppers
{'id70', 'id34', 'id89', 'id11', 'id55', 'id56', 'id23', 'id77', 'id45'}
>>> toppers.add('id19')
>>> toppers
{'id70', 'id34', 'id89', 'id11', 'id55', 'id56', 'id23', 'id77', 'id19', 'id45'}
>>> toppers.remove('id19')
>>> toppeers
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    toppeers
NameError: name 'toppeers' is not defined
>>> toppers
{'id70', 'id34', 'id89', 'id11', 'id55', 'id56', 'id23', 'id77', 'id45'}
>>> champions.remove('id70')
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    champions.remove('id70')
KeyError: 'id70'
>>> champions.remove('id19')
>>> champions
{'id13', 'id56', 'id23', 'id80', 'id79', 'id78', 'id99', 'id45'}
>>> champions.remove('id80')
>>> champions
{'id13', 'id56', 'id23', 'id79', 'id78', 'id99', 'id45'}
>>> champions.add('id49')
>>> champions
{'id13', 'id56', 'id23', 'id79', 'id78', 'id99', 'id49', 'id45'}
>>> champions.add('id19')
>>> champions
{'id13', 'id56', 'id23', 'id79', 'id78', 'id99', 'id49', 'id19', 'id45'}
>>> set(toppers)&set(champions)
{'id56', 'id23', 'id45'}
>>> set(toppers) || set(champions)
SyntaxError: invalid syntax
>>> toppers-champions
{'id70', 'id34', 'id89', 'id11', 'id55', 'id77'}
>>> champions-topppers
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    champions-topppers
NameError: name 'topppers' is not defined
>>> champions-toppers
{'id13', 'id79', 'id78', 'id99', 'id49', 'id19'}
>>> toppers &champions
{'id56', 'id23', 'id45'}
>>> toppers|champions
{'id70', 'id13', 'id34', 'id89', 'id11', 'id55', 'id56', 'id23', 'id79', 'id78', 'id77', 'id99', 'id49', 'id19', 'id45'}
>>> toppers ^ champions
{'id13', 'id70', 'id34', 'id89', 'id11', 'id55', 'id79', 'id78', 'id77', 'id99', 'id49', 'id19'}
>>> toppers
{'id70', 'id34', 'id89', 'id11', 'id55', 'id56', 'id23', 'id77', 'id45'}
>>> champions
{'id13', 'id56', 'id23', 'id79', 'id78', 'id99', 'id49', 'id19', 'id45'}
>>> toppers.pop('id70')
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    toppers.pop('id70')
TypeError: set.pop() takes no arguments (1 given)
>>> toppers.popitem()
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    toppers.popitem()
AttributeError: 'set' object has no attribute 'popitem'
>>> 