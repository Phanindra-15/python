i=1
while i<=3:
    print('outer while loop',i)
    for j in range(1,5):
        print('\t inner for loop',j)
    i=i+1

#first example of nested loop
    
n=3
for i in range(1,11):
    print(f'{n} x {i} ={ n*i:3}')

print()

n=5
for i in range(1,11):
    print(f'{n} x {i} ={ n*i:3}')

print()

n=7
for i in range(1,11):
    print(f'{n} x {i} ={ n*i:3}')

print()

n=9
for i in range(1,11):
    print(f'{n} x {i} ={ n*i:3}')

print()
# short cut

for n in [3,4,5,6]:
    for i in range(1,11):
        print(f'{n} x {i} ={ n*i}')

    print()

