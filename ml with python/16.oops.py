Python 3.10.0 (tags/v3.10.0:b494f59, Oct  4 2021, 19:00:18) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
l=[1,2,3,4]

print(type(l))
<class 'list'>
print(type(4))
<class 'int'>
class Sample:
    pass

sample = Sample()
print(type(sample))
<class '__main__.Sample'>

class Dog:
    def__init__(self,breed):
        
SyntaxError: invalid syntax
class Dog:
    def __init__(self,breed):
        self.breed = breed
        #self : objects of its own class

      
sam = Dog(breed='lab')
sam
<__main__.Dog object at 0x000001CA7B1165F0>
sam.breed
'lab'
frank = Dog(breed='huske')
frank
<__main__.Dog object at 0x000001CA7B116650>
frank.breed
'huske'


class dog:
    def __init__(self.breed,name,color):
        
SyntaxError: invalid syntax
class dog:
    def __init__(self,breed,name,color):
        self.breed = breed
        self.name =  name
        self.color =color

        
sam = dog(breed = 'lab',name='sam',color='red')

frank=dog(breed = 'aab',name='tam',color='dazzle')

sam
<__main__.dog object at 0x000001CA7B116320>
frank
<__main__.dog object at 0x000001CA7B115FF0>
sam.dog
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    sam.dog
AttributeError: 'dog' object has no attribute 'dog'
sam.breed
'lab'
sam.name
'sam'
sam.color
'red'

frank.breed
'aab'
frank.name
'tam'
frank.color
'dazzle'
