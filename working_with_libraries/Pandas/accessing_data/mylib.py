""" Example of a library file.

Library files should only contain function or class definitions, and no
other python code.

This library defines the functions hello_world() and square()

Author: Uli Wortmann
Date: 2021
License: GPL
"""
from __future__ import annotations

def hello_world() -> None:
    """This function takes no arguments and prints Hello World"""

    print("Hello World")


def square(n: int | float) -> int | float:
    """This function takes a number n as argument
    and returns n*n
    """
    return n * n
