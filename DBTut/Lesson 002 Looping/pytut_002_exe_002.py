# INVESTMENT CALCULATOR
# Have the user enter their investment amount and expected interest
# Each year their investment will increase by:
# their investment + their investment * interest rate is
# Print out the earnings after a 10 year period

# Ask user HOW MUCH they would like to invest and evaluate
investment = eval(input('Enter your investment in USD: '))

# Ask user HOW LONG they would like to invest and evaluate
years = eval(input('How many years you would like to keep your investment?\n'
                   'Enter number of years: '))

# Ask user to enter the CURRENT INVESTMENT RATE and evaluate
rate = eval(input('What is the current rate? Enter rate in %: '))

# Summarize the investment parameters
print('Your initial investment is {}USD.\n'
      'You are investing for {} years at a steady rate of {}%.'
      .format(investment, years, rate))

# Create new value to allow work with difference from initial investment
value = investment

# Convert the investment rate to %
rate *= .01

# Loop through given number of years and calculate
for i in range(years):
    # circular reference to add up for each year performance
    value += value * rate

# Print all the user needs to know
print('Your earnings after {} years is {:.2f}USD\n'
      'That is a total of {:.2f}USD on your account.'
      .format(years, value - investment, value))
