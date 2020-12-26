"""
This module implements some functions based on linear search algo
"""
from typing import Sequence


def min_search(arr: Sequence) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    if not arr:
        return -1

    min_index = 0
    minimum = arr[min_index]
    for index, elem in enumerate(arr):
        if elem < minimum:  # не используйте функцию min. Она вам не нужна
            minimum = elem
            min_index = index
    return min_index
