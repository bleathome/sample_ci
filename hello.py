"""
This module provides a simple greeting functionality.
It contains a `say_hello` function that generates a personalized greeting
message by incorporating the given name into the greeting.
"""
def say_hello(name):
    """
    Generate a greeting string for the given name.
    Parameters:
    - name (str): The name to include in the greeting.
    Returns:
    - str: A greeting string that says "Hello" followed by the given name.
    """
    return f"Hello {name}"
