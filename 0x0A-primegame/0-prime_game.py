#!/usr/bin/python3
"""
Prime Game
"""


def isWinner(x, nums):
    """
    determine who the winner of each game is.
    """
    maria_wins = 0
    ben_wins = 0

    for num in nums:
        prime_count = sum(1 for i in range(2, num + 1)
                          if all(i % j != 0 for j in range(2, int(i ** 0.5) + 1)))

        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif maria_wins < ben_wins:
        return 'Ben'
    else:
        return None
