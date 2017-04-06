# Solve for x
# equation format: x + 4 = 9

# x will always be the 1st value received and you only will deal with addition


# Get the user input
# Put equation into list
equation = input('Equation to be solved: ').split()


# equation_list = equation.split()

# List position 0 and 2 and 4 into variables
pos0 = equation[0]
pos2 = int(equation[2])
pos4 = int(equation[4])

# Define the function to get the x
def getX (pos2, pos4):
    return pos4 - pos2

# Print x
print('{} = {}'.format(pos0, getX(pos2, pos4)))