# Solve for x
# equation format: x + 4 = 9
# equation format: 4 + x = 9
# for + - * /


# Get the user input
# Put equation into list
equation = input('Equation to be solved: ')

equa = equation.split()

# get the position of x
x_pos = None

if equa[0] == 'x':
    x_pos = 0
elif equa[2] == 'x':
    x_pos = 2


# get value1 and value2
num1 = None
num2 = None

if x_pos == 0:
    num1 = int(equa[2])
    num2 = int(equa[4])
elif x_pos == 2:
    num1 = int(equa[0])
    num2 = int(equa[4])


# define function for each math operation
def addi():
    return num2 - num1


def subt():
    if x_pos == 0:
        return num2 + num1
    elif x_pos == 2:
        return num1 - num2


def mult():
    return num2 / num1


def divi():
    if x_pos == 0:
        return num2 * num1
    elif x_pos == 2:
        return num1 / num2


# determine the math operation to be performed and print on screen9
if equa[1] == '+':
    print('{} = {}'.format(equation, addi()))
elif equa[1] == '-':
    print('{} = {}'.format(equation, subt()))
elif equa[1] == '*':
    print('{} = {}'.format(equation, mult()))
elif equa[1] == '/':
    print('{} = {}'.format(equation, divi()))
