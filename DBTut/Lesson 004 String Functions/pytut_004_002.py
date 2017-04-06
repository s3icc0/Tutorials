# MORE STRING METHODS

letter_z = 'z'
num_3 = '3'
num_3_14 = '3.14'
a_space = ' '

print('Is Z a letter or number? ', letter_z.isalnum())
print('Is Z a letter? ', letter_z.isalpha())
print('Is 3 a number? ', num_3.isdigit())
# float is not recognized as number
print('Is 3.14 a number? ', num_3_14.isdigit())
print('Is Z a lowercase? ', letter_z.islower())
print('Is Z a uppercase? ', letter_z.isupper())
print('Is Z a space? ', a_space.isspace())
print()


# FIRST FUNCTION
# define function isfloat with an attribute str_val
def isfloat(str_val):
    # try to convert value to float
    try:
        float(str_val)
        # if converted return True
        return True
    # if not converted to float successfully
    except ValueError:
        # return False
        return False

# call the new function with the attribute value
print('Is 3.14 a number? ', isfloat(num_3_14))
