# GENERATE THE MULTIPLICATION TABLE

# With 2 for loops fill the cells in a multidimensional list with a
# multiplication table using values 1-9

''' This should be the result:
1, 2, 3, 4, 5, 6, 7, 8, 9,
2, 4, 6, 8, 10, 12, 14, 16, 18,
3, 6, 9, 12, 15, 18, 21, 24, 27,
4, 8, 12, 16, 20, 24, 28, 32, 36,
5, 10, 15, 20, 25, 30, 35, 40, 45,
6, 12, 18, 24, 30, 36, 42, 48, 54,
7, 14, 21, 28, 35, 42, 49, 56, 63,
8, 16, 24, 32, 40, 48, 56, 64, 72,
9, 18, 27, 36, 45, 54, 63, 72, 81
'''


import random
import math


# Create the multiD list
# create list with any value * 10 index positions (0-9)
multiTable = [[1] * 10 for i in range(10)]

# increment with outer for
# perform the calculation from x-th to y-th list
for i in range(0, 10):
    # increment with inner for
    # perform the calculation from x-th to y-th index in the lists
    for j in range(0, 10):
        # assign the value to the cell
        # for list number * index number
        multiTable[i][j] = i * j


print()

# output the data
# skip list 0 by starting at 1
for i in range(1, 10):
    # skip index 0 in the lists by starting at 1
    for j in range(1, 10):
        # print format
        print(multiTable[i][j], end=', ')
    print()

# so in reality the data are created just by the index values, therefore any
# index (both i and j) with 0 value will return 0 - that is the reason why we
# are hiding the first list and the first index
