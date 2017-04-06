# BUBBLE SORT
# used to sort a list
# moves the largest number to the end of the list each round it goes

""" The Bubble sort is a way to sort a list
It works this way:
1. An outer loop decreases in size each time
2. The goal is to have the largest number at the end of the list when the
   outer loop completes 1 cycle
3. The inner loop starts comparing indexes at the beginning of the loop
4. Check if list[Index] > list[Index + 1]
5. If so swap the index values
6. When the inner loop completes the largest number is at the end of the list
7. Decrement the outer loop by 1
"""

import random

# create a list to be sorted
numList = []

for i in range(15):
    numList.append(random.randrange(0, 10))

print(numList)
print()

# create a value to decrement in the outer loop
# getting each index number for each item in a list
# as list starts with 0 we need to subtract 1 from the number of items we have
i = len(numList) - 1

# outer loop
while i > 0:

    # inner loop
    j = 0

    while j < i:

        # to know what is going on in the loop
        print('\nIs {} > {}'.format(numList[j], numList[j + 1]))

        # check if lower index value is larger then the one index above
        if numList[j] > numList[j + 1]:

            print('Switch')

            # SWAP CONCEPT
            # swap values in the list
            # temporarily store the lower index value
            temp = numList[j]
            #
            numList[j] = numList[j + 1]
            numList[j + 1] = temp
        else:
            print('Don\'t Switch')

        j += 1

        for k in numList:
            print(k, end=', ')
        print()

    print('END OF ROUND')

    i -= 1

for k in numList:
    print(k, end=', ')
print()
