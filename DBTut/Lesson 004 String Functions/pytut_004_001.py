# STRING FUNCTIONS

rand_string = '      this is an important string     '
print('whitespace ->', rand_string, '<- whitespace')

# strip whitespace from left
rand_string = rand_string.lstrip()
print(rand_string,  '<- whitespace')

# strip whitespace from right
rand_string = rand_string.rstrip()
print(rand_string)

rand_string = '      this is an important string     '
print('whitespace ->', rand_string,  '<- whitespace')
# strip whitespace from both left and right
rand_string = rand_string.strip()
print(rand_string)

# Capitalize first character
print(rand_string.capitalize())
# convert to: UPPERCASE
print(rand_string.upper())
# convert to: lowercase
print(rand_string.lower())
print()

# convert this list to string using join
a_list = ['Bunch', 'of', 'random', 'words']
# define separator and join selected list to string
print(' '.join(a_list))
print()

# split the string and store as list
a_list_2 = rand_string.split()
# the new list printout
print(a_list_2)
# cycle through the list
for i in a_list_2:
    # print each list entry on new line
    print(i)

print()

# count selected string in the string
print('How many times \'is\' is in the string? ', '\n',
      rand_string.count('is'))
print()

# returns starting position of the string
print('Where is string \'string\' in the string? ', '\n',
      rand_string.find('string'))

print()

# replace part of the string with new string
print(rand_string.replace('an ', 'a kind of '))
print()
