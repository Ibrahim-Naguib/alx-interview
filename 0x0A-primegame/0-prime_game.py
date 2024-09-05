#!/usr/bin/python3
"""Prime Game"""


def sieve_of_eratosthenes(max_n):
    """
    Generate a list of prime numbers up to max_n.

    Args:
    max_n (int): The upper limit for generating prime numbers.

    Returns:
    List[int]: A list of prime numbers up to max_n.
    """
    is_prime = [True] * (max_n + 1)
    p = 2
    while (p * p <= max_n):
        if (is_prime[p] is True):
            for i in range(p * p, max_n + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(2, max_n + 1) if is_prime[p]]
    return primes


def count_primes_upto_n(n, primes):
    """
    Count the number of prime numbers less than or equal to n.

    Args:
    n (int): The upper limit to count primes.
    primes (List[int]): The list of precomputed prime numbers.

    Returns:
    int: The count of prime numbers up to n.
    """
    count = 0
    for prime in primes:
        if prime <= n:
            count += 1
        else:
            break
    return count


def isWinner(x, nums):
    """
    Determine the winner of the prime number game after x rounds.

    Args:
    x (int): The number of rounds.
    nums: A list of integers representing the upper limit for each round.

    Returns:
    str or None: The name of the player with the most wins ('Maria' or 'Ben').
                 If the game is a tie, return None.
    """
    max_n = max(nums)
    primes = sieve_of_eratosthenes(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        prime_count = count_primes_upto_n(n, primes)
        # If prime_count is odd, Maria wins. If even, Ben wins.
        if prime_count % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
