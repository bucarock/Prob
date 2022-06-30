a = {1,3,4,2,8,3}
b = frozenset([2,17,3,4,9,5])

c = a|b
print(a.union(b))
print(c)

print(a&b)
print(a.intersection(b))

for i in b:
    print(i)