""" DON'T USE THESE AS VARIABLE NAMES:
and, del, from, not, while, as, elif, global,
or, with, assert, else, if, pass, yield, break,
except, import, print, class, exec, in, raise,
continue, finally, is, return, def, for, lambda,
try
"""

# Ask the user to input 2values and store them in variables num1 num2
# multiple variables defined
# .split() if there is a space between separate values into variables
num1, num2 = input('Enter 2 numbers separated by space: ').split()

# Convert the strings into regular numbers Integer
# variable names are case sensitive and can start with letters or _underscore
num1 = int(num1)
num2 = int(num2)

# Add the values entered and store in sum
sum_total = num1 + num2

# Subtract the values and store in difference
difference = num1 - num2

# Multiply the values and store in product
product = num1 * num2

# Divide the values and store in quotient
quotient = num1 / num2

# Use modulus on the values to find the remainder
remainder = num1 % num2

# Print the results
print('{} + {} = {}'.format(num1, num2, sum_total))
print('{} - {} = {}'.format(num1, num2, difference))
print('{} * {} = {}'.format(num1, num2, product))
print('{} / {} = {}'.format(num1, num2, quotient))
print('{} % {} = {}'.format(num1, num2, remainder))
