''' Cycle through each line
that is going to be output

return number of words per line
return average length of word in the line
'''

import os

def lineList(line):

    return line.split()


def wordCount():

    return len(lineList(line))


def wordLenAvg():
    chars = 0

    for word in lineList(line):
        chars += len(word)

    return chars / wordCount()


with open('mydata2.txt', encoding='utf-8') as myFile:

    while True:
        line = myFile.readline()

        if not line:
            break

        print('{} is {} words long with an average word length of {:.2f}'
            .format(lineList(line), wordCount(), wordLenAvg())
              )
