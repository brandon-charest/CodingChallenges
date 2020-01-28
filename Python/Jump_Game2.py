""" 45. Jump Game II
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2

Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.

Note:
You can assume that you can always reach the last index.
"""

from typing import List


def jump(nums: List[int]) -> int:
    steps, curr_max, max_so_far = 0, 0, 0
    for i in range(len(nums)):
        if i > curr_max:
            curr_max = max_so_far
            steps += 1
            if curr_max >= len(nums):
                break
        max_so_far = max(max_so_far, nums[i] + i)
    return steps

print(jump([2,3,1,1,4]))