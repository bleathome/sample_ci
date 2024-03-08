"""
This module contains tests for the `hello` module.
It includes tests to verify that the `say_hello` function behaves as expected,
ensuring that the output is correct for given inputs.
"""
from hello import say_hello


def test_say_hello():
    """
    Test the say_hello function to ensure it correctly returns a greeting.
    This test checks two things:
    1. The output is a string.
    2. The output correctly incorporates the name passed to the say_hello function.
    """
    name = "Bob"
    result = say_hello(name)

    # Check that the result is a string
    assert isinstance(result, str), "The result should be a string"

    # Check that the result contains the name
    assert f"Hello {name}" in result, f"The result should include the name '{name}'"
