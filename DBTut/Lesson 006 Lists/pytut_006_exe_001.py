#RANDOM LIST
# generate a list with 5 values between 1 and 9

import random
import math

randList = []

for i in range(100):
    randList.append(random.randrange(1, 10))

for i in randList:
    print('{} : {}'.format(randList.index(i), i))