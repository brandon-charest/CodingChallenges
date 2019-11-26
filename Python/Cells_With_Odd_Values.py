""" 1252. Cells with Odd Values in a Matrix
Given n and m which are the dimensions of a matrix initialized by zeros and given an array indices where
indices[i] = [ri, ci]. For each pair of [ri, ci] you have to increment all cells in row ri and column ci by 1.

Return the number of cells with odd values in the matrix after applying the increment to all indices.

Example 1:
0 0 0   1 2 1   1 3 1
0 0 0   0 1 0   1 3 1

Input: n = 2, m = 3, indices = [[0,1],[1,1]]
Output: 6
Explanation: Initial matrix = [[0,0,0],[0,0,0]].
After applying first increment it becomes [[1,2,1],[0,1,0]].
The final matrix will be [[1,3,1],[1,3,1]] which contains 6 odd numbers.

Example 2:
0 0     0 1     2 2
0 0     1 2     2 2

Input: n = 2, m = 2, indices = [[1,1],[0,0]]
Output: 0
Explanation: Final matrix = [[2,2],[2,2]]. There is no odd number in the final matrix.
"""

from typing import List
import numpy as np


def print_matrix(mat):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in mat]))

"""Brute force"""
def odd_cells(n: int, m: int, indices: List[List[int]]) -> int:
    matrix = [[0 for _ in range(m)] for _ in range(n)]
    odds = 0
    for row, col in indices:
        for x in range(0, m):
            matrix[row][x] += 1
            if matrix[row][x] % 2 == 0:
                odds -= 1
            else:
                odds += 1
        for y in range(0, n):
            matrix[y][col] += 1
            if matrix[y][col] % 2 == 0:
                odds -= 1
            else:
                odds += 1
    print_matrix(matrix)
    return odds


"""Numpy version for fun"""
def odd_cells_np(n: int, m: int, indices: List[List[int]]) -> int:
    matrix = np.zeros(shape=(n, m), dtype=int)
    for row, col in indices:
        matrix[row, :] += 1
        matrix[:, col] += 1
    print(matrix)
    return np.count_nonzero(matrix % 2 == 1)

x = set()
x.

print(odd_cells(2,3,[[0,1], [1,1]]))
print(odd_cells(2,2,[[0,0], [1,1]]))

print(odd_cells_np(2,3,[[0,1], [1,1]]))