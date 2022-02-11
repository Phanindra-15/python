names=[]

while True:
    name = input('enter name:')
    if name == 'done':
        break
    if not name.isalpha():
        print('invalid name')
        continue
    names.append(name)
print(names)
