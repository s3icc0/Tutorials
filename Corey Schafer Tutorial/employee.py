import logging

# __name__ will = to module name
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter(
    '%(lineno)d : '
    '%(levelname)s : '
    '%(name)s : '
    '%(message)s')

# file handler
file_handler = logging.FileHandler('logging_employee.log')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info('Created Employee: {} - {}'
                     .format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@company.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Ondrej', 'Sisler')
emp_2 = Employee('Verunka', 'Sislerova')
emp_3 = Employee('Baba', 'Jaga')
