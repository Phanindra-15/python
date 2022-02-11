Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> student={'name':'phani',
	     'age':21,
	     'city':'ongole',
	     'marks':{'maths':45,
		      'phy':56,
		      'che':67
		      },
	     'gender':M
	    }
Traceback (most recent call last):
  File "<pyshell#8>", line 8, in <module>
    'gender':M
NameError: name 'M' is not defined
>>> student={'name':'phani',
	     'age':21,
	     'city':'ongole',
	     'marks':{'maths':45,
		      'phy':56,
		      'che':67
		      },
	      'gender':'M'
	    }
>>> student['name']
'phani'
>>> student['age'
	]
21
>>> student['city']
'ongole'
>>> student['marks']
{'maths': 45, 'phy': 56, 'che': 67}
>>> student['marks']['maths']
45
>>> student['marks']['phy']
56
>>> student['marks']['che']
67
>>> student['gender']
'M'
>>> students={ 105416:{'name':'phani',
	     'age':21,
	     'city':'ongole',
	     'marks':{'maths':45,
		      'phy':56,
		      'che':67
		      },
	     'gender':M
	    },

	   144547: {student={'name':'hemanth',
	                     'age':24,
	                     'city':'chni',
	                     'marks':{'maths':65,
		             'phy':96,
		             'che':97
		                     },
	                     'gender':M
	    },
		    
SyntaxError: invalid syntax
>>> students={ 105416:{'name':'phani',
	     'age':21,
	     'city':'ongole',
	     'marks':{'maths':45,
		      'phy':56,
		      'che':67
		      },
	     'gender':M
	    },



	   144547 : {'name':'hemanth',
	                     'age':24,
	                     'city':'chni',
	                     'marks':{'maths':65,
		             'phy':96,
		             'che':97
		                     },
	                     'gender':M
	    },


	   133299 : {'name':'sumanth',
	                     'age':14,
	                     'city':'rjm',
	                     'marks':{'maths':55,
		             'phy':46,
		             'che':57
		                     },
	                     'gender':M
		     }
	    }
Traceback (most recent call last):
  File "<pyshell#32>", line 8, in <module>
    'gender':M
NameError: name 'M' is not defined
>>> students={ 105416:{'name':'phani',
	     'age':21,
	     'city':'ongole',
	     'marks':{'maths':45,
		      'phy':56,
		      'che':67
		      },
	     'gender':'M'
	    },



	   144547 : {'name':'hemanth',
	                     'age':24,
	                     'city':'chni',
	                     'marks':{'maths':65,
		             'phy':96,
		             'che':97
		                     },
	                     'gender':'M'
	    },


	   133299 : {'name':'sumanth',
	                     'age':14,
	                     'city':'rjm',
	                     'marks':{'maths':55,
		             'phy':46,
		             'che':57
		                     },
	                     'gender':'M'
		     }
	    }
>>> print(students)
{105416: {'name': 'phani', 'age': 21, 'city': 'ongole', 'marks': {'maths': 45, 'phy': 56, 'che': 67}, 'gender': 'M'}, 144547: {'name': 'hemanth', 'age': 24, 'city': 'chni', 'marks': {'maths': 65, 'phy': 96, 'che': 97}, 'gender': 'M'}, 133299: {'name': 'sumanth', 'age': 14, 'city': 'rjm', 'marks': {'maths': 55, 'phy': 46, 'che': 57}, 'gender': 'M'}}
>>> import pprint
>>> pprint.pprint(students)
{105416: {'age': 21,
          'city': 'ongole',
          'gender': 'M',
          'marks': {'che': 67, 'maths': 45, 'phy': 56},
          'name': 'phani'},
 133299: {'age': 14,
          'city': 'rjm',
          'gender': 'M',
          'marks': {'che': 57, 'maths': 55, 'phy': 46},
          'name': 'sumanth'},
 144547: {'age': 24,
          'city': 'chni',
          'gender': 'M',
          'marks': {'che': 97, 'maths': 65, 'phy': 96},
          'name': 'hemanth'}}
>>> students(105416)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    students(105416)
TypeError: 'dict' object is not callable
>>> TypeError: 'dict' object is not callable
SyntaxError: invalid syntax
>>> students[105416]
{'name': 'phani', 'age': 21, 'city': 'ongole', 'marks': {'maths': 45, 'phy': 56, 'che': 67}, 'gender': 'M'}
>>> students[133299]
{'name': 'sumanth', 'age': 14, 'city': 'rjm', 'marks': {'maths': 55, 'phy': 46, 'che': 57}, 'gender': 'M'}
>>> pprint.print(students[105416])
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    pprint.print(students[105416])
AttributeError: module 'pprint' has no attribute 'print'
>>> pprint.pprint(students[105416])
{'age': 21,
 'city': 'ongole',
 'gender': 'M',
 'marks': {'che': 67, 'maths': 45, 'phy': 56},
 'name': 'phani'}
>>> pprint.pprint(students[133299])
{'age': 14,
 'city': 'rjm',
 'gender': 'M',
 'marks': {'che': 57, 'maths': 55, 'phy': 46},
 'name': 'sumanth'}
>>> pprint.pprint(students[144547])
{'age': 24,
 'city': 'chni',
 'gender': 'M',
 'marks': {'che': 97, 'maths': 65, 'phy': 96},
 'name': 'hemanth'}
>>> students[105416]['name']
'phani'
>>> students[133299]['name']
'sumanth'
>>> students[144547]['name']
'hemanth'
>>> students[105416]['marks']
{'maths': 45, 'phy': 56, 'che': 67}
>>> students[105416]['marks']['maths']
45
>>> students[105416]['marks']['phy']
56
>>> students[105416]['gender']
'M'
>>> students[144547]['city']
'chni'
>>> students[105416]['marks']
{'maths': 45, 'phy': 56, 'che': 67}
>>> students[105416]['city']
'ongole'
>>> 