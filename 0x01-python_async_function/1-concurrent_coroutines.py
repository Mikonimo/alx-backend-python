#!/usr/bin/env python3
"""This module contains an async function"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns the list of all the delays"""
    vals = [wait_random(max_delay) for _ in range(n)]
    vals = asyncio.as_completed(vals)
    delays = [await val for val in vals]
    return delays
