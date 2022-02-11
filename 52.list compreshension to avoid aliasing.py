Python 3.9.1 (tags/v3.9.1:1e5d33e, Dec  7 2020, 17:08:21) [MSC v.1927 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l1=[ [] ] *4
>>> l1
[[], [], [], []]
>>> l1[0].append(9)
>>> l1
[[9], [9], [9], [9]]
>>> #using list comprehension to avaoid alaising
>>> l2=[ [] for i in range(4)]
>>> l2
[[], [], [], []]
>>> l2[0].append(9)
>>> l2
[[9], [], [], []]
>>> l2[1].append(2)
>>> l2
[[9], [2], [], []]
>>> 
>>> l3=[ [0]*3 ] *4
>>> l3
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> l3[0].pop()
0
>>> l3[1].pop()
0
>>> l3
[[0], [0], [0], [0]]
>>> #using list comprehensions to avoid alaising
>>> l4=[ [0]*3 for i  in range(4)]
>>> l4
[[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]
>>> l4[1].pop()
0
>>> l4
[[0, 0, 0], [0, 0], [0, 0, 0], [0, 0, 0]]
>>> l4[0].pop()
0
>>> l4
[[0, 0], [0, 0], [0, 0, 0], [0, 0, 0]]
>>> 