# GUESSING GAME

# Guess a number between 1 and 10 by entering a number
# Repeat until the number is guessed correctly

# define the secret number
secret_number = 5

# repeat until breaking off this loop
while True:
    # try this or handle errors
    # noinspection PyBroadException
    try:
        # store value entered by user as Integer
        user_guess = int(input('Guess the secret number.\n'
                               'Enter a whole number between 1-10: '))

        # when value is outside of the range or go next condition if not true
        if 1 > user_guess or 10 < user_guess:
            print('Just 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 \n')
            continue
        # already in range but not the correct value
        elif secret_number != user_guess:
            print('Sorry, {} is incorrect!'.format(user_guess), '\n')
            continue
        # correct guess and break off the loop
        elif user_guess == secret_number:
            print('You guessed it!!!')
            break

    # handle floats
    except ValueError:
        print('Please enter whole number.')
    # handle undefined errors
    except:
        print('Please enter whole number.')
