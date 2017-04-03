# ------------------------------------------------------------------------------
# CHECK TWO VARIABLES AGAINST

latest_python = 3
my_python = 3

# The bad way
if latest_python > my_python:
    msg = 'Update available'
else:
    msg = 'Up to date'

print('Update check: {}'.format(msg))

# The good way - Pythonic way

latest_python = 3
my_python = 3

# inline if statement
msg = 'Update available' if latest_python > my_python else 'Up to date'

print('Update check: {}'.format(msg))
