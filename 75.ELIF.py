marks=input('enter marks:')
marks=int(marks)

if marks>=70:
    grade='A'

elif marks >=60:
    grade='B'

elif marks >=50:
    grade='C'
    
elif marks >=40:
    grade='D'

elif marks >=30:
    grade='E'

else:
    grade='F'

print(grade,'IS THE GRADE OF RESPECTED STUDENT')
    
          
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
          
          
          
          
