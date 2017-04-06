# CALCULATE AREA FOR MULTIPLE DIFFERENT SHAPES

import math


def get_area(shape):
    shape = shape.lower()

    if shape == 'rectangle':
        rectangle_area()
    elif shape == 'circle':
        circle_area()
    else:
        print('Please enter rectangle or circle.')


def rectangle_area():
    length = float(input('Enter the rectangle length: '))
    width = float(input('Enter the rectangle width: '))

    area = length * width

    print('The area of the rectangle is {:.3f}.'.format(area))


def circle_area():
    radius = float(input('Enter the circle radius: '))

    area = math.pi * math.pow(radius, 2)

    print('The area of the circle is {:.3f}.'.format(area))


# run functions from within a main() function
def main():
    shape_type = input('Get area for what shape? \n'
                       '     Enter shape name: \n')

    get_area(shape_type)


# main is executed after all definitions
main()