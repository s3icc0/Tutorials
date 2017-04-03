# ------------------------------------------------------------------------------
# SWAP TWO VARIABLES (or even more?)

""" Sometimes better on one line for better readability experience
x = 10
y = -10
"""

x, y = 10, -10

print('Before: x = {}, y = {}'.format(x, y))
""" # The bad way
tmp = y
y = x
x = tmp
"""

# The good way - Pythonic way

# less lines, easier to read, less variables
x, y = y, x
print('After: x = {}, y = {}'.format(x, y))
