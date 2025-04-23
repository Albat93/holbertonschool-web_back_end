#!/usr/bin/env python3
"""Module that provides a function to sum a list of ints and floats."""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a list of integers and floats as a float.

    Args:
        mxd_lst (List[Union[int, float]]): The list of numbers to sum.

    Returns:
        float: The total sum of the list.
    """
    return sum(mxd_lst)
