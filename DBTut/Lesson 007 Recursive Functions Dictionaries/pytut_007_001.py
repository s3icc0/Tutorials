# DICTIONARIES
# List is organized by pairs of:         index : value
# Dictionary is organized by pairs of:   key : value
# Dictionary is non-sequential (the order is not defined)

# create dictionary
derekDict = {'fName': 'Derek', 'lName': 'Banas',
             'address': '123 Main St'}

# print value of a key
print('My Name:', derekDict['fName'])

# change a value of a key
derekDict['address'] = '215 North St'

# the whole dictionary may not be printed in same order as created
print(derekDict)

# add new key : value pair
derekDict['city'] = 'Pittsburg'

# check if key exists
print('Is there a city? ', 'city' in derekDict)

# get list of values
print(derekDict.values())
print()

# get list of keys
print(derekDict.keys())
print()

# get both keys and values using for loop
for k, v in derekDict.items():
    print(k, v)

print()

# get a key value or return default
print(derekDict.get('mName', 'Not here'))
print()

# delete a key (and associated value)
del derekDict['fName']

# loop in keys
for i in derekDict:
    print(i)

print()

# clear dictionary
derekDict.clear()
print()

# create list able to hold dictionaries
# employees list
employees = []

# ask of the two variables (split input to separate)
# TODO fix only one string entered with an exception
fName, lName = input('Enter Employee Name: ').split()

# append the dictionary to the list
# reference variables obtained from user
employees.append({'fName': fName, 'lName': lName})

print(employees)






















