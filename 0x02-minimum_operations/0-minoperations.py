#!/usr/bin/python3
"""Minimum Operations """


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result in
    exactly n 'H' characters in a text file, starting from
    a single 'H', using only theoperations "Copy All" and "Paste".

    Args:
    n (int): The target number of 'H' characters.

    Returns:
    int: The minimum number of operations required to achieve n 'H'
    characters, or 0 if n is impossible.
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
