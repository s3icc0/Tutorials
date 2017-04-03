# ------------------------------------------------------------------------------
# HANDLE EXCEPTIONS

# e.g. convert integer to int
print('Converting!')
print(int(1))
print('Done!')

# e.g. convert string to int
print('Converting!')
try:
    print(int('x'))
except:
    print('Conversion failed!')
print('Done!')


print('Converting!')
try:
    print(int('x'))
except:
    print('Conversion failed!')
else:  # if no except occurrs
    print('Conversion successful!')
finally:  # always executed, even if error occurs
    print('Done!')
