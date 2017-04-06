# GENERATE 10x10 LIST oF LIST


import random
import math


# create 10 lists with 10 values of 0
# [0] * 10 creates a list of 10 values of 0
# for loop will do it 10 times
multiDList = [[0] * 10 for i in range(10)]

for i in multiDList:
    print(i)

print()

# 1st attribute [] defines the list #
# 2nd attribute [] defines the position in the list
# put value of 10 to position 1 in list nr 0
multiDList[0][1] = 10

# print first value from 2nd list
print(multiDList[1][0])
print()

for i in multiDList:
    print(i)

print()

# how the structure really looks (list number # || list index)
listTable = [[0] * 4 for i in range(4)]

for i in range(4):
    for j in range(4):
        listTable[i][j] = '{} : {}'.format(i, j)

for i in range(4):
    for j in range(4):
        print(listTable[i][j], end=' || ')
    print()

print()