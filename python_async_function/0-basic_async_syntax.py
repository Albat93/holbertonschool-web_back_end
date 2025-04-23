#!/usr/bin/env python3
"""Async function that waits for a random delay and returns it."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay between 0 and max_delay (float included).

    Args:
        max_delay (int): Maximum delay value.

    Returns:
        float: The actual delay used.
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
