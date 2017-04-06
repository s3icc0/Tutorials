# FUNCTIONS

# def for define - defines function
# values in brackets are expected to be passed to the function
def add_numbers(num1, num2):
    return num1 + num2

print('5 + 4 = ', add_numbers(5, 4))


# LOCAL VARIABLES

def assign_name():
    # name is not available outside a function as it is created locally inside
    name = 'Doug'

assign_name()
# print(name)  # this will return an error as name is not known outside


# GLOBAL VARIABLES

def change_name(name):
    name = 'Mark'

name = 'Tom'
change_name(name)  # change name from Tom to Mark
print(name)  # still not working as name is defined inside a function

# But ...
def change_name1(name):
    return 'Mark'  # what the function will return

name = 'Tom'

name = change_name1(name)  # change name from Tom to Mark

print(name)  # got it


# And ...
gbl_name = 'Sally'  # defined outside

def change_name2():
    global gbl_name  # get permission to use the variable defined outside
    gbl_name = 'Sammy'

change_name2()  # call the function (it now stands for    gbl_name = 'Sammy')

print(gbl_name)  # got it again

# Again ... not working
def get_sum(num1, num2):
    sum = num1 + num2  # this is not valid outside

print(get_sum(5, 4))  # therefore this returns 'None'
