# SECRET MESSAGE - handling 1, 2 and 3 digits Unicode

user_entry = str(input('Enter a string to hide it: '))
print('\n', 'You entered \'{}\'.'.format(user_entry), '\n')


secret_num = ''

for char in user_entry:
    print(ord(char), end='')
    uni_len = len(str(ord(char)))
    if uni_len == 1:
        secret_num = secret_num + ' ' + ' ' + str(ord(char))
    elif uni_len == 2:
        secret_num = secret_num + ' ' + str(ord(char))
    elif uni_len == 3:
        secret_num += str(ord(char))
print()

print('\n', secret_num)
print(len(secret_num))
print()

# placeholder for the final string
input_str = ''

for i in range(0, len(secret_num)-1, 3):
    original_str = secret_num[i] + secret_num[i+1] + secret_num[i+2]
    # DEBUG print(chr(int(original_str)), end='')
    # adds all character to new string
    input_str += chr(int(original_str))

print('The same string as user entered: ', input_str)
