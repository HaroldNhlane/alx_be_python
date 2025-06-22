# polymorphism_demo.py

import math

class Shape:
    """
    Base class for all shapes.
    Defines an 'area' method that should be overridden by derived classes.
    """
    def area(self):
        """
        Calculates the area of the shape.
        This method must be overridden by concrete shape classes.
        Raises:
            NotImplementedError: If the method is not overridden in a derived class.
        """
        raise NotImplementedError("Subclasses must implement the 'area' method.")

class Rectangle(Shape):
    """
    Derived class representing a rectangle, inheriting from Shape.
    Attributes:
        length (int or float): The length of the rectangle.
        width (int or float): The width of the rectangle.
    """
    def __init__(self, length: float, width: float):
        """
        Initializes a new Rectangle instance.

        Args:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Overrides the area method to calculate the area of the rectangle.

        Returns:
            float: The area of the rectangle (length * width).
        """
        return self.length * self.width

class Circle(Shape):
    """
    Derived class representing a circle, inheriting from Shape.
    Attributes:
        radius (int or float): The radius of the circle.
    """
    def __init__(self, radius: float):
        """
        Initializes a new Circle instance.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Overrides the area method to calculate the area of the circle.
        Uses math.pi for the value of pi.

        Returns:
            float: The area of the circle (pi * radius^2).
        """
        return math.pi * (self.radius ** 2)