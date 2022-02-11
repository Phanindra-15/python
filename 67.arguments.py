n=[11,21,31,51,61]

def func(l):
    for i in range(len(l)):
        l[i]*=2

func(n)
print(n)


print()

d={}

def enter_data(d):
    while True:
        id=input('enter id:')
        if id == '0':
            break
        name=input('entr name:')
        d[id]=name

enter_data(d)
print(d)
