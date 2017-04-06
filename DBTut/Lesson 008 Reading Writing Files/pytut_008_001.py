# READING AND WRITING TEXT TO A FILE


# os module help to manipulate files
import os


# with helps to properly close the file in case of crash
# locate the file
# mode='w' will override anything already in the file
# mode='a' will enable appending to the file only
# UTF-8 store text using Unicode
# define where to store the file object : as myFile
with open('mydata.txt', mode='w', encoding='utf-8') as myFile:
    # write to file
    # insert end of line as python does not do it automatically
    myFile.write('Some random text\nMore random text\nAnd some more')

# open the file for reading
with open('mydata.txt', encoding='utf-8') as myFile:
    """Reading methods:
    read() : read everything as one string until newline (no newline)
    readline() : read everything including newline as string
    readlines() : return list of lines including newline
    """
    print(myFile.read())

# check file is closed (with method closes automatically)
print(myFile.closed)

# return filename
print(myFile.name)

# return the last mode used
print(myFile.mode)

# rename the file in the OS
os.rename('mydata.txt', 'mydata2.txt')

# remove the file
os.remove('mydata2.txt')

# create directory
# os.mkdir('mydir')  # cannot create existing dir

# change path to the directory
os.chdir('mydir')

# check current directory
print('Current Directory: ', os.getcwd())

# remove directory
# 1st move backwards level up
os.chdir('..')
print('Current Directory: ', os.getcwd())
os.rmdir('mydir')
