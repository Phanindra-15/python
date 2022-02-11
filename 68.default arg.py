def display_line():
    print('-' *20)
    print()
    print('=='*25)
    
display_line()


print()


#using default arguments

def display_line(ch='-'):
    print(ch*20)

display_line()
display_line('()')
display_line('%')
display_line('&')
display_line('::')


print()
print()

def func(a,l=[]):
    l.append(a)
    print(l)

func(10,[1,2,3])
func(8,[5,6])
func(9)
func('hello')
func(100)
