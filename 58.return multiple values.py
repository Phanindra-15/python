def func(text):
    u=i=d=0
    for ch in text:
        if ch.isupper():
            u+=1
        elif ch.islower():
            i+=1
        elif ch.isdigit():
            d+=1
    return(u,i,d)

uppers,lowers,digits = func('There are 52 cards in a deck')
print(uppers,lowers,digits)


t=func('There are 52 cards in a deck')
print(t)
