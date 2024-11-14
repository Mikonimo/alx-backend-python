#!/usr/bin/env python3
"""This module contains an async function"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for wait_n function"""
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time: float = time.perf_counter() - start_time

    return total_time / n
