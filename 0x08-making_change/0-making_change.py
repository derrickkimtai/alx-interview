#!/usr/bin/python3

def makeChange(coins, total):
    """Given a pile """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    count = 0
    for coin in coins:
        count += total // coin
        total %= coin
    if total > 0:
        return -1
    return count
