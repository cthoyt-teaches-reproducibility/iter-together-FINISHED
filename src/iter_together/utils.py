# -*- coding: utf-8 -*-

"""Utilities for``iter-together``."""

from typing import Iterable, Tuple

__all__ = [
    'iter_together',
]


def iter_together(
    left_path: str,
    right_path: str,
    sep: str = ',',
) -> Iterable[Tuple[str, ...]]:
    """Iterate over two files with the same index.

    - Assumes the left-most column in each file is the same
    - Splats the remaining rows in order so each row is a tuple of strings

    :param left_path: The path to the first file (assumes file is CSV-like)
    :param right_path: The path to the second file (assumes file is CSV-like)
    :param sep: The separator used in the files
    """
    with open(left_path) as left_file, open(right_path) as right_file:
        for left_line, right_line in zip(left_file, right_file):
            left_idx, *left_values = left_line.strip().split(sep)
            right_idx, *right_values = right_line.strip().split(sep)
            yield (left_idx, *left_values, *right_values)
