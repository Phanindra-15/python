marks=input('enter marks:')
marks=int(marks)

if marks>=70:
    grade='a'

elif marks >=60:
    grade='b'

elif marks >=50:
    grade='c'
    
elif marks >=40:
    grade='d'

elif marks >=30:
    grade='e'

else:
    grade='f'

print(grade)
    
          
print('==============')

ch=input('enter a single character')

if len(ch)!=1:
    print('not entered a single character')
elif ch.isupper():
    print('entered a upper case')

elif ch.islower():
    print('entered a lower case')

elif ch.isnumeric():
    print('entered a number')
elif ch.isspace():
    print('entered a space')
else:
    print('entered a special character')
print('bye')
          
          
          
          
