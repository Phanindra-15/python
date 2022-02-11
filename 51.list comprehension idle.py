Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> cubes=[n**3 for n in range(5,21)]
>>> cubes
[125, 216, 343, 512, 729, 1000, 1331, 1728, 2197, 2744, 3375, 4096, 4913, 5832, 6859, 8000]
>>> l=[2,3,4,7,6,5]
>>> cubes= [n**3 for n in l]
>>> cubes
[8, 27, 64, 343, 216, 125]
>>> l2=[n*2 for n in l]
>>> l2
[4, 6, 8, 14, 12, 10]
>>> [str(n) for n in l]
['2', '3', '4', '7', '6', '5']
>>> [float for n in l]
[<class 'float'>, <class 'float'>, <class 'float'>, <class 'float'>, <class 'float'>, <class 'float'>]
>>> [float(n) for n in l]
[2.0, 3.0, 4.0, 7.0, 6.0, 5.0]
>>> cities=['ongole','newyork','chennai','england','france']
>>> 
>>> [city[:3] for city in cities]
['ong', 'new', 'che', 'eng', 'fra']
>>> [city.title() for city in cities]
['Ongole', 'Newyork', 'Chennai', 'England', 'France']
>>> 
>>> [(city,len(city)) for city in cities]
[('ongole', 6), ('newyork', 7), ('chennai', 7), ('england', 7), ('france', 6)]
>>> [[city,len(city)] for city in cities]
[['ongole', 6], ['newyork', 7], ['chennai', 7], ['england', 7], ['france', 6]]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> heights=[12,23,3,14,21]
>>> 
>>> weights[2500,5443,3321,3330,6660]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    weights[2500,5443,3321,3330,6660]
NameError: name 'weights' is not defined
>>> 
>>> heights=[12,23,3,14,21]
>>> 
>>> weights=[2500,5443,3321,3330,6660]
>>> 
>>> [h*2.54 for h in heights]
[30.48, 58.42, 7.62, 35.56, 53.34]
>>> 
>>> [h*2 for h in heights]
[24, 46, 6, 28, 42]
>>> 
>>> [h*4 for h in heights]
[48, 92, 12, 56, 84]
>>> 
>>> l2=[(w//1000,w%10000) for w in weights]
>>> l2
[(2, 2500), (5, 5443), (3, 3321), (3, 3330), (6, 6660)]
>>> l2=[(t(0)*1000+t(1)) for t in l2]
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    l2=[(t(0)*1000+t(1)) for t in l2]
  File "<pyshell#38>", line 1, in <listcomp>
    l2=[(t(0)*1000+t(1)) for t in l2]
TypeError: 'tuple' object is not callable
>>> l2=[(w//1000) for w in weights]
>>> l2
[2, 5, 3, 3, 6]
>>> l2=[(w%1000) for w in weights]
>>> l2
[500, 443, 321, 330, 660]
>>> ]
>>> 
>>> [h*2.54 for h in heights]
[
	
SyntaxError: unmatched ']'
>>> 