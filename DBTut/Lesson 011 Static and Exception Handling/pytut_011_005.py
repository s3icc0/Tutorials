class dognameerror(Exception):

    def __init(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)


try:
    dogname = input('What is your dogs name? ')

    if any(char.isdigit() for char in dogname):

        raise dognameerror

except dognameerror:
    print('Your dogs name can\'t contain a number')
