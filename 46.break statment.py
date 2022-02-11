trip=['ongole','nellore','guntur','vij','rjm','chirala','kavali','chennai','banglore','kochi']

for city in trip:
    print(city)
    if city=='chennai':
        break
print()

n=[3,34,4,5,56,6,7,76,90,45,2,45,7,78]


found= False
for no in n:
    if no <0:
        print('found a negative number in the list')
        found =True
        break
if found == False:
    print('no negative number in the list')
