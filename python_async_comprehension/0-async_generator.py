#!/usr/bin/env python3
"""Module for asynchronous generator task."""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Coroutine that asynchronously yields random floats between 0 and 10.

    It loops 10 times, waiting 1 second between each yield.
    Yields:
        float: A random float between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
    # The function is an asynchronous generator that yields random floats
    # between 0 and 10, waiting 1 second between each yield.
