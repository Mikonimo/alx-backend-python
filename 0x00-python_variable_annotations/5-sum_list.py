#!/usr/bin/env python3
"""Type-annotated function sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Takes a list of floats and returns their sum as float"""
    result: float = 0.0
    for i in input_list:
        result += i
    return result
