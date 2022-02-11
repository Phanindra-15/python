def add(a,b):
    print(a+b)

add(13,7)

print()

num1=11
num2=17
add(num1,num2)


add(num1*2, num2/3)

add(3.2,5.6)

add('ac','fv')
add([1,2,3],[4,5,6])



def sum(a,b):
    s=0
    for i in range(a,b+1):
        s=s+i
        print(s)
sum(2,6)
