# tests/test_example.py
# pylint: disable=missing-docstring
# pylint: disable=too-few-public-methods
from hello import say_hello
def test_example():
    result = say_hello()
    assert isinstance(result) == str
