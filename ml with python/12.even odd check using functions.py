#even and odd check using functions in python

def even_check(n):
    if n%2 == 0:
        return True
    else:
        return False
    
s=even_check(12)
print(s)


#to check even or odd using lists using functions in python

def even_check_list(l):
    for num in l:
        if num %2==0:
            return True
        else:
            return False
m=even_check_list([1,5,3,7,9])
print(m)

m1=even_check_list([1,2,4,5,3,7,9])
print(m1)
