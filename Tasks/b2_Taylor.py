"""
Taylor series
"""
from typing import Union


def factorial(fac: int) -> int:
    factorial_ = 1
    for f in range(fac, 0, -1):
        factorial_ *= f
    return factorial_


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    delta = 0.0001
    exp = 0
    for n in range(10000000):
        value = x ** n / factorial(n)
        if value <= delta:
            return exp
        else:
            exp += value


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    delta = 0.0001
    current_value = 0
    for n in range(10000000):
        current_value += (-1) ** n * (x ** (2 * n + 1)) / factorial(2 * n + 1)
        next_value = (-1) ** (n + 1) * (x ** (2 * (n + 1) + 1)) / factorial(2 * (n + 1) + 1)
        next_value += current_value
        if abs(current_value - next_value) <= delta:
            return current_value
