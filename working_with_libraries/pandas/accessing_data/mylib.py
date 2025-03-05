"""Example of a library file.

Library files should only contain function or class definitions, and no
other python code.

This library defines the functions hello_world() and square()

Author: Uli Wortmann
Date: 2021
License: GPL
"""


def hello_world() -> None:
    """Print Hello World."""
    print("Hello World")


def square(n: int | float) -> int | float:
    """Compute the n*n.

    Parameters
    ----------
    n : int | float
        any number

    Returns
    -------
    int | float
        n squared

    """
    return n * n
