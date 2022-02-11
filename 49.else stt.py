n=[3,34,4,5,56,6,7,76,90,45,2,-45,7,78]



for no in n:
    if no <0:
        print('found a negative number in the list')
        break
else:
    print('no negative number in the list')
