#!/usr/bin/env python3
"""Module that provides a function returning elements and their lengths."""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Return a list of tuples with elements and their lengths.

    Args:
        lst (Iterable[Sequence]): An iterable of sequence-like elements.

    Returns:
        List[Tuple[Sequence, int]]: A list of tuples where each tuple contains
        an element and its length.
    """
    return [(i, len(i)) for i in lst]
