# Арефьев Дмитрий

from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    if elem in arr or not arr:
        first = 0
        last = len(arr) - 1
        index = -1
        while first <= last and index == -1:
            mid = (first + last) // 2
            if arr[mid] == elem:
                index = mid
            else:
                if elem < arr[mid]:
                    last = mid - 1
                else:
                    first = mid + 1
        return index
    return None
