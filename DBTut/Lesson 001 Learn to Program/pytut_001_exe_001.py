# Problem: Receive miles and convert to kilometers
# kilometers = miles * 1.60934
# Enter Miles 5
# 5 miles equals 8.04 kilometers

print()
print('Whole numbers miles to kilometers converter')
print()

# Ask user to enter miles and assign it to the mi variable
mi = input('Enter distance in miles: ')

# Convert mi variable to number type float to allow decimals
mi = int(mi)

# Define constant for conversion
const = 1.60934

# Define variable for converting miles to kilometers
mi_to_km = mi * const

# Print output
print('{} miles = {} kilometers'.format(mi, mi_to_km))
