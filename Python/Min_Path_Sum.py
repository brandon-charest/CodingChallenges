""" 64. Minimum Path Sum
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum
of all numbers along its path.

Note: You can only move either down or right at any point in time.
Example:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

from typing import List


def print_matrix(mat):
    print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in mat]))


def minPathSum(grid: List[List[int]]) -> int:
    if grid is None or len(grid) is 0:
        return 0
    dp = grid
    for j in range(len(dp)):
        for i in range(len(dp[j])):
            if i is 0 and j is 0:
                continue
            elif i is 0:
                dp[j][0] += dp[j-1][0]
            elif j is 0:
                dp[0][i] += dp[0][i-1]
            else:
                dp[j][i] += min(dp[j - 1][i], dp[j][i - 1])
    print_matrix(dp)
    return dp[-1][-1]


path = [
  [1, 3, 1],
  [1, 5, 1],
  [4, 2, 1]
]

res = minPathSum(grid=path)
print(res)
