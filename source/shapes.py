import math


class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius) -> None:
        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length, width) -> None:
        self.length = length
        self.width = width

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Rectangle):
            return False
        return self.width == value.width and self.length == value.length

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Square(Rectangle):
    def __init__(self, length) -> None:
        super().__init__(length, length)
