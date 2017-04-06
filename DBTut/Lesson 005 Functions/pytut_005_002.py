# RETURN MULTIPLE VALUES

def mult_divide(num1, num2):
    # separate all you need to return by comas
    return (num1 * num2), (num1 / num2)

# set multiple variables with the function
mult, divide = mult_divide(5, 4)

print('5 * 4 = ', mult)
print('5 / 4 = ', divide)