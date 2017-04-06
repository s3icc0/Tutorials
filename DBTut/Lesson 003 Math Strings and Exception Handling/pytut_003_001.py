# EXCEPTION HANDLING

# Loop until break is reached
while True:
    # the code to be challenged
    # noinspection PyBroadException
    try:
        number = int(input('Please enter a number: '))
        break
    # handle specific error - ValueError
    except ValueError:
        print('You didn\'t enter a number!')
    # handle any error (default) - but recommended is to know the errors
    except:
        print('An unknown error occurred')

print('Thank you for entering a number {}.'.format(number))

''' DO WHILE LOOP - executes the code at least once
do:
   .. bunch of code ..
while condition
'''
