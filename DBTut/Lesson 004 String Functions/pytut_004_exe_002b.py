# CAESAR'S CIPHER
# Receive a message and then encrypt it by shifting the
# characters by a requested amount to the right
# A becomes D, B becomes E for example
# Also decrypt the message back again

# A-Z have the numbers 65-90 in unicode
# a-z have the numbers 97-122
# You get the unicode of a character with ord(yourLetter)
# You convert from unicode to character with chr(yourNumber)

# You should check if a character is a letter and if not
# leave it as its default

import math

print('CAESAR\'S CIPHER', '\n')

# PART 1 - GET INPUT

# ask to get the string and make sure it will be a string
entryStr = str(input('Enter the text you want to make cypher using Ceasar\'s '
                     'cypher: \n'))

# ask how many characters to move
# handle letters and floats try-except
while True:
    try:  # store user input if valid
        cypShift = int(input('How many characters should the text be moved? '))
        break
    except ValueError:  # print ERROR on ValueError
        print('\n', 'ERROR : Enter a whole number', '\n')

if cypShift == 0:  # handle 0 shift
    print()
    print('Sorry - \'0\' is not doing anything, let\'s save some computing '
          'time.\n'
          'Have a nice day!')
else:

    # PART 2 - CYPHER STUFF
    # put string into list
    entryWords = entryStr.split()

    # funct to decide how to add cypher value and remain within character set
    def circleadd(charint, rangesize, rangemin, rangemax):
        # if new total value is out of range of character set
        if charint + cypShift > rangemax:
            # get remaining space in range (org(max_value) - org(current_value))
            room = rangemax - charint
            # get rid of part used to fill range from current to max value
            frommin = cypShift - room - 1
            # consume cypher value and get remainder to add from range min value
            addmod = frommin % rangesize
            # return the new unicode
            return rangemin + addmod
        # handle negative input
        elif charint + cypShift < rangemin:
            room = charint - rangemin
            tomin = int(math.fabs(cypShift)) - room - 1
            addmod = tomin % rangesize
            return rangemax - addmod
        # if new total value is within range
        else:
            # return new unicode
            return charint + cypShift

    # get the result for each character set
    def caesarin(y):
        # A - Z
        if ord(y) in range(65, 91):
            # length of the range
            series = 26
            # lowest range unicode value
            minx = 65
            # highest range unicode value
            maxx = 90
            # get the final unicode value
            return circleadd(ord(y), series, minx, maxx)
        # a - z
        elif ord(y) in range(97, 123):
            series = 26
            minx = 97
            maxx = 122
            return circleadd(ord(y), series, minx, maxx)
        # 0 - 9
        elif ord(y) in range(48, 58):
            series = 10
            minx = 48
            maxx = 57
            return circleadd(ord(y), series, minx, maxx)
        # anything else
        else:
            return ord(y)

    # placeholder for cyphred string
    caesarStr = ''

    # loop through list for each list entry
    for i in entryWords:
        # loop through list entry
        for j in i:
            # add each characters value in the entry to caesar
            caesarStr += chr(caesarin(j))

        # add spaces between words
        caesarStr += ' '

    print()
    # cyphred string
    print('Below is your cyphred string shifted by {} characters: \n'
          '{}'.format(cypShift, caesarStr))
    print()

    # PART 3 - DECYPHER STUFF
    # put string into list
    cyphredWords = caesarStr.split()

    # decide how to subtract from cyphered value and remain within character set
    # it has reverse logic of the circleadd()
    def circlesubt(charint, rangesize, rangemin, rangemax):
        if charint - cypShift < rangemin:
            room = rangemin - charint
            frommax = cypShift + room - 1
            subtmod = frommax % rangesize
            return rangemax - subtmod
        elif charint - cypShift > rangemax:
            room = rangemax - charint
            tomin = int(math.fabs(cypShift)) - room - 1
            addmod = tomin % rangesize
            return rangemin + addmod
        else:
            return charint - cypShift

    # get result for each char set, same as caesarin(), just with circlesubt()
    def caesarout(y):
        # A - Z
        if ord(y) in range(65, 91):
            # length of the range
            series = 26
            # lowest range unicode value
            minx = 65
            # highest range unicode value
            maxx = 90
            # get the final unicode value
            return circlesubt(ord(y), series, minx, maxx)
        # a - z
        elif ord(y) in range(97, 123):
            series = 26
            minx = 97
            maxx = 122
            return circlesubt(ord(y), series, minx, maxx)
        # 0 - 9
        elif ord(y) in range(48, 58):
            series = 10
            minx = 48
            maxx = 57
            return circlesubt(ord(y), series, minx, maxx)
        # anything else
        else:
            return ord(y)

    # placeholder for decyphred string
    decyphredStr = ''

    # loop through list for each list entry
    for i in cyphredWords:
        # loop through list entry
        for j in i:
            # add each characters value in the entry to caesar
            decyphredStr += chr(caesarout(j))

        # add spaces between words
        decyphredStr += ' '

    # decyphred string
    print('So it is decyphred: \n'
          '{}'.format(decyphredStr))
    print()
