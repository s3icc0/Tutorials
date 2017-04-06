# Solve for x
# equation format: x + 4 = 9

# x will always be the 1st value received and you only will deal with addition

def solve_eq(equation):
    # split the equation string from user entry
    # define variables and assign the splited values
    x, add, num1, equal, num2 = equation.split()

    # convert the numbers to integers
    num1, num2 = int(num1), int(num2)

    # calculate and create string
    return x + ' = ' + str(num2 - num1)

# the input is our equation string to be solved
print(solve_eq(input('Enter the equation: ')))