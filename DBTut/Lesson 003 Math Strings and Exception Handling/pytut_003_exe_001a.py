# GUESSING GAME

# Guess a number between 1 and 10 by entering a number
# Repeat until the number is guessed correctly

# define the secret number
secret_number = 5

while True:
    user_guess = int(input('Guess the secret number.\n'
                           'Enter a whole number between 1-10: '))
    if user_guess == secret_number:
        print('You guessed it!!!')
        break

# handle the user not to enter anything else besides 1-10 whole (int) numbers
# test the entered number match the secret number
# ask user to enter number between 1-10
# if the guess is correct congratulate the user
