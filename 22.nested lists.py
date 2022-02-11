L = ['a', 'b', ['cc', 'dd', ['eee', 'fff']], 'g', 'h']


print(L[2])

print(L[2][2])

print(L[2][2][0])

print(L[2][2][1])


print(L[1])



m = ['a', ['bb', 'cc'], 'd']
m[1].append('xx')
print(m)



m[1].extend([1,2,3])
print(m)
