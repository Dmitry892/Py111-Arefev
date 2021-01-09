from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    if elem not in arr:
        return None
    low = 0
    high = len(arr) - 1
    mid = (low + high) // 2
    if arr[mid] == elem:
        return mid
    else:
        if elem < arr[mid]:
            return binary_search(elem, arr[:mid])
        else:
            return binary_search(elem, arr[mid + 1:]) + (mid + 1)
