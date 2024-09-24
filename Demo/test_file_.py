import pytest


def test_file1_method1():
    x = 5
    y = 6
    assert x + 1 == y, "test failed"
    assert x == y, "test failed"


def test_file1_method2():
    x = 5
    y = 6
    assert x + 1 == y, "X + 1 is not equal to y so the test failed!"


def test_file1_method1():
    expected = True
    actual = False
    assert expected == actual, "Error Occured expected value: " + str(
        expected) + " is not matching with the actual value: " + str(actual)  # is an assertion failure.

