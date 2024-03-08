"""test example is a script to test the code of the hello module"""
from hello import say_hello
def test_say_hello():
    """this test check that the function returns a string containing bob"""
    result = say_hello("bob")
    assert isinstance(result) == str
    assert "bob" in result
