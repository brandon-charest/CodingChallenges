""" 46. Permutations
Given a collection of distinct integers, return all possible permutations.

Example:
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

from typing import List


def permute_recursive(nums: List[int]) -> List[List[int]]:
    if len(nums) <= 1:
        return [nums]
    res = []
    for i in range(len(nums)):
        temp = nums[i]
        left_over = nums[:i] + nums[i + 1:]
        for p in permute_recursive(left_over):
            res.append([temp] + p)
    return res


x = [1, 2, 3]
print(permute_recursive(x))