from typing import Sequence, Optional


def binary_search(elem: int, arr: Sequence) -> Optional[int]:
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    low = 0
    high = len(arr) - 1
    mid = (low + high) // 2

    if arr:
        if arr[mid] == elem:
            return mid
        else:
            if elem < arr[mid]:
                return binary_search(elem, arr[:mid])
            else:
                search = binary_search(elem, arr[mid + 1:])
                return (mid + 1) + search if search is not None else None
    return None
