# import numpy as np 
# from data import data

# ob = data()
# df = ob.getData()
# a = np.arange(len(df)) + 1
# print(a)
# # #a = np.random.randint(1,100, 105, dtype='int')
# print(a)
# # print(a.shape)
# # print(a.type)

# b = list()
# for i in range(len(a)):
# 	b.append(a)

# print(b)

import random

r = list(range(100))
random.shuffle(r)
for i in r:
	print(i)