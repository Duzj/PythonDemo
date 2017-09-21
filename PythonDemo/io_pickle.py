# encoding=utf-8
import pickle

shoplistfile = 'shoplist.data'

shoplist = ['apple', 'mango', 'carrot']

# b代码用二进制来写
f = open(shoplistfile, 'wb')


pickle.dump(shoplist, f)

f.close()


del shoplist


f = open(shoplistfile, 'rb')

# f = open(shoplistfile, "rt", encoding="utf-8")

storedlist = pickle.load(f)

print(storedlist)
