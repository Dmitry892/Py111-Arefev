from typing import List


def sort(container: List[int]) -> List[int]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    for i in range(len(container)):
        for j in range(len(container) - 1):
            if container[i] < container[j]:
                container[i], container[j] = container[j], container[i]
    return container
