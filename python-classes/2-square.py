#!/usr/bin/python3
"""a class for a Square" wwith size"""


class Square:
    """Square class represents a square with size."""
    def __init__(self, size):
        """Initialize the square with size."""
        self.__size = size
        try:
            type(size) == int
        except TypeError: 
            print("size must be an intege")
        except ValueError:
            print("size must be >= 0")
    
    pass
