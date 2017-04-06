# LIST COMPREHENTION
# perform action on each item in the list

import random
import math


# double each i to be put to the list
# perform a e.g. calculation on the geerated range
evenList = [i * 2 for i in range(11)]

for i in evenList:
    print(i)

print()
print()


numList =[1, 2, 3, 4, 5]

# multidimensional list
# perform actions in list on each item in the list of values
# for each value create a list with all calculations (action)
listOfValues = [[math.pow(m, 2), math.pow(m, 3), math.pow(m, 4)]
                for m in numList]

for i in listOfValues:
    print(i)

print()
