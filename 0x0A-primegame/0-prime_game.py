#!/usr/bin/python3

def sieve_of_eratosthenes(max_n):
    is_prime = [True] * (max_n + 1)
    p = 2
    while (p * p <= max_n):
        if (is_prime[p]):
            for i in range(p * p, max_n + 1, p):
                is_prime[i] = False
        p += 1
    primes = [p for p in range(2, max_n + 1) if is_prime[p]]
    return primes


def count_primes_upto_n(n, primes):
    count = 0
    for prime in primes:
        if prime <= n:
            count += 1
        else:
            break
    return count


def isWinner(x, nums):
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
