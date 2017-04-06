# WHILE LOOP
# use when you don't know how long to loop

# importing a standard random library / module
import random

# random value between 1-50
rand_num = random.randrange(1, 51)

# define the value (iterator) to be incremented before the while loop
i = 1

# loop until this becames true
while i != rand_num:
    # increment the iterator each time (same as i = i + 1)
    i += 1

# print the result when i == rand_num
print('The random value is: ', rand_num)
