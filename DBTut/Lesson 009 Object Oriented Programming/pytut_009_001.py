# OBJECT ORIENTED PROGRAMMING

"""
Real World Objects : Attribute & Capabilities

DOG
Attributes (Fields / Variables) : Height, Weight, Favorite Food
Capabilities (Methods / Functions): Run, Walk, Eat
"""

# Object is created for a template called Class
# Classes defines Attributes and Capabilities of an Object


class Dog:
    # __init__ : initial equation
    # self is used to enable refering to 'Myself'
    # attributes with default values e.g. Dog with no name
    def __init__(self, name='', height=0, weight=0):
        # define attributes
        self.name = name
        self.height = height
        self.weight = weight

    # define methods
    def run(self):
        print('{} the dog runs'.format(self.name))

    def eat(self):
        print('{} the dog eats'.format(self.name))

    def bark(self):
        print('{} the dog barks'.format(self.name))


def main():

    # create Dog with name Spot (height 66, width 26)
    spot = Dog('Spot', 66, 26)

    # make the spot bark
    spot.bark()

    # create new John Doe Dog
    bowser = Dog()

    # unknown Dog barking
    bowser.bark()

    # name a Dog
    bowser.name = 'Bowser'

    bowser.run()


main()
