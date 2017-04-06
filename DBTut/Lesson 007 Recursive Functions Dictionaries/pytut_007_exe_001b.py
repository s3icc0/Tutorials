# CUSTOMER LIST

# My approach - it works but is way more complicated then Derek's version

# Create an array of customer dictionaries
""" Output should look like this:
Q: Enter Customer (Yes/No) : y
A: Enter Customer Name : Derek Banas
Q: Enter Customer (Yes/No) : y
A: Enter Customer Name : Sally Smith
Q: Enter Customer (Yes/No) : n
Result:
Derek Banas
Sally Smith
"""


# Ask to enter the customer (Yes/No)
def askcreate():
    question = input('Enter Customer (Yes/No) : ')
    decideaction(question)


# Decision (enter/print)
def decideaction(decision):
    if decision.lower() in ('yes', 'y', ''):
        getname()
    elif decision.lower() in ('no', 'n', 'not', 'result', 'results'):
        showcustomers()


# Get name
def getname():
    name = input('Enter Customer Name : ')
    print('Name to be appended : ', name)
    addname(name)


# Split and append to list as dictionary
def addname(name):
    fname, lname = name.split()
    customers.append({'fName': fname, 'lName': lname})
    main()


# Print results
def showcustomers():
    for i in customers:
        print(i['fName'], i['lName'])


def main():
    global customers
    askcreate()


customers = []

main()
