import math
class Shape:
    def __init__ (self, name):
        self.name = name
    def area(self):
        raise NotImplementedError("Try Again")
class Rectangle(Shape):
    def __init__ (self, length, width, name = "Rectangle"):
        super(). __init__(name)
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
class Circle(Shape):
    def __init__ (self, radius, name = "Circle"):
        super(). __init__(name)
        self.radius = radius
    def area(self):
        return math.pi * self.radius * self.radius

