matrix = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
list_ = [[row[i] for row in matrix] for i in range(4)]
print(list_)
list2 = list(zip(*matrix))
print(list2)

t = 12345, 543221, 'hello'
print(t[0])
u = t, (1, 2, 3, 4, 5)
print(u)
print(t[0])
empty = ()
sinline = 'hello', 'world'
print(len(empty))
print(len(sinline))

print('--------------')
a = [1,2,3,4,5]
del a[2:3]
print(a)

