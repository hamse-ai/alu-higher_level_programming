#!/usr/bin/python3
"""a class for a Square with size"""


class Square:
    """Square class represents a square with size."""

    def __init__(self, size=0):
        """Initialize the square with size.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If `size` is not an integer.
            ValueError: If `size` is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    