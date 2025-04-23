#!/usr/bin/env python3
"""Module that provides a function which returns a multiplier function."""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by the given multiplier.

    Args:
        multiplier (float): The number to multiply by.

    Returns:
        Callable[[float], float]: A function that takes a float and returns
        the result of multiplying it by the multiplier.
    """
    def multiply(n: float) -> float:
        return n * multiplier

    return multiply
