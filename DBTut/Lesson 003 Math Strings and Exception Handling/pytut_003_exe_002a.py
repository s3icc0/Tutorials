# SECRET MESSAGE

# Receive a uppercase string and then hide its meaning by turning
# it into a string of unicodes
# Then translate it from unicode back into its original meaning

# Get a string from the user
user_entry = str(input('Enter a string to hide it: '))
print('\n', 'You entered \'{}\'.'.format(user_entry), '\n')

# Loop through characters and convert each to Unicode and concatenate all
# Make sure all numbers will have the same number of positions

# define the placeholder for the new string
secret_num = ''

# loop through original string
for char in user_entry:
    # print string characters as Unicode
    print(ord(char), end='')
    # concatenate characters to placeholder
    secret_num += str(ord(char))

print('\n', secret_num)
print(len(secret_num))
print()

# Read the resulting number, split it into separate characters
# loop through the new string for each 2 characters
for i in range(0, len(secret_num)-1, 2):
    # Get each group of 2 numbers as string
    original_str = secret_num[i] + secret_num[i+1]
    # Convert each string to int and back from Unicode, but is not stored as one
    print(chr(int(original_str)), end='')

print()
