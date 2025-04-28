#!/usr/bin/env python3
"""Module providing simple pagination functionality."""

import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate start and end indexes for pagination.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the start index and end index.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset.

        Returns:
            List[List]: The dataset without the header row.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return a page of the dataset.

        Args:
            page (int): Page number (1-indexed).
            page_size (int): Number of items per page.

        Returns:
            List[List]: list of dataset rows corresponding requested page.
        """
        assert isinstance(
            page, int) and page > 0, "Page must be a positive integer"
        assert isinstance(
            page_size, int) and page_size > 0, "Page size must be positive int"

        dataset = self.dataset()
        start, end = index_range(page, page_size)

        return dataset[start:end]
