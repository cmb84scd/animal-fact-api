"""A docstring."""

import math
from collections.abc import Iterable


def some_numbers(num: Iterable[int]) -> int:
    """Return the power of, of each num in the list."""
    for n in num:
        return math.pow(n, 2)


def some_string(name: str) -> str:
    """Return a greeting to someone."""
    return "hello " + name


def some_func(word: str) -> str:
    """Return capitalised word."""
    return word.capitalize
