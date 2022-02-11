def simple_interest(p,r,t):
    si=(p*t*r)/100
    print(si)

principal = 2000
rate = 5
time = 4

simple_interest(principal,rate,time)

#using return statment

def simple_interest(p,r,t):
    si=(p*t*r)/100
    return si

principal = 2000
rate = 5
time = 4

interest=simple_interest(principal,rate,time)
amount=principal + interest
print(amount)


print()

def compare(a,b):
    if a>b:
        return 1
    elif a<b:
        return -1
    else:
        return 0

a=4
b=6
print(compare)
