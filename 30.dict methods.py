Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> p={'pencil':20,'pen':24,'scale':25,'eraser':5}
>>> p['ruler']=20
>>> p
{'pencil': 20, 'pen': 24, 'scale': 25, 'eraser': 5, 'ruler': 20}
>>> p['ruler']=25
>>> p
{'pencil': 20, 'pen': 24, 'scale': 25, 'eraser': 5, 'ruler': 25}
>>> p.get('pen')
24
>>> p.get('stapler')
>>> print(p.get('stapler'))
None
>>> (p.get('stapler',0)

 g
 
SyntaxError: invalid syntax
>>> p.setdefault('pen')
24
>>> p.setdefault('stapler')
>>> p
{'pencil': 20, 'pen': 24, 'scale': 25, 'eraser': 5, 'ruler': 25, 'stapler': None}
>>> p.setdefault('stapler',29)
>>> p
{'pencil': 20, 'pen': 24, 'scale': 25, 'eraser': 5, 'ruler': 25, 'stapler': None}
>>> p.keys()
dict_keys(['pencil', 'pen', 'scale', 'eraser', 'ruler', 'stapler'])
>>> p.values()
dict_values([20, 24, 25, 5, 25, None])
>>> list(p.values())
[20, 24, 25, 5, 25, None]
>>> p.items()
dict_items([('pencil', 20), ('pen', 24), ('scale', 25), ('eraser', 5), ('ruler', 25), ('stapler', None)])
>>> 'pen' in p
True
>>> 'pen'not in p
False
>>> 