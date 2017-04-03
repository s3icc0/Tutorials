# ------------------------------------------------------------------------------
# SEARCH FOR VALUE IN LIST

needle = 'd'
haystack = ['a', 'b', 'c']

""" # The bad way
found = False
for letter in haystack:
    if needle == letter:
        print('Found!')
        found = True
        break
if not found:
    print('Not found!')
"""

# The good way - Pythonic way

# using the for loop else staement
# less lines, no additional variable
for letter in haystack:
    if needle == letter:
        print('Found!')
        break
else:  # if no break occurred
    print('Not found!')
