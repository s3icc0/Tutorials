# CALCULATE AREA FOR MULTIPLE DIFFERENT SHAPES

import math


def get_area(shape):
    shape = shape.lower()

    if shape == '1':
        rect_a()
    elif shape == '2':
        ask_circ()
    elif shape == '3':
        ask_tria()
    elif shape == '4':
        para_a()
    elif shape == '5':
        ask_rhom()
    elif shape == '6':
        trap_a()
    else:
        print('Please select a shape: \n')
        main()


def ask_circ():
    circ_type = str(input('What do you know about this circle? \n'
                          '  for radius type \'1\'\n'
                          '  for diameter type \'2\'\n'))

    get_area_circ(circ_type)


def get_area_circ(type):
    type = type.lower()

    if type == '1':
        circ_r_a()
    elif type == '2':
        circ_d_a()
    else:
        print('Invalid entry, please try again: \n')
        main()


def ask_tria():
    tria_type = str(input('What do you know about this triangle? \n'
                          '  for base and height type \'1\'\n'
                          '  for 3 sides type \'1\'\n'
                          '  for 2 sides and an angle between type \'2\'\n'))

    get_area_tria(tria_type)


def get_area_tria(type):
    type = type.lower()

    if type == '1':
        tria_bh_a()
    elif type == '2':
        tria_3_a()
    elif type == '2':
        tria_2a_a()
    else:
        print('Invalid entry, please try again: \n')
        main()


def ask_rhom():
    rhom_type = str(input('What do you know about this rhombus? \n'
                          '  for sides type \'1\'\n'
                          '  for diagonals type \'1\'\n'
                          '  for side and angle type \'2\'\n'))

    get_area_rhom(rhom_type)


def get_area_rhom(type):
    type = type.lower()

    if type == '1':
        rhom_sides_a()
    elif type == '2':
        rhom_diag_a()
    elif type == '2':
        rhom_trig_a()
    else:
        print('Invalid entry, please try again: \n')
        main()


def rect_a():
    length = float(input('Enter the rectangle length: '))
    width = float(input('Enter the rectangle width: '))

    area = length * width

    print()
    print('The area of the rectangle is {:.3f}.'.format(area))
    print()
    askrestart()


def circ_r_a():
    radius = float(input('Enter the circle radius: '))

    area = math.pi * math.pow(radius, 2)

    print()
    print('The area of the circle is {:.3f}.'.format(area))
    print()
    askrestart()


def circ_d_a():
    diameter = float(input('Enter the circle diameter: '))

    area = math.pi * math.pow((diameter / 2), 2)

    print()
    print('The area of the circle is {:.3f}.'.format(area))
    print()
    askrestart()


def tria_bh_a():
    base = float(input('Enter the triangle base: '))
    height = float(input('Enter the triangle height: '))

    area = (base * height) / 2

    print()
    print('The area of the triangle is {:.3f}.'.format(area))
    print()
    askrestart()


def tria_3_a():
    a_side = float(input('Enter the triangle length of side a: '))
    b_side = float(input('Enter the triangle length of side a: '))
    c_side = float(input('Enter the triangle length of side a: '))

    s_val = (a_side + b_side + c_side) / 2
    s_a = (s_val - a_side)
    s_b = (s_val - b_side)
    s_c = (s_val - c_side)
    area = math.sqrt(s_val * s_a * s_b * s_c)

    print()
    print('The area of the triangle is {:.3f}.'.format(area))
    print()
    askrestart()


def tria_2a_a():
    side1 = float(input('Enter the triangle length of 1st side: '))
    side2 = float(input('Enter the triangle length of 2nd side: '))
    angle = float(input('Enter the triangle angle between sides in degrees: '))

    area = ((side1 * side2) / 2) * math.sin(angle)

    print()
    print('The area of the triangle is {:.3f}.'.format(area))
    print()
    askrestart()


def para_a():
    base = float(input('Enter the parallelogram base length: '))
    height = float(input('Enter the parallelogram height: '))

    area = base * height

    print()
    print('The area of the parallelogram is {:.3f}.'.format(area))
    print()
    askrestart()


def rhom_sides_a():
    base = float(input('Enter the rhombus base: '))
    height = float(input('Enter the rhombus height: '))

    area = (base * height) / 2

    print()
    print('The area of the rhombus is {:.3f}.'.format(area))
    print()
    askrestart()


def rhom_diag_a():
    diag1 = float(input('Enter the rhombus length of 1st diagonal: '))
    diag2 = float(input('Enter the rhombus length of 2nd diagonal: '))

    area = (diag1 * diag2) / 2

    print()
    print('The area of the rhombus is {:.3f}.'.format(area))
    print()
    askrestart()


def rhom_trig_a():
    side = float(input('Enter the rhombus length of a side: '))
    angle = float(input('Enter the rhombus angle between sides: '))

    area = math.pow(side, 2) * math.sin(angle)

    print()
    print('The area of the rhombus is {:.3f}.'.format(area))
    print()
    askrestart()


def trap_a():
    base1 = float(input('Enter the trapezoid length of 1st base: '))
    base2 = float(input('Enter the trapezoid length of 2nd base: '))
    height = float(input('Enter the trapezoid height: '))

    area = ((base1 + base2) / 2) * height

    print()
    print('The area of the trapezoid is {:.3f}.'.format(area))
    print()
    askrestart()


def askrestart():
    restart = str(input('Do you want to calculate area for another shape?\n'
                        '     Type : \'Yes\' or \'No\''))
    deciderestart(restart)


def deciderestart(restart):
    if restart.strip().lower() in ('', ' ', 'y', 'yes', 'ok', 'go', 'start',
                                   '1', 'true'):
        print()
        main()
    elif restart.strip().lower() in ('n', 'no', 'not', 'ng', 'stop', 'quit',
                                     'exit', '0', 'false'):
        print('\n Thank you!')
    else:
        askrestart()


def main():
    shape_type = str(input('\nGet area for what shape? \n'
                           '  for rectangle type \'1\' \n'
                           '  for circle type \'2\' \n'
                           '  for triangle type \'3\' \n'
                           '  for parallelogram type \'4\' \n'
                           '  for rhombus type \'5\' \n'
                           '  for trapezoid type \'6\' \n'))

    get_area(shape_type)


main()
