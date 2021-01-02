"""
Priority Queue

Queue priorities are from 0 to 10
Арефьев Дмитрий
"""
from typing import Any

_priority = []

def enqueue(elem: Any, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    _priority.append([elem, priority])
    return None


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.

    :return: dequeued element
    """
    if len(_priority):
        value = []
        _priority.sort(key=lambda priority: priority[1])
        for i in _priority:
            value.append(i[0])
        _priority.pop(0)
        while value:
            return value.pop(0)
    return None


def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    if len(_priority):
        return _priority[ind][priority]
    return None


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    _priority.clear()
    return None
