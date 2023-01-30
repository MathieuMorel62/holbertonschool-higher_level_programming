#!/usr/bin/python3
""" Class representing a Square. """


class Square:
    """ Class representing a Square. """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a Square object with the given size and position.
        :param size (int): The size of the Square (default: 0)
        :param position (tuple): The position of the Square (default: (0, 0))
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter for the size attribute.
        :return: The size of the Square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for the size attribute
        :param value: Value to set the size of the square to
        :raise TypeError: If value is not an integer
        :raise TypeError: If value is less than 0
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise TypeError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """
        Getter for the position attribute.
        :return: The position of the Square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter for the position attribute
        :param value: Value to set the position of the square
        :raise TypeError: If value is not a tuple of 2 positive integers
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integer")
        elif type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integer")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integer")
        else:
            self.__position = value

    def area(self):
        """
        Method to calculate the area of the square
        :return: Area of the square
        """
        return self.size ** 2

    def my_print(self):
        """ Prints the Square object to the console. """
        if self.size == 0:
            print()
        else:
            for row in range(self.position[1]):
                print()
            for i in range(self.size):
                for space in range(self.position[0]):
                    print(" ", end="")
                for j in range(self.size):
                    print("#", end="")
                print()

    def __str__(self):
        """
        Method to return a string representation of the square
        :return: String representation of the square
        """
        res = []
        if self.size == 0:
            res.append("")
        else:
            for i in range(self.position[1]):
                res.append("")
            for i in range(self.size):
                res.append(" " * self.position[0] + "#" * self.size)
        return "\n".join(res)
