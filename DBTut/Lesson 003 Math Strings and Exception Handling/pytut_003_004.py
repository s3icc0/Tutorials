# STRINGS

# get data type returns Int as Integer
print(type(3))
# returns Float
print(type(3.14))
# returns Str as String in single quotes
print(type('3'))
# double quotes makes no difference
print(type("3"))

samp_string = 'This is a very important string'

# return whatever is on position 0 in the string
print(samp_string[0])
# return last character
print(samp_string[-1])
# returns 8th character, variables can be used
print(samp_string[3+5])

# get length of the string
print('Length : ', len(samp_string))
# slice from position 0 to 3 (returns whatever is 0+1+2+3
print(samp_string[0:4])
# slice from 8th index to the end
print(samp_string[8:])
# concatenate strings
print('Green ' + 'Eggs')
# return the string 5 times
print('Hello ' * 5)

# convert integer or float into string
print(str(4.1))

# cycle through given string and return characters one-by-one
for char in samp_string:
    print(char, '', end='')
print()

# start from 0 to length-1 (length is 31 but index only 30 due to 0)
# the 2 defines that 2 characters will be processed
for i in range(0, len(samp_string)-1, 2):
    # we need to increase by 1 not to repeat the second char next
    print(samp_string[i] + samp_string[i+1], ' ', end='')
print()

# Computers assign characters with a number known as a Unicode
# A-Z have the numbers 65-90 and a-z 97-122

# You can get the Unicode code with ord()
print("A =", ord("A"))

# You can convert from Unicode with chr
print("65 =", chr(65))
