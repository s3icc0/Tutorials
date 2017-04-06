# GETTERS and SETTERS

# protects our objects from assigning bad fields and values
# provides improved output


class Square:

    def __init__(self, height='0', width='0'):
        self.height = height
        self.width = width

    # Getter - property will allow us to access the fields internally
    @property
    def height(self):
        print('Retrieving the height')

        # 2x_ access private field ?????
        return self.__height

    @height.setter
    def height(self, value):

        # protect height entry for bad values
        # are we testing that input is non-negative int or float?
        if value.isdigit():
            self.__height = value
        else:
            print('Please only enter numbers for height')

    @property
    def width(self):
        print('Retrieving the width')

        return self.__width

    @width.setter
    def width(self, value):

        if value.isdigit():
            self.__width = value
        else:
            print('Please only enter numbers for width')

    def getarea(self):
        return int(self.__width) * int(self.__height)

    def getperimeter(self):
        return int(self.width) * 2 + int(self.height) * 2


def main():
    asquare = Square()

    height = input('Enter height :')
    width = input('Enter width :')

    asquare.height = height
    asquare.width = width

    print('Height :', asquare.height)
    print('Width :', asquare.width)

    print('The perimeter is :', asquare.getperimeter())
    print('The area is :', asquare.getarea())

main()
