# LISTS

import random
import math

""" How list works?
List stores a values in boxes assigned to numbered keys starting from 0
Lists can grow!

[0 : 'string'] [1 :1.234] [2 : 28] [3 : 'c']
 ID    value    ID  value  ....
"""

randList = ['string', 1.234, 28, 'c']

print(randList)
print()

oneToTen = list(range(10))

print(oneToTen)
print()

randList = randList + oneToTen

print(randList)
print()

# get the nth value
print(randList[0])

print('List Length = ', len(randList))
print()

first3 = randList[0 : 3]

print('First 3 items : ')
print()

for i in first3:
    print('{} : {}'.format(first3.index(i), i))

print()

print(first3[0] * 3)
print()

# return True or False for item presence in the list
print('string' in first3)
print()

print('Index of string: ', first3.index('string'))
print()

print('How many time the \'string\' is in the list: ', first3.count('string'))
print()

# change item in list by referencing its index
first3[0] = 'new string'
print(first3[0])
print()

first3.append('Appended string')
print(first3)
print()























