for n in range(2,10):
  isprime=True
  for i in range(2,n):
       if n%i == 0:
           isprime = False
           print(f'{n} is not prime')
           break
  if isprime:
     print(f'{n} is prime')

print()
print()
#another program

for n in range(10,20):
  isprime=True
  for i in range(2,n):
       if n%i == 0:
           isprime = False
           print(f'{n} is not prime')
           break
  if isprime:
     print(f'{n} is prime')
