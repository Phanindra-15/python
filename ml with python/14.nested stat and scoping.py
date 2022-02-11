x = 90

def hello():
    x = 100
    return x
print(x)

print(hello())

# scope is used to access particular variable or variable name in a program

# global variables  can be accessed every where

# but the local variables can be accessed only to the specified location present in the variable

# there is one rule in understanding how to declare which value will be printed

#  """"LEGB RULE""""

#local
#     def hello():
#x = 100 # this is local to this function
    #return x

#enclosing : - the name we writing some thing between them

 #eg:
name='sid'

def  greet():
    name='sai'  #it is inside local and global so we call it as a enclosing rule
    def hello():
        name='kiran'
        print('hello',name)

    hello()
print('greet',name)
greet()
 
print(name)
