#!/usr/bin/python3

import sys

def is_safe(board, row, col, N):
    for i in range(row):
        if board[i] == col or \
            board[i] - i == col - row or \
            board[i] + i == col + row:
            return False
    return True

def solve_nqueens(N):
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    def solve(board, row, N, result):
        if row == N:
            result.append(board[:])
            return
        for col in range(N):
            if is_safe(board, row, col, N):
                board[row] = col
                solve(board, row + 1, N, result)

    result = []
    solve([-1] * N, 0, N, result)
    for solution in result:
        print(' '.join(str(col + 1) for col in solution))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    solve_nqueens(sys.argv[1])
