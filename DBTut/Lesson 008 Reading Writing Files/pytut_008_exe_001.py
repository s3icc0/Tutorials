# FIBONACCI SEQUENCE

# Previously we generated 1 number in the
# Fibonacci sequence. This time ask the user to define
# how many numbers they want and display them
# The formula for calculating the Fibonacci sequence is
# Fn = Fn-1 + Fn-2
# Where F0 = 0 and F1 = 1

""" Sample Output
How many Fibonacci values should be found : 30
1
1
2
3
5
All Done
"""


def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        result = fib(num - 1) + fib(num - 2)
        return result

# Ask how many numbers they want
numfibvalues = int(input('How many Fibonacci values should be found? '))

# Loop while calling for each new number
i = 1

while i < numfibvalues:
    fibvalue = fib(i)

    print(fibvalue, end=', ')

    i += 1

print(fib(i))

print('\nAll Done')

# Print result and increment value used for loop