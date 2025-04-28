#!/usr/bin/env python3
"""Module that provides a simple pagination helper function."""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns:
        Tuple[int, int]: A tuple containing the start index and the end index.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
