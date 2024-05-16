#!/usr/bin/python3
"""Prime Game"""

def isWinner(x, nums):
  """Prime Game"""
  maria_wins = ben_wins = 0
  for _ in range(x):
    n = len(nums)
    if n % 2 == 0:
      ben_wins += 1
    else:
      if n > 1:
        # Calculate prime count for n (replace with your logic from your code)
        prime_count = sum(1 for i in range(2, n + 1)
                          if all(i % j != 0 for j in range(2, int(i ** 0.5) + 1)))
        if prime_count % 2 == 0:
          ben_wins += 1
        else:
          maria_wins += 1
      else:
        ben_wins += 1
    nums = []
  if maria_wins > ben_wins:
    return "Maria"
  elif ben_wins > maria_wins:
    return "Ben"
  else:
    return None
