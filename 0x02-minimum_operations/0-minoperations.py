#!/usr/bin/python3

def minOperations(n):
    if n < 2:
        return 0
    if n % 2 == 0:
        return minOperations(n // 2) + 2
    for i in range(3, n + 1, 2):
        if n % i == 0:
            return minOperations(n // i) + i
    return n