# MORE LIST FUNCTIONS

import random
import math

numList = []
for i in range(5):
    numList.append(random.randrange(1, 10))

numList.sort()
print(numList, '\n')

numList.reverse()
print(numList, '\n')

# insert a value to a list position (position, value)
numList.insert(5, 10)
print(numList, '\n')

# remove a value from the list
numList.remove(10)
print(numList, '\n')

# remove item from specific index
numList.pop(5)
print(numList, '\n')



for k in numList:
    print(k, end=', ')
print()
