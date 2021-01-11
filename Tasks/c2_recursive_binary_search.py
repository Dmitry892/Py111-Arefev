from typing import Sequence, Optional

arr = [1,2,3,4,5,7,10]

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
        elif elem < arr[mid]:
            return binary_search(elem, arr[:mid])
        elif elem > arr[mid]:
            return binary_search(elem, arr[mid + 1:]) + (mid + 1)
    return None


print(binary_search(5, arr))
