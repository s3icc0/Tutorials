# READ ONE LINE AT A TIME USING FILES


import os


with open('mydata2.txt', mode='w', encoding='utf-8') as myFile:
    myFile.write('Some random text\nMore random text\nAnd some more')

# with open('mydata2.txt', encoding='utf-8') as myFile:
#
#     # keep track of line number
#     linenum = 1
#
#     # loop through unknown number of lines
#     while True:
#
#         # read one line up to newline
#         line = myFile.readline()
#
#         # if line has no data stop reading
#         if not line:
#             break
#
#         print('Line', linenum, ' : ', line, end='')
#
#         linenum += 1
