n = int(input("Enter a number:"))
for i in range(1,n+1):
    if(n%i==0):
        print(i)

print()

#2nd program


i=2
while n%i!=0:
    i+=1
print("Smallest divisor is:",i)

print()

for i in range(2,n):
    if(n%i==0):
        break
print("Smallest divisor is:",i)
 
