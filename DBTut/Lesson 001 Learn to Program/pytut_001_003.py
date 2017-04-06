# CALCULATOR
# Enter Calculation: 5 * 6
# 5 * 6 = 30

print()
print('Whole numbers simple calculator')
print()

# Store the user input of 2 numbers and the operator
num1, operator, num2 = input('Enter calculation and hit ENTER \n'
                             '(make sure you separate entries with space)'
                             ': ').split()

# Convert the strings into integers
num1 = int(num1)
num2 = int(num2)

# if + then we need to provide output based on addition
# if - then we need to provide output based on subtraction
# if * then we need to provide output based on multiplication
# if / then we need to provide output based on division
# Print the result
if operator == '+':
    print('{} + {} = {}'.format(num1, num2, num1 + num2))
elif operator == '-':
    print('{} - {} = {}'.format(num1, num2, num1 - num2))
elif operator == '*':
    print('{} * {} = {}'.format(num1, num2, num1 * num2))
elif operator == '/':
    print('{} / {} = {}'.format(num1, num2, num1 / num2))
else:
    print('Use either + - * or / next time')

# other ways to test conditions: >  <  >=  <=  != (last is not equal to)
