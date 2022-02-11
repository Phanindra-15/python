l=[1,3,2,4,5,2,6,3,2,1]
n=2
while n in l:
      l.remove(n)
print(l)



print('==============')

name=input('enter your name:')
if not name.istitle():
    print('wrong input')
else:
    print(name)

print('------------------------------------')

name=input('enter your name:')
while not name.istitle():
    print('wrong input')
    name=input('enter your name:')

    print(name)
