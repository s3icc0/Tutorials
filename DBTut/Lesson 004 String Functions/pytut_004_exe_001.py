# ACRONYM GENERATOR

# Random Access Memory -> RAM


# Ask the user for input and make sure that is a string
print('ACRONYM GENERATOR', '\n')
full_str = str(input('Enter the text you want to make acronym of: '))

# format the string and do the list
# strip whitespace - this is not needed as split will do anyway
# convert to UPPERCASE
# convert string to list
lst_str = full_str.upper().split()

# loop through the list and output in new var acro
acro = ''
for i in lst_str:
    # return the character on position 0
    # concatenate the result in new var acro
    acro += i[0]

print('The acronym of \'{}\' is {}.'.format(full_str, acro), '\n')
