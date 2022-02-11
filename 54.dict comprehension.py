Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[1,2,-3,4,-5,6,-7]
>>> 
>>> d={n: n**2 for n in l}
>>> d
{1: 1, 2: 4, -3: 9, 4: 16, -5: 25, 6: 36, -7: 49}
>>> 
>>> d={n: n**2 for n in l if n > 0}
>>> d
{1: 1, 2: 4, 4: 16, 6: 36}
>>> d={n: n**2 for n in l if n < 0}
>>> d
{-3: 9, -5: 25, -7: 49}
>>> m={'india':'new delhi','france':'paris','egypt','cairo'.'japan':'tokyo'}
SyntaxError: invalid syntax
>>> m={'india':'new delhi','france':'paris','egypt':'cairo','japan':'tokyo'}
>>> 
>>> m1={value:key for key,value in m.items()}
>>> m1
{'new delhi': 'india', 'paris': 'france', 'cairo': 'egypt', 'tokyo': 'japan'}
>>> text='hello world |||'
>>> 
>>> {ch:text.count(ch) for ch in text}
{'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 2, 'w': 1, 'r': 1, 'd': 1, '|': 3}
>>> 
>>> {ch:text.count(ch) for ch in set(text)}
{'d': 1, 'h': 1, 'r': 1, 'w': 1, 'o': 2, '|': 3, ' ': 2, 'l': 3, 'e': 1}
>>> 