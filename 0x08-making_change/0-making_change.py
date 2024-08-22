#!/usr/bin/python3
"""Change comes from within"""


def makeChange(coins, total):
    """Return: fewest number of coins needed to meet total"""
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        if total == 0:
            break
        count += total // coin
        total %= coin
    return count if total == 0 else -1
