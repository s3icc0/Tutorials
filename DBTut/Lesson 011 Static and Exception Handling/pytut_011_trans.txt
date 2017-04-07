# YouTube : https://www.youtube.com/watch?v=7vbgD-3s-w4

# ---------- STATIC METHODS ----------

# Static methods allow access without the need to initialize
# a class. They should be used as utility methods, or when
# a method is needed, but it doesn't make sense for the real
# world object to be able to perform a task

class Sum:
    # You use the static method decorator to define that a
    # method is static
    @staticmethod
    def getSum(*args):
        sum = 0

        for i in args:
            sum += i

        return sum


def main():
    # Call a static method by proceeding it with its class
    # name
    print("Sum :", Sum.getSum(1, 2, 3, 4, 5))


main()


# ---------- STATIC VARIABLES ----------
# Fields declared in a class, but outside of any method
# are static variables. There value is shared by every
# object of that class

class Dog:
    # This is a static variable
    num_of_dogs = 0

    def __init__(self, name="Unknown"):
        self.name = name

        # You reference the static variable by proceeding
        # it with the class name
        Dog.num_of_dogs += 1

    @staticmethod
    def getNumOfDogs():
        print("There are currently {} dogs".format(Dog.num_of_dogs))


def main():
    spot = Dog("Spot")

    doug = Dog("Doug")

    spot.getNumOfDogs()


main()


# ---------- MODULES ----------
# Your Python programs will contain a main program that
# includes your main function. Then you will create many
# modules in separate files. Modules also end with .py
# just like any other Python file

# ————— sum.py —————
def getSum(*args):
    sum = 0

    for i in args:
        sum += i

    return sum


# ————— End of sum.py —————

# You can import by listing the file name minus the py
import sum

# Get access to functions by proceeding with the file
# name and then the function you want
print("Sum :", sum.getSum(1, 2, 3, 4, 5))

# ---------- FROM ----------

# You can use from to copy specific functions from a module
# You can use from sum import * to import all functions
# You can import multiple functions by listing them after
# import separated by commas
from sum import getSum

# You don't have to reference the module name now
print("Sum :", getSum(1, 2, 3, 4, 5))

# ---------- EXCEPTION HANDLING ----------
# Exceptions are triggered either when an error occurs
# or when you want them to.

# We use exceptions are used to handle errors, execute
# specific code when code generates something out of
# the ordinary, to always execute code when something
# happens (close a file that was opened),

# When an error occurs you stop executing code and jump
# to execute other code that responds to that error

# Let's handle an IndexError exception that is
# triggered when you try to access an index in a list
# that doesn't exist

# Surround a potential exception with try
try:
    aList = [1, 2, 3]

    print(aList[3])

# Catch the exception with except followed by the
# exception you want to catch

# You can catch multiple exceptions by separating them
# with commas inside parentheses
# except (IndexError, NameError):
except IndexError:
    print("Sorry that index doesn't exist")

# If the exception wasn't caught above this will
# catch all others
except:
    print("An unknown error occurred")


# ---------- CUSTOM EXCEPTIONS ----------

# Lets trigger an exception if the user enters a
# name that contains a number

# Although you won't commonly create your own exceptions
# this is how you do it

# Create a class that inherits from Exception
class DogNameError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


try:
    dogName = input("What is your dogs name : ")

    if any(char.isdigit() for char in dogName):
        # Raise your own exception
        # You can raise the built in exceptions as well
        raise DogNameError

except DogNameError:
    print("Your dogs name can't contain a number")

# ---------- FINALLY & ELSE ----------
# finally is used when you always want certain code to
# execute whether an exception is raised or not

num1, num2 = input("Enter to values to divide : ").split()

try:
    quotient = int(num1) / int(num2)
    print("{} / {} = {}".format(num1, num2, quotient))

except ZeroDivisionError:
    print("You can't divide by zero")

# else is only executed if no exception was raised
else:
    print("You didn't raise an exception")

finally:
    print("I execute no matter what")

# ---------- PROBLEM EXCEPTIONS & FILES ----------
# 1. Create a file named mydata2.txt and put data in it
# 2. Using what you learned in part 8 and Google to find
# out how to open a file without with try to open the
# file in a try block
# 3. Catch the FileNotFoundError exception
# 4. In else print the file contents
# 5. In finally close the file
# 6. Try to open the nonexistent file mydata3.txt and
# test to see if you caught the exception

try:
    myFile = open("mydata2.txt", encoding="utf-8")

# We can use as to access data and methods in the
# exception class
except FileNotFoundError as ex:
    print("That file was not found")

    # Print out further data on the exception
    print(ex.args)

else:
    print("File :", myFile.read())
    myFile.close()

finally:
    print("Finished Working with File")
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
196
197
198
199
200
201
202
203
204
205
206
207
208
209


# ---------- STATIC METHODS ----------

# Static methods allow access without the need to initialize
# a class. They should be used as utility methods, or when
# a method is needed, but it doesn't make sense for the real
# world object to be able to perform a task

class Sum:
    # You use the static method decorator to define that a
    # method is static
    @staticmethod
    def getSum(*args):
        sum = 0

        for i in args:
            sum += i

        return sum


def main():
    # Call a static method by proceeding it with its class
    # name
    print("Sum :", Sum.getSum(1, 2, 3, 4, 5))


main()


# ---------- STATIC VARIABLES ----------
# Fields declared in a class, but outside of any method
# are static variables. There value is shared by every
# object of that class

class Dog:
    # This is a static variable
    num_of_dogs = 0

    def __init__(self, name="Unknown"):
        self.name = name

        # You reference the static variable by proceeding
        # it with the class name
        Dog.num_of_dogs += 1

    @staticmethod
    def getNumOfDogs():
        print("There are currently {} dogs".format(Dog.num_of_dogs))


def main():
    spot = Dog("Spot")

    doug = Dog("Doug")

    spot.getNumOfDogs()


main()


# ---------- MODULES ----------
# Your Python programs will contain a main program that
# includes your main function. Then you will create many
# modules in separate files. Modules also end with .py
# just like any other Python file

# ————— sum.py —————
def getSum(*args):
    sum = 0

    for i in args:
        sum += i

    return sum


# ————— End of sum.py —————

# You can import by listing the file name minus the py
import sum

# Get access to functions by proceeding with the file
# name and then the function you want
print("Sum :", sum.getSum(1, 2, 3, 4, 5))

# ---------- FROM ----------

# You can use from to copy specific functions from a module
# You can use from sum import * to import all functions
# You can import multiple functions by listing them after
# import separated by commas
from sum import getSum

# You don't have to reference the module name now
print("Sum :", getSum(1, 2, 3, 4, 5))

# ---------- EXCEPTION HANDLING ----------
# Exceptions are triggered either when an error occurs
# or when you want them to.

# We use exceptions are used to handle errors, execute
# specific code when code generates something out of
# the ordinary, to always execute code when something
# happens (close a file that was opened),

# When an error occurs you stop executing code and jump
# to execute other code that responds to that error

# Let's handle an IndexError exception that is
# triggered when you try to access an index in a list
# that doesn't exist

# Surround a potential exception with try
try:
    aList = [1, 2, 3]

    print(aList[3])

# Catch the exception with except followed by the
# exception you want to catch

# You can catch multiple exceptions by separating them
# with commas inside parentheses
# except (IndexError, NameError):
except IndexError:
    print("Sorry that index doesn't exist")

# If the exception wasn't caught above this will
# catch all others
except:
    print("An unknown error occurred")


# ---------- CUSTOM EXCEPTIONS ----------

# Lets trigger an exception if the user enters a
# name that contains a number

# Although you won't commonly create your own exceptions
# this is how you do it

# Create a class that inherits from Exception
class DogNameError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


try:
    dogName = input("What is your dogs name : ")

    if any(char.isdigit() for char in dogName):
        # Raise your own exception
        # You can raise the built in exceptions as well
        raise DogNameError

except DogNameError:
    print("Your dogs name can't contain a number")

# ---------- FINALLY & ELSE ----------
# finally is used when you always want certain code to
# execute whether an exception is raised or not

num1, num2 = input("Enter to values to divide : ").split()

try:
    quotient = int(num1) / int(num2)
    print("{} / {} = {}".format(num1, num2, quotient))

except ZeroDivisionError:
    print("You can't divide by zero")

# else is only executed if no exception was raised
else:
    print("You didn't raise an exception")

finally:
    print("I execute no matter what")

# ---------- PROBLEM EXCEPTIONS & FILES ----------
# 1. Create a file named mydata2.txt and put data in it
# 2. Using what you learned in part 8 and Google to find
# out how to open a file without with try to open the
# file in a try block
# 3. Catch the FileNotFoundError exception
# 4. In else print the file contents
# 5. In finally close the file
# 6. Try to open the nonexistent file mydata3.txt and
# test to see if you caught the exception

try:
    myFile = open("mydata2.txt", encoding="utf-8")

# We can use as to access data and methods in the
# exception class
except FileNotFoundError as ex:
    print("That file was not found")

    # Print out further data on the exception
    print(ex.args)

else:
    print("File :", myFile.read())
    myFile.close()

finally:
    print("Finished Working with File")
