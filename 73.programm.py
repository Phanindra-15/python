names = ['John', 'Joe', 'Ted', 'Sam', 'Jack', 'Jill']
heights = [160, 152, 147, 167, 177, 182]
weights = [54, 60, 90, 77, 87, 67]

L = [ ( name, (wt/(ht*ht*0.0001)) ) for name, ht, wt in zip(names, heights,weights)]
print(L,end=' ')


print()
print('=======================================')
#6th program

cubes = [ n**3  for n in range(5,21,2) ]
print(cubes)


print('=========================================')

prices = { 'pencil': 23,'pen': 34, 'eraser':12,'sharpener':13, 'marker':30}
 
l=[product for product, price in prices.items() if price > 20]
print(l)
