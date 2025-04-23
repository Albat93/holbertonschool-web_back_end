#!/usr/bin/env python3
"""Module that creates and returns an asyncio Task for wait_random."""

import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """Return an asyncio.Task for the wait_random coroutine.

    Args:
        max_delay (int): The maximum delay to use for wait_random.

    Returns:
        asyncio.Task: An asyncio Task that will execute wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
