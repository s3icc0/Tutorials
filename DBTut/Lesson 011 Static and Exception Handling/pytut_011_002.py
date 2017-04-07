class Dog:

    num_of_dogs = 0

    def __init__(self, name='Unknown'):
        self.name = name

        Dog.num_of_dogs += 1

    @staticmethod
    def getnumofdogs():
        print('There are currently {} dogs'.format(Dog.num_of_dogs))


def main():

    spot = Dog('Spot')
    doug = Dog('Doug')

    spot.getnumofdogs()
    doug.getnumofdogs()
    

main()
