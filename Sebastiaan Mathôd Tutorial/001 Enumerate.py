# ------------------------------------------------------------------------------
# WALK THROUGH THE LIST

citties = ['Marseille', 'Amsterdam', 'New York', 'London']

""" # The bad way
i = 0  # create counter variable
for city in citties:
    print(i, city)
    i += 1
"""

# The good way - Pythonic way

# enumerate returns both indices and values (keep track of both)
# less lines, easier to read
for i, city in enumerate(citties):
    print(i, city)
