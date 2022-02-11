data=[1,2,3,4,5]

for number in data:
    print(number)

print('- - -- - -- - - - - -')

data=[1,2,3,4,5]

for number in data:
    print(number,end=' ')

print('- - -- - -- - - - - -')
data=[1,2,3,4,5]

for number in data:
    if number %2==0:
       print(number*number,end=' ')

print(dir(str))
print('- - - - - - - - - -- - ')

print('- - - - - - - - - -- - ')
print('- - - - - - - - - -- - ')


print('- - - - - - - - - -- - ')


l=[]
for item in dir(str):
   if item.startswith('is'):
      l.append(item)
   
    
print(l)
