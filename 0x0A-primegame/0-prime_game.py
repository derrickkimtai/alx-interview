#!/usr/bin/python3
"""prime game"""

def isWinner(x, nums):
    """prime game"""
    maria_wins = 0
    ben_wins = 0
    for n in nums:
        prime_count = sum([1 for i in range(1, n + 1) if n % i == 0])
        if prime_count == 2:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Ben"
    if maria_wins < ben_wins:
        return "Maria"
    return None
