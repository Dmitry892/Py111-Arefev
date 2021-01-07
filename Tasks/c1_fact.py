# Арефьев Дмитрий

def factorial_recursive(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in recursive way
    :param n: int > 0
    :return: factorial of n
    """
    try:
        if n < 0:
            raise ValueError
        elif n == 0:
            return 1
        else:
            return factorial_recursive(n - 1) * n
    except ValueError:
        raise


def factorial_iterative(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in iterative way

    :param n: int > 0
    :return: factorial of n
    """
    try:
        if n < 0:
            raise ValueError
        elif n == 0:
            return 1
        else:
            factorial = 1
            for f in range(n, 0, -1):
                factorial *= f
            return factorial
    except ValueError:
        raise
