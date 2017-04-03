# ------------------------------------------------------------------------------
# HANDLE EXISTENCE OF VALUES IN DICTIONARY

ages = {
    'Mary': 31,
    'Jonathan': 28
    }

# age = ages['Dick']

""" # The bad way
# check 'Dick' is in the dictionary
if 'Dick' in ages:
    age = ages['Dick]
else:
    age = 'Unknown'
print('Dick is {} years old'.format(age))
"""

# The good way - Pythonic way

# using the get function we can check and define the default value in case
# lot less lines
# noinspection PyTypeChecker
age = ages.get('Dick', 'Unknown')
print('Dick is {} years old'.format(age))
