n=int(input('enter a number:'))
if n%2==0:
    print('n is even')
else:
    print('n is odd')


print('=============================')

s=input('enter a string')
if s==s[::-1]:
    print(s,'is a palindrome')
else:
    print(s,'is not a palindrome')
    
print('=========================')

m=input('enter a string')
if m==m[::-1]:
    if len(m)<5:
        print(m,'is a small palindrome')
    else:
        print(m,'is a big palindrome')
else:
    print(m,'is not a palindrome')
        
