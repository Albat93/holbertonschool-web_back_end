#!/usr/bin/env python3
"""Module that provides a simple pagination helper function."""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate start and end indexes for pagination.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index and the end index.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
