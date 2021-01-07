# Арефьев Дмитрий

def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    try:
        if n < 0:
            raise ValueError
        elif n == 0:
            return 0
        else:
            if n in (1, 2):
                return 1
            return fib_recursive(n - 1) + fib_recursive(n - 2)
    except ValueError:
        raise


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    try:
        if n < 0:
            raise ValueError
        elif n == 0:
            return 0
        else:
            fib = fib2 = 1
            for i in range(2, n):
                fib, fib2 = fib2, fib + fib2
            return fib2
    except ValueError:
        raise
