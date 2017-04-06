# TODO PEP-8

import random  # import a random number generator
import sys  # this is required for input
import os  # this allows to work with files on the drive?

  # single line comment (space space hash space)
'''multiline comment using 3x
still the same comment'''

print('Hello World!')  # print a text string within '' or ""

name = 'Ondřej'  # string definition
print(name)
print()  # new line

print('Data types: Numbers, Strings, Lists, Tuples, Dictionaries (Maps)')
print()

print('MATH')
print('Algorythmical operators:')
print('5 + 2 =', 5 + 2)  # notice merging of the strings by using a colon
print('5 - 2 =', 5 - 2)
print('5 * 2 =', 5 * 2)
print('5 / 2 =', 5 / 2)
print('5 % 2 =', 5 % 2)  # % for modulus (returns remainder after division
print('5 ** 2 =', 5 ** 2)  # ** make an exponent
print('5 // 2 =', 5 // 2)  # divide without anything left

print('Order of math ops:')
print('1 + 2 - 3 * 2 = ', 1 + 2 - 3 * 2)
print('(1 + 2 - 3) * 2 = ', (1 + 2 - 3) * 2)
print('\n' * 2)  # so we need to repeat whatever is our result

print('STRINGS')
quote = '\"Always remember you are unique'  # use backslash \ to enable special characters

multi_line_quote = ''' just
like everyone else'''  # use 3 quotes ''' to start and end multiline string

print('%s %s %s' % ('I like the quote', quote, multi_line_quote))
  # merge 3 strings by using 3x %s and then calling it using % '''
print()
print('I don\'t like ', end='')  # use end='' to surpress breaking lines
print('newlines')
print()

print('LISTS')
grocery_list = ['Juice', 'Tomatoes', 'Potatoes',
                'Bananas']  # define a list by using []

print('First Item: ', grocery_list[0])  # call list item at position 0

grocery_list[0] = 'Green Juice'  # change list item at position 0
print('First Item after change: ', grocery_list[0])

print(grocery_list[1:3])  # only show item at positions 1 to 2

other_events = ['Wash Car', 'Pick Up Kids',
                'Cash Check']

to_do_list = [other_events, grocery_list]  # merge two lists in new string
print(to_do_list)

print('2nd item from 2nd list: ', (to_do_list[1][1]))  # call fro merged string lists

grocery_list.append('Onions')  # append an item to the list
print(to_do_list)

grocery_list.insert(1, 'Pickle')  # insert an item to certain position in the list
print('Pickle added to 2nd position: ', grocery_list)

grocery_list.remove('Pickle')  # remove an item from the list
print('Removed Pickle: ', grocery_list)

grocery_list.sort()  # sort the list lowest to highest (or alphabetically)
print('Sorted list: ', grocery_list)

grocery_list.reverse()  # reverse the order of items in the list
print('Reversed list: ', grocery_list)

del grocery_list[4]  # delete item at 4th position in the list
print('Position 4 Item deleted: ', to_do_list)

to_do_list2 = other_events + grocery_list
print(to_do_list2)

print('Length of the two lists combined into new list: ', len(to_do_list2))  # length of the list
print('The highest item: ', max(to_do_list2))  # highest or maximum item in the list
print('The lowest item: ', min(to_do_list2))  # lowest ...
print()

print('TUPLES')  # similar to lists but cannot be changed
  # in fact you can change by converting to list, doing changes and converting back

pi_tuple = (3, 1, 4, 1, 5, 9)  # tuple

tuple_to_list = list(pi_tuple)  # tuple to list
list_to_tuple = tuple(tuple_to_list)  # list to tuple

print('Length of the tuple: ', len(tuple_to_list))  # get length
print('Min value of the tuple: ', min(tuple_to_list))  # get min value
print('Max value of the tuple: ', max(tuple_to_list))  # get max value
print()

print('DICTIONARIES / MAPS')
print('Dictionary is a list of values with the unique key for each value')
print('Dictionaries cannot be joined together as lists')

nicknames_map = {  # curly brackets
    'Ondřej': 's3icc0',  # key : value
    'Tomáš': 'bAdys',
    'Martin': 'lanza',
    'Vlado': 'bubulak'}

print(nicknames_map['Tomáš'])  # print the value to the given key

del nicknames_map['Vlado']  # delete the entry defined by the key
nicknames_map['Martin'] = 'lanýž'  # change the value of the given key

print('Number of nicknames: ', len(nicknames_map))

print(nicknames_map.get('Ondřej'))
print('Keys: ', nicknames_map.keys())
print('Values: ', nicknames_map.values())
print()

print('CONDITIONALS')
print('Statements: if else elif \n')
print('Conditions: \n'
      'Equal to == \n'
      'Not equal to != \n'
      'Greater than > (Alt + 62) \n'
      'Greater than or equal to >= \n'
      'Less then < \n'
      'Less then or equal to <= \n')
print('Logical operators: and or not \n')

age = 31
print('Your age is', age)
if age > 16:
    print('You are old enough to drive')
else:
    print('You are not old enough to drive')

if age >= 21:
    print('You are old enough to drive a tractor trailer')
elif age >= 16:
    print('You are not old enough to drive')
else:
    print('You are not old enough to drive')

if (age >= 15) and (age < 18):
    print('You are an adolescent')
elif (age >= 18) and (age < 60):
    print('You are an adult')
elif age >= 60:
    print('You are too old to start python')
elif age == 0:
    print('You an infant')
else:
    print('You are a kid')
print()

print('LOOPS')

print('FOR loops')

for x in range(0, 10):
    print(x, ' ', end='')  # for each x(0-9) print x 1*space and dont break line
print()

for x in grocery_list:
    print(x, ', ', end='')
print()

for x in [2, 4, 6, 8, 10]:
    print(x, ' ', end='')
print()

for x in [2, 4, 6, 8, 10]:
    if x < 10:
        print(x, ', ', end='')
    else:
        print(x)
print()

num_list = [[1, 2, 3], [10, 20, 30], [100, 200, 300]]

for x in range(0, 3):  # cycle through 3 lists (0, 1 and 2)
    for y in range(0, 3):  # cycle through items in the lists
        print(num_list[x][y])
print()

print('WHILE loops')

random_num = random.randrange(0, 100)  # define random number using the random module and random within a range

while random_num != 15:
    print(random_num)
    random_num = random.randrange(0, 100)
print()

i = 0

while i <= 20:
    if i % 2 == 0 and i != 0:
        print(i)
    elif i == 17:
        break  # break off the loop and don't go further if this is true
    else:
        i += 1  # i = i + 1     meaning 1 is added to i
        continue  # and looping again

    i += 1  # why we need to increment here when this is not part of the loop ???
print()

print()

print('FUNCTIONS')

def addnumber(firstnum, lastnum):  # define addition on 1st and 2nd number
    sumnum = firstnum + lastnum  # sumnum only exist outside of the function
    return sumnum  # we need to return something from the function

print(addnumber(1, 4))  # just print the output

string = addnumber(2, 5)  # define the result of the function as a string
print(string)

print('User input')

print(' What is your name?', '\n', 'Christ just enter the name so we can continue!!!')
'''  temporarily commented out not to block the execution
name = sys.stdin.readline()  # standard input
'''
name = 'Ondřej'  # used instead of standard input
print('Hello', name)
print()

print('Long strings')

long_string = 'i\'ll catch you if you fall - The Floor'
print('This is a long string: ', long_string)
print(long_string[0:4])  # print characters 0, 1, 2 and 3 (first 4)
print(long_string[-5:])  # print last 5 chars
print(long_string[:-5])  # print without last 5 chars
print(long_string[:4] + ' be there')  # concatenate two strings
print('%c is my %s letter and my number %d number is %.5f'
      % ('X', 'favorite', 1, 13))  # % to call the placeholders
'''
%c - character placeholder
%s - string placeholder
%d - number placeholder
%.5f - ???? something to say 5 decimal places - formating
'''

print(long_string.capitalize())  # capitalize first character of the string
print(long_string.find('Floor'))  # case sensitive find starting position of () withing a string
print(long_string.isalpha())  # returns TRUE if all chars in the string are letters
print(long_string.isalnum())  # returns TRUE if all chars in the string are numbers
print(len(long_string))  # returns length
print(long_string.replace('Floor', 'Ground'))  # replaces Floor with Ground
print(long_string.replace('ground', 'Floor'))  # it's not case sensitive
print(long_string.strip())  # strip white space (there is no whitespace at beginning or end in long_string

quote_list = long_string.split(' ')  # convert into list removing spaces
print(quote_list)
print()

print('FILE I/O')

test_file = open('test.txt', 'wb')  # open (and create) file and allow write with 'wb'
  # use 'ab+' to Read & Append to File
print(test_file.mode)  # returns the mode enabled on the file
print(test_file.name)  # returns the file name

test_file.write(bytes('Write me to the file\n', 'UTF-8'))  # write to file
test_file.close()  # close the file

test_file = open('test.txt', 'r+')  # open the file and enable Read & Write
text_in_file = test_file.read()  # read contents of the file
print(text_in_file)
test_file.close()  # close the file

os.remove('test.txt')  # call os module and delete the file
print('File', test_file.name, 'has been removed')
print()

print('OBJECTS')

class Animal:  # blueprint Animal object
    __name = ''  # aids or attributes, using None instead of '' is also possible
    __height = 0  # __ means the attributes are going to be private
    __weight = 0  # to change and get the attributes we need function inside the class
    __sound = 0

    def __init__(self, name, height, weight, sound):  # constructor __init__
        self.__name = name  # initialise attributes
        self.__height = height
        self.__weight = weight
        self.__sound = sound

    def set_name(self, name):  # setter is required to allow usage outside of the class
        self.__name = name
    def get_name(self):  # getter is required to allow usage outside of the class
        return self.__name
    def set_height(self, height):  # setter
        self.__height = height
    def get_height(self):  # getter
        return self.__height
    def set_weight(self, weight):  # setter
        self.__weight = weight
    def get_weight(self):  # getter
        return self.__weight
    def set_sound(self, sound):  # setter
        self.__sound = sound
    def get_sound(self):  # getter
        return self.__sound
    def get_type(self):  # one more to be able to return class name (type)
        print('Animal')
    def toString(self):  # allow printing to the screen
        return '{} is {} cm tall and {} kilograms and say {}'.format(self.__name,
                                                                     self.__height,
                                                                     self.__weight,
                                                                     self.__sound)
          # the {} represents where I want the information to go'''
          # order matters
          # setters and getters are not required now as we work inside the class

# this is based later in the lesson - my changed code to print on one line separated by commas
    def multiple_sounds_separated(self, how_many=None):
        if how_many is None:
            print(self.get_sound())
        else:
            i = 0
            while i < how_many:
                if i == how_many:
                    print(self.get_sound())
                else:
                    print(self.get_sound(), ' ', end='')
                    i += 1
                    continue

                i += 1


cat = Animal('Whiskers', 33, 10, 'Meow')  # create cat in Animal object
print(cat.toString())  # print cat as the prepared string
print(cat.get_name())  # print cat name using the getter

class Dog(Animal):  # inheritance of class properties
    __owner = ''  # Dog class has all properties of Animal class + owner

    def __init__(self, name, height, weight, sound, owner):  # init the attributes with owner
        self.__owner = owner  # define the missing owner
        super(Dog, self).__init__(name, height, weight, sound)  # add the missing attributes from super class Animal

    def set_owner(self, owner):  # missing owner setter
        self.__owner = owner
    def get_owner(self):  # missing owner getter
        return self.__owner

    def get_type(self):  # allow getting the Dog type
        print('Dog')

    # overide the existing super class string toString
    def toString(self):
        return '{} is {} cm tall and {} kilograms and say {}. His owner is {}.'.format(self.get_name(),
                                                                                       self.get_height(),
                                                                                       self.get_weight(),
                                                                                       self.get_sound(),
                                                                                       self.__owner)  # add the owner

    def multiple_sounds(self, how_many=None):  # none means the value will not be required
        if how_many is None:
            print(self.get_sound())  # do sound 1x
        else:
            print(self.get_sound() * how_many)  # do sound multiple times

spot = Dog('Spot', 53, 27, 'Ruff', 'Ondřej')  # create object spot in Dog class

print(spot.toString())  # object spot printed through toString method
spot.multiple_sounds(4)  # print Dog class built in multiple_sounds
print()

print('POLYMORPHISM')

class AnimalTesting:
    def get_type(self, animal):
        animal.get_type()

test_animals = AnimalTesting()

test_animals.get_type(cat)
test_animals.get_type(spot)

spot.multiple_sounds_separated(4)  # print custom Animal class built in multiple_sounds_separated