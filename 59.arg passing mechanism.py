x=5
print(id(x))

def func(num):
    print('num is',num)
    print(id(num))

    
func(x)
print('x is',x)
print()

print('===================================')

x=15


def func(num):
    print('num is',num)
    num=10
    print('num is',num)

    
func(x)
print('x is',x)


print('=============================')


evens=[2,4,6,8]

def func(l):
    print('l is',l)
    l=[10,20,25,30]
    print('l is',l)
    
func(evens)
print('evens is', evens)
