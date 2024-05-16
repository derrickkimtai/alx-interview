#!/usr/bin/python3
"""prime game"""

def isWinner(x, nums):
    """prime game"""
    if not nums or x < 1:
        return None
    n = max(nums)
    sieve = [True for _ in range(max(n + 1, 2))]
    sieve[0:2] = [False, False]
    for i in range(2, int(n ** 0.5) + 1):
        if not sieve[i]:
            continue
        for j in range(i * i, n + 1, i):
            sieve[j] = False
    sieve = [i for i, j in enumerate(sieve) if j]
    m = len(sieve)
    scores = {1: 0, 2: 1}
    for i in range(3, n + 1):
        scores[i] = 0
        for j in range(m):
            if sieve[j] > i:
                break
            if i % sieve[j] == 0 and scores[i - sieve[j]] == 0:
                scores[i] = 1
                break
    player1 = 0
    for i in nums:
        player1 += scores[i]
    if player1 * 2 == len(nums):
        return None
    if player1 * 2 < len(nums):
        return "Ben"
    return "Maria"