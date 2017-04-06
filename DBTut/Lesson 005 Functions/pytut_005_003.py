# UNKNOWN NUMBER OF ARGUMENTS IN FUNCTIONS


# splatter *args will provide all given arguments
def sumAll(*args):
    sum = 0

    for i in args:
        sum += i

    return sum

print('Sum: ', sumAll(1, 2, 3, 4, 5))


