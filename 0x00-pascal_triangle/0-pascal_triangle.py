#!/usr/bin/python3

def pascal_triangle(n):
    """
     Generate Pascal's triangle up to 'n' rows.

    Args:
    - n (int): Number of rows for Pascal's triangle.

    Returns:
    - list of lists: Pascal's triangle represented as a list of lists.
    """
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
