""" Python Object-Oriented Programming
https://www.youtube.com/watch?v=ZDa-Z5JzLYM 
"""
"""methods
regular - automatically passes the instance as first argument called self
class - automatically passes the class as first instance called cls
static - does not pass anything"""

import datetime


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

    # @classmethod decorator will make self to pass the class name
    # cls is class as self (standard naming)
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    # alternative instance constructor from string
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday == 6:
            return False
        return True


# Inherited from Employee
class Developer(Employee):
    # all of the functionality is inherited
    # pass
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        # take the arguments from the higher class
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())
        print()


dev_1 = Developer('Ondrej', 'Sisler', 50000, 'Python')
dev_2 = Developer('Test', 'User', 10000, 'Java')
mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(dev_1.email)
print(dev_1.prog_lang)

print(mgr_1.email)

mgr_1.print_emps()

mgr_1.add_emp(dev_2)

mgr_1.print_emps()

mgr_1.remove_emp(dev_1)

mgr_1.print_emps()

# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)


# help function to analyze the function
# print(help(Developer))

# my_date = datetime.date(2017, 7, 10)
# print(Employee.is_workday(my_date))

print(isinstance(mgr_1, Developer))
print(issubclass(Manager, Developer))
