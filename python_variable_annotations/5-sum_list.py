#!/usr/bin/env python3
"""Module that provides a function to sum a list of floats."""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """Return the sum of a list of float numbers.

    Args:
        input_list (List[float]): A list of float numbers.

    Returns:
        float: The total sum of the list.
    """
    return sum(input_list)
