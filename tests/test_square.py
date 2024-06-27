import pytest

from source.shapes import Square


@pytest.mark.parametrize("length, expected_area", [(5, 25), (6, 36), (4, 16)])
def test_multiple_square_areas(length, expected_area):
    assert Square(length=length).area() == expected_area


@pytest.mark.parametrize("length, expected_perimeter", [(5, 20), (3, 12), (4, 16)])
def test_multiple_perimeter(length, expected_perimeter):
    assert Square(length=length).perimeter() == expected_perimeter
