""" 47. Permutations II
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:
Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

from typing import List


def permute(nums):
    if len(nums) <= 1:
        return [nums]
    res = []
    for i in range(len(nums)):
        temp = nums[i]
        left_over = nums[:i] + nums[i + 1:]
        for p in permute(left_over):
            res.append([temp] + p)
    return res


def permute_unique(nums: List[int]) -> List[List[int]]:
    return [list(x) for x in set(tuple(x) for x in permute(nums))]

x = [1, 1, 3]
print(permute_unique(x))