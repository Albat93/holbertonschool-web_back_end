#!/usr/bin/env python3
"""Module that provides a function returning tuple from string and a number."""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with a string and the square of a number as a float.

    Args:
        k (str): The string key.
        v (Union[int, float]): A number (int or float).

    Returns:
        Tuple[str, float]: A tuple with the string and the squared number.
    """
    return (k, float(v ** 2))
