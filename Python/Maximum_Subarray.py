""" 152. Maximum Product Subarray
Given an integer array nums, find the contiguous subarray within an array (containing at least one number)
which has the largest product.

Example 1:
Input: [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Example 2:
Input: [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
"""
from typing import List


def max_product(nums: List[int]) -> int:
    if not nums:
        return 0

    result = nums[0]
    curr_min = nums[0]
    curr_max = nums[0]

    for i in range(1, len(nums)):

        if nums[i] < 0:
            curr_min, curr_max = curr_max, curr_min

        curr_max = max(nums[i], nums[i] * curr_max)
        curr_min = min(nums[i], nums[i] * curr_min)
        result = max(result, curr_max)

    return result


x = [-2, 0, -1]
print(max_product(x))
x = [-2, 3, -4]
print(max_product(x))
x = [-4, -3, -2]  # 12
print(max_product(x))
