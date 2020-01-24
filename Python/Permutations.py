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


# replace recursion with stack
def premute_iterative(nums: List[int]) -> List[List[int]]:
    stack = nums
    res = [stack.pop()]
    while len(stack) != 0:
        temp = stack.pop()
        temp_res = []
        for r in res:
            for i in range(len(r) + 1):
                temp_res.append(r[:i] + temp + r[i:])
        res = temp_res

    return res



x = [1, 2, 3]
print(premute_iterative(x))