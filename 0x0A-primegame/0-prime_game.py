#!/usr/bin/python3
"""Prime Game"""
def isWinner(x, nums):
    """Prime Game"""
    if not nums or x < 1:
        return None
    n = max(nums)
    sieve = [1] * (n + 1)
    sieve[0] = sieve[1] = 0
    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i] == 1:
            for j in range(i * i, n + 1, i):
                sieve[j] = 0
    sieve = [i for i in range(n + 1) if sieve[i] == 1]
    m = len(sieve)
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1]
        for j in range(m):
            if sieve[j] > i:
                break
            if not dp[i - sieve[j]]:
                dp[i] = 1
                break
    p1 = 0
    for i in nums:
        p1 += dp[i]
    if p1 * 2 == len(nums):
        return None
    if p1 * 2 < len(nums):
        return "Ben"
    return "Maria"
