# ------------------------------------------------------------------------------
# WALK THROUGH MULTIPLE LISTS AT SAME TIME

x_list = [1, 2, 3]
y_list = [2, 4, 6]

""" # The bad way
for i in range(len(x_list)):
    x = x_list[i]
    y = y_list[i]
    print(x, y)
"""

# The good way - Pythonic way

# zip takes 2+ lists and zips those together by creating tuples for each i
for x, y in zip(x_list, y_list):
    print(x, y)
