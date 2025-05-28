#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        """
        Initializes a new Shoe object.

        Args:
            brand (str): The brand of the shoe.
            size (int): The size of the shoe.
        """
        self._brand = brand
        self._size = 0
        self.size = size
        self._condition = "New"

    @property
    def brand(self):
        """
        Getter for the brand of the shoe.
        """
        return self._brand

    @brand.setter
    def brand(self, value):
        """
        Setter for the brand of the shoe.
        """
        self._brand = value

    @property
    def size(self):
        """
        Getter for the size of the shoe.
        """
        return self._size

    @size.setter
    def size(self, value):
        """
        Setter for the size of the shoe.
        Validates that the size is an integer.
        """
        if not isinstance(value, int):
            print("size must be an integer")
        else:
            self._size = value

    @property
    def condition(self):
        """
        Getter for the condition of the shoe.
        """
        return self._condition

    @condition.setter
    def condition(self, value):
        """
        Setter for the condition of the shoe.
        """
        self._condition = value

    def cobble(self):
        """
        Repairs the shoe and sets its condition to 'New'.
        """
        print("Your shoe is as good as new!")
        self.condition = "New"