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


emp_1 = Employee('Ondrej', 'Sisler', 50000)
emp_2 = Employee('Test', 'User', 10000)

my_date = datetime.date(2017, 7, 10)

print(Employee.is_workday(my_date))
