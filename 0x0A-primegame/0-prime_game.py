#!/usr/bin/python3
"""prime game"""

def isWinner(x, nums):
    if not nums or x < 1:
        return None

    max_num = max(nums)
    sieve = [1] * (max_num + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, int(max_num ** 0.5) + 1):
        if sieve[i] == 1:
            for j in range(i * i, max_num + 1, i):
                sieve[j] = 0
    primes = [i for i in range(max_num + 1) if sieve[i] == 1]

    wins_for_maria = 0
    for num in nums:
        if num in primes:
            wins_for_maria += 1

    if wins_for_maria == 0:
        return "Ben"
    elif wins_for_maria % 2 == 0:
        return "Maria"
    else:
        return "Ben"
