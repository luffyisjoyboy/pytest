# we can use this to define global fixtures

import pytest
from source.shapes import Rectangle


@pytest.fixture
def my_rectangle():
    return Rectangle(10, 20)


@pytest.fixture
def weird_rectangle():
    return Rectangle(5, 6)
