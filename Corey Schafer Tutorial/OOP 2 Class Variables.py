""" Python Object-Oriented Programming
https://www.youtube.com/watch?v=ZDa-Z5JzLYM 
"""

class Employee:

    num_of_emps = 0
    raise_amount = 1.04 # class variable

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        # class variable applied to the class
        Employee.num_of_emps += 1 # increase with every employee

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # class variable applied to an instance
        self.pay = int(self.pay * self.raise_amount)


print(Employee.num_of_emps)

emp_1 = Employee('Ondrej', 'Sisler', 50000)
emp_2 = Employee('Test', 'User', 10000)

print(Employee.num_of_emps)

# print(emp_1.__dict__) # print instance name space
# print(Employee.__dict__) # print instance name space

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)
#
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
#
# emp_1.raise_amount = 1.05
#
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
#
# print(emp_1.__dict__)

