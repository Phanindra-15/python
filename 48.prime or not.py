n=int(input('enter a  number:'))

is_prime=True
for i in range(2,n):
    if n%i == 0:
        is_prime = False
        break
if is_prime:
    print(f'{n} is  prime')
else:
    print(f'{n} is not prime')


print()
print()

for m in range(2,10):
    is_prime=True
    for i in range(2,m):
        if m%i == 0:
           is_prime = False
           break
    if is_prime:
       print(m)

#break inside while loop



total = 0
while total<=100:
    num=int(input('enter  number:'))
    if num<0:
        break
    total +=num
print(total)
