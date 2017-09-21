print('simple assignment')

shoplist = ['apple', 'mango', 'carrot', 'banana']

malist = shoplist

del shoplist[0]

print(shoplist)

print(malist)


malist = shoplist[:]

del malist[0]

del shoplist[-1]
print(shoplist)
print(malist)
