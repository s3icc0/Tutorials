# DRAW A TREE
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

# Get the starting spaces for the top of the tree
spaces = tree_height - 1

# There is one hash to start that will be incremented
hashes = 1

# Save stump spaces til later
stump_spaces = tree_height - 1

# Make sure the right number of rows are printed
while tree_height != 0:
    # Print the spaces
    for i in range(spaces):
        print(' ', end='')
    # Print the hashes
    for j in range(hashes):
        print('#', end='')
    # Newline after each row is printed
    print()
    # Spaces are decremented by 1 each time
    spaces -= 1
    # Hashes is incremented by 2 each time
    hashes += 2
    # Decrement tree heigh each time to jump out of the loop
    tree_height -= 1

# Print the spaces before the stump and then the final hash
for k in range(stump_spaces):
    print(' ', end='')

print('#')
