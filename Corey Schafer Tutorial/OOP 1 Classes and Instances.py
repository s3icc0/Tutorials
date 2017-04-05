""" Python Object-Oriented Programming
https://www.youtube.com/watch?v=ZDa-Z5JzLYM 
"""

class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Ondrej', 'Sisler', 50000)
emp_2 = Employee('Test', 'User', 10000)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())

print(Employee.fullname(emp_1)) # argument as self