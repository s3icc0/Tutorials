# TODO lang: add support for czech
# TODO lang: add support for other european languages fr, sk, sp, ge, ...
# TODO lang: add support for even more languages
# TODO lang: addition of other languages require modifying the character sets
# TODO lang: e.g. czech: a, b, c, č, d, ď, e, é, ě ...
# TODO obviously the script needs more advanced approach - need to learn more py

import math


print('CAESAR\'S CIPHER', '\n')

# global variables
# Uppercase letters
AZSeries, AZMin, AZMax = 26, 65, 90

# Lowercase letters
azSeries, azMin, azMax = 26, 97, 122

# Numbers
numSeries, numMin, numMax = 10, 48, 57

entryStr, toDoEntry, cypShift, entryWords = '', '', None, ''
cyphredWords, caesarStr, decyphredStr, toRestart = '', '', '', ''


def askentry():
    global entryStr
    entryStr = ''
    entryStr = str(input('Enter the text you want to make cypher using '
                         'Caesar\'s cypher: \n'))
    return entryStr


def askaction():
    global toDoEntry
    toDoEntry = ''
    toDoEntry = str(input('What do you want to do with the string?\n'
                          '     For both cypher and decypher - leave '
                          'empty\n'
                          '     To cypher given string type '
                          '\'c\' or \'cypher\'\n'
                          '     To decypher given string type '
                          ' \'d\' or \'decypher\'\n\n'
                          '     Your entry: \n'))
    return toDoEntry


def askshift():
    while True:
        try:
            global cypShift
            cypShift = ''
            cypShift = int(input('How many characters should the text be '
                                 'moved? \n'))
            return cypShift
        except ValueError:
            print('\n', 'ERROR : Enter a whole number', '\n')


def circleadd(char_int, range_size, range_min, range_max):
    global cypShift
    if char_int + cypShift > range_max:
        room = range_max - char_int
        frommin = cypShift - room - 1
        addmod = frommin % range_size
        return range_min + addmod
    elif char_int + cypShift < range_min:
        room = char_int - range_min
        tomin = int(math.fabs(cypShift)) - room - 1
        addmod = tomin % range_size
        return range_max - addmod
    else:
        return char_int + cypShift


def caesarin(y):
    global AZSeries, AZMin, AZMax
    global azSeries, azMin, azMax
    global numSeries, numMin, numMax
    if ord(y) in range(65, 91):
        return circleadd(ord(y), AZSeries, AZMin, AZMax)
    elif ord(y) in range(97, 123):
        return circleadd(ord(y), azSeries, azMin, azMax)
    elif ord(y) in range(48, 58):
        return circleadd(ord(y), numSeries, numMin, numMax)
    else:
        return ord(y)


def circlesubt(char_int, range_size, range_min, range_max):
    global cypShift
    if char_int - cypShift < range_min:
        room = range_min - char_int
        frommax = cypShift + room - 1
        subtmod = frommax % range_size
        return range_max - subtmod
    elif char_int - cypShift > range_max:
        room = range_max - char_int
        tomin = int(math.fabs(cypShift)) - room - 1
        addmod = tomin % range_size
        return range_min + addmod
    else:
        return char_int - cypShift


def caesarout(y):
    global AZSeries, AZMin, AZMax
    global azSeries, azMin, azMax
    global numSeries, numMin, numMax
    if ord(y) in range(65, 91):
        return circlesubt(ord(y), AZSeries, AZMin, AZMax)
    elif ord(y) in range(97, 123):
        return circlesubt(ord(y), azSeries, azMin, azMax)
    elif ord(y) in range(48, 58):
        return circlesubt(ord(y), numSeries, numMin, numMax)
    else:
        return ord(y)


def docypher():
    global entryWords
    entryWords = ''
    global caesarStr
    caesarStr = ''
    global entryStr
    global cypShift
    entryWords = entryStr.split()
    for i in entryWords:
        for j in i:
            caesarStr += chr(caesarin(j))
        caesarStr += ' '
    print('Below is your cyphred string shifted by {} characters: \n'
          '{}'.format(cypShift, caesarStr))
    print()


def dodecypher():
    global cyphredWords
    cyphredWords = ''
    global decyphredStr
    decyphredStr = ''
    global caesarStr
    cyphredWords = caesarStr.split()
    for i in cyphredWords:
        for j in i:
            decyphredStr += chr(caesarout(j))
        decyphredStr += ' '
    print('So it is decyphred: \n'
          '{}'.format(decyphredStr))
    print()
    askrestart()
    deciderestart()


def decideaction():
    global toDoEntry
    if toDoEntry.strip().lower() in ('c', 'cyp', 'cypher'):
        docypher()
    elif toDoEntry.strip().lower() in ('d', 'decyp', 'decypher',
                                       'de-cypher'):
        dodecypher()
    elif toDoEntry.strip().lower() in ('', ' ', None, 'all', 'both'):
        docypher()
        dodecypher()
    else:
        print('Let\'s try again ... \n')
        main()


def play():
    global cypShift
    if cypShift < 1:
        print()
        print('Sorry - \'0\' is not doing anything, let\'s save some '
              'computing time.\n'
              'Have a nice day!')
        print()
    else:
        decideaction()


def askrestart():
    global toRestart
    toRestart = ''
    toRestart = str(input('Do you want to enter new string?\n'
                          '     Type : \'Yes\' or \'No\''))
    return toRestart


def deciderestart():
    global toRestart
    if toRestart.strip().lower() in ('', ' ', 'y', 'yes', 'ok', 'go', 'start',
                                     '1', 'true'):
        print()
        main()
    elif toRestart.strip().lower() in ('n', 'no', 'not', 'ng', 'stop', 'quit',
                                       'exit', '0', 'false'):
        print('\n Thank you!')
    else:
        askrestart()


def main():
    askentry()
    askaction()
    askshift()
    play()


main()
