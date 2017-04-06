# DRAW A TREE - CUSTOM SOLUTION
# User will define how tall the tree is (how many lines it has)
""" Tree of 5 lines:
    #
   ###
  #####
 #######
#########
    #
- first line has one # in the distance of lines (spaces = lines - 1)
- each next line has 2 more # and 1 less space
- last line equals to first line

EXAMPLE FOR HEIGHT = 5
1. s * (h - 1) + 1 * t
2. s * (h - 2) + 3 * t
3. s * (h - 3) + 5 * t
4. s * (h - 4) + 7 * t
5. s * (h - 5) + 9 * t
6. = 1.

THIS IS WHAT I NEED TO OUTPUT
print(s * (h - i) + i * t)
print(s * (h - i) + (i = i + 2) * t)
print(s * (h - i) + (i = i + 2) * t)
print(s * (h - i) + (i = i + 2) * t)
print(s * (h - i) + (i = i + 2) * t)
print(s * (h - 1) + 1 * t)
"""

""" Need to do:
1. Decrement spaces by 1 each time through the loop
2. Increment the hashes by 2 each time through the loop
3. Save spaces to the stump by calculating tree height - 1
4. Decrement from tree height until it equals 0
5. Print spaces and then hashes for each row
6. Print stump spaces and then 1 hash
"""

# Ask the user how many lines he would like to see
tree_height = int(input('How tall the tree should be?\n'
                        'Enter number of the lines and hit ENTER: '))

# define some variables
# space multiplicator
s = tree_height - 1
# first line
s1 = s
# hash multiplicator
h = 1
# first line
h1 = h
# additionally define characters as variables as I like how it looks
# space character
space = ' '
# hash character
hashe = '#'

# print tree from top to bottom
# repeat until getting to the stump
while tree_height != 0:
    # print defined number of spaces and hashes
    print('{}{}'.format(s * space, h * hashe))
    # reduce number of space for next line
    s -= 1
    # increase number of hashes for next line
    h += 2
    # go to the next line
    tree_height -= 1

# print the stomp line
print('{}{}'.format(s1 * space, h1 * hashe))
