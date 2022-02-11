n=int(input('enter a number:-'))
factorial=1

for i in range(1,n+1):
    factorial *= i

print(factorial)



#fibonacci series

x,y=1,1
for i in range(10):
    print(x,end=' ')
    x,y=y,x+y
print('======================')

x,y=1,1
while x<500:
    print(x,end=' ')
    x,y=y,x+y
