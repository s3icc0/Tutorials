# COMPARE TWO SETS OF VARIABLES (lists, dictionaries, maybe tuples) AGAINST

latest_python = (3, 5, 2)
my_python = (3, 5, 2)


# The bad way
msg = 'Up to date'
for i in range(len(latest_python)):
    if latest_python[i] > my_python[i]:
        msg = 'Update available'
        break

print('Update check: {}'.format(msg))


# Slightly better way

# zips into pairs and allows comparison fair way
for latest_subversion, my_subversion in zip(latest_python, my_python):
    if latest_subversion > my_subversion:
        msg = 'Update available'
        break
    else:
        msg = 'Up to date'

print('Update check: {}'.format(msg))


# The good way - Pythonic way

msg = 'Update available' if latest_python > my_python else 'Up to date'

print('Update check: {}'.format(msg))
