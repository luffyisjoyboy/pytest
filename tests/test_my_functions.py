import time

import pytest

from source import my_functions as my_functions


def test_add():
    result = my_functions.add(2, 3)
    assert result == 5


def test_divide():
    result = my_functions.divide(3, 2)
    assert result == 1.5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        my_functions.divide(10, 0)


def test_add_strings():
    result = my_functions.add("i like", " tests")
    assert result == "i like tests"


@pytest.mark.slow
def test_very_slow():
    time.sleep(5)
    result = my_functions.add(2, 3)
    assert result == 5


@pytest.mark.skip(reason="This feature is being tested")
def test_skip_add():
    assert True


@pytest.mark.xfail(reason="we cannot divide by zero")
def test_divide_by_zero_broken():
    my_functions.divide(10, 0)
