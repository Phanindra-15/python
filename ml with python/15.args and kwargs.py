def myfunc(a,b):
    return sum((a,b))

x=myfunc(1,2)
x1=myfunc(2,4)

print(x)
print(x1)

print('============================')
def myfunc(a,b,c):
    return sum((a,b,c))

x=myfunc(1,2,4)
x1=myfunc(2,4,6)

print(x)
print(x1)

print('-----------------------')

def myfunc(a=0,b=0,c=0,d=0,e=0):
    return sum((a,b,c,d,e))

x=myfunc(1,2,3,4,5)
y=myfunc(1,2,3)
print(x)
print(y)
print('----------------------')
# when a fun parameter start with * it allows us to pass arbitrsry number of constants

def myfunc(*args):
    print(args)
    return sum(args)

x = myfunc(1,2,3)

y = myfunc(1,2,3,4,5,6,7,8,9,12,34,57,87)

print(x)
print(y)


# KWARGS

def myfunc(**kwargs):
    print(kwargs)
    

x=myfunc(a=1,b=2,c=3,d=4)
print(x)
# if the function is taking more values and then we need to have specific value then we csn get the value of the
# specific value can be obtained b usin kwargs method
def myfunc(**kwargs):
    print(kwargs)
    print('=========================')
    print(kwargs['a'])
    print(kwargs['b'])
    

x=myfunc(a=1,b=2,c=3,d=4)
print(x)
print('connection betweeen args and kwargs')

#connection between args and kwargs


def myfunc(*x,**y):
    print(y)
    print(x)

myfunc(1,2,3,4,a=10,b=45)
