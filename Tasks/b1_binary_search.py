# Арефьев Дмитрий

from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    if arr:
        first = 0
        last = len(arr) - 1
        while first <= last:
            mid = (first + last) // 2
            if arr[mid] == elem:
                return mid
            elif elem < arr[mid]:
                last = mid - 1
            elif elem > arr[mid]:
                first = mid + 1
        else:
            return None
    return None
