import logging


logging.basicConfig(
    filename='logging_employee.log',
    level=logging.INFO,
    format='%(lineno)d : '
           '%(levelname)s : '
           '%(message)s')


class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

    logging.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Ondrej', 'Sisler')
emp_2 = Employee('Verunka', 'Sislerova')
emp_3 = Employee('Baba', 'Jaga')
