import math

from source.shapes import Circle


class TestCircle:
    def setup_method(self, method):
        self.circle = Circle(radius=10)

    def teardown_method(self, method):
        pass

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius**2

    def test_perimeter(self):
        result = self.circle.perimeter()
        assert result == 2 * math.pi * self.circle.radius
